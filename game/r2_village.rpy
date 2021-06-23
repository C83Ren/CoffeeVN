init python:
    v_house1 = 0
    v_house2 = 0
    v_house3 = 0
    v_house4 = 0
    v_talk = 0

label r2_village:
    scene bg village

    "After a bit we arrived at the village"

    #smug1

    p "This is a nice village, but why there’s no one outside?"

    e "Maybe they fear the oh so fearsome Majna Eden Ba-"

    p "Yeah you’re right, let’s just explore around"

label village_menu:
    scene bg village
    menu:
        "Where should we go~"
        "Talk":
            jump village_talk
        "Announcement Board":
            jump village_announcement
        "House 1":
            jump village_house_1
        "House 2":
            jump village_house_2
        "House 3":
            jump village_house_3
        "House 4":
            jump village_house_4
        "World Map" if v_house4 > 0:
            jump r2_map_2

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

    #idle

    e "Why are we here again?"

    p "…"

    p "You were the one who said we should go here!"

    #smile1

    e "Put trust in Eve, the wind blesses me and told me we should go here"

    p "You had no plan!"

    #smile2

    e "Put trust in the wind~"

    p "Yeah right, let’s just explore around"

    jump village_menu

label village_talk_2:

    #idle

    p "You called me second salvation, what was the first?"

    #smug1

    e "It is I, the Great Majna Eden Bat Azuma Nula Sedun"

    p "What does it mean being a salvation anyway?"

    #idle

    e "It means giving hope to everyone"

    p "Hope huh…"

    jump village_menu

label village_talk_3:

    #idle

    p "How the special region looks like anyway?"

    #laugh2

    e "They are as magnificent as myself~"

    p "That doesn’t explain anything…you said the magical energy sometimes go on a rampage or something right"

    #idle

    e "Yes, it is horrible. Captain Jack almost died because of it"

    e "A sudden thunderstorm, followed by an earthquake, then a vortex of lightning bolt surrounding him"

    p "How did he survived that…"

    #smug1

    e "All thanks to the Great Eve’s help~"

    p "I see…not gonna bother asking"

    jump village_menu

label village_announcement:
    "\"Join the army not the rebels!\""

    #idle

    p "What a weird poster"

    e "It is from when the rebel and the army were still fighting around here"

    e "Not many people around here anymore, don’t think they will bother updating this"

    jump village_menu

label village_house_1_1:

    play sound dooropen

    #idle

    e "Hitoni! I am here!"

    hn "Oh been a while. Still Traveling around I see"

    hn "Hm? Who’s that beside you?"

    #smile1

    e "This is our second salvation! After me of course~"

    hn "So you’ve found someone compatible?"

    e "Of course~ The wind is telling me so"

    hn "Either it is true or not, don’t let her waste it like you did"

    #laugh2

    e "“Afraid not Hitoni, Eve will set things straight once and for all. And you all will be under King Eve~"

    hn "Again with that talk"

    #idle

    e "Anyway our second salvation name is Hitona, found her in the forest"

    p "Hello I’m Hitona"

    hn "Nice to meet you Hitona, what brings you here?"

    e "Show us your spell selection. She only has Wind Blast now"

    p "Huh? He has spells? Isn’t the only one who has spells is the army?"

    hn "The army almost never comes to this place anymore. So what do you want to have?"

    menu:
        "What should I get?"
        "Upgrade Wind Blast to Wind Cutter":
            $ hitona_stats["spell"][0] = "Wind Cutter"
            play sound correctchoice
            "You get Wind Cutter spell!"
            jump village_menu
        "Get Fire Ball (Burn Effect)":
            play sound correctchoice
            "You get Fire Ball spell!"
            $ hitona_stats["spell"].append("Fire Ball")
            jump village_menu
        "Get Electric Bolt (Paralysis Effect)":
            play sound correctchoice
            "You get Electric Bolt spell!"
            $ hitona_stats["spell"].append("Electric Bolt")
            jump village_menu

label village_house_1_2:
    play sound dooropen

    hn "Did you forget something?"

    p "No nothing, just wondering what’s your relation with Eve"

    hn "You could’ve just asked Eve"

    p "Her talk is nonsense most of the time"

    hn "Hahaha! You got that right!"

    #pout2

    e "My eye is sensing someone is mocking the great Majna Eden Bat Azuna Nula Sedun!"

    p "See? Told you"

    hn "Well I’ll tell you later okay Hitona~"

    jump village_menu

label village_house_2_1:

    play sound dooropen

    "??" "Who would come to this place in the middle of the day, I got no money okay~"

    #laugh2

    e "You should be grateful that the great Majna is came to greet you"

    "??" "Oh…it’s you…Even worse, get out"

    #surprised1

    e "Such ungrateful person you are Hitoshi"

    hs "Nothing good ever comes when you’re around"

    hs "Hmm? Who’s that behind you?"

    #smile1

    e "Glad you asked, she’s the second salvation, after me of course!"

    hs "Salvation you say…You talk big but nothing to show"

    e "Don’t worry this time the wind is telling the truth"

    hs "But I see you’re still in great spirit. You should greet the Captain if you haven’t already"

    jump village_menu

label village_house_2_2:

    play sound dooropen

    hs "What is it this time, oh it’s you. I didn’t catch your name"

    p "It’s Hitona"

    hs "Hitona hmm? I hope Eve is right this time about you being the salvation"

    p "I have no idea what you two are talking about, but I doubt it"

    hs "It’s fine, a little bit of hope is nice to have"

    jump village_menu

label village_house_3_1:

    play sound dooropen

    #laugh2

    e "Captain! The Great Majna is here with the one who’ll bring the second salvation~"

    "??" "Huh if it isn’t Eve"

    "??" "Second salvation you say? Is it the one beside you right now?"

    #smile1

    e "Yes it is her, she’s Hitona"

    p "I’m Hitona nice to meet you"

    "??" "Considering your personality, I am guessing you just dragged her here without much explanation"

    p "You got that right, I have no idea why I am here…"

    #idle

    e "Well then Eve will leave Majna to you captain, I’ll be waiting outside"

    #hide eve

    play sound dooropen

    "Eve then left the house leaving me alone with this man"

    "??" "So Hitona why are you here?"

    p "You tell me! I somehow got into this world then fought some soldier with magic no less...got dragged around by a weird girl"

    "??" "Ahahahahaha as expected of Eve"

    hj "First of all I am Hitoju"

    hj "You say you got transported here? I see now why she calls you the second salvation"

    p "Well I don’t!"

    hj "Hahaha calm down now, have some tea"

    "Hitoji poured some tea to a cup and offered it to me"

    hj "So, To what extent she explained to you?"

    "I explained what Eve had told me up until now"

    hj "Hmmm…Is that so…"

    hj "Basically we want the king to be defeated, is the reason Eve brought you here"

    p "I don’t see how someone who doesn’t know anything can help you reach that goal"

    hj "The King’s army is frankly very powerful and now the only way for us to defeat him is to use the Ultimate Spells"

    p "Ultimate spells?"

    hj "Ultimate spells are very powerful spells that resides in the special region near here"

    p "You mean the ones called Tranquility, Turmoil, and Rage?"

    hj "You’re right, those regions hold the ultimate spells. We need you to gather it"

    p "Why doesn’t Eve do it herself…"

    hj "Unlike normal spells where it can be used by everyone, ultimate spells can only be use by chosen people"

    p "And you’re saying I’m one of the chosen?"

    hj "Hahaha who knows, but Eve says so. Just believe her for now"

    hj "But the question is, do you want to help us?"

    label village_forced_option:
        menu:
            extend ""

            "No":
                hj "Don’t be like that, you are our last hope. You can think this as a little fun trip. How about it?"

                jump village_forced_option

            "Yes":
                hj "That’s the spirit!"

                hj "For now I recommend you to go to Tranquility. That’s one of the safest special region."

                hj "Good luck with your journey"

                play sound dooropen

                "I went out after that and Eve was waiting there"

                #idle

                e "Oh you’re done with the Captain?"

                p "Yeah, he said we should go to Tranquility"

                e "Let’s stop by my domain before that"

                p "Which one was it again?"

                e "It’s the one on the bottom right if you see the map"

                jump village_menu

label village_house_3_2:

    play sound dooropen

    hj "You need something from me?"

    p "Uuuh no, I guess"

    hj "Well great timing, I was going to give you this"

    "You got God Blessing"

    $ hitona_stats["item"].append("God Blessing")

    hj "It’s gonna get rough out there, just stay safe. Hopefully not run into any soldier"

    jump village_menu

label village_house_3_3:

    play sound dooropen

    hj "Back here again"

    p "I have no excuse"

    hj "Well you got places to go~"

    e "Yeah we got places to go, let's go"

    jump village_menu

label village_house_4_1:

    #angry3

    e "This is a very dangerous domain, let’s explore somewhere else first"

    p "Looks normal to me though…"

    jump village_menu

label village_house_4_2:

    play sound dooropen

    #idle

    p "Huh so this is your house"

    "The house was full of books and Eve was searching through them"

    e "Now where was it…"

    p "What are you trying to find?"

    "I tried flipping some books as well"

    "What is this language…I can’t read it at all"

    e "Here we go, some hints about the Tranquility region"

    p "Huh? Hints? What?"

    e "If you’re expecting we go into the region and casually get the ultimate spell you are going to be very disappointed"

    e "The spells are hidden and locked behind some kind of mechanism"

    p "Is that so…"

    e "So the hint is ‘What you seek lies deep in the water’"

    p "That seems straight forward enough for a hint"

    e "…I sure hope so"

    e "Let’s go when you are ready"

    # Triggers the World Map to be open again

    jump village_menu

label village_house_4_3:

    #idle

    e "I know my domain is such a lovely place, but we got places to go"

    jump village_menu
