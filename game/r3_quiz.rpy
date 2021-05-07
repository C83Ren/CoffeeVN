label r3_quiz:
    scene bg quiz

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

    $ quiz_count = 0
    $ quiz_done = []

    jump quiz_check

label quiz_menu:
    menu:
        "Did you succeed?"
        "Yeah!":
            jump r3_bomb
        "Nope~":
            jump quiz_fail

label quiz_fail:
    scene bg quiz

    show lios front

    "Someone with a black cape suddenly appeared in front of us"

    l "So much for being a great detective…"

    # hitona says this as well ^

    show hitona3 pout hat at hitona_left
    show lios front at lios_right behind hitona3

    pi "Hey don’t blame me! You were the one answering!"

    l "You kept quite cause you don’t know the answer either right"

    show hitona3 surprised2 hat

    "Pierrot looked away and whistled"

    l "Off you go little girls~"

    scene bg room

    p "Eh? I’m in my room? On my bed…"

    p "Even if that was a dream, I wonder what was stolen…"

    "I looked up at my phone"

    p "…"

    p "AAAAAAA I’M SO SORRY SENPAI!"

    "I rushed out of the room"

    scene black

    "While going to the park that dream kept spinning in my head"

    "I wonder what was that all about"

    "I guess I will never figure out what that dream was all about"

    "Dream stay as dream huh"

    return
