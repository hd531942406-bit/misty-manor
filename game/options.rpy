## 迷雾庄园 — 游戏配置 v2.0
## 视觉效果 · 角色系统 · 成就 · 音效

init python:
    import sys
    sys.path.insert(0, renpy.config.gamedir)

    # ── 字体替换：把默认字体映射到 SimHei ──
    config.font_replacement_map["DejaVuSans.ttf", False, False] = ("SimHei.ttf", False, False)
    config.font_replacement_map["DejaVuSans.ttf", True, False]  = ("SimHei.ttf", True, False)
    config.font_replacement_map["DejaVuSans.ttf", False, True]  = ("SimHei.ttf", False, True)
    config.font_replacement_map["DejaVuSans.ttf", True, True]   = ("SimHei.ttf", True, True)

    # ═══════════════════════════════════════
    # 游戏状态
    # ═══════════════════════════════════════

    class GameState:
        def __init__(self):
            self.inventory = []
            self.flags = set()
            self.visit_count = {}

        def has_item(self, item_id):
            return item_id in self.inventory

        def add_item(self, item_id):
            if item_id not in self.inventory:
                self.inventory.append(item_id)
                return True
            return False

        def has_flag(self, flag):
            return flag in self.flags

        def set_flag(self, flag):
            self.flags.add(flag)

        def visited(self, scene_id):
            return self.visit_count.get(scene_id, 0)

        def visit(self, scene_id):
            self.visit_count[scene_id] = self.visit_count.get(scene_id, 0) + 1

    # ═══════════════════════════════════════
    # 成就函数（使用 Ren'Py 内置 persistent）
    # ═══════════════════════════════════════

    def grant_achievement(ach_id):
        """解锁成就 (Steam 兼容)"""
        if ach_id not in persistent.achievements:
            persistent.achievements.add(ach_id)
            achievement.grant(ach_id)
            renpy.show_screen("achievement_popup", ach_id)

    def unlock_ending(ending_id):
        """记录结局"""
        persistent.endings_seen.add(ending_id)
        if persistent.total_plays is None:
            persistent.total_plays = 0
        persistent.total_plays += 1

    # ═══════════════════════════════════════
    # 物品数据
    # ═══════════════════════════════════════

    ITEMS = {
        'old_key':       ('生锈的旧钥匙', '一把古铜色的钥匙，布满铜绿，似乎有些年头了。'),
        'cellar_key':    ('地窖钥匙',     '一枚沉甸甸的铁钥匙，柄上刻着诡异的圆形符号，触手冰凉。'),
        'diary':         ('陈旧的日记本',  '庄园主人的私人日记，封面上写着「李柘远」。'),
        'cipher_letter': ('密信',         '一封用密码写成的信函，落款处的印章——一个圆形符号。'),
        'jade_token':    ('玉坠',         '一枚温润的圆形玉坠，雕刻着古老的纹路。'),
    }

# ═══════════════════════════════════════
# 持久化变量
# ═══════════════════════════════════════

default state = GameState()

# 使用 Ren'Py 内置 persistent — 跨周目持久化
init python:
    if persistent.achievements is None:
        persistent.achievements = set()
    if persistent.endings_seen is None:
        persistent.endings_seen = set()
    if persistent.cgs_unlocked is None:
        persistent.cgs_unlocked = set()
    if persistent.total_plays is None:
        persistent.total_plays = 0

# ═══════════════════════════════════════
# 游戏信息
# ═══════════════════════════════════════

define config.name = "迷雾庄园"
define config.version = "0.3.0"
define gui.show_name = True
define config.window_title = "迷雾庄园 — Misty Manor"

# ═══════════════════════════════════════
# 存档设置
# ═══════════════════════════════════════

define config.has_autosave = True
define config.autosave_on_choice = True
define config.autosave_on_quit = True
define config.rollback_enabled = True
define config.hard_rollback_limit = 30
define config.skip_delay = 50
define config.history_length = 200


# ═══════════════════════════════════════
# 音效系统
# ═══════════════════════════════════════

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

# 音频通道
init python:
    renpy.music.register_channel("ambient", "sfx", True)   # 环境音
    renpy.music.register_channel("sfx2", "sfx", False)      # 第二音效
    renpy.music.register_channel("ui", "sfx", False)        # UI 音效

# 音效引用（占位 — 后续替换为实际文件）
define audio.bgm_title      = "audio/bgm_title.ogg"
define audio.bgm_explore    = "audio/bgm_explore.ogg"
define audio.bgm_tense      = "audio/bgm_tense.ogg"
define audio.bgm_climax     = "audio/bgm_climax.ogg"
define audio.bgm_ending_good = "audio/bgm_ending_good.ogg"
define audio.bgm_ending_bad  = "audio/bgm_ending_bad.ogg"

define audio.ambient_wind   = "audio/ambient_wind.ogg"
define audio.ambient_clock  = "audio/ambient_clock.ogg"
define audio.ambient_rain   = "audio/ambient_rain.ogg"
define audio.ambient_fire   = "audio/ambient_fire.ogg"

define audio.sfx_door       = "audio/sfx_door.ogg"
define audio.sfx_key        = "audio/sfx_key.ogg"
define audio.sfx_item       = "audio/sfx_item.ogg"
define audio.sfx_click      = "audio/sfx_click.ogg"
define audio.sfx_heartbeat  = "audio/sfx_heartbeat.ogg"

# ═══════════════════════════════════════
# 视觉效果
# ═══════════════════════════════════════

# 过渡效果
define dissolve   = Dissolve(0.5)
define fade       = Fade(0.5, 0.3, 0.5)
define flash      = Fade(0.1, 0.0, 0.1, color="#fff")
define slow_fade  = Fade(1.5, 0.5, 1.5)

# 场景效果
transform fog_drift:
    """雾气粒子漂移效果"""
    alpha 0.3
    parallel:
        xpos 0.2
        linear 20.0 xpos 0.8
        linear 20.0 xpos 0.2
        repeat
    parallel:
        ypos 0.8
        linear 15.0 ypos 0.6
        linear 15.0 ypos 0.8
        repeat

transform title_float:
    """标题浮动"""
    ypos 0.45
    easeout 4.0 ypos 0.43
    easein  4.0 ypos 0.45
    repeat

transform screen_shake:
    """屏幕震动"""
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 3
    linear 0.05 xoffset -3
    linear 0.05 xoffset 0

transform slow_zoom:
    """慢速缩放 (Ken Burns 效果)"""
    zoom 1.0
    linear 30.0 zoom 1.05

transform vignette:
    """暗角叠加"""
    alpha 0.0

transform rune_glow:
    """符文发光脉冲"""
    alpha 0.5
    linear 2.0 alpha 0.8
    linear 2.0 alpha 0.5
    repeat

# 场景粒子
image firefly = SnowBlossom(
    Solid("#88ff88", xsize=4, ysize=4),
    count=30,
    border=80,
    xspeed=(1, 5),
    yspeed=(-3, 1),
    start=0
)

image rune_spark = SnowBlossom(
    Solid("#4466ff", xsize=3, ysize=3),
    count=60,
    border=100,
    xspeed=(2, 6),
    yspeed=(-2, 2),
    start=0
)

image mist_heavy = SnowBlossom(
    Solid("#3a3530", xsize=8, ysize=8),
    count=120,
    border=120,
    xspeed=(1, 4),
    yspeed=(-2, 1),
    start=0
)

# ═══════════════════════════════════════
# 角色立绘 — 图片已在 images/ 目录，自动加载
# ═══════════════════════════════════════

# 角色出场位置
transform left_enter:
    xalign -0.3 yalign 1.0
    easein 0.8 xalign 0.15

transform right_enter:
    xalign 1.3 yalign 1.0
    easein 0.8 xalign 0.85

transform center_stand:
    xalign 0.5 yalign 1.0

transform left_stand:
    xalign 0.15 yalign 1.0

transform right_stand:
    xalign 0.85 yalign 1.0

# ═══════════════════════════════════════
# 成就定义 (Steam 兼容)
# ═══════════════════════════════════════

init python:
    # 注册成就
    achievement.register("first_step")
    achievement.register("secret_finder")
    achievement.register("diary_reader")
    achievement.register("truth_seeker")
    achievement.register("escape_artist")
    achievement.register("trapped_soul")
    achievement.register("new_master")
    achievement.register("collector")
    achievement.register("explorer")
    achievement.register("all_endings")

    # 成就描述
    ACHIEVEMENTS = {
        "first_step":     ("第一步",        "抵达庄园大厅"),
        "secret_finder":  ("秘密发掘者",    "在书架中发现密信"),
        "diary_reader":   ("日记读者",      "找到庄园主人的日记"),
        "truth_seeker":   ("真相追寻者",    "揭露迷雾庄园的秘密——真相大白结局"),
        "escape_artist":  ("逃脱大师",      "成功逃离迷雾庄园"),
        "trapped_soul":   ("困于迷雾",      "被庄园永远困住"),
        "new_master":     ("新任庄主",      "成为庄园的新主人"),
        "collector":      ("收藏家",        "在一个周目中集齐全部 5 件物品"),
        "explorer":       ("探险家",        "探索全部场景"),
        "all_endings":    ("全结局收集",    "达成全部 4 个结局"),
    }

    def get_ach_name(ach_id):
        return ACHIEVEMENTS.get(ach_id, (ach_id, ""))[0]

    def get_ach_desc(ach_id):
        return ACHIEVEMENTS.get(ach_id, ("", ach_id))[1]
