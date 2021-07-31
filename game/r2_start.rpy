label r2_start:
    scene bg forest with Fade(1.0, 1.0, 1.0)

    play music forest fadein 1.0

    p "..."

    p "..."

    "{i}Trees...huts...bushes...{/i}"

    "It seems like I’ve been suddenly transported to a forest. In the distance, a person could be seen running this way."

    p "..."
    p "...eh?"

    play sound bushrustling

    "The bush beside me suddenly started moving, and something suddenly popped out...!"

    "???" "You! Are you the chosen one??"

    "It was a girl wearing a cat ear hoodie and an eyepatch."

    show hitona2 idle with dissolve

    p "Huh? What are you talking about?"

    show hitona2 pout

    "???" "Based on your expression it seems you have been cursed by a brain manipulation spell."

    show hitona2 smile1

    "???" "It’s good that you aren’t being completely controlled though, and are only suffering from some memory loss."

    "???" "In that case, a proper introduction is required!"

    "???" "I am Majna Eden Bat Azuma Nula Sedun"

    e "But you can just call me Eve~"

    p "Huh???? Wait, there are so many things I want to point out...but first...how did that become Eve??!!"

    play sound staffsummon

    "Without answering, Eve suddenly manifested a staff out of nowhere and into her hand."

    show hitona2 idle

    play sound magiccasting

    p "By the blessing of the wind, cleanse this girl from the curse!"

    "When she said that, my body lit up for a moment, then returned to normal."

    show hitona2 angry

    e "I see, I see, so your name is Hitona Kohigashi, and you were summoned here by...hmm how do I say this name...List...Lizen...uh...ahh, geez I can’t read this! But I should say my thanks to them later..."

    p "What in the world are you talking about..."

    show hitona2 smile1

    e "Well, don’t fuss over the small things! Welcome to the Kingdom of Soso!"

    e "Also known as the kingdom of magic!"

    p "Magic?"

    e "This Kingdom is renowned for its usage of magic!"

    show hitona2 angry

    e "However, because the current king, King Achnost, is monopolizing the usage of magic, the use of magic has been suppressed."

    show hitona2 surprised

    e "King Achnost is the worst! He is taxing his people way too much just for his own benefit!"

    p "Is that...so..."

    show hitona2 angry

    e "Because of that, rebels popped out one by one and banded together to take down the king."

    e "But, since the king monopolizes magic, the defenseless rebels were easily suppressed."

    p "Haaa..."

    show hitona2 laugh

    e "However! This Eve here has decided to take down the king!"

    p "Huh??"

    show hitona2 angry

    e "King Achnost only orders people around and lazes around!"

    show hitona2 smug

    e "I want to be a NEET King like him!"

    "{i}Wow...{/i}"

    play sound footstepforest

    "{i}Now that think about it...there was someone running in this direction earlier wasn’t there...{/i}"

    "{i}Ah, here they are.{/i}"

    show soldier with dissolve
    show hitona2 angry

    so "You over there! Halt!"

    "{i}We weren’t even moving at all though...{/i}"

    e "Geeeh, it’s a soldier..."

    e "Well, it’s no good having Hitona go deeper into the forest, so I guess we just have to stop him here!"

    p "W...What!?"

    play sound staffsummon

    e "Here, a staff! It has ’Wind Blast’ spell stored inside!"

    p "Wai...huuhhh?!?!"

    e "I’ll properly explain after this so help me out!"

    hide hitona2 with dissolve
    hide soldier with dissolve

    stop music fadeout 1.0

    """
    A fight is about to start!

    You can use spells or items to attack and heal!

    If you use an attacking spell, you can double your damage by winning rock paper scissors!

    But, if you lose, your damage will be halved instead, so be careful!

    The fastest way to learn is to just try it, so let’s go!
    """

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

    jump r2_fight

label r2_start_after_battle:
    scene bg forest with dissolve

    hide screen multi_stat
    hide screen multi_sprite
    play music forest fadein 1.0

    show hitona2 smug with dissolve

    e "That was easy~"

    p "What part of that was easy...it took my everything just to cast a spell..."

    p "Wait no, to begin with, I shouldn’t even be able to use magic right?"

    p "{i}Feels like I’ve only been getting more and more confused ever since I got here...{/i}"

    p "{i}That fight was so exhausting too...{/i}"

    show hitona2 idle

    e "Well anyone can use magic if they have a spell orb."

    p "Spell orb?"

    e "Yup, it’s an orb that stores magic."

    e "Like the orb in that staff you used, by using your own energy to activate it, the magic spell stored in the orb can be used."

    p "So anyways, why did that soldier attack us again?"

    e "Ah."

    show hitona2 laugh

    e "It’s probably because I’m on the wanted list."

    p "Because you were rebelling against the king?"

    show hitona2 idle

    e "Well there’s also that of course."

    e "But it’s probably because I’ve been collecting and stealing spell orbs from all around?"

    p "Ehhhh?"

    e "Well I mentioned it earlier right? About how the king is monopolizing magic and all."

    show hitona2 smile1

    e "So here I am being a wanted person~"

    e "Well either way, come with me Hitona!"

    p "Ehh, why?"

    show hitona2 idle

    e "You don’t have anywhere to go anyways, right?"

    "I looked around my room...but I’m no longer in my room."

    p "Fine then..."

    show hitona2 smile2

    e "Let’s go then~"

    stop music fadeout 1.0

    "Things may change if you visit the same place a second time. Be sure to check them all!"

    play music adventure_bgm fadein 1.0

    jump r2_forest
