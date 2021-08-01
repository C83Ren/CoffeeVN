label r3_drawing:
    $ save_enabled = True
    scene bg river

    p "Just as expected~"

    p "Don’t underestimate me, the romance master!"

    show hitona3 laugh hat at hitona_left

    pi "Yeah, such a simple challenge couldn’t possibly defeat the great detective Pierrot!"

    p "You didn’t help at all!"

    show lios front at lios_right behind hitona3

    l "Well, at least finally you made it here..."

    show hitona3 smile hat

    "Pierrot looked somewhat relieved"

    "Without really thinking about it, I checked my phone."

    p "Huh?"

    hide hitona3
    hide lios

    play audio messagetone

    window hide
    $ renpy.pause(1.0)

    "It seems like I received some texts."

    "“Unread Messages: 100+”"

    "“Kohi! Where are you?”"

    "“Kohi?”"

    "“Hello?!?!!”"

    p "{i}This is kind of scary...{/i}"

    p "{i}To begin with, who’s even sending these...? The name...for some reason I can’t read it...{/i}"

    p "{i}Oh well...{/i}"


    show lios front at lios_right
    show hitona3 smile hat at hitona_left

    l "Anyways, keep moving."

    pi "Let’s go, Kohigashi!"

    pi "To the next challenge!"

    stop sound

    "We walked a bit again and the room suddenly changed"

    scene bg quiz with Fade(1.0, 1.0, 1.0)

    p "It still weirds me out that these rooms can change just like that..."

    show lios front at lios_right with dissolve
    show hitona3 worried hat at hitona_left with dissolve

    pi "I really think the animal flirting from before was weirder though..."

    l "How cruel. Animals have hearts too, you know."

    p "You popping up out of nowhere is even weirder though."

    l "Well anyways, just look at the monitor."

    show hitona3 idle hat

    pi "Then what?"

    l "You’ll see."

    hide hitona3
    hide lios

    "I looked at the monitor. On the screen, “Just a little bit more!” was displayed in large font."

    p "..."

    p "Huh?"

    show lios front at lios_right
    show hitona3 idle hat at hitona_left

    l "Time to do more quizzes!"

    l "Guess the situation in the drawings!"

    pi "Seems quite tame for your standards."

    l "Shut it."

    l "Just like last time, 6 out of 6." id r3_drawing_da46fbfd

    l "Like Pierrot said, it should be easy."

    show hitona3 worried hat

    pi "Now that you put it that way, I’m not so sure anymore..."

    $ save_enabled = False

    hide hitona3 with dissolve
    hide lios

    play sound quizstart
    $ renpy.pause(3.0, hard=True)

    "START"

    jump quiz_pic_default

    #menu:
        #"Did you succeed?"
        #"Yeah":
            #jump r3_bomb
        #"Nope":
            #jump drawing_fail

label drawing_fail:
    $ save_enabled = True

    scene bg computer with Fade(1.0, 1.0, 1.0)

    show lios front at lios_right with dissolve
    show hitona3 angry hat at hitona_left with dissolve

    pi "Lios...YOUR DOODLE IS HORRIBLE!"

    l "You just don’t understand my artistic sense, Pierrot."

    p "It was a bit..."

    l "Uuugh, if you knew who drew these you would be singing praises instead."

    l "But no matter."

    l "There’s no need to talk about such trifling things anymore."

    l "Since you failed, goodbye."

    l "Go on, shoo shoo."

    show hitona3 surprised2 hat

    pi "Come ooooon we were so close...!"

    pi "Lios, pleeeeeaaase!"

    l "Nope, nothing like that, off you go."

    l "Actually, I’ll just kick you out myself."

    l "Bye."

    stop music fadeout 1.0

    scene bg room with Fade(1.0, 1.0, 1.0)
    play music room_bgm fadein 1.0
    play sound phonecall

    p "Huh?!"

    "I suddenly woke up on my bed. My phone was ringing."

    stop sound

    "XXX" "KOHIIIII! I’ve been waiting for XX minutes already! Where are you!?"

    p "..."

    "I hung up, and dashed out from my room."

    scene black with fade

    "While running towards the park, that dream? kept spinning in my mind."

    "It seems like the meaning of that dream? will stay unknown forever."

    "I guess dreams will just be dreams."

    jump bad_end
