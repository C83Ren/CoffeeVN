label start:
    scene bg room with dissolve
    play music room_bgm fadein 1.0 volume 0.2
    #play music "room_bgm.wav"

    # disable save until after questionnaire
    $ quick_menu = False

    #show hitona1 happy3
    #show lios front:
        #xzoom 0.5 yzoom 0.5 xpos 440 ypos 100 xanchor 0 yanchor 0

    #"??" "続けて. 次は君の最悪敵だ~"

    p "Sigh"

    p "What a hot day today is. I'm all sweaty...I have to take a bath again"

    "It was Saturday afternoon. Here I am just lazing around after a series of unfortunate events."

    "Going to a convenience store to get food then a sudden downpour? The weather forecast said it’s sunny! Not to mention that speeding car that splashed all that mud…"

    "And I can’t believe I got lost because of the huge downpour that was happening"

    p "After all that I didn’t even get my favourite chips and lunch! *sigh"

    p "Probably my luck is saved up for this gacha!"

    p "Let’s pull!!!!"

    "Only R cards came up"

    p "…*sigh Yeah right what was I expecting"

    "If I think further I probably can list down how bad today was…As soon as I thought about that"

    play audio doorbell noloop
    pause 1.0

    "??" "Delivery!"

    p "A delivery? I wonder what it is"

    "Mailman" "Here is your delivery maam. For ummm Kohigashi Hitona correct? Please sign here"

    p "Ah yes, okay"

    "The mailman then left leaving a huge box at the front door."

    "On top of the box there was letter attached to it. I took it and opened it"

    "\"Dear Kohi,"

    "Kohi you left this in your old room! Can’t believe you forgot to bring something so huge! Here~ Be thankful that your senpai is so reliable. Hope we can meet sometime~"

    "Sincerely, Your Senpai"

    p "So it was from senpai. Been a while since I last met her"

    p "But really, what is she talking about? I don’t think I would forget bringing something so huge. Let’s see what’s inside"

    p "It’s a…safe?"

    "It was a gray safe that had a lock with a 4 characters password and a keyhole."

    p "I don’t think I ever had this. Hmmm let’s just put it inside and ask senpai what it’s all about"

    "I put the safe inside…which was quite heavy and texted senpai asking what it is"

    "After that I just lazed back to the computer chair. Staring the monitor blankly…"

    p "What to do..."

    "As soon I was lost in thought, a message came"

    "\"“Kohigashiii! I found an interesting questionnaire! Try it Try it!”"

    p "Oh that’s kinda rare and…random but that’s just how she is I guess."

    p "Let’s try it then"

    "I opened the link that was on the message"

    #if  and persistent.ed_unlocked_5 and persistent.ed_unlocked_8:
        #menu:
            #"Try opening the box?"
            #"Yes":
                #
                #$ quick_menu = True
                #jump true_end
            #"No":
                #pass

    menu:
        "1. Enter your name"
        "Kohi":
            $ intro_name = "Kohi"
        "Hitona":
            $ intro_name = "Hitona"
        "Kohigashi":
            $ intro_name = "Kohigashi"

    menu:
        "2. Most favourite color among these"
        "Purple":
            $ intro_color = "purple"
            $ intro_q2 = __("compassionate")
        "Pink":
            $ intro_color = "pink"
            $ intro_q2 = __("cute")
        "Yellow":
            $ intro_color = "yellow"
            $ intro_q2 = __("cheerful")
        "Black":
            $ intro_color = "black"
            $ intro_q2 = __("deep")
        "White":
            $ intro_color = "white"
            $ intro_q2 = __("pure")
        "Red":
            $ intro_color = "red"
            $ intro_q2 = __("passionate")
        "Blue":
            $ intro_color = "blue"
            $ intro_q2 = __("calm")

    menu:
        "3. Favourite food among these"
        "Pasta":
            $ intro_food = "pasta"
            $ intro_q3 = __("herself")
        "Yakiniku":
            $ intro_food = "yakiniku"
            $ intro_q3 = __("others")
        "Salad":
            $ intro_food = "salad"
            $ intro_q3 = __("both herself and others")

    "Then a lot more questions came until this one"

    menu:
        "Which one you want to keep giving (Notice, this option determines the route you’re going to take)?"
        "Support":
            $ route = 1
        "Joy":
            $ route = 2
        "Memories":
            $ route = 3

    p "Finally done! What was the questionnaire gonna give me~"

    python:
        something2 = intro_color + intro_food

        if something2 == "purplepasta":
            something = "You are compassionate towards yourself. A good trait to have! You should always care about yourself"
        elif something2 == "purpleyakiniku":
            something = "You are compassionate towards others. Your friends and those around you must be lucky having you around."
        elif something2 == "purplesalad":
            something = "You are compassionate towards yourself and others. Equally loving everyone is always a good thing~"
        elif something2 == "pinkpasta":
            something = "You think you are cute. Hey no one's judging, and I think you are really cute!"
        elif something2 == "pinkyakiniku":
            something = "You think others are cute. A lot of people are cute physically, but you see beyond that, you see how cute they are even in their hearts."
        elif something2 == "pinksalad":
            something = "You think you and others are cute. When everything in this world is cute, surely the world looks a lot better"
        elif something2 == "yellowpasta":
            something = "You are a cheerful person. Always looking forward to what you're going to do next!"
        elif something2 == "yellowyakiniku":
            something = "You are cheerful when around people. Having a bright sunshine around is a blessing that everyone near you should be grateful"
        elif something2 == "yellowsalad":
            "You are an infinite energy of cheerfulness. Everyone arounds you become suddenly cheerful because of you. I have no idea how, but I want one of you right here in my home~"
        elif something2 == "blackpasta":
            something = "You think deeply about yourself. You often get lost in thought when it concerns you."
        elif something2 == "blackyakiniku":
            something = "You think deeply about others. You often get lost in thought when it concerns others but less when it concers you"
        elif something2 == "blacksalad":
            something = "You are a deep thinker. You think about everything. Be careful going too deep"
        elif something2 == "whitepasta":
            something = "You are an innocent person. No one in this world is more innocent than you. White as sheet, just like a baby"
        elif something2 == "whiteyakiniku":
            something = "You think others are not guilty of anything. Every of their action is a pre determined course for them and they are not guilty of it. They are just following that route"
        elif something2 == "whitesalad":
            something = "You think everyone in this world is innocent. Of course including yourself. As long people can forgive each other and not repeat the mistake they made, the world can be as pure as paper."
        elif something2 == "redpasta":
            "You are very ambitious about your project. Nothing in this world can stop you when you are working on it"
        elif something2 == "redyakiniku":
            something = "You are very ambitious about others project. You stop at nothing to help them reach their goal"
        elif something2 == "redsalad":
            something = "You are avery ambitious person. You want to do all 100% no 200% about anything."
        elif something2 == "bluepasta":
            something = "You are a very calm person. When something involves you, you can think very calmly not panicking and reach a solution quickly without any struggle."
        elif something2 == "blueyakiniku":
            something = "You are a very calm person when it is about others. You can solve other people problem no sweat. But the opposite when it comes to yourself. Probably because you put yourself out of the equation here?"
        else:
            something = "You are a very calm person. The most calm person in the world. I want you to be my consultant"

    "[something]"

    #"\"{color=#a0a}{b}[intro_name]{/b}{/color} is {color=#a0a}{b}[intro_q2]{/b}{/color} to {color=#a0a}{b}[intro_q3]{/b}{/color}.\""

    p "…That’s it??? After all those questions that’s it???? Such a day this has been…"

    """
    I looked outside and the clock, it was already midnight.

    How did that questionnaire took so much time…uugh…I feel sleepy…I’ll just sleep
    """

    stop music fadeout 1.5
    play sound ["<silence 5.0 loop 5.0>", alarm] loop
    scene bg room with Fade(2.0, 4.0, 3.0)
    $ quick_menu = True

    p "Uuugh…is it a call…ughh"

    "I picked up the phone saw it was senpai calling"

    stop sound
    play music ["<silence 1.0 loop 1.0>", room_bgm] fadein 3.0 volume 0.2

    p "…Hello…Morning…"

    sn "Kohiiii! Morniiing! Can you meet me at the park right now?"

    sn "There’s something I want to give you. Well just come okay, I’ll be waiting~"

    """
    She hung up…I didn’t even manage to say anything

    Senpai seemed very excited, well she didn’t reply my message yesterday might as well meet her and ask her directly

    I prepared myself to meet senpai.

    Reach out the door, I can only sigh while looking back at the safe.
    """

    p "Let's go then~"

    if route == 1:
        jump r1_start
    elif route == 2:
        jump r2_start
    else:
        jump r3_start





# just some example stuff that never gets used

label example:
    scene bg conbini

    $ a = 3
    play music p

    "narration"

    play music p if_changed

    show hitona1 idle1

    "more narration"

    # bliss2 for one line only
    hc bliss2 "text1"

    hc "text2"

    # cry1 for one line, then switch to bliss1
    hc bliss1 @ cry1 "text3"

    hc "text4"

    "more narration [a]"

    call show_cg("BirthdayKohi") from _call_show_cg

    "More text"

    return

label utawaku_quiz_example:
    show hitona1 stareyes3
    check_lyrics hc "audio/kokoronasi.mp3" "Enter the following lyrics" "Incorrect, try again" "それはねここにあるよ"

    show hitona1 stareyes4
    hc "Correct"

label map_example:
    scene bg conbini
    show screen map_buttons

    p "This is a map."

    window hide
    $ map_active = True
    $ renpy.pause(hard=True)

default map_visits = [False, False, False]

label map_choice1:
    $ map_active = False
    $ map_visits[0] = True
    p "1"

    jump map_branch_end

label map_choice2:
    $ map_active = False
    $ map_visits[1] = True
    p "2"

    jump map_branch_end

label map_choice3:
    $ map_active = False
    $ map_visits[2] = True
    p "3"

    jump map_branch_end

label map_branch_end:
    if all(map_visits):
        jump map_final
    else:
        window hide
        $ map_active = True
        $ renpy.pause(hard=True)

label map_final:
    hide screen map_buttons

    ""
