label r2_start:
    scene bg forest with Fade(1.0, 1.0, 1.0)

    play music forest fadein 1.0

    p "…"

    p "…"

    "I see…trees…huts…bushes…"

    p "…eh?"

    play sound bushrustling

    "I see a bush beside me was moving and suddenly something popped out from it"

    "??" "You! Are you the one??"

    "It was a girl with a cat ear hoodie and wearing an eyepatch"

    # idle

    p "Huh? What are you talking about?"

    #pout2

    "??" "Based on your expression it seems you have been cursed by the brain manipulation spell"

    #smile1

    "??" "I am just glad that they didn’t manage to control you completely instead only manage to erase some of your memory"

    "??" "In that case, a proper introduction is required"

    e "I am Majna Eden Bat Azuma Nula Sedun, you can just call me Eve"

    p "Huh???? There are so many things I want to point out but first…how did that become Eve???!"

    play sound staffsummon

    "This girl suddenly manifested a staff from nowhere onto her hand"

    #idle

    play sound magiccasting

    p "By the blessing of the wind, cleanse this girl from its curse"

    "As she said that, my body lighted up a bit then dimmed back"

    #angry3

    e "I see so your name is Hitona, and you were summoned here by…hmm how do I say this name… ‘Risu…’ dunno how to say it but I have to say my thanks to them later"

    p "What are you talking about…"

    #smile1

    e "Well welcome to the Kingdom of Soso!"

    e "The kingdom of magic~"

    p "Magic?"

    e "Just so you know this Kingdom is known for its usage of magic"

    #angry3

    e "But because of the current king, King Achnost, he’s suppressing the usage of it by monopolizing it"

    #angry2

    e "King Achnost is the worst! He is taking tax from his people way too much just for his own benefit"

    p "Is that so…"

    #angry3

    e "Because of that rebels were popping out one by one and band together to defeat the king"

    e "But because of the king monopolizes magic, the rebels are defenseless and now is no more"

    p "Haaa…"

    #laugh2

    e "With that! I shall defeat the king!"

    p "Huh??"

    #angry3

    e "King Achnost only order people around and then laze around after!"

    #smug1

    e "I want to be a NEET King like him!"

    p "Wow…"

    play sound footstepforest

    "Now that think about it…there is someone who is running towards here for a while"

    "And now he’s here"

    #soldier
    #angry3

    so "You there! Halt!"

    p "We weren’t even moving though…"

    e "Geeeh, it’s the guard…Well Hitona going to the forest is a bad idea so I guess we just have to stop him here!"

    p "What?"

    play sound staffsummon

    e "Here a staff you can use, it has ‘Wind Blast’ spell In it"

    p "Wait…what??"

    e "Help me, I’ll properly explain everything after this"

    #blank

    stop music fadeout 1.0

    '''
    You’re going to get into a fight

    Here you can use spells or items to attack or heal

    If you use an attacking spell you can multiply your damage by winning the rock paper scissor!

    If you lose, you’ll do half damage

    What’s a  better way to learn then just try it? Let’s go!
    '''

    play music battletheme_bgm fadein 1.0 volume 0.5

    #angry3 during fight

    #Gets into fight
    python:
        fight_order = [hitona_stats, eve_stats, soldier1_stats]
        fight_list = [eve_stats, soldier1_stats]
        ally_list = [hitona_stats, eve_stats]
        enemy_list = [soldier1_stats]
        fight_label = "r2_start_after_battle"
        x = 0

    "FIGHT!"

    jump r2_fight

label r2_start_after_battle:
    scene bg forest with dissolve

    hide screen multi_stat
    hide screen multi_sprite
    play music forest fadein 1.0

    #smug1

    e "That was easy~"

    p "How was that easy…it took my everything just to cast some spell…and how I could use magic..."

    "It feels like I only got confused since I got here"

    "And I am so exhausted from that fight…"

    #idle

    e "Well everyone can use magic if they have a spell orb"

    p "Spell orb?"

    e "Yup, it’s an orb where magic is stored"

    e "Like the one you used, when you use magic spell stored in the orb you use your own energy to activate it"

    p "So why did that soldier attack us again?"

    #laugh2

    e "Ah…because I’m on the wanted list"

    p "Because you were rebelling against the king before?"

    #idle

    e "Well that is one but it’s mainly because I’ve been collecting and stealing orbs from all around"

    p "Eeeeeh?"

    e "Well you know I did say the king is monopolizing all the magic, so no one is allowed to use it"

    #smile1

    e "So here I am being a wanted person~"

    e "Well either way, come with me Hitona!"

    p "Eeh why?"

    #idle

    e "You don’t know where to go anyway right?"

    "I looked at my room…which is not there anymore…"

    p "Fine then…"

    #smile2

    e "Let’s go then~"

    stop music fadeout 1.0

    "You can check same place more than once"

    "Be sure to check them all!"

    play music adventure_bgm fadein 1.0

    jump r2_forest
