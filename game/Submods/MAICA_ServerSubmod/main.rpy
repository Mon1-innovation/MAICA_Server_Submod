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

    def change_maica_tp_apis(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_tp_apis",
        renpy.substitute(_("MAICA Server 第三方API配置")),
        on_change=change_maica_tp_apis
    )

    def change_maica_mvista_addr(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_mvista_addr",
        renpy.substitute(_("MAICA Server MVista服务商url")),
        on_change=change_maica_mvista_addr
    )

    def change_maica_mvista_key(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_mvista_key",
        renpy.substitute(_("MAICA Server MVista服务商api key")),
        on_change=change_maica_mvista_key
    )

    def change_maica_mvista_choice(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_mvista_choice",
        renpy.substitute(_("MAICA Server MVista模型名称")),
        on_change=change_maica_mvista_choice
    )


    def change_maica_mnerve_addr(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_mnerve_addr",
        renpy.substitute(_("MAICA Server MNerve服务商url")),
        on_change=change_maica_mnerve_addr
    )

    def change_maica_mnerve_key(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_mnerve_key",
        renpy.substitute(_("MAICA Server MNerve服务商api key")),
        on_change=change_maica_mnerve_key
    )

    def change_maica_mnerve_choice(param):
        return True, param
    store.mas_registerAPIKey(
        "maica_mnerve_choice",
        renpy.substitute(_("MAICA Server MNerve模型名称")),
        on_change=change_maica_mnerve_choice
    )

    def maica_update_key():
        # Core URL and key from registered API keys
        maicasv.set_env('MAICA_MCORE_ADDR', mas_getAPIKey("maica_core_url") or '')
        maicasv.set_env('MAICA_MCORE_KEY', mas_getAPIKey("maica_core_key") or '')
        maicasv.set_env('MAICA_MCORE_CHOICE', mas_getAPIKey("maica_core_model") or '')

        # MFocus URL and key from registered API keys
        maicasv.set_env('MAICA_MFOCUS_ADDR', mas_getAPIKey("maica_mfocus_url") or '')
        maicasv.set_env('MAICA_MFOCUS_KEY', mas_getAPIKey("maica_mfocus_key") or '')
        maicasv.set_env('MAICA_MFOCUS_CHOICE', mas_getAPIKey("maica_mfocus_model") or '')

        # MVista URL and key from registered API keys
        maicasv.set_env('MAICA_MVISTA_ADDR', mas_getAPIKey("maica_mvista_addr") or '')
        maicasv.set_env('MAICA_MVISTA_KEY', mas_getAPIKey("maica_mvista_key") or '')
        maicasv.set_env('MAICA_MVISTA_CHOICE', mas_getAPIKey("maica_mvista_choice") or '')
        # maicasv.set_env('MAICA_MVISTA_EXTRA', mas_getAPIKey("maica_mvista_extra") or '{\n        "extra_body": {\n        }\n    }')

        # MNerve URL and key from registered API keys
        maicasv.set_env('MAICA_MNERVE_ADDR', mas_getAPIKey("maica_mnerve_addr") or '')
        maicasv.set_env('MAICA_MNERVE_KEY', mas_getAPIKey("maica_mnerve_key") or '')
        maicasv.set_env('MAICA_MNERVE_CHOICE', mas_getAPIKey("maica_mnerve_choice") or '')

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

        # Third-party APIs from registered API keys
        maicasv.set_env('MAICA_TP_APIS', mas_getAPIKey("maica_tp_apis") or '{\n        "GAODE_WEATHER": ""\n    }')

        # Connection and performance settings
        maicasv.set_env('MAICA_KICK_STALE_CONNS', '1')
        maicasv.set_env('MAICA_F2B_COUNT', '20')
        maicasv.set_env('MAICA_F2B_TIME', '600')
        maicasv.set_env('MAICA_FULL_RESTFUL', '1')
        maicasv.set_env('MAICA_ROTATE_MSCACHE', '0')
        maicasv.set_env('MAICA_PRINT_VERBOSE', '1')

        # Developer and system info
        maicasv.set_env('MAICA_DEV_IDENTITY', 'Marshmallow')
        maicasv.set_env('MAICA_DEV_STATUS', 'serving')
        maicasv.set_env('MAICA_SESSION_MAX_TOKEN', '28672')
        maicasv.set_env('MAICA_MCORE_NODE', 'HGX690-nuclear-edition')
        maicasv.set_env('MAICA_MFOCUS_NODE', 'HGX610-biohazard-edition')
        maicasv.set_env('MAICA_ALT_TOOLCALL', '1')
        maicasv.set_env('MAICA_IS_REAL_ENV', '1')

        store.mas_submod_utils.getAndRunFunctions("maica_update_key")

init 500 python:
    if persistent.maica_sv_autostart:
        maica_update_key()
        maicasv.start_server()