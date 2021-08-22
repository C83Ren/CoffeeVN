label r2_map_init():
    $ m_turmoil = 0
    $ m_rage = 0
    return

label r2_map_1:
    scene bg map with Fade(1.0, 1.0, 1.0)
    $ renpy.pause(3.0)

    show hitona2 idle with dissolve

    play sound staffsummon

    "Eve took out a map out of thin air."

    p "How do you do that!? I don’t want to carry anything either!"

    show hitona2 smug

    e "’Tis this Majna Eve’s special power!"

    show hitona2 idle

    e "Well, that staff has a dimensional storage spell in it as well, just use that."

    p "Oh you’re right!"

    "I put all of my belongings inside the dimensional storage."

    e "So look at this map."

    e "At the far right is the castle. And here on the lower left is the village."

    p "...There’s only one village?! How is this kingdom still here?!"

    e "Most of the cities and villages are much farther away."

    e "Between the village and the castle are the {color=#00c}Tranquility{/color}, {color=#00c}Turmoil{/color}, and {color=#00c}Rage{/color} regions."

    e "Because of these three dangerous areas, there aren’t many people living nearby."

    p "What’s with those regions?"

    e "Those special regions contain a great magical power that from time to time goes rampant and impacts nearby areas."

    e "Well, enough of that, let’s go to the village!"

    call screen world_map()

label on_to_village:

    show hitona2 idle with dissolve

    p "Eve..."

    e "What is it?"

    p "Eve..."

    show hitona2 smile1

    e "Yes, my name is Eve. I am the holder of emptiness itself!"

    p "Eve..."

    show hitona2 smug

    e "Yes, you may call me Eve! I am the one who controls the wind of the east!"

    p "I still don’t get how the hell you call yourself Eve..."

    show hitona2 laugh

    e "I see! Then, I, Majna Eden Bat Azuma Nula Sedun, shall bestow you with knowledge of the origin of my name!"

    p "Ah, there’s no need for that."

    "A bit after that, we arrived at the village."

    jump r2_village

label r2_map_2:
    #scene bg map with dissolve
    #python:
        #m_turmoil = 0
        #m_rage = 0

label map_menu:
    $ renpy.choice_for_skipping()
    scene bg map with fade
    call screen world_map()

    menu:
        "Where should we go?"
        "Talk":
            jump map_talk
        "Castle":
            jump map_castle
        "Turmoil":
            jump map_turmoil
        "Rage":
            jump map_rage
        "Village":
            jump village_menu
        "Tranquility":
            jump map_tranquility

label map_turmoil:
    if m_turmoil == 0:
        $ m_turmoil = 1
        jump r2_turmoil
    else:
        jump turmoil_default

label map_rage:
    if m_rage == 0:
        $ m_rage = 1
        jump map_rage_1
    else:
        jump map_rage_2

label map_talk:

    if m_rage > 0 or m_turmoil > 0:
        "{i}Seems like whenever we talk about the special regions, Eve becomes a lot more humble and serious.{/i}"

        "{i}Wonder what happened...{/i}"
    else:

        show hitona2 smile1

        e "Time for another adventure!!!"

        p "Yaaaaay!"

        p "To be honest, I’m really excited!"

        show hitona2 smug

        e "You should be! You are accompanying the great Eve after all!"

        p "Uuuh...sure..."

        p "More importantly, I can use magic!! So exciting!"

        show hitona2 smile2

        e "Ah I understand that feeling~"

        e "I was really excited when I used my first spell as a child!"

        p "What type of spell was it?"

        e "It was a spell that created a hole in the ground!"

        p "Oh that’s cool!"

        e "Yeah, I remember the whole village sank!"

        e "Good times~"

        p "..."

    jump map_menu

label map_castle:

    show hitona2 idle with dissolve

    p "Why are we here..."

    e "Just to take a look around~"

    e "Since we’re here already, might as take a peek inside!"

    p "No, wait! I barely have anything with me!"

    p "And weren’t you the one who wanted me to get those ultimate spells to take down the king?!"

    show hitona2 smug

    e "Don’t worry! You’re with the great Eve, what can possibly go wrong!"

    e "Let’s go!"

    scene black with dissolve
    stop music fadeout 1.0

    "Eve charged in straight through the front door!"

    play sound flamethrower

    "After that, we found ourselves on the receiving end of an uncountable number of spells casted by the soldiers, and were completely obliterated."

    jump bad_end

label map_rage_1:

    play music volcano fadein 1.0

    call show_cg("spreg3", False) from _call_show_cg_24

    show hitona2 idle with dissolve

    p "I can feel overwhelming pressure just looking at it from here."

    e "It is called Rage for a reason"

    e "In any case, we can’t pass through here."

    e "That fire wall surrounding the region is going to be a pain to deal with..."

    p "Can’t you just use some magic?"

    e "This fire wall is produced by the region’s ultimate spell."

    e "The only thing that can negate it is another ultimate spell."

    p "You make sense sometimes, huh. Sometimes."

    show hitona2 angry

    e "You want me to Wind Blast you into that fire wall?"

    p "No thanks, there’s no need for that."

    play music adventure_bgm fadein 1.0

    jump map_menu

label map_rage_2:
    play music volcano fadein 1.0

    call show_cg("spreg3", False) from _call_show_cg_25

    p "Rage sound kinda cool don’t you think?"

    show hitona2 laugh with dissolve

    e "You dare praise such a lame name in front of this wonderfully named Eve?"

    p "By the way, what does your name mean anyway?"

    show hitona2 pout

    e "..."

    p "..."

    e "Let’s go."

    play music adventure_bgm fadein 1.0

    jump map_menu

label map_tranquility:

    menu:
        "Enter Tranquility?\n(Warning: you won’t be able to leave after entering)"
        "Enter Tranquility":
            jump r2_tranquility
        "Don't enter Tranquility":
            jump map_menu
