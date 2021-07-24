label r2_final:
    scene black with dissolve

    e "Hey Hitona!"

    e "Oiii Hitona!"

    p "Huh?"

    scene bg castle room with Fade(1.0, 1.0, 2.0)
    play music beforefinal_intro_bgm noloop fadein 2.0 volume 0.5
    queue music beforefinal_loop_bgm volume 0.5

    p "Why are we here…"

    #angry3

    e "It’s not the time to ponder around!"

    #laugh2

    e "It’s time to become the king!"

    p "Eh what happened?!"

    #smug1

    e "You already gathered every ultimate spell!"

    e "Tranquility, Turmoil, and Rage"

    p "WHAT? BUT!"

    #pout2

    e "And I have my Void but…we’ll see"

    #angry3

    k "So you came here huh…"

    "The king in front of us…King Achnost…"

    "Is just lying down lazily"

    "He stand up facing us"

    k "Rebels must be purged~"

    python:
        hitona_stats["hp"] = 300
        hitona_stats["hp_max"] = 300
        hitona_stats["spell"] = ["Wind Lance", "Fire Wall", "Lightning Strike"]
        eve_stats["hp"] = 300
        eve_stats["spell"] = ["Wind Lance", "Fire Wall", "Lightning Strike"]
        eve_stats["item"] = ["Heal Aura", "Flamethrower", "God Blessing"]
        fight_order = [hitona_stats, eve_stats, king_stats]
        ally_list = [hitona_stats, eve_stats]
        enemy_list = [king_stats]
        fight_label = "r2_final_after_battle"
        x = 0

    "FIGHT!"

    play music king_intro_bgm noloop fadein 1.0 volume 0.3
    queue music king_loop_bgm loop volume 0.3

    jump r2_fight

label r2_final_after_battle:

    hide screen multi_stat

    k "Annoying little pest"

    k "Bend to my will~ Absolute~"

    #surprised1

    e "Huh?"

    p "Eh? We can’t cast magic??"

    #angry3

    e "No! He’s taking our magic to his own!"

    e "Look at that!"

    "In front of us there was this huge magic ball ready to be blasted at us"

    e "We won’t survive this one if we don’t have anything"

    p "Then…"

    e "Don’t worry I have one barrier spell that I can use once"

    e "But after that, there’s no more…"

    e "While I block this one spell, decide do we use the Grand Spell or not"

    p "Eh?? But…"

    e "Quick!"

    menu:
        "Do we use the Grand Spell?!"
        "Use it!":
            jump final_grand_spell
        "Don't use it!":
            jump final_no_grand_spell

label final_no_grand_spell:
    p "I won’t use it!"

    e "If we fail here, no one be able to stand up to him again!"

    p "But I still won’t use it, knowing that you need to use Void…"

    #idle

    e "I see…"

    #smile1

    e "Then let’s try our best"

    play sound absolutespell

    "The king unleashed its attack and Eve managed to dispel it using her barrier spell"

    #angry3

    "But…"

    k "Wahahahaha there’s more to that!"

    "The king casted the same spell…"

    "And that was it…"

    "Bad End"

    return

label final_grand_spell:
    p "Okay…Let’s use it! The Grand Spell!"

    #smile1

    e "Okay!"

    #idle

    e "Before that, did you take the catalyst from before??"

    menu:
        "Did I take the catalyst???"
        "Yeah I did!":
            $ catalyst = True
        "No I don't think so":
            $ catalyst = False

    #smile1

    e "Okay Let’s do it!"

    play sound absolutespell

    "The king unleashed its attack and Eve managed to dispel it using her barrier spell"

    "But…"

    k "Wahahahaha there’s more to that!"

    "The king casted the same spell…"

    scene cg 5 unscaled with dissolve

    p "Tranquility, Turmoil, Rage, I, Hitona, rule over the composition of emotion. Compile everything to one"

    e "I, Majna Eden Bat Azuma Nula Sedun, ruler of the Void. Give the emotion infinite space to burst"

    p "Apeiros Iris!"

    # Hitona and Eve supposed to be saying it together

    play sound apeirosiris

    "We casted the Grand Spell, a rainbow magical ball from me and pitch black magical ball from Eve combined together"

    "The outcome was obvious…"

    "The king was no more"

    if catalyst:
        jump final_good_end
    else:
        jump final_bad_end

label final_bad_end:
    scene black with dissolve
    play music r2bad_bgm fadein 1.0

    "But…Eve was just there…lying down on the floor"

    p "I knew this would happen…I’m sorry Eve…"

    p "If only there was some other way…"

    "The king is gone, but…his replacement is gone as well…"

    "Bad End"

    return

label final_good_end:
label end_2:
    $ persistent.ed_unlocked_2 = True

    scene bg castle room with dissolve

    "I looked at Eve…"

    p "Eh?"

    #angry3

    e "Eh?"

    play music r2end_bgm fadein 2.0

    p "You’re alive!"

    #surprised1

    e "Yeah…somehow…"

    #idle

    e "Ah probably because of the catalyst"

    p "Whatever it is, you’re alive!!!"

    "I hugged Eve tightly"

    #smile2

    e "Haha…yeah…"

    "We both fell on our knees"

    "The exhaustion just sank in…"

    p "Hahahahahaha…Haaaa…"

    # Hitona and Eve supposed to be saying it together

    e "Thank you Hitona…truly…"

    p "Hey…I had a lot of fun as well"

    #smug1

    e "And don’t worry about this, I’ll be a good NEET King Okay~"

    p "Hahaha yeah…ugh…"

    "I feel very dizzy…and everything went black…"

    scene bg room with Fade(1.0, 2.0, 1.0)

    p "Huh? Where am I…"

    "I’m on my bed…"

    p "What a dream that was…"

    play sound messagetone

    p "A message?"

    nvl_narrator "“Surely you got back safely right?"

    nvl_narrator "Wahahahaha you should trust The Great Majna Eden Bat Azuma Nula Sedun more"

    nvl_narrator "This NEET King will make the Kingdom prosper again okay~"

    nvl_narrator "Until next time!”"

    nvl clear

    p "Hahahahahaha"

    p "If you’re a king you’re not a NEET anymore Eve!"

    "Good End"

    "On the ground there was something..."

    p "Huh? What’s This?"

    p "A key?"

    p "And also a note with the number 1?"

    return
