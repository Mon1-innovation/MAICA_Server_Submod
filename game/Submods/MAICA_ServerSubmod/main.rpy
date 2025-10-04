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
        maicasv.set_env('MAICA_CURR_VERSION', '1.1.003')
        maicasv.set_env('MAICA_MCORE_ADDR', mas_getAPIKey("maica_core_url") or '')
        maicasv.set_env('MAICA_MCORE_KEY', mas_getAPIKey("maica_core_key") or '')
        maicasv.set_env('MAICA_MCORE_CHOICE', mas_getAPIKey("maica_core_model") or '')

        # MFocus URL and key from registered API keys
        maicasv.set_env('MAICA_MFOCUS_ADDR', mas_getAPIKey("maica_mfocus_url") or '')
        maicasv.set_env('MAICA_MFOCUS_KEY', mas_getAPIKey("maica_mfocus_key") or '')
        maicasv.set_env('MAICA_MFOCUS_CHOICE', mas_getAPIKey("maica_mfocus_model") or '')

        # Other service keys from registered API keys
        #maicasv.set_env('MAICA_MVISTA_ADDR', '')
        #maicasv.set_env('MAICA_MVISTA_KEY', 'EMPTY')
        #maicasv.set_env('MAICA_MVISTA_CHOICE', '')

        # Proxy address from registered API keys
        maicasv.set_env('MAICA_PROXY_ADDR', mas_getAPIKey("maica_proxy_addr") or '')
        #SESSION_MAX_TOKEN = '28672'
        maicasv.set_env('MAICA_SESSION_MAX_TOKEN', '28672')
        # Database and other configuration settings
        maicasv.set_env('MAICA_DB_ADDR', 'sqlite')
        maicasv.set_env('MAICA_DB_USER', 'user')
        maicasv.set_env('MAICA_DB_PASSWORD', '123456')
        maicasv.set_env('MAICA_AUTH_DB', 'forum_flarum_db.db')
        maicasv.set_env('MAICA_DATA_DB', 'maica.db')

        # Weather key from registered API keys
        maicasv.set_env('MAICA_WEATHER_KEY', mas_getAPIKey("maica_gaode_key") or '')

        # Connection and performance settings
        maicasv.set_env('MAICA_KICK_STALE_CONNS', '1')
        maicasv.set_env('MAICA_F2B_COUNT', '20')
        maicasv.set_env('MAICA_F2B_TIME', '600')
        maicasv.set_env('MAICA_FULL_RESTFUL', '1')
        maicasv.set_env('MAICA_ROTATE_MSCACHE', '0')
        maicasv.set_env('MAICA_PRINT_VERBOSE', '1')

        # Developer and system info
        maicasv.set_env('MAICA_DEV_IDENTITY', 'Evan & Clifford')
        maicasv.set_env('MAICA_DEV_STATUS', 'serving')
        maicasv.set_env('MAICA_VERSION_CONTROL', '1.1.000')
        maicasv.set_env('MAICA_SESSION_MAX_TOKEN', '28672')
        maicasv.set_env('MAICA_MCORE_NODE', 'HGX690-nuclear-edition')
        maicasv.set_env('MAICA_MFOCUS_NODE', 'HGX610-biohazard-edition')
        maicasv.set_env('MAICA_ALT_TOOLCALL', '1')
        maicasv.set_env('MAICA_IS_REAL_ENV', '1')

        MAICA_MCORE_EXTRA = """\
    {
        "extra_body": {
            "repetition_penalty": 1.0,
            "length_penalty": 1.0
        }
    }"""
        maicasv.set_env('MAICA_MCORE_EXTRA', MAICA_MCORE_EXTRA)

        MAICA_MFOCUS_EXTRA = """\
        {
            "temperature": 0.2,
            "seed": 42,
            "extra_body": {
                "repetition_penalty": 1.05,
                "length_penalty": 1.1
            }
        }"""
        maicasv.set_env('MAICA_MFOCUS_EXTRA', MAICA_MFOCUS_EXTRA)

        MAICA_SERVERS_LIST = """\
            {
                "isMaicaNameServer": true,
                "servers": [
                    {"id": 0, "name": "Local MAICA Instance", "description": "Used for conveniently connecting to a local deployed MAICA instance", "isOfficial": true, "portalPage":"http://127.0.0.1", "servingModel": "UNKNOWN", "modelLink": "UNKNOWN", "wsInterface": "ws://127.0.0.1:5000", "httpInterface": "http://127.0.0.1:6000", "isFullRestful": true}
                ]
            }
        """
        maicasv.set_env('MAICA_SERVERS_LIST', MAICA_SERVERS_LIST)
        store.mas_submod_utils.getAndRunFunctions("maica_update_key")

init 500 python:
    if persistent.maica_sv_autostart:
        maica_update_key()
        maicasv.start_server()