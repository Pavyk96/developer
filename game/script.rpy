init:
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
image kas normal = im.Scale("SecondChapter/kaseki.png.", 326, 805)
image vasya_at_the_computer = im.Scale("bg/Vasya at the computer.png", 1920, 1080)
image vasya_at_the_computer_surprised = im.Scale("bg/Vasya at the computer with a surprised face.png", 1920, 1080)

# enviroment sprites
image forest_and_road_purple_wheel_with_vasya = im.Scale("FirstChapter/forest and road final without wheel.png", 1920, 1080) 
image forest_and_road_normal_with_vasya = im.Scale("FirstChapter/forest and road final.png", 1920, 1080)
# The game starts here.
label start:
    call variables from _call_variables

    # introduction
    call Preface from _call_Preface

    # first chapter
    call FirstChapter from _call_FirstChapter  

    # second chapter
    call SecondChapter
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
    return

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

label variables:
    $ coder_points = 0.0
    return

label end:
    "THE END!"
    return
