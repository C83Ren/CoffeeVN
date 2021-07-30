label r3_river:

    init python:
        affection = 0

    scene bg hub with fade

    stop music fadeout 1.0
    play music lios_bgm fadein 2.0 volume 0.1

    p "We somehow managed to finished that… pant pant pant"

    show hitona3 laugh hat at hitona_left with dissolve

    pi "Worst enemy? Yeah cause it was too easy Lios!"

    pi "Don’t you think so too Hitona?"

    p "Didn’t you hear what I was saying… pant pant pant"

    pi "I powered up since last time Lios!"

    hide hitona3
    show lios front at lios_right with dissolve

    l "Well you might powered up, but doesn’t seem the little girl right there understand anything"

    p "Eh? Me?"

    l "See?"

    show hitona3 idle hat at hitona_left

    pi "She’ll get it eventually, especially when you give it back to her"

    p  "Let’s just move on Hitona~"

    l "You won’t be that optimistic when you see the next one"

    hide hitona3 with dissolve
    hide lios with dissolve

    "We walked for a bit and again"

    scene bg river with Fade(1.0, 0.0, 1.0)
    play sound riverbank loop

    p "How does he change these places so easily"

    pi "Trust me, he can do weirder stuff if he wants to"

    $ animal_route = renpy.random.randint(1,3)

    if animal_route == 1:
        jump river_cat
    elif animal_route == 2:
        jump river_dog
    else:
        jump river_deer

label river_cat:

    show cat smile with dissolve

    "Now a cat is in front of us…"

    "A huge cat, it has the same height as me…"

    p "Okay…this is weird…"

    pi "So what is it this time? I’ll show you what a great detective is capable of!"

    l "Make it fall in love with Hitona"

    p "…"

    pi "…"

    p "what…?"

    # Pierrot says this as well ^

    c "Meow meow meow meow meow"

    p "So uuh Pierrot…uuh…"

    pi "Don’t look at me like that…"

    "What should I do now…"

    jump river_menu1

label river_dog:

    show dog smile with dissolve

    "Now a dog is in front of us…"

    "A huge dog, it has the same height as me…"

    p "Okay…this is weird…"

    pi "So what is it this time? I’ll show you what a great detective is capable of!"

    l "Make it fall in love with Hitona"

    p "…"

    pi "…"

    p "what…?"

    # Pierrot says this as well ^

    do "Woof Woof woof woof"

    p "So uuh Pierrot…uuh…"

    pi "Don’t look at me like that…"

    "What should I do now…"

    jump river_menu1

label river_deer:

    show deer smile with dissolve

    "Now a deer is in front of us…"

    pi "So what is it this time? I’ll show you what a great detective is capable of!"

    l "Make it fall in love with Hitona"

    p "…"

    pi "…"

    p "what…?"

    # Pierrot says this as well ^

    de "..."

    p "So uuh Pierrot…uuh…"

    pi "Don’t look at me like that…"

    "What should I do now…"

    jump river_menu1

label river_menu1:

    menu:
        extend ""
        "Pat its head":
            jump river_pat
        "\"What's your name?\"":
            jump river_name
        "\"I love you\"":
            jump river_love

label river_pat:
    if animal_route == 1:
        $ affection = affection - 10

        show cat happy

        p "Oh she looks happy"

        c "Meow meow"

        pi "She's not happy at all"

        l "Yeah that cat is not happy at all"

        p "But it looks so happy!"

    elif animal_route == 2:
        $ affection = affection + 20

        show dog happy

        do "Woof woof woof!"

        p "It looks so excited"

        pi "I don't think I could've patted a dog just like that"

        l "The reason you would fail this one Pierrot"

        p "The dog is cute though"

    else:
        $ affection = affection - 10

        show deer sad

        de "..."

        p "This deer is uuh...kinda scary"

        pi "I at least can tell you probably patting was a bad idea"

        "Lios nodded in aggreement"

        p "Uuh okay?"

    jump river_menu2

label river_name:
    if animal_route == 1:
        $ affection = affection + 20

        show cat sad

        c "Nyaaaa"

        p "Uuuh...I just asked her name why the sad face..."

        pi " She said her name is Hakuto"

        l "She's quite happy though you want to talk to her"

        p "You're making stuff up right?!"

    elif animal_route == 2:
        $ affection = affection - 10

        show dog smile

        do "Woof"

        p "That reaction is kinda weak"

        pi "Looking at the dog you should know this dog loves affection"

        l "Either way the dog doesn't seem happy"

        p "Makes me wonder how you two are so in sync now..."

    else:
        show deer smile

        de "..."

        p "..."

        pi "She said her name is Kaba"

        l "Let me correct that, it's Kava"

        p "...How?"

    jump river_menu2

label river_love:
    if animal_route == 1:
        $ affection = affection + 10

        show cat smile

        p "What kind of reaction I was expecting..."

        pi "You got her good, she didn't expect that"

        l "You're a cat killer huh"

        p "What are you two talking about..."

    elif animal_route == 2:
        $ affection = affection + 10

        show dog blush

        do "Woooooof!"

        p "This is the first time I've ever seen a dog blush..."

        pi "Wow she looks elated"

        l "Do you feel like patting it now?"

        p "Kinda do yeah"

    else:
        show deer smile

        de "..."

        p "...I'm begging you react to that..."

        pi "Never thoght I see the day where someone would just say that to an animal she just met"

        l "Should've recorded that"

        p "Don't you dare..."

    jump river_menu2

label river_menu2:
    menu:
        "Now what should I do next?"
        "Rub its chin":
            jump river_rub
        "\"What do you do on your days off?\"":
            jump river_daysoff
        "\"Let's go on a date!\"":
            jump river_date

label river_rub:
    if animal_route == 1:
        $ affection = affection - 30

        show cat blush

        c "Meeeoow~"

        p "This cat must be so happy that it's blushing"

        pi "You think so?"

        l "Think again~"

        p "Eh?"

    elif animal_route == 2:
        $ affection = affection + 20

        show dog smile

        do "Wooooof!"

        p "I guess any dog would love a good rub"

        pi "Seems like it"

        l "Yeah seems like it"

        p "You two seem so indifferent..."

    else:
        $ affection = affection - 20

        show deer blush

        de "..."

        p "..."

        pi "Be careful not to get kicked"

        l "That deer is pissed I can tell yo that much"

        p "NO!"

    jump river_menu3

label river_daysoff:
    if animal_route == 1:
        $ affection = affection + 20

        show cat sad

        c "Meow meow meow meow"

        p "I swear I have no intention of making her cry"

        pi "She said she play games during her days off"

        l "She's ather pleased though"

        p "She was so happy she cried???"

    elif animal_route == 2:
        $ affection = affection - 20

        show dog sad

        do "Woof..."

        p "Why are you crying?!"

        pi "She thinks you are being too distant with her"

        l "Poor Charu"

        p "It's this guy name??"

    else:
        $ affection = affection + 10

        show deer smile

        de "..."

        p "..."

        pi "She said she likes reading book"

        l "And don't forget singing"

        p "When she is so silent????"

    jump river_menu3

label river_date:
    if animal_route == 1:
        show cat happy

        c "Meow meow"

        p "I can't believe I said that...but at least she looks happy"

        pi "She's quite indifferent to it though"

        l "I recorded it don't worry"

        p "Delet that!"

    elif animal_route == 2:
        $ affection = affection + 30

        show dog happy

        do "Woof Woof Woof Woof!"

        p "Woah yeah calm down, we gonna go to places don't worry"

        pi "A dog sure love a walk"

        l "She needs her exercise yeah, but not now do it later"

        p "Okay..."
    else:
        show deer smile

        de "..."

        p "..."

        pi "You just asked a deer out on a date~"

        l "You just asked a deer out on a date~"

        p "I know okay!"

    jump river_menu3

label river_menu3:
    menu:
        "For the final blow, what should I say?"
        "Let's be friends~":
            jump river_friend
        "Be my girlfriend!":
            jump river_girlfriend

label river_friend:
    if animal_route == 1:
        $ affection = affection + 30

        show cat sad

        c "Meoow~"

        p "So what is it now?"

        pi "I think you're good"

        l "Yeah she's sad but I think you're good"

    elif animal_route == 2:
        $ affection = affection - 30

        show dog sad

        do "..."

        p "Woah I'm sorry okay!"

        pi "Can't believe you just said that to a poor dog"

        l "Such cruel world you're living in Charu"

        p "I mean...I mean...I have no excuse..."

    else:
        $ affection = affection + 20

        show deer happy

        de "..."

        p "I hope her expression shows what she's feeling now..."

        pi "Don't worry, she's happy"

        l "Yeah don't worry"

        p "Well that was something"

    jump river_final

label river_girlfriend:
    if animal_route == 1:
        show cat smile

        c "Meow meow~"

        p "I have no idea what that means"

        pi "I think you messed up"

        l "Yeah"

    elif animal_route == 2:
        $ affection = affection + 30

        show dog happy

        do "Wooooof!"

        p "Woah yeah, we're gonna be together!"

        pi "You got that Lios?"

        l "Yeah all recorded~"

        p "NOOOOO"

    else:
        $ affection = affection - 20

        show deer blush

        de "..."

        p "I put my everything on that confession!"

        pi "I guess your everything wasn't enough"

        l "Her blushing doesn't mean anything good I can tell you that"

        p "WHYYYY"

    jump river_final

label river_final:
    scene bg river with fade

    p "I did what I could, what now?"

    show lios front at lios_right with dissolve
    show hitona3 worried hat at hitona_left with dissolve

    l "What do you think Pierrot? Did she pass?"

    pi "Hmmmm"

    p "Why are you two judging together?!"

    l "Well let's just ask the one who was involved"

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

    l "Yeah"

    #Lios says this as well ^

    p "YOU SHOULD'VE SAID SO!"

    if affection > 0:
        jump r3_drawing
    else:
        jump river_fail

label river_fail:
    scene bg river

    p "Well that was heartbreaking…"

    p "I mean…trying to make an animal to fall in love with you…"

    p "How is this faiiir!"

    show lios front

    l "Well a fail is a fail so off you go~"

    stop sound fadeout 1.0
    play music room_bgm fadein 1.0 volume 0.2

    scene bg room with Fade(1.0, 1.0, 1.0)

    "I opened my eyes and I was holding my room door knob"

    "Where was I going to go again…?"

    play sound messagetone

    "Oh there’s a message on my phone"

    "\"Kohi…come here quickly…or else…\""

    "I guess I gotta go…"

    scene black with fade

    "While going to the park that dream kept spinning in my head"

    "I wonder what was that all about"

    "I guess I will never figure out what that dream was all about"

    "Dream stay as dream huh"

    "Bad End"

    return
