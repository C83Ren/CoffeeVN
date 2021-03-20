label r1_7_11:
    # 7/11
    # 
    # Music: Happy excited, doesn’t loop, > 3 minutes (same as before)
    # Background: Convenience Store
    # 
    # Hitona and Shiraishi arrived at 7/11.
    # Similar with before, Shiraishi was very excited but this time she kept holding Hitona’s hand.
    # Shiraishi asked “What will be having for lunch Hitona nee chan?”.
    # “Whatever you like~”. “I want to have Hitona neechan’s recommendation!”.
    # What will you give?

    menu:
        "What will you give?"
        "Item 1":
            "Item 1 Dialogue here"
        "Item 2":
            "Item 2 Dialogue here"
        "Item 3":
            "Item 3 Dialogue here"
    
    # “Sounds yummy!”. They proceed buying the goods, found somewhere to sit and eat the goodies.
    # The choices will reflect on whether it is good okay or bad. Shiraishi will mention about the stream regardless.
    # “Eh? Stream? What do you mean?”
    # “Hitona neechan streams about reviewing food right? I love those! Gush talk~”
    # “Did I ever mention about streaming?”. Shiraishi just smiled and continued eating what she had.
    # Both of them stuffed themselves with food.
    # Now it seemed that Shiraishi had calmed down, it even looks like she was feeling sleepy.
    # What should I do?
    
    menu:
        "where to go?"
        "home":
            jump r1_home_bad_end
        "park":
            $ r1_regrets = False
            jump r1_park_end
