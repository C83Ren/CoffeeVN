label r2_turmoil:
    scene bg turmoil

    play music storm
    play sound thunder loop

    p "This is such a heavy rain…"

    e "With lightning striking the ground no less"

    e "There’s not much we can do here probably since we have no clue what to do"

    p "Can you do a magic like this storm Eve?"

    e "At a smaller scale yeah~"

    p "That’s oddly humble from you"

    e "That’s plenty enough to defeat small chumps like the soldiers, no need to be fancy"

    e "If Hitona can defeat them, why bother use such a flashy spell"

    p "You’re mocking me aren’t you"

    "Eve patted me for some reason…"

    p "I’ll get you back sometime later!"

    jump turmoil_menu

label turmoil_default:
    play music storm
    play sound thunder loop

label turmoil_menu:
    scene bg turmoil

    menu:
        "Pillar":
            "It’s a stone pillar"

            e "Better not get close to it, the lightning might strike it"

            jump turmoil_menu

        "Tablet":
            "It’s a stone tablet but there’s no inscription"

            p "What’s this doing here?"

            e "Might have to do with how we get the ultimate spell. Just remember it for now"

            jump turmoil_menu

        "World Map":
            play music adventure_bgm
            stop sound

            jump map_menu

    return
