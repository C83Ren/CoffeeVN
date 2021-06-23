init python:
    f_spot1 = 0
    f_spot2 = 0
    f_hut1 = 0
    f_hut2 = 0

label r2_forest:

    label forest_menu:
        menu:
            "Where to go?"
            "Forest Spot 1":
                jump forest_spot_1
            "Forest Spot 2":
                jump forest_spot_2
            "Hut 1":
                jump forest_hut_1
            "Hut 2":
                jump forest_hut_2
            "Pathway":
                jump forest_exit

label forest_spot_1:
    if f_spot1 == 0:
        $ f_spot1 = 1

        #idle

        e "Why are you going there Hitona?"

        p "Hey I don’t see this kind of thing often you know"

        p "Oooh what’s this? Looks kinda shiny"

        e "Shiny? What’s shiny? Nothing is…oooh"

        #angry3

        e "I advised you to not touch that"

        p "Why not? It’s shiny…"

        "The one I’m looking at is shining gold and looks like a cucumber"

        e "No seriously, don’t touch it…it won’t kill you but…"

        "I pick it up"

        "…"

        "I put it back down…"

        p "WHY DIDN’T YOU TELL ME?! IT’S TURD!"

        p "SHINY TURD! HOW CAN A TURD BE THAT SHINY! NOOOOO!"

        e "It has an illusion spell to it that makes it look like gold. So yeah…"

        "Eve casted a spell to make water to wash my hands…"

        jump forest_menu

    else:

        #surprised1

        e "Why are you going there again…do you subconsciously have a fascination for turd…"

        "I looked at the thing"

        p "That thing truly looks like gold…"

        p "Who the hell would make a gold turd in the middle of the forest"

        #smug1

        e "“…Who else?! But I Majna Eden Bat Azuma Nula Sedun"

        p "“…If I wasn’t so exhausted I would slice you to pieces with this staff, not using magic, just using this blunt staff"

        jump forest_menu


label forest_spot_2:
    if f_spot2 == 0:
        $ f_spot2 = 1

        #idle

        e "I sense a magical power from here"

        p "You can do that?"

        #smug1

        e "You underestimate me too much young one"

        #smile1

        e "Ah look something is shiny! It’s a healing spell orb!"

        e "Oh but it’s a one time use, still useful to have. Take it Hitona"

        play sound correctchoice

        "You got Heal Orb"

        $ hitona_stats["item"].append("Heal Orb")

        jump forest_menu

    else:

        #idle

        p "I wonder if I can find anything else here"

        e "Naah you won’t, the great Majna doesn’t sense anything from there anymore. Let’s go"

        jump forest_menu



label forest_hut_1:
    if f_hut1 == 0:
        $ f_hut1 = 1

        #idle

        p "I wonder if anyone is home?"

        #laugh2

        e "Bring everything to the great Nula!"

        play sound dooropen

        "Eve just barged in…"

        p "Why did you do that?!"

        "But inside…it was empty and full of dust"

        #idle

        e "No one lives here Hitona dear"

        e "This place is wiped out as you can see"

        "I looked down and…there were skeletons around…"

        p "?!"

        e "Nothing to see here~"

        jump forest_menu

    else:

        #idle

        p "What do you mean this place is wiped out?"

        e "This place was one of the place where the rebels fought the army"

        e "While magic is quite useful, some are scary young Hitona. Like the one that was used here"

        p "What was used here?"

        e "You don’t want to know~ Let’s move on"

        jump forest_menu

label forest_hut_2:
    if f_hut2 == 0:
        $ f_hut2 = 1

        #smile1

        play sound dooropen

        e "Look look Hitona! What a rare fine! A spell item!"

        e "I think this one spews fire or something"

        e "It’ll break after one use so don’t use it willy nilly"

        play sound correctchoice

        "You got Flamethrower"

        $ hitona_stats["item"].append("Flamethrower")

        jump forest_menu

    else:

        #idle

        p "Can I try the item now Eve?"

        #angry3

        e "I told you it’ll break after one use"

        p "But…"

        #idle

        e "Eve will get you another spell okay little one~"

        p "Didn’t you say you were stealing the orbs…give me another!"

        #pout2

        e "It’s in my staff…"

        p "…"

        e "…"

        jump forest_menu

label forest_exit:
    menu:
        "You sure? (You won't be able to come back here again)"
        "Yes":
            jump r2_map_1
        "No":
            jump forest_menu
