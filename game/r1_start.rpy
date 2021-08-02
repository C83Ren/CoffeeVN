label r1_start:
    # Route 1 Start
    #########################################################################################
    # Music: Happy excited, doesn’t loop, > 3 minutes
    # Background: Intersection day
    #
    scene bg intersection day with fade

    "8:00 AM."

    "It’s sunny today. Unlike yesterday..."

    p "{i}What is senpai planning...?{/i}"

    "While enjoying my walk, I noticed a young girl just standing there at the intersection."

    p "{i}Maybe she’s lost?{/i}"

    "While thinking that, the young girl approached me."

    play music hitona_theme fadein 1.0

    show hitona1 idle1 with dissolve

    "???" "Onee-chan!"

    p "Eh? Me?"

    "???" "Yes, onee-chan! Are you busy right now?"

    show hitona1 happy1

    "The girl displayed a bright smile while asking the question. It’s such a bright smile."

    p "Ummm... I’m going to meet a friend right now."

    p "Are you perhaps lost?"

    show hitona1 idle1

    "???" "Not at all! I was just waiting for someone to play with!"

    p "Ehhh?"

    show hitona1 idle3

    "???" "Onee-chan, play with Shiraishi!"

    p "You know... you should be a bit more careful around strangers! Anyways, let’s get you back to your parents."

    show hitona1 pout3

    "???" "Ehhhhh? Noooo! Shiraishi wants to play! Shiraishi wants to play with onee-chaan!"

    p "{i}Ah, this kid is turning out to be more troublesome than I first thought...{/i}"

    "It seems like her name is Shiraishi."

    "I’m at a loss about what to do. For now, I guess I’ll call senpai and tell her about the situation."

    p "Ah, okay, okay, give me a moment."

    p "Let me call my friend first."

    show hitona1 idle2

    s "Okaaay. Shiraishi will waiiit."

    "I took out my phone and called senpai."

    play sound ringingtone
    window hide
    $ renpy.pause(3.0, hard=True)
    stop sound
    # TODO ring tone, pause

    sn "Hello?"

    p "Senpai, I might be a bit late."

    sn "Ah Kohi! What’s the matter? Did something happen?"

    p "So there’s this girl..."

    "I told Senpai what had happened."

    sn "Ah, is that so? Then just go play with her! Don’t worry about me!"

    sn "We can always find another time to meet, no worries!"

    p "Eh?"

    sn "It’s more important for Kohi to play with her! But make sure to have fun with her, okay! Otherwise..."

    sn "You really don’t want to know what’s going to happen. Hehehe..."

    p "H...Huh...? O...Okay...I understand..."

    sn "Okay Kohii, I’m hanging up! See you sometime~"

    play sound endcall

    # TODO endcall

    p "{i}I swear everyone has been so weird recently...{/i}"

    show hitona1 stareyes2

    "At the corner of my vision, Shiraishi was looking up to me with a beaming smile. In any case it looks like I’ll be playing with her."

    p "Shiraishi... was it? Nee-chan will play with you."

    show hitona1 happy1

    s "Yaaay! Let’s play, [player_name] onee-chan!" id r1_start_e2940143

    p "Eh...? Huh...? Yeah...so do you want to play in the park?"

    show hitona1 idle2

    s "No! Shiraishi want to go somewhere with a lot of games!"

    p "You mean the game store?"

    s "No! A place where you put in coins and then play!"

    p "Oooh okay, the game center, right? Yeah sure, let’s go!"

    show hitona1 smile2

    "Holding Shiraishi’s hand, we walked towards the game center."

    p "Shiraishi, how old are you again?"

    s "10 years old!"

    p "Do you always wait around for someone to play like this?"

    s "No, not really. Shiraishi just felt like doing it today."

    s "After all, playing games makes anyone happy!"

    "I could only smile at her innocent response."

    p "{i}I wonder if I was that cheerful and innocent back when I was 10 years old...{/i}"

    stop music fadeout 1.0

    scene bg gamecenter with Fade(0.5, 0.5, 0.5)

    play music game_arcade fadein 1.0

    p "And here we are, the game center~"

    show hitona1 stareyes1 with dissolve

    "Shiraishi was standing by my side; her eyes were filled with excitement."

    "Unable to wait any longer, she let go of my hand and started heading inside without me."

    p "Oiii, Shiraishi!"

    "She seemed to be so entranced by the game center that she couldn’t even hear my voice."

    "Shiraishi walked around the game center, admiring every machine there was."

    "I just quietly followed her without saying a word."

    show hitona1 sad1

    "She took a full round around the game center before finally realizing that I wasn’t walking beside her."

    "Realizing this, she stopped and looked around worriedly, but smiled again when our eyes met."

    show hitona1 happy3

    "She tottered back to me and held my hand again."

    p "So what do you think of the game center?"

    s "It’s really fun!"

    p "We haven’t even tried anything though..."

    s "It’s still fun! [player_name] onee-chan, let’s play something!" id r1_start_d42765e6

    p "What should we play then?"

    show hitona1 idle2

    s "Hmmmm..."

    p "How about a racing game? There’s two of us, so it might be fun if we race against each other."

    s "Hmmm no..."

    p "Then how about the drum rhythm game? It’s fun listening to music as well!"

    s "Ummm... Shiraishi feels like playing something else though..."

    "Even though she was excited looking at everything, she’s unexpectedly picky."

    p "{i}Oh well, I’m not that good at those games anyways.{/i}"

    p "Well then... how about we try the crane game then?"

    show hitona1 stareyes4

    "As soon as I said that, Shiraishi was smiling ear to ear."

    s "Yess! Shiraishi wants to try that with [player_name] onee-chan!" id r1_start_631fed18

    show hitona1 smile1

    "With that said, we started heading towards the crane games."

    "There were plushies, figurines, bags, all sorts of prizes."

    p "{i}Ah that’s right...{/i}"

    p "Which one do you want to try, Shiraishi?"

    s "Hmmm... Shiraishi wants to look around first!"

    p "Okay, let’s have a look around then~"

    "We went from one machine to the next, looking at the different prizes."

    s "Ooooh this one is cute! That one is cute as well!"

    p "Yeah you’re right! This one over here is cute too!"

    "Shiraishi nodded vigorously."

    "And just like that, we spent an hour without trying even a single machine."

    p "Hey, Shiraishi... we should pick one soon; we’ve been looking around for an hour already."

    show hitona1 idle2

    s "Hmmm... but they’re all so cute..."

    p "I know right! It’s such a dilemma! But we still have to pick one."

    p "After all, the trick with crane games is to pick a single machine! It’s no good to try each machine one by one."

    "Shiraishi went into deep thought."

    p "How about that plushie over there? The white dog wearing the yellow shirt? The San**o character."

    show hitona1 smug1

    s "Shiraishi has decided!"

    p "Oh?"

    s "The one with the pretty lady!"

    "Shiraishi was pointing at the machine with bishoujo figurines."

    "It was a Hatsu** Miku figure with an orange jacket and green skirt."

    p "{i}For some reason, it feels like I’ve won this one before...{/i}"

    p "Eh? I totally thought you were going to choose one with a plushie."

    s "No! Shiraishi wants to play the one with the pretty lady!"

    p "Okay then, let’s try it!"

    hide hitona1

    "As soon as I went to insert a coin, various memories flooded into my mind... that struggle... the bitterness and the tears."

    p "{i}For Shiraishi’s sake! Let’s win the prize!{/i}"

    p "Let’s GOO!"

    s "OOOOU!"

    "I put the first coin in."

    play sound quizquestion
    $ renpy.pause(2.0, hard=True)

    #Coin sfx, arcade start sfx

    p "A bit more to the right, a bit forward... right there! No... a bit more to the left... okay, let’s go!"

    show hitona1 sad3

    "As the crane went down, Shiraishi was beside me, fidgeting and staring with hopeful eyes..."

    play sound falsechoice_long
    $renpy.pause(2.0, hard=True)
    #Crane sfx

    "...but the crane didn’t even touch the prize."

    show hitona1 happy2

    s "Don’t worry, [player_name] onee-chan! You’ll definitely get it next time!" id r1_start_2136fc24

    "Shiraishi looks so sure that I’ll get it; I must not disappoint!"

    p "Yes! [player_name] nee-chan will get it this time!" id r1_start_ea796bbf

    hide hitona1

    "I put a second coin in."

    play sound quizquestion
    $ renpy.pause(2.0, hard=True)

    #Coin sfx, arcade start sfx

    p "{i}I didn’t hit it last time so I should try a bit more to the right... a little bit more to the back... ah who cares, let’s just try it!{/i}"

    "Push!"

    p "{i}Ahh, doesn’t seem like it’s gonna work... sigh...{/i}"

    play sound cranegame
    queue sound cranegame
    queue sound cranegame

    $renpy.pause(3.0, hard=True)

    s "[player_name] onee-chan! We got it!!! Yaaaaaay!" id r1_start_dc7811d2

    p "Huh?! We got it???"

    "There it is, the prize. Shiraishi took it and showed it to me happily."

    show hitona1 happy1

    s "Yaaay! Yaaaay! Thank you, [player_name] onee-chan!" id r1_start_dffc0e4f

    p "{i}Wow... even though I was prepared to do this for another 60 times.{/i}"

    "We high-fived with both of our hands!"

    "After that, Shiraishi immediately found another machine that caught her attention."

    "The attention span of a child is shorter than I expected."

    show hitona1 idle2

    "Shiraishi was looking at the popular purikura booth."

    s "[player_name] onee-chan, how does that thing work?" id r1_start_73c7baad

    p "Ah that, you can take a picture of yourself there, then decorate it with cute and funny things!"

    show hitona1 stareyes1

    # On the way Hitona cross upon an intersection with a young girl standing there.
    #
    # Hitona was wondering whether she was lost, but suddenly the young girl came up to her.
    #
    # “Nee-chan! Are you busy?”
    #
    # Hitona was surprised and when looks at her closely her face seems familiar…
    #
    # “Eh? I need to meet someone, but are you lost?”
    #
    # “Not at all! I was waiting for someone to play with!”
    #
    # “eeeh?”
    #
    # Have a little chat, call senpai about the situation, senpai told her not to worry instead just play with the girl.
    # She said she’ll contact her again at a later time and made sure to tell Hitona to play with the young kid.
    # Hitona feels bad but she just followed what her senpai told her to do.
    #
    # Hitona introduced herself to young hitona and likewise young Hitona introduced herself as Shiraishi.
    # They chatted about themselves then Shiraishi asked Hitona to go somewhere.
    #
    # Hitona thought about it for a bit, but then Shiraishi suggested to go to the game center with beaming eyes.
    #
    #########################################################################################
    # Music: Happy excited, doesn’t loop, > 3 minutes (same as before)
    # Background: Game Center
    #
    # They arrived at the game center, then Shiraishi let go Hitona’s hand walked around the game center.
    # She seemed very excited. She walked around the game center and she just realized she left Hitona behind.
    #
    # She went back to Hitona and hold her hand again.
    # Hitona asked what does she want to do.
    #
    # After some thinking they went with the crane game.
    # Some people went in to the purikuri booth.
    #
    # Shiraishi asked what that booth is.
    # Hitona explained it and showed one that she took before.
    # Shiraishi was super excited.
    # She almost seem she is jumping for joy.
    #
    # So do you want to take one?

    menu:
        "Shiraishi was looking at it with hopeful eyes. She’s practically jumping up in the air wanting to try it."
        "Use the purikura":
            jump r1_purikuri
        "Don’t use the purikura":
            jump r1_food_choice_no_purikuri
