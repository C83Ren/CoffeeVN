label r2_tranquility_setup():
    $ t_talk = 0
    $ t_pond = 0
    $ t_spot1 = 0
    $ t_spot2 = 0
    $ t_spot3 = 0
    $ t_pond = 0
    $ t_oldman = 0
    $ t_bait1 = False
    $ t_bait2 = False
    $ t_bait3 = False
    $ t_fish1 = False
    $ t_fish2 = False
    $ t_fish3 = False
    $ t_bfish = False
    $ t_forest = 0
    $ t_pond2 = 0
    return

label r2_tranquility:
    scene bg map with Fade(0.5, 0.5, 0.5)

    show hitona2 angry with dissolve

    e "Huh? Why is the army here?"

    p "Eh really? They are probably searching for you..."

    "But as I said that, Eve had already left to greet the soldiers."

    show hitona2 laugh with dissolve

    e "Hello soldiers!"

    p "Idiot! Why would you do that!?"

    show soldier with dissolve
    show soldier as soldier_s:
        xalign 1.0
        ypos 1080

    so "It’s her! Get her!"

    p "..."

    $ save_enabled = False

    hide hitona2
    hide soldier
    hide soldier_s

    python:
        hitona_stats["hp"] = 200
        hitona_stats["hp_max"] = 200
        eve_stats["hp"] = 300
        eve_stats["spell"] = ["Wind Cutter", "Fire Ball", "Electric Bolt"]
        eve_stats["item"] = ["Heal Aura", "Flamethrower"]
        fight_order = [hitona_stats, eve_stats, soldier2_stats, soldier3_stats]
        fight_list = [eve_stats, soldier2_stats, soldier3_stats]
        ally_list = [hitona_stats, eve_stats]
        enemy_list = [soldier2_stats, soldier3_stats]
        fight_label = "r2_tranquility_after_battle"
        x = 0

    play music battletheme_bgm fadein 1.0 volume 0.5

    jump r2_fight

label r2_tranquility_after_battle:
    $ save_enabled = True
    scene bg map with Fade(0.5, 0.5, 0.5)
    play music adventure_bgm fadein 1.0 volume 0.5

    hide screen multi_stat
    hide screen multi_sprite

    window hide
    $ renpy.pause(3.0)

    $ hitona_stats["item"].append("Paralyzing Spark")

    $ hitona_stats["item"].append("Heal Aura")

    play sound correctchoice

    "{b}You have obtained a Paralyzing Spark!{/b}"

    play sound correctchoice

    "{b}You have obtained a Heal Aura!{/b}"

    show hitona2 idle with dissolve

    e "Ooh, you’re getting better!"

    e "Still far compared to this great Eve, but progress is progress!"

    p "I thought the army doesn’t even come here anymore..."

    e "Something might be going on in the castle." id r2_tranquility_after_battle_9c01ae39

    e "Well, no need to worry about it, let’s go into the forest!"

    "We walked into the forest filled with a serene and sublime atmosphere."

    call show_cg("spreg1", False)
    play music waterfall fadein 2.0

    $ renpy.pause(3.0)

    scene bg tranquility with dissolve

    p "Such a peaceful place..."

    show hitona2 idle with dissolve

    e "It is called Tranquility after all."

    p "The forest is so thick though..."

    show hitona2 angry

    e "Shh..."

    p "Huh?"

    e "There’s someone there, prepare your staff."

    "???" "Don’t be alarmed young ones, I ain’t no bad guy."

    "It’s an old man fishing in a pond."

    p "What’s with this place..."

    hide hitona2

    "The forest was too thick."

    "The amount of greenery was overwhelming."

    "The waterfall is enormous."

    "The river flowing above the waterfall is way too wide."

    "But..."

    p "ISN’T THAT POND TOO SMALL?!!!"

    p "I’ve seen bathtubs larger than that?!"

    show hitona2 angry

    p "Where the heck is all that water from the waterfall going to?!"

    e "Old man, what are you doing here?"

    om "As you can see, I’m just fishing."

    p "The pond is so small, there can’t be any fish in there though?!"

    show hitona2 idle

    e "Well don’t mind him, Hitona. Let’s just find that thing."

    e "Remember, {b}“What you seek lies deep in the water.”{/b}"

label tranquility_menu:
    scene bg tranquility with fade
    call screen tranquility_map

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

    p "That pond is really so small..."

    p "I’m pretty sure I’ve seen puddles larger than that..."

    show hitona2 angry with dissolve

    e "While that waterfall is massive, right?"

    p "Haven’t you been here before, Eve?"

    e "Believe it or not, the special regions changes over time."

    e "So yes, I have been here before, but it’s my first time seeing this pond."

    p "What was it when you were here in the past?"

    e "It was surrounded by forest like this, but in the middle there was a ring of waterfalls dropping out of nowhere."

    e "And in the middle of that ring of waterfalls was a huge lake."

    p "I can’t picture that at all."

    e "Well, this is much more tame than what I saw back then, we should be grateful."

    show hitona2 idle

    e "Anyway remember, {b}“What you seek lies deep in the water.”{/b}"

    jump tranquility_menu

label tranquility_talk_2:

    show hitona2 idle with dissolve

    e "Did you forget the hint already?"

    e "It’s {b}“What you seek lies deep in the water.”{/b}"

    p "Yes, yes, you’ve been repeating it nonstop that there’s no way I could forget it."

    jump tranquility_menu

label tranquility_pond_1:

    show hitona2 idle with dissolve

    p "You think the ultimate spell is down there?"

    e "Probably, yeah."

    p "Use your magic Eve!"

    show hitona2 angry

    e "To drain the water?"

    p "Of course not! To swim!"

    show hitona2 pout

    e "..."

    e "The great Eve has been forbidden from swimming ever since she was born."

    p "..."

    p "You can’t swim, can you?"

    e "You can’t swim, can you, Hitona?"

    p "..."

    e "..."

    jump tranquility_menu

label tranquility_pond_2:

    show hitona2 angry with dissolve

    menu:
        e "So you’re gonna swim??"
        "Of course!":
            p "Of course!"

            e "Well, go on."

            stop music fadeout 1.0

            scene black

            "I jumped into the pond"

            "The pressure from the waterfall is overwhelming."

            "I’m being pushed down and down."

            "I keep sinking further and further down."

            "There doesn’t seem to be a bottom to this lake."

            "I...can’t...move..."

            jump bad_end

        "Of course not...":
            p "Of course not..."

            show hitona2 idle

            e "Yeah, thought so"

            jump tranquility_menu

label tranquility_spot_1_1:
    $ t_spot1 = 1

    if t_oldman > 0:

        play sound frog loop

        show hitona2 idle with dissolve

        p "There’s a disturbing amount of frogs here..." id tranquility_spot_1_1_3af2fb24

        e "Well, we can use it as bait, let’s grab one."

        play audio correctchoice

        "{b}You have obtained a slimy frog!{/b}"

        $ t_bait1 = True

        stop sound

        jump tranquility_menu

    else:

        play sound frog loop

        show hitona2 idle with dissolve

        p "There’s a disturbing amount of frogs here..." id tranquility_spot_1_1_3af2fb24_1

        stop sound

        jump tranquility_menu

label tranquility_spot_1_2:
    if t_oldman > 0 and not t_bait1 and not t_fish1:

        play sound frog loop

        show hitona2 idle with dissolve

        e "Do you love frogs or something?"

        p "Uuuh not really?"

        p "I just thought that we could use it as bait, so we should grab one."

        play audio correctchoice

        "{b}You have obtained a slimy frog!{/b}"

        $ t_bait1 = True

        stop sound

        jump tranquility_menu

    elif t_bait1 or t_fish1:

        play sound frog loop

        show hitona2 idle with dissolve

        e "Are you sure you don’t love frogs?"

        p "Now I’m not so sure anymore..."

        stop sound

        jump tranquility_menu

    else:

        play sound frog loop

        show hitona2 idle with dissolve

        e "Do you love frogs or something?"

        p "Uhhh not really?"

        stop sound

        jump tranquility_menu

label tranquility_spot_2_1:
    $ t_spot2 = 1

    if t_oldman > 0:

        show hitona2 idle with dissolve

        e "That’s a weird space for those to gather."

        p "What are you talking about?"

        "Eve pointed to a certain spot."

        p "What is that pink thing...It’s...moving..."

        p "Eh?"

        show hitona2 smile2

        "Eve pushed me from behind into the pink...something."

        p "What are you doooo-aaaaaAAAAAAAAAAAA"

        show hitona2 idle

        e "Yeah, what are such a massive amount of worms doing over there~"

        p "EEEEVEEEE!!!!!"

        e "Well calm down, we can use it as bait, so go grab one."

        play sound correctchoice

        "{b}You have obtained a slimy worm!{/b}"

        $ t_bait2 = True

        jump tranquility_menu

    else:

        show hitona2 idle with dissolve

        e "That’s a weird space for those to gather."

        p "What are you talking about?"

        "Eve pointed to a certain spot."

        p "What is that pink thing...It’s...moving..."

        "{i}Eh?{/i}"

        show hitona2 smile2

        "Eve pushed me from behind into the pink...something."

        p "What are you doooo-aaaaaAAAAAAAAAAAA"

        show hitona2 idle

        e "Yeah, what are such a massive amount of worms doing over there~"

        p "EEEEVEEEE!!!!!"

        jump tranquility_menu

label tranquility_spot_2_2:
    if t_oldman > 0 and not t_bait2 and not t_fish2:

        show hitona2 smile2 with dissolve

        p "You remember that place, Eve?"

        "I put on my biggest smile"

        show hitona2 surprised

        e "Yeah...let’s take one as bait and go..."

        play sound correctchoice

        "{b}You have obtained a slimy worm!{/b}"

        $ t_bait2 = True

        jump tranquility_menu

    elif t_bait2 or t_fish2:

        p "Do we have to go there again...?"

        show hitona2 smile2

        e "You might start liking them, you know."

        p "I could say the same back to you..."

        show hitona2 angry

        e "Y...Yeah, let’s go back..."

        jump tranquility_menu

    else:
        p "Want to go there again, Eve?"

        show hitona2 surprised with dissolve

        e "That smile on your face makes me say no."

        jump tranquility_menu

label tranquility_spot_3_1:
    $ t_spot3 = 1

    if t_oldman > 0:
        "There was a black wall at this part of the forest."

        p "What’s this weird big black wall doing in the middle of this forest?"

        show hitona2 angry with dissolve

        e "Hitona, do you really think that’s a wall?"

        "Saying that, Eve pushed me from behind towards the black wall."

        p "..."

        "The black wall dispersed."

        p "..."

        show hitona2 smile1

        e "Catch one Hitona! We can use it as bait!"

        p "..."

        play sound correctchoice

        "{b}You have obtained a cockroach!{/b}"

        p "I got one...cockroach..."

        p "Why did you push me!?"

        e "So that you wouldn’t have any second thoughts about it."

        p "I should note that tactic down..."

        $ t_bait3 = True

        jump tranquility_menu

    else:
        "There was a black wall at this part of the forest."

        p "What’s this weird big black wall doing in the middle of this forest?"

        show hitona2 angry with dissolve

        e "Hitona, do you really think that’s a wall?"

        "Saying that, Eve pushed me from behind towards the black wall."

        p "..."

        "The black wall dispersed."

        p "..."

        show hitona2 smile1

        p "Let’s go back..."

        "Eve patted my head"

        e "How did you see a massive amount of cockroaches as a wall?"

        p "Don’t comment on it..."

        jump tranquility_menu

label tranquility_spot_3_2:
    if t_oldman > 0 and not t_bait3 and not t_fish3:

        show hitona2 idle with dissolve

        e "Surely now you know that isn’t a black wall, right Hitona?"

        p "I know!"

        e "We can use it as a bait, so go catch one."

        play sound correctchoice

        "{b}You have obtained a cockroach!{/b}"

        $ t_bait3 = True

        jump tranquility_menu

    elif t_bait3:

        show hitona2 idle with dissolve

        p "I never knew you could use cockroaches as a fishing bait..."

        e "Yeah me neither..."

        p "..."

        e "What?"

        jump tranquility_menu

    else:

        show hitona2 angry with dissolve

        e "Are you testing your luck again hoping that there won’t be any cockroaches, Hitona?"

        p "Shut up will you!"

        jump tranquility_menu

label tranquility_oldman_1:

    show hitona2 idle with dissolve

    e "So old man, can you help us out?"

    e "We’re trying to find something that’s probably at the bottom of this small pond."

    e "Any idea how?"

    p "Huh? We’re asking him?!"

    om "Under the water? Easy! You fish it!"

    p "Seriously...?"

    e "I’ll try using magic then!"

    play sound magiccasting

    e "I call the mana of aquos, break free!"

    $ renpy.pause(2.0, hard=True)

    p "..."

    "Nothing happened." id tranquility_oldman_1_a37ef08e

    p "Umm nothing happened though?”"

    show hitona2 pout

    e "This pond...is blocking magic..."

    om "Didn’t I say? You fish it!"

    e "I guess we have no choice..."

    om "Well, if you bring me the bait, I can help you fish."

    p "Time to find some bait I guess."

    jump tranquility_menu

label tranquility_oldman_2:
    om "You got some bait?"

    menu:
        "Which bait to give?"
        "Frog" if t_bait1:
            $ fish_string = _("Big Fish")
            $ t_bait1 = False
            $ t_fish1 = True
            $ bait_name = _("frog")
        "Slimy Worm" if t_bait2:
            $ fish_string = _("Medium Fish")
            $ t_bait2 = False
            $ t_fish2 = True
            $ bait_name = _("slimy worm")
        "Cockroach" if t_bait3:
            $ fish_string = _("Small Fish")
            $ t_bait3 = False
            $ t_fish3 = True
            $ bait_name = _("cockroach")
        "Cancel":
            jump tranquility_menu

    om "This is a nice bait."

    "The old man tried to fish with the [bait_name!t] bait."

    play sound fishing

    "A [fish_string!t] was fished out!"

    if t_fish1 and t_fish2 and t_fish3:
        jump tranquility_after_fishing

    jump tranquility_menu

label tranquility_after_fishing:
    p "We got no spell..."

    p "WE GOT NO SPELL!"

    show hitona2 angry with dissolve

    e "Yeah I can see that Hitona, calm down."

    p "You’re always so crazy, so why are you suddenly calm now?"

    om "Are you two going to eat the fish?"

    p "No, probably not."

    om "Then you should release it back to the pond."

    om "‘Tis the way of fishers."

    jump tranquility_menu

label tranquility_release_fishes:
    menu:
        "What to do?"
        "Release the fish":
            om "The god of fish will surely bless you."

            p "I sure hope so..."

            "When I released the fish..."

            play sound fishing

            "...the pond suddenly lit up, and from the bottom jumped out a massive fish."

            "So massive, that it was surely impossible for it to have fit in that small pond."

            p "Fish..."

            "I just stood there in awe"

            python:
                t_fish1 = False
                t_fish2 = False
                t_fish3 = False
                t_bfish = True

            show hitona2 surprised

            e "That fish, it’s not the ultimate spell, but it still holds an amazing amount of magical power."

            p "What are we going to do with this fish..."

            "For now, we decided to put it in the dimensional storage."

            "{b}You have obtained a massive fish!{/b}"

            jump tranquility_menu

        "Don’t release the fish":
            p "I need more time to think..." id tranquility_release_fishes_6adf49f3

            jump tranquility_menu

label tranquility_forest_1:
    $ t_forest = 1

    show hitona2 idle with dissolve

    e "Are you going to use the fish here in the forest...?"

    p "The clue might be a trick to make us look away from the forest!"

    e "Okay let’s try releasing the fish there!"

    "We released the fish right in the middle of the forest"

    "{size=100}BOOM!{/size}"

    show hitona2 angry

    "It fell with a loud thump onto the ground..."

    play sound fishflap loop

    "...and now it’s flailing and bouncing up and down."

    p "Nothing happened..."

    e "I even feel sorry for the fish."

    e "Okay, Amafi, come back here to the dimensional storage."

    p "You even named it?!"

    stop sound

    jump tranquility_menu

label tranquility_forest_2:

    show hitona2 angry with dissolve

    e "You’re gonna let Amafi go through that kind of experience again?"

    p "No I wasn’t! Don’t make me look like I’m the bad guy here!"

    jump tranquility_menu

label tranquility_pond_after_1:
    $ t_pond2 = 1

    show hitona2 idle with dissolve

    p "Let’s try releasing this fish in the pond."

    e "Umm...I really doubt the fish can fit into that pond...it’s too big."

    p "Wait, hold on, but it came from this very pond!"

    e "This is one magical pond after all."

    p "Ah, whatever, let’s just try it."

    "We dropped the fish back into the pond but..."

    p "It’s stuck..."

    e "Yeah, it’s stuck..."

    "...it was so big, it covered the entire pond instead."

    p "Let’s put it back into the dimensional storage."

    jump tranquility_menu

label tranquility_pond_after_2:

    p "How the hell did that fish come out from that pond?"

    show hitona2 smug with dissolve

    e "I can cast a spell that makes you huge as well, want to try?"

    p "That sounds kind of useful."

    e "Only for half a second though."

    p "Give me back the admiration I just gave you!"

    jump tranquility_menu

label tranquility_waterfall:

    show hitona2 idle with dissolve

    p "How about we let the fish swim up the waterfall?"

    e "That...actually might work?"

    "We released the fish into the waterfall and let it swim in the waterfall..."

    p "It’s actually swimming up there..."

    "...and it reached the top of the waterfall without problems, blocking the flow of water."

    p "The waterfall disappeared..."

    stop music fadeout 1.0

    show hitona2 surprised

    e "That fish is surely huge, huh."

    "We looked at the pond and it too had dried up."

    "The hole left behind was so deep, the bottom could not be seen. But in the hole..."

    p "There! Something is shining!"

    "Something was shining."

    show hitona2 idle

    play sound magiccasting

    e "Wind among us, elevate!"

    $ renpy.pause(2.0, hard=True)

    "As Eve cast her the spell, a shining blue orb flew up from the hole, and landed gently in my open hands."

    "Then, the orb entered my body on its own."

    show hitona2 smile1

    e "Congratulations, the wind didn’t lie this time."

    e "You are indeed the second salvation that will save this world, Hitona."

    p "..."

    stop music

    jump r2_final
