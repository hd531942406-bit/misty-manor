## 迷雾庄园 — 界面 v3

# ═══════════════════════════════════════
# 标题画面
# ═══════════════════════════════════════

screen title_screen():
    tag menu
    add Solid("#0d0d12")

    vbox:
        xalign 0.5 ypos 150
        text "迷 雾 庄 园" size 72 color "#d4a853" xalign 0.5
        text "Misty Manor" size 22 color "#8a7b6b" xalign 0.5

    vbox:
        xalign 0.5 ypos 400 spacing 22

        textbutton "开始游戏":
            action Start()
            xalign 0.5
            text_size 36
            text_color "#e8d5a3"
            text_hover_color "#ffffff"

        textbutton "继续游戏":
            action ShowMenu("load")
            xalign 0.5
            text_size 32
            text_color "#c8b897"
            text_hover_color "#e8d5a3"

    hbox:
        xalign 0.5 ypos 660 spacing 40
        textbutton "设置" action ShowMenu("game_settings"):
            text_size 22 text_color "#8a7b6b" text_hover_color "#c8b897"
        textbutton "成就" action ShowMenu("achievement_screen"):
            text_size 22 text_color "#8a7b6b" text_hover_color "#c8b897"
        textbutton "画廊" action ShowMenu("ending_gallery"):
            text_size 22 text_color "#8a7b6b" text_hover_color "#c8b897"
        textbutton "退出" action Quit(confirm=True):
            text_size 22 text_color "#8a7b6b" text_hover_color "#c8b897"

    text "v[config.version]" size 14 color "#4a4a4a" xalign 0.98 yalign 0.98

# ═══════════════════════════════════════
# 背包
# ═══════════════════════════════════════

screen inventory_screen():
    tag menu
    modal True
    zorder 100
    add Solid("#0d0d12")

    vbox:
        xalign 0.5 yalign 0.5 spacing 25
        text "背 包" size 52 color "#d4a853" xalign 0.5
        null height 10

        viewport:
            xalign 0.5 xsize 850 ysize 450 draggable True mousewheel True
            vbox:
                spacing 18
                if state.inventory:
                    for item_id in state.inventory:
                        if item_id in ITEMS:
                            $ name, desc = ITEMS[item_id]
                            frame:
                                background Solid("#151520")
                                padding (24, 18) xfill True
                                hbox:
                                    spacing 20
                                    text "◆" size 24 color "#d4a853" yalign 0.5
                                    vbox:
                                        text name size 26 color "#e8d5a3"
                                        text desc size 18 color "#8a7b6b"
                else:
                    text "背包是空的" size 24 color "#6b5d4e" xalign 0.5

        null height 20
        textbutton "关闭":
            action Return()
            xalign 0.5 text_size 26
            text_color "#d4a853" text_hover_color "#ffffff"


# ═══════════════════════════════════════
# 成就弹窗
# ═══════════════════════════════════════

screen achievement_popup(ach_id):
    zorder 200
    timer 3.5 action Hide("achievement_popup")
    frame:
        xalign 0.98 ypos 20 xsize 380
        background Frame(Solid("#151525"), 12, 12)
        padding (22, 18)
        vbox:
            text "✦ 成就解锁" size 18 color "#d4a853"
            text get_ach_name(ach_id) size 24 color "#e8d5a3"
            text get_ach_desc(ach_id) size 16 color "#8a7b6b"


init python:
    def achievement_scroll_warper(done):
        done = max(0.0, min(1.0, done))
        return 1.0 - (1.0 - done) ** 3

    def smooth_achievement_scroll(adjustment, amount):
        target = max(0, min(adjustment.range, adjustment.value + amount))
        delta = target - adjustment.value
        if delta:
            adjustment.animate(delta, 0.22, achievement_scroll_warper)


style achievement_scrollbar is vscrollbar:
    xsize 10
    base_bar Solid("#24202a")
    thumb Solid("#d4a853")
    hover_thumb Solid("#e8d5a3")
    thumb_shadow None
    thumb_offset 0
    bar_resizing True


# ═══════════════════════════════════════
# 成就列表
# ═══════════════════════════════════════

screen achievement_screen():
    tag menu
    modal True
    default achievement_yadjustment = ui.adjustment(step=24)

    key "viewport_wheelup" action Function(smooth_achievement_scroll, achievement_yadjustment, -64)
    key "viewport_wheeldown" action Function(smooth_achievement_scroll, achievement_yadjustment, 64)

    add Solid("#0d0d12")

    textbutton "返回" action Return():
        xalign 0.96 ypos 12
        text_size 22 text_color "#8a7b6b" text_hover_color "#d4a853"

    vbox:
        xalign 0.5 ypos 36 spacing 16
        text "成 就" size 52 color "#d4a853" xalign 0.5
        text "已解锁 {color=#d4a853}[persistent.achievements.__len__()]{/color} / 10" size 22 color "#8a7b6b" xalign 0.5
        null height 4

        hbox:
            xalign 0.5
            spacing 12

            viewport id "achievement_viewport":
                xsize 900
                ysize 440
                yadjustment achievement_yadjustment
                draggable True
                mousewheel False
                pagekeys True

                vbox:
                    spacing 12
                    for ach_id, (name, desc) in sorted(ACHIEVEMENTS.items()):
                        $ unlocked = ach_id in persistent.achievements
                        frame:
                            xsize 880
                            background Solid("#151520" if unlocked else "#0e0e15")
                            padding (22, 14)
                            hbox:
                                xfill True
                                vbox:
                                    xsize 760
                                    text name size 24 color ("#e8d5a3" if unlocked else "#5a5a5a")
                                    text desc:
                                        size 16
                                        color ("#8a7b6b" if unlocked else "#4a4a4a")
                                        xmaximum 740
                                if unlocked:
                                    text "✦" size 32 color "#d4a853" yalign 0.5
                                else:
                                    text "◇" size 28 color "#4a4a4a" yalign 0.5

            vbar value YScrollValue("achievement_viewport") style "achievement_scrollbar":
                ysize 440

        null height 6
        textbutton "返回":
            action Return()
            xalign 0.5 text_size 26
            text_color "#d4a853" text_hover_color "#ffffff"


# ═══════════════════════════════════════
# 结局画廊
# ═══════════════════════════════════════

screen ending_gallery():
    tag menu
    modal True
    add Solid("#0d0d12")

    vbox:
        xalign 0.5 ypos 60 spacing 30
        text "结 局 画 廊" size 52 color "#d4a853" xalign 0.5
        text "已达成 {color=#d4a853}[persistent.endings_seen.__len__()]{/color} / 4" size 22 color "#8a7b6b" xalign 0.5
        null height 10

        hbox:
            xalign 0.5 spacing 50
            for ending_id, ending_name, ending_color, ending_desc in [
                ("truth",  "真相大白", "#e8d5a3", "揭露庄园的秘密，\n将真相公之于众。"),
                ("escape", "逃离庄园", "#c8b897", "离开迷雾庄园，\n但真相永埋心底。"),
                ("trapped","永远困住", "#cc5555", "被庄园吞噬，\n成为迷雾的永远居民。"),
                ("master", "庄园之主", "#d4a853", "继承庄园，\n成为新一代守护者。"),
            ]:
                $ unlocked = ending_id in persistent.endings_seen
                frame:
                    background Solid("#151520" if unlocked else "#0e0e15")
                    xsize 280 ysize 260 padding (24, 24)
                    vbox:
                        xalign 0.5 yalign 0.5 spacing 12
                        if unlocked:
                            text ending_name size 28 color ending_color xalign 0.5
                            null height 6
                            text ending_desc size 16 color "#8a7b6b" xalign 0.5 text_align 0.5
                        else:
                            text "???" size 28 color "#5a5a5a" xalign 0.5
                            null height 6
                            text "尚未解锁" size 16 color "#4a4a4a" xalign 0.5

        null height 20
        textbutton "返回":
            action Return()
            xalign 0.5 text_size 26
            text_color "#d4a853" text_hover_color "#ffffff"


# ═══════════════════════════════════════
# 确认弹窗
# ═══════════════════════════════════════

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#000000cc")

    frame:
        xalign 0.5 yalign 0.5
        xsize 550 ysize 200
        background Frame(Solid("#151520"), 12, 12)
        padding (35, 30)

        vbox:
            xalign 0.5 yalign 0.5 spacing 25
            text message size 24 color "#c8b897" xalign 0.5 text_align 0.5

            hbox:
                xalign 0.5 spacing 50
                textbutton "确定":
                    action yes_action
                    text_size 24
                    text_color "#d4a853" text_hover_color "#ffffff"
                textbutton "取消":
                    action no_action
                    text_size 24
                    text_color "#8a7b6b" text_hover_color "#c8b897"


# ═══════════════════════════════════════
# 导航（加入成就和画廊入口）
# ═══════════════════════════════════════

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton "开始游戏" action Start()
        else:
            textbutton "历史记录" action ShowMenu("history")
            textbutton "保存游戏" action ShowMenu("save")

        textbutton "读取存档" action ShowMenu("load")

        if not main_menu:
            textbutton "成就列表" action ShowMenu("achievement_screen")
            textbutton "结局画廊" action ShowMenu("ending_gallery")

        if main_menu:
            textbutton "成就列表" action ShowMenu("achievement_screen")
            textbutton "结局画廊" action ShowMenu("ending_gallery")

        if renpy.variant("pc"):
            textbutton "设置" action ShowMenu("game_settings")

        if main_menu:
            textbutton "关于" action ShowMenu("about")

        if not main_menu:
            textbutton "主菜单" action MainMenu()

        if renpy.variant("pc"):
            textbutton "退出" action Quit(confirm=True)


# ═══════════════════════════════════════
# 游戏内快捷按钮
# ═══════════════════════════════════════

# ═══════════════════════════════════════
# 选项屏幕 — 居中显示
# ═══════════════════════════════════════

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.65
        spacing gui.choice_spacing

        for i in items:
            textbutton i.caption:
                action i.action
                xalign 0.5
                text_xalign 0.5
                at transform:
                    alpha 0.0
                    linear 0.2 alpha 1.0

screen quick_buttons():
    hbox:
        xalign 0.98 yalign 0.02 spacing 10
        textbutton "设置" action ShowMenu("game_settings"):
            text_size 15 text_color "#8a7b6b" text_hover_color "#d4a853"
        textbutton "回看" action ShowMenu("history"):
            text_size 15 text_color "#8a7b6b" text_hover_color "#d4a853"
        textbutton "存档" action ShowMenu("save"):
            text_size 15 text_color "#8a7b6b" text_hover_color "#d4a853"
        textbutton "读档" action ShowMenu("load"):
            text_size 15 text_color "#8a7b6b" text_hover_color "#d4a853"
        textbutton "背包" action ShowMenu("inventory_screen"):
            text_size 15 text_color "#8a7b6b" text_hover_color "#d4a853"
        textbutton "成就" action ShowMenu("achievement_screen"):
            text_size 15 text_color "#8a7b6b" text_hover_color "#d4a853"
        textbutton "画廊" action ShowMenu("ending_gallery"):
            text_size 15 text_color "#8a7b6b" text_hover_color "#d4a853"


# ═══════════════════════════════════════
# 存档 / 读档界面
# ═══════════════════════════════════════

screen save():
    tag menu
    use file_slots("保存游戏")

screen load():
    tag menu
    use file_slots("读取存档")

screen file_slots(title):
    add Solid("#0d0d12")

    textbutton "返回" action Return():
        xalign 0.96 ypos 12
        text_size 22 text_color "#8a7b6b" text_hover_color "#d4a853"

    vbox:
        xalign 0.5 ypos 50 spacing 25
        text title size 48 color "#d4a853" xalign 0.5
        null height 10

        grid 3 2:
            xalign 0.5 spacing 35
            for i in range(1, 7):
                $ slot_name = FileSlotName(i, 6)
                $ save_time = FileTime(i, empty="")
                $ has_save = FileLoadable(i)

                button:
                    action FileAction(i)
                    xsize 360 ysize 240
                    background Frame(Solid("#151520"), 10, 10)
                    hover_background Frame(Solid("#252535"), 10, 10)

                    vbox:
                        xalign 0.5 yalign 0.5 spacing 8
                        text "存档 [i]" size 22 color "#d4a853" xalign 0.5
                        if has_save:
                            text save_time size 16 color "#8a7b6b" xalign 0.5
                        else:
                            text "—— 空 ——" size 16 color "#5a5a5a" xalign 0.5

        null height 15
        textbutton "返回":
            action Return()
            xalign 0.5 text_size 26
            text_color "#d4a853" text_hover_color "#ffffff"


# ═══════════════════════════════════════
# 设置界面 — 中文
# ═══════════════════════════════════════

style settings_bar:
    left_bar Solid("#d4a853")
    right_bar Solid("#333333")
    thumb Solid("#e8d5a3")
    thumb_offset 8
    ysize 28

screen game_settings():
    tag menu
    add Solid("#0d0d12")

    textbutton "返回" action Return():
        xalign 0.96 ypos 12
        text_size 22 text_color "#8a7b6b" text_hover_color "#d4a853"

    vbox:
        xalign 0.5 ypos 60 spacing 22
        text "设 置" size 48 color "#d4a853" xalign 0.5

        null height 15

        # 游戏音量
        hbox:
            xalign 0.5 spacing 30
            text "游戏音量" size 28 color "#c8b897" yalign 0.5 xsize 180
            bar value Preference("music volume") xsize 340 ysize 36 style "settings_bar"

        # 游戏音效
        hbox:
            xalign 0.5 spacing 30
            text "游戏音效" size 28 color "#c8b897" yalign 0.5 xsize 180
            bar value Preference("sound volume") xsize 340 ysize 36 style "settings_bar"

        # 文字速度
        hbox:
            xalign 0.5 spacing 30
            text "文字速度" size 28 color "#c8b897" yalign 0.5 xsize 180
            bar value Preference("text speed") xsize 340 ysize 36 style "settings_bar"

        # 自动播放
        hbox:
            xalign 0.5 spacing 30
            text "自动播放" size 28 color "#c8b897" yalign 0.5 xsize 180
            bar value Preference("auto-forward time") xsize 340 ysize 36 style "settings_bar"

        null height 20

        # 全屏/窗口
        hbox:
            xalign 0.5 spacing 50
            textbutton "窗口" action Preference("display", "window"):
                text_size 24 text_color "#c8b897" text_hover_color "#ffffff"
                text_selected_color "#d4a853"
            textbutton "全屏" action Preference("display", "fullscreen"):
                text_size 24 text_color "#c8b897" text_hover_color "#ffffff"
                text_selected_color "#d4a853"

        # 跳过
        hbox:
            xalign 0.5 spacing 50
            textbutton "跳过已读" action Preference("skip", "seen"):
                text_size 24 text_color "#c8b897" text_hover_color "#ffffff"
                text_selected_color "#d4a853"
            textbutton "跳过全部" action Preference("skip", "all"):
                text_size 24 text_color "#c8b897" text_hover_color "#ffffff"
                text_selected_color "#d4a853"

        null height 15

        textbutton "返回":
            action Return()
            xalign 0.5 text_size 28
            text_color "#d4a853" text_hover_color "#ffffff"


# ═══════════════════════════════════════
# 回看界面
# ═══════════════════════════════════════

screen history():
    tag menu
    add Solid("#0d0d12")

    vbox:
        xalign 0.5 ypos 30 spacing 10
        text "回 看" size 48 color "#d4a853" xalign 0.5
        text "共 [_history_list.__len__()] 条" size 18 color "#6b5d4e" xalign 0.5

        null height 5

        viewport:
            xalign 0.5
            xsize 1000 ysize 460
            draggable True mousewheel True
            yinitial 1.0
            scrollbars "vertical"

            vbox:
                spacing 8
                for h in _history_list:
                    $ w = h.who or ""
                    $ t = h.what or ""
                    # 去掉所有 {color} {/color} 等标签
                    $ import re
                    $ t = re.sub(r'\{[^}]*\}', '', t)
                    frame:
                        background None
                        padding (5, 5)
                        if w:
                            text w size 20 color "#d4a853" bold True
                        if t.strip():
                            text t size 20 color "#ffffff"
                        else:
                            text "(empty)" size 14 color "#444"

        null height 10

        textbutton "返回":
            action Return()
            xalign 0.5 text_size 26
            text_color "#d4a853" text_hover_color "#ffffff"


# ═══════════════════════════════════════
# 对话框 — 左上角显示说话人姓名
# ═══════════════════════════════════════

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        background Frame(Solid("#0d0d12cc"), 10, 10)

        if who is not None:
            frame:
                xalign 0.0 yalign 0.0
                xpos 50 ypos 15
                background Frame(Solid("#151520aa"), 6, 6)
                padding (15, 8)
                text who:
                    size 28
                    color "#d4a853"
                    bold True

        text what:
            id "what"
            xalign 0.0 yalign 0.5
            text_align 0.0


init python:
    config.overlay_screens.append("quick_buttons")
