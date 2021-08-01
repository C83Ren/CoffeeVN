init python:
    def custom_random(exclude):

        randInt = renpy.random.randint(0,5)

        while randInt in exclude:
            randInt = renpy.random.randint(0,5)

        return randInt

label quiz_mechanic_init():
    $ quiz_count = 0
    $ quiz_done = []
    $ quiz_num = 0
    return

label quiz_default:
    python:
        quiz_count = 0
        quiz_done = []
        quiz_num = 0

label quiz_check:
    $ quiz_num = custom_random(quiz_done)

    if quiz_count < 3:
        $ quiz_done.append(quiz_num)
        $ quiz_count = quiz_count + 1
        if quiz_num == 0:
            jump quiz_1
        elif quiz_num == 1:
            jump quiz_2
        elif quiz_num == 2:
            jump quiz_3
        elif quiz_num == 3:
            jump quiz_4
        elif quiz_num == 4:
            jump quiz_5
        else:
            jump quiz_6
    else:
        play sound challengecomplete
        "Congratulations! You got all 3 correct!"
        jump r3_sing

label quiz_1:
    menu:
        "Who is the very first heroine that Hitona Kohigashi conquered?"
        "Ayatsuji":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail
        "Yuri":
            play sound correctchoice
            "{b}CORRECT{/b}"
            pi "I would have never picked her as the first one if I knew how she was..."
            jump quiz_check
        "Kano":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail

label quiz_2:
    menu:
        "Which of the following scents does Hitona Kohigashi dislike?"
        "Vanilla":
            play sound correctchoice
            "{b}CORRECT{/b}"
            pi "Vanilla scent is too sweet for me too. I like the smell of fresh yakiniku though!"
            jump quiz_check
        "Pizza":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail
        "Verveine Hand Cream":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail

label quiz_3:
    menu:
        "In the game called Mahjong Soul, Hitona Kohigashi was hoping to get one at least out of the following four from gacha: Kaavi, Aihara Mai, Suzumiya Anju, and Yagi Yui. Within 11 pulls, she pulled two of the four, but on which pull did she get Yagi Yui?"
        "2nd":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail
        "6th":
            play sound correctchoice
            "{b}CORRECT{/b}"
            pi "Believe in the power of your pinky!"
            jump quiz_check
        "11th":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail

label quiz_4:
    menu:
        "What was the prize in the very first online crane machine Hitona Kohigashi attempted?"
        "Hatsune Miku Birthday Figure 2020~Pop idol ver~":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail
        "Re:Zero kara Hajimeru Isekai Seikatsu SSS Figure Dowa Series - Rem = Mermaid Princess":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail
        "Marshmellow Animal Bolster (Harinezumi GRAY)":
            play sound correctchoice
            "{b}CORRECT{/b}"
            pi "This game is a money sink...I need to be careful."
            jump quiz_check

label quiz_5:
    image honmono_sign = "images/honmono no sign.png"
    window hide
    show honmono_sign with dissolve:
        yalign 0.5
        xalign 0.5
    $ renpy.pause(5.0)
    menu:
        "What is the name of this famous piece of art?"
        "Honmono no Sign":
            play sound correctchoice
            "{b}CORRECT{/b}"
            pi "You know, it looks more like a drawing than a sign."
            jump quiz_check
        "Honjin no Sign":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail
        "Kimi wa Boku":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail
        "See picture again":
            jump quiz_5

label quiz_6:
    menu:
        "In the game called Uma Musume, during the first time that Hitona Kohigashi tried to raise Maruzensky, she came in 5th place during the Nippon Derby. Who came in first place?"
        "Narita Taishin":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail
        "Ines Fujin":
            play sound correctchoice
            "{b}CORRECT{/b}"
            pi "It’s always sad to see someone failing even though they've tried so hard."
            jump quiz_check
        "Mihono Bourbon":
            play sound falsechoice_long
            "{b}WRONG{/b}"
            jump quiz_fail
