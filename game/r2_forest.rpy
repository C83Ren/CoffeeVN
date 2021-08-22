label r2_forest_init():
    $ f_spot1 = 0
    $ f_spot2 = 0
    $ f_hut1 = 0
    $ f_hut2 = 0
    return

label r2_forest:

    label forest_menu:
        $ renpy.choice_for_skipping()
        scene bg forest with fade
        call screen forest_map

label forest_spot_1:
    if f_spot1 == 0:
        $ f_spot1 = 1

        show hitona2 idle with dissolve

        e "Why are you going there [player_name]?" id forest_spot_1_46eaf765

        p "Hey I don’t go to these types of places very often you know."

        p "Oooh what’s this? Looks kinda shiny"

        e "Shiny? What’s shiny? Nothing is...oooh"

        show hitona2 angry

        e "I advise you not to touch that"

        p "Why not? It’s shiny..."

        "It shines like gold and looks like a cucumber."

        e "No seriously. Don’t touch it. It won’t kill you but..."

        "I picked it up." id forest_spot_1_0f21d916

        p "..." id forest_spot_1_a20cefa7

        "I put it back down." id forest_spot_1_87bb6f24

        p "WHY DIDN’T YOU TELL ME?!"

        p "IT’S TURD!"

        p "HOW CAN A TURD BE THAT SHINY!"

        p "NOOOOO!" id forest_spot_1_ab382a4f

        e "It has an illusion spell applied on it that makes it look like gold. So yeah..."

        "Eve casted a spell to create water so I could wash my hand."

        jump forest_menu

    else:

        show hitona2 surprised with dissolve

        e "Why are you going there again? Do you have a fascination for turd?"

        p "There’s no way in hell!"

        "I looked at the thing."

        p "It really looks like gold..."

        p "Who the hell would make a gold turd in the middle of the forest..."

        show hitona2 smug

        e "...Who else?! But I, Majna Eden Bat Azuma Nula Sedun!"

        p "If I weren’t so exhausted I would slice you to pieces with this staff! Not using magic, just hitting you with this staff!"

        jump forest_menu


label forest_spot_2:
    if f_spot2 == 0:
        $ f_spot2 = 1

        show hitona2 idle with dissolve

        e "I perceive a certain magical power from here."

        p "You can do that?"

        show hitona2 smug

        e "You underestimate me too much, young one."

        show hitona2 smile1

        e "Look, over there! It’s shining! It’s a healing spell orb!"

        e "Oh, it’s one time use, but still useful to have. Take it [player_name]!" id forest_spot_2_2b2870c7

        play sound correctchoice

        "{b}You have obtained a Heal Orb!{/b}"

        $ hitona_stats["item"].append("Heal Orb")

        jump forest_menu

    else:

        show hitona2 idle with dissolve

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

        show hitona2 idle with dissolve

        p "Is anyone home?"

        show hitona2 laugh

        e "Listen up! Offer all your possessions to this great Nula!"

        play sound dooropen

        "Without any trace of courtesy, Eve barged into the house."

        p "Why did you do that?!"

        "But, there was no one inside the empty hut filled with dust."

        show hitona2 idle

        e "No one lives here, [player_name] dear." id forest_hut_1_a75df0d8

        e "This place is wiped out as you can see."

        e "No one is here anymore."

        "Looking down, I saw skeletons scattered across the floor."

        p "?!"

        e "There’s nothing to see here."

        jump forest_menu

    else:

        show hitona2 idle with dissolve

        p "What did you mean by “no one is here anymore”"

        e "This place was one of the places where the rebels fought the army."

        e "While there are many useful magics, there are also scary ones, young [player_name]." id forest_hut_1_c5422492

        e "Like the one that was used here."

        p "What magic was used here...?"

        e "You don’t want to know that."

        e "Anyways, let’s go somewhere else!"

        jump forest_menu

label forest_hut_2:
    if f_hut2 == 0:
        $ f_hut2 = 1

        show hitona2 smile1 with dissolve

        play sound dooropen

        e "Look, look, [player_name]! I found a rare item! A spell orb!" id forest_hut_2_0ed097b3

        e "I think the spell in this one spews fire or something."

        e "It seems like it’ll break after one use though, so don’t use it willy nilly."

        play sound correctchoice

        "{b}You have obtained a Flamethrower!{/b}"

        $ hitona_stats["item"].append("Flamethrower")

        jump forest_menu

    else:

        show hitona2 idle with dissolve

        p "Hey, Eve."

        p "Can I try using that spell orb?"

        show hitona2 angry

        e "Didn’t I say it earlier? It’ll break after one use."

        p "But..."

        show hitona2 idle

        e "Haaa...I’ll get you another spell orb later, okay."

        p "Didn’t you say you were stealing the orbs?"

        p "Give me some!"

        show hitona2 pout

        e "It’s in my staff..."

        p "..."

        e "..."

        jump forest_menu

label forest_exit:


    menu:
        "Leave the forest?\n(Warning: you won’t be able to come back after leaving)"
        "Leave the forest":
            jump r2_map_1
        "Remain in the forest":
            jump forest_menu
