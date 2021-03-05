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

    $ purikuri_flag = True
    menu:
        "look at purikuri?"
        "yes":
            jump r1_purikuri_bad_end
        "no":
            jump r1_food_choice_purikuri
