label r2_turmoil:
    scene bg turmoil_front with fade
    play music storm fadein 1.0 volume 0.2
    play sound thunder loop volume 0.2

    $ renpy.pause(3.0)

    scene bg turmoil with dissolve


    p "This is such a heavy rain..."

    e "With lightning striking the ground so frequently as well."

    e "We don’t have any clue about what to do here; we probably can’t pass through here..."

    p "Can you make a storm like this with magic, Eve?"

    e "At a smaller scale, yeah."

    p "That’s oddly humble from you"

    e "That’s plenty enough to defeat small fries like the soldiers, no need to use a fancier spell."

    e "If Hitona can defeat them, why bother using such a flashy spell?"

    p "You’re mocking me, aren’t you?"

    "For some reason, Eve started patting me on the head."

    p "I’ll get you back later for this!"

    jump turmoil_menu

label turmoil_default:
    play music storm fadein 1.0
    play sound thunder loop

label turmoil_menu:
    call screen turmoil_map

label turmoil_pillar:
    "It’s a normal-looking stone pillar."

    e "Be careful not to get close to it."

    e "Lightning might strike it at any moment."

    jump turmoil_menu

label turmoil_tablet:
    "It’s a stone tablet with no inscription."

    p "What’s this doing here?"

    e "Might have to do with how we get the ultimate spell."

    e "Just remember it for now."

    jump turmoil_menu

label turmoil_world_map:
    play music adventure_bgm fadein 1.0
    stop sound

    jump map_menu
