import os
import sys
import logging
path = r"E:\GithubKu\MAICA_Server_Submod\game\Submods\MAICA_ServerSubmod\Register.exe"
logger=None
def register_user(username, email, password, db_path=None):
    global logger
    if logger is None:
        logger = logging.getLogger(__name__)
    """
    Register a user by calling the Register.exe with provided credentials.
    
    :param username: User's username
    :param email: User's email address
    :param password: User's password
    :param db_path: Optional database path (default: None)
    :return: True if registration successful, False otherwise
    """
    # Construct the command arguments
    cmd = [
        path,
        "--username", username,
        "--email", email,
        "--password", password
    ]
    
    # Add optional database path if provided

    
    try:
        # Construct command string with proper escaping
        cmd_str = "{} --username \"{}\" --email \"{}\" --password \"{}\" ".format(path, username, email, password) + "--db \"{}\"".format(db_path) if db_path else ""
        logger.info("Executing Register.exe with args: {}".format(cmd_str))
        # Use os.system to execute the command
        result = os.system(cmd_str)
        
        # Check the return code (0 means success in os.system)
        if result == 0:
            logger.info("User registration successful")
            return True
        else:
            logger.error("Registration failed. Return code: {}".format(result))
            return False
    
    except Exception as e:
        logger.error("Error executing Register.exe: {}".format(e))
        return False

# Example usage
if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Example of how to use the function
    result = register_user(
        username="testuser", 
        email="test@example.com", 
        password="securepassword123"
    )
    sys.exit(0 if result else 1)