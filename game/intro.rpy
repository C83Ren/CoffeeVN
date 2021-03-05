label start:
    scene bg room with dissolve
    play music room_bgm fadein 1.0

    # disable save until after questionnaire
    $ quick_menu = False

    "Hitona doing a rare afternoon stream. Finished the stream and talks how it was fun and she is hungry, what she'd like for dinner."

    play audio doorbell noloop
    pause 1.0

    """
    Then her bell rangs, turns out it was from the delivery guy. He brought up a huge box.

    The sender was her senpai/friend.

    Along with the box was a message saying \"Kohi you left this in your old room! Can’t believe you forgot to bring something so huge\".

    ...

    Hitona doesn’t know what her senpai/friend was talking about.

    Keeps pondering about what it is (spouting possible item it might be) none she thinks seem to fit in.

    Hitona then just proceeds in opening the package.

    She opened the package there she found something she never would’ve thought of, it was a safe.

    The safe has a lock with a 4 character password.
    """

    p "What’s this...I don’t remember even having this."

    if persistent.ed_unlocked_1 and persistent.ed_unlocked_5 and persistent.ed_unlocked_8:
        menu:
            "Try opening the box?"
            "Yes":
                $ quick_menu = True
                jump true_end
            "No":
                pass

    """
    Hitona still confused about the package, but then she just put it inside.

    Messaged the one who sent it, asking what it is about.

    Hitona went back to her computer.

    Not long after a message reply came.

    \"Kohi! I found an interesting questionnaire! Try it Try it!\"

    Hitona was interested and tried it.
    """

    menu:
        "1. Enter your name"
        "Kohi":
            $ intro_name = "Kohi"
        "Hitona":
            $ intro_name = "Hitona"
        "Kohigashi":
            $ intro_name = "Kohigashi"

    menu:
        "2. Most favourite color among these"
        "Purple":
            $ intro_color = "purple"
            $ intro_q2 = __("compassionate")
        "Pink":
            $ intro_color = "pink"
            $ intro_q2 = __("cute")
        "Yellow":
            $ intro_color = "yellow"
            $ intro_q2 = __("cheerful")
        "Black":
            $ intro_color = "black"
            $ intro_q2 = __("deep")
        "White":
            $ intro_color = "white"
            $ intro_q2 = __("pure")
        "Red":
            $ intro_color = "red"
            $ intro_q2 = __("passionate")
        "Blue":
            $ intro_color = "blue"
            $ intro_q2 = __("calm")

    menu:
        "3. Favourite food among these"
        "Pasta":
            $ intro_food = "pasta"
            $ intro_q3 = __("herself")
        "Yakiniku":
            $ intro_food = "yakiniku"
            $ intro_q3 = __("others")
        "Salad":
            $ intro_food = "salad"
            $ intro_q3 = __("both herself and others")

    "..."

    menu:
        "1107. Which one you want to keep giving?"
        "Support":
            $ route = 1
        "Joy":
            $ route = 2
        "Memories":
            $ route = 3

    "..."

    "\"{color=#a0a}{b}[intro_name]{/b}{/color} is {color=#a0a}{b}[intro_q2]{/b}{/color} to {color=#a0a}{b}[intro_q3]{/b}{/color}.\""

    p "That was a long one...for such a simple result"

    """
    Turns out answering all the questions took a lot of time and now it was midnight.

    Hitona felt sleepy and tucked in for the night.
    """

    stop music fadeout 1.5
    play sound ["<silence 5.0 loop 5.0>", alarm] loop
    scene bg room with Fade(2.0, 4.0, 3.0)
    $ quick_menu = True

    """
    Hitona got woken up by a call from someone.

    Turns out it was from her senpai that sent the mysterious package.

    Hitona still half awoke answered the phone.
    """

    stop sound
    play music ["<silence 1.0 loop 1.0>", room_bgm] fadein 3.0

    p "Morning..."

    s "Kohiiii! Morniiing! Can you meet me at the park right now?"
    s "There’s something I want to give you."
    s "Well just come okay, I’ll be waiting~"

    """
    Hitona couldn’t even said another word.

    Didn’t seem like she was going to answer her message yesterday so might as well meet with her and ask her directly.

    Hitona prepared herself, looks at the safe, sighs, then she opened the door...
    """

    if route == 1:
        jump r1_start
    elif route == 2:
        jump r2_start
    else:
        jump r3_start





# just some example stuff that never gets used

label example:
    scene bg conbini

    $ a = 3
    play music p

    "narration"

    play music p if_changed

    show hitona1 idle1

    "more narration"

    # bliss2 for one line only
    hc bliss2 "text1"

    hc "text2"

    # cry1 for one line, then switch to bliss1
    hc bliss1 @ cry1 "text3"

    hc "text4"

    "more narration [a]"

    call show_cg("BirthdayKohi") from _call_show_cg

    "More text"

    return

label utawaku_quiz_example:
    show hitona1 stareyes3
    check_lyrics hc "audio/kokoronasi.mp3" "Enter the following lyrics" "Incorrect, try again" "それはねここにあるよ"

    show hitona1 stareyes4
    hc "Correct"

label map_example:
    scene bg conbini
    show screen map_buttons

    p "This is a map."

    window hide
    $ map_active = True
    $ renpy.pause(hard=True)

default map_visits = [False, False, False]

label map_choice1:
    $ map_active = False
    $ map_visits[0] = True
    p "1"

    jump map_branch_end

label map_choice2:
    $ map_active = False
    $ map_visits[1] = True
    p "2"

    jump map_branch_end

label map_choice3:
    $ map_active = False
    $ map_visits[2] = True
    p "3"

    jump map_branch_end

label map_branch_end:
    if all(map_visits):
        jump map_final
    else:
        window hide
        $ map_active = True
        $ renpy.pause(hard=True)

label map_final:
    hide screen map_buttons

    ""
