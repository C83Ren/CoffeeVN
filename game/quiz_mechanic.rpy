init python:
    def custom_random(exclude):

        randInt = renpy.random.randint(1,6)

        while randInt in exclude:
            randInt = renpy.random.randint(1,6)

        return randInt

    quiz_count = 0
    quiz_done = []
    quiz_num = 0

label quiz_check:
    $ quiz_num = custom_random(quiz_done)

    if quiz_count < 3:
        $ quiz_done.append(quiz_num)
        $ quiz_count = quiz_count + 1
        if quiz_num == 1:
            jump quiz_1
        elif quiz_num == 2:
            jump quiz_2
        elif quiz_num == 3:
            jump quiz_3
        elif quiz_num == 4:
            jump quiz_4
        elif quiz_num == 5:
            jump quiz_5
        else:
            jump quiz_6
    else:
        jump r3_bomb

label quiz_1:
    menu:
        "Who is the first heroine Hitona ever conquered?"
        "Ayatsuji":
            "WRONG"
            jump quiz_fail
        "Yuri":
            "CORRECT"
            jump quiz_check
        "Kano":
            "WRONG"
            jump quiz_fail

label quiz_2:
    menu:
        "What scent that Hitona can't take?"
        "Vanilla":
            "CORRECT"
            jump quiz_check
        "Pizza":
            "WRONG"
            jump quiz_fail
        "Verveine Hand Cream":
            "WRONG"
            jump quiz_fail

label quiz_3:
    menu:
        "In Mahjong Souls Hitona was hoping to get one out of four of these Kaavi, Aihara Mai, Suzumiya Anju, or Yagi Yui. Hitona got 2 characters from 11 pulls. At what pull Hitona got Yagi Yui?"
        "6th":
            "CORRECT"
            jump quiz_check
        "10th":
            "WRONG"
            jump quiz_fail
        "3rd":
            "WRONG"
            jump quiz_fail

label quiz_4:
    menu:
        "What was the prize in the first online crane machine Hitona tried?"
        "Hatsune Miku Birthday Figure 2020~Pop idol ver":
            "WRONG"
            jump quiz_fail
        "Re Zero kara Hajimeru Isekai Seikatsu SSS Figure Dowa Series Rem Mermaid Princess":
            "WRONG"
            jump quiz_fail
        "Marshmellow Animal Bolster Harinezumi GRAY":
            "CORRECT"
            jump quiz_check

label quiz_5:
    menu:
        "What was this paint named? Show paint"
        "Honmono no Sign":
            "CORRECT"
            jump quiz_check
        "Dai Sutaa no Sign":
            "WRONG"
            jump quiz_fail
        "Kiduki":
            "WRONG"
            jump quiz_fail

label quiz_6:
    menu:
        "The first character Hitona used in uma musume was maruzenski. The first race she didn't get first place was when she got 5th place. But who got first place?"
        "Narita Bryan":
            "CORRECT"
            jump quiz_check
        "Ines Fujin":
            "WRONG"
            jump quiz_fail
        "Grass Wonder":
            "WRONG"
            jump quiz_fail
