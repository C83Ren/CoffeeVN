label r3_end:
label end_3:
    $ persistent.ed_unlocked_3 = True
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

    "Pierrot & Lios" "Your memories~"

    scene cg 4 unscaled with Fade(1.0, 1.0, 1.0)

    $ renpy.pause(15.0)

label r3_secret_ending:

    if r3_secret:
        nvl_narrator "Congrats for getting the secret exit!"

        nvl_narrator "Not sure if it was easier to get compared to the normal exit, but...congrats anyway!"

        nvl_narrator "Thanks for playing until the end of route 3!"

        nvl_narrator "So what do you get when you reach the secret exit? Do you want to see a 10 page essay on how cute Hitona is? Probably no right w"

        nvl_narrator "So just an extra appreciation. If this is the third route you;ve played, then good luck with the true end."

        nvl_narrator "If not, hope you enjoy the rest of the game!"

        nvl clear

        scene bg room with fade
        play music room_bgm fadein 1.0 volume 0.2
        play sound apeirosiris loop

        "I’ve been hearing noises from my fridge for a while..."

        "And I’m afraid to open it..."

        "After been bothered by it, I mustered up my courage to open it"

        play sound dooropen

        "There was a couple of cups of ominous looking rainbow-colored pudding that someone gave to me from a while back"

        "{i}Yeah I’m not eating that anytime soon{/i}"

        "But more importantly! There was a small safe besides it that I didn’t remember putting inside"

        "{i}I mean...who the hell would put a safe inside a fridge!{/i}"

        "This must be some kind of joke!"

        "But recalling events from last time..."

        "My curiosity got the better of me"

        "{i}Here goes nothing{/i}"

        "I opened the safe with the password “503158” that was on the note that was on the (un)safe"

        scene black with dissolve

        "Then the world went black..."

        scene bg secret_field with fade

        "The moment light came back, I saw a blue sky and an open field"

        "{i}...{/i}"

        "{i}Really? Is my house an isekai portal?{/i}"

        "{i}Where do I request for exorcism nowadays?{/i}"

        "After that flash of thought came to me I finally realized there were other beings standing in front of me"

        show rabbit together with fade

        $ renpy.pause(3.0)

        "The crowd was filled with...random people...if you can call them people that is"

        "From the center of the crowd, there was one cute big, really big, fluffy black rabbit who stepped forward"

        show rabbit alone

        r "Who thou? State thy business this present, for thous hast intruded the holy ground of our only goddess"

        p "I'm Kohigashi Hitona"

        p " I don’t know if you will believe me, but it seems I was cursed by the pudding god and was sent here haha..."

        "{i}For whatever reasons, I don’t feel anxious being sent into another world anymore{/i}"

        r "Fie?! Oh Goddess Hitona! Please forgive me for my rudeness!"

        show rabbit together

        "The crowd was visibly shocked and went to their knees"

        "At this moment, I finally noticed the statue that they call their goddess"

        "{i}No matter how you look at it...that statue is me isn’t it...{/i}"

        "{i}It’s me with a pony tail, in a waitress uniform with stockings...{/i}"

        "{i}Should I arrest them...{/i}"

        r "Everyone! Chant with me! Chant with all thy hearts poured!"

        "{i}Now what are they up to…{/i}"

        "Everyone" "First of all of course the ponytail! Her elegant long purple hair tied up. It emphasized her face more! The slight blue hair in front becomes more noticable."
        "Everyone" "While the blue hair that is only behind her neck becomes much more attractive! Thanks to sudden change of color from purple to blue."
        "Everyone" "In a 3D setting, the blue hairin front makes a critical “foreshadowing” of what you’re going to see when you see the whole hair."

        p "..."

        "Everyone" "Next is the clothing! WHITE UNIFORM! You expect to see such purity from her clothing with her personality, but in reality you see quite a lot of mischievous clothes."
        "Everyone" "For example her uniform without the frills, her cat costume is a no brainer, her black jacket emphasizes the mischievous part. In the track maker she has open shoulder with a skirt and with that pose."
        "Everyone" "SO basically pure white clothes is rare and something of a bless to see...not to mention with that pose!"

        p "I see, I see... That’s how it is huh..."

        p "ARREST ALL OF THEM!! I WILL--"

        "Before I finished my judgement, someone with a familiar voice was calling me from the sky"

        "It was the nostalgic-looking detective and of course the phantom thief"

        "They were riding the magenta flame scythe flying from the sky"

        "Then they grabbed my hand and carried me off with them to the sky"

        "The rabbit down below let out a huge voice to the crowd"

        show rabbit together

        r "Compose a VN out of this holy event! We shall offer it to our goddess! Finish it in 2 months and a half!"

        "{i}What the hell is that guy saying{/i}"

        scene bg secret_sky

        show lios front at lios_right
        show hitona3 sad hat at hitona_left

        pi "Sorry Kohigashi! Lios mistakenly left the gateway to this world when he was setting up the maze."

        pi "We’ll bring you back to your own world now"

        p "Pierrot?! And Lios too?!"

        p "Long time no see! That explains how I entered this weird world."

        p "I think I did find something different while running through that maze..."

        show hitona3 pout hat

        pi "That was a bug Lios left in his maze because he had to rush setting things up before the deadline of the VN release"

        pi "He thought you wouldn’t find it"

        l "Shut it Pierrot! That should have been sealed behind the maze wall!"

        l "If you didn't fail so many times I wouldn’t have needed to make a maze in the first place!"

        p "Well at least you found me quickly and I can go back. All’s well that ends well!"

        p "Besides, I get to see you two again! I’m glad you left that bug!"

        show hitona3 idle hat

        "Both of them went silent"

        pi "Well if you say so…"

        show hitona3 happy hat

        pi "I’m also glad we get to see each other again! It’s actually a little bit lonely after all the fun we had"

        l "Station Earth. Station Earth. Please ensure your belonging is not left behind. Mind the gap between the scythe and the platform."

        show hitona3 angry hat

        pi "Way to ruin the mood!"

        l "Well we always see her from within anyway. No need to get emotional"

        l "Now here you are, your own world~"

        show hitona3 smile hat

        p "Thanks for the help! See you lat--"

        "Oh I just remembered"

        "I hopped off the scythe and opened the fridge"

        "I took the “puddings” that I wouldn’t dare eat and put them inside a cute small empty paper bag"

        p "Consider these your souvenirs!"

        scene bg secret_pudding

        "I gave them the brightest smile I could, sending them off with a \"gift\""

        window hide

        $ renpy.pause(10.0)

        stop music


    scene bg room with fade

    p "What’s this?"

    "A paper and a key was on the floor"

    play sound takecard

    nvl_narrator "Hey hope you enjoyed that"

    nvl_narrator "By the way to open the safe you need to input some passcode right?"

    nvl_narrator "Well the passcode is just how many cards there are in one suit of trump cards and the number from your own name!"

    nvl_narrator "Here you get the number 0~"

    nvl_narrator "Good luck~"

    nvl clear

    return
