init python:
    quiz_count = 0
    quiz_done = []
    quiz_num = 0

    drawing_list = [
    ["1.png", "Asking for help", "Distributing flyer", " Food delivery", 2, "This is actually not that bad", "Flattery won't get you anywhere"],
    ["2.png", "Jiangshi", "Vampire", "Dracula", 1, "Before I really can't remember its name", "Well now you do, good for you"],
    ["3.png", "Bath", "Onsen", "Soap", 3, "You're saying the one above his head is soap as well?", "I'll leave it to your imagination"],
    ["4.png", "Barrel", "Izakaya", "Dinner", 1, "Is the dinner above it really necessary...", "It's the most important part of this"],
    ["5.png", "Taking exam", "Focus Power", "Studying", 2, "That answer is oddly specific...", "I'll tell you as well, I wish it wasn't this specific"],
    ["6.png", "Gyudon Shop", "Izakaya", "Ramen Shop", 1, "Without the staff I would've thought it's just the food", "Even I almost forgot it wasn't about the food"]
    ]

label quiz_pic_default:
    python:
        quiz_count = 0
        quiz_done = []
        quiz_num = 0

label quiz_pic_check:
    $ quiz_num = custom_random(quiz_done)

    if quiz_count < 3:
        $ quiz_done.append(quiz_num)
        $ quiz_count = quiz_count + 1
    else:
        play sound challengecomplete
        "Congratulation! You got all 3 correct!"
        jump r3_sing

    python:
        img_str = drawing_list[quiz_num][0]
        quiz_opt1 = drawing_list[quiz_num][1]
        quiz_opt2 = drawing_list[quiz_num][2]
        quiz_opt3 = drawing_list[quiz_num][3]
        user_answer = 0

    image quiz_image = "images/r3_drawing/[img_str]"

    show quiz_image with dissolve
    play sound quizquestion

    menu:
        "What is this drawing?"
        "[quiz_opt1]":
            $ user_answer = 1
        "[quiz_opt2]":
            $ user_answer = 2
        "[quiz_opt3]":
            $ user_answer = 3

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
