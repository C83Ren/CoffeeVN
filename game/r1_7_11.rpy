label r1_7_11:
    menu:
        "where to go?"
        "home":
            jump r1_home_bad_end
        "park":
            $ r1_regrets = False
            jump r1_park_end
