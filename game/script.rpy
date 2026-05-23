## 迷雾庄园 — 主游戏脚本 v3.0
## 扩充剧本 · 视觉特效 · 增强叙事

# ═══════════════════════════════════════
# 角色（ADV 模式 — 底部对话框）
# ═══════════════════════════════════════

define narrator = Character(None, what_color="#d4c4a0", what_size=28)
define n = Character(None, what_color="#d4c4a0", what_size=28)

define detective = Character("侦探", color="#c8b897")
define butler_char = Character("管家", color="#8a7b6b")
define girl_char = Character("若兰", color="#d4a853")

# ═══════════════════════════════════════
# 背景图
# ═══════════════════════════════════════

image bg black = Solid("#000000")
image bg dark  = Solid("#0d0d12")

# 以下背景图由 Ren'Py 从 images/ 目录自动加载（文件名去掉 .png 即为图像名）

# ═══════════════════════════════════════
# 开场
# ═══════════════════════════════════════

label main_menu:
    call screen title_screen
    return

label splashscreen:
    scene bg black
    with fade
    return

# ═══════════════════════════════════════
# 序章 — 侦探办公室
# ═══════════════════════════════════════

label start:
    scene bg black
    with slow_fade

    $ state = GameState()

    """下午四点十七分，你的办公室门缝下多了一封信。

    没有邮戳，没有寄件人。信封是泛黄的奶油色，封口处滴着一枚暗红色的蜡封——上面印着一个从未见过的圆形符号，像是一条衔尾的蛇，又像是一道闭合的门。

    你拆开信封。信纸上的字迹修长而急促：

    {color=#c8b897}「致尊敬的侦探先生：\n\n    城郊迷雾庄园的主人李柘远先生，于三个月前失踪。警方已放弃搜寻。但他的女儿至今仍在等待一个答案。\n    随信附上庄园地址与一张旧照片。若您愿意接手此案，请于今夜前往庄园。\n    门不会锁。」{/color}

    信纸背面粘着一张褪色的照片——两个年轻男子站在一座灰白色庄园前，勾肩搭背，笑容灿烂。照片下方写着：「柘远与一鹤，建庄十年志。」

    {color=#8a7b6b}照片的边角已磨损发白，像是被人反复摩挲过。{/color}

    你点了一支烟，在暮色中思考了十分钟。然后拿起外套和钥匙，出了门。
    """

    """深夜十一点，你按照信上的地址，驱车来到城郊的「迷雾庄园」。

    车停在一片铁艺大门前。门扉半掩，铁锈斑驳。大门后的车道已被荒草侵占，远处一座灰白色的宅邸在月光下若隐若现。

    你下了车。空气里弥漫着泥土和腐叶的气息。雾很浓，像一层薄纱笼罩着整座庄园。

    四周一片寂静——没有虫鸣，没有风声，连自己的呼吸声都显得格外清晰。

    你注意到大门旁有一盏熄灭的门灯，门柱上刻着四个字：\n          {color=#d4a853}「雾 锁 重 门」{/color}
    """

    menu start_choice:
        "上前敲门":
            jump knock_door
        "绕到侧面翻墙入院" if not state.has_flag('entered_via_garden'):
            jump climb_wall

# ═══════════════════════════════════════
# 敲门
# ═══════════════════════════════════════

label knock_door:
    $ state.set_flag('entered_via_door')
    scene bg dark
    show mist_heavy
    with dissolve

    """
    你握住沉重的铜门环，在门上叩了三下。声音在夜空中回荡，像是惊醒了什么沉睡的东西。

    过了很久——久到你几乎要放弃时——门内传来缓慢的脚步声。吱呀一声，沉重的木门向内打开。

    {color=#c8b897}门缝里露出一张苍老的面孔。{/color}那是一个身着黑色旧式西装的老者，背微驼，目光浑浊而平静。他默默地打量着你，嘴角没有一丝弧度。

    {color=#8a7b6b}他没有问你的身份，没有确认你的来意。只是侧过身，做了一个「请进」的手势。{/color}

    你犹豫了一瞬，跨过门槛。身后，大门自动合拢，发出一声沉闷的响声。
    """

    hide mist_heavy

    jump hall

# ═══════════════════════════════════════
# 翻墙
# ═══════════════════════════════════════

label climb_wall:
    $ state.set_flag('entered_via_garden')
    scene bg garden
    show mist_heavy
    with dissolve

    """
    你沿着庄园的围墙走了几分钟，找到一处被藤蔓覆盖的低矮墙面。藤蔓很粗壮，足够承受一个人的重量。

    你攀着藤蔓翻上墙头。在墙头短暂停留的瞬间，整座庄园在脚下展开——灰白色的宅邸、荒芜的花园、远处隐约可见的温室玻璃在月光下泛着微光。

    你跳入墙内，落在松软的泥土上。双脚刚一落地，不远处的宅邸里突然亮起一盏灯。

    {color=#d4a853}有人在家。{/color}
    """

    hide mist_heavy

    menu:
        "沿着小路走向宅邸大门":
            jump hall
        "先在花园中探索":
            jump garden

# ═══════════════════════════════════════
# 大厅
# ═══════════════════════════════════════

label hall:
    $ state.visit('hall')
    $ state.set_flag('arrived_hall')
    scene bg hall
    with dissolve

    if not state.has_flag('_ach_first_step'):
        $ state.set_flag('_ach_first_step')
        $ grant_achievement("first_step")

    if state.has_flag('entered_via_door'):
        """
        宽敞的大厅比你想象的更加古老。

        穹顶高耸，一盏水晶吊灯垂在中央——只亮了不到一半的灯泡，投下昏黄的光晕。{color=#8a7b6b}那些熄灭的灯泡像是被什么东西刻意拧掉的。{/color}

        墙壁上挂着几幅肖像画，画中人的目光似乎在随着你的移动而转动。肖像画下方各有一块黄铜铭牌，但字迹已模糊难辨。

        墙角有一座古老的落地钟，钟摆在寂静中发出沉重的滴答声——{color=#8a7b6b}每一下都像是在为谁来倒计时。{/color}

        大厅四面各有一扇门，通向庄园的不同区域。老管家已经无声地消失在走廊深处，留下你独自站在大厅中央。
        """
    else:
        """
        你推开宅邸的侧门走进大厅。昏黄的烛光将影子拉得很长，墙上挂着的画像目光幽深。

        中央的摆钟滴答作响，声音在空旷的大厅中回荡。四面各有一扇门，通向不同的房间。
        """

    menu hall_choices:
        "仔细环顾大厅四周" if not state.has_flag('hall_explored'):
            jump hall_explore
        "寻找管家的踪影" if state.has_flag('hall_explored') and not state.has_flag('butler_spoke'):
            jump butler_encounter
        "前往图书馆":
            jump library
        "前往书房":
            jump study
        "前往花园":
            jump garden
        "前往地下室" if state.has_item('cellar_key'):
            jump basement
        "前往地下室（需要钥匙）" if not state.has_item('cellar_key'):
            "一扇厚重的铁门上挂着一把大锁，锁孔锈迹斑斑，需要对应的钥匙才能打开。"
            jump hall_choices
        "检查雨伞架" if state.visited('hall') >= 2 and not state.has_item('jade_token'):
            $ state.add_item('jade_token')
            "你在雨伞架底部发现了一枚玉坠，触手温润，上面刻着奇怪的纹路。"
            call check_collector_achievement
            jump hall_choices
        "上楼去卧室看看" if state.has_flag('hall_explored') and not state.has_flag('visited_bedroom'):
            jump master_bedroom
        "前往餐厅" if (state.visited('library') > 0 or state.visited('study') > 0) and not state.has_flag('visited_dining'):
            jump dining_hall
        "从正门离开庄园" if state.has_flag('entered_via_door') and state.visited('hall') >= 2:
            jump ending_escape

# ═══════════════════════════════════════
# 大厅探索（新场景）
# ═══════════════════════════════════════

label hall_explore:
    $ state.set_flag('hall_explored')

    """
    你放慢脚步，在大厅中仔细巡视。

    壁炉上方的肖像画是一个神情严肃的中年男人——{color=#c8b897}应该就是庄园主李柘远。{/color}画中的他穿着剪裁考究的西装，但眼神中有一丝不易察觉的焦虑。

    落地钟的钟面已经发黄，罗马数字像是手绘的。你注意到钟摆的节奏不太均匀——每隔十几秒，它会轻微地顿一下，像是被什么东西绊住了。

    水晶吊灯的正下方，地毯上有一块深色的污渍。{color=#8a7b6b}你蹲下来看了看——不是酒渍，更像是曾经有什么液体浸透后又干涸了。{/color}

    大厅两侧各有两扇门，分别通向图书馆、书房、花园和地下室。每扇门上方都雕刻着一个圆形符号——与信封蜡封上的符号完全一致。
    """

    jump hall_choices

# ═══════════════════════════════════════
# 管家对话（新场景）
# ═══════════════════════════════════════

label butler_encounter:
    $ state.set_flag('butler_spoke')

    """
    你在大厅侧面的走廊尽头找到了管家。

    他正站在一扇窗前，望着窗外的月色。窗台上积着厚厚的灰——{color=#8a7b6b}他可能已经站了很久。{/color}

    你走近时，他没有回头，只是缓缓开口，声音沙哑得像枯叶刮过石板：
    """

    butler_char "「你是来找那个人的。」"

    "不是疑问句。"

    butler_char "「李柘远。三个月前。他下地窖的时候，我就知道不会再见到他了。」"

    """
    管家终于转过身来。浑浊的眼睛里映着月光，没有焦点。
    """

    butler_char "「这座庄园需要一位主人。不是我们这种——是被选中的人。你是被邀请来的。我也是。」"

    """
    你问他在这里待了多久。

    管家没有回答。他的嘴角似乎动了一下——也许是微笑，也许是肌肉的痉挛。然后他离开了，脚步声被地毯吸收得干干净净。

    {color=#8a7b6b}你注意到他刚才站的位置——窗台上，灰尘里有他指尖划出的痕迹，隐约是一个圆形。{/color}
    """

    jump hall_choices

# ═══════════════════════════════════════
# 二楼卧室（新场景）
# ═══════════════════════════════════════

label master_bedroom:
    $ state.set_flag('visited_bedroom')
    scene bg dark
    with dissolve

    """
    你沿着大厅后方的楼梯走上二楼。木质楼梯在你脚下发出吱嘎的呻吟，每一声都像是整座庄园在你耳边低语。

    推开走廊尽头那扇半掩的门，你走进了庄园主人的卧室。房间不大，布置也很朴素——一张铁架床、一个衣柜、一张小书桌。{color=#8a7b6b}这里更像是苦行僧的住处，而不是拥有整座庄园的人的卧房。{/color}

    床铺整齐得近乎刻意——被角折成直角，枕头端正地放在正中央。床单上没有一丝褶皱。{color=#8a7b6b}不像是有人睡过的样子——更像是最后一次整理后就再也没有人碰过。{/color}

    桌上放着一个相框。你走近一看——照片上是一个年轻女人，怀里抱着一个婴儿。照片背面写着：「吾妻婉如，小女若兰，摄于建庄五年。」{color=#d4a853}原来温室的女孩叫若兰。{/color}

    你拉开抽屉，里面只有一个文件夹，标签上写着：「守护者传承：第一代至第四代记录。」你翻开第一页，密密麻麻的手写笔记记载着顾北川以来每一位庄园主人的生平和死因。

    {color=#8a7b6b}每一代的结语都一样：「自愿入阵，以血为约。门已闭，雾已散。」{/color}
    """

    jump hall_choices

# ═══════════════════════════════════════
# 餐厅（新场景）
# ═══════════════════════════════════════

label dining_hall:
    $ state.set_flag('visited_dining')
    scene bg dark
    with dissolve

    """
    你推开餐厅的双开弹簧门，走进一个可以容纳二十人用餐的宽敞空间。

    长桌中央放着一排银烛台，蜡烛早已燃尽，只剩下凝固的蜡泪。{color=#8a7b6b}桌上摆着六套餐具——但只有主位的那一套有使用过的痕迹。{/color}

    其他位置的餐具落满了灰尘，银器已经氧化发黑。显然这个庄园很久没有招待过客人了。但李柘远仍然每晚坐在主位上，独自用餐。

    墙壁上挂着一幅褪色的油画——画中是一个繁花盛开的花园，与现在的荒芜花园形成鲜明的对比。油画下方有一张小型供桌，桌上供着五张泛黄的照片。{color=#8a7b6b}每一张照片上的面孔都不一样，男女老少都有，但他们的眼神都带着同一种神色——不是恐惧，而是释然。{/color}

    供桌上放着一本烫金封面的册子，扉页上写着：「历代守护者名录。」你翻开最后一页——第六行是空的，第七行也是。{color=#c8b897}李柘远是第五代。{/color}

    册子里夹着一张手写字条：「吾之后来者，此非诅咒，乃天命也。庄园之下，万灵之枢。一代一人，方得其安。」落款处写着：「第四代守护者——秦一鹤。」
    """

    jump hall_choices

# ═══════════════════════════════════════
# 图书馆
# ═══════════════════════════════════════

label library:
    $ state.visit('library')
    scene bg library
    with dissolve

    """
    推开厚重的橡木门，你走进一间巨大的圆形图书室。

    从地板到天花板的整面墙壁都是书架，藏书数量惊人。{color=#8a7b6b}一股旧纸、皮革和时光的气息扑面而来。{/color}

    房间中央有一张宽大的橡木书桌，桌面上散落着几本书和一张泛白的信纸。一盏绿罩台灯是房间里唯一的光源——灯光在桌面上投下一圈暖绿色的光晕。

    你注意到墙壁上有一块区域的灰尘比其他地方薄——似乎有人近期移动过那里的书。
    """

    menu:
        "检查书架上的暗格" if not state.has_flag('found_letter'):
            jump bookshelf
        "翻阅桌上的书和信纸" if not state.has_flag('found_book'):
            jump read_book
        "深入检查图书馆" if not state.has_flag('library_searched'):
            jump library_search
        "返回大厅":
            jump hall

label bookshelf:
    $ state.set_flag('found_letter')
    $ state.add_item('cipher_letter')
    $ grant_achievement("secret_finder")

    """
    你走到那面灰尘有异动的书架前，手指沿着书脊滑过。在一排百科全书中间，有一本书的背脊比其他书稍微突出了一点。

    你将它抽出——书的封面上没有标题，只有一枚圆形印章。{color=#d4a853}书是中空的。{/color}

    里面藏着一封信，信纸上写满了看似毫无意义的字符组合。你翻到信纸背面，看见一行小字：\n          {color=#d4a853}「圆锁圆开，血引路来」{/color}

    这是某种暗号的提示。你将信纸小心折好收入口袋。

    {color=#d4a853}◆ 获得物品：密信{/color}
    """

    call check_collector_achievement

    jump library

label read_book:
    $ state.set_flag('found_book')
    $ state.add_item('old_key')

    """
    你走到书桌前，翻看那几本书。大部分是关于植物学和天文观测的专著，书页间夹着许多手写的批注——字迹潦草但有力，像是在与什么人辩论。

    在最下面一本书中，你发现了一封夹在书页间的信：

    {color=#c8b897}「柘远吾友：\n    你所追查之事，我劝你到此为止。那扇门后的东西，不是此世之物。我已见过太多因此消失的人。\n    若你还有一丝理智，锁好地窖，永远不要再下去。\n    切切。—— 一鹤」{/color}

    信纸下面压着一把古铜色的钥匙，似乎已经在这里躺了很多年了。

    {color=#d4a853}◆ 获得物品：生锈的旧钥匙{/color}
    """

    call check_collector_achievement

    jump library

# ═══════════════════════════════════════
# 图书馆深入搜索（新场景）
# ═══════════════════════════════════════

label library_search:
    $ state.set_flag('library_searched')

    """
    你沿着圆形墙壁慢慢走着，手指拂过一排排书脊。{color=#8a7b6b}大部分书都是十九世纪末到二十世纪初的版本，保养良好但极少被翻阅的痕迹。{/color}

    你停在了一个书架前。这一排全是关于民间信仰和巫术仪式的研究著作——《远东秘仪考》《圆形法阵与降灵术》《血契：古代中国的人祭记录》。

    {color=#8a7b6b}这些书被翻阅得最多，书脊已经起了毛边。有人在反复查阅这些内容。{/color}

    你抽出一本，翻到夹了书签的一页。书签是一张旧照片的碎片——只拍到了一只手，手指上戴着一枚刻有圆形符号的戒指。

    {color=#c8b897}与信封蜡封上的符号一模一样。{/color}
    """

    jump library

# ═══════════════════════════════════════
# 书房
# ═══════════════════════════════════════

label study:
    $ state.visit('study')
    scene bg study
    with dissolve

    """
    书房比图书馆小得多，但布置更有人情味。

    壁炉里的灰烬尚有余温。一张红木书桌上摆着墨水瓶、钢笔和一本摊开的笔记——{color=#8a7b6b}钢笔的笔帽没有合上，墨水已经干涸。写字的人像是匆忙离开的。{/color}

    书桌后方的墙上一幅人物肖像画有些歪斜，似乎被人动过。一侧有一个老式保险柜。落地窗前，月光如水银泻地。

    {color=#8a7b6b}这个房间的主人离开得很急——连壁炉的火都没来得及添柴。{/color}
    """

    menu:
        "翻看书桌上的笔记" if not state.has_flag('found_diary'):
            jump desk
        "检查墙上那幅歪斜的肖像画" if not state.has_flag('found_cellar_key'):
            jump portrait
        "检查保险柜" if state.has_item('old_key'):
            "你将生锈的旧钥匙插入保险柜的锁孔——咔哒一声，柜门开了。里面空荡荡的，只有一张发黄的旧照片：两个年轻男子站在庄园门前。照片背面写着：「柘远与一鹤，建庄十年志。」"
            jump study
        "将密信与日记对照分析" if state.has_item('cipher_letter') and state.has_item('diary') and not state.has_flag('cipher_decoded'):
            jump cipher_decode
        "返回大厅":
            jump hall

label desk:
    $ state.set_flag('found_diary')
    $ state.add_item('diary')
    $ grant_achievement("diary_reader")

    """
    你翻开桌上的笔记本。这不是普通的笔记——这是一本日记。

    最后一篇的日期是三个月前：

    {color=#c8b897}「我越来越确信，这座庄园的地下埋着什么东西。不是尸体，不是宝藏——而是某种古老的、有生命的东西。\n    一鹤说我疯了。也许他说得对。但那天晚上在地窖里看到的光……那不是幻觉。\n    明天我要再次下去。这次我会带上相机。如果我没有回来——」{/color}

    {color=#8a7b6b}字迹在这里戛然而止。{/color}

    你翻到日记的第一页，上面写着一个名字：{color=#d4a853}李柘远{/color}——这座庄园的主人。

    {color=#d4a853}◆ 获得物品：陈旧的日记本{/color}
    """

    call check_collector_achievement

    jump study

label portrait:
    $ state.set_flag('found_cellar_key')
    $ state.add_item('cellar_key')

    """
    你走到那幅歪斜的肖像画前——画中是一个神情严肃的中年男子，眉宇间有一股阴郁之气。画框边缘有一道不易察觉的缝隙。

    {color=#8a7b6b}你伸手推开画框。{/color}

    画后的墙壁上露出一个浅浅的暗格。暗格里放着一枚铁钥匙，柄上刻着一个圆形符号。

    钥匙下面压着一张纸条，只有两个字：\n          {color=#cc5555}「別開。」{/color}

    字迹颤抖，仿佛写字的人手在发抖。

    {color=#d4a853}◆ 获得物品：地窖钥匙{/color}
    """

    call check_collector_achievement

    jump study

# ═══════════════════════════════════════
# 密信解读（新场景）
# ═══════════════════════════════════════

label cipher_decode:
    $ state.set_flag('cipher_decoded')

    """
    你坐在书房的书桌前，将密信和日记并排放在台灯下。

    密信上的字符初看毫无意义——但当你将日记中反复出现的几个关键词（{color=#d4a853}「地窖」「门」「灵」「圆」{/color}）与密信上的符号逐行对比时，一个规律浮现了。

    {color=#c8b897}这不是密码——这是音译。{/color}每一个符号对应一个音节，而那个圆形符号反复出现在每个句子的末尾——它不是什么文字，{color=#d4a853}它是一个终止符。{/color}用来结束一个仪式步骤的标记。

    你按照发音规律将整封信译了出来：

    {color=#c8b897}「一人入阵，以血为约。\n圆环不破，灵不可出。\n若阵中无人，门启于子时。\n门启则灵至，灵至则雾生，雾生则万物为牢。」{/color}

    末尾还有一行字，笔迹与前面不同——更端正，更用力：

    {color=#d4a853}「余，李柘远，第五代守门人。今留此书，以告后来者：\n法阵需以生者之血维系。吾去矣。后来者自择。」{/color}

    {color=#8a7b6b}你放下译稿，指尖冰凉。李柘远早就知道——他下地窖不是去探索。他是去赴死的。{/color}
    """

    jump study

# ═══════════════════════════════════════
# 花园
# ═══════════════════════════════════════

label garden:
    $ state.visit('garden')
    scene bg garden
    show mist_heavy
    with dissolve

    """
    荒芜的花园在月光下有一种诡异的美感。

    曾经修剪整齐的灌木如今已经疯长，小径被杂草覆盖。花园中央有一座石砌喷泉，池水早已干涸——{color=#8a7b6b}池底铺满了深色的落叶，像是某种祭坛的遗迹。{/color}

    远处有一座玻璃温室，在月光下泛着幽幽的绿光。几只萤火虫在草丛间明灭不定——{color=#8a7b6b}但你看清楚了：那不是萤火虫。那是从温室方向飘来的、微小的绿色光点。{/color}
    """

    menu:
        "检查干涸的喷泉" if not state.has_flag('checked_fountain'):
            jump fountain
        "前往温室查看" if not state.has_flag('girl_gone'):
            jump greenhouse
        "沿着小径深入花园" if not state.has_flag('garden_path'):
            jump garden_path
        "再次去温室找那个女孩" if state.has_flag('girl_gone') and not state.has_flag('girl_deep'):
            jump greenhouse_return
        "向若兰告别" if state.has_flag('girl_deep') and not state.has_flag('girl_farewell') and state.has_item('cellar_key'):
            jump girl_farewell
        "返回大厅":
            jump hall

label fountain:
    $ state.set_flag('checked_fountain')
    $ state.add_item('old_key')

    """
    你走到花园中央的喷泉前。池子里没有水，只有一层厚厚的落叶和淤泥。

    你蹲下身拨开落叶，在池底摸到一样冰凉的金属物——一把锈迹斑斑的钥匙。{color=#8a7b6b}它被精心地藏在池底最深的裂缝里，像是有人不希望它被轻易找到。{/color}

    {color=#d4a853}◆ 获得物品：生锈的旧钥匙{/color}
    """

    call check_collector_achievement

    jump garden

# ═══════════════════════════════════════
# 花园小径（新场景）
# ═══════════════════════════════════════

label garden_path:
    $ state.set_flag('garden_path')

    """
    你沿着一条几乎被杂草淹没的石板小径，向花园深处走去。

    小径两旁的石灯已经全部熄灭。藤蔓爬满了石灯的表面，从缝隙中长出细小的白花——{color=#8a7b6b}在月光下显得格外苍白，像是小小的指骨。{/color}

    小径的尽头是一堵长满苔藓的石墙。墙面上爬着一棵枯萎的紫藤，枝条如血管般盘旋。石墙中央嵌着一扇铁门——已经锈死了。

    铁门上又出现了那个圆形符号。{color=#d4a853}这一次它被刻得很深，像是用尽全力凿出来的。{/color}
    """

    jump garden

# ═══════════════════════════════════════
# 温室
# ═══════════════════════════════════════

label greenhouse:
    $ state.set_flag('met_girl')
    scene bg greenhouse
    show firefly
    show mist_heavy
    with dissolve

    show char girl at right_enter
    with dissolve

    """
    你推开温室斑驳的玻璃门，一股温湿的空气扑面而来。

    温室里长满了各种植物——有些已经枯萎，有些却在疯狂生长。破碎的玻璃顶棚透下斑驳的月光。{color=#88ff88}微小的绿色光点在你周围飘浮，像是被惊扰的萤火。{/color}

    在植物丛中，你看见一个人影——一个年轻的女孩，约莫十七八岁，穿着白色的长裙，赤着脚站在泥土中。

    她看到你，并不惊讶。

    {color=#d4a853}「你终于来了。我等你很久了。」{/color}

    她走上前来，目光清澈而坚定。{color=#c8b897}「我是李柘远的女儿。我知道你来这里是为了什么。父亲三个月前下了地窖，再也没有上来。」{/color}
    """

    menu:
        "问她为什么不离开这里":
            jump greenhouse_talk
        "告诉她你一定会查明真相":
            jump greenhouse_promise

label greenhouse_talk:
    hide char girl
    $ state.add_item('jade_token')
    $ state.set_flag('girl_gone')

    detective "「为什么不离开？」"

    "女孩苦笑着摇了摇头。"

    girl_char "「我走不了。这座庄园……它不允许我离开。每次我走到大门口，都会有一股浓雾将我逼回来。」"

    "她看着你，眼神中有一丝怜悯："

    girl_char "「你现在也走不了了。除非——你在地窖里找到那东西，并且做出正确的选择。」"

    """
    她将手伸进口袋，取出一枚圆形玉坠，放在你手心——触手温润，仿佛有体温。
    """

    girl_char "「这个给你。它也许能保护你。」"

    """
    {color=#d4a853}◆ 获得物品：玉坠{/color}

    女孩微微一笑，转身消失在植物丛中。
    """

    call check_collector_achievement
    hide firefly
    hide mist_heavy

    jump garden

label greenhouse_promise:
    hide char girl
    $ state.add_item('jade_token')
    $ state.set_flag('girl_gone')

    """
    {color=#c8b897}「查明真相……」{/color}女孩低垂着眼帘。{color=#d4a853}「我父亲也曾说过同样的话。他查了二十年，最后把自己查进了地窖。」{/color}

    她抬起头，看着你：{color=#d4a853}「但你是不同的——我看见你身上有光。」{/color}

    她从颈上取下一枚玉坠，递给你。{color=#d4a853}「拿着吧。这是我父亲留给我的，据说能辟邪。你比我更需要它。」{/color}

    她转身走向温室深处，身影渐渐隐没。{color=#8a7b6b}「小心。那扇门后的东西，会看穿你的心。」{/color}

    {color=#d4a853}◆ 获得物品：玉坠{/color}
    """

    call check_collector_achievement
    hide firefly
    hide mist_heavy

    jump garden

# ═══════════════════════════════════════
# 温室再访 — 女孩的回忆（新场景）
# ═══════════════════════════════════════

label greenhouse_return:
    $ state.set_flag('girl_deep')
    scene bg greenhouse
    show firefly
    show mist_heavy
    with dissolve

    show char girl at center_stand
    with dissolve

    """
    你再次推开温室的玻璃门。

    她还站在那里——仿佛从未离开过。{color=#8a7b6b}也可能她确实没有离开过。{/color}

    她看着你手里的日记本，目光柔和了几分。{color=#d4a853}「你找到了我父亲的日记。这是最后他留下的东西。」{/color}

    她走近了几步，月光透过碎玻璃落在她的脸上。{color=#d4a853}「你知道这座庄园最初是谁建造的吗？不是什么贵族——是一个叫顾北川的学者。1892年，他从某个古墓里带回了一块刻着圆形符号的石板。」{/color}

    {color=#d4a853}「石板上的文字他研究了二十年。最后他得出结论——那个圆形符号不是文字，而是一道「门」。一道通往某个……地方的门。」{/color}

    她停顿了一下，声音更轻了：{color=#d4a853}「顾北川建了这座庄园，把石板埋在地底，然后在上面盖了一座法阵来镇住它。但法阵不是永久的——每一代都需要有人主动进入阵眼，成为「灵」的新容器。否则，门就会打开。」{/color}

    {color=#c8b897}「我父亲是第五代。」{/color} 她的声音有些颤抖了。{color=#d4a853}「他下地窖的那天晚上，跟我说：『如果天亮前我还没上来，就写信给那个侦探。他会来的。』」{/color}

    你沉默了很久。最后开口问道：{color=#c8b897}「他为什么选我？」{/color}

    女孩微微一笑。{color=#d4a853}「因为你不会拒绝一个需要帮助的人。他认为这是唯一的优点，也是唯一需要的东西。」{/color}
    """

    hide char girl
    hide firefly
    hide mist_heavy

    jump garden

# ═══════════════════════════════════════
# 女孩告别（新场景）
# ═══════════════════════════════════════

label girl_farewell:
    $ state.set_flag('girl_farewell')
    scene bg greenhouse
    show firefly
    with dissolve

    show char girl at center_stand
    with dissolve

    """
    你最后一次走进温室。若兰站在月光中，似乎一直在等你。

    {color=#d4a853}「你拿到了钥匙。」{/color} 她看着你的手。{color=#d4a853}「也拿到了日记。还有玉坠。你准备好了。」{/color}

    """

    girl_char "「我父亲下去之前，最后做了一件事——他站在这里，看着月光穿过碎玻璃落在我的脸上。」"

    """
    她的声音轻得像是雾气。

    """

    girl_char "「然后他说：『若兰，如果我成功了，这座庄园就会自由。如果我没有——下一个来的人会是一个侦探。告诉他——他只有一个机会。必须把玉坠放在阵眼，然后把所有符文倒过来读。那是封闭法阵的唯一方法。』」"

    """

    你默默记下了这句话。{color=#8a7b6b}所有符文倒过来读。{/color}

    """

    girl_char "「还有——」 她的眼睛突然湿润了。「如果你成功了，我会走出去。如果你失败了——请让下一个人知道，我叫若兰。我已经等了五年了。」"

    """

    你点了点头。没有说出任何承诺。你知道——如果失败了，可能再没有下一个人了。

    你转身走向宅邸，手中握着地窖钥匙，口袋里装着玉坠和日记。今晚的月亮格外明亮，像是有人在上面点了一盏灯。
    """

    hide char girl
    hide firefly
    jump garden

# ═══════════════════════════════════════
# 地下室
# ═══════════════════════════════════════

label basement:
    $ state.visit('basement')
    scene bg basement
    with dissolve

    """
    一扇厚重的铁门嵌在走廊尽头的墙壁中。门上没有把手，只有一个圆形的锁孔——{color=#d4a853}与你手中的地窖钥匙完美匹配。{/color}

    门上刻着一行字：\n          {color=#8a7b6b}「入此門者，當捨弃一切希望」{/color}

    但丁的诗句被刻在这里。{color=#8a7b6b}铁门表面冰冷，你伸手触碰时，感到一股微微的震动从门后传来——像是有什么东西在地底深处呼吸。{/color}
    """

    menu:
        "用地窖钥匙打开铁门":
            $ state.set_flag('opened_cellar')
            "钥匙插入锁孔——它转动得异常顺畅，仿佛昨天才被使用过。铁门发出一声沉闷的响声，缓缓打开。\n\n一股潮湿的、带着泥土气息的风从门内涌出。{color=#8a7b6b}那风中夹杂着一种你无法形容的气味——不是腐烂，更像是时间和空间本身在朽坏。{/color}"

            if state.has_flag('butler_spoke') and not state.has_flag('butler_warned'):
                jump butler_warning

            jump basement_corridor
        "返回大厅":
            jump hall

# ═══════════════════════════════════════
# 管家警告（新场景）
# ═══════════════════════════════════════

label butler_warning:
    $ state.set_flag('butler_warned')

    """
    你正要踏入铁门，身后传来一个沙哑的声音。

    {color=#c8b897}「你确定要下去？」{/color}

    管家不知何时出现在走廊里。他依旧面无表情，但那双浑浊的眼睛里似乎多了一丝什么——{color=#8a7b6b}也许是关切，也许只是好奇。{/color}

    butler_char "「我已经送走四代人了。顾北川是新郎官走进去的。第二代是半夜自己下去的。第三代写了一封遗书，放在你现在踩着的这块石板下面。秦一鹤跟我喝完了一整瓶酒。李柘远——他什么也没说，只是看了若兰一眼。」"

    {color=#c8b897}「你是第六个。可能也是最后一个。」{/color}

    他往后退了一步，半个身子隐没在走廊的阴影中。{color=#8a7b6b}「如果你回不来——我会把灯关掉的。」{/color}

    然后他转身走进了黑暗。脚步声逐渐远去，直到完全被地底传来的那种低沉震动所吞没。
    """

    jump basement_corridor

label basement_corridor:
    $ state.visit('basement_corridor')
    scene bg corridor
    with dissolve
    with vpunch

    """
    铁门之后，是一段向下延伸的石阶。墙壁上每隔几步插着一支火把，火焰呈不自然的幽蓝色，无声地跳动着。

    你沿着石阶向下走。空气越来越湿冷——{color=#8a7b6b}但奇怪的是，你并不感到害怕。相反，有一种莫名的吸引力在牵引着你前进，像是有人在你的意识深处低语。{/color}

    石阶尽头，一条长长的走廊向前延伸。走廊两侧的墙壁上画满了古老的壁画，在幽蓝的火光下忽明忽暗。走廊尽头有一扇石门，门缝中透出微弱的白光。

    {color=#8a7b6b}地面微微震动着，像是地底有什么巨大的心脏在跳动。{/color}
    """

    menu:
        "走向那扇发光的石门" if state.has_item('diary'):
            jump ritual_room
        "走向那扇发光的石门（需要更多线索）" if not state.has_item('diary'):
            "你向前走了几步，但心中忽然涌起一阵强烈的不安——你对这里一无所知，至少应该先了解更多再深入。"
            jump basement_corridor
        "仔细观察墙壁上的壁画":
            jump basement_wall
        "停下来感受周围的环境" if not state.has_flag('basement_fear'):
            jump basement_fear
        "转身返回":
            jump hall

# ═══════════════════════════════════════
# 地下室恐惧（新场景）
# ═══════════════════════════════════════

label basement_fear:
    $ state.set_flag('basement_fear')

    with vpunch

    """
    你停下了脚步。

    走廊里很静——{color=#cc5555}太静了。{/color}只有你自己的心跳声在耳中擂鼓。

    你回头看了一下来时的路。石阶上方，地下室那扇铁门已经自动合拢了。火把的幽蓝色火焰依旧无声地跳动着——但你注意到，{color=#cc5555}火把的数量比刚才多了。{/color}

    那些多出来的火把是谁点燃的？

    你深吸一口气。{color=#c8b897}你是侦探。你见过太多死者，太多谎言，太多黑暗的角落。但此刻，你第一次感到了某种超越理性和经验的恐惧。{/color}

    你咬紧牙关，继续向前。
    """

    jump basement_corridor

label basement_wall:
    $ state.set_flag('studied_wall')

    """
    你靠近墙壁，仔细端详那些壁画。

    壁画描绘了一个古老的仪式——一群人围成圆圈，圆圈中央有一道光柱直冲天际。光柱之中，一个模糊的影子在成形。

    {color=#8a7b6b}顺着壁画的顺序看下去：仪式成功了，但后果是灾难性的——参与仪式的人一个个倒下了，而那个影子变得越来越清晰。{/color}

    最后一幅壁画上，影子已经凝结成一个戴着面具的人形，它站在一座庄园前——正是这座庄园。

    壁画下方有一行褪色的文字：\n          {color=#d4a853}「門開則靈至，靈至則主易」{/color}

    {color=#8a7b6b}门打开，灵到来；灵到来，主人更换。{/color}你脊背一阵发凉。
    """

    menu:
        "走向那扇发光的石门" if state.has_item('diary'):
            jump ritual_room
        "返回走廊入口":
            jump basement_corridor

# ═══════════════════════════════════════
# 仪式厅
# ═══════════════════════════════════════

label ritual_room:
    $ state.visit('ritual_room')
    scene bg ritual
    show rune_spark
    with slow_fade

    if state.has_item('diary'):
        """
        你推开石门，走进一间圆形的地下大厅。

        穹顶足有三层楼高。墙壁上密密麻麻地刻满了发光的符文——数以百计的圆形符号同时发出幽蓝色的微光，像是一片星海被压缩到了四面墙壁上。

        大厅中央的地面上刻着一个巨大的圆形法阵。法阵中心躺着一具骸骨——从那件衣服的样式来看，应该就是庄园主人，{color=#d4a853}李柘远。{/color}

        他手中握着一封信。

        墙上的铭文写道：\n        {color=#d4a853}「圓環之靈，以血為契。舊主逝去，新主繼立。若無繼者，門不得閉；門若不閉，霧不可散。」{/color}

        你明白了。{color=#c8b897}这座庄园建立在一个古老的仪式法阵之上。每一代主人都必须镇守这扇「门」。当主人逝去，必须有新的人继承——否则门将永远打开，迷雾将永远笼罩。{/color}

        你握紧了日记本。李柘远在最后一篇日记中写道：「如果我回不来……」

        你知道自己该怎么做了。
        """
    else:
        """
        你推开石门，走进一间圆形的地下大厅。

        穹顶高耸，墙壁上密密麻麻地刻满了发光的符文。大厅中央有一个巨大的圆形法阵，法阵中心躺着一具骸骨。

        {color=#8a7b6b}你不完全理解这里的一切。但你本能地感到——你必须做一个选择。{/color}
        """

    menu:
        "拾起骸骨旁的信，按照仪式程序封闭法阵" if state.has_item('diary'):
            "你拾起那封信。上面详细记录了封闭法阵的步骤。借着日记中记录的线索，你开始一项项拆除符文……"
            jump ending_truth
        "将玉坠放入法阵中心" if state.has_item('jade_token') and not state.has_item('diary'):
            "你将玉坠放入法阵中心……"
            jump ending_master
        "握着玉坠，走入法阵中央" if state.has_item('jade_token') and state.has_item('diary'):
            "你一手握着日记，一手握着玉坠，走向法阵中央。你知道还有一个选择——代替李柘远，成为这座庄园的新主人。\n\n{color=#d4a853}不是为了权力。是为了守护。{/color}"
            jump ending_master
        "闭上双眼，触碰法阵核心" if state.has_item('jade_token') and state.has_flag('cipher_decoded') and not state.has_flag('had_vision'):
            jump ritual_vision
        "你感到恐惧，转身逃离":
            jump ending_escape
        "好奇心驱使，你触碰了法阵中心的符文" if not state.has_item('jade_token') and not state.has_item('diary'):
            jump ending_trapped

# ═══════════════════════════════════════
# 仪式幻象（新场景）
# ═══════════════════════════════════════

label ritual_vision:
    $ state.set_flag('had_vision')
    show rune_spark
    with vpunch

    """
    你闭上双眼。

    瞬间——{color=#8a7b6b}不，甚至不到瞬间。{/color}

    你的意识被卷入了一个漩涡。符文的光芒穿透你的眼皮，在黑暗中织出一幅幅画面：

    {color=#c8b897}第一幅{/color}——一个穿着清朝长衫的学者（顾北川）跪在一座古墓中，面前是一块裂开的石板，石板上刻着圆形符号。他的嘴唇在动，但没有声音。

    {color=#c8b897}第二幅{/color}——同一个学者站在正在建造的庄园前，手里托着那块石板。他的脸上满是恐惧，但也有一丝决然。

    {color=#c8b897}第三幅{/color}——一个又一个不同时代的人，走入地窖，走入法阵，走入光中。有些是老人，有些还很年轻。但他们的神情都一样：{color=#8a7b6b}不是恐惧，而是释然。{/color}

    {color=#c8b897}第四幅{/color}——李柘远。他坐在你现在坐的位置——同样的日记本，同样的台灯，同样的犹豫。然后他站起身，拿起地窖钥匙，向地窖走去。

    {color=#d4a853}第五幅{/color}——{color=#d4a853}是一个空白的画面。{/color}没有任何人。法阵还在，但阵眼是空的。门开了。

    然后你看到了——{color=#cc5555}门外的景象。{/color}

    那不是地狱，不是虚无。那是纯粹的、绝对的、吞噬一切的黑暗，正在向四面八方延伸。迷雾庄园只是它触碰到这个世界的第一个点。

    {color=#8a7b6b}第五幅画面消失了。{/color}

    你睁开眼睛，发现自己还跪在法阵前，冷汗湿透了衬衫。玉坠在你手心里烫得灼人。

    {color=#c8b897}你现在明白了——逃避不是选项。从来都不是。{/color}
    """

    hide rune_spark

    jump ritual_room

# ═══════════════════════════════════════
# 结局 1：真相大白
# ═══════════════════════════════════════

label ending_truth:
    scene bg black
    show bg manor at slow_zoom
    with slow_fade

    $ unlock_ending("truth")
    $ grant_achievement("truth_seeker")
    if persistent.endings_seen.__len__() >= 4:
        $ grant_achievement("all_endings")

    "{size=+18}{color=#d4a853}真 相 大 白{/color}{/size}"

    """你按照信中的指引，一步步拆解了法阵。

    当最后的符文黯淡下去时，整座庄园发出一声长长的叹息——墙壁上的光芒渐渐消散，大厅里传来的钟声敲响了十二下。

    你走出地窖，惊讶地发现迷雾已经散去。月光清澈如水，洒在庄园的每一个角落。温室旁，那个女孩正站在那里，微笑着向你点头。{color=#d4a853}她不再是困在庄园中的囚徒——她自由了。{/color}

    你带着日记和信函离开了庄园。第二天，你将所有证据交给了报社。「迷雾庄园」的秘密震惊了整座城市——一段跨越百年的黑暗历史，终于被公之于众。

    一个月后，你收到了一封没有署名的信，里面只有一张照片：那座庄园正在被拆除，阳光照在曾经被迷雾笼罩的土地上。

    照片背后写着一行字：\n          {color=#d4a853}「霧散月明，萬事歸清。」{/color}

    {color=#8a7b6b}—— 真相大白结局 ——{/color}
    """

    jump game_end

# ═══════════════════════════════════════
# 结局 2：逃离庄园
# ═══════════════════════════════════════

label ending_escape:
    scene bg black
    with slow_fade

    $ unlock_ending("escape")
    $ grant_achievement("escape_artist")
    if persistent.endings_seen.__len__() >= 4:
        $ grant_achievement("all_endings")

    "{size=+18}{color=#8a7b6b}逃 离 庄 园{/color}{/size}"

    """你转身就跑。

    跑过走廊，跑上石阶，跑过大厅，跑出大门。你的车还停在原处，引擎一打就着了。

    你踩下油门，庄园在后视镜中越来越小，最终消失在浓雾之中。{color=#8a7b6b}你安全了。{/color}

    但你永远也不会知道那座庄园的地下藏着什么。也许这样也好——有些秘密，不知道反而是一种幸运。

    只是有时候，在深夜失眠的时候，你会想起那个温室里的女孩。她还在那里吗？还在等下一个访客吗？

    {color=#8a7b6b}你关了灯，不再想了。{/color}

    {color=#8a7b6b}—— 逃离庄园结局 ——{/color}
    """

    jump game_end

# ═══════════════════════════════════════
# 结局 3：永远困住
# ═══════════════════════════════════════

label ending_trapped:
    scene bg black
    with slow_fade

    $ unlock_ending("trapped")
    $ grant_achievement("trapped_soul")
    if persistent.endings_seen.__len__() >= 4:
        $ grant_achievement("all_endings")

    "{size=+18}{color=#cc5555}永 远 困 住{/color}{/size}"

    """你触碰法阵中符文的瞬间，所有幽蓝色的光芒突然变得刺目。

    一股强大的力量将你吸向法阵中心。你感到自己在坠落——不是向下，而是向某个无法名状的方向。

    {color=#cc5555}「又一位访客。欢迎来到永恒的迷雾。」{/color}

    当你再次睁开眼睛时，你发现自己站在庄园的大门外。但与之前不同——你无法触碰门环，无法发出声音。你低头看向自己的双手——它们正在变得透明。

    你成为了庄园的一部分。{color=#8a7b6b}你将在迷雾中永远徘徊，看着下一个访客的到来——像管家曾经做的那样，像这座庄园所有迷失的灵魂一样。{/color}

    {color=#cc5555}—— 永远困住结局 ——{/color}
    """

    jump game_end

# ═══════════════════════════════════════
# 结局 4：庄园之主
# ═══════════════════════════════════════

label ending_master:
    scene bg black
    show bg manor at slow_zoom
    with slow_fade

    $ unlock_ending("master")
    $ grant_achievement("new_master")
    if persistent.endings_seen.__len__() >= 4:
        $ grant_achievement("all_endings")

    "{size=+18}{color=#d4a853}庄 园 之 主{/color}{/size}"

    """你走入法阵中央，将玉坠放置在阵眼之上。

    符文的光芒骤然大盛，又在一瞬间归于平静。你感到一阵奇异的暖流从脚底升起，流遍全身——那是与整座庄园血脉相连的感觉。

    你能「感觉」到每一个房间，每一块砖石，每一寸土地。{color=#d4a853}你能「感觉」到大门外的雾正在缓缓收拢，退回到地底深处。{/color}

    你成为了这座庄园的新主人。

    你走出地窖，天已经蒙蒙亮了。温室旁的女孩正站在喷泉边等你。{color=#d4a853}「看来你已经做出了选择。」{/color}她轻声说。

    你点了点头。这座庄园不再是一个牢笼——在传承了百年的诅咒之后，你成为了第一个自愿接过重任的人。

    {color=#d4a853}—— 庄园之主结局 ——{/color}
    """

    jump game_end

# ═══════════════════════════════════════
# 游戏结束
# ═══════════════════════════════════════

label game_end:

    python:
        all_scenes = ['hall', 'hall_explore', 'butler_encounter',
                      'master_bedroom', 'dining_hall',
                      'library', 'bookshelf', 'read_book', 'library_search',
                      'study', 'desk', 'portrait', 'cipher_decode',
                      'garden', 'fountain', 'garden_path',
                      'greenhouse', 'greenhouse_talk', 'greenhouse_promise',
                      'greenhouse_return', 'girl_farewell',
                      'basement', 'basement_corridor', 'basement_fear',
                      'basement_wall', 'butler_warning',
                      'ritual_room', 'ritual_vision']
        visited_all = all(state.visited(s) > 0 for s in all_scenes)
        if visited_all:
            grant_achievement("explorer")

    ""

    menu:
        "重新开始":
            $ state = GameState()
            jump start
        "返回标题":
            return

# ═══════════════════════════════════════
# 辅助
# ═══════════════════════════════════════

label check_collector_achievement:
    if len(state.inventory) >= 5:
        $ grant_achievement("collector")
    return
