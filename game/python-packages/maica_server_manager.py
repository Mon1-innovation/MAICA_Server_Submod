from __future__ import print_function
import os
import os.path
import sys
import subprocess

# Version compatibility imports
try:
    # Python 3
    from typing import Optional, Dict, Any
except ImportError:
    # Python 2 fallback
    Optional = Dict = Any = None

try:
    # Python 3
    import logging
    import psutil
    import time
except ImportError:
    # Python 2 compatibility
    logging = None
    psutil = None
    time = None

class MAICAManager(object):
    def __init__(self, exe_path):
        """Initialize the MAICA Server Manager."""
        self.exe_path = exe_path

        # Basic logging fallback
        self._log_messages = []
        
        # Logging setup with version compatibility
        if logging:
            try:
                logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s'
                )
                self.logger = logging.getLogger(__name__)
            except Exception:
                self.logger = None
        
        # Environment variables store
        self._env_vars = {}
    
    def __del__(self):
        """Automatically stop server when MAICAManager is deleted."""
        try:
            self.stop_server()
        except Exception:
            pass  # Suppress any errors during deletion

    def set_env(self, key, variable):
        """Set an environment variable."""
        try:
            self._env_vars[key] = str(variable)
            if self.logger:
                self.logger.info('Environment variable set: %s', key)
            else:
                self._log_messages.append('Environment variable set: ' + key)
        except Exception as e:
            error_msg = 'Error setting environment variable {}: {}'.format(key, e)
            if self.logger:
                self.logger.error(error_msg)
            else:
                self._log_messages.append(error_msg)
    
    def get_env(self, key):
        """Retrieve an environment variable."""
        return self._env_vars.get(key) or os.environ.get(key)
    
    def del_env(self, key):
        """Remove an environment variable."""
        try:
            # Remove from class-level tracking
            if key in self._env_vars:
                del self._env_vars[key]
            
            # Remove from os.environ if present
            if key in os.environ:
                del os.environ[key]
            
            # Log the deletion
            if self.logger:
                self.logger.info('Environment variable deleted: %s', key)
            else:
                self._log_messages.append('Environment variable deleted: ' + key)
            
            return True
        except Exception as e:
            error_msg = 'Error deleting environment variable {}: {}'.format(key, e)
            if self.logger:
                self.logger.error(error_msg)
            else:
                self._log_messages.append(error_msg)
            return False
    
    def start_server(self, timeout=10):
        """Start the server with error handling."""
        try:
            # Prepare environment 
            for key, value in self._env_vars.items():
                os.environ[key] = str(value)

            self._log_info('Environment Variables:')
            for key, value in self._env_vars.items():
                self._log_info('{0}: {1} (type: {2})'.format(key, value, type(value).__name__))

            # Create .env file in the same directory as executable
            exe_dir = os.path.dirname(self.exe_path)
            env_path = os.path.join(exe_dir, '.env')
            
            try:
                with open(env_path, 'w', encoding="utf-8") as env_file:
                    for key, value in self._env_vars.items():
                        # Ensure value is a string and wrap in quotes
                        quoted_value = '"{}"'.format(str(value).replace('"', '\\"'))
                        env_file.write('{}={}\n'.format(key, quoted_value))
                self._log_info('Created .env file at {}'.format(env_path))
            except Exception as e:
                self._log_error('Error creating .env file: {}'.format(e))

            # Start the process using os.startfile()
            os.startfile(self.exe_path)
            
            # Basic wait and check for Python 2/3
            if time and psutil:
                start_time = time.time()
                while time.time() - start_time < timeout:
                    if self.check_server_running():
                        self._log_info('Server started successfully')
                        return True
                    
                    time.sleep(0.5)
                
                self._log_warning('Server start timeout reached')
                return False
            else:
                # Fallback for environments without time/psutil
                self._log_info('Server started')
                return True
        
        except Exception as e:
            import traceback
            self._log_error('Error starting server: {}'.format(traceback.format_exc()))
            
            return False
    
    def _check_port_in_use(self, port):
        """Check if a specific port is in use."""
        if psutil:
            try:
                for conn in psutil.net_connections():
                    if conn.status == 'LISTEN' and conn.laddr.port == port:
                        return True
                return False
            except Exception as e:
                self._log_error('Error checking port {}: {}'.format(port, e))
                return False
        return False

    def stop_server(self):
        """Stop the server gracefully."""
        self._log_info("taskkill /f /im " + os.path.basename(self.exe_path))
        if os.system("taskkill /f /im " + os.path.basename(self.exe_path)):
            return True

        if psutil:
            try:
                ports_to_check = [5000, 6000]
                stopped_ports = []
                
                # Terminate processes using these ports
                for conn in psutil.net_connections():
                    if conn.status == 'LISTEN' and conn.laddr.port in ports_to_check:
                        try:
                            proc = psutil.Process(conn.pid)
                            if os.path.basename(proc.exe()) == os.path.basename(self.exe_path):
                                proc.terminate()
                                proc.wait(timeout=5)
                                stopped_ports.append(conn.laddr.port)
                        except Exception as e:
                            self._log_error('Error terminating process on port {}: {}'.format(conn.laddr.port, e))
                
                if stopped_ports:
                    self._log_info('Server stopped on ports: {}'.format(stopped_ports))
                    return True
                
                # Fallback to process name/exe check
                for proc in psutil.process_iter(['name', 'exe']):
                    if os.path.basename(proc.info.get('exe', '')) == os.path.basename(self.exe_path):
                        proc.terminate()
                        proc.wait(timeout=5)
                        self._log_info('Server stopped successfully')
                        return True
                return False
            except Exception as e:
                self._log_error('Error stopping server: {}'.format(e))
                return False
        else:
            # Fallback for systems without psutil
            self._log_warning('Server stop not supported in this environment')
            return False
    
    
    def check_server_running(self):
        """Check if the server is currently running."""
        if psutil:
            try:
                # Check if either port 5000 or 6000 is in use by the server
                ports_to_check = [5000, 6000]
                for port in ports_to_check:
                    if self._check_port_in_use(port):
                        return True
                
                # Fallback to process check
                for proc in psutil.process_iter(['name', 'exe']):
                    # Additional debugging
                    exe_path = proc.info.get('exe')
                    if exe_path is None:
                        self._log_error('Process info has no exe path: {}'.format(proc.info))
                        continue
                    
                    if os.path.basename(exe_path) == os.path.basename(self.exe_path):
                        return True
                
                return False
            except Exception as e:
                self._log_error('Error checking server status: {}'.format(e))
                import traceback
                self._log_error('Traceback: {}'.format(traceback.format_exc()))
                return False
        else:
            # Fallback for systems without psutil
            #self._log_warning('Server status check not supported')
            return False
    
    def _log_info(self, message):
        """Log info message"""
        if self.logger:
            self.logger.info(message)
        else:
            print(message)
            self._log_messages.append(message)
    
    def _log_error(self, message):
        """Log error message"""
        if self.logger:
            self.logger.error(message)
        else:
            print('ERROR: ' + message, file=sys.stderr)
            self._log_messages.append('ERROR: ' + message)
    
    def _log_warning(self, message):
        """Log warning message"""
        if self.logger:
            self.logger.warning(message)
        else:
            print('WARNING: ' + message, file=sys.stderr)
            self._log_messages.append('WARNING: ' + message)
    
    def get_logs(self):
        """Retrieve log messages."""
        return self._log_messages