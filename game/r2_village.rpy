label r2_village_init():
    $ v_house1 = 0
    $ v_house2 = 0
    $ v_house3 = 0
    $ v_house4 = 0
    $ v_talk = 0
    return

label r2_village:
    scene bg village with Fade(1.0, 1.0, 1.0)

    show hitona2 smug with dissolve

    p "This is a nice village, but why is there no one outside?"

    e "Maybe it’s because they fear the oh so fearsome Majna Eden Ba-"

    p "Yeah, yeah, you’re right, let’s just explore around."



label village_menu:
    scene bg village with Fade(1.0, 1.0, 1.0)
    call screen village_map

    "Where should we go?"

    scene bg village with dissolve

label village_talk:
    if v_house3 == 0:
        jump village_talk_1
    elif v_talk == 0:
        $ v_talk = 1
        jump village_talk_2
    else:
        jump village_talk_3

label village_house_1:
    if v_house1 == 0:
        $ v_house1 = 1
        jump village_house_1_1
    else:
        jump village_house_1_2

label village_house_2:
    if v_house2 == 0:
        $ v_house2 = 1
        jump village_house_2_1
    else:
        jump village_house_2_2

label village_house_3:
    if v_house3 == 0:
        $ v_house3 = 1
        jump village_house_3_1
    elif v_house3 == 1:
        $ v_house3 = 2
        jump village_house_3_2
    else:
        jump village_house_3_3

label village_house_4:
    if v_house3 == 0:
        jump village_house_4_1
    elif v_house4 == 0:
        $ v_house4 = 1
        jump village_house_4_2
    else:
        jump village_house_4_3

label village_talk_1:

    show hitona2 idle with dissolve

    e "Why are we here again?"

    p "..."

    p "You were the one who said we should go here!"

    show hitona2 smile1

    e "Believe in this Eve! The one blessed by the wind who told me we should come here!"

    p "You had no plan!"

    show hitona2 smile2

    e "Believe in the wind!"

    p "Yes yes, let’s just explore around."

    jump village_menu

label village_talk_2:

    show hitona2 idle with dissolve

    p "You called me second salvation, so who was the first?"

    show hitona2 smug

    e "Of course it is I, the Great Majna Eden Bat Azuma Nula Sedun!"

    p "What does it mean being a salvation anyways...?"

    show hitona2 idle

    e "A salvation is an existence that grants hope to everyone."

    p "Hope huh..."

    jump village_menu

label village_talk_3:

    show hitona2 idle with dissolve

    p "What do the special regions look like anyway?"

    show hitona2 laugh

    e "They are as magnificent as myself!"

    p "That doesn’t explain anything at all..."

    p "You said the magical energy in the regions sometimes go on a rampage or something like that right?"

    show hitona2 idle

    e "Yes, it is horrible! The Captain almost died once because of it!"

    e "A sudden thunderstorm, followed by an earthquake, then a vortex of lightning surrounding him..."

    p "How in the world did he survive that..."

    show hitona2 smug

    e "That’s because of this great Eve!"

    p "I see...I don’t feel like hearing anymore."

    jump village_menu

label village_announcement:
    "“Join the army, not the rebels!”"

    show hitona2 idle with dissolve

    p "What a weird poster..."

    e "It’s from when the rebels and the army were still fighting around this area."

    e "There aren’t many people around here anymore, I doubt anyone will update this or anything."

    jump village_menu

label village_house_1_1:

    play sound dooropen

    show hitona2 idle with dissolve

    e "Hitoni! I have arrived!"

    hn "Oh, it’s been a while. Still traveling around I see."

    hn "Hm? Who’s that girl beside you?"

    show hitona2 smile1

    e "This is our second salvation who will save this world! After me of course~"

    hn "So you’ve found someone compatible?"

    e "Of course! The wind told me so!"

    hn "Well, true or not, don’t let her waste it like you did."

    show hitona2 laugh

    e "Do not fear! This Eve will set things straight once and for all. And then after that everyone will be subjects of King Eve!"

    hn "Again with that talk..."

    show hitona2 idle

    e "Anyways, this is our second salvation, her name is [player_name]. Found her in the forest." id village_house_1_1_d0d441c3

    p "Nice to meet you, I’m [player_full_name]." id village_house_1_1_4ac634e1

    hn "Nice to meet you."

    hn "So, what brings you here?"

    e "Show us your spell selection!"

    e "[player_name] only has Wind Blast right now." id village_house_1_1_913add89

    p "Huh? He has spells? I thought only the army could use magic?"

    hn "Well, the army pretty much never comes here these days. So, which one do you want?"

    menu:
        "Upgrade Wind Blast to Wind Cutter":
            $ hitona_stats["spell"][0] = "Wind Cutter"
            play sound correctchoice
            "{b}Wind Blast has been upgraded into Wind Cutter!{/b}"
            jump village_menu
        "Get Fire Ball (Occasionally inflicts the Burn Status)":
            play sound correctchoice
            "{b}You have obtained the Fire Ball spell!{/b}"
            $ hitona_stats["spell"].append("Fire Ball")
            jump village_menu
        "Get Electric Bolt (Occasionally inflicts the Paralysis Status)":
            play sound correctchoice
            "{b}You have obtained the Electric Bolt spell!{/b}"
            $ hitona_stats["spell"].append("Electric Bolt")
            jump village_menu

label village_house_1_2:
    play sound dooropen

    hn "Did you forget something?"

    p "No nothing, just wondering what’s your relation with Eve."

    hn "You could’ve just asked Eve herself."

    p "Her talk is nonsense most of the time though..."

    hn "Hahaha! You got that right!"

    show hitona2 pout

    e "My eye is sensing someone is mocking this great Majna Eden Bat Azuna Nula Sedun!"

    p "Speak of the devil."

    hn "Ahaha, I’ll tell you later then."

    jump village_menu

label village_house_2_1:

    play sound dooropen

    "???" "Who would come to this place in the middle of the day? I don’t have any money!"

    show hitona2 laugh

    e "You should be grateful that this great Majna came out to greet you!"

    "???" "Oh, it’s you. Even worse, hurry up and get out."

    show hitona2 surprised

    e "Ungrateful as always, Hitoshi."

    hs "Nothing good ever comes when you’re nearby."

    hs "Hmm? Who’s that behind you?"

    show hitona2 smile1

    e "Glad you asked! This is the world’s second salvation! After me of course!"

    hs "Salvation you say... You’re always talking big but have nothing to show for it."

    e "There’s no need to worry! This time around, the wind is telling the truth!"

    hs "But I see you’re still in great spirits. You should go and greet the Captain if you haven’t already."

    jump village_menu

label village_house_2_2:

    play sound dooropen

    hs "What do you wa... oh it’s you. I didn’t catch your name last time."

    p "It’s [player_full_name]." id village_house_2_2_ca928913

    hs "[player_last_name] hmm? It would be nice if what Eve said, about you being the world’s salvation, is true..." id village_house_2_2_509080dd

    p "I have no idea what you two are talking about, but I doubt it..."

    hs "Well, it’s fine. It’s good to have a little bit of hope every now and then."

    jump village_menu

label village_house_3_1:

    play sound dooropen

    show hitona2 laugh with dissolve

    e "Captain! The Great Majna has come with the world’s second salvation!"

    "???" "Huh, if it isn’t Eve!"

    "???" "Second salvation you say? Is she the one beside you right now?"

    show hitona2 smile1

    e "Yep, she’s [player_name]." id village_house_3_1_d24acfd4

    p "Nice to meet you, I’m [player_full_name]." id village_house_3_1_4ac634e1

    "???" "Given Eve’s personality, I guess you probably just got dragged her without any much explanation."

    p "You got that right, I have no idea why I am here."

    show hitona2 idle

    e "Well then, I will leave [player_name] to you, Captain! I’ll be waiting outside." id village_house_3_1_dea3fd8a

    hide hitona2 with dissolve

    play sound dooropen

    "Saying that, Eve left the house."

    "???" "So, how did you end up here?"

    p "You tell me...I somehow got suddenly dragged into this world, somehow fought a soldier with magic, and got dragged around by that weird girl."

    "???" "Ahahahahaha as expected of Eve!"

    hj "First of all, I am Hitoju."

    hj "You said you got suddenly transported into this world... I see, now I understand why she calls you the second salvation."

    p "Well I don’t!"

    hj "Hahaha, calm down, calm down."

    hj "Have some tea?"

    "Hitoju poured some tea to a cup and offered it to me."

    hj "So, to what extent has she explained it to you?"

    "I summarized everything Eve had told me up until now."

    hj "Hmmm...Is that so..."

    hj "Basically, we want the king to be defeated, and that is the reason Eve brought you here."

    p "I don’t see how someone who doesn’t know anything can help you reach that goal."

    hj "Honestly, the King’s army is frankly very powerful. So powerful that the only way for us to defeat him is to use the Ultimate Spells."

    p "Ultimate spells?"

    hj "Ultimate spells are very powerful spells that reside in the three special regions near here."

    p "You mean the ones called Tranquility, Turmoil, and Rage?"

    hj "Yes, those regions each hold an ultimate spell."

    hj "What we need you to do is to go to each region and gather all three of the ultimate spells."

    p "Then why doesn’t Eve just do it herself..."

    hj "Unlike normal spells that can be used by anyone, ultimate spells can only be gathered and used by chosen people."

    p "And you’re saying I’m chosen?"

    hj "Ahaha, who knows."

    hj "But that’s what Eve thinks, so let’s just believe her for now."

    hj "With that said, will you help us?"

    label village_forced_option:
        menu:
            extend ""

            "I’ll go collect the ultimate spells for you":
                hj "That’s the spirit!"

                hj "I recommend going to Tranquility first. It’s safer than the other special regions."

                hj "Have a good journey!"

                play sound dooropen

                "I went out and found Eve waiting."

                show hitona2 idle with dissolve

                e "Oh you’re done talking with the Captain?"

                p "Yeah, he said we should go to Tranquility"

                e "Let’s stop by my domain before that then."

                p "Where is that?"

                e "It’s on the bottom right of the map."

                jump village_menu

            "Nope, it sounds too annoying":
                hj "Don’t be like that, you are our last hope. Just think of this as a little fun trip. How about it?"

                jump village_forced_option

label village_house_3_2:

    play sound dooropen

    hj "Do you need something from me?"

    p "Uhhh no, nothing."

    hj "Well great timing, I was going to give you this."

    play sound correctchoice

    "{b}You have obtained God Blessing!{/b}"

    $ hitona_stats["item"].append("God Blessing")

    hj "It’s gonna get rough out there, stay safe."

    hj "May you not run into any soldiers."

    jump village_menu

label village_house_3_3:

    play sound dooropen

    hj "Back here again."

    p "I have no excuse."

    hj "Well you got places to go."

    e "Yeah we got places to go, let’s go."

    jump village_menu

label village_house_4_1:

    show hitona2 angry with dissolve

    e "This a very dangerous domain; let’s explore somewhere else first!"

    p "Looks normal to me though..."

    jump village_menu

label village_house_4_2:

    play sound dooropen

    show hitona2 idle with dissolve

    p "I see, so this is your house."

    "The house was filled to brim with books, and Eve was busily searching through them."

    e "Now where did I put it..."

    p "What are you trying to find?"

    "I tried flipping some books as well."

    p "{i}What is this language...I can’t read it at all!{/i}"

    e "Here we go! Some hints about the Tranquility region!"

    p "Huh? Hints? What?"

    e "If you thought we could casually stroll into the region and pick up the ultimate spell, you are going to be very disappointed."

    e "The spells are hidden and sealed behind some kind of mechanism."

    p "Is that so..."

    e "The hint for the Tranquility region is..."

    e "{b}“What you seek lies deep in the water.”{/b}"

    p "That seems really straightforward."

    e "...I sure hope so."

    e "Let’s go when you are ready!"

    # Triggers the World Map to be open again

    jump village_menu

label village_house_4_3:

    show hitona2 idle with dissolve

    e "I know my domain is such a lovely place, but we got places to go."

    jump village_menu
