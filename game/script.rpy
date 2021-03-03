define player = Character(_('Hitona'), color="#880088")
define hc = Character(_('Hitona'), color="#338833", image="hitona1")

label start:
    scene bg conbini

    # play music "music.ogg"

    "narration"

    show hitona1 idle1

    "more narration"

    # bliss2 for one line only
    hc bliss2 "text1"

    hc "text2"

    # cry1 for one line, then switch to bliss1
    hc bliss1 @ cry1 "text3"

    hc "text4"

    "more narration"

    call show_cg("BirthdayKohi")

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

    player "This is a map."

    window hide
    $ map_active = True
    $ renpy.pause(hard=True)

default map_visits = [False, False, False]

label map_choice1:
    $ map_active = False
    $ map_visits[0] = True
    player "1"

    jump map_branch_end

label map_choice2:
    $ map_active = False
    $ map_visits[1] = True
    player "2"

    jump map_branch_end

label map_choice3:
    $ map_active = False
    $ map_visits[2] = True
    player "3"

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
