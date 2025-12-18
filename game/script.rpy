define config.default_fullscreen = True 

define gui.text_font = "gui/fonts/LXGWWenKai-Light.ttf"
define gui.name_text_font ="gui/fonts/LXGWWenKai-Bold.ttf"

define m0 = Character("???",who_color="#c8c53c")

define r0 =Character("??",who_color="#c84a3c")

define a0 = Character("???",who_color="#3cc8c8")

define k0 = Character("??",who_color="#c87b3c")

define s0 = Character("??",who_color="#3c90c8")

define y0 = Character("?",who_color="#bababa")

define rm0 = Character("????",who_color="#c83c43")

define m = Character(_("雾雨 魔理沙"),who_color="#c8c53c")

define re = Character(_("博丽 灵梦"),who_color="#c84a3c")

define k = Character(_("本居 小铃"),who_color="#c87b3c")

define a = Character(_("爱丽丝 玛格特罗依德"),who_color="#3cc8c8")

define y = Character(_("射命丸 文"),who_color="#bababa")

define s = Character(_("十六夜 咲夜"),who_color="#3c90c8")

define rm = Character(_("蕾米莉亚 斯卡蕾特"),who_color="#c83c43")

define p = Character(_("帕秋莉 诺蕾姬"),who_color="#b35edb")

image splash = "logo 1.png"

transform disappear:
    alpha 0.0

transform slowdisappear:
    linear 0.5 alpha 0.0

transform fadeInLeft:
    alpha 0.0
    xalign 0.15 
    yalign 1.0  
    zoom 0.75  
    linear 1.0 alpha 1.0

transform fadeInLeftMiddle:
    alpha 0.0
    xalign 0.4 
    yalign 1.0  
    zoom 0.75  
    linear 1.0 alpha 1.0

transform fadeInRightMiddle:
    alpha 0.0
    xalign 0.6 
    yalign 1.0  
    zoom 0.75  
    linear 1.0 alpha 1.0

transform fadeInRight:
    alpha 0.0
    xalign 0.85  
    yalign 1.0 
    zoom 0.75   
    linear 1.0 alpha 1.0

transform afadeInRight:
    alpha 0.0
    xalign 0.95  
    yalign 1.0 
    zoom 0.9   
    linear 1.0 alpha 1.0

transform rightToMiddle:
    xalign 0.85
    linear 1.0 xalign 0.6

transform leftToMiddle:
    xalign 0.15
    linear 1.0 xalign 0.4

transform middleToRight:
    xalign 0.6
    linear 1.0 xalign 0.85

transform middleToLeft:
    xalign 0.4
    linear 1.0 xalign 0.15

transform moveInRight:
    zoom 0.75 
    xalign 1.33
    yalign 1.0
    linear 1.0 xalign 0.85

transform moveInLeft:
    zoom 0.75 
    xalign -0.33
    yalign 1.0
    linear 1.0 xalign 0.15

transform rmiddle:
    zoom 0.75
    xalign 0.6
    yalign 1.0

transform lmiddle:
    zoom 0.75
    xalign 0.4
    yalign 1.0

transform right:
    zoom 0.75
    xalign 0.85
    yalign 1.0

transform aright:
    zoom 0.9
    xalign 0.95
    yalign 1.0

transform left:
    zoom 0.75
    xalign 0.15
    yalign 1.0

transform rightMoveOut:
    xalign 0.85
    linear 1.0 xalign 1.33

transform arightMoveOut:
    xalign 0.95
    linear 1.0 xalign 1.5

transform leftMoveOut:
    xalign 0.15
    linear 1.0 xalign -0.33

transform rightFadeOut:
    zoom 0.75
    xalign 0.85
    yalign 1.0
    linear 1.0 alpha 0.0

transform leftFadeOut:
    zoom 0.75
    xalign 0.15
    yalign 1.0
    linear 1.0 alpha 0.0

label splashscreen:
    scene black
    with Pause(0.5)

    show splash with dissolve
    with Pause(1)

    scene black with dissolve
    with Pause(0.5)

    return

label start:
    $_dismiss_pause=False
    $ renpy.music.stop(fadeout=1.0)
    $ renpy.pause(1.0, hard=True)
    $ style.say_dialogue.xalign = 0.5
    $ style.say_dialogue.yalign = 0.5

    show text "東方プロジェクトガイドライン\nby 上海アリス幻樂団\n\n本ガイドラインは博麗神主ZUN氏が日本において頒布した諸規定を基に整理され、上海アリス幻樂団の承認を経て公開されたものです。\n\n本ゲームはこれらの規定に従います。" with Fade(1.0, 2.0, 1.0)
    $ renpy.pause(2.0, hard=True)
    scene bg black with fade
    $ renpy.pause(1.0, hard=True)

    play music "the festival.mp3" fadein 5
    scene bg black

    "..."

    "..."

    m0"呃..."

    voice "voice/marisa1.wav"
    m0"我说，灵梦啊，"

    r0"什么？"

    voice "voice/marisa2.wav"
    m0"今天街上怎么这么热闹？"

    r0"今天..."


label village:
    $_dismiss_pause=False
    scene bg village with fade
    $ renpy.pause(1.0, hard=True)

    "人间之里的景象显得与平日不同。"

    "随风舞动的五光十色的灯笼，如同星星点点，悬挂在古老的房檐下，又或是树梢间，为这幽静的村庄穿上了盛装。"

    voice "voice/marisa3.wav"
    m"话说..."

    voice "voice/marisa4.wav"
    m"平日里街上有这么热闹吗？"

    show reimu 2 at fadeInRight
    $ renpy.pause(1.0, hard=True)

    re"..."

    "木质的招牌下，传来了香甜的糖葫芦和热腾腾的烤红薯的香味，"

    "让每一个经过的人都忍不住驻足。"

    k0"诶诶，你们不知道吗？"

    show reimu 2 at rightToMiddle
    show kosuzu 1 at moveInRight
    
    "香甜的团子气息从小铃手中的木碟上飘荡出来。"

    "很好闻，让人有想吃的欲望。"

    k"灵梦小姐，请用！"

    show reimu 7 at rmiddle

    "灵梦毫不犹豫地接过了团子，优雅地品尝了一口。"

    show kosuzu 6 at right

    k"今晚要举行花火祭啊，"

    "小铃双手交叉，显然对这个节日充满了期待。"

    k"几乎全村的人都会参加，当然也包括外面的人们。"

    k"花火祭是幻想乡的每个人都盼望的盛大节日喔！"

    show kosuzu 1 at right

    "灵梦小姐满意地嚼着团子。"

    m"嗯..."

    voice "voice/marisa5.wav"
    m"啊，去年有举办过这种活动吗？"

    show reimu 1 at rmiddle
    show kosuzu 6 at right

    k"灵梦小姐和魔理沙小姐也会来的对吧？我们都很期待！"

    show reimu 13 at rmiddle
    show kosuzu 1 at right

    re"是啊..."

    re"..."

    show reimu 7 at rmiddle

    re"我也一直期待着呢。"
    
    m"..."


label undertheroof:
    $_dismiss_pause=False
    scene bg black with fade
    $ renpy.pause(1.0, hard=True)
    play sound "rain.mp3" loop
    $ renpy.pause(1.0, hard=True)

    "..."
    
    voice "voice/marisa6.wav"
    m"我说灵梦啊，花火祭在雨天也能办吗？"

    scene bg roof with fade
    $ renpy.pause(1.0, hard=True)

    re"如果只是小雨的话。"

    show marisa 16 at fadeInRight
    $ renpy.pause(1.0, hard=True)

    m"..."

    re"...大到这个份上我估计多半是没戏了。"

    re"嗯..."

    re"本来是打算放烟花的。"

    "灵梦望着外面。"

    m"呃..."

    show marisa 19 at right

    voice "voice/marisa7.wav"
    m"嘛，干脆找几个人拿着焰火，"

    voice "voice/marisa8.wav"
    m"直接飞到天上点火如何？咚的一声。"

    re"会烧起来的吧。"

    voice "voice/marisa9.wav"
    m"靠雨水来灭火啊。"

    show marisa 16 at right

    m"..."

    m"灵梦，"

    m"诶诶，该我抽牌了，"

    show marisa 27 at right

    m"...灵梦？"

    m"..."

    voice "voice/marisa10.wav"
    m"喂...听得见吗？"

    m"该-我-抽-牌-了！"

    "灵梦突然回过神来。"

    show marisa 16 at right

    voice "voice/marisa11.wav"
    m"怎么了？突然发起呆来。"

    re"..."

    re"抱，抱歉，没什么..."

    "灵梦重新将视线转到手中的牌上。"

    "理了理牌，犹豫着出哪一张。"

    re"...看样子应该会下一整天吧。"

    re"明明人家还蛮期待的。"

    m"..."

    m"诶，意外啊，灵梦竟然会期待焰火什么的。"

    re"意外是什么意思啊。"

    m"..."

    m"。"
    
    voice "voice/marisa12.wav"
    m"不好意思，突然有点急事。"

    re"诶，冒着这么大的雨吗？"

    m"..."

    show marisa 25 at right

    m"啊啊，是必须马上办的事情。"

    "魔理沙戴上帽子，骑上扫帚离开了神社。"


label choice:
    $_dismiss_pause=False
    scene bg black with fade
    $ renpy.pause(1.0, hard=True)
    $ renpy.music.stop(fadeout=1.0)
    $ renpy.pause(1.0, hard=True)
    show marisa 2 at fadeInLeft
    $ renpy.pause(1.0, hard=True)

    m"(灵梦一定很想看今晚的花火祭吧...)"

    m"(但是雨下个不停...)"

    show marisa 14 at left

    m"(我需要找人帮忙。)"

    show marisa 2 at left

    m"(魔法森林的深处是爱丽丝的宅邸)"

    m"(爱丽丝身为魔法使，说不定能帮上忙)"

    m"(而雾之湖的另一畔是蕾米莉亚的洋馆)"

    m"(红魔馆的人们各有特点，或许能派上用场)"

    menu:
        m"(我应该去...)"

        "魔法森林":
            $ player_choice = 1
            jump choice1

        "红魔馆":
            $ player_choice = 2
            jump choice2


label choice1:
    $_dismiss_pause=False
    $ renpy.music.stop(fadeout=1.0)
    $ renpy.pause(1.0, hard=True)
    play music "faith.mp3" fadein 5

    m"嗯..."

    voice "voice/marisa13.wav"
    m"决定了，我这就去拜访爱丽丝的宅邸。"

    show marisa 2 at leftFadeOut
    $ renpy.pause(1.0, hard=True)

    "..."

    a0"...谁在敲门？"

    m"...魔理沙。"

    "门应声而开。"

    $ renpy.pause(1.0, hard=True)
    scene bg alice with fade
    $ renpy.pause(1.0, hard=True)

    a"这么大的雨..."

    a"..."

    a"浑身都湿透了呢。"

    "爱丽丝起身向壁炉里添加了一些燃料。"

    "温暖的炉火或许能更快地烘干身上的水分。"

    voice "voice/marisa14.wav"
    m"没关系的ZE..."

    a"说吧。"

    a"...冒着这么大的雨来我家，是有什么事情吗？"

    m"爱丽丝，今晚有花火祭你知道吧。"

    a"嗯。"

    "魔理沙从口袋中拿出一些类似石头的东西。"

    voice "voice/marisa15.wav"
    m"你知道这是什么吗？"

    "很显然，那些不是路边普通的石头，因为它们不会有如此规整的形状。"

    a"我看看，你先擦擦头发。"

    a"这是..."

    a"...魔石？"

    a"...如果我没看错的话，这是一种注入魔力就会发光发热的晶体。"

    a"通常被称为魔石。"

    voice "voice/marisa16.wav"
    m"嗯嗯，看的很准嘛。"

    a"难道说，这是今天的烟花的替代品？"

    m"正是如此。"

    voice "voice/marisa17.wav"
    m"光凭我一个人的力量肯定点亮不了这么多魔石..."

    m"所以今天晚上,"

    m"和我一起注入魔力点亮它们吧！"

    a"..."

    a"雨这么大，光是到场就不会有多少人的吧..."

    a"明年再去也是可以的哦。"

    voice "voice/marisa18.wav"
    m"我想现在看。"

    a"明年不行吗。"

    m"现在能看到的东西，只有现在才能看到。"

    m"所以拜托了就这样吧。"

    a"...你们对这种事情，真是在意啊。"

    scene bg ralice with fade
    $ renpy.pause(1.0, hard=True)

    "爱丽丝来到窗边，望着宅邸上方滴落的雨。"

    "雨珠前后相连，形成了一串又一串的雨纱，如同帷幕层层铺叠而开。"

    "没有丝毫停的迹象，反而愈演愈烈。"

    a"..."

    a"真是麻烦啊。"

    a"..."

    a"你有在听吗..."

    a"...魔理沙?"

    "魔理沙微微蜷缩着身体，靠在壁炉边的沙发上，"

    "闭着眼睛，看样子应该绝对是睡着了。"

    a"搞什么啊。"

    a"莫名其妙来我家，又莫名其妙地在我家睡着.."

    a"就像夏日的阵雨一样..."

    "爱丽丝近距离感受着魔石的魔力。"

    a"..."

    a"..."

    a"嗯..."

    a"...红魔馆的气息?"

    "魔石和爱丽丝以往见到的那些略有不同。"

    "上面有那位来自红魔馆的大魔法使的印记。"

    "而且外观过于灰暗，就像是..."

    a"...就像是被谁一次又一次注入过魔力，"

    a"但又不足以将其完全点亮的后果一样..."

    scene bg black with fade
    $ renpy.pause(1.0, hard=True)

    "..."

    m"..."

    m"。"

    m"!"

    show marisa 23 at right

    m"现在几点了？"

    show marisa 22 at right

    voice "voice/marisa19.wav"
    m"爱丽丝，现在几点了？"

    a"...祭典的两个小时前。"

    show marisa 26 at right

    m"...还好。"

    m"还来得及。"

    "爱丽丝走上前来，将烘干的魔女帽戴在魔理沙头上。"

    show marisa 2 at right

    a"快点准备好，去吧。"

    m"..."

    show marisa 11 at right
    voice "voice/marisa20.wav"
    m"当然...我先走了！"

    "魔理沙骑上扫帚，以最快的速度飞进了窗外的大雨中。"

    jump rvillage


label choice2:
    $_dismiss_pause=False
    $ renpy.music.stop(fadeout=1.0)
    $ renpy.pause(1.0, hard=True)
    play music "faith.mp3" fadein 5

    m"嗯..."

    voice "voice/marisa21.wav"
    m"决定了，我这就去一趟红魔馆。"

    scene bg gate with fade
    $ renpy.pause(1.0, hard=True)

    "..."

    rm0"雨啊。"

    s0"下雨了呢。"

    rm0"难得清静真好。"

    show marisa 1 at fadeInLeft

    voice "voice/marisa22.wav"
    m"...到了。"

    rm0"看来这下没法清静了。"

    s0"...是啊。"

    stop sound
    scene bg dining with fade
    $ renpy.pause(1.0, hard=True)
    show marisa 15 at fadeInLeftMiddle
    show remilia 1 at fadeInRight
    $ renpy.pause(1.0, hard=True)

    rm"找帕琪有事？"

    m"嗯。"

    show sakuya 1 at moveInLeft
    $ renpy.pause(1.0, hard=True)

    s"请用茶。"

    "咲夜沏好新鲜的茶，优雅地将其置于托盘上，交付给魔理沙。"

    m"..."

    show marisa 22 at lmiddle

    voice "voice/marisa23.wav"
    m"好烫！"

    show marisa 16 at lmiddle
    show sakuya 6 at left

    s"当然烫了。"

    rm"咲夜，把帕琪叫过来。"

    s"好的。"

    show sakuya 1 at leftMoveOut
    show marisa 16 at lmiddle

    m"(这么烫根本没法喝嘛...)"

    show remilia 2 at right

    rm"我说魔理沙。"

    rm"你的打算是“重新举办因雨终止的烟花祭典”，"

    rm"对吧。"

    voice "voice/marisa24.wav"
    m"嗯，说是这么说..."

    show remilia 3 at right

    rm"你是为了谁才在干这种事情？"

    rm"谁值得让你淋成这样，也要专程跑一趟？"

    m"呃..."

    p"来了。"

    show remilia 1 at right

    m"..."

    p"在说话之前先把身上烘干吧。"

    p"那边就有暖炉。"

    scene bg black with fade
    $ renpy.pause(1.0, hard=True)

    "..."

    p"干了吗？"

    m"啊啊。"

    "帕秋莉的手中提有一个袋子。"

    scene bg desk with fade
    $ renpy.pause(1.0, hard=True)
    
    voice "voice/marisa25.wav"
    m"那个袋子是什么？"

    show patchouli 1 at fadeInRight
    $ renpy.pause(1.0, hard=True)

    p"帮你解决烦恼的锦囊哦。"

    voice "voice/marisa26.wav"
    m"里面是什么？"

    p"魔石，用来做照明魔法的媒介的。"

    m"那东西要怎么用？"

    p"所谓的魔石，能够把受到的魔力增幅再放出，"

    show patchouli 7 at right

    p"但是容纳的魔力超过储存界限就会破损。"

    p"利用这一点，可以让它发挥焰火的作用。"

    voice "voice/marisa27.wav"
    m"...我不是很懂。"

    show patchouli 1 at right

    p"毕竟你没有实际见过，可能有点难以理解。"

    m"那你做一次给我看看吧。"
    
    scene bg library with fade
    $ renpy.pause(1.0, hard=True)

    "一阵强光从帕秋莉的手中放出。"

    "与外面的阴雨天气不同，整个图书馆仿佛都被照得透亮。"

    p"你看。"

    p"大概就是这种感觉。"

    "魔理沙捂着被光刺到的眼睛。"

    voice "voice/marisa28.wav"
    m"闪瞎了..."

    p"..."

    scene bg black with fade
    $ renpy.pause(1.0, hard=True)

    scene bg dining with fade
    $ renpy.pause(1.0, hard=True)

    s"打扰了。"

    show sakuya 1 at fadeInLeft
    $ renpy.pause(1.0, hard=True)

    "..."
    
    show remilia 1 at fadeInRight
    $ renpy.pause(1.0, hard=True)

    rm"魔理沙走了吗？"

    s"是，我刚刚送完她回来。"

    rm"是吗。"

    rm"我说，咲夜。"

    rm"祭典什么时候开始？"

    s"九点。"

    rm"听魔理沙说的？"

    s"...不是。"

    rm"你还挺了解的嘛。"

    "..."

    rm"你也去参加吧。"

    show sakuya 7 at left

    s"诶...。"

    rm"身边的人一脸心神不定的样子，我也淡定不下来啦。"

    show sakuya 1 at left

    "..."

    rm"偶尔也要学会顺从自己的内心。"

    rm"你也是人嘛。"

    s"..."

    "咲夜鞠了一躬。"

    show sakuya 1 at disappear

    "..."

    p"你也真够宠她的。"

    show remilia 3 at right

    rm"彼此彼此吧。"

    rm"你教给魔理沙的东西，全都是假的对吧。"

    p"..."

    p"那东西不是我本人来的话就没有意义了。"

    show remilia 1 at right

    rm"是啊。"

    rm"我是希望咲夜能留下比悼念她时所鲜之花还要多的回忆。"

    play sound "rain.mp3" loop

    jump rvillage


label rvillage:
    $_dismiss_pause=False
    scene bg rvillage with fade
    $ renpy.pause(1.0, hard=True)
    
    "..."

    show marisa 1 at fadeInLeft
    show kosuzu 2 at fadeInRightMiddle
    $ renpy.pause(1.0, hard=True)

    k"就算说让我把所有人聚集起来..."

    show marisa 2 at left

    m"尽量就好，能拜托你吗？"

    show kosuzu 7 at rmiddle

    k"我是很想帮你，但是这么大的雨..."

    k"而且只有我一个人，实在是能力有限..."

    m"是吗..."

    voice "voice/marisa29.wav"
    m"...抱歉打扰了。"

    $ renpy.pause(1.0, hard=True)

    y"这种事情不应该是我的工作吗？"

    show aya 1 at afadeInRight
    $ renpy.pause(1.0, hard=True)
    
    k"啊，文小姐"

    show kosuzu 1 at rmiddle
    show marisa 5 at left

    m"从哪里冒出来的？"

    show aya 4 at aright

    if player_choice == 1:
        y"我从魔法森林一路跟过来的。"

    elif player_choice == 2:
        y"我从红魔馆一路跟过来的。"

    show aya 1 at aright

    voice "voice/marisa30.wav"
    m"我就知道是这样...。"

    y"那种事情先放到一边，不知你意下如何啊？"

    show marisa 2 at left

    y"交给我的话，就能迅速把消息传遍幻想乡喔？"

    y"想必能为你派上用场吧。"

    y"怎样？"

    "..."

    "..."

    show marisa 11 at left

    m"啊啊..."
    
    m"那就拜托你了。"

    show aya 8 at aright

    y"看来交易已经完成了呢！"

    y"那么我现在就去准备新闻，先走一步！"

    y"请多多关照清廉正直的射命丸~"

    show aya 8 at arightMoveOut
    show marisa 1 at left

    m"那我也离开..."

    show kosuzu 7 at rmiddle

    k"等一下，魔理沙小姐！"

    m"...嗯？"

    k"..."

    $ renpy.pause(1.0, hard=True)
    show kosuzu 6 at rmiddle

    k"我，很期待今晚的焰火！"

    k"请一定要加油啊！"

    show marisa 2 at left

    m"..."

    s"原来你在这儿啊。"

    show sakuya 8 at right
    show marisa 9 at left
    show kosuzu 7 at rmiddle

    s"小铃，能让我在这里呆到祭典开始为止吗？"

    k"诶。啊，当然可以..."

    show marisa 5 at left

    m"蕾米莉亚不用管了吗？"

    show sakuya 1 at right

    s"因为我想来，所以就来了。"

    s"我可是期待了这么久，今天轻松一下也可以嘛。"

    show kosuzu 6 at rmiddle

    k"咲夜小姐，要不要猜猜魔理沙要做什么啊？"

    s"不好意思我可是知道谜底的。想知道吗？"

    show kosuzu 7 at rmiddle

    k"诶！不要告诉我啦，我要把悬念留到最后！"

    show sakuya 6 at right

    s"那就这样吧。"

    show kosuzu 6 at rmiddle

    k"啊，但能不能就稍微剧透一点点？"

    s"那就..."

    show marisa 13 at left

    s"大概会比焰火还要漂亮吧。"

    k"哇！这么一说越来越期待了呢！"


label home:
    $_dismiss_pause=False
    scene bg black with fade
    $ renpy.pause(1.0, hard=True)

    "..."

    "雨声如急促的鼓点坠落，掩盖了所有其他的声响。"

    "撞击在屋檐上，激起一阵又一阵的雨花。"

    "..."

    m"你们当然是期待了。"

    m"..."

    "昏暗的光线从窗户上的玻璃透过，留下长长的阴影。"

    "魔石仿佛有了一点光芒。"

    "...但是也只有一点。"

    m"...呼..."

    m"...明明灌入了这么多魔力，却只有这点光吗..."

    m"..."

    m"只凭一个人的力量果然办不到吗..."

    m"可恶..."

    m"..."
    

label hakurei:
    $_dismiss_pause=False
    scene bg night with fade
    $ renpy.pause(1.0, hard=True)

    "..."

    "雨声中所有的喧嚣与浮躁都仿佛被洗涤得一干二净。"

    "只剩下纯粹的单调的声音。"

    "思绪就像这激烈的雨点一样，"

    "不断冲击着心中难以说出的事物。"

    "..."

    "灵梦倚在神社的屋檐下，面对着无际的大雨走神。"

    "..."

    $ renpy.pause(2.0, hard=True)

    voice "voice/marisa31.wav"
    m"会感冒的。"

    re"..."

    $ renpy.pause(0.5, hard=True)

    m"早就发现了？"

    re"你的气息太明显了。"

    m"..."

    m"你也有在期待吗？"

    menu:
        re"你猜？"
        "是":
            voice "voice/marisa32.wav"
            m"是的。"
            m"..."

        "不是":
            voice "voice/marisa33.wav"
            m"不是。"
            m"..."

    voice "voice/marisa34.wav"
    m"这都是我的自言自语啊。"

    voice "voice/marisa35.wav"
    m"我啊...好像有点想错了。"

    voice "voice/marisa36.wav"
    m"我本以为我这么做，都是为了“一个人”。"

    voice "voice/marisa37.wav"
    m"我本以为“只要让那个人开心就好了”。"

    voice "voice/marisa38.wav"
    m"但是，对此抱有期待的人却远远不止那一人。"

    voice "voice/marisa39.wav"
    m"让我愈发体会到，人果然是一种渴求着创造回忆的生物。"

    voice "voice/marisa40.wav"
    m"然后，现在又有点..."

    voice "voice/marisa41.wav"
    m"...开始害怕了。"

    re"虽然你好像在说些什么不着边际的东西，"

    re"但雨声太大我听不见哦。"

    m"是吗..."

    m"...我去去就回。"

    $ renpy.music.stop(fadeout=1.0)
    $ renpy.pause(1.0, hard=True)
    play music "reimu and marisa.mp3" fadein 5
    scene bg shrine with fade
    $ renpy.pause(1.0, hard=True)
    show marisa 26 at fadeInLeft
    $ renpy.pause(1.0, hard=True)

    re"就不能带着开心的表情出发吗？"

    re"..."

    re"一脸愁容可不适合你喔。"

    m"..."

    show marisa 16 at left
    $ renpy.pause(1.0, hard=True)

    m"想笑就笑吧。"

    show marisa 28 at left

    m"我承认我现在很心虚。"

    m"看起来很像个窝囊废吧。"

    re"时间快到了哦。"

    re"你不快点走吗？"

    show marisa 17 at left

    m"啊啊我知道了，我走啦！"

    m"可别到时候再来找我抱怨哦！"

    $ renpy.pause(1.0, hard=True)

    re"我相信你。"

    show marisa 27 at left
    $ renpy.pause(1.0, hard=True)

    re"祭典的成功失败不过是细枝末节。"

    re"能够令人难忘便足够了。"

    re"不论结果如何，魔理沙，只要贯彻你的风格做到最后，"

    re"我都愿意铭记于心。"

    re"这样你有不满吗？"

    $ renpy.pause(2.0, hard=True)

    show marisa 21 at left

    m"还能有什么不满啊。"

    m"那就如你所愿，给你看最美的焰火。"

    show marisa 21 at leftFadeOut

    "..."

    re"这才像魔理沙嘛。"


label sky:
    $_dismiss_pause=False
    scene bg sky with fade
    $ renpy.pause(1.0, hard=True)

    "..."

    k0"那我们走吧。"

    k0"哇，好多人啊。"

    s0"小铃，"

    s0"能把伞偏过来一点吗？"

    k0"啊，对不起！"

    y0"啊呀呀，刚才真是多谢。"

    s0"原来如此，这事你也掺了一脚啊，"

    s0"难怪消息传的这么快。"

    y0"我觉得人还是越多越好。"

    y0"好了，差不多也该到九点了。"

    y0"就等她来画上点睛一笔了。"

    "..."

    menu:
        m"..."

        "丢出魔石":
            $ he = 1

    "一抹闪光从魔理沙的手中射出。"

    "像是漫漫暗夜中的炽热星辰，在被发现的那一刻起就不会被世人遗忘。"

    "紧接着在下一瞬间，那抹光芒熄灭了。"

    menu:
        m"...可恶，再来一次！"

        "丢出魔石":
            $ he = 1
        
    k0"文小姐，你有没有看见那个？貌似发光的东西..."

    y0"嗯，我的相机里什么都没有拍到啊。"

    y0"嘛老老实实地等吧。可能是魔理沙那边有些什么状况。"

    "我说，现在几点了？九点已经过了吧。"

    "已经九点半了，来的可真够慢的啊。"

    "虽然我不大想直说，但该不会是失败了吧...。"

    "有可能啊。"

    "毕竟一个人还是很吃力的吧。"

    "明明只要事前说一声的话我们也可以帮忙的..."

    y0"想回去的话就回去吧。"

    y0"事已至此，就算抱怨也为时已晚了。"

    y0"但我要看到最后。"

    if player_choice == 1:
        a0"相信自己，魔理沙。"

        a0"...你能做到。"

    "..."

    "还剩最后一颗魔石。"

    r0"只要能贯彻你的风格做到最后，"

    $ renpy.pause(1.0, hard=True)

    r0"我愿意铭记于心。"

    $ renpy.pause(1.0, hard=True)

    menu:
        m"...最后一颗魔石。"

        "丢出魔石":
            $ he = 1
        "留着它":
            $ he = 2

    m"世间不如意事十有八九啊。"

    scene bg black with fade
    $ renpy.pause(1.0, hard=True)

    m"「魔符」"

    scene bg marisa with fade
    $ renpy.pause(1.0, hard=True)

    voice "voice/marisa42.wav"
    m"「星屑幻想」。"

    scene bg black with fade
    $ renpy.pause(1.0, hard=True)

    y0"啊。"

    y0"魔理沙掉下来了。"

    k0"!"

    s0"她该不会没力气了吧..."

    m"..."

    voice "voice/marisa43.wav"
    m"这一切，都是为了我自己。"

    $ renpy.pause(1.0, hard=True)

    r0"我也一直期待着呢。"

    voice "voice/marisa44.wav"
    m"因为每次看到你寂寞的神情。"

    voice "voice/marisa45.wav"
    m"我就会心痛。"

    "下坠的时间非常漫长。"

    "雨点渐渐地和天空平行，落在身上也不再有感觉。"

    "..."

    r0"你啊，太勉强自己了。"

    "一个模糊的红白色的身影仿佛正在靠近自己。"

    "下一秒钟，下落中的身体被一种温暖的感觉托住。"

    r0"你已经很努力了，接下来的事..."

    "..."

    voice "voice/marisa46.wav"
    m"看，上面。"

    $ renpy.music.stop(fadeout=1.0)
    $ renpy.pause(1.0, hard=True)
    play music "epilogue.mp3" fadein 4

    re"..."

    scene bg reimu with fade
    $ renpy.pause(1.5, hard=True)

    "星星从那最后的魔石中迸发而出。"

    "红色，白色，蓝色，绿色，彩色，在那一瞬间爆裂开来。"

    "就像是天空的花火，如鸢，如华，如光，如影，"

    "静止、聆听、欣赏，似乎宇宙间的一切都为这一时刻凝结成为回忆，"

    "...璀璨而满目星光。"

    re"..."

    k"好美..."

    y"我就说嘛...魔理沙一定能做到。"

    s"比焰火还要漂亮..."

    if player_choice == 1:
        a"看来不需要我出手了呢。"

    re"..."

    re"(...美到说不出话。)"

    m"灵梦..."

    $ renpy.pause(1.0, hard=True)

    voice "voice/marisa47.wav"
    m"一脸愁容可不适合你喔。"

    re"..."

    $ renpy.pause(1.0, hard=True)

    voice "voice/marisa48.wav"
    m"...哈哈...想不到灵梦也会哭哦。"

    re"...你以为是谁的错啊。"

    $ renpy.pause(1.0, hard=True)

    re"(...最美的焰火)"

    re"(真的做到了啊...)"

    re"(魔理沙。)"

    $ renpy.pause(1.0, hard=True)

    re"(...我会铭记于心的。)"


label epilogue:
    $_dismiss_pause=False
    scene bg black with None
    $ renpy.pause(1.0, hard=True)

    $ style.say_dialogue.xalign = 0.5
    $ style.say_dialogue.yalign = 0.5

    show text "Original Work\n\n東方Project" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "Story\n\nウサホリ《光を唱えて》" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "Studio\n\nVisual Cube" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "Program\n\nReitsuki Hikari" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "Track List\n\n永遠の巫女\n神社の前で\n流星スペクトラ\n東の国の眠らない夜\nさくらさくら ~ Japanize Dream" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "Composers\n\nRe:Volte\n夜秋\nFoxtail-Grass Studio\nファクトリー・ノイズ&AG\nDemetori" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "Artwork\n\ndairi\n東方LostWord\n萃\nりすたる\n遠坂あさぎ" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "Voice Cast\n\n宮尾 時雨(skytnt) as 霧雨 魔理沙" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "しゃめいまる あや\n射命丸 文" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "もとおり こすず\n本居 小鈴" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "いざよい さくや\n十六夜 咲夜" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "はくれい れいむ\n博麗 霊夢" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "きりさめ まりさ\n霧雨 魔理沙" with Fade(2.0, 4.0, 2.0)

    pause 2.0
    show text "東方夢雨祭\n～ Phantasmal Rain Reverie" with Fade(2.0, 4.0, 2.0)

        
    pause 5.0
    $ renpy.music.stop(fadeout=1.0)
    $ renpy.pause(1.0, hard=True)

    return
