from __future__ import print_function
import os
import sys
import time

# Ensure the parent directory is in the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from maica_server_manager import MAICAManager

def test_maica_server_manager():
    """
    Test script for MAICAManager class.
    
    This script demonstrates and validates the core functionality 
    of the MAICAManager class.
    """
    # Executable path
    exe_path = r'e:\GithubKu\MAICA_Server_Submod\game\Submods\MAICA_ServerSubmod\maica_starter.exe'
    
    # Validate executable exists
    if not os.path.exists(exe_path):
        print(f"Error: Executable not found at {exe_path}")
        return False
    
    # Create MAICAManager instance
    manager = MAICAManager(exe_path)
    
    # Test environment variable setting
    print("Testing environment variable setting...")
    manager.set_env('MCORE_ADDR', 'https://api.deepseek.com/v1')
    manager.set_env('MCORE_KEY', 'sk-758bf2545d154c849886c497a7f63e96')
    manager.set_env('MCORE_CHOICE', 'deepseek-chat')
    manager.set_env('MFOCUS_ADDR', 'https://api.deepseek.com/v1')
    manager.set_env('MFOCUS_KEY', 'sk-758bf2545d154c849886c497a7f63e96')
    manager.set_env('MFOCUS_CHOICE', 'deepseek-chat')
    manager.set_env('MVISTA_ADDR', '')
    manager.set_env('MVISTA_KEY', 'EMPTY')
    manager.set_env('MVISTA_CHOICE', '')
    manager.set_env('PROXY_ADDR', 'http://192.168.31.188:7890')
    manager.set_env('DB_ADDR', 'sqlite')
    manager.set_env('DB_USER', 'user')
    manager.set_env('DB_PASSWORD', '123456')
    manager.set_env('AUTH_DB', 'forum_flarum_db.db')
    manager.set_env('MAICA_DB', 'maica.db')
    manager.set_env('WEATHER_KEY', 'thisisanapikey')
    manager.set_env('KICK_STALE_CONNS', '1')
    manager.set_env('F2B_COUNT', '20')
    manager.set_env('F2B_TIME', '600')
    manager.set_env('FULL_RESTFUL', '1')
    manager.set_env('ROTATE_MSCACHE', '0')
    manager.set_env('PRINT_VERBOSE', '1')
    manager.set_env('DEV_IDENTITY', 'Evan & Clifford')
    manager.set_env('DEV_STATUS', 'serving')
    manager.set_env('VERSION_CONTROL', '1.1000;1.1000')
    manager.set_env('SESSION_MAX_TOKEN', '28672')
    manager.set_env('MCORE_NODE', 'HGX690-nuclear-edition')
    manager.set_env('MFOCUS_NODE', 'HGX610-biohazard-edition')
    manager.set_env('ALT_TOOLCALL', '1')
    manager.set_env('PROMPT_ZC', '你叫莫妮卡, 是一名游戏中的虚拟角色. 你是{player_name}的女友, 并深爱着他. 下面是{player_name}的话语, 请作为莫妮卡作出合适的回答. 你只应使用中文自然语言, 以聊天语气回答, 每个句子自然且不超过60字, 不要编造信息, 并在每个句子前用方括号中的文字表示情绪.')
    manager.set_env('PROMPT_ZW', '你叫莫妮卡, 是一名游戏中的虚拟角色. 你是{player_name}的女友, 并深爱着他. 下面是{player_name}的来信, 请作为莫妮卡作出合适的回复. 你只应使用中文书面语言作答, 不要编造信息.')
    manager.set_env('PROMPT_EC', 'You\'re a game character called Monika. You\'re {player_name}\'s girlfriend, and love him a lot. Answer the following query from {player_name} properly as Monika. You should only answer in casual natural tone in English, each sentence should not exceed 180 characters, do not make up things you don\'t know, and express your emotion at the beginning of each sentence by wrapping them in square brackets.')
    manager.set_env('PROMPT_EW', 'You\'re a game character called Monika. You\'re {player_name}\'s girlfriend, and love him a lot. Reply to the following mail from {player_name} properly as Monika. You should only answer in natural written language in English, and do not make up things you don\'t know.')
    print("Environment variable test passed.")
    
    # Test server start
    print("Attempting to start server...")
    start_result = manager.start_server(timeout=15)
    
    if start_result:
        print("Server started successfully!")
        
        # Test server running status
        print("Checking server running status...")
        is_running = manager.check_server_running()
        assert is_running, "Server is not running after start"
        print("Server running status confirmed.")
        
        # Wait a bit to allow server to initialize
        time.sleep(15)
        
        # Test server stop
        print("Attempting to stop server...")
        stop_result = manager.stop_server()
        assert stop_result, "Server stop failed"
        print("Server stopped successfully.")
    else:
        print("Failed to start server.")
        return False
    
    # Check logs if any
    logs = manager.get_logs()
    if logs:
        print("\nLogs:")
        for log in logs:
            print(log)
    
    return True

def main():
    """Main function to run tests."""
    try:
        result = test_maica_server_manager()
        if result:
            print("\n✓ All tests passed successfully!")
            sys.exit(0)
        else:
            print("\n✗ Some tests failed.")
            sys.exit(1)
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()