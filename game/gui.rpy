## 迷雾庄园 — GUI v3
## ADV 模式 — 底部对话框 · 居中选项

# ═══════════════════════════════════════
# 字体
# ═══════════════════════════════════════

define gui.text_font = "SimHei.ttf"
define gui.name_font = "SimHei.ttf"
define gui.interface_font = "SimHei.ttf"
define gui.choice_button_text_font = "SimHei.ttf"
define gui.button_text_font = "SimHei.ttf"
define gui.label_text_font = "SimHei.ttf"

# ═══════════════════════════════════════
# 逐字显示速度 — 每秒 40 字
# ═══════════════════════════════════════

default preferences.text_cps = 40

# ═══════════════════════════════════════
# 字号
# ═══════════════════════════════════════

define gui.text_size = 28
define gui.name_text_size = 30
define gui.interface_text_size = 24
define gui.label_text_size = 36
define gui.notify_text_size = 20
define gui.title_text_size = 56

# ═══════════════════════════════════════
# 文字颜色
# ═══════════════════════════════════════

define gui.text_color = "#d4c4a0"
define gui.interface_text_color = "#c8b897"
define gui.hover_color = "#e8d5a3"
define gui.selected_color = "#d4a853"
define gui.idle_color = "#8a7b6b"
define gui.idle_small_color = "#6b5d4e"
define gui.accent_color = "#d4a853"

# ═══════════════════════════════════════
# 主菜单
# ═══════════════════════════════════════

define gui.main_menu_background = "#0d0d12"
define gui.main_menu_text_color = "#c8b897"
define gui.game_menu_background = "#0d0d12"
define gui.game_menu_text_color = "#c8b897"

# ═══════════════════════════════════════
# 对话框 — 底部居中
# ═══════════════════════════════════════

define gui.dialogue_xpos = 0.08
define gui.dialogue_ypos = 0.78
define gui.dialogue_width = 0.84
define gui.dialogue_text_xpos = 0.08
define gui.dialogue_text_xalign = 0.0
define gui.dialogue_text_yalign = 0.5
define gui.dialogue_height = 200

# 对话框背景透明暗底
define gui.dialogue_background = Frame(Solid("#0d0d12cc"), 10, 10)

# ═══════════════════════════════════════
# 选项 — 屏幕正中
# ═══════════════════════════════════════

define gui.choice_button_width = 700
define gui.choice_button_height = None
define gui.choice_button_xalign = 0.5
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_borders = Borders(30, 18, 30, 18)
define gui.choice_button_text_size = 26
define gui.choice_button_text_idle_color = "#c8b897"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_background = Frame(Solid("#151520"), 8, 8)
define gui.choice_button_hover_background = Frame(Solid("#252535"), 8, 8)

# 选项间距
define gui.choice_spacing = 16

# ═══════════════════════════════════════
# 存档槽
# ═══════════════════════════════════════

define gui.slot_background = Frame(Solid("#151520"), 10, 10)
define gui.slot_hover_background = Frame(Solid("#252535"), 10, 10)
define gui.slot_text_color = "#c8b897"
define gui.slot_text_hover_color = "#e8d5a3"
define gui.slot_text_size = 22
define gui.slot_button_text_size = 18

# ═══════════════════════════════════════
# 滚动条 / 滑块
# ═══════════════════════════════════════

# 滑动条 — 金色，可见
define gui.bar_idle_thumb = Solid("#d4a853")
define gui.bar_hover_thumb = Solid("#e8d5a3")
define gui.bar_idle_bar = Frame(Solid("#d4a85333"), 4, 4)
define gui.bar_hover_bar = Frame(Solid("#d4a85366"), 4, 4)
define gui.scrollbar_idle_bar = Frame(Solid("#d4a85333"), 4, 4)
define gui.scrollbar_hover_bar = Frame(Solid("#d4a85366"), 4, 4)
define gui.slider_idle_bar = Frame(Solid("#d4a85333"), 4, 4)
define gui.slider_hover_bar = Frame(Solid("#d4a85366"), 4, 4)
define gui.scrollbar_idle_thumb = Solid("#d4a853")
define gui.scrollbar_hover_thumb = Solid("#e8d5a3")

# ═══════════════════════════════════════
# 确认弹窗 / 过渡
# ═══════════════════════════════════════

define gui.confirm_frame_background = Frame(Solid("#151520"), 10, 10)
define gui.default_transition = Dissolve(0.4)

# ═══════════════════════════════════════
# 导航
# ═══════════════════════════════════════

define gui.navigation_spacing = 12
define gui.navigation_xpos = 80
