﻿init:
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')

define vas = Character("Вася", color="#00e4fd")
define kas = Character("Касеки", color="#fbff00ff")

# background images
image portal = im.Scale("bg/portal.png", 1920, 1080)
image blank = im.Scale("bg/blank background.jpg", 1920, 1080)
image forest_without_vasa = im.Scale("bg/forest_without_vasa.png", 1920, 1080)

# character sprites
image dummy = im.Scale("character/dummy.png.", 768, 768)
image vas normal = im.Scale("FirstChapter/vasya.png.", 326, 805)
image kas normal = im.Scale("SecondChapter/kaseki.png.", 326, 805) #нужен спрайт
image vasya_at_the_computer = im.Scale("bg/Vasya at the computer.png", 1920, 1080)
image vasya_at_the_computer_surprised = im.Scale("bg/Vasya at the computer with a surprised face.png", 1920, 1080)

# mobs sprites
image goblin = im.Scale("mobs/goblin.png.", 768, 768) #нужен спрайт

# enviroment sprites
image forest_and_road_purple_wheel_with_vasya = im.Scale("FirstChapter/forest and road final without wheel.png", 1920, 1080) 
image forest_and_road_normal_with_vasya = im.Scale("FirstChapter/forest and road final.png", 1920, 1080)
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
    call SecondChapter

    # third chapter
    call ThirdChapter
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
    call ComingOfKaseki
    call AskForDirectionsToTheVillage
    call ChooseDirection
    return

label ThirdChapter:
    if (straight_or_right == "straight"):
        call TheWayToDange
        call WayAtNight
        call Bug
        call ProblemWithNight
        call NexToGate
        call ChoosingSolution
    else:
        call Right
        if (withKaseki == False):
            call RroadToVillage
        call ProblemWithBridge
        if (withKaseki == True):
            call SecondPartShortWay
            call NexToGate
        else:
            call SecondPartLongWay
            call NexToGate
        call ChoosingSolution 

# map section. Chapter 1.1      
label WorldMap:
    scene forest_without_vasa
    with fade
    show vas normal at left
    "Перед собой вы видите фэнтезийный мир и озадаченного Васю"
    
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
    with fade
    pause 2
    
    "Вася смотрел на Вас около 5 минут и не понимал, почему вы молчите"
    
    vas "Привет, я очень рад тебя видеть!"
    
    vas "Можешь мне помочь пожалуйста?"

    menu:
        'Спросить: "Что случилось?" ':
            call what_happend from _call_what_happend_1
    return

# Chapter 1.2
label BrokenCart:
    scene forest_and_road_purple_wheel_with_vasya with fade
    vas "У повозки пропало куда-то колесо."
    vas "Можешь мне помочь пожалуйста?"
    menu: 
        "Подумать над решением этой проблемы":
            "Хм{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            "Хм{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}{nw}"
            "Хм{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}{nw}"
    "Вы вместе подумали и нашли несколько решений"
    
    vas "Как ты думаешь, какой вариант лучше?"

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
    menu:
        "Почему им нужна наша помощь? Почему они не справляются сами?":
            vas "Не знаю, ахахахаха"
            vas "Но не думаю, что они просто так отправили заявку в гильдию"
            vas "Когда доедем до деревни, можешь спросить у старосты"
    "Вы поехали дальше..."
    return

# chapter 2.1
label ComingOfKaseki:
    scene blank
    with fade
    "Вы ехали, пока не наткнулись на развилку с деревянным домиком."
    "Из домика вышел немолодой мужчина."
    menu:
        "Остановится у домика и послушать мужчину":
            "Вы остановились. У Вас завязался диалог."
    show dummy at left
    "???" "Приветствую, путники."
    kas "Я слежу за этим домом, меня зовут Касеки."
    kas "Как вас зовут? Куда вы направляйтесь?"
    return

# chapter 2.2
label AskForDirectionsToTheVillage:
    show dummy at right
    "Рядом находился данж {w=1.5} {nw}"
    menu:
        "Представится и спросить, какой путь ведет до деревни Гудзё?":
            return
        "Спросить, что Касеки делает в таком опасном месте?":
            call AboutKaseki
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
    menu:
        "Представится и спросить, какой путь ведет до деревни Гудзё?":
            return

# chapter 2.3
label ChooseDirection:
    "Вы представились, вам стали объяснять, как добраться до деревни."
    kas "Можно поехать прямо, но тот путь может оказать не безопасным."
    kas "Можно поехать направо, тот путь длинный и более безопасный."
    kas "Но на этом пути много развилок, без человека знающего путь, можно потратить много времени."
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

# chapter 3.1
label TheWayToDange:
    scene dungeon_at_day
    menu:
        "Просто проехать, вдруг повезет.":
            show goblin at right with Dissolve(.3)
            "Не удачное решение, на пути видны монстры."
            show vas normal at left with Dissolve(.5)
            vas "Это будет слишком опасно, давай выберем другое решение."
            hide goblin with easeoutright
            hide vas normal with easeoutleft
            call TheWayToDange
        "Поедем медленно, но тихо.":
            "Не удачное решение, на пути видны монстры."
            show goblin at right with Dissolve(.3)
            show vas normal at left with Dissolve(.5)
            vas "Мне кажется, это будет хорошей идеей, если мы отправимся ночью, как думаешь?"
            hide goblin with easeoutright
            hide vas normal with easeoutleft
            call TheWayToDange
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
    menu:
        "Оставим эту полезную фичу.":
            "Интересное решение, но в этом случае оно не сработает."
            call Bug
        "Исправить ошибку":
            "Вы стали думать над решением этой проблемы."
            vas "Ошибка показывает, что в строчке кода находится синтаксическая ошибка."
            vas "Помоги мне найти правильный ответ, пожалуйста..."
    return

label ProblemWithNight:
        menu:
            "image.SetAttributes(new ImageAttributes().SetGamma(10f, ColorAdjustTypeBitmap));":
                "Неправильно, попробуйте еще раз."
                call ProblemWithNight
            "ImageSetAttributes(new ImageAttributes.SetGamma(2.2f, ColorAdjustType.Bitmap));":
                "Неправильно, попробуйте еще раз."
                call ProblemWithNight
            "image.SetAttributes(new ImageAttributes().SetGamma(2.2f, ColorAdjustType.Bitmap));":
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
    menu:
        "Double":
            "Неверно... Попробуйте другой ответ."
            call ChoosingSolution
        "Long":
            "Неверно... Попробуйте другой ответ."
            call ChoosingSolution
        "Float":
            return
    return

# Chapter 3.2
label Right:
    menu:
        "Спросить у Касеки путь.":
            "Касеки начал вам рассказывать, как добраться до деревни."
            kas "Я вас скажу, куда нужно поворачивать на развилках, а вы запоминайте, чтобы быстрее добраться до деревни."
            kas "На пути вам встретится, пять развилок и два моста."
            kas "Право, лево, мост, прямо, лево, мост, прямо"
            kas "Если вы пройдете так, на всех развилках, то вы попадете в деревню, если сойдете с пути, то ничего страшного, вы попадете к речке."
            vas "Хорошо, мы вас поняли, большое спасибо!"
            menu:
                "Тогда, поехали!":
                    scene forest with fade
                    "Вы ехали, пока не наткнулись на развилку."
            show vas normal at left with Dissolve(.5)
            vas "Какой путь нам лучше выбрать?"
            $ withKaseki = False
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
            call Right
    return

    


label RroadToVillage:
    menu:
        "Влево.":
            "Не правильно, вы потеряли время на неверный путь."
        "Вправо.":
            "Правильный путь, вы поехали дальше."
    vas "Какой путь нам лучше выбрать?"
    menu:
        "Влево.":
            "Правильный путь, вы поехали дальше."
        "Вправо.":
            "Не правильно, вы потеряли время на неверный путь."
    "Вы наткнулись на речку, где должен был быть мостик, но по какой-то причине его нету и показывается странную ошибку."
    vas "Что-то странное, тут должен быть мостик, но его нету."
    vas "Тут ошибка, показывает что с кодом игры что-то не так..."
    vas "Нужно правильный вариант кода, при котором мостик появится."
    scene river_without_bridge with fade
    return


label ProblemWithBridge:
    menu:
        "GameObject Bridge = Instantiate(bridgePrefab, new Vector3(xyz), Quaternion.identity);":
            "К сожалению, не правильно, попробуйте еще раз."
            call ProblemWithBridge
        "GameObject Bridge = Instantiate(bridgePrefab, new Vector3(x, y, z), Quaternion.identity);":
            "Правильно, вы нашли правильный код!"
            vas "Проблема решена!"
            vas "Теперь можно отправляться дальше!"
        "GameObject Bridge Instantiate(bridgePrefab, new Vector3(x, y, z), QuaternionIdentity);":
            "К сожалению, не правильно, попробуйте еще раз."
            call ProblemWithBridge
    return

label SecondPartLongWay:
    scene forest with fade
    show vas normal at left with Dissolve(.5)
    vas "Какой путь нам лучше выбрать?"
    menu:
        "Прямо":
            "Правильный путь, вы поехали дальше."
        "Лево":
            "Не правильно, вы потеряли время на неверный путь."
    vas "Какой путь нам лучше выбрать?"
    menu:
        "Лево":
            "Правильный путь, вы поехали дальше."
        "Право":
            "Не правильно, вы потеряли время на неверный путь."
    vas "Какой путь нам лучше выбрать?"
    menu:
        "Прямо":
            "Правильный путь, вы поехали дальше."
        "Влево":
            "Не правильно, вы потеряли время на неверный путь."


label SecondPartShortWay:
    "Вы ехали, пока не наткнулись на ворота деревни."
    vas "Теперь нужно открыть ворота, чтобы въехать в деревню."
    vas "Сейчас они закрыты, но они открываются, если решить маленькую загадку."
    return

label variables:
    $ coder_points = 0.0
    return

label end:
    "THE END!"
    return
