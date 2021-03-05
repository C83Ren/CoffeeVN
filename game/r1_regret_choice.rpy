label r1_regret_choice:
    menu:
        "do you have regrets?"
        "yes":
            $ r1_regrets = True
        "no":
            $ r1_regrets = False
    jump r1_park_end
