label r2_map_1:
    scene bg map with Fade(1.0, 1.0, 1.0)
    $ renpy.pause(3.0)

    #idle

    play sound staffsummon

    "Eve took out a map out of thin air"

    p "How do you do that!? I don’t want to carry anything either!"

    #smug1

    e "'Tis this Majna Eve’s special power!"

    #idle

    e "Well, that staff has a dimensional storage spell in it as well, just use that."

    p "Oh you’re right!"

    "I put all of my belongings inside the dimensional storage."

    e "So look at this map"

    e "At the far right is the castle. Before that you can see a village"

    p "...There’s only one village?! How is this kingdom still here?!"

    e "Most of the cities and villages are on the other side."

    e "Because of these three dangerous areas, there aren’t many people living over here."

    e "At the top of the map there’s the Tranquility and Turmoil regions. And then there’s the Rage region near the village and castle."

    p "What’s with those regions?"

    e "Those special regions contain a great magical power that from time to time goes rampant and impacts nearby areas."

    e "Well, enough of that, let’s go to the village!"

    call screen world_map()

    menu:
        "Where to go"
        "Village":
            jump on_to_village

    # Put button to pick village

    #jump on_to_village

label on_to_village:

    #idle

    p "Eve..."

    e "What is it?"

    p "Eve..."

    #smile1

    e "Yes, my name is Eve. I am the holder of emptiness itself!"

    p "Eve..."

    #smug1

    e "Yes, you may call me Eve! I am the one who controls the wind of the east!"

    p "I still don’t get how the hell you call yourself Eve..."

    #laugh2

    e "I see! Then, I, Majna Eden Bat Azuma Nula Sedun, shall bestow you with knowledge of the origin of my name!"

    p "Ah, there’s no need for that."

    "A bit after that, we arrived at the village."

    jump r2_village

label r2_map_2:
    scene bg map with dissolve
    python:
        m_turmoil = 0
        m_rage = 0

label map_menu:
    scene bg map
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

        #smile1

        e "Time for another adventure!!!"

        p "Yaaaaay!"

        p "To be honest, I’m really excited!"

        #smug1

        e "You should be! You are accompanying the great Eve after all!"

        p "Uuuh...sure..."

        p "More importantly, I can use magic!! So exciting!"

        #smile2

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

    #idle

    p "Why are we here..."

    e "Just to take a look around~"

    e "Since we’re here already, might as take a peek inside!"

    p "No, wait! I barely have anything with me!"

    p "And weren’t you the one who wanted me to get those ultimate spells to take down the king?!"

    #smug1

    e "Don’t worry! You’re with the great Eve, what can possibly go wrong!"

    e "Let’s go!"

    scene black with dissolve

    "Eve charged in straight through the front door!"

    "After that, we found ourselves on the receiving end of an uncountable number of spells casted by the soldiers, and were completely obliterated."

    "Bad End"

    return

label map_rage_1:

    scene bg rage with fade

    play music volcano fadein 1.0

    $ renpy.pause(3.0)

    #idle

    p "I can feel overwhelming pressure just looking at it from here."

    e "It is called Rage for a reason"

    e "In any case, we can’t pass through here."

    e "That fire wall surrounding the region is going to be a pain to deal with..."

    p "Can’t you just use some magic?"

    e "This fire wall is produced by the region’s ultimate spell."

    e "The only thing that can negate it is another ultimate spell."

    p "You make sense sometimes, huh. Sometimes."

    #angry3

    e "You want me to Wind Blast you into that fire wall?"

    p "No thanks, there’s no need for that."

    play music adventure_bgm fadein 1.0

    jump map_menu

label map_rage_2:

    scene bg rage with fade

    play music volcano fadein 1.0

    p "Rage sound kinda cool don’t you think?"

    #laugh2

    e "You dare praise such a lame name in front of this wonderfully named Eve?"

    p "By the way, what does your name mean anyway?"

    #pout2

    e "..."

    p "..."

    e "Let’s go."

    play music adventure_bgm fadein 1.0

    jump map_menu

label map_tranquility:

    "Enter Tranquility?"

    menu:
        "(Warning: you won’t be able to leave after entering)"
        "Yes":
            jump r2_tranquility
        "No":
            jump map_menu
