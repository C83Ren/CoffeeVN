##(C83’s comment: should we differ this scene into 2 seprate dialogue since it has bit diffrent dialogue I think...
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

    "I’ll just put it away for now; it’ll still be black anyways."

    show hitona1 shy5

    "Shiraishi was looking downwards and seemed a bit strange."

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

    show hitona1 bliss3

    "I patted Shiraishi."

    p "Let’s play another game! Like... the guitar game over there."

    show hitona1 smile1

    "Shiraishi nodded and smiled, but right as we were going to move again..."

    show hitona1 shy5

    jump r1_food_choice

label r1_food_choice:
    #
    # “Let’s go eat!” Hitona announced.
    #
    # Shiraishi looked embarrassed but she nodded right after.
    # Now where should we eat?

    "{i}Grumbleee{/i}"

    "It seems like Shiraishi’s a bit hungry."

    p "Ahaha. Let’s go eat then?"

    "Shiraishi looked embarrassed and immediately nodded in agreement."

    menu:
        "Where should we go to eat?"
        "7/*1":
            $ add_choice_to_history("7/*1")
            jump r1_7_11
        "Family Restaurant":
            $ add_choice_to_history("Family Restaurant")
            jump r1_famres
