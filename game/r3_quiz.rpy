label r3_quiz:
    scene bg quiz with fade

    play sound lightswitch

    "Then the room lighted up again, showing a quiz like room"

    l "First up is a quiz challenge! Get 3 out of 3 and you shall pass~"

    l "If not…you don’t want to know what happen next do you?"

    show hitona3 smile hat

    pi "Don’t worry Hitona, this first part is usually easy"

    p "Huh? You’ve been here before?"

    show hitona3 smug hat

    "Pierrot didn’t answer, she just smiled smugly"

    l "Go on to the podium"

    "Wondering about all this I just walked to the podium"

    l "Let’s start!"

    play sound quizstart

    "QUIZ START"

    hide hitona3 with dissolve

    jump quiz_default

label quiz_fail:
    scene bg quiz

    show lios front at lios_right with dissolve

    "Someone with a black cape suddenly appeared in front of us"

    l "So much for being a great detective…"

    # hitona says this as well ^

    show hitona3 pout hat at hitona_left with dissolve
    #show lios front at lios_right behind hitona3

    pi "Hey don’t blame me! You were the one answering!"

    l "You kept quite cause you don’t know the answer either right"

    show hitona3 surprised2 hat

    "Pierrot looked away and whistled"

    l "Off you go little girls~"

    stop music fadeout 1.0

    scene bg room with Fade(1.0, 1.0, 1.0)

    play music room_bgm fadein 3.0 volume 0.2

    p "Eh? I’m in my room? On my bed…"

    p "Even if that was a dream, I wonder what was stolen…"

    "I looked up at my phone"

    p "…"

    p "AAAAAAA I’M SO SORRY SENPAI!"

    "I rushed out of the room"

    scene black with dissolve

    "While going to the park that dream kept spinning in my head"

    "I wonder what was that all about"

    "I guess I will never figure out what that dream was all about"

    "Dream stay as dream huh"

    return
