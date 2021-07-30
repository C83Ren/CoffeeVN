init python:
   purikuri_flag = False

label r1_purikuri:
    # Take Purikuri
    #
    # Music: Happy excited, doesn’t loop, > 3 minutes (same as before)
    # Background: Game Center
    #
    # Hitona and Shiraishi went in to the booth.
    # They tinkered around with the features and when it seemed good enough they took the picture.
    # Hitona took the picture and went out of the booth.
    # Hitona was going to look at the picture but she saw Shiraishi then feel little bit reluctant.
    # What will you do?
    p "Why don’t we take a picture?"

    show hitona1 happy3

    s "Yaay let’s goo!"

    "I went into the booth with a very happy Shiraishi holding the bishoujo figure."

    p "Face that way Shiraishi! I’m taking the photo now!"

    s "Okay!"

    "We pose with our hands wrapped around each others’ shoulders."

    window hide
    $ renpy.pause(0.5, hard=True)
    with Fade(0.1, 0.0, 0.5, color="#fff")
    $ renpy.pause(0.5, hard=True)

    show hitona1 idle2

    p "That was a great photo! Let’s go decorate it now!"

    s "Ooooh then I want to have these big eyes!"

    p "Ah, then I want an afro for my hair!"

    s "Let’s add some balloons!"

    p "Some stars too!"

    s "Fishies! Add some fishies too!"

    "We added all sorts of things to our photo, but now that I thought about it..."

    p "{i}Hmm? What did the final photo look like...?{/i}"

    "...it seems like I can’t remember what the photo we just decorated looks like."

    p "{i}Maybe I should take a peek at it?{/i}"

    show hitona1 smile1

    "I thought of taking a look at the printed picture, but when I looked at Shiraishi, I felt a bit reluctant."

    $ purikuri_flag = True

    menu:
        "Look at the picture?"
        "Look at it":
            jump r1_purikuri_bad_end
        "Don’t look at it":
            jump r1_food_choice_purikuri
