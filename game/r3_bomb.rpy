label r3_bomb:
    $ save_enabled = True

    scene bg quiz with fade

    show lios front at lios_right with dissolve
    show hitona3 happy hat at hitona_left with dissolve

    pi "Ahhh, sure brings back memories."

    l "Amazes me that you still remember those drawings, Pierrot."

    pi "It reminds me of when Kohigashi was playing XXXXXX and she drew XXXX."

    p "Yeah, that’s right!"

    p "{i}Huh?{/i}"

    p "{i}What was I saying?? What game? What drawing?{/i}"

    show hitona3 worried hat

    l "She still looks confused, Pierrot."

    pi "Haa..."

    l "You underestimate this domain effect."

    l "But those who reach the end will surely be justly compensated."

    show hitona3 angry hat

    pi "You’re the one who stole it though..."

    l "Hey don’t blame me!"

    l "You’re the one who triggered it!"

    l "Well anyways, off you go to the last challenge."

    p "You said last????"

    l "Yeah, I did."

    p "I can’t believe it..."

    show hitona3 surprised1 hat

    pi "Which is why we should hurry!"

    scene bg hub with Fade(1.0, 1.0, 1.0)

    "Pierrot pulled my hands and led me on a search for the last challenge."

    "Though it will probably just drop out of nowhere."

    p "What were you talking about with Lios earlier?"

    show hitona3 idle hat with dissolve

    pi "What do you mean?"

    p "About the domain effect and what not."

    pi "Hmmm, I guess it’s fine to tell it now since it is the last challenge."

    pi "Basically, Lios’ domain has the effect of amplifying a human’s forgetfulness."

    p "Huh??"

    pi "It’s really strong!"

    pi "It can cause you to forget even the most obvious things."

    p "Is that so..."

    "While I was still processing what Pierrot said, the scene suddenly changed again."

    scene bg hub with fade

    show lios front with dissolve

    stop music fadeout 2.0

    pause 2.0

    play music bomb_intro_bgm noloop

    l "The last challenge!"

    l "Go on~ Your worst enemy is next."

    p "Eh? Worst enemy??"

    pi "Don’t falter, Kohigashi! You can do it!"

    l "You have to escape from the maze within the time limit. If you’re too slow..."

    l "The bomb will explode."

    p "What????"

    l "Here, a map, I’ll let you see it for a little bit."

    l "The time limit is 2 minutes, yes, 2 minutes for you who’s sitting on the other side of the monitor."

    l "Right after I take the map back, 2 minutes, good luck~"

    hide lios with dissolve
    show hitona3 angry hat with dissolve

    pi "WHAT? This is not part of the plan LIOOOS!"

    $ save_enabled = False

    play music bomb_loop_bgm loop volume 0.2 fadein 3.0

    jump bomb_mechanic

    init python:
        r3_secret = False

label bomb_fail:
    $ save_enabled = True
    hide countdown
    scene black
    stop music
    play sound bombexplode

    "{size=100}BOOM!{/size}"

    $ renpy.pause(3.0)

    scene bg hub with fade

    play music lios_bgm fadein 1.0 volume 0.1

    "We got sent back to the first room."

    show lios front at lios_right with dissolve

    l "Told you it was your worst enemy."

    show hitona3 angry hat at hitona_left with dissolve

    pi "You mean exercise?!"

    p "Huff...nothing...huff...I could...huff...do...huff...about that..."

    show hitona3 pout hat

    pi "Aren’t you annoyed?! That’s the last challenge!"

    pi "Lios you must have cheated somehow!"

    l "That doesn’t really matter now, does it?"

    l "I make the rules here."

    l "You’re only players."

    pi "Cheater! cheater! Lios is a cheater!"

    p "After all that, you still have the energy to get angry huh, Pierrot."

    show hitona3 worried hat

    pi "Well, oh well. I guess we can try it again at another time."

    l "Yes, yes, off you go, little girls."

    l "Until next time."

    stop music fadeout 1.0

    scene bg room with Fade(1.0, 1.0, 1.0)

    play music room_bgm fadein 3.0 volume 0.2

    "{i}Eh? I’m in...my room? On my bed...{/i}"

    "{i}Even if that was a dream, I wonder what was stolen...{/i}"

    "I looked up at my phone screen."

    p "..."

    p "AAAAAAA I’M SO SORRY SENPAI!"

    "I rushed out of my room in a hurry to meet senpai."

    scene black with dissolve

    "While running towards the park, that dream? kept spinning in my mind."

    "It seems like the meaning of that dream? will stay unknown forever."

    "I guess dreams will just be dreams."

    jump bad_end
