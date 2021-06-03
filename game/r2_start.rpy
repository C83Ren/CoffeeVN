label r2_start:
    scene bg forest

    p "…"

    p "…"

    "I see…trees…huts…bushes…"

    p "…eh?"

    "I see a bush beside me was moving and suddenly something popped out from it"

    "??" "You! Are you the one??"

    "It was a girl with a cat ear hoodie and wearing an eyepatch"

    p "Huh? What are you talking about?"

    "??" "Based on your expression it seems you have been cursed by the brain manipulation spell"

    "??" "I am just glad that they didn’t manage to control you completely instead only manage to erase some of your memory"

    "??" "In that case, a proper introduction is required"

    e "I am Majna Eden Bat Azuma Nula Sedun, you can just call me Eve"

    p "Huh???? There are so many things I want to point out but first…how did that become Eve???!"

    "This girl suddenly manifested a staff from nowhere onto her hand"

    p "By the blessing of the wind, cleanse this girl from its curse"

    "As she said that, my body lighted up a bit then dimmed back"

    e "I see so your name is Hitona, and you were summoned here by…hmm how do I say this name… ‘Risu…’ dunno how to say it but I have to say my thanks to them later"

    p "What are you talking about…"

    e "Well welcome to the Kingdom of Soso!"

    e "The kingdom of magic~"

    p "Magic?"

    e "Just so you know this Kingdom is known for its usage of magic"

    e "But because of the current king, King Achnost, he’s suppressing the usage of it by monopolizing it"

    e "King Achnost is the worst! He is taking tax from his people way too much just for his own benefit"

    p "Is that so…"

    e "Because of that rebels were popping out one by one and band together to defeat the king"

    e "But because of the king monopolizes magic, the rebels are defenseless and now is no more"

    p "Haaa…"

    e "With that! I shall defeat the king!"

    p "Huh??"

    e "King Achnost only order people around and then laze around after!"

    e "I want to be a NEET King like him!"

    p "Wow…"

    "Now that think about it…there is someone who is running towards here for a while"

    "And now he’s here"

    so "You there! Halt!"

    p "We weren’t even moving though…"

    e "Geeeh, it’s the guard…Well Hitona going to the forest is a bad idea so I guess we just have to stop him here!"

    p "What?"

    e "Here a staff you can use, it has ‘Air Blast’ spell In it"

    p "Wait…what??"

    e "Help me, I’ll properly explain everything after this"

    #Gets into fight
    python:
        fight_order = [hitona_stats, eve_stats, soldier1_stats]
        ally_list = [hitona_stats, eve_stats]
        enemy_list = [soldier1_stats]
        fight_label = "r2_start_after_battle"
        x = 0

    "FIGHT!"

    jump r2_fight

label r2_start_after_battle:
    scene bg forest

    hide screen multi_stat

    e "That was easy~"

    p "How was that easy…it took my everything just to cast some spell…and how I could use magic..."

    "It feels like I only got confused since I got here"

    "And I am so exhausted from that fight…"

    e "Well everyone can use magic if they have a spell orb"

    p "Spell orb?"

    e "Yup, it’s an orb where magic is stored"

    e "Like the one you used, when you use magic spell stored in the orb you use your own energy to activate it"

    p "So why did that soldier attack us again?"

    e "Ah…because I’m on the wanted list"

    p "Because you were rebelling against the king before?"

    e "Well that is one but it’s mainly because I’ve been collecting and stealing orbs from all around"

    p "Eeeeeh?"

    e "Well you know I did say the king is monopolizing all the magic, so no one is allowed to use it"

    e "So here I am being a wanted person~"

    e "Well either way, come with me Hitona!"

    p "Eeh why?"

    e "You don’t know where to go anyway right?"

    "I looked at my room…which is not there anymore…"

    p "Fine then…"

    e "Let’s go then~"

    jump r2_forest

label end_5:
    $ persistent.ed_unlocked_5 = True
    "route 2 end"
    return
