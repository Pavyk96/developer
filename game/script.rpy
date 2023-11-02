init:
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')

define vas = Character("Vasya", color="#00e4fd")

# background images
image fountain_bg = im.Scale("bg/fountain.png", 1920, 1080)
image balcony_bg = im.Scale("bg/balcony.png", 1920, 1080)
image map = im.Scale("bg/world_map.jpg", 1920, 1080)

# obstacle images
image broken_cart = im.Scale("obstacles/broken cart.jpg", 860, 540)


# character sprites
image vas normal = im.Scale("character/boy casual normal.png.", 500, 900)
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
    call introdution

    # first chapter
    call firstChapter  
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
    scene map
    show vas normal at left
    with fade

    show vas cry
    "О нет! У Васи что-то случилось!"
    
    menu:
        'Спросить: "Что случилось?" ':
            call whatHappend
        "Продолжить любоваться Васей":
            call admireVasya
    return



label whatHappend:
    vas "Я зашел в свою игру, но тут слишком много багов."
    show vas sad
    vas "Помоги, пожалуйста!"
    return

label admireVasya:
    show vas nervous
    pause 0.5
    
    show vas confused
    pause 0.5

    show vas shocked
    pause 0.6

    show vas flustered
    pause 0.2

    show vas normal
    
    vas """Извини, но не мог бы ты мне помочь?
    
    Я зашел в свою игру, но тут слишком много багов.

    Надо что-то сделать!
    """
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