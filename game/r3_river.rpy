label r3_river_init():
    $ affection = 0
    return

label r3_river:
    $ save_enabled = True

    scene bg hub with fade

    stop music fadeout 1.0
    play music lios_bgm fadein 2.0 volume 0.1

    show hitona3 laugh hat at hitona_left with dissolve

    pi "I powered up since last time Lios!"

    hide hitona3
    show lios front at lios_right with dissolve

    l "Well you might have powered up, but it doesn’t seem like the girl over there understands anything."

    p "Eh? Me?"

    l "See?"

    show hitona3 idle hat at hitona_left

    pi "She’ll get it eventually, especially when you give it back to her."

    p  "Let’s just move on to the next challenge, Kohigashi."

    l "You won’t be that optimistic when you see the next one."

    hide hitona3 with dissolve
    hide lios with dissolve

    "We walked for a bit again and..."

    scene bg river with Fade(1.0, 0.0, 1.0)
    play sound riverbank loop

    p "How does he change the setting so easily..."

    pi "Trust me, he can do much stranger things if he wants to."

    $ save_enabled = False

    $ animal_route = renpy.random.randint(1,3)

    if animal_route == 1:
        jump river_cat
    elif animal_route == 2:
        jump river_dog
    else:
        jump river_deer

label river_cat:

    show cat smile with dissolve

    "There is a cat standing in front of us."

    "Though it’s a cat, it’s about the same height as me."

    p "Something...feels weird..."

    pi "So? What is it this time? I’ll show you what a great detective is capable of!"

    l "Make it fall in love with you."

    p "..."

    pi "..."

    "{color=[p.who_args[color]]}[p]{/color} & {color=[pi.who_args[color]]}[pi]{/color}" "Come again...?"

    c "Meow meow meow meow meow"

    l "I said, make it fall in love with you."

    p "So uhh, Pierrot...uhh..."

    pi "Don’t look at me like that..."

    "What should I do?"

    jump river_menu1

label river_dog:

    show dog smile with dissolve

    "There is a dog standing in front of us."

    "Though it’s a dog, it’s about the same height as me."

    p "Something...feels weird..."

    pi "So? What is it this time? I’ll show you what a great detective is capable of!"

    l "Make it fall in love with you."

    p "..."

    pi "..."

    "{color=[p.who_args[color]]}[p]{/color} & {color=[pi.who_args[color]]}[pi]{/color}" "Come again...?"

    do "Woof Woof woof woof"

    l "I said, make it fall in love with you."

    p "So uhh, Pierrot...uhh..."

    pi "Don’t look at me like that..."

    "What should I do?"

    jump river_menu1

label river_deer:

    show deer smile with dissolve

    "There is a deer standing in front of us."

    "Though it’s a deer, it’s about the same height as me."

    p "Something...feels weird..."

    pi "So? What is it this time? I’ll show you what a great detective is capable of!"

    l "Make it fall in love with you."

    p "..."

    pi "..."

    "{color=[p.who_args[color]]}[p]{/color} & {color=[pi.who_args[color]]}[pi]{/color}" "Come again...?"

    de "..."

    l "I said, make it fall in love with you."

    p "So uhh, Pierrot...uhh..."

    pi "Don’t look at me like that..."

    "What should I do?"

    jump river_menu1

label river_menu1:

    menu:
        extend ""
        "Pat its head":
            jump river_pat
        "“What’s your name?”":
            jump river_name
        "“I love you.”":
            jump river_love

label river_pat:
    if animal_route == 1:
        $ affection = affection - 10

        show cat happy

        p "Oh, she looks happy."

        c "Meow meow."

        pi "She’s not happy at all."

        l "Yeah that cat is not happy at all."

        p "But she looks so happy!"

        pi "...you’ve still got much to learn."

    elif animal_route == 2:
        $ affection = affection + 20

        show dog happy

        do "Woof woof woof!"

        p "It looks so excited"

        pi "I don’t think I could’ve patted a dog like that"

        l "That’s the reson you’d fail here, Pierrot."

        p "The dog is so cute!"

    else:
        $ affection = affection - 10

        show deer sad

        de "..."

        p "This deer is... kinda scary"

        pi "I can at least tell you, patting her was probably a bad idea."

        "Lios just nodded in agreement."

        p "Uhh, okay?"

    jump river_menu2

label river_name:
    if animal_route == 1:
        $ affection = affection + 20

        show cat sad

        c "Nyaaaaa"

        p "Uhhh...I only asked for her name though...why is she making such a sad face...?"

        pi "She said her name is Hakuto."

        l "She’s quite happy though that you want to talk to her."

        p "You’re making this up, right?!"

    elif animal_route == 2:
        $ affection = affection - 10

        show dog smile

        do "Woof"

        p "That reaction seems kind of weak."

        pi "Looking at this dog, it should be obvious that she wants affection."

        l "Either way, the dog doesn’t seem very happy."

        p "Aren’t you two way too in sync with each other?"

    else:
        show deer smile

        de "..."

        p "..."

        pi "She says her name is Kaba."

        l "Let me correct you, it’s Kava."

        p "...How do you know?"

    jump river_menu2

label river_love:
    if animal_route == 1:
        $ affection = affection + 10

        show cat smile

        c "Meow"

        p "What kind of reaction I was expecting..."

        pi "You got her good!"

        l "You’re a cat killer, huh."

        p "What are you saying..."

    elif animal_route == 2:
        $ affection = affection + 10

        show dog blush

        do "Woooooof!"

        p "This might be the first time I’ve ever seen a dog blush..."

        pi "Wow. she looks elated."

        l "Do you feel like patting her now?"

        p "A bit, yeah."

    else:
        show deer smile

        de "..."

        p "...I’m begging you react to that..."

        pi "Never thought I see the day where someone would just say that to an animal she just met."

        l "Should’ve recorded that..."

        p "Don’t you dare!"

    jump river_menu2

label river_menu2:
    menu:
        "What should I do next?"
        "Rub its chin":
            jump river_rub
        "“What do you do on your days off?”":
            jump river_daysoff
        "“Let’s go on a date!”":
            jump river_date

label river_rub:
    if animal_route == 1:
        $ affection = affection - 30

        show cat blush

        c "Meeeoow~"

        p "This cat must be so happy that she’s blushing, huh."

        pi "You think so?"

        l "Think again."

        p "Eh?"

    elif animal_route == 2:
        $ affection = affection + 20

        show dog smile

        do "Wooooof!"

        p "I guess any dog would enjoy a good rub."

        pi "Seems like it."

        l "Yeah, seems like it."

        p "You two seemed so indifferent..."

    else:
        $ affection = affection - 20

        show deer blush

        de "..."

        p "..."

        pi "Be careful not to get kicked."

        l "That deer is quite pissed."

        p "No!"

    jump river_menu3

label river_daysoff:
    if animal_route == 1:
        $ affection = affection + 20

        show cat sad

        c "Meow meow meow meow"

        p "I swear I have no intention of making her cry!!"

        l "She’s rather pleased though."

        pi "She says she play games on her days off."

        p "She was so happy she cried???"

    elif animal_route == 2:
        $ affection = affection - 20

        show dog sad

        do "Woof..."

        p "Why are you crying?!"

        pi "She thinks you are being too distant with her"

        l "Poor Charu..."

        p "That’s this dog’s name??"

    else:
        $ affection = affection + 10

        show deer smile

        de "..."

        p "..."

        pi "She said she likes reading books."

        l "Also singing."

        p "She didn’t say anything though???"

    jump river_menu3

label river_date:
    if animal_route == 1:
        show cat happy

        c "Meow meow"

        p "I can’t believe I said that...but at least she looks happy"

        pi "Nah, she’s quite indifferent."

        l "I recorded that, don’t worry."

        p "Hurry up and delete that recording!"

    elif animal_route == 2:
        $ affection = affection + 30

        show dog happy

        do "Woof Woof Woof Woof!"

        p "Woah there, calm down, we going to all sorts of places, don’t worry."

        pi "A dog sure loves a good walk."

        l "She does need her exercise, yeah, but not now, do it later."

        p "Okay..."
    else:
        show deer smile

        de "..."

        p "..."

        pi "You just asked a deer out on a date~"

        l "You just asked a deer out on a date~"

        p "I know, geez!"

    jump river_menu3

label river_menu3:
    menu:
        "For the final blow, what should I say?"
        "“Let’s be friends~”":
            jump river_friend
        "“Go out with me!”":
            $ add_choice_to_history("Be my girlfriend!")
            jump river_girlfriend

label river_friend:
    if animal_route == 1:
        $ affection = affection + 30

        show cat sad

        c "Meoow~"

        p "So what is it now?"

        pi "I think you’re good."

        l "Yeah she’s sad but I think you’re good, let’s see."

        p "See what?"

    elif animal_route == 2:
        $ affection = affection - 30

        show dog sad

        do "..."

        p "Woah, I’m sorry!"

        pi "Can’t believe you just said that to a poor dog."

        l "Such cruel world you’re living in, Charu."

        p "I mean...I mean...I have no excuse..."

    else:
        $ affection = affection + 20

        show deer happy

        de "..."

        p "I hope her expression shows what she’s feeling now..."

        pi "Don’t worry, she’s happy."

        l "Yeah don’t worry."

        p "That’s good to hear."

    jump river_final

label river_girlfriend:
    if animal_route == 1:
        show cat smile

        c "Meow meow~"

        p "I have no idea what that means..."

        pi "I think you messed up."

        l "Yeah she’s sad but I think you’re good, let’s see."

        p "See what?"

    elif animal_route == 2:
        $ affection = affection + 30

        show dog happy

        do "Wooooof!"

        p "Woah yeah, we’ll be together for life!"

        pi "You got that, Lios?"

        l "Yeah, all recorded~"

        p "NOOOOO!! DELETE IT!"

    else:
        $ affection = affection - 20

        show deer blush

        de "..."

        p "I put my everything on that confession!"

        pi "I guess your everything wasn’t enough."

        l "Her blushing doesn’t mean anything good, let me tell you that."

        p "WHYYYY!!"

    jump river_final

label river_final:
    scene bg river with fade

    p "I did what I could, what now?"

    show lios front at lios_right with dissolve
    show hitona3 worried hat at hitona_left with dissolve

    l "What do you think, Pierrot? Did she pass?"

    pi "Hmmmm..."

    p "Why are you two judging together?!"

    l "Well let’s just ask the one in question."

    hide hitona3
    hide lios

    if animal_route == 1:
        show cat smile
        if affection > 0:
            play audio challengecomplete
            c "She passed~"
        else:
            play audio falsechoice_long
            c "She failed~"
        hide cat
    elif animal_route == 2:
        show dog smile
        if affection > 0:
            play audio challengecomplete
            do "She passed~"
        else:
            play audio falsechoice_long
            do "She failed~"
        hide dog
    else:
        show deer smile
        if affection > 0:
            play audio challengecomplete
            de "She passed~"
        else:
            play audio falsechoice_long
            de "She failed~"
        hide deer

    show lios front at lios_right
    show hitona3 worried hat at hitona_left

    p "She can talk?????!!!!!"

    "{color=[l.who_args[color]]}[l]{/color} & {color=[pi.who_args[color]]}[pi]{/color}" "Yeah."

    p "YOU SHOULD’VE SAID SO!"

    if affection > 0:
        jump r3_drawing
    else:
        jump river_fail

label river_fail:
    $ save_enabled = True
    scene bg river

    p "Well that was heartbreaking..."

    p "I mean...trying to make an animal to fall in love with you is a bit..."

    p "How is this fair!!!!!"

    show lios front

    l "Well, a fail is a fail, so off you go."

    stop music fadeout 1.0

    scene bg room with Fade(1.0, 1.0, 1.0)

    play music room_bgm fadein 3.0 volume 0.2

    "When I opened my eyes, I was holding the doorknob of my own room."

    p "{i}Where was I going to go again...?{/i}"

    "When I looked at my phone, there was a single message."

    "“Kohi……hurry up already!”"

    p "{i}This isn’t good; if I don’t hurry up...{/i}"

    scene black with dissolve

    "While running towards the park, that dream? kept spinning in my mind."

    "It seems like the meaning of that dream? will stay unknown forever."

    "I guess dreams will just be dreams."

    jump bad_end
