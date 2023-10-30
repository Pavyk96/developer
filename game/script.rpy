init:
    $ config.keymap['skip'].remove('K_LCTRL')
    $ config.keymap['skip'].remove('K_RCTRL')

define vas = Character("Vasya", color="#00e4fd")
image fountain_bg = im.Scale("bg/fountain.png", 1920, 1080)
image balcony_bg = im.Scale("bg/balcony.png", 1920, 1080)
image boy_happy = im.Scale("character/boy casual happy.png", 700, 1000)
image boy_angry = im.Scale("character/boy casual angry.png.", 700, 1000)

# The game starts here.
label start:
    scene fountain_bg
    "Привет! Это Вася.
    Васе 23 года. Он - выпускник УрФУ, живет в Екатеринбурге. Один в своей квартире."
    call variables
    menu:
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.":
            call variables
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodtempor incididunt ut labore et dolore magna aliqua.":
            call variables
        "LOrem":
            pass
    return

label variables:
    return

label end:
    scene balcony_bg
    "THE END!"
    return
