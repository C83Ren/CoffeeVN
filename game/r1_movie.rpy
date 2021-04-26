label r1_movie:
    # Go to the movie
    #
    # Music: Happy excited, doesn’t loop, > 3 minutes (same as before)
    # Background: Cinema
    #
    # They arrived at the cinema. Saw there were two movies that were playing today.
    # One was horror and the other was romance.
    # “Shiraishi, which one do you want to watch?”
    # “I’ll leave it to Hitona neechan~”.
    # So it’s obvious which one right?

    menu:
        "So it’s obvious which one right?"
        "Horror Movie":
            "Horror movie dialogue"
        "Romance Movie":
            "Romance movie dialogue"
        
    # Shiraishi then asked “Would you watch a movie again someday?”.
    # Surely you know what to say
    menu:
        "watch again?"
        "i don't know":
            jump r1_movie_bad_end
        "definitely":
            jump r1_after_movie
