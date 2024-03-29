label r1_park_end:
label end_1:
    # "park end"
    scene bg park with Fade(0.5, 0.5, 0.5)

    "We walked for quite a while, and finally arrived at the park."

    # bgm 泣いて泣いて泣き止んだら
    play music r1end_bgm fadein 1.0

    show hitona1 smile1 with dissolve

    "Shiraishi pointed at the swings, and I understood."

    "She hopped on the swings, and I pushed it from behind."

    show hitona1 smile2

    s "Today was fun, [player_name] onee-chan!" id end_1_6b4f7a76

    p "Yeah, it really was!"

    "It was different from my original plan, but it certainly was a fun day."

    s "We went to the game center and played the crane game!"

    p "Yeah, we even got a prize at our second try! I was so surprised!"

    if _in_replay or combiniflag == 1 and movieflag == 1:

        show hitona1 happy2
        s "And then after that, we went to get food at the best place ever!"

        p "Ooooh you understand!"

        show hitona1 happy1

        s "Shiraishi got to eat [player_name] onee-chan’s recommendation!" id end_1_7dcd5bba

        p "Hehehe, now can I get a sponsor from them?"

        show hitona1 idle2

        s "Sponsor?"

        p "Ah, nevermind."

        show hitona1 happy2

        s "We then went to the movies!"

        p "Food before the movie, I’m surprised we didn’t fall asleep while watching it."

        show hitona1 smile2

        s "The movie was too interesting for Shiraishi to sleep!"

        p "I guess so, yeah."

    elif combiniflag == 1:

        show hitona1 happy2

        s "And then after that, we went to get food at the best place ever!"

        p "Ooooh you understand!"

        show hitona1 happy1

        s "Shiraishi got to eat [player_name] onee-chan’s recommendation!" id end_1_7dcd5bba_1

        p "Hehehe, now can I get a sponsor from them?"

        show hitona1 idle2

        s "Sponsor?"

        p "Ah, nevermind."

        show hitona1 bliss4

        if shoppingflag == "suit":

            s "What’s more, Shiraishi even got to see [player_name] onee-chan in such a cool suit!" id end_1_de4f0b86
        else:

            s "What’s more, Shiraishi even got to see [player_name] onee-chan in such a beautiful dress!" id end_1_1c2a8e3d

        p "Shiraishi was really cute in that witch outfit too!"

    elif famresflag == 1 and movieflag == 1:

        show hitona1 happy2

        s "And then after that, we went to the family restaurant!"

        p "You ordered way too many things..."

        show hitona1 bliss1

        s "Hehehe it was tasty!"

        p "Food before the movie, I’m surprised we didn’t fall asleep while watching it."

        show hitona1 smile2

        s "The movie was too interesting for Shiraishi to sleep!"

        p "I guess so, yeah."

    elif famresflag == 1:

        show hitona1 happy2

        s "After that we went to the family restaurant!"

        p "And you ordered so many things..."

        s "Hehehe it was tasty!"

        show hitona1 bliss1

        p "Well, I guess we burned quite some calories walking in the shopping district."

        show hitona1 bliss4

        if shoppingflag == "suit":

            s "What’s more, Shiraishi even got to see [player_name] onee-chan in such a cool suit!" id end_1_de4f0b86_1
        else:

            s "What’s more, Shiraishi even got to see [player_name] onee-chan in such a beautiful dress!" id end_1_1c2a8e3d_1

        p "Shiraishi was really cute in that witch outfit too!"

    hide hitona1

    "As the sun set, Shiraishi jumped up from the swings."

    show hitona1 smile2

    s "Hey, [player_name] onee-chan, thank you for today." id end_1_70904dbc

    s "I really had a lot of fun!"

    "Shiraishi smiled at me while saying that."

    p "Eh? Shiraishi, you look a little pale...?"

    if (not _in_replay) and purikuri_flag:

        "Something is starting to heat up inside my pocket."

        "I pulled it out. It was the photo we took."

        hide hitona1

        call show_cg("anniv", False) from _call_show_cg_33
        $ persistent.room = 'room 2'

        p "Huh...? Where is Shiraishi?"

        "The photo was just me and...a congratulatory message."

        p "I don’t remember us writing this message...?"

        "I look back up towards Shiraishi, but..."

        scene bg park

        "...she wasn’t there."

    else:

        s "Hehehe, it’s okay, [player_name] onee-chan." id end_1_b8559320

        p "We should go back soon."

        show hitona1 blur1 with dissolve

        "As I said that, my vision started to get blurry."

        "Rather, I can’t really make out Shiraishi’s figure."

        show hitona1 blur2 with dissolve

        "The blurriness got worse and worse, and I can’t see Shiraishi anymore."

        show hitona1 blur3 with dissolve

        p "Shiraishi?"

        hide hitona1 with dissolve

        #back to normal

        "My vision returned to normal, but Shiraishi was no longer there."

        "I looked around frantically, but she was nowhere to be found. In her place appeared messages dancing lightly through the air."

    if (_in_replay and persistent.cg_unlocked_9) or (not _in_replay and regret_choice == "Yeah, I regret something"):
        window hide
        call show_cg("regret1", False) from _call_show_cg_34
        call show_cg("regret2", False) from _call_show_cg_35
        call show_cg("regret3", False) from _call_show_cg_36
        call show_cg("regret4", False) from _call_show_cg_37
    else:
        window hide
        call show_cg("noregret1", False) from _call_show_cg_38
        call show_cg("noregret2", False) from _call_show_cg_39
        call show_cg("noregret3", False) from _call_show_cg_40
        call show_cg("noregret4", False) from _call_show_cg_41

    window hide
    $ _skipping = False
    if _preferences.language == 'simplified_chinese':
        show image 'images/r1_end_c.png' with dissolve
    else:
        show image 'images/r1_end.png' with dissolve
    if (not persistent.ed_unlocked_1) and persistent.ed_unlocked_3 and persistent.ed_unlocked_2:
        $ renpy.notify(__("A new route has been unlocked!"))
    $ persistent.ed_unlocked_1 = True
    $ renpy.pause(1.0, hard=True)
    pause
    $ _skipping = True

    scene bg park with fade

    p "{i}What’s this on the ground? A key?{/i}" id end_1_2071b73a

    p "{i}And also a note with “0” written on it...?{/i}" id end_1_1abb9b93

    return
