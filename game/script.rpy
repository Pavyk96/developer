init:
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')

define vas = Character("Вася", color="#00e4fd")
define kas = Character("Касеки", color="#fbff00ff")
define umi = Character("Юми", color="#e600ffff")

# background images
image portal = im.Scale("bg/portal.png", 1920, 1080)
image blank = im.Scale("bg/blank background.jpg", 1920, 1080)

# character sprites
image dummy = im.Scale("character/dummy.png.", 768, 768)
image kas normal = im.Scale("SecondChapter/old man.png.", 328, 808)
image vas normal = im.Scale("FirstChapter/vasya.png.", 326, 805)
image vasya_at_the_computer = im.Scale("bg/Vasya at the computer.png", 1920, 1080)
image vasya_at_the_computer_surprised = im.Scale("bg/Vasya at the computer with a surprised face.png", 1920, 1080)

# mobs sprites
image goblin = im.Scale("mobs/goblin.png.", 768, 768) #нужен спрайт

# enviroment sprites
image forest_and_road_purple_wheel_with_vasya = im.Scale("FirstChapter/forest and road final without wheel.png", 1920, 1080) 
image forest_and_road_normal_with_vasya = im.Scale("FirstChapter/forest and road final.png", 1920, 1080)
image forest_without_vasa = im.Scale("bg/forest_without_vasa.png", 1920, 1080)
image kasekiHouse = im.Scale("SecondChapter/home.png", 1920, 1080)
image dungeon_at_day = im.Scale("ThirdChapter/dungeon_at_day.jpg", 1920, 1080) #нужен спрайт
image dungeon_at_nigth = im.Scale("ThirdChapter/dungeon_at_nigth.jpg", 1920, 1080) #нужен спрайт
image vilage_gate = im.Scale("ThirdChapter/vilage_gate.png", 1920, 1080) #нужен спрайт
image river_without_bridge = im.Scale("ThirdChapter/river_without_bridge.png", 1920, 1080) #нужен спрайт
image forest = im.Scale("ThirdChapter/forest.jpg", 1920, 1080) #нужен спрайт
# The game starts here.
label start:
    call variables from _call_variables

    # introduction
    call Preface from _call_Preface

    # first chapter
    call FirstChapter from _call_FirstChapter  

    # second chapter
    call SecondChapter from _call_SecondChapter

    # third chapter
    call ThirdChapter from _call_ThirdChapter

    # fourth chapter
    call FourthChapter from _call_FourthChapter
    return


#  Предисловие Pavyk96
label Preface:
    show vasya_at_the_computer
    "Вася, которому мы помогали исправлять ошибки на Ulearn, закончил университет и начал разработку собственной игры."
    "У него возникли проблемы в создании игры, появились баги, которые нужно исправить. В этом ему очень нужна ваша помощь!"
    show vasya_at_the_computer_surprised
    pause 2
    show portal
    "Вас с Васей засасывает в игру..." 
    return

# first chapter
label FirstChapter:
    call WorldMap from _call_WorldMap
    call BrokenCart from _call_BrokenCart
    call CartIsFixed from _call_CartIsFixed
    return

label SecondChapter:
    call ComingOfKaseki from _call_ComingOfKaseki
    call AskForDirectionsToTheVillage from _call_AskForDirectionsToTheVillage
    call ChooseDirection from _call_ChooseDirection
    return

label ThirdChapter:
    if (straight_or_right == "straight"):
        call TheWayToDange from _call_TheWayToDange
        call WayAtNight from _call_WayAtNight
        call Bug from _call_Bug
        call ProblemWithNight from _call_ProblemWithNight
        call NexToGate from _call_NexToGate
        call ChoosingSolution from _call_ChoosingSolution
    else:
        call Right from _call_Right
        if (withKaseki == False):
            call RroadToVillage from _call_RroadToVillage
        call ProblemWithBridge from _call_ProblemWithBridge
        if (withKaseki == True):
            call SecondPartShortWay from _call_SecondPartShortWay
            call NexToGate from _call_NexToGate_1
        else:
            call SecondPartLongWay from _call_SecondPartLongWay
            call NexToGate from _call_NexToGate_2
        call ChoosingSolution from _call_ChoosingSolution_1 
    return

label FourthChapter:
    call ChoiseInVillage from _call_ChoiseInVillage
    call MeetingWithUmi from _call_MeetingWithUmi 
    return

# map section. Chapter 1.1      
label WorldMap:
    scene forest_without_vasa
    with fade
    show vas normal at left
    "Перед собой вы видите фэнтезийный мир и озадаченного Васю"
   
    $ card_shirts = "question_mark | eyes"
    menu:
        'Спросить: "Что случилось?" ':
            call what_happend from _call_what_happend
        "Оглядеться и оценить обстановку":
            call admire_vasya from _call_admire_vasya
    return

label what_happend:
    vas "Я зашел в свою игру, но тут слишком много багов."
    show vas normal
    vas "Помоги, пожалуйста!"
    return

label admire_vasya:
    show forest_without_vasa
    show vas normal at left
    pause 2
    
    "Вася смотрел на Вас около 5 минут и не понимал, почему вы молчите"
    
    vas "Привет, я очень рад тебя видеть!"
    
    vas "Можешь мне помочь, пожалуйста?"

    menu:
        'Спросить: "Что случилось?" ':
            call what_happend from _call_what_happend_1
    return

# Chapter 1.2
label BrokenCart:
    scene forest_and_road_purple_wheel_with_vasya
    vas "У повозки пропало куда-то колесо."
    vas "Можешь мне помочь, пожалуйста?"
    $ card_shirts = "head_and_question_mark"
    menu: 
        "Подумать над решением этой проблемы":
            "Хм{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            "Хм{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            "Хм{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}{nw}"
    "Вы вместе подумали и нашли несколько решений"
    
    vas "Как ты думаешь, какой вариант лучше?"

    $ card_shirts = 'magnier | tools | wooden_wheel'
    menu:
        "Исправить баг в коде повозки":
            call chapter1_2_code_game from _call_chapter1_2_code_game
            vas "Мы хорошо постарались и исправили нужную переменную!"
            "Выглядит надёжно, теперь вы можете отправляться дальше!"
        "Рядом лес! Просто сделаем новое колесо, да и все!":
            $ coder_points -= 0.2
            vas "Это было долго, мы потеряли много времени, но справились!" 
            vas "Выглядит вроде надежно, можем, наверное, отправляться дальше..."
        "Повозка сможет ехать и на трех колесах, зачем ей четвертое?":
            "Странно, но это сработало."
            call three_wheeled_carts from _call_three_wheeled_carts
    return

label chapter1_2_code_game:
    $ coder_points += 5
    
    while(True):
        $ card_shirts = 'shirt | shirt | shirt'
        menu:
            "class Cart(): \n ... \n    numberOfWheels = 1":
                "Неправильно, сколько всего колес у повозки?"
            "class Cart(): \n ... \n    numberOfWheels = 3":
                    "Неправильно, сколько всего колес у повозки?"
            "class Cart(): \n ... \n    numberOfWheels = 4":
                    "Правильно, теперь у повозки 4 колеса!"
                    return
                            
label three_wheeled_carts:
    vas "Выглядит не очень надежно. Давай все-таки попробуем другой способ?"
    menu:
        "Исправить баг в коде повозки":
            call chapter1_2_code_game from _call_chapter1_2_code_game_1
            "Мы хорошо постарались и исправили нужную переменную!"
        "Рядом лес! Просто сделаем новое колесо, да и все!":
            if coder_points >= 0.2:
                $ coder_points -= 0.2
            "Это было долго, мы потеряли много времени, но справились!" 
            vas "Выглядит вроде надежно, можем, наверное, отправляться дальше..."
    return

# Chapter 1.3 
label CartIsFixed:
    scene forest_and_road_normal_with_vasya

    $ card_shirts = 'way_to_forest | question_mark'
    menu:
        "Поехали дальше!":
            return
        "Куда мы отправляемя и зачем?":
            call chapter1_3_where_to from _call_chapter1_3_where_to
    return

label chapter1_3_where_to:
    vas "Нам нужно доставить снаряжение для авантюристов в деревню Гудзё"
    vas "Потому что около неё появилось данж с монстрами и никто не вызывался помочь, кроме нас"
    vas "Поэтому за эту срочную задачу от гильдии взялись только мы, рискуя своими жизнями"
    
    $ card_shirts = 'mouth'
    menu:
        "Почему им нужна наша помощь? Почему они не справляются сами?":
            vas "Не знаю, ахахахаха"
            vas "Но не думаю, что они просто так отправили заявку в гильдию"
            vas "Когда доедем до деревни, можешь спросить у старосты"
    "Вы поехали дальше..."
    return

# chapter 2.1
label ComingOfKaseki:
    scene kasekiHouse
    with fade
    "Вы ехали, пока не наткнулись на развилку с деревянным домиком."
    "Из домика вышел немолодой мужчина."
    show kas normal at left with Dissolve(.3)

    $ card_shirts = 'ear'
    menu:
        "Остановится у домика и послушать мужчину":
            "Вы остановились. У Вас завязался диалог."
    "???" "Приветствую, путники."
    kas "Я слежу за этим домом, меня зовут Касеки."
    kas "Как вас зовут? Куда вы направляйтесь?"
    return

# chapter 2.2
label AskForDirectionsToTheVillage:
    show kas normal at right
    "Рядом находился данж {w=1.5} {nw}"
    $ card_shirts = 'mouth | question_mark'
    menu:
        "Представится и спросить, какой путь ведет до деревни Гудзё?":
            return
        "Спросить, что Касеки делает в таком опасном месте?":
            call AboutKaseki from _call_AboutKaseki
    return

label AboutKaseki:
    "Касеки начал вам объяснять."
    kas "Я был смотрителем этой шахты, но недавно тут появились гоблины."
    kas "Говорят, что в пещере появился Вождь Гоблинов, и он присвоил себе с легкостью это место, потому что у него не было охраны."
    kas "Ведь наша деревня не такая большая, и не может позволить себе охранников."
    kas "А я не ушел из этого дома, потому что я уже, как видите, стар, мне некуда пойти, тем более это мой любимый дом..."
    kas "А еще мне передали сообщение из деревни, что они попросили помощи из города, и мне надо будет помочь добраться путешественникам до деревни."
    kas "Это вы те самые путешественники?"
    vas "Да, мы доставляем вооружение для авантюристов из деревни!"

    $ card_shirts = 'mouth'
    menu:
        "Представится и спросить, какой путь ведет до деревни Гудзё?":
            return

# chapter 2.3
label ChooseDirection:
    "Вы представились, вам стали объяснять, как добраться до деревни."
    kas "Можно поехать прямо, но тот путь может оказать не безопасным."
    kas "Можно поехать направо, тот путь длинный и более безопасный."
    kas "Но на этом пути много развилок, без человека знающего путь, можно потратить много времени."
    
    $ card_shirts = 'dangerous_place | road'
    menu:
        "Поехать прямо.":
            "Вы хотели отправиться прямо, но есть одно но..."
            vas "Нам нужно придумать план, как мы будем ехать по этому пути."
            vas "Ведь прямо по этому пути находится данж."
            $ straight_or_right = "straight"
            return
        "Поехать направо.":
            "Вы хотели поехать вправо, но возник вопрос..."
            vas "Как мы поймем, куда нам ехать? Какой путь правильный?"
            vas "Нам бы какую-нибудь карту, или что-то похожее..."
            $ straight_or_right = "right"
            return
    return

# TODO: deal with card shirts and sprites HERE
# chapter 3.1
label TheWayToDange:
    scene dungeon_at_day
    $ card_shirts = 'head_and_question_mark | head_and_question_mark | head_and_question_mark'
    menu:
        "Просто проехать, вдруг повезет.":
            # show goblin at right with Dissolve(.3)
            show goblin at right with vpunch
            "Не удачное решение, на пути видны монстры."
            show vas normal at left with Dissolve(.5)
            vas "Это будет слишком опасно, давай выберем другое решение."
            hide goblin with easeoutright
            hide vas normal with easeoutleft
            call TheWayToDange from _call_TheWayToDange_1
        "Поедем медленно, но тихо.":
            "Не удачное решение, на пути видны монстры."
            # show goblin at right with Dissolve(.3)
            show goblin at right with vpunch
            show vas normal at left with Dissolve(.5)
            vas "Мне кажется, это будет хорошей идеей, если мы отправимся ночью, как думаешь?"
            hide goblin with easeoutright
            hide vas normal with easeoutleft
            call TheWayToDange from _call_TheWayToDange_2
        "Дождаться ночи и отправится в путь.":
            "Вот этот метод может сработать, надо попробовать. Вы стали ожидать ночи."
            scene dungeon_at_nigth with fade
            show vas normal at left with Dissolve(.5)
            vas "Наступила ночь, отправляемся?"
            menu:
                "Да, отправляемся!":
                    return
    return

label WayAtNight:
    "Вы наткнулись на что-то непонятное... Луна сменила солнце, но видно как днем..."
    vas "Вылезла ошибка, она ругается, и показывает что-то непонятное..."
    vas "Из-за нее мы видим ночью как днем..."
    return

label Bug:
    vas "Что будем делать?"

    $ card_shirts = 'head_and_question_mark | tools'
    menu:
        "Оставим эту полезную фичу.":
            "Интересное решение, но в этом случае оно не сработает."
            call Bug from _call_Bug_1
        "Исправить ошибку":
            "Вы стали думать над решением этой проблемы."
            vas "Exception показывает, что в строчке кода находится ошибка."
            vas "Помоги мне найти правильный ответ, пожалуйста..."
    return

label ProblemWithNight:
        $ card_shirts = 'shirt | shirt | shirt'
        menu:
            "public static class Cave\n var nightTime = 1000":
                "Неправильно, попробуйте еще раз."
                call ProblemWithNight from _call_ProblemWithNight_1
            "private static class CAVEE\n var nightTime = 1000":
                "Неправильно, попробуйте еще раз."
                call ProblemWithNight from _call_ProblemWithNight_2
            "private static classe Cave\n var nightTime = 1000":
                "Правильно, теперь ночью стало темно!"
                vas "Проблема решена!"
                return
        return

label NexToGate:
    scene vilage_gate with fade
    show vas normal at left with Dissolve(.5)
    vas "Теперь нам надо проехать в деревню, а для этого нужно открыть ворота."
    vas "Сейчас они закрыты, но они открываются, если решить маленькую загадку."
    vas "Нужно определить возвращаемый тип выражения, которое написано рядом с воротами."
    return
        
label ChoosingSolution:
    "var a = 2 / 3 * 5;"

    $ card_shirts = 'shirt | shirt | shirt'
    menu:
        "Double":
            "Неверно... Попробуйте другой ответ."
            call ChoosingSolution from _call_ChoosingSolution_2
        "Long":
            "Неверно... Попробуйте другой ответ."
            call ChoosingSolution from _call_ChoosingSolution_3
        "int":
            return
    return

# Chapter 3.2
label Right:

    $ card_shirts = 'mouth | head_and_question_mark | eyes'
    menu:
        "Спросить у Касеки путь.":
            "Касеки начал вам рассказывать, как добраться до деревни."
            kas "Я вас скажу, куда нужно поворачивать на развилках, а вы запоминайте, чтобы быстрее добраться до деревни."
            kas "На пути вам встретится, пять развилок и два моста."
            kas "Вправо, влево, мост, прямо, влево, мост, прямо"
            kas "Если вы пройдете так, на всех развилках, то вы попадете в деревню, если сойдете с пути, то ничего страшного, вы попадете к речке."
            vas "Хорошо, мы вас поняли, большое спасибо!"
            $ card_shirts = 'mouth'
            menu:
                "Тогда, поехали!":
                    scene forest with fade
                    "Вы ехали, пока не наткнулись на развилку."
            show vas normal at left with Dissolve(.5)
            vas "Какой путь нам лучше выбрать?"
            $ withKaseki = False
            return
        "Взять с собой в путь Касеки.":
            "Касеки согласился вам показать путь до деревни."
            scene river_without_bridge with fade
            "Касеки показывал вам верные пути, пока вы не наткнулись на речку."
            show vas normal at left with Dissolve(.5)
            vas "На этом месте должен был быть мост, которого нету по какой то причине и код игры показывает странную ошибку."
            $ withKaseki = True
            return
        "Просто поехать куда глаза глядят.":
            "Мне кажется это не самый лучший вариант, мы можем запутаться."
            vas "Если мы выберем этот вариант, мы потеряем много времени, давай выберем другое решение?"
            call Right from _call_Right_1
    return

label RroadToVillage:
    $ card_shirts = 'left_arrow | right_arrow'
    $ rightChoice = False
    while(not rightChoice):
        menu:
            "Влево.":
                "Не правильно, вы потеряли время на неверный путь."
            "Вправо.":
                "Правильный путь, вы поехали дальше."
                $ rightChoice = True
    vas "Какой путь нам лучше выбрать?"
    
    $ card_shirts = 'left_arrow | right_arrow'
    $ rightChoice = False
    while(not rightChoice):
        menu:
            "Влево.":
                "Правильный путь, вы поехали дальше."
                $ rightChoice = True    
            "Вправо.":
                "Не правильно, вы потеряли время на неверный путь."
    "Вы наткнулись на речку, где должен был быть мостик, но по какой-то причине его нет и показывается странную ошибку."
    vas "Что-то странное, тут должен быть мостик, но его нет."
    vas "Тут ошибка, показывает что с кодом игры что-то не так..."
    vas "Нужно правильный вариант кода, при котором мостик появится."
    scene river_without_bridge with fade
    return

# TODO: deal with menu section here.
label ProblemWithBridge:
    $ card_shirts = 'shirt | shirt | shirt'
    menu:
        "GameeeObject Bridge = Instantiate(bridgePrefab, new Vector3(xyz), Quaternion.identity);":
            "К сожалению, не правильно, попробуйте еще раз."
            call ProblemWithBridge from _call_ProblemWithBridge_1
        "GameObject Bridge = Instantiate(bridgePrefab, new Vector3(x, y, z), Quaternion.identity);":
            "Правильно, вы нашли правильный код!"
            vas "Проблема решена!"
            vas "Теперь можно отправляться дальше!"
        "GameObject Bridge\n Instantiate(bridgePrefab, new Vector3(x, y, z), QuaternionIdentity);":
            "К сожалению, не правильно, попробуйте еще раз."
            call ProblemWithBridge from _call_ProblemWithBridge_2
    return

label SecondPartLongWay:
    scene forest with fade
    show vas normal at left with Dissolve(.5)
    vas "Какой путь нам лучше выбрать?"
    
    $ card_shirts = 'up_arrow | left_arrow'
    $ rightChoice = False
    while(not rightChoice):
        menu:
            "Прямо":
                "Правильный путь, вы поехали дальше."
                $ rightChoice = True
            "Влево":
                "Не правильно, вы потеряли время на неверный путь."
    vas "Какой путь нам лучше выбрать?"
    
    $ card_shirts = 'left_arrow | right_arrow'
    $ rightChoice = False
    while(not rightChoice):
        menu:
            "Влево":    
                "Правильный путь, вы поехали дальше."
                $ rightChoice = True
            "вправо":
                "Не правильно, вы потеряли время на неверный путь."
    vas "Какой путь нам лучше выбрать?"
    
    $ card_shirts = 'up_arrow | left_arrow'
    $ rightChoice = False
    while(not rightChoice):
        menu:
            "Прямо":
                "Правильный путь, вы поехали дальше."
                $ rightChoice = True
            "Влево":
                "Не правильно, вы потеряли время на неверный путь."

    return
label SecondPartShortWay:
    "Вы ехали, пока не наткнулись на ворота деревни."
    vas "Теперь нужно открыть ворота, чтобы въехать в деревню."
    vas "Сейчас они закрыты, но они открываются, если решить маленькую загадку."
    return

# chapter 4.1
label ChoiseInVillage:
    scene blank with pixellate
    show kas normal at right
    show vas normal at left
    "Вы зашли в деревню и начали искать гильдию."
    kas "Здесь наши пути расходятся, я выполнил свое задание. Удачи вам."

    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    menu:
        "Вам тоже удачи!":
            "Вы отправились искать гильдию."
            vas "Теперь нам нужно найти гильдию, нас там уже ждут."
        "Постойте пожалуйста, скажите как нам найти гильдию?":
            kas "На здании гильдии должен быть меч, поэтому отличительному знаку вы должны быстро найти ее."
            vas "Все понял, надеюсь мы ее найдем, больше спасибо. Удачи вам."   
    
    hide kas
    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    menu:
        "Библиотека":
            vas "Хмм, библиотека пустует... В ней нет посетителей..."
            vas "Но тут есть записка! Давайте почитаем, что тут написано!"
            """Посетителей становится все меньше, потому что все боятся заходить в нашу деревню...
            Я считаю, что это из-за этих проклятых, очень сильных гоблинов... 
            Наша библиотека вынуждена закрыться..."""
            # picture
        "Мясная лавка":
            vas "Лавка выглядит заброшенной..."
            vas "Но тут есть какая-то записка! Давайте прочитаем, что тут написано!"
            """***Наша лавка пришла в упадок...
            Все из-за сильных гоблинов, которые воруют наш скот...
            По этой причине мы вынуждены закрыться...
            Всего хорошего"""
        "Гильдия":
            vas "Это гильдия! Идем!"
            return
    return

# chapter 4.2
label MeetingWithUmi:
    scene blank with pixellate
    show vas normal at center
    "Вы зашли в здание, и оказались правы - это гильдия."
    show vas normal at right with dissolve
    vas "Нам нужно подойти к стойке администрации, чтобы сообщить, что мы уже прибыли."
    "Вы подошли к стойке"
    show dummy at left with dissolve
    umi "Здравствуйте!" 
    umi "Меня зовут Юми, я представитель гильдии."
    umi "Зачем вы пришли?"
    vas "Мы выполняем задание от вашей деревни. Доставляем магическое оружие для ваших авантюристов."
    umi "Хорошо. Наверное вы устали с дороги, не хотите перекусить?"
    
    $ card_shirts = "dangerous_place | mouth"
    menu:
        "Отправиться в данж.":
            return
        "Перекусить.":
            umi "Давайте перекусим"
            call eat from _call_eat
            vas "Хорошо поели! Теперь идем?"
            $ card_shirts = "dangerous_place"
            menu:
                "Отправиться в данж":
                    return
    return
label eat:
    "IN DEVELOPMENT"
    return

label variables:
    $ coder_points = 0.0
    $ card_shirts = ""
    return

label end:
    "THE END!"
    return
