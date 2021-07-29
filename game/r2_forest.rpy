init python:
    f_spot1 = 0
    f_spot2 = 0
    f_hut1 = 0
    f_hut2 = 0

label r2_forest:
    scene bg forest with fade

    label forest_menu:
        "Where to go?"
        call screen forest_map

label forest_spot_1:
    if f_spot1 == 0:
        $ f_spot1 = 1

        #idle

        e "Why are you going there Hitona?"

        p "Hey I don’t go to these types of places very often you know."

        p "Oooh what’s this? Looks kinda shiny"

        e "Shiny? What’s shiny? Nothing is...oooh"

        #angry3

        e "I advise you not to touch that"

        p "Why not? It’s shiny..."

        "It shines like gold and looks like a cucumber."

        e "No seriously. Don’t touch it. It won’t kill you but..."

        "I pick it up"

        "..."

        "I put it back down"

        p "WHY DIDN’T YOU TELL ME?!"

        p "IT’S TURD!"

        p "HOW CAN A TURD BE THAT SHINY!"

        p "NOOOOO"

        e "It has an illusion spell applied on it that makes it look like gold. So yeah..."

        "Eve casted a spell to create water so I could wash my hand."

        jump forest_menu

    else:

        #surprised1

        e "Why are you going there again? Do you have a fascination for turd?"

        p "There’s no way in hell!"

        "I looked at the thing."

        p "It really looks like gold..."

        p "Who the hell would make a gold turd in the middle of the forest..."

        #smug1

        e "...Who else?! But I, Majna Eden Bat Azuma Nula Sedun!"

        p "If I weren’t so exhausted I would slice you to pieces with this staff! Not using magic, just hitting you with this staff!"

        jump forest_menu


label forest_spot_2:
    if f_spot2 == 0:
        $ f_spot2 = 1

        #idle

        e "I perceive a certain magical power from here."

        p "You can do that?"

        #smug1

        e "You underestimate me too much, young one"

        #smile1

        e "Look, over there! It’s shining! It’s a healing spell orb!"

        e "Oh, it’s one time use, but still useful to have. Take it Hitona!"

        play sound correctchoice

        "You got Heal Orb"

        $ hitona_stats["item"].append("Heal Orb")

        jump forest_menu

    else:

        #idle

        p "I wonder if I can find anything else here..."

        e "Naah you won’t."

        e "This great Majna does not sense any magic power here."

        e "Well, there are some edible weeds I guess."

        e "If you filter some river water and eat these weeds, you can probably survive for a while."

        p "I’ll pass."

        jump forest_menu

label forest_hut_1:
    if f_hut1 == 0:
        $ f_hut1 = 1

        #idle

        p "Is anyone home?"

        #laugh2

        e "Listen up! Offer all your possessions to this great Nula!"

        play sound dooropen

        "Without any trace of courtesy, Eve barged into the house."

        p "Why did you do that?!"

        "But, there was no one inside the empty hut filled with dust."

        #idle

        e "No one lives here Hitona dear"

        e "This place is wiped out as you can see"

        e "No one is here anymore."

        "Looking down, I saw skeletons scattered across the floor."

        p "?!"

        e "There’s nothing to see here."

        jump forest_menu

    else:

        #idle

        p "What did you mean by “no one is here anymore”"

        e "This place was one of the places where the rebels fought the army."

        e "Like the one that was used here."

        p "What magic was used here…?"

        e "You don’t want to know that."

        e "Anyways, let’s go somewhere else!"

        jump forest_menu

label forest_hut_2:
    if f_hut2 == 0:
        $ f_hut2 = 1

        #smile1

        play sound dooropen

        e "Look, look, Hitona! I found a rare item! A spell orb!"

        e "I think the spell in this one spews fire or something."

        e "It seems like it’ll break after one use though, so don’t use it willy nilly."

        play sound correctchoice

        "You got Flamethrower"

        $ hitona_stats["item"].append("Flamethrower")

        jump forest_menu

    else:

        #idle

        p "Hey, Eve."

        p "Can I try using that spell orb?"

        #angry3

        e "Didn’t I say it earlier? It’ll break after one use."

        p "But..."

        #idle

        e "Haaa...I’ll get you another spell orb later, okay."

        p "Didn’t you say you were stealing the orbs?"

        p "Give me some!"

        #pout2

        e "It’s in my staff..."

        p "..."

        e "..."

        jump forest_menu

label forest_exit:

    "Leave the forest?"

    menu:
        "(Warning: you won’t be able to come back after leaving)"
        "Yes":
            jump r2_map_1
        "No":
            jump forest_menu
