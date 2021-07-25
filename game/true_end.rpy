label true_end:
label end_4:
label end_14: # lazy and don't want to fix tl tags
    $ persistent.ed_unlocked_4 = True

    scene bg shop with dissolve

    "While heading to the park…"

    play audio phonecall loop
    pause 3.0

    "…my phone started to ring."

    stop audio

    sn "Kohi~"

    p "Ah senpai, I’m on my way there now!"

    sn "Hmmm? I’m in front of your place though…"

    sn "I kept waiting but you didn’t come, so I decided to go to you instead."

    p "Eh? But it hasn’t even been 5 minutes…"

    p "Did we pass by each other somehow???"

    sn "Well, I’ll wait here then. You wanted to ask about the safe as well, right?"

    p "I…okay, I’ll head back now then."

    p "{i}I just left though…weird. How did I not see her??{/i}"

    scene bg intersection day with dissolve

    "When I returned, I found senpai standing outside my door waiting for me."

    sn "Hi Kohiii! It’s been a while, hasn’t it!"

    p "Ah senpaaai!"

    p "You should’ve told me you were coming!"

    sn "It’s because Kohi took so long!"

    p "But…I headed straight for the park right after you called!"

    sn "Eh…but I waited so long though…"

    p "{i}Weird…{/i}"

    "I opened the door, and the two of us went inside."

    scene bg room with dissolve

    sn "About the safe though, here is the last key. You left it in your room."

    p "Huh? What are you talking…about…?"

    p" {i}Come to think of it, I do remember having 3 pieces of paper and 3 keys…{/i}"

    "I took three keys and slips of paper out from my drawer."

    "4 keys, and three sheets of papers with 1, 0, and 7 written on them."

    sn "Try opening the safe!"

label true_end_combination:
    show screen lock_buttons

    "It’s a combination lock with 4 digits."

    $ lock_active = True
    while True:
        $ renpy.pause(hard=True)

    label combination_lock_wrong:
        $ lock_active = False
        p "{i}It’s not opening…probably the wrong code. Let’s try again.{/i}"
        $ lock_active = True
        while True:
            $ renpy.pause(hard=True)

    label combination_lock_correct:
        $ lock_active = False
        p "Oh it opened!"
        hide screen lock_buttons


label true_end_combination_unlocked:
    "There’s a letter inside and…another safe with a keyhole."

    nvl clear
    nvl_narrator "“Hitona!"
    nvl_narrator "This is our gift to you."
    nvl_narrator "Open each safe with each key!”"

    "insert key"

    call show_cg("BirthdayKohi")

    nvl clear
    nvl_narrator "“First of all!"
    nvl_narrator "We want to tell you that your fans are always there behind you!"
    nvl_narrator "No matter when or where, across time and space, we will always be there for you!”"

    "There’s another locked safe inside, and there are three keys left."

    "insert key"

    # call show_cg("")

    nvl_narrator "“Second!"
    nvl_narrator "Keep being yourself!"
    nvl_narrator "That is Hitona’s unique charm!"
    nvl_narrator "Let loose!”"

    "There’s another locked safe inside, and there are two keys left."

    "insert key"

    # call show_cg("")

    nvl_narrator "“Third!"
    nvl_narrator "The memories that you have made all this time are irreplaceable!"
    nvl_narrator "We want Hitona to keep on making wonderful memories!”"

    "There’s another locked safe inside, and there is one key left."

    "insert key"

    # call show_cg("")

    # credits, etc.
    call credits()

    return
