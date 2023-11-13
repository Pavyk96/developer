init:
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')

define vas = Character("Вася", color="#00e4fd")

# background images
image fountain_bg = im.Scale("bg/fountain.png", 1920, 1080)
image balcony_bg = im.Scale("bg/balcony.png", 1920, 1080)
image map = im.Scale("bg/test1.png", 1920, 1080)
image vasya_at_the_computer = im.Scale("bg/Vasya at the computer.png", 1920, 1080)
image vasya_at_the_computer_surprised = im.Scale("bg/Vasya at the computer with a surprised face.png", 1920, 1080)
image portal = im.Scale("bg/portal.png", 1920, 1080)
image forest_without_vasa = im.Scale("bg/forest_without_vasa.png", 1920, 1080)

# obstacle images

# enviroment images
image forest_and_road_purple_wheel_with_vasya = im.Scale("FirstChapter/forest and road final without wheel.png", 1920, 1080) 

# The game starts here.
label start:
    call variables
    call preface

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
    show vas sad
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

# # Chapter 1.2
# label brokenCart:
#     show vas normal at left
#     show broken_cart at topright
#     vas "Повозка почему-то сломалась..."
#     hide broken_cart
#     menu:
#         "Рядом лес! Прсто сделаем новое колесо и все...":
#             "Это было долго, ты потерял много времени. Но ты справилися!"
#         "Написать грамотную функцию поиска колес":
#             call searchWheelFunction   
#         "Написать костыль, чтобы повозка ездила на трех колесах":
#             "Странно, но это сработало. Вы быстро справились с задачей! {w=3}Но теперь по всему миру трехколесные повозки..."
#     return

# label searchWheelFunction:
#     show vas sad
#     "currently unavaliable"
#     return

# # Chapter 1.3 
# label cartIsFixed:
#     hide broken_cart
#     show fixed_cart
#     vas "Поздравляю! Мы собрали повозку, теперь можем отправляться дальше"


# label end:
#     scene balcony_bg
#     "THE END!"
#     return

# label variables:
#     return