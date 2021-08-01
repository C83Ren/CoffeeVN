label quiz_pic_mechanic_init():
    $ quiz_count = 0
    $ quiz_done = []
    $ quiz_num = 0

    $ drawing_list = [
    ["1.png", _("Asking for help"), _("Distributing flyers"), _("Food delivery"), 2, _("This one’s actually not that bad."), _("Flattery won’t get you anywhere, you know.")],
    ["2.png", _("Jiangshi"), _("Vampire"), _("Dracula"), 1, _("I really couldn’t remember its name last time."), _("Well now you do, good for you.")],
    ["3.png", _("Bath"), _("Hot Springs"), _("Soap"), 3, _("You’re saying the one above his head is soap as well?"), _("I’ll leave it to your imagination.")],
    ["4.png", _("Barrel"), _("Izakaya"), _("Dining table"), 1, _("Is the food above it really necessary...?"), _("It’s the most important part.")],
    ["5.png", _("Taking an exam"), _("Focus power"), _("Studying"), 2, _("That answer is way too specific..."), _("I do wish it wasn’t this specific as well.")],
    ["6.png", _("Gyudon shop"), _("Izakaya"), _("Ramen shop"), 1, _("If it weren’t for the waiter I would’ve thought it was about just the food."), _("Even I almost forgot it wasn’t about the food.")]
    ]
    return

label quiz_pic_default:
    python:
        quiz_count = 0
        quiz_done = []
        quiz_num = 0

label quiz_pic_check:
    $ quiz_num = custom_random(quiz_done)

    if quiz_count < 6:
        $ quiz_done.append(quiz_num)
        $ quiz_count = quiz_count + 1
    else:
        play sound challengecomplete
        "Congratulations! You got all 6 correct!" id quiz_pic_check_2eaaa4a4
        jump r3_bomb

    python:
        img_str = drawing_list[quiz_num][0]
        quiz_opt1 = drawing_list[quiz_num][1]
        quiz_opt2 = drawing_list[quiz_num][2]
        quiz_opt3 = drawing_list[quiz_num][3]
        user_answer = 0

    image quiz_image = "images/r3_drawing/[img_str]"

label quiz_pic_showing:

    show quiz_image with dissolve
    play sound quizquestion
    window hide
    pause 5.0

    menu:
        "What is this drawing of?"
        "[quiz_opt1!t]":
            $ user_answer = 1
        "[quiz_opt2!t]":
            $ user_answer = 2
        "[quiz_opt3!t]":
            $ user_answer = 3
        "Look at picture again":
            jump quiz_pic_showing

    if user_answer == drawing_list[quiz_num][4]:
        play sound correctchoice
        "CORRECT"
        $ pi(drawing_list[quiz_num][5])
        $ l(drawing_list[quiz_num][6])
        jump quiz_pic_check
    else:
        play sound falsechoice_long
        "WRONG"
        jump drawing_fail
