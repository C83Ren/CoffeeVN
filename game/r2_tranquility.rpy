init python:
    t_talk = 0
    t_pond = 0
    t_spot1 = 0
    t_spot2 = 0
    t_spot3 = 0
    t_pond = 0
    t_oldman = 0
    t_bait1 = False
    t_bait2 = False
    t_bait3 = False
    t_fish1 = False
    t_fish2 = False
    t_fish3 = False
    t_bfish = False
    t_forest = 0
    t_pond2 = 0

label r2_tranquility:
    scene bg map with Fade(0.5, 0.5, 0.5)

    #angry3

    e "Huh? Why is the army here?"

    p "Eh really? They are probably searching for you"

    "Eve then suddenly just closes in to the soldiers"

    #laugh2

    e "Hello soldiers!!"

    p "Why would you do that!???"

    so "It’s her! Damn you little! Get her!"

    python:
        hitona_stats["hp"] = 200
        hitona_stats["hp_max"] = 200
        eve_stats["hp"] = 300
        eve_stats["spell"] = ["Wind Cutter", "Fire Ball", "Electric Bolt"]
        eve_stats["item"] = ["Heal Aura", "Flamethrower"]
        fight_order = [hitona_stats, eve_stats, soldier2_stats, soldier3_stats]
        ally_list = [hitona_stats, eve_stats]
        enemy_list = [soldier2_stats, soldier3_stats]
        fight_label = "r2_tranquility_after_battle"
        x = 0

    "FIGHT!"

    play music battletheme_bgm fadein 1.0 volume 0.5

    jump r2_fight

label r2_tranquility_after_battle:
    scene bg map with Fade(0.5, 0.5, 0.5)
    play music adventure_bgm fadein 1.0

    hide screen multi_stat

    $ hitona_stats["item"].append("Paralyzing Spark")

    $ hitona_stats["item"].append("Heal Aura")

    #idle

    e "Oh you’re getting better, still far compared to me but progress at least"

    p "You said the army doesn’t even go here anymore"

    p "This is the second time we met them"

    e "Something might be going on in the castle"

    e "Well don’t need to worry about it, let’s go in"

    "We walk into the forest and the scene was sublime…"

    scene bg tranquility with Fade(1.0, 0.5, 1.0)

    play music waterfall fadein 2.0

    p "Such a peaceful place…"

    #idle

    e "It is called Tranquility after all"

    p "The forest is so thick though"

    #angry3

    e "Shh…"

    p "Huh?"

    e "There’s someone there, prepare your staff"

    om "Don’t be alarmed young ones, I am no bad guy"

    "The old man is fishin at the pond"

    p "What’s with this scenery…"

    #hide

    "The forest was thick"

    "The greenery is enormous"

    "The waterfall is enormous as well"

    "The river flowing above is massive also but…"

    p "THAT POND IS SO SMALL!"

    p "That has a size of a small bath tub!"

    #angry3

    e "Where is all the water going though"

    e "Old man what are you doing here?"

    om "As you can see, I’m fishing"

    p "Of all places here you’re fishing…"

    #idle

    e "Well don’t mind him Hitona, let’s just find the thing"

    e "Remember \"What you seek lies deep in the water\""

label tranquility_menu:
    if t_bfish:
        menu:
            "Where should I use this fish~"
            "Forest":
                jump tranquility_forest
            "Pond":
                jump tranquility_pond_after
            "Waterfall":
                jump tranquility_waterfall
    elif t_fish1 and t_fish2 and t_fish3:
        menu:
            "Pond":
                jump tranquility_release_fishes
    else:
        menu:
            "Where should I go~"
            "Forest Spot 1":
                jump tranquility_spot_1
            "Forest Spot 2":
                jump tranquility_spot_2
            "Forest Spot 3":
                jump tranquility_spot_3
            "Pond":
                jump tranquility_pond
            "Old Man":
                jump tranquility_oldman
            "Talk":
                jump tranquility_talk

label tranquility_forest:
    if t_forest == 0:
        $ t_forest = 1
        jump tranquility_forest_1
    else:
        jump tranquility_forest_2

label tranquility_pond_after:
    if t_pond2 == 0:
        $ t_pond2 = 1
        jump tranquility_pond_after_1
    else:
        jump tranquility_pond_after_2

label tranquility_spot_1:
    if t_spot1 == 0:
        $ t_spot1 = 1
        jump tranquility_spot_1_1
    else:
        jump tranquility_spot_1_2

label tranquility_spot_2:
    if t_spot2 == 0:
        $ t_spot2 = 1
        jump tranquility_spot_2_1
    else:
        jump tranquility_spot_2_2

label tranquility_spot_3:
    if t_spot3 == 0:
        $ t_spot3 = 1
        jump tranquility_spot_3_1
    else:
        jump tranquility_spot_3_2

label tranquility_pond:
    if t_pond == 0:
        $ t_pond = 1
        jump tranquility_pond_1
    else:
        jump tranquility_pond_2

label tranquility_oldman:
    if t_oldman == 0:
        $ t_oldman = 1
        jump tranquility_oldman_1
    else:
        jump tranquility_oldman_2

label tranquility_talk:
    if t_talk == 0:
        $ t_talk = 1
        jump tranquility_talk_1
    else:
        jump tranquility_talk_2

label tranquility_talk_1:

    p "That pond is so small…"

    #angry3

    e "While that waterfall is massive"

    p "Haven’t you been here before Eve?"

    e "Believe it or not, the special regions changes over time."

    e "So yes I have been here, but it wasn’t like this"

    p "What was it when you were here before?"

    e "It was surrounded by forest, but in the middle there was a ring of water fall dropping out of nowhere"

    e "And in the middle of that ring wall, was a huge lake"

    p "I can’t imagine that"

    e "So this is much more tame than what I saw back then, be grateful"

    #idle

    e "Anyway remember ‘What you seek lies deep in the water’"

    jump tranquility_menu

label tranquility_talk_2:

    #idle

    e "Did you forget the clue already?"

    e "It’s ‘What you seek lies deep in the water’"

    p "Yeah I know, now that you keep repeating it, it is stuck in my mind"

    jump tranquility_menu

label tranquility_pond_1:

    #idle

    p "You think the spell is down there?"

    e "Most likely yeah"

    p "Use your magic Eve!"

    #angry3

    e "To drain the water?"

    p "Of course not! To swim!"

    #pout2

    e "…"

    e "The great Eve is forbidden from swimming since she was a child"

    p "…"

    p "You can’t swim can you"

    e "You can’t swim can you Hitona"

    p "…"

    e "…"

    jump tranquility_menu

label tranquility_pond_2:

    #angry3

    e "So you’re gonna swim??"

    menu:
        "Yes":
            p "Of course!"

            e "Let’s see then~"

            scene black

            "I jumped into the pond"

            "The waterfall is hitting me hard"

            "I got further and further down…"

            "And…"

            "Bad End"

            return

        "No":
            p "Of course not..."

            #idle

            e "Yeah thought so"

            jump tranquility_menu

label tranquility_spot_1_1:
    $ t_spot1 = 1

    if t_oldman > 0:

        play sound frog loop

        #idle

        "There’s a lot of frogs here…"

        "It’s kinda disturbing"

        e "We can use it as a bait, let’s take one"

        play audio correctchoice

        "Get frog as bait"

        $ t_bait1 = True

        stop sound

        jump tranquility_menu

    else:

        play sound frog loop

        #idle

        "There’s a lot of frogs here…"

        "It’s kinda disturbing"

        stop sound

        jump tranquility_menu

label tranquility_spot_1_2:
    if t_oldman > 0 and not t_bait1 and not t_fish1:

        play sound frog loop

        #idle

        e "You love frogs or something?"

        p "Uuuh not really?"

        p "I just thought we can use it as bait, let’s take one"

        play audio correctchoice

        "Get frog as bait"

        $ t_bait1 = True

        stop sound

        jump tranquility_menu

    elif t_bait1 or t_fish1:

        play sound frog loop

        #idle

        e "You sure you don’t love frogs"

        p "Now I’m not so sure…"

        stop sound

        jump tranquility_menu

    else:

        play sound frog loop

        #idle

        e "You love frogs or something?"

        p "Uuuh not really?"

        stop sound

        jump tranquility_menu

label tranquility_spot_2_1:
    $ t_spot2 = 1

    if t_oldman > 0:

        #idle

        e "That’s a weird space for those to gather"

        p "What are you talking about?"

        "Eve pointed to a certain spot"

        p "What is that pink thing…It’s….kinda moving"

        "Eh?"

        #smile2

        "She pushed me…"

        p "What are you doooo AAAAAAAAAAAAAAAA"

        #idle

        e "Yeah what is a massive amount of worms doing there I wonder"

        p "EEEEVEEEE"

        e "Well calm down, we can use it as a bait, let’s take one"

        play sound correctchoice

        "Get worm as bait"

        $ t_bait2 = True

        jump tranquility_menu

    else:

        #idle

        e "That’s a weird space for those to gather"

        p "What are you talking about?"

        "Eve pointed to a certain spot"

        p "What is that pink thing…It’s….kinda moving"

        "Eh?"

        #smile2

        "She pushed me…"

        p "What are you doooo AAAAAAAAAAAAAAAA"

        #idle

        e "Yeah what is a massive amount of worms doing there I wonder"

        p "EEEEVEEEE"

        jump tranquility_menu

label tranquility_spot_2_2:
    if t_oldman > 0 and not t_bait2 and not t_fish2:

        #smile2

        p "You remember that place Eve?"

        "I put my biggest smile ever"

        #surprised1

        e "Yeah…let’s take one as a bait…"

        play sound correctchoice

        "Get worm as bait"

        $ t_bait2 = True

        jump tranquility_menu

    elif t_bait2 or t_fish2:

        p "Do we have to go there again…"

        #smile2

        e "You might like them eventually"

        p "I could say the same to you…"

        #angry3

        e "Yeah let’s go back…"

        jump tranquility_menu

    else:
        p "Want to go there again Eve?"

        #surprised1

        e "That smile on your face makes me say no"

        jump tranquility_menu

label tranquility_spot_3_1:
    $ t_spot3 = 1

    if t_oldman > 0:
        "There was a black wall at that part of the forest"

        p "What a weird big black wall doing in the forest?"

        #angry3

        e "Hitona you really think that’s a wall?"

        "I felt pushed...and it was towards the black wall"

        "…"

        "The black wall dispersed…"

        #smile1

        e "Catch one Hitona! We can use it as a bait!"

        p "I got one…one cockroach…Why you pushed me?!"

        e "So you don’t have any second thought about it"

        p "I should note that tactic down"

        play sound correctchoice

        "Get \"bug\" as bait"

        $ t_bait3 = True

        jump tranquility_menu

    else:
        "There was a black wall at that part of the forest"

        p "What a weird big black wall doing in the forest?"

        #angry3

        e "Hitona you really think that’s a wall?"

        "I felt pushed...and it was towards the black wall"

        "…"

        "The black wall dispersed…"

        #smile1

        p "Let’s go back…"

        "Eve patted me"

        e "How can you see a massive amount of cockroaches as a wall"

        p "Don’t comment on it…"

        jump tranquility_menu

label tranquility_spot_3_2:
    if t_oldman > 0 and not t_bait3 and not t_fish3:

        #idle

        e "Surely now you know that isn’t a black wall right Hitona?"

        p "I know!"

        e "We can use it as a bait so let’s take one"

        play sound correctchoice

        "Get \"bug\" as bait"

        $ t_bait3 = True

        jump tranquility_menu

    elif t_bait3:

        #idle

        p "I never knew you can use bug as a bait"

        e "Yeah me neither"

        p "…"

        e "What?"

        jump tranquility_menu

    else:

        #angry3

        e "Are you testing your luck again thinking there won’t be any cockroaches Hitona?"

        p "Shut up will you!"

        jump tranquility_menu

label tranquility_oldman_1:

    #idle

    e "So old man, can you help us?"

    e "We’re trying to find something probably under this small pond"

    e "Any idea how?"

    p "Huh? We’re asking him?!"

    om "Under the water? Easy! You fish it!"

    p "Seriously…?"

    e "I’ll try using magic then~"

    play sound magiccasting

    e "I call the mana of aquos, break free!"

    "Nothing happened"

    p "Uuuh nothing happened though?”"

    #pout2

    e "This pond…is blocking magic…"

    om "Like I said. You fish!"

    e "I guess we got no choice"

    om "Bring me bait then I’ll help you fish it"

    p "Time to find some bait"

    jump tranquility_menu

label tranquility_oldman_2:
    om "You got some bait?"

    menu:
        "Which bait to give?"
        "Frog" if t_bait1:
            $ fish_string = "Big Fish"
            $ t_bait1 = False
            $ t_fish1 = True
        "Worm" if t_bait2:
            $ fish_string = "Medium Fish"
            $ t_bait2 = False
            $ t_fish2 = True
        "Bug" if t_bait3:
            $ fish_string = "Small Fish"
            $ t_bait3 = False
            $ t_fish3 = True
        "Cancel":
            jump tranquility_menu

    om "A nice bait this is, let’s try it"

    "The old man fished using the bait"

    play sound fishing

    "You get [fish_string]"

    if t_fish1 and t_fish2 and t_fish3:
        jump tranquility_after_fishing

    jump tranquility_menu

label tranquility_after_fishing:
    p "We got no spell…"

    p "WE GOT NO SPELL!"

    #angry3

    e "Yeah I can see that Hitona, calm down"

    p "Why are you so calm when you’re usually so weird"

    om "Are you two going to eat the fishes?"

    p "No probably not"

    om "Then release it back to the pond~"

    om "That is the way of fisherman"

    jump tranquility_menu

label tranquility_release_fishes:
    menu:
        "What should I do..."
        "Release the fishes":
            om "The fishes will truly bless you young girl"

            p "I sure hope so…"

            "I released the fishes then…"

            play sound fishing

            "The pond lighted up and out of the pond one massive fish came out"

            "The fish is SO HUGE that I’m sure it can clog up pretty much anything"

            p "Fish…"

            "I just stood there in awe"

            python:
                t_fish1 = False
                t_fish2 = False
                t_fish3 = False
                t_bfish = True

            #surprised1

            e "That fish holds amazing amount of magical power as well…it’s not the Ultimate spell but that fish packs a huge punch"

            p "What are we gonna do with this…"

            jump tranquility_menu

        "Cancel":
            "I need more time to think"

            jump tranquility_menu

label tranquility_forest_1:
    $ t_forest = 1

    #idle

    e "Are you going to use the fish there?"

    p "The clue might be a trick to make us look away from the forest!"

    e "Okay let’s try releasing the fish there!"

    "We released the fish right in the middle of the forest"

    "BOOM!"

    #angry3

    "It fell with a thump"

    play sound fishflap loop

    "And now…it’s flailing around…."

    p "Doesn’t seem like it’s working…"

    e "I even feel sorry for the fish"

    e "Okay ‘Amafi’ come back here to the storage"

    p "You’re naming that fish???"

    stop sound

    jump tranquility_menu

label tranquility_forest_2:

    #angry3

    e "You’re gonna let Amafi go through that kind of experience again Hitona??”"

    p "No I wasn’t…Don’t make look like I’m the bad guy here!"

    jump tranquility_menu

label tranquility_pond_after_1:
    $ t_pond2 = 1

    #angry3

    p "Let’s try dropping this fish to the pond"

    e "I really doubt the fish can fit into that pond"

    p "But it came from the pond!"

    e "That is one magical pond I tell you"

    p "Let’s just try it"

    "We dropped the fish to the pond but…"

    p "It’s stuck…"

    e "Yeah it’s stuck…"

    p "Let’s put it back"

    jump tranquility_menu

label tranquility_pond_after_2:

    p "How the hell that fish came from that pond"

    #smug1

    e "I can cast a spell that make you huge as well, wanna try?"

    p "That is kind of useful"

    e "Only for half a second though"

    p "I take back my admiration…"

    jump tranquility_menu

label tranquility_waterfall:

    #idle

    p "How about we let the fish swim up the waterfall"

    e "That…actually might work?"

    "We then released the fish to the waterfall"

    p "It’s actually swimming up there…"

    "It reached the top of the waterfall then it clogged the stream"

    p "The waterfall stopped…"

    stop music fadeout 1.0

    #surprised1

    e "That fish is surely huge huh"

    "We looked at the pond and it was dried up"

    "The pond was really deep, might as well call it a well"

    p "There! Something is shining there!"

    #idle

    play sound magiccasting

    e "Wind among us, elevate~"

    "As Eve casted the spell, the shiny blue orb lifted up and landed on my hands"

    "Then suddenly the orb entered my body"

    #smile1

    e "Congrats, the wind didn’t lie"

    e "You are the second salvation Hitona"

    "…"

    stop music

    jump r2_final
