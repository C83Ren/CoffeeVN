label r3_end:
label end_3:
    $ save_enabled = True
    scene bg hub with Fade(1.0, 1.0, 1.0)

    play music r3end_bgm fadein 2.0

    show lios front at lios_right with dissolve
    show hitona3 smile hat at hitona_left with dissolve

    pi "Ahhhhhh, finally...!"

    p "Huff...we somehow managed to finish that...huff..."

    pi "Worst enemy? Yeah, because it was too easy, Lios!"

    pi "Don’t you think so too, Kohigashi?"

    p "Huff...what part was easy...huff"

    l "How many tries has this been Pierrot?"

    show hitona3 idle hat

    pi "I have no idea...way too many to count, that for sure."

    pi "I leave the rest to you, Lios."

    p "What’s happening?? I did finish the challenge...right?"

    l "Yeah, don’t worry, congratulations on finishing every challenge there is~"

    show hitona3 smile hat

    pi "Yaaay!"

    l "You really don’t know how long it took you to finish all these, huh."

    p "Did it really take that long?"

    l "Well, one try doesn’t take long."

    p "One try?"

    l "You’ve been doing this more than one time."

    show hitona3 idle hat

    p "Huh?"

    pi "I said it earlier, didn’t I? This domain makes you forget {b}even the most obvious things{/b}."

    p "No way...how many times?"

    l "That’s what I asked Pierrot just now."

    pi "I lost count."

    pi "Somewhere around 11,070 times? I’m really not sure."

    p "...I can’t...believe it..."

    l "Well, all of this was Pierrot’s idea anyway."

    p "Huh?"

    show hitona3 angry hat

    pi "You rat me out now???"

    l "She was the one who ordered me to steal it."

    p "What? Pierrot did????"

    show hitona3 smug hat

    pi "Hmph, fine, everything went according to the plan anyways."

    p "Why do you look so smug!?"

    l "And look where it brought us Pierrot..."

    show hitona3 idle hat

    pi "...yeah let’s not do it again."

    p "Why did you do that?!"

    l "Well anyways, do you know what I stole from you?"

    p "Uhhh no...I don’t think I figured it out yet."

    hide lios
    hide hitona3
    show hitona3 idle hat

    pi "A lasting impression"

    p "Eh?"

    pi "If there’s a lasting impression, you’ll remember it more clearly."

    pi "Such as these challenges."

    hide hitona3
    show lios front

    l "And that is why we stole it from you."

    show hitona3 idle hat
    hide lios

    pi "So it will have a lasting impression."

    hide hitona3
    show lios front

    l "So that you will remember it more strongly when you get it back."

    p "Get what back?!"

    "{color=[l.who_args[color]]}[l]{/color} & {color=[pi.who_args[color]]}[pi]{/color}" "Your memories."

    scene black

    window hide
    show art_1 with dissolve
    $ renpy.pause(3.0)
    hide art_1 with dissolve
    show art_2 with dissolve
    $ renpy.pause(3.0)
    hide art_2 with dissolve
    show art_3 with dissolve
    $ renpy.pause(3.0)

    p "These are...?"

    l "They’re your memories."

    pi "Albeit altered."

    hide art_3 with dissolve

    #show art_4 with dissolve:
        #zoom 0.8
        #xalign 0.5
        #yalign 0.3
    call show_cg("artreel1", False) from _call_show_cg_26

    p "Altered?"

    l "What’s shown here has been a bit altered, that’s all."

    window hide
    scene black with dissolve
    show art_5 with dissolve
    $ renpy.pause(3.0)
    hide art_5 with dissolve
    show art_6 with dissolve
    $ renpy.pause(3.0)

    p "You’re telling me...you’re giving me back altered memories?!"

    hide art_6 with dissolve
    call show_cg("artreel2", False) from _call_show_cg_27

    pi "Don’t worry, don’t worry."

    p "I should worry!"

    scene black with dissolve
    show art_8 with dissolve

    l "She meant that the memories you got back are not altered. Only what’s being shown here is altered."

    window hide
    hide art_8 with dissolve
    show art_9 with dissolve
    $ renpy.pause(3.0)
    hide art_9 with dissolve
    show art_10 with dissolve

    p "But why though..."

    hide art_10 with dissolve
    call show_cg("artreel3", False) from _call_show_cg_28

    pi "To make things more interesting."

    l "So it becomes more memorable?"

    scene black with dissolve
    show art_12 with dissolve

    pi "Probably yeah."

    hide art_12 with dissolve
    call show_cg("artreel4", False) from _call_show_cg_29

    p "Oi, you two sound so unsure about it!?"

    scene black with dissolve
    show art_14 with dissolve:
        zoom 0.5
        xalign 0.5
        yalign 0.3

    pi "Hey, who cares! Just enjoy the view!"

    hide art_14 with dissolve
    show art_15 with dissolve

    l "I have to agree with Pierrot."

    hide art_15 with dissolve
    show art_16 with dissolve:
        zoom 0.5
        xalign 0.5
        yalign 0.3

    "While watching the scene, a thought came to mind."

    hide art_16 with dissolve
    show art_17 with dissolve

    "What will happen to these two after this?"

    hide art_17 with dissolve
    show art_18 with dissolve:
        zoom 0.5
        xalign 0.5
        yalign 0.3

    "As if they had heard me..."

    pi "Don’t be sad, we’ll still be with you, Kohigashi."

    hide art_18 with dissolve
    show art_19 with dissolve:
        zoom 0.8
        xalign 0.5
        yalign 0.3

    p "Eh?"

    pi "We’ll stay inside your memories."

    p "Oh so that’s what you mean..."

    hide art_19 with dissolve
    call show_cg("artreel5", False) from _call_show_cg_30

    l "No, like, in the truest sense; we’re the one managing your memories."

    l "So, we’ll always be in your memories."

    p "What...?"

    scene black with dissolve

    pi "Well that’s how it is, see you!"

    l "See you."

    call show_cg("hitonamemory", False) from _call_show_cg_31

    $ renpy.pause(10.0)

    window hide
    $ _skipping = False
    show image 'images/r3_end.png' with dissolve
    if (not persistent.ed_unlocked_3) and persistent.ed_unlocked_1 and persistent.ed_unlocked_2:
        $ renpy.notify(__("A new route has been unlocked!"))
    $ persistent.ed_unlocked_3 = True
    $ renpy.pause(1.0, hard=True)
    pause
    $ _skipping = True

    scene bg room with fade

    stop music fadeout 1.0

    "{i}What’s this...a key...and paper?{/i}"

    "On the floor were two sheets of paper and a key."

    play sound takecard

    nvl_narrator "“Hey! Did you enjoy the challenges?”"

    nvl_narrator "“By the way, that safe has a 4 digit passcode right?”"

    nvl_narrator "“{b}How many cards are there in a suit in a deck of cards? The answer appears in the passcode.{/b}”"

    nvl_narrator "“Good luck~”"

    nvl clear

    "On the other piece of paper, there was only “1” written on it."

    scene black with fade

    if 'r3_secret' not in globals() or not r3_secret:
        return

label end_5:
label r3_secret_ending:
    if_in_replay:
        scene black

    if True:
        nvl_narrator "Hello, this is BlackRabbit13."

        nvl_narrator "Congratulations for reaching the secret exit of the maze!"

        nvl_narrator "Not sure if it was easier to reach than the normal exit, but congratulations anyways!"

        nvl_narrator "Thank you for playing to the end of the Memories route."

        nvl_narrator "Did you have fun?"

        nvl_narrator "What would you like as a reward for reaching the secret exit?"

        nvl_narrator "Would you like to see a 10 page essay on how cute Hitona is?"

        nvl_narrator "Probably not, right? Haha."

        nvl_narrator "So, just as a little gift, enjoy the extra scenario after this note."

        nvl clear

        nvl_narrator "If you have already finished the Support and Joy routes, please also enjoy the true ending that has just been unlocked."

        nvl_narrator "And if not, please enjoy the remaining routes as well!"

        nvl_narrator "BlackRabbit13"

        nvl clear

        scene bg room with fade
        play music room_bgm fadein 1.0
        play sound apeirosiris loop

        "I’ve been hearing noises from my fridge for a while now."

        "And I’ve been afraid to open it."

        "But the constant noise has been really annoying, and so I mustered up my courage to open it up."

        play sound dooropen

        "When I opened the door, a couple of cups of ominous looking rainbow-colored pudding that a friend gave me a long time ago greeted me."

        p "{i}Yea, there’s no way I’m eating that anytime soon.{/i}"

        "But more importantly! There was a small safe next to those pudding cups that I don’t remember putting in the fridge."

        p "{i}I mean…who the hell would put a safe inside a fridge!{/i}"

        "This must be some kind of joke!"

        "But, recalling events from last time..."

        "My curiosity got the better of me"

        p "{i}Here goes nothing{/i}"

        "I entered the password “503158” that was on the note attached to the top of the (un)safe, and opened it up."

        scene black with dissolve

        "The moment I opened the door, everything went black."

        scene bg secret_field with fade

        "When the light came back to my eyes, I saw a blue sky and an open field."

        p "{i}...{/i}"

        p "{i}Really? Is my house an isekai portal now?{/i}"

        p "{i}Where do I request for exorcism these days...?{/i}"

        "After that flash of thought came to me, I finally realized there was a crowd standing in front of me."

        show rabbit together with fade

        $ renpy.pause(3.0)

        "The crowd was filled with all sorts of...people, if you can call them that."

        "From the center of the crowd, one cute, big, really big, fluffy black rabbit stepped forward to address me."

        show rabbit alone

        r "Who art thou? State thy business this present moment, for thou hast intruded upon these holy grounds of our only goddess!"

        p "I’m Hitona Kohigashi."

        p " I don’t know if you’ll believe me, but it seems that I was cursed by the pudding god and sent here haha..."

        p "{i}For whatever reasons, I don’t feel anxious being sent into another world anymore.{/i}"

        r "Fie?! O’ Goddess Hitona! Please forgive this worthless rabbit for her sinful rudeness!"

        show rabbit together

        "The crowd was visibly shocked, and immediately prostrated before me."

        "At that moment, I finally noticed the statue that they called their goddess."

        p "{i}No matter how you look at it...that statue is me isn’t it...{/i}"

        p "{i}It’s me with a ponytail, in a waitress uniform with stockings...{/i}"

        p "{i}Should I arrest them...{/i}"

        r "Everyone! Chant with me! Chant with all thy hearts poured for our peerless goddess!"

        p "{i}Now what are they up to...{/i}"

        "Everyone" "First of all of course is the ponytail!"
        "Everyone" "Her elegant long purple hair tied up!"
        "Everyone" "It emphasizes that unmatched beautiful face more!"
        "Everyone" "The slight blue hair in front makes it even more noticeable!"
        "Everyone" "While the blue hair that is only behind her neck becomes much more attractive thanks to the sudden change of color from purple to blue!"
        "Everyone" "In a 3D setting, the blue hair in front also makes a critical foreshadowing of what you’re going to see when you see the whole hair!"

        p "..."

        "Everyone" "Next is the clothing!"
        "Everyone" "WHITE UNIFORM!"
        "Everyone" "You expect to see purity radiating from her clothing given her personality, but in reality you see quite a lot of mischievous clothes instead!"
        "Everyone" "For example, her uniform without the frills!"
        "Everyone" "Her cat costume is a no brainer!"
        "Everyone" "Her black jacket emphasizes the mischievous part!"
        "Everyone" "In the video for “Indoor kei nara Trackmaker” she has open shoulders and that skirt and that pose!"
        "Everyone" "SO, pure white clothes are rare and something of a blessing to see...not to mention with that pose!"

        p "{i}I see, I see...That’s how it is huh...{/i}"

        p "ARREST ALL OF THEM!! I WILL--"

        "Before I finished my judgement, a familiar voice called for me from the sky."

        "It was the nostalgic-looking detective and, of course, the phantom thief."

        "They were riding the magenta flame scythe, flying through the sky."

        "Grabbing my hand, the three of us went off into the sky."

        "Seeing that, the rabbit below us ordered the crowd in a huge voice."

        show rabbit together

        r "Compose a VN to memorialize this sacred encounter! We shall offer it to our one and only goddess! Finish it within 2 months and a half!"

        p "{i}What the hell is that guy saying...{/i}"

        scene bg secret_sky

        show lios front at lios_right
        show hitona3 sad hat at hitona_left

        pi "Sorry, Kohigashi! Lios mistakenly left the gateway to this world when he was setting up the maze!"

        pi "We’ll bring you back to your own world now!"

        p "Pierrot?! And Lios too?!"

        p "Long time no see! That explains how I entered this weird world."

        p "Speaking of which, I do recall something being weird about the exit in that maze..."

        show hitona3 pout hat

        pi "That was a bug that Lios left in the maze in order to make the deadline of the VN release."

        pi "He thought there was no way you would find it."

        l "Shut it, Pierrot! That should have been sealed behind the maze wall!"

        l "If you didn’t fail so many times I wouldn’t have needed to make a maze in the first place!"

        p "Well at least you found me quickly and I can go back. All’s well that ends well!"

        p "Besides, I get to see you two again! So I’m glad you left that bug in!"

        show hitona3 idle hat

        "Both of them went silent."

        pi "Well if you say so..."

        show hitona3 happy hat

        pi "I’m also glad we get to see each other again! It’s actually a little bit lonely after all the fun we had."

        l "Station Earth. Station Earth. Please make sure you take all your belongings with you when you leave the scythe. Mind the gap between the scythe and the platform."

        show hitona3 angry hat

        pi "Way to ruin the mood!"

        l "Well we’re always watching her from within anyway. No need to get emotional."

        l "Now here you are, back to your world."

        show hitona3 smile hat

        p "Thanks for the help! See you lat--"

        "I suddenly remembered."

        "Hopping off the scythe, I opened my fridge door."

        "I took out the “pudding” that I would never want to eat and put them inside a small cute paper bag."

        p "Consider these your souvenirs!"

        scene bg secret_pudding

        "I gave them the brightest smile I could, and sent them off with their “gift”."

        window hide

        $ renpy.pause(10.0)

        stop music

        window hide
        show image 'images/extra_end.png' with dissolve
        $ persistent.ed_unlocked_5 = True
        $ renpy.pause(1.0, hard=True)
        pause

    return
