init:
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
image goblins = im.Scale("images/ThirdChapter/DungeonSection/goblins.png", 960, 670)
image goblin1= im.Scale("images/ThirdChapter/DungeonSection/goblin 1.png", 276, 648)
image goblin2 = im.Scale("images/ThirdChapter/DungeonSection/goblin 2.png", 321, 567)
image goblin3 = im.Scale("images/ThirdChapter/DungeonSection/goblin 3.png", 317, 530)

# enviroment sprites
image forest_and_road_purple_wheel_with_vasya = im.Scale("FirstChapter/forest and road final without wheel.png", 1920, 1080) 
image forest_and_road_normal_with_vasya = im.Scale("FirstChapter/forest and road final.png", 1920, 1080)
image forest_and_road_purple_wheel_without_vasya = im.Scale("FirstChapter/forest and road final without wheel without vasya.png", 1920, 1080)
image forest_without_vasa = im.Scale("bg/forest_without_vasa.png", 1920, 1080)
image petrHouse = im.Scale("SecondChapter/home.png", 1920, 1080)
image dungeon_at_day = im.Scale("ThirdChapter/DungeonSection/cave sun day.png", 1920, 1080)
image dungeon_at_nigth = im.Scale("ThirdChapter/DungeonSection/cave moon night.png", 1920, 1080)
image vilage_gate = im.Scale("ThirdChapter/DungeonSection/Gate.png", 1920, 1080)
image bug_with_night = im.Scale("ThirdChapter/DungeonSection/cave moon day.png", 1920, 1080)
image river_without_bridge = im.Scale("ThirdChapter/river_without_bridge.png", 1920, 1080) #нужен спрайт
image forest = im.Scale("ThirdChapter/forest.jpg", 1920, 1080) #нужен спрайт
image normal_boss_gates = im.Scale("FifthChapter/normalGates.jpg", 1920*0.5, 1080*0.5) #нужен спрайт
image strange_boss_gates = im.Scale("FifthChapter/StrangeGates.png", 1920*0.5, 1080*0.5) #нужен спрайт
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
    
    # end 
    call End
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
    call NearBoss
    call Boss
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
            $ coder_points -= 1
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")

            vas "Это было долго, мы потеряли много времени, но справились!" 
            vas "Выглядит вроде надежно, можем, наверное, отправляться дальше..."
        "Повозка сможет ехать и на трех колесах, зачем ей четвертое?":
            "Странно, но это сработало."
            call three_wheeled_carts from _call_three_wheeled_carts
    return

label chapter1_2_code_game:
    $ coder_points += 5
    $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
    
    while(True):
        $ card_shirts = 'code1 | code2 | code3'
        menu:
            "class Cart(): \n ... \n    numberOfWheels = 1":
                "Неправильно, сколько всего колес у повозки?"
                $ coder_points -= 0.5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
            "class Cart(): \n ... \n    numberOfWheels = 3":
                    "Неправильно, сколько всего колес у повозки?"
                    $ coder_points -= 0.5
                    $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
            "class Cart(): \n ... \n    numberOfWheels = 4":
                    "Правильно, теперь у повозки 4 колеса!"
                    $ coder_points += 2
                    $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
                    return
                            
label three_wheeled_carts:
    vas "Выглядит не очень надежно. Давай все-таки попробуем другой способ?"
    
    $ card_shirts = 'magnier | tools | wooden_wheel'
    menu:
        "Исправить баг в коде повозки":
            call chapter1_2_code_game from _call_chapter1_2_code_game_1
            "Мы хорошо постарались и исправили нужную переменную!"
        "Рядом лес! Просто сделаем новое колесо, да и все!":
            $ coder_points -= 1
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
            "Это было долго, мы потеряли много времени, но справились!" 
            vas "Выглядит вроде надежно, можем, наверное, отправляться дальше..."
        "Оставить все как есть":
            vas "Ну ладно, может само починится"
            $ withoutWheel = True
            $ coder_points -= 3
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
    
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
    $ card_shirts = 'fast | slow | moon'
    menu:
        "Просто быстро проехать, вдруг повезет.":
            play sound "audio/SFX/Fail_3.ogg" volume 0.5 fadeout 0.5
            show goblins at right with vpunch
            "Неудачное решение, на пути видны монстры."
            show vas normal at left with Dissolve(.5)
            vas "Это слишком опасно, давай выберем другое решение."
            hide goblins with Dissolve(.5)
            hide vas normal with Dissolve(.5)
            call TheWayToDange from _call_TheWayToDange_1
        "Поедем медленно, но тихо.":
            play sound "audio/SFX/Fail_3.ogg" volume 0.5 fadeout 0.5
            show goblins at right with vpunch
            "Неудачное решение, на пути видны монстры."
            show vas normal at left with Dissolve(.5)
            vas "Мне кажется, это будет хорошей идеей, если мы отправимся ночью, как думаешь?"
            hide goblins with Dissolve(.5)
            hide vas normal with Dissolve(.5)
            call TheWayToDange from _call_TheWayToDange_2
        "Дождаться ночи и отправится в путь.":
            "Вот этот метод может сработать, надо попробовать. Вы стали ожидать ночи."
            scene dungeon_at_nigth with fade
            show vas normal at left with Dissolve(.5)
            vas "Наступила ночь, отправляемся?"
            $card_shirts = "exclamation_mark"
            menu:
                "Да, отправляемся!":
                    return
    return

label WayAtNight:
    scene bug_with_night with pixellate
    "Но тут произошло что-то непонятное... Хоть луна и сменила солнце, светло осталось, как днем..."
    show vas normal at center with dissolve
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
        $ card_shirts = 'code5 | code6 | code7'
        menu:
            "public class Cave\n var nightLight = 10000":
                "Неправильно, попробуйте еще раз."
                $ coder_points -= 0.5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
                call ProblemWithNight from _call_ProblemWithNight_1
            "public class Cave\n var nightLight = 1000":
                "Неправильно, попробуйте еще раз."
                $ coder_points -= 0.5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
                call ProblemWithNight from _call_ProblemWithNight_2
            "public class Cave\n var nightLight = 10":
                scene dungeon_at_nigth
                $ coder_points += 2
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
                "Правильно, теперь ночью стало темно!"
                vas "Проблема решена!"
                scene black with dissolve
                "Вы успешно прошли пещеру!"
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
    $ card_shirts = 'code8 | code1 | code3'
    menu:
        "Double":
            "Неверно... Попробуйте другой ответ."
            call ChoosingSolution from _call_ChoosingSolution_2
            $ coder_points -= 0.5
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
        "Long":
            "Неверно... Попробуйте другой ответ."
            call ChoosingSolution from _call_ChoosingSolution_3
            $ coder_points -= 0.5
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
        "int":
            $ coder_points += 2
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
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
    $ card_shirts = 'code4 | code5 | code7'
    menu:
        "GameeeObject Bridge = Instantiate(bridgePrefab, new Vector3(xyz), Quaternion.identity);":
            "К сожалению, неправильно. Попробуйте еще раз."
            $ coder_points -= 0.5
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
            call ProblemWithBridge from _call_ProblemWithBridge_1
        "GameObject Bridge = Instantiate(bridgePrefab, new Vector3(x, y, z), Quaternion.identity);":
            "Правильно, вы нашли правильный код!"
            vas "Проблема решена!"
            vas "Теперь можно отправляться дальше!"
            $ coder_points += 2
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
        "GameObject Bridge\n Instantiate(bridgePrefab, new Vector3(x, y, z), QuaternionIdentity);":
            "К сожалению, неправильно. Попробуйте еще раз."
            $ coder_points -= 0.5
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
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

# TODO: deal with card shirts and sprites HERE
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

# TODO: deal with card shirts and sprites HERE
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

# TODO: deal with card shirts and sprites HERE
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
    vas "Вкусно..."
    nas "Вкусно!"
    return

# TODO: deal with card shirts and sprites HERE
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

# TODO: deal with card shirts and sprites HERE
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
    show goblins at truecenter
    "Ваш мирный и душевный диалог прервали монстры..." with vpunch
    vas "ОСТОРОЖНО!!! Это те самые монстры, о которых говорили в Гильдии!"
    "Между вами и монстрами произошла небольшая стычка..."
    hide goblins 
    return

# TODO: deal with card shirts and sprites HERE
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
            $ coder_points += 0.5
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
        "50 ХП":
            vas "Отлично! Противники теперь будут сбалансированы!"
            $ coder_points += 6
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
        "100 ХП":
            vas "Плохое решение... Игрок не сумеет одолеть таких противников..."
            $ coder_points -= 0.5
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
    
    "Вы выполнили роль геймдизайнера и программиста."
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
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
        "Деньги":
            "Хорошо, эти деньги игрок сможет потратить в трактире! Но ему будет сложно двигаться дальше без здоровья"
            $ coder_points += 2
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
        "Ничего не давать":
            "Плохое решение... Игроку будет жаль потраченных сил и времени..."
            $ coder_points += 1
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
    
    "Вы выполнили роль геймдизайнера."
    vas "Хмм, по сюжету все монстры дальше станут сильнее обычного..."
    vas "Нужно дать игроку хорошую экипировку, чтобы он смог пойти дальше!"
    vas "Как думаешь, что следует вручить игроку еще?"
    
    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    menu:
        "СУПЕР ГИГА УЛЬТРА МЕЧ":
            "Противоречивое решение... Игрок с легкостью справится со всеми монстрами на следующих стычках..."
            $ is_giga_sword_is_given = True
            $ coder_points += 3
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
        "Сухую ветку":
            "Плохое решение... Игрок не сможет преодолеть последующих монстров..."
            $ coder_points += 1.5
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
        "Двуручный топор":
            "Отличное решение! Урон игрока возрос и ему не будет скучно в следующих стычках!"
            $ coder_points += 6
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
    
    "Вы выполнили роль геймдизайнера."
    vas "Супер! Игрок укомплектован и может двигаться дальше!"
    "Вы двинулись дальше..."
    return

# TODO: deal with card shirts and sprites HERE
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
            $ coder_points += 3
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
        "Оставим ламу, в качестве пасхалки":
            "Хорошее решение! Мы можем оставить эту Ламу, как пасхалку для игроков!"
            $ coder_points += 1.5
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
            $ is_the_lama_easter_egg = True
        "Поменяем ламу на скелета":
            "Отличное решение! Скелет сможет разнообразить геймплей."
            $ coder_points += 6
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
    vas "Замечательно!!! Моя игра становится все интереснее и интереснее!"
    vas "Остается совсем немного! Пойдемте вперед!"
    hide dummy
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

# chapter 5.4
label NearBoss:
    scene blank with pixellate
    "Вы наткнулись на ворота..."
    show vas normal at left with dissolve
    vas "Мы пришли к главному боссу этого подземелья!"
    vas "Хмм... Странно... Эти ворота не должны выглядеть так..."
    show strange_boss_gates at truecenter
    vas "Давайте подберем воротам другую стилистику!"
    
    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    $ rightChoice = False
    menu:
        "Милые розовые ворота":
            "Плохое решение... Эти ворота очень сильно выбиваются из общей стилистики игры..."
            $ coder_points += 1
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
        "Брутальные металлические двери":
            "Отличное решение! Эти ворота идеально вписываются в общую стилистику подземелья!"
            $ coder_points += 6
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
            $ rightChoice = True
        "Эпичный демонический портал":
            "Хорошее решение! Но тебе не кажется странным, что демонические ворота находятся в подземелье гоблинов?"
            $ coder_points += 2
            $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
    if(rightChoice): 
        hide strange_boss_gates
        show normal_boss_gates at truecenter 
    "Вы выполнили работу дизайнера"
    vas "Теперь можно отправляться на босса..."
    vas "Вперёд!!!"
    $ card_shirts = "head_and_question_mark"
    menu:
        "Вперёд!":
            return
    return

# Chapter 5.5
label Boss:
    scene blank with pixellate
    show vas normal at right with dissolve
    "Вы столкнулись с ужасающим существом..."
    show dummy at center 
    "Вы даже не сразу поняли, что это именно босс..."
    "Вас встретила непонятная субстанция..."
    vas "О нет! Все как я и думал..."
    vas "Босс подземелья весь поражен ошибками в коде... Его настройки все слетели..."
    vas 'Давай "починим" его! Тебе как раз понадобятся все навыки геймразработчика'
    vas 'Для начала следует "присвоить" боссу правильные текстуры'

    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    $ rightChoice = False
    while(not rightChoice):
        menu:
            "Текстура скелета":
                "Вы ошиблись. Всю текстуру скелета перекосило. Попробуйте снова..."
                $ coder_points -= 0.5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
            "Текстура тёмного мага":
                "Вы ошиблись. Всю текстуру мага перекосило. Попробуйте снова..."
                $ coder_points -= 0.5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
            "Текстура гоблина":
                vas "Так держать!"
                $ coder_points += 5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
                $ rightChoice = True
                
    vas "Теперь давайте пропишем ему количество здоровья..."  
    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    $ rightChoice = False
    while(not rightChoice):
        menu:
            "1000 хп":
                vas "Так держать!"
                $ coder_points += 5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
                $ rightChoice = True
            "100 хп":
                vas "Босс получается, как сильный моб..." 
                vas "Играть не интересно. Попробуй снова!"
                $ coder_points -= 0.5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
            "10 хп":
                vas "Босс получается, совесем скучным! Даже у гоблинов больше здоровья!" 
                vas "Попробуй снова!"
                $ coder_points -= 0.5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")

    vas "Какое оружие по сценарию должен использовать король гоблинов?"   
    $ card_shirts = "head_and_question_mark | head_and_question_mark | head_and_question_mark"
    $ rightChoice = False
    while(not rightChoice):
        menu:
            "Шпагу":
                vas "Он же гоблин! Какая шпага?"
                $ coder_points -= 0.5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
            "Царский щит":
                vas "А как он будет атаковать?"
                $ coder_points -= 0.5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}") 
            "Посох с черепом":
                vas "Так держать!" 
                $ coder_points += 5
                $ renpy.notify(f"Очки разработчика {round(coder_points, 2)}")
                $ rightChoice = True

    vas "Фух, это было не просто... Но ты справился!"
    vas "Это было просто нечто! Спасибо тебе большое!"
    vas "Остается только победить этого босса!"
    vas "Вперёд!"
    if(is_giga_sword_is_given):
        "Вы моментально победили босса, потому что у вас был СУПЕР ГИГА УЛЬТРА МЕЧ!" 
        "Но вы чувствуете, что поработали не зря!"
    else:
        "Вы долго сражались с этим боссом. Но все-таки победили! Вы поработали не зря!"
    hide dummy
    vas "Неужели! В игре больше нет ошибок и багов!"
    vas "Я очень тебе благодарен!"
    vas "Теперь я могу опубликовать игру на площадках!"
    vas "Мне не терпится узнать, какие оценки она соберет!"
    # lama
    show dummy at truecenter 
    "Спустя какое-то время, Вася выложил игру на разные площадки..."
    if(coder_points < 16):
        "Васина игра не возымела большой популярности. Но Вася получил большой опыт. И начинает разрабатывать вторую часть игры!"
        "И все это ваша заслуга!"
    elif (16 <= coder_points < 22):
        "Васину игру хорошо оценили игроки. Фанаты требуют второй части! И все это ваша заслуга!"
    else:
        "Васину игра взлетела по популярности среди игроков. Она рвет все рекорды по онлайнам. И все благодаря вам!"
    return

label variables:
    $ coder_points = 0.0
    $ card_shirts = ""
    $ withoutWheel = False
    $ is_giga_sword_is_given = False
    $ is_the_lama_easter_egg = False
    $ flag = False
    return

label End:
    show black with fade
    "Конец!"
    "Над игрой работали: {w=1.2} {nw}"
    "Программист - Матушкин Антон {w=1.5} {nw}"
    "Тимлид - Мезев Даниил {w=1.5} {nw}"
    "Геймдизайнер - Кабицкий Георгий {w=1.5} {nw}"
    "Аналитик - Лещев Даниил {w=1.5} {nw}"
    "Сценарист - Воронцов Егор {w=1.5} {nw}"
    return
