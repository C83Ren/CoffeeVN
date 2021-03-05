label r1_purikuri:
    $ purikuri_flag = True
    menu:
        "look at purikuri?"
        "yes":
            jump r1_purikuri_bad_end
        "no":
            jump r1_food_choice_purikuri
