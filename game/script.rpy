init:
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')

define vas = Character("Vasya", color="#00e4fd")

# background images
image fountain_bg = im.Scale("bg/fountain.png", 1920, 1080)
image balcony_bg = im.Scale("bg/balcony.png", 1920, 1080)
image map = im.Scale("bg/test1.png", 1920, 1080)
image vasya_at_the_computer = im.Scale("bg/Vasya at the computer.png", 1920, 1080)
image vasya_at_the_computer_surprised = im.Scale("bg/Vasya at the computer with a surprised face.png", 1920, 1080)
image portal = im.Scale("bg/portal.png", 1920, 1080)
image forest_without_vasa = im.Scale("bg/forest_without_vasa.png", 1920, 1080)

# obstacle images
image broken_cart = im.Scale("obstacles/broken cart.jpg", 860, 540)


# character sprites
image vas normal = im.Scale("character/vasya.png.", 500, 900)
image vas sad = im.Scale("character/boy casual sad.png.", 500, 900)
image vas happy = im.Scale("character/boy casual happy.png", 500, 900)
image vas angry = im.Scale("character/boy casual angry.png.", 500, 900)
image vas nervous = im.Scale("character/boy casual nervous.png.", 500, 900)
image vas flustered = im.Scale("character/boy casual flustered.png.", 500, 900)
image vas confused = im.Scale("character/boy casual confused.png.", 500, 900)
image vas shocked = im.Scale("character/boy casual shocked.png.", 500, 900)
image vas cry = im.Scale("character/boy casual cry.png.", 500, 900)

# The game starts here.
label start:
    call variables
    call preface
    call introdution

    # first chapter
    call firstChapter  
    return

#  Предисловие Pavyk96
label preface:
    show vasya_at_the_computer
    "Вася, которому мы помогали исправлять ошибки на Ulearn, закончил университет и начал разработку собственной игры."
    "У него возникли проблемы в создании игры, появились баги, которые нужно исправить, и в этом ему очень нужна ваша помощь!"
    show vasya_at_the_computer_surprised
    pause 2
    show portal
    "После чего вы попадает вместе с Васей в игру..." 
    return

# introdution section
label introdution:
    show fountain_bg
    show vas normal
    "Привет! Это Вася."
    "Васе 23 года."
    "Он - выпускник УрФУ, живет в Екатеринбурге."
    show vas sad
    "Один."
    show vas happy
    "Один, в своей квартире!"
    show vas angry
    hide vas
    return

# first chapter
label firstChapter:
    call worldMap
    call brokenCart
    return

# map section. Chapter 1.1  
label worldMap:
    scene forest_without_vasa
    with fade
    show vas normal at left
    "Перед собой вы видите фэнтезийный мир и озадаченного Васю"
    
    menu:
        'Спросить: "Что случилось?" ':
            call whatHappend
        "Оглядеться и оценить обстановку":
            call admireVasya
    return



label whatHappend:
    vas "Я зашел в свою игру, но тут слишком много багов."
    vas "Помоги, пожалуйста!"
    return

label admireVasya:
    show forest_without_vasa
    show vas normal at left
    with fade
    
    vas """*Вася смотрел на вас около 5 минут и не понимал, почему вы молчите*
    
    Привет, я очень рад тебя видеть!
    
    Можешь мне помочь пожалуйста?
    """

    menu:
        'Спросить: "Что случилось?" ':
            call whatHappend
    return

# Chapter 1.2
label brokenCart:
    show vas normal at left
    show broken_cart at topright
    vas "Повозка почему-то сломалась..."
    hide broken_cart
    menu:
        "Рядом лес! Прсто сделаем новое колесо и все...":
            "Это было долго, ты потерял много времени. Но ты справилися!"
        "Написать грамотную функцию поиска колес":
            call searchWheelFunction   
        "Написать костыль, чтобы повозка ездила на трех колесах":
            "Странно, но это сработало. Вы быстро справились с задачей! {w=3}Но теперь по всему миру трехколесные повозки..."
    return

label searchWheelFunction:
    show vas sad
    "currently unavaliable"
    return

label end:
    scene balcony_bg
    "THE END!"
    return

label variables:
    return