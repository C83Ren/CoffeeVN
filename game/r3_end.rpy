label r3_end:
    scene bg sing with fade

    play music r3end_bgm fadein 2.0

    show lios front at lios_right with dissolve
    show hitona3 smile hat at hitona_left with dissolve

    pi "Aaaaaaaaaaaaaaaaaaah finally…"

    l "How many tries has this been Pierrot?"

    show hitona3 idle hat

    pi "I have no idea…to many to count that for sure"

    pi "I leave the rest to you Lios"

    scene bg hub with Fade(1.0, 1.0, 1.0)

    p "What’s happening?? I did finish the challenge right?"

    show lios front with dissolve

    l "Yeah don’t worry, congrats on finishing every challenge there is"

    pi "Yaaay~"

    l "You don’t know how long it took you to finish all these"

    p "Did it really take that long?"

    l "Well one try doesn’t take long"

    p "One try?"

    l "You’ve been doing this more than one time"

    p "huh?"

    p "What?"

    hide lios
    show hitona3 idle hat at hitona_left

    pi "I did say his domain makes you forget very obvious things"

    p "No way…How many times?"

    show lios front at lios_right behind hitona3

    l "That’s what I asked Pierrot just now right?"

    pi "I lost count~ Probably 15,532 times? I’m not sure"

    p "…I can’t believe it…"

    l "Well all of this is Pierrot’s idea anyway"

    p "huh?"

    show hitona3 angry hat

    pi "You ratted me out now???"

    l "She told me to stole the thing and I did"

    p "What? Pierrot did????"

    show hitona3 smug hat

    pi "Hmph fine, it was all part of the plan though"

    p "Why you look so smug!?"

    l "And look where it brought us Pierrot…"

    show hitona3 idle hat

    pi "…yeah let’s not do that again"

    p "Why did you do that?!"

    l "Well do you know what I stole from you?"

    p "Uuuh no…I don’t think I figured it out"

    hide lios
    hide hitona3
    show hitona3 idle hat

    pi "A lasting impression"

    p "Eh?"

    pi "You will remember something more powerfully when it gives you a lasting impression"

    pi "Such as these challenges"

    hide hitona3
    show lios front

    l "And that is why we stole it from you"

    show hitona3 idle hat
    hide lios

    pi "So it will have a lasting impression"

    hide hitona3
    show lios front

    l "So you will remember it more strongly when we give it back to you"

    p "Remember what?"

    l "Your memories~"

    # Pierrot says this also ^

    scene cg 4 unscaled with Fade(1.0, 1.0, 1.0)

    #"Thanks for playing"
    pause 15.0

    if r3_secret:
        "The hidden message"

    scene bg room with fade

    p "What’s this?"

    "A paper and a key was on the floor"

    "\"Hey hope you enjoyed that\""

    "\"By the way to open the safe you need to input some passcode right?\""

    "\"Well the passcode is just how many cards there are in one suit of trump cards and the number from your own name\""

    "\"Here you get the number 0~\""

    "\"Good luck~\""

label end_8:
    $ persistent.ed_unlocked_8 = True
    "route 3 end"
    return
