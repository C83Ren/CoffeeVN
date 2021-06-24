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
    p "Let’s take one Shiraishi~"
    
    show hitona1 happy3

    s "Yaay let’s goo!"
    
    "I went into the booth with a very happy Shiraishi holding a bag with bishojo figure"
    
    p "Look at the screen Shiraishi, we’ll take our photo here"
    
    s "Okay!"

    "We pose wrapping our hands to each other’s shoulder"

    "{i}Click{/i}"

    show hitona1 idle2

    p "Look our photo is there Shiraishi, now we can decorate it"

    s "ooooh I want to have this big eye!"

    p "Well I want an Afro as my hair~"

    s "Shiraishi wants balloons!"

    p "And add some stars~"

    s "Fishies! Add fishies!"

    "We added a lot of decoration to our picture, but now that I thought about it…I wasn’t focusing much on the picture"

    "I wonder how it looks hmmm"

    show hitona1 smile1

    "I thought of looking at the printed picture but when I look at Shiraishi, I felt reluctant…"

    $ purikuri_flag = True
    menu:
        "Should I see the picture?"
        "yes":
            jump r1_purikuri_bad_end
        "no":
            jump r1_food_choice_purikuri
