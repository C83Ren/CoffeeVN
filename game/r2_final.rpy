label r2_final:
    scene black

    e "Hey Hitona!"

    e "Oiii Hitona!"

    p "Huh?"

    scene bg castle room

    p "Why are we here…"

    e "It’s not the time to ponder around!"

    e "It’s time to become the king!"

    p "Eh what happened?!"

    e "You already gathered every ultimate spell!"

    e "Tranquility, Turmoil, and Rage"

    p "WHAT? BUT!"

    e "And I have my Void but…we’ll see"

    k "So you came here huh…"

    "The king in front of us…King Achnost…"

    "Is just lying down lazily"

    "He stand up facing us"

    k "Rebels must be purged~"

    "Fight until half HP"

    k "Annoying little pest"

    k "Bend to my will~ Absolute~"

    e "Huh?"

    p "Eh? We can’t cast magic??"

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

    e "I see…"

    e "Then let’s try our best"

    "The king unleashed its attack and Eve managed to dispel it using her barrier spell"

    "But…"

    k "Wahahahaha there’s more to that!"

    "The king casted the same spell…"

    "And that was it…"

    "Bad End"

    return

label final_grand_spell:
    p "Okay…Let’s use it! The Grand Spell!"

    e "Okay!"

    e "Before that, did you take the catalyst from before??"

    menu:
        "Did I take the catalyst???"
        "Yeah I did!":
            $ catalyst = True
        "No I don't think so":
            $ catalyst = False

    e "Okay Let’s do it!"

    "The king unleashed its attack and Eve managed to dispel it using her barrier spell"

    "But…"

    k "Wahahahaha there’s more to that!"

    "The king casted the same spell…"

    scene bg grand spell

    p "Tranquility, Turmoil, Rage, I, Hitona, rule over the composition of emotion. Compile everything to one"

    e "I, Majna Eden Bat Azuma Nula Sedun, ruler of the Void. Give the emotion infinite space to burst"

    p "Apeiros Iris!"

    # Hitona and Eve supposed to be saying it together

    "We casted the Grand Spell, a rainbow magical ball from me and pitch black magical ball from Eve combined together"

    "The outcome was obvious…"

    "The king was no more"

    if catalyst:
        jump final_good_end
    else:
        jump final_bad_end

label final_bad_end:
    "But…Eve was just there…lying down on the floor"

    p "I knew this would happen…I’m sorry Eve…"

    p "If only there was some other way…"

    "The king is gone, but…his replacement is gone as well…"

    "Bad End"

    return

label final_good_end:
    "I looked at Eve…"

    p "Eh?"

    e "Eh?"

    p "You’re alive!"

    e "Yeah…somehow…"

    e "Ah probably because of the catalyst"

    p "Whatever it is, you’re alive!!!"

    "I hugged Eve tightly"

    e "Haha…yeah…"

    "We both fell on our knees"

    "The exhaustion just sank in…"

    p "Hahahahahaha…Haaaa…"

    # Hitona and Eve supposed to be saying it together

    e "Thank you Hitona…truly…"

    p "Hey…I had a lot of fun as well"

    e "And don’t worry about this, I’ll be a good NEET King Okay~"

    p "Hahaha yeah…ugh…"

    "I feel very dizzy…and everything went black…"

    scene bg room

    p "Huh? Where am I…"

    "I’m on my bed…"

    p "What a dream that was…"

    "Ring ring"

    p "A message?"

    "“Surely you got back safely right?”"

    "\"Wahahahaha you should trust The Great Majna Eden Bat Azuma Nula Sedun more\""

    "\"This NEET King will make the Kingdom prosper again okay~\""

    "\"Until next time!\""

    p "Hahahahahaha"

    p "If you’re a king you’re not a NEET anymore Eve!"

    "Good End"

    "On the ground there was something..."

    p "Huh? What’s This?"

    p "A key?"

    p "And also a note with the number 1?"

    return
