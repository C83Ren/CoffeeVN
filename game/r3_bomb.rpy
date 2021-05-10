label r3_bomb:
    scene bg quiz

    show lios front

    "Someone with a black cape suddenly appeared in front of us"

    l "You got all right huh, unexpected"

    show hitona3 laugh hat at hitona_left
    show lios front at lios_right behind hitona3

    pi "Like I said, don’t underestimate the Great Detective Pierrot"

    show hitona3 smug hat

    pi "Such petty quiz you’re giving us"

    p "But I was the one answering…"

    l "Pierrot don’t get too cocky, you’ve been doing this for a while now it is no surprise that you would memorize it by now"

    show hitona3 angry hat

    pi "How dare you say that! You always change the question!"

    "Even though they’re arguing seems like they are quite close somehow"

    l "Well no matter, it’s not like you will manage to clear the next one"

    l "Go on, see your worst enemy"

    p "Eh? Worst enemy?"

    show hitona3 idle hat

    pi "Don’t falter Hitona! Let’s goo"

    scene bg hub

    "We walked for a bit, then somehow we were back in the previous room"

    show lios front

    l "You have to escape the maze within the time limit. If not the bomb would explode~"

    p "What?"

    l "Here a map, you can see it for a bit"

    l "By the way the time limit is 2 minutes, like actually 2 minutes yes I’m looking at you player"

    l "Right after the map is gone, 2 minutes, good luck~"

    hide lios
    show hitona3 angry hat

    pi "WHAT? This is not part of the plan LIOOOS!"

    play music bomb_bgm
    show bomb map at center

    "Remember this map~"

    hide bomb map
    jump bomb_mechanic

    init python:
        r3_secret = False

    menu:
        "Did you succeed escaping?"
        "Yes!":
            jump r3_river
        "No...":
            jump bomb_fail
        "Through the secret exit~":
            $ r3_secret = True
            jump r3_river

label bomb_fail:
    hide countdown
    scene black

    "BOOOM"

    scene bg hub

    "We got sent back to the first room…"

    show lios front at lios_right

    l "Told you it’s your worst enemy~"

    show hitona3 angry hat at hitona_left

    pi "By worst you mean actually running?!"

    p "Huuf…nothing…huuf…we could…huuuf about that…"

    show hitona3 pout hat

    pi "Aren’t you annoyed?! It was just the second challenge!"

    pi "Lios you must have cheated somehow!"

    l "Doesn’t really matter now does it"

    l "I make the rule here and you’re here to solve it…somehow…"

    pi "Cheater, cheater, cheater, cheater Lios~"

    p "After all that you still have the energy to get angry huh Pierrot"

    show hitona3 worried hat

    pi "Well I guess we can try it again at another time"

    l "Yes off you go little girls"

    l "Til Next time~"

    scene bg room

    play music room_bgm

    p "Eh?"

    "I opened my eyes and I was in my room lying on my bed…"

    "My phone was ringing…I just looked at it…then the caller hung up"

    p "…"

    p "…eh? NOO SENPAI SORRY!"

    "I rushed out of the room"

    scene black

    "While going to the park that dream kept spinning in my head"

    "I wonder what was that all about"

    "I guess I will never figure out what that dream was all about"

    "Dream stay as dream huh"

    return
