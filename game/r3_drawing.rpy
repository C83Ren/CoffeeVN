label r3_drawing:
    scene bg river

    p "Well the result was as I was expecting~"

    p "Don’t underestimate Hitona the romance master~"

    show hitona3 laugh hat at hitona_left

    pi "Yeah such challenge can’t defeat the great detective Pierrot!"

    p "You didn’t help!"

    show lios front at lios_right behind hitona3

    l "Well at least finally you got here…"

    show hitona3 smile hat

    "Pierrot looked somewhat relief"

    p "Huh?"

    hide hitona3
    hide lios

    play audio messagetone

    "Oh there’s a message from my phone"

    "100+ unread messages…"

    "“Kohiii, where are you?”"

    "This is kinda scary…Who’s sending these anyway? I can’t read its name"

    "Oh well~"

    show lios front at lios_right
    show hitona3 smile hat at hitona_left

    l "Go on to the next one"

    pi "Let’s go Hitona, to the next challenge!"

    stop sound

    "We walked a bit again and the room suddenly changed"

    scene bg computer with Fade(1.0, 1.0, 1.0)

    p "It still weirds me out that these rooms can change just like that"

    show lios front at lios_right with dissolve
    show hitona3 worried hat at hitona_left with dissolve

    pi "I really think the animal from before was weirder…"

    l "The animal has heart too you know, such cruelty"

    p "You popping up whenever and wherever is probably weirder yeah…"

    l "Well just sit in front of that computer"

    show hitona3 idle hat

    pi "Then what?"

    l "You’ll see"

    hide hitona3
    hide lios

    "I sat on the chair and the computer screen showed “Just a little bit more!”"

    p "Okay…?"

    show lios front at lios_right
    show hitona3 idle hat at hitona_left

    l "Time to do more quizzes~ Guess the drawings!"

    pi "Seem quite tame for your standards"

    l "Shut it will you…"

    l "Guess 3 out of 3 okay. Like Pierrot said should be easy~"

    show hitona3 worried hat

    pi "Now I’m not so sure when you put it that way…"

    p "Just got to try then"

    hide hitona3 with dissolve

    play sound quizstart

    "START"

    jump quiz_pic_default

    menu:
        "Did you succeed?"
        "Yeah":
            jump r3_sing
        "Nope":
            jump drawing_fail

label drawing_fail:
    scene bg computer with Fade(1.0, 1.0, 1.0)

    show lios front at lios_right with dissolve
    show hitona3 angry hat at hitona_left with dissolve

    pi "Lios…YOUR DOODLE IS HORRIBLE!"

    l "You just don’t understand my artistic sense Pierrot"

    p "It was…yeah kinda horrible Lios"

    l "Uuugh, if you knew who drew these you would singing praises"

    l "But no matter, such trifle thing should not be brought up any further"

    l "Cause you failed it means you getting out of here. Go on, shoo shoo~"

    show hitona3 surprised2 hat

    pi "Come ooooon we were so close. Lios pleeeeeaaase"

    l "Nope, nothing like that, go on. I’ll kick you out myself then. Ciao~"

    stop music fadeout 1.0

    scene bg room with Fade(1.0, 1.0, 1.0)
    play music room_bgm fadein 1.0 volume 0.2
    play sound phonecall

    p "Huh?!"

    "I suddenly woke up on my bed…"

    "Cause of the phone was ringing"

    "A call?"

    stop sound

    "“KOHIIIII! I’ve been waiting for xx minutes now! Where are you?!”"

    "…"

    "I hung up and dash outside"

    scene black with fade

    "While going to the park that dream kept spinning in my head"

    "I wonder what was that all about"

    "I guess I will never figure out what that dream was all about"

    "Dream stay as dream huh"

    "Bad End"


    return
