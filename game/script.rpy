init:
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')

define vas = Character("Вася", color="#00e4fd")

# background images
image portal = im.Scale("bg/portal.png", 1920, 1080)
image forest_without_vasa = im.Scale("bg/forest_without_vasa.png", 1920, 1080)

# character sprites

# character sprites
image vas normal = im.Scale("FirstChapter/vasya.png.", 326, 805)
image vasya_at_the_computer = im.Scale("bg/Vasya at the computer.png", 1920, 1080)
image vasya_at_the_computer_surprised = im.Scale("bg/Vasya at the computer with a surprised face.png", 1920, 1080)

# enviroment sprites
image forest_and_road_purple_wheel_with_vasya = im.Scale("FirstChapter/forest and road final without wheel.png", 1920, 1080) 
image forest_and_road_normal_with_vasya = im.Scale("FirstChapter/forest and road final.png", 1920, 1080)
# The game starts here.
label start:
    call variables

    # introduction
    call Preface

    # first chapter
    call FirstChapter  
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
    call WorldMap
    call BrokenCart
    call CartIsFixed
    return

# map section. Chapter 1.1  
label WorldMap:
    scene forest_without_vasa
    with fade
    show vas normal at left
    "Перед собой вы видите фэнтезийный мир и озадаченного Васю"
    
    menu:
        'Спросить: "Что случилось?" ':
            call what_happend
        "Оглядеться и оценить обстановку":
            call admire_vasya
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
    
    "Вася смотрел на вас около 5 минут и не понимал, почему вы молчите"
    
    vas "Привет, я очень рад тебя видеть!"
    
    vas "Можешь мне помочь пожалуйста?"

    menu:
        'Спросить: "Что случилось?" ':
            call what_happend
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
        "Изменить код, чтобы части от повозки искались сами, рядом в лесу":
            call chapter1_2_code_game
            vas "Мы хорошо постарались и исправили нужную функцию!"
            "Выглядит надёжно, теперь вы можете отправляться дальше!"
        "Рядом лес! Просто сделаем новое колесо, да и все!":
            $ coder_points -= 0.2
            vas "Это было долго, мы потеряли много времени, но справились!" 
            vas "Выглядит вроде надежно, можем, наверное, отправляться дальше..."
        "Повозка сможет ехать и на трех колесах, зачем ей четвертое?":
            "Странно, но это сработало."
            call three_wheeled_carts
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
        "Изменить код, чтобы части от повозки искались сами, рядом в лесу":
            call chapter1_2_code_game
            "Мы хорошо постарались и исправили нужную функцию!"
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
            call chapter1_3_where_to
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

label variables:
    $ coder_points = 0.0
    return

label end:
    "THE END!"
    return
