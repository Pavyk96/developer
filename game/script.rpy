init:
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')

define vas = Character("Вася", color="#00e4fd")

# background images
image fountain_bg = im.Scale("bg/fountain.png", 1920, 1080)
image balcony_bg = im.Scale("bg/balcony.png", 1920, 1080)

# obstacle images

# enviroment images
image forest_and_road_purple_wheel_with_vasya = im.Scale("FirstChapter/forest and road final without wheel.png", 1920, 1080) 

# character sprites
image vas normal = im.Scale("FirstChapter/vasya.png.", 326, 805)
image vas big thinking = im.Scale("FirstChapter/Head and question mark.png.", 375, 705)
image vas normal thinking = im.Scale("FirstChapter/Head and question mark.png.", 250, 470)
image vas small thinking = im.Scale("FirstChapter/Head and question mark.png.", 187.5, 352.5)

# The game starts here.
label start:
    # call introdution

    # first chapter
    call firstChapter  
    return

# introdution section
label introdution:
    # show fountain_bg
    "Вася, которому мы помогали исправлять ошибки на Ulearn, закончил университет и начал разработку собственной игры."
    pause 0.5

    show vas normal
    "Один."
    "Один, в своей квартире!"
    hide vas
    return

# first chapter
label firstChapter:
    show forest_and_road_purple_wheel_with_vasya
    pause 0.5
    vas "У повозки куда-то пропало колесо!"
    vas "Можешь мне помочь?"
    vas  "Пожалуйста..."
    menu:
        "text":
            "reaction"
    $ choice_var = "mouth"
    menu:
        "text":
            "new reaction"
    return
        
label success:
    "SUCCESS!"
    return

# # map section. Chapter 1.1  
# label worldMap:
#     scene map
#     show vas normal at left
#     with fade

#     show vas cry
#     "О нет! У Васи что-то случилось!"
    
#     menu:
#         'Спросить: "Что случилось?" ':
#             call whatHappend
#         "Продолжить любоваться Васей":
#             call admireVasya
#     return



# label whatHappend:
#     vas "Я зашел в свою игру, но тут слишком много багов."
#     show vas sad
#     vas "Помоги, пожалуйста!"
#     return

# label admireVasya:
#     show vas nervous
#     pause 0.5
    
#     show vas confused
#     pause 0.5

#     show vas shocked
#     pause 0.6

#     show vas flustered
#     pause 0.2

#     show vas normal
    
#     vas """Извини, но не мог бы ты мне помочь?
    
#     Я зашел в свою игру, но тут слишком много багов.

#     Надо что-то сделать!
#     """
#     return

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