label r3_quiz:
    play sound lightswitch

    scene bg quiz with fade

    $ renpy.pause(1.0)
    window hide

    "A moment later, the lights returned, and the room had become like a quiz corner."

    l "First up is the quiz challenge! Get 3 out of 3 correct to continue!"

    l "If you miss even one...well, you don’t want to know what will happen."

    show hitona3 smile hat

    pi "Don’t worry, Kohigashi! This first part is usually really easy!"

    p "Huh? You’ve done this before?"

    show hitona3 smug hat

    "Pierrot answered with a smile."

    l "Go on, to the podium"

    "Not understanding what was going on, I decided to just head over to the podium anyways."

    l "Let’s start!"

    play sound quizstart

    "QUIZ START"

    hide hitona3 with dissolve

    jump quiz_default

label quiz_fail:
    scene bg quiz

    show lios front at lios_right with dissolve

    "Someone with a black cape suddenly appeared in front of us."

    "It was Lios."

    "{color=[l.who_args[color]]}[l]{/color} & {color=[p.who_args[color]]}[p]{/color}" "So much for being a great detective..."

    show hitona3 pout hat at hitona_left with dissolve
    #show lios front at lios_right behind hitona3

    pi "Hey don’t blame me! Kohigashi was the only one answering!"

    l "You kept quiet because you didn’t know the answer either though."

    show hitona3 surprised2 hat

    "Pierrot looked away and whistled without saying another word."

    l "Goodbye, little girls~"

    stop music fadeout 1.0

    scene bg room with Fade(1.0, 1.0, 1.0)

    play music room_bgm fadein 3.0 volume 0.2

    p "{i}Eh? I’m in...my room? On my bed...{/i}"

    p "{i}Even if that was a dream, I wonder what was stolen...{/i}"

    "I looked up at my phone screen."

    p "..."

    p "AAAAAAA I’M SO SORRY SENPAI!"

    "I rushed out of my room in a hurry to meet senpai."

    scene black with dissolve

    "While running towards the park, that dream? kept spinning in my mind."

    "It seems like the meaning of that dream? will stay unknown forever."

    "I guess dreams will just be dreams."

    jump bad_end
