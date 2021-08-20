label r2_final_init():
    $ catalyst = False
    return

label r2_final:
    scene black with dissolve

    e "[player_name]!" id r2_final_7f21cf64

    e "Hey, [player_name]!" id r2_final_a5f5e9ba

    p "Huh?"

    scene bg castle room with Fade(1.0, 1.0, 2.0)
    play music beforefinal_intro_bgm noloop fadein 2.0
    queue music beforefinal_loop_bgm

    p "Why are we here..."

    show hitona2 angry with dissolve

    e "It’s not the time to ponder around!"

    show hitona2 laugh

    e "It’s time to become the king!"

    p "Eh? What happened?!"

    show hitona2 smug

    e "You already gathered every ultimate spell! Tranquility, Turmoil, and Rage!"

    p "WHAT? Wait, wait, wait!!"

    p "We were just in Tranquility! Like...5 seconds ago!"

    e "I see...must be a spell from a soldier in the courtyard earlier that’s making you so confused."

    e "Anyways! You already gathered all the spells we need to go against the King!"

    show hitona2 pout

    e "And I have my Void ready as well..."

    p "Huh...?"

    """
    At that moment, a great number of memories suddenly surfaced in my mind like a storm.

    Memories about how in that storm-filled Turmoil region, I obtained the Turmoil spell.

    Memories about how I sacrificed myself in the Rage region to obtain the Rage spell.

    Memories about Eve telling me about the ultimate spell she controls called Void.

    How she caused the death of a countless number of people in a catastrophic disaster the last time she used Void.

    How, in order to activate the Grand Spell, the three ultimate spells I gathered were insufficient by themselves, and Void must be used alongside.

    And finally, how, in order to cast Void even just one more time, a terrible price would be required from Eve.

    As these memories rushed in, someone began to talk.
    """

    show hitona2 angry

    k "So you finally came here, huh..."

    "The king in front of us...King Achnost..."

    "...is just lying down lazily"

    show king

    "In what seemed like a massive amount of effort, he stood up to face us."

    k "Rebels must be purged."

    hide hitona2
    hide king

    python:
        hitona_stats["hp"] = 250
        hitona_stats["hp_max"] = 250
        hitona_stats["spell"] = ["Wind Lance", "Fire Wall", "Lightning Strike"]
        hitona_stats["item"].append("Paralyzing Spark")
        hitona_stats["item"].append("Flamethrower")
        hitona_stats["item"].append("God Blessing")
        hitona_stats["item"].append("Heal Aura")
        eve_stats["hp"] = 200
        eve_stats["spell"] = ["Wind Lance", "Fire Wall", "Lightning Strike"]
        eve_stats["item"] = ["Heal Aura", "Flamethrower", "God Blessing"]
        fight_order = [hitona_stats, eve_stats, king_stats]
        fight_list = [eve_stats, king_stats]
        ally_list = [hitona_stats, eve_stats]
        enemy_list = [king_stats]
        fight_label = "r2_final_after_battle"
        x = 0

    play music king_intro_bgm noloop fadein 1.0
    queue music king_loop_bgm loop

    jump r2_fight

label r2_final_after_battle:

    hide screen multi_stat
    hide screen multi_sprite

    show hitona2 angry with dissolve
    show king

    k "Annoying little pest. Know that resistance is futile!"

    k "Bend to my will! Absolute Domain!"

    show hitona2 surprised

    e "Huh?"

    p "Eh? We can’t cast magic??"

    show hitona2 angry

    e "No! He’s taking our magic!"

    e "Look over there!"

    "In front of us there was a huge magic ball about to hit us."

    e "We won’t survive if we don’t do something about it!"

    p "Then..."

    e "Don’t worry I have one last barrier spell!"

    e "But after that..."

    e "While I block this one spell, decide if we should use the Grand Spell or not!"

    p "Eh?? But..."

    e "Quick!"

    menu:
        "Use the Grand Spell?!"
        "Use it!":
            jump final_grand_spell
        "Don’t use it!":
            jump final_no_grand_spell

label final_no_grand_spell:
    p "I won’t use it! I don’t want to use it!"

    e "If we die here, there’s no meaning to saving it!"

    p "Even then, I won’t use it! You would have to use Void right?"

    show hitona2 idle

    e "I see..."

    show hitona2 smile1

    e "Then, let’s try our best"

    window hide
    play sound absolutespell

    $ renpy.pause(2.0, hard=True)

    "Eve barely managed to block the magic ball with her last barrier spell."

    show hitona2 angry

    "I don’t want her to pay the price for using the Void, but..."

    k "Wahahahaha, there’s more where that came from!"

    "...the king casted the same spell again. To the two of us who no longer had any means of defense, the ball of magic wiped all traces of our existence from the world."

    jump bad_end

label final_grand_spell:
    p "...okay! Let’s use it! The Grand Spell!"

    show hitona2 smile1

    e "Okay!"

    show hitona2 idle

    menu:
        e "By the way, did you bring the catalyst from before??"
        "Yeah I did!":
            $ catalyst = True
            "Hearing my response, Eve looked relieved."
        "No I don’t think so":
            $ catalyst = False
            "Hearing my response, Eve looked resigned."

label end_2 hide:
    if _in_replay:
        scene bg castle room
        play music king_intro_bgm noloop fadein 1.0
        queue music king_loop_bgm loop
        show king

    show hitona2 idle

    e "Okay let’s do it!" id final_grand_spell_4470a325

    window hide
    play sound absolutespell

    $ renpy.pause(2.0, hard=True)

    "Eve barely managed to block the magic ball with her last barrier spell."

    k "Wahahahaha, there’s more where that came from!"

    "In response to the king casting the same spell again, we began to chant the Grand Spell!"

    call show_cg("grandspell", False) from _call_show_cg_32

    p "Tranquility, Turmoil, Rage! I, [player_name], the ruler of the composition of emotions, order you. Combine, and unleash your true power!" id final_grand_spell_3513c7b8

    e "I am Majna Eden Bat Azuma Nula Sedun, ruler of the Void! To allow the power of the emotions to be fully unleashed, use this life, expand the void, and create an infinite space!"

    "{color=[p.who_args[color]]}[p]{/color} & {color=[e.who_args[color]]}[e]{/color}" "Apeiros Iris!" id final_grand_spell_70ac1851

    play sound apeirosiris

    "As we cast the Grand Spell, a rainbow ball of magic from me and pitch black ball of magic from Eve combined together, and filled the castle with a blinding light."

    window hide
    scene bg castle room with Fade(0.5, 3.0, 0.5, color='#fff')

    "When the light faded away, King Achnost had already been sent away to the afterlife, but..."

    "Eve..."

    if _in_replay or catalyst:
        jump final_good_end
    else:
        jump final_bad_end

label final_bad_end:
    play music r2bad_bgm fadein 1.0

    "...was lying motionlessly on the ground."

    p "{i}I knew this would happen...{/i}"

    p "{i}Eve...I’m sorry.{/i}"

    p "{i}If only there was some other way...{/i}"

    "The king was successfully defeated, but the new king was no longer here to take his place."

    jump bad_end

label final_good_end:
    stop music fadeout 1.0

    p "Eh?"

    show hitona2 angry with dissolve

    e "Eh?"

    play music r2end_bgm fadein 2.0

    p "You’re alive!"

    show hitona2 surprised

    e "Yeah...somehow..."

    show hitona2 idle

    e "Ah, it’s probably because of the catalyst."

    p "Whatever it is, you’re alive!!! I’m just happy you’re alive!!"

    "I hugged Eve, who, even though she used Void, was still alive, tightly."

    show hitona2 smile2

    e "Haha...yeah..."

    "The feeling of exhaustion finally sunk in, and we both fell onto our knees."

    "{color=[p.who_args[color]]}[p]{/color} & {color=[e.who_args[color]]}[e]{/color}" "Hahahahahaha...Haaaa..." id final_good_end_f11e976f

    e "Thank you, [player_name]...truly..." id final_good_end_4081c499

    p "Hey...I had a lot of fun too"

    show hitona2 smug

    e "And don’t worry about this, I’ll be a good NEET King okay."

    p "Hahaha yeah...ugh..."

    "I suddenly felt very dizzy, and then everything went black..."

    scene bg room with Fade(1.0, 2.0, 1.0)

    p "{i}Huh? Where am I...{/i}"

    p "{i}On my bed...lying down...?{/i}"

    p "{i}What a dream that was...{/i}"

    play sound messagetone
    window hide
    $ renpy.pause(2.0, hard=True)

    p "{i}A text?{/i}"

    nvl_narrator "You got back safely right?"

    nvl_narrator "Wahahahaha! You should trust The Great Majna Eden Bat Azuma Nula Sedun more!"

    nvl_narrator "By the way, the wind says {b}‘it resembles thy name, but one digit differs’{/b}"

    nvl_narrator "Until next time!"

    p "{i}Hahahahahaha{/i}"

    p "{i}If you’re a king you’re not a NEET anymore, Eve!{/i}"

    window hide
    $ _skipping = False
    if _preferences.language == 'simplified_chinese':
        show image 'images/r2_end_c.png' with dissolve
    else:
        show image 'images/r2_end.png' with dissolve
    if (not persistent.ed_unlocked_2) and persistent.ed_unlocked_3 and persistent.ed_unlocked_1:
        $ renpy.notify(__("A new route has been unlocked!"))
    $ persistent.ed_unlocked_2 = True
    $ renpy.pause(1.0, hard=True)
    pause
    $ _skipping = True

    scene bg room with dissolve

    "On the ground there was something..."

    p "{i}Huh? What’s this...? a key{/i}"

    p "{i}And also a note with the number 7?{/i}"

    return
