init -5 python:
    import maica_server_manager
    maicasv = maica_server_manager.MAICAManager(os.path.join(renpy.config.basedir, "game", "Submods", "MAICA_ServerSubmod", "maica_starter.exe"))
    maicasv.logger = store.mas_submod_utils.submod_log

    @store.mas_submod_utils.functionplugin("_quit", )
    def clear_maica_sv():
        maicasv.stop_server()

    def change_maica_core_url(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_core_url",
        renpy.substitute(_("MAICA Server 核心服务商url")),
        on_change=change_maica_core_url
    )

    def change_api(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_core_key",
        renpy.substitute(_("MAICA Server 核心服务商api key")),
        on_change=change_maica_core_url
    )

    def change_maica_core_url(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_core_model",
        renpy.substitute(_("MAICA Server 核心模型名称")),
        on_change=change_maica_core_url
    )

    def change_maica_mfocus_url(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_mfocus_url",
        renpy.substitute(_("MAICA Server MFocus服务商url")),
        on_change=change_maica_mfocus_url
    )

    def change_maica_mfocus_key(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_mfocus_key",
        renpy.substitute(_("MAICA Server MFocus服务商api key")),
        on_change=change_maica_mfocus_key
    )    

    def change_maica_mfocus_model(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_mfocus_model",
        renpy.substitute(_("MAICA Server MFocus模型名称")),
        on_change=change_maica_mfocus_model
    )

    def change_maica_proxy_addr(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_proxy_addr",
        renpy.substitute(_("MAICA Server 搜索引擎代理地址")),
        on_change=change_maica_proxy_addr
    )

    def change_maica_gaode_key(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_gaode_key",
        renpy.substitute(_("MAICA Server 高德天气KEY")),
        on_change=change_maica_gaode_key
    )
    def maica_update_key():
        # Core URL and key from registered API keys
        maicasv.set_env('MCORE_ADDR', mas_getAPIKey("maica_core_url") or '')
        maicasv.set_env('MCORE_KEY', mas_getAPIKey("maica_core_key") or '')
        maicasv.set_env('MCORE_CHOICE', mas_getAPIKey("maica_core_model") or '')
        
        # MFocus URL and key from registered API keys
        maicasv.set_env('MFOCUS_ADDR', mas_getAPIKey("maica_mfocus_url") or '')
        maicasv.set_env('MFOCUS_KEY', mas_getAPIKey("maica_mfocus_key") or '')
        maicasv.set_env('MFOCUS_CHOICE', mas_getAPIKey("maica_mfocus_model") or '')
        
        # Other service keys from registered API keys
        #maicasv.set_env('MVISTA_ADDR', '')
        #maicasv.set_env('MVISTA_KEY', 'EMPTY')
        #maicasv.set_env('MVISTA_CHOICE', '')
        
        # Proxy address from registered API keys
        maicasv.set_env('PROXY_ADDR', mas_getAPIKey("maica_proxy_addr") or '')
        
        # Database and other configuration settings
        maicasv.set_env('DB_ADDR', 'sqlite')
        maicasv.set_env('DB_USER', 'user')
        maicasv.set_env('DB_PASSWORD', '123456')
        maicasv.set_env('AUTH_DB', 'forum_flarum_db.db')
        maicasv.set_env('MAICA_DB', 'maica.db')
        
        # Weather key from registered API keys
        maicasv.set_env('WEATHER_KEY', mas_getAPIKey("maica_gaode_key") or '')
        
        # Connection and performance settings
        maicasv.set_env('KICK_STALE_CONNS', '1')
        maicasv.set_env('F2B_COUNT', '20')
        maicasv.set_env('F2B_TIME', '600')
        maicasv.set_env('FULL_RESTFUL', '1')
        maicasv.set_env('ROTATE_MSCACHE', '0')
        maicasv.set_env('PRINT_VERBOSE', '1')
        
        # Developer and system info
        maicasv.set_env('DEV_IDENTITY', 'Evan & Clifford')
        maicasv.set_env('DEV_STATUS', 'serving')
        maicasv.set_env('VERSION_CONTROL', '1.1000;1.1000')
        maicasv.set_env('SESSION_MAX_TOKEN', '28672')
        maicasv.set_env('MCORE_NODE', 'HGX690-nuclear-edition')
        maicasv.set_env('MFOCUS_NODE', 'HGX610-biohazard-edition')
        maicasv.set_env('ALT_TOOLCALL', '1')
        
        store.mas_submod_utils.getAndRunFunctions("maica_update_key")
    
init 500 python:
    if persistent.maica_sv_autostart:
        maica_update_key()
        maicasv.start_server()