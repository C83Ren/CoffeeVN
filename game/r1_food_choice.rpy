##(C83's comment: should we differ this scene into 2 seprate dialogue since it has bit diffrent dialogue I think...
label r1_food_choice_purikuri:
    # Don’t look at it
    # 
    # Music: Happy excited, doesn’t loop, > 3 minutes (same as before)
    # Background: Game Center
    # 
    # Hitona knew the pic was still black, so she just put it away.
    # She just thought if they could look at it together later, it seemed Shiraishi had something else in her mind.
    # Shiraishi looked a little bit down, then suddenly her stomach was grumbling.
    #
    
    "I’ll just put it away for now, it’s still black anyway"

    "Shiraishi was looking down seemed a bit off"
    
    jump r1_food_choice

label r1_food_choice_no_purikuri:
    # Don’t Take Purikuri
    #
    # Music: Happy excited, doesn’t loop, > 3 minutes (same as before)
    # Background: Game Center
    #
    # Hitona patted Shiraishi’s head and pointed out at some other games.
    # Shiraishi didn’t look disappointed. She just nodded and smiled again.
    # But before they could go around the game center, Shiraishi’s stomach grumbled.
    #

    "I patted Shiraishi"

    p "Let’s play some other stuff, like the guitar right there"

    "Shiraishi just nodded and smiled but as soon we were going to move again"

    jump r1_food_choice

label r1_food_choice:
    #
    # “Let’s go eat!” Hitona announced.
    #
    # Shiraishi looked embarrassed but she nodded right after.
    # Now where should we eat?

    "{i}Grumbleee{/i}"

    p "Let’s go eat~"

    "Shiraishi looked embarrassed but she nodded right away"

    menu:
        "Where should we eat~"
        "7/11":
            jump r1_7_11
        "family restaurant":
            jump r1_famres
