label r1_home_bad_end:
    stop music fadeout 1.0

    p "It’s getting late, Shiraishi; you should go home now. I’ll accompany you."

    show hitona1 smile4

    "Shiraishi looked surprised."

    s "..."

    s "..."

    show hitona1 smile1

    "She nodded reluctantly without saying anything."

    p "Let’s go then. Which way do we go?"

    s "Don’t worry, [player_name] onee-chan. Just, follow me." id r1_home_bad_end_5929b738

    "Saying that, Shiraishi stood up and led the way."

    scene bg intersection day with Fade(0.5, 0.5, 0.5)

    play music r2bad_bgm fadein 1.0

    "We walked for quite a long time."

    p "Shiraishi, are you maybe lost?"

    show hitona1 smile1 with dissolve

    s "It’s okay, [player_name] onee-chan. We’ll be there soon." id r1_home_bad_end_fb854112

    scene bg intersection evening with dissolve

    "We then walked and walked and walked."

    "It didn’t seem like we were getting any closer, and the sun was also starting to set."

    p "Hey Shiraishi..."

    "Without turning around, she stopped in place."

    s "[player_name] onee-chan, I really had a lot of fun today." id r1_home_bad_end_53a1cc0b

    s "I hope we can do something again, someday! See you!"

    p "Eh?"

    window hide
    play sound phonecall
    $ renpy.pause(2.0, hard=True)

    # phonecall tone

    "My phone is ringing."

    stop sound

    sn "I told you, right, to have fun with that girl."

    p "Eh...? Senpai?"

    sn "Ah it doesn’t matter anymore, don’t think too much about it, Kohi."

    "Senpai hung up."

    p "Eh? Shiraishi? Where are you?"

    p "{i}She was... right... the...{/i}"

    scene bg famres with Fade(2.0, 1.0, 2.0)

    "Friend" "OOOOI! KOHIII!"

    p "Eh?"

    "Friend" "You’ve been daydreaming for a while now, is something on your mind?"

    p "Eh... ah... no... nothing at all... nothing... at all."

    p "What were we talking about again?"

    "Friend" "I guess I can’t help it..."

    "Friend" "So Kohi! I was playing this one game..."

    "What was that all about? Was it a dream?"

    "My memory has become fuzzy, and I can’t clearly remember it anymore."

    "I guess dreams will just be dreams."

    jump bad_end
