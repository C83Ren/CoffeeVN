label r3_sing:
    $ save_enabled = True

    scene bg quiz

    show lios front at lios_right with dissolve

    "Someone with a black cape suddenly appeared in front of us."

    "It was Lios."

    l "You got them all right, huh. That’s unexpected."

    show hitona3 laugh hat at hitona_left with dissolve
    # show lios front at lios_right behind hitona3

    pi "Like I said, don’t underestimate the Great Detective Pierrot"

    show hitona3 smug hat

    pi "Such a quiz like that is no big deal!"

    p "But I was the one answering..."

    l "Pierrot don’t get too cocky."

    l "You’ve been doing this for quite a while now, you could even say you’re quite slow."

    show hitona3 angry hat

    pi "How dare you! You always change the question!"

    "Even though they’re arguing, it seems like they are actually quite close."

    l "Well, no matter, it’s not like you will manage to clear the next one anyways."

    "We walked for a bit, then somehow ended up back in the previous room."

    scene bg sing with Fade(1.0, 1.0, 1.0)

    stop music fadeout 1.0

    p "It’s a... stage?"

    show hitona3 idle hat

    pi "Yeah..."

    hide hitona3
    show lios front with dissolve

    l "Go to the stage!"

    "Grabbing the microphone, I went up to the stage."

    p "So you want me to...sing?"

    l "Not quite~"

    l "You have to sing the next line when the song stops!"

    hide lios
    show hitona3 smug hat

    pi "This should be easy~"
    hide hitona3 with dissolve

    $ save_enabled = False

    play sound quizstart
    "{b}LET'S START{/b}"

    check_lyrics l "audio/Hana_ni_Bourei.mp3" "Type in the lyrics that come next." sing_retry "あせをぬぐってなつめく" "aseonuguttenatsumeku" "俺不知道"
    play sound correctchoice
    "{b}CORRECT{/b}"
    pi "What a fitting song...this was on purpose wasn’t it?"
    l "I have no idea what you’re talking about."
    "{b}NEXT{/b}"

    check_lyrics l "audio/mousouzei.mp3" "Type in the lyrics that come next." sing_retry "でかいけつさせましょう" "dekaiketsusasemashou" "俺不知道"
    play sound correctchoice
    "{b}CORRECT{/b}"
    pi "I never really understood this song."
    l "Just shows how young you are."
    "{b}NEXT{/b}"

    check_lyrics l "audio/cherry.mp3" "Type in the lyrics that come next." sing_retry "ゆびさきでおくるきみへのめっせーじ" "yubisakideokurukimienomesseeji" "yubisakideokurukimienomesse-ji" "俺不知道"
    play sound correctchoice
    "{b}CORRECT{/b}"
    pi "Lios don’t be such a tsundere, if you like Kohigashi, just say so."
    l "You’re definitely tired. aren’t you..."
    "{b}NEXT{/b}"

    check_lyrics l "audio/jikoshoukai.mp3" "Type in the lyrics that come next." sing_retry "きょうのためいっしょけんめいがんばった" "kyounotameisshokenmeiganbatta" "きょうのためいっしょうけんめいがんばった" "kyounotameisshoukenmeiganbatta" "俺不知道"
    play sound correctchoice
    "{b}CORRECT{/b}"
    pi "Pierrot also did her best!"
    l "Did your best to make things harder~"
    "{b}NEXT{/b}"

    check_lyrics l "audio/futariboshi.mp3" "Type in the lyrics that come next." sing_retry "ぼくのなまえ" "bokunonamae" "俺不知道"
    play sound correctchoice
    "{b}CORRECT{/b}" id r3_sing_a403d1d8
    pi "What was this song's name again?" id r3_sing_fb37f0d8
    l "Pretty sure it's Hitoriboshi...but now that you ask, I'm not so sure anymore." id r3_sing_4aa33a81
    "{b}NEXT{/b}" id r3_sing_4454a96a

    check_lyrics l "audio/SAKURA.mp3" "Type in the lyrics that come next." sing_retry "いまはるにつつまれていくよ" "imawarunitsutsumareteikuyo" "俺不知道"
    play sound correctchoice
    "{b}CORRECT{/b}"
    pi "Spring is such a bittersweet season."
    l "You’re right, just like right now, when it all ends, you can only reminisce."
    "{b}NEXT{/b}"

    check_lyrics l "audio/Kokoronashi.mp3" "Type in the lyrics that come next." sing_retry "でもぼくにはそんざいしないからじゃあせめてここにきてよ" "demobokuniwasonzaishinaikarajaasemetekokonikiteyo" "俺不知道"
    play sound correctchoice
    "{b}CORRECT{/b}"
    pi "Listening to this always makes me shiver, don’t you Lios?"
    l "After repeating this whole thing for thousand times, I feel numb, and not about the song."

    jump r3_river

label sing_retry(hint=False):
    scene bg sing

    play sound falsechoice_short

    show lios front at lios_right
    show hitona3 sad hat at hitona_left

    pi "Lios...please...Lios..."

    l "Who was the one who said it’d be easy?"

    pi "I’m sorry!"

    l "Fine, you can try again if you want."

    l "I feel nice today."

    show hitona3 surprised1 hat

    pi "THANK YOU!"

    pi "Let’s try again!"

    if hint:
        pi "You were so close last time! Just sing a little more!"

    menu:
        "What should I do?"
        "Try again":
            hide hitona3
            hide lios
            return ""
        "Give up":
            hide hitona3
            hide lios
            return "sing_fail"

label sing_fail:

    $ save_enabled = True

    stop music fadeout 1.0

    scene bg room with Fade(1.0, 1.0, 1.0)

    play music room_bgm fadein 3.0

    p "{i}Eh? I’m in...my room? On my bed...{/i}"

    p "{i}Even if that was a dream, I wonder what was stolen...{/i}"

    "I looked up at my phone screen."

    p "..."

    p "AAAAAAA I’M SO SORRY SENPAI!"

    "I rushed out of my room in a hurry to meet senpai."

    scene black with dissolve

    "While running towards the park, that dream? kept spinning in my mind."

    "It seems like the meaning of that dream? will stay unknown forever."

    "I guess dreams will just be dreams."

    jump bad_end
