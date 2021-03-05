label r1_movie:
    menu:
        "watch again?"
        "i don't know":
            jump r1_movie_bad_end
        "definitely":
            jump r1_regret_choice
