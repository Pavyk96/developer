﻿init:
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')

define vas = Character("Вася", color="#00e4fd")
define petr = Character("Дед Петр", color="#fbff00ff")
define nas = Character("Настя", color="#e600ffff")

# background images
image portal = im.Scale("bg/portal.png", 1920, 1080)
image blank = im.Scale("bg/blank background.jpg", 1920, 1080)

# character sprites
image dummy = im.Scale("character/dummy.png.", 768, 768)
image petr normal = im.Scale("SecondChapter/old man.png.", 328, 808)
image vas normal = im.Scale("FirstChapter/vasya.png.", 326, 805)
image vasya_at_the_computer = im.Scale("bg/Vasya at the computer.png", 1920, 1080)
image vasya_at_the_computer_surprised = im.Scale("bg/Vasya at the computer with a surprised face.png", 1920, 1080)

# mobs sprites
image goblin = im.Scale("mobs/goblin.png.", 768, 768) #нужен спрайт

# enviroment sprites
image forest_and_road_purple_wheel_with_vasya = im.Scale("FirstChapter/forest and road final without wheel.png", 1920, 1080) 
image forest_and_road_normal_with_vasya = im.Scale("FirstChapter/forest and road final.png", 1920, 1080)
image forest_and_road_purple_wheel_without_vasya = im.Scale("FirstChapter/forest and road final without wheel without vasya.png", 1920, 1080)
image forest_without_vasa = im.Scale("bg/forest_without_vasa.png", 1920, 1080)
image petrHouse = im.Scale("SecondChapter/home.png", 1920, 1080)
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

    # fifth chapter
    call FifthChapter
    return


#  Предисловие Pavyk96
label Preface:
    play music "audio/Various Themes/Origins.ogg" fadein 0.5 volume 0.1 loop
    show vasya_at_the_computer
    "Вася, которому мы помогали исправлять ошибки на Ulearn, закончил университет и начал разработку собственной игры."
    "У него возникли проблемы в создании игры, появились баги, которые нужно исправить. В этом ему очень нужна ваша помощь!"
    show vasya_at_the_computer_surprised
    pause 2
    play sound "audio/SFX/Awe_1.ogg" volume 0.5
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
    call ComingOfPetr from _call_ComingOfPetr
    call AskForDirectionsToTheVillage from _call_AskForDirectionsToTheVillage
    call ChooseDirection from _call_ChooseDirection
    return

label ThirdChapter:
    if (straight_or_right == "straight"):
        call TheWayToDange from _call_TheWayToDange
        call WayAtNight from _call_WayAtNight
        call Bug from _call_Bug
        call ProblemWithNight from _call_ProblemWithNight
        call NextToGate from _call_NextToGate
        call ChoosingSolution from _call_ChoosingSolution
    else:
        call Right from _call_Right
        if (withPetr == False):
            call RoadToVillage from _call_RoadToVillage
        call ProblemWithBridge from _call_ProblemWithBridge
        if (withPetr == True):
            call SecondPartShortWay from _call_SecondPartShortWay
        else:
            call SecondPartLongWay from _call_SecondPartLongWay
            call NextToGate from _call_NextToGate_1
        call ChoosingSolution from _call_ChoosingSolution_1 
    return

label FourthChapter:
    call ChoiseInVillage from _call_ChoiseInVillage
    call MeetingWithNas from _call_MeetingWithNas 
    return

label FifthChapter:
    call DialogueNearDungeon
    call BugFix
    call TheWayToBoss
    return

# map section. Chapter 1.1      
label WorldMap:
    scene forest_and_road_purple_wheel_without_vasya
    with fade
    stop music
    stop sound
    play music "audio/Towns/Farm Life.ogg" volume 0.035 fadein 0.5 loop
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
    vas "Мы попали в мою игру! Но я еще не успел исправить баги..."
    show vas normal
    vas "Помоги, пожалуйста! Иначе мы не выберемся..."
    return

label admire_vasya:
    scene forest_and_road_purple_wheel_without_vasya
    show vas normal at left
    pause 2
    
    "Вася смотрел на Вас около 5 минут и не понимал, почему Вы молчите"
    
    vas "Можешь мне помочь, пожалуйста?"
    menu:
        'Спросить: "Что случилось?" ':
            call what_happend from _call_what_happend_1
    return

# Chapter 1.2
label BrokenCart:
    scene forest_and_road_purple_wheel_with_vasya
    vas "У повозки куда-то пропало колесо."
    vas "Что делать?"
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
    
    $ card_shirts = 'magnier | tools | wooden_wheel'
    menu:
        "Исправить баг в коде повозки":
            call chapter1_2_code_game from _call_chapter1_2_code_game_1
            "Мы хорошо постарались и исправили нужную переменную!"
        "Рядом лес! Просто сделаем новое колесо, да и все!":
            $ coder_points -= 0.2
            "Это было долго, мы потеряли много времени, но справились!" 
            vas "Выглядит вроде надежно, можем, наверное, отправляться дальше..."
        "Оставить все как есть":
            vas "Ну ладно, может само починится"
            $ withoutWheel = True
            $ coder_points -= 5
    
    return

# Chapter 1.3 
label CartIsFixed:
    if (not withoutWheel):
        scene forest_and_road_normal_with_vasya
    else:
        scene forest_and_road_purple_wheel_with_vasya

    $ card_shirts = 'way_to_forest | question_mark'
    menu:
        "Поехали дальше!":
            return
        "Куда мы отправляемя и зачем?":
            call chapter1_3_where_to from _call_chapter1_3_where_to
    return

label chapter1_3_where_to:
    vas "Нам нужно доставить снаряжение для авантюристов в деревню неподалеку"
    vas "Около неё появился данж с монстрами, и никто не вызывался помочь, кроме нас"
    vas "Поэтому за эту срочную задачу от гильдии взялись только мы, рискуя своими жизнями."
    
    $ card_shirts = 'mouth'
    menu:
        "Почему им нужна наша помощь? Почему они не справляются сами?":
            vas "Не знаю, ахахахаха"
            vas "Но не думаю, что они просто так отправили заявку в гильдию"
            vas "Когда доедем до деревни, можешь спросить у старосты"
    "Вы поехали дальше..."
    return

# chapter 2.1
label ComingOfPetr:
    stop music fadeout 0.5
    play music "audio/Overworld/Journey Across the Blue.ogg" fadein 0.5 volume 0.04 loop
    scene petrHouse
    with fade
    "Вы ехали, пока не наткнулись на развилку с деревянным домиком."
    "Из домика вышел немолодой мужчина."
    show petr normal at left with Dissolve(.3)

    $ card_shirts = 'ear'
    menu:
        "Остановиться у домика и послушать, что скажет мужчина":
            "Вы остановились. У Вас завязался диалог."
    "???" "Приветствую Вас, путники."
    petr "Я слежу за этим домом, меня зовут Петр Петрович, но вы можете называть меня Дед Петр."
    petr "Как вас зовут? Куда вы направляетесь?"
    return

# chapter 2.2
label AskForDirectionsToTheVillage:
    show petr normal at right
    $ card_shirts = 'mouth | question_mark'
    menu:
        "Представиться и спросить, какой путь ведет до деревни":
            return
        "Спросить, что Дед Петр делает в таком опасном месте":
            call AboutPetr from _call_AboutPetr
    return

label AboutPetr:
    "Дед Петр начал вам объяснять."
    petr "Я был смотрителем шахты, но недавно тут появились гоблины."
    petr "Говорят, что в пещере появился Вождь Гоблинов. Он с легкостью присвоил себе это место, ведь там не было охраны."
    petr "Наша деревня не такая большая, мы не можем позволить себе охранников."
    petr "Я не ушел из этого дома, потому что я уже стар, мне некуда пойти, тем более это мой любимый дом..."
    petr "А еще мне передали, что помощь для деревни уже в пути. Сказали, что мне надо помочь путешественникам добраться до деревни."
    petr "Это вы те самые путешественники?"
    vas "Да, мы доставляем вооружение для авантюристов из деревни!"

    $ card_shirts = 'mouth'
    menu:
        "Представиться и спросить, какой путь ведет до деревни":
            return

# chapter 2.3
label ChooseDirection:
    "Вы представились. Вам стали объяснять, как добраться до деревни."
    petr "Можно поехать прямо, но тот путь может оказаться небезопасным."
    petr "Можно поехать направо, тот путь длинный и более безопасный."
    petr "Но на этом пути много развилок, без человека знающего путь, можно потратить много времени."
    
    $ card_shirts = 'dangerous_place | road'
    menu:
        "Поехать прямо.":
            "Вы хотели отправиться прямо, но есть одно но..."
            vas "Нам нужно придумать план, как мы будем ехать по этому пути."
            vas "Ведь дальше находится данж."
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
    stop music fadeout 0.5
    play music "audio/Dungeons/Temple of Tomb.ogg" fadein 0.5 volume 0.5 loop
    scene dungeon_at_day
    $ card_shirts = 'head_and_question_mark | head_and_question_mark | head_and_question_mark'
    menu:
        "Просто проехать, вдруг повезет.":
            # show goblin at right with Dissolve(.3)
            play sound "audio/SFX/Fail_3.ogg" volume 0.5 fadeout 0.5
            show goblin at right with vpunch
            "Неудачное решение, на пути видны монстры."
            show vas normal at left with Dissolve(.5)
            vas "Это слишком опасно, давай выберем другое решение."
            hide goblin with easeoutright
            hide vas normal with easeoutleft
            call TheWayToDange from _call_TheWayToDange_1
        "Поедем медленно, но тихо.":
            play sound "audio/SFX/Fail_3.ogg" volume 0.5 fadeout 0.5
            show goblin at right with vpunch
            "Неудачное решение, на пути видны монстры."
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
    vas "Вылезла ошибка, она ругается и показывает что-то непонятное..."
    vas "Из-за нее мы видим ночью, как днем..."
    return

label Bug:
    vas "Что будем делать?"

    $ card_shirts = 'head_and_question_mark | tools'
    menu:
        "Оставим эту полезную фичу.":
            "Интересное решение, но монстры нас увидят."
            call Bug from _call_Bug_1
        "Исправить ошибку":
            "Вы стали думать над решением этой проблемы."
            vas "Exception показывает, что в строчке кода находится ошибка."
            vas "Помоги мне найти правильный ответ, пожалуйста..."
    return

label ProblemWithNight:
        $ card_shirts = 'shirt | shirt | shirt'
        menu:
            "public class Cave\n var nightLight = 10000":
                "Неправильно, попробуйте еще раз."
                call ProblemWithNight from _call_ProblemWithNight_1
            "public class Cave\n var nightLight = 1000":
                "Неправильно, попробуйте еще раз."
                call ProblemWithNight from _call_ProblemWithNight_2
            "public class Cave\n var nightLight = 10":
                "Правильно, теперь ночью стало темно!"
                vas "Проблема решена!"
                return
        return

label NextToGate:
    stop music fadeout 0.5
    play music "audio/Towns/Smooth As Glass.ogg" volume 0.035 fadein 0.5 loop 
    scene vilage_gate with fade
    show vas normal at left with Dissolve(.5)
    vas "Теперь нам надо проехать в деревню, а для этого нужно открыть ворота."
    vas "Сейчас они закрыты, но они откроются, если решить маленькую загадку."
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
    stop music
    play music "audio/Overworld/World Travelers.ogg" fadein 0.5 volume 0.04 loop
    $ card_shirts = 'mouth | head_and_question_mark | eyes'
    menu:
        "Спросить у Деда Петра путь.":
            "Дед Петр начал вам рассказывать, как добраться до деревни."
            petr "Я вам скажу, куда нужно поворачивать на развилках, а вы запоминайте, чтобы быстрее добраться до деревни."
            petr "На пути вам встретится пять развилок и один мост."
            petr "Вправо, влево, мост, прямо, влево, прямо"
            petr "Если вы пройдете так, на всех развилках, то вы попадете в деревню, если сойдете с пути, то ничего страшного, вы попадете к речке."
            vas "Хорошо, мы вас поняли, большое спасибо!"
            $ card_shirts = 'mouth'
            menu:
                "Тогда, поехали!":
                    scene forest with fade
                    "Вы ехали, пока не наткнулись на развилку."
            show vas normal at left with Dissolve(.5)
            vas "Какой путь нам лучше выбрать?"
            $ withPetr = False
            return
        "Взять с собой в путь Деда Петра.":
            "Дед Петр согласился вам показать путь до деревни."
            scene river_without_bridge with fade
            "Дед Петр показывал вам верные пути, пока вы не наткнулись на речку."
            show vas normal at left with Dissolve(.5)
            vas "На этом месте должен был быть мост, которого нету по какой то причине. Код игры показывает странную ошибку.
            Помоги найти верный варинат."
            $ withPetr = True
            return
        "Просто поехать куда глаза глядят.":
            "Мне кажется это не самый лучший вариант, мы можем запутаться."
            vas "Если мы выберем этот вариант, мы потеряем много времени, давай выберем другое решение?"
            call Right from _call_Right_1
    return

label RoadToVillage:
    $ card_shirts = 'left_arrow | right_arrow'
    $ rightChoice = False
    while(not rightChoice):
        menu:
            "Влево.":
                "Неправильно, вы потеряли время на неверный путь."
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
                "Неправильно, вы потеряли время на неверный путь."
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
            "К сожалению, неправильно. Попробуйте еще раз."
            $ coder_points -= 1
            call ProblemWithBridge from _call_ProblemWithBridge_1
        "GameObject Bridge = Instantiate(bridgePrefab, new Vector3(x, y, z), Quaternion.identity);":
            "Правильно, вы нашли правильный код!"
            vas "Проблема решена!"
            vas "Теперь можно отправляться дальше!"
            $ coder_points += 1
        "GameObject Bridge\n Instantiate(bridgePrefab, new Vector3(x, y, z), QuaternionIdentity);":
            "К сожалению, неправильно. Попробуйте еще раз."
            $ coder_points -= 1
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
                "Неправильно, вы потеряли время на неверный путь."
    
    vas "Какой путь нам лучше выбрать?"
    $ card_shirts = 'left_arrow | right_arrow'
    $ rightChoice = False
    while(not rightChoice):
        menu:
            "Влево":    
                "Правильный путь, вы поехали дальше."
                $ rightChoice = True
            "вправо":
                "Неправильно, вы потеряли время на неверный путь."
    vas "Какой путь нам лучше выбрать?"
    $ card_shirts = 'up_arrow | left_arrow'
    $ rightChoice = False
    while(not rightChoice):
        menu:
            "Прямо":
                "Правильный путь, вы поехали дальше."
                $ rightChoice = True
            "Влево":
                "Неправильно, вы потеряли время на неверный путь."

    return
label SecondPartShortWay:
    "Вы ехали, пока не наткнулись на ворота деревни."
    call NextToGate from _call_NextToGate_2
    return

# chapter 4.1
label ChoiseInVillage:
    scene blank with pixellate
    show petr normal at right
    show vas normal at left
    "Вы зашли в деревню и начали искать гильдию."
    petr "Здесь наши пути расходятся, я выполнил свое задание. Удачи вам."

    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    menu:
        "Вам тоже удачи!":
            "Вы отправились искать гильдию."
            vas "Теперь нам нужно найти гильдию, нас там уже ждут."
        "Постойте пожалуйста, скажите как нам найти гильдию?":
            petr "На здании гильдии должен быть меч, поэтому отличительному знаку вы должны быстро найти ее."
            vas "Все понял, надеюсь мы ее найдем, больше спасибо. Удачи вам."   
    
    hide petr
    call choice_in_village_menu from _call_choice_in_village_menu
    return

label choice_in_village_menu:
    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    menu:
        "Библиотека":
            vas "Хмм, библиотека пустует... В ней нет посетителей..."
            vas "Но тут есть записка! Давайте почитаем, что тут написано!"
            """Посетителей становится все меньше, потому что все боятся заходить в нашу деревню...
            Я считаю, что это из-за этих проклятых, очень сильных, гоблинов... 
            Наша библиотека вынуждена закрыться..."""
            vas "Ладно, похоже тут никого мы не найдем."
            # picture
            call choice_in_village_menu from _call_choice_in_village_menu_1
        "Мясная лавка":
            vas "Лавка выглядит заброшенной..."
            vas "Но тут есть какая-то записка! Давайте прочитаем, что тут написано!"
            """***Наша лавка пришла в упадок...
            Все из-за сильных гоблинов, которые воруют наш скот...
            По этой причине мы вынуждены закрыться...
            Всего хорошего."""
            vas "Ладно, похоже здесь никого мы точно не найдем."
            # picture
            call choice_in_village_menu from _call_choice_in_village_menu_2
        "Гильдия":
            vas "Это гильдия! Идем!"
            return
    return  
# chapter 4.2
label MeetingWithNas:
    scene blank with pixellate
    show vas normal at center
    "Вы зашли в здание и оказались правы - это гильдия."
    show vas normal at right with dissolve
    vas "Нам нужно подойти к стойке администрации, чтобы сообщить, что мы уже прибыли."
    "Вы подошли к стойке"
    show dummy at left with dissolve
    nas "Здравствуйте!" 
    nas "Меня зовут Настя, я представитель гильдии."
    nas "Зачем вы пришли?"
    vas "Мы выполняем задание от вашей деревни. Доставляем магическое оружие для ваших авантюристов."
    nas "Хорошо. Наверное вы устали с дороги, не хотите перекусить?"
    
    $ card_shirts = "dangerous_place | mouth"
    menu:
        "Отправиться в данж.":
            return
        "Перекусить.":
            nas "Давайте перекусим"
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

# Chapter 5.1
label DialogueNearDungeon:
    scene blank with pixellate
    show vas normal at left
    "Вы у входа в подземелье"
    vas "Настя сказала, что в этом подземелье начали обитать очень сильные мобы..."
    vas "Это очень сильно нарушает баланс моей игры... Интересно в чем же проблема?"
    $ card_shirts = "head_and_question_mark"
    menu: 
        "Скоро узнаем...":
            pass
    vas "Верно..."
    
    $ card_shirts = "head_and_question_mark"
    menu: 
        "Войти в подземелье":
            call inTheDungeon
    return

label inTheDungeon:
    scene blank with pixellate
    show vas normal at right    
    "Вы вошли в подземелье..."
    "Пока вы пробирались в глубь подземелья, через мокрые скалы и темные лабиринты, Вам стало очень скучно и одиноко..."
    $ card_shirts = "mouth"
    menu:
        "Поговорить с Васей о жизни":
            pass
    "Вы спросили почему Вася решил сделать свою игру"
    vas "Мне всегда нравилось играть в видеоигры, они гораздо интереснее книг и фильмов..."
    vas 'Поэтому я выучился на профессию "ГЕЙМРАЗРАБОТЧКА"'
    $ card_shirts = "question_mark"    
    menu:
        "Чем занимается геймразработчик?":
            pass
    vas "На самом деле, это очень обширное название..."
    vas "Геймразработчики делятся на разные специальности"
    vas "Над игрой трудится большое количество людей - "
    vas "Дизайнеры, Сценаристы, Программисты..."
    "Ваш мирный и душевный диалог прервали монстры..." with vpunch
    vas "ОСТОРОЖНО!!! Это те самые монстры, о которых говорили в Гильдии!"
    "Между вами и монстрами произошла небольшая стычка..."
    return

# Chapter 5.2
label BugFix:
    show vas normal at center with dissolve
    vas "Странно, такое ощущение, что мы даже не поцарапали врагов..."
    vas "Давай глянем в код игры и посмотрим, что там творится..."
    vas "Вот в чем проблема! Монстры просто бессмертны... Давай исправим этот баг!"
    show vas normal at left with dissolve
    $ card_shirts = "head_and_question_mark"
    menu:
        "За дело!":
            pass
    vas "Мы должны подобрать такое количество здоровья врагам, чтобы они не показались игроку слишком лёгкими"
    vas "или слишком сложными..."

    show vas normal at right with dissolve
    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    menu:
        "10 ХП":
            vas "Неплохое решение... Но противники теперь будут слишком простые..."
            $ coder_points += 4
        "50 ХП":
            vas "Отлично! Противники теперь будут сбалансированы!"
            $ coder_points += 6
        "100 ХП":
            vas "Плохое решение... Игрок не сумеет одолеть таких противников..."
            $ coder_points += 2
    "Вы двинулись дальше... В глубь подземелья..."
    
    vas "После битвы с монстрами, игрока обычно ждет вознаграждение..."
    vas "Давай дадим награды игроку за победу в битве!"
    vas "Но какую награду лучше выбрать...?"

    show vas normal at left with dissolve
    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    menu:
        "Зелье здоровья":
            "Отлично! Теперь у игроков будет чем восполнить недостающее здоровье!"
            $ coder_points += 6
        "Деньги":
            "Хорошо, эти деньги игрок сможет потратить в трактире! Но ему будет сложно двигаться дальше без здоровья"
            $ coder_points += 4
        "Ничего не давать":
            "Плохое решение... Игроку будет жаль потраченных сил и времени..."
            $ coder_points += 2
    vas "Хмм, по сюжету все монстры дальше станут сильнее обычного..."
    vas "Нужно дать игроку хорошую экипировку, чтобы он смог пойти дальше!"
    vas "Как думаешь, что следует вручить игроку еще?"
    
    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    menu:
        "СУПЕР ГИГА УЛЬТРА МЕЧ":
            "Противоречивое решение... Игрок с легкостью справится со всеми монстрами на следующих стычках..."
            $ is_giga_sword_is_given = True
            $ coder_points += 4
        "Сухую ветку":
            "Плохое решение... Игрок не сможет преодолеть последующих монстров..."
            $ is_stick_is_given = True
            $ coder_points += 2
        "Двуручный топор":
            "Отличное решение! Урон игрока возрос и ему не будет скучно в следующих стычках!"
            $ is_axe_is_given = True
            $ coder_points += 6

    vas "Супер! Игрок укомплектован и может двигаться дальше!"
    "Вы двинулись дальше..."
    return

# Chapter 5.3
label TheWayToBoss:
    scene blank
    show vas normal at right with dissolve
    "Пока вы шли по пещерам, у вас снова завязался душевный диалог"
    vas "А! Точно! Я же не договорил!"
    vas "Я окончил Уральский федеральный университет."
    vas 'Учился на специальности "программная инженерия"!'
    vas "Я хотел стать программистом, который пишет код для игр, и сделать свою игру... Выучил C#!"
    vas "Учёба мне далась легко. Я выбирал только те курсы, которые были мне интересны и соответствовали моей будущей профессии."
    vas "Я выбрал пары по тому формату (очно/онлайн), по которому мне было удобно..."
    vas "Поэтому я все успевал и получал много баллов за работы!"
    "Вы с упоением слушали Васину речь..."
    "Но вдруг встретили какое-то непонятное существо..."
    show dummy at center
    vas "Смотри..."
    vas "Тут стоит..."
    vas "Лама???"
    vas "Такое ощущение, что она не вписывается в лор подземелья..."
    vas "Что будем делать?"
    
    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    menu:
        "Поменяем ламу на гоблина":
            'Хорошее решение! Не стоит забывать, что наше подземелье называется "Подземелье гоблинов"'
            $ coder_points += 4
        "Оставим ламу, в качестве пасхалки":
            "Хорошее решение! Мы можем оставить эту Ламу, как пасхалку для игроков!"
            $ coder_points += 2
            $ is_the_lama_easter_egg = True
        "Поменяем ламу на скелета":
            "Отличное решение! Скелет сможет разнообразить геймплей."
            $ coder_points += 6
    vas "Замечательно!!! Моя игра становится все интереснее и интереснее!"
    vas "Остается совсем немного! Пойдемте вперед!"
    "Вы пошли вперед..."
    vas "Программист - пишет код для игры, оптимизирует ее..."
    vas "Добавляет механики в игру, придуманные геймдизайнером..."
    vas 'Геймдизайнер отвечает за сюжет игры, ее "интересность" и "необычность".'
    vas "На плечах геймдизайнера лежит задача заинтересовать игрока, увлечь его геймлпеем, сделать игру уникальной!"
    vas 'Дизайнер делает так, чтобы игра выглядела "сочно" и "вкусно".'
    vas 'Все эти специальности подходят под профессию "ГЕЙМРАЗРАБОТЧИКА"'
    vas "Поэтому очень важно определиться с тем, что тебе больше нравится!"
    vas "А какая специальность тебе больше нравится в геймдеве?"

    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    menu: 
        "Программист":
            "Чтобы выучится на программиста тебе следует подучить языки программирования, например C# / C++ / Java / Swift и другие..."
        "Геймдизайнер":
            "Чтобы выучится на геймдизайнера, тебе следует узнать, как устроены игры, уметь писать интересные сценарии и д.р"
        "Дизайнер":
            "Чтобы выучится на дизайнера тебе нужно уметь делать 3D модели / 2D модели / уметь использовать спецэффекты и д.р"
    return

label variables:
    $ coder_points = 0.0
    $ card_shirts = ""
    $ withoutWheel = False
    $ is_giga_sword_is_given = False
    $ is_stick_is_given = False
    $ is_the_lama_easter_egg = False
    return

label end:
    "THE END!"
    return
