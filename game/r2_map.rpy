label r2_map_1:
    scene bg map

    #idle

    play sound staffsummon

    "Eve took out a map out of thin air"

    p "How do you do that!? I don’t want to carry anything either!"

    #smug1

    e "Majna Eve’s special power!"

    #idle

    e "That staff has dimensional storage spell as well. Just use that"

    p "Oh you’re right"

    "I put every of my belonging inside the storage"

    e "So look at this map"

    e "At the far right is the castle. Before that you can see a village"

    p "“…There’s only one village…how is this kingdom still here?!"

    e "Most of the cities and village are on the other side of this map"

    e "Not many people lives on this side due to these 3 places"

    e "Tranquility and Turmoil region on the upper part of the map. Rage region near the village and incidentally near the castle as well"

    p "What’s with those regions?"

    e "Those regions have huge magical power that sometimes it goes rampant and affects nearby areas"

    e "Enough of that, let’s go to the village"

    menu:
        "Where to go"
        "Village":
            jump on_to_village

    # Put button to pick village

    #jump on_to_village

label on_to_village:
    "We then walked to the village"

    #idle

    p "Eve…"

    e "What is it?"

    p "Eve…"

    #smile1

    e "Yes I am Eve the holder of emptiness itself~ Nula"

    p "Eve…"

    #smug1

    e "Yes call me Eve, the one who controls the wind of the east~"

    p "I still don’t get how the hell you call yourself Eve…"

    #laugh2

    e "I, Majna Eden Bat Azuma Nula Sedun, shall bestow you with knowledge of the origin of my name!"

    p "No let’s not…"

    jump r2_village

label r2_map_2:
    scene bg map
    python:
        m_turmoil = 0
        m_rage = 0

label map_menu:
    scene bg map
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

    #smile1

    e "Time for another adventure!!!"

    p "Yaaaaay! To be honest I am quite excited~"

    #smug1

    e "You should be! You are accompanying the great Eve~"

    p "Uuuh sure…mostly because I can use magic!! So exciting!"

    #smile2

    e "Eve understands~ When I was a little I used my first magic"

    p "What was it?"

    e "It was a spell that creates a hole in the ground"

    p "Oh that’s cool"

    e "Yeah I remember the whole village sank, good times~"

    p "…"

    jump map_menu

label map_castle:

    #idle

    p "Why are we here…"

    e "Just to take a look around~"

    e "Might as well go inside don’t you think?"

    p "No… I barely have anything with me!"

    p "And weren’t you the one who wanted me to get those ultimate spells?!"

    #smug1

    e "You’re with the great Eve, what can go wrong?"

    e "Let’s go!"

    scene black

    "Eve charged in and I had to follow her"

    "You got obliterated by innumerous amount of spell casted by the soldiers"

    "Bad End"

    return

label map_rage_1:

    scene bg rage

    play music volcano

    #idle

    p "Just looking this from here looks very intimidating"

    e "It is called Rage for a reason"

    e "We can’t pass through here anyway."

    e "That Fire wall surrounding it going to be a pain to deal with"

    p "Can’t you just use some magic of yours?"

    e "This Fire wall is the magic produced by the region"

    e "The only thing that can deal with this is another ultimate spell"

    p "You speak logical sometimes huh"

    #angry3

    e "You want me to wind blast you to that fire wall?"

    p "I will decline for now"

    play music adventure_bgm

    jump map_menu

label map_rage_2:

    scene bg rage

    play music volcano

    p "Rage sound kinda cool don’t you think?"

    #laugh2

    e "You compare such pity naming sense with Eve?"

    p "What does your name mean anyway?"

    #pout2

    e "…"

    p "…"

    e "Let’s go~"

    play music adventure_bgm

    jump map_menu

label map_tranquility:
    menu:
        "You sure? (You won't be able to come back here again)"
        "Yes":
            jump r2_tranquility
        "No":
            jump map_menu
