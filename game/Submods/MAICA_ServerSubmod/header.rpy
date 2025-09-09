init -990 python:
    maica_sv_ver = "1.0.2"
    store.mas_submod_utils.Submod(
        author="P",
        name="MAICA Illuminator compact",
        description=_("MAICA 后端服务器子模组"),
        version=maica_sv_ver,
        settings_pane="maica_server_setting_pane",
        dependencies={"MAICA Blessland":("1.3.0", "1.99.99")},
    )
default persistent.maica_sv_autostart = False
screen maica_server_setting_pane(): 
    python:
        import socket
        MaicaProviderManager.fakelocalprovider.update({
            "name":renpy.substitute(_("MAICA Illuminator compact 本地部署")),
            "deviceName": socket.gethostname(),
            "portalPage": "https://github.com/Mon1-innovation/MAICA_Server_Submod",
            "servingModel": mas_getAPIKey("maica_core_model"),
        })
    vbox:
        xmaximum 800
        xfill True
        style_prefix "check"
        textbutton _("> 启动服务器"):
            action [Function(maica_update_key),
            Function(maicasv.start_server)]
        textbutton _("> 关闭服务器"):
            action Function(maicasv.stop_server)
        textbutton _("> 添加账号"):
            action Show("maica_add_account")
        textbutton _("> 要求 MAICA Blessland 重新检测可用性"):
            action Function(store.maica.maica.accessable)
        textbutton _("> 自动启动"):
            action ToggleField(persistent, "maica_sv_autostart")

screen maica_add_account():
    python:
        import maica_user_registration
        maica_user_registration.logger = store.mas_submod_utils.submod_log
        maica_user_registration.path = os.path.join(renpy.config.basedir, "game", "Submods", "MAICA_ServerSubmod", "Register.exe")
        db_path = os.path.join(renpy.config.basedir, "game", "Submods", "MAICA_ServerSubmod", "forum_flarum_db.db") 

        def maica_clear():
            store.mas_api_keys.api_keys.update({"Maica_Token":store.maica.maica.ciphertext})
            store.mas_api_keys.save_keys()
    modal True
    zorder 215

    style_prefix "confirm"

    frame:
        vbox:
            xfill False
            yfill False
            spacing 5                        

                    
            hbox:
                textbutton _("输入邮箱"):
                    action Show("maica_login_input",message = _("请输入账号邮箱"),returnto = "_maica_LoginEmail")
            hbox:
                textbutton _("输入用户名"):
                    action Show("maica_login_input",message = _("请输入账号用户名") ,returnto = "_maica_LoginAcc")
            hbox:
                textbutton _("输入密码"):
                    action Show("maica_login_input",message = _("请输入账号密码"),returnto = "_maica_LoginPw")
            hbox:
                text ""
            hbox:
                textbutton _("创建账号"):
                    action [
                        Function(maica_user_registration.register_user, store._maica_LoginAcc, store._maica_LoginEmail, store._maica_LoginPw, db_path),
                    ]
                textbutton _("在 MAICA Blessland 中应用（须提前开启服务器）"):
                    action [
                        Function(store.maica.maica.accessable),
                        Function(store.maica.maica._gen_token, store._maica_LoginAcc, store._maica_LoginPw, "", store._maica_LoginEmail if store._maica_LoginEmail != "" else None),
                        Function(_maica_verify_token),
                        Function(maica_clear),
                        ]

                textbutton _("关闭"):
                    action [Hide("maica_add_account")]
            hbox:
                text _("{size=-10}此处的账密等信息建议仅使用英文和数字，避免使用特殊符号")
            hbox:
                text _("{size=-10}此处使用的邮箱不会验证合法性")
            hbox:
                text _("{size=-10}此处输入的信息不会被自动清理, 以便备读")


screen maica_server_setting():
    python:
        submods_screen = store.renpy.get_screen("submods", "screens")

        if submods_screen:
            _tooltip = submods_screen.scope.get("tooltip", None)
        else:
            _tooltip = None
    modal True
    zorder 215
    
    style_prefix "check"

    frame:
        vbox:
            xmaximum 1100
            spacing 5
            viewport:
                id "viewport"
                scrollbars "vertical"
                ymaximum 600
                xmaximum 1100
                xfill True
                yfill False
                mousewheel True
                draggable True
                
                vbox:
                    xmaximum 1100
                    xfill True
                    yfill False
                    hbox:
                        text "text"
                
                    hbox:
                        style_prefix "confirm"
                        textbutton _("关闭"):
                            action Hide("maica_server_setting")
