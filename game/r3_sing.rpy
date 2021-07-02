label r3_sing:
    scene bg computer with fade

    show lios front at lios_right with dissolve
    show hitona3 happy hat at hitona_left with dissolve

    pi "Aaah sure brings back memories"

    l "Amazes me you still remember those drawings Pierrot"

    pi "It reminds me when Hitona was playing *** and she drew ***"

    p "Yeah you’re right!"

    "?"

    "What was I saying?? What game? What drawing?"

    show hitona3 worried hat

    l "She still looks confused Pierrot"

    pi "Sigh"

    l "You underestimate this domain effect Pierrot. But those who finishes it surely will be compensated equally"

    show hitona3 angry hat

    pi "Even when you’re the one who stole it you dare say that…"

    l "Hey don’t blame me, you’re the one who triggered it"

    l "Well go on to the last challenge"

    p "You said last????"

    l "Yeah I did"

    p "I can’t believe it…"

    show hitona3 surprised1 hat

    pi "Which is why we should hurry!"

    scene bg hub with Fade(1.0, 1.0, 1.0)

    "Pierrot pulled my hands and we walked around the hub finding the challenge"

    "Which will probably just gonna drop out of nowhere again"

    p "What were you talking with Lios Pierrot?"

    show hitona3 idle hat with dissolve

    pi "About what?"

    p "About the domain effect and what not"

    pi "Hmmm I guess it’s fine to tell it now since it is the last challenge"

    pi "Basically Lios domain has the effect to amplify human’s forgetfulness"

    p "Huh??"

    pi "The effect is really strong just so you know"

    pi "You can forget really obvious things"

    p "Is that so…"

    "As I was still trying to understand what Pierrot was saying the scene suddenly changed again"

    scene bg sing with Fade(1.0, 1.0, 1.0)

    stop music fadeout 1.0

    p "It’s a…stage?"

    show hitona3 idle hat

    pi "Yeah…"

    hide hitona3
    show lios front with dissolve

    l "The last challenge!"

    l "Go to the stage little one~"

    "I went up to the stage with the mic"

    p "So you want me to…sing?"

    l "Not quite~"

    l "You have to guess the next line from the songs~"

    hide lios
    show hitona3 smug hat

    pi "This should be easy~"
    hide hitona3 with dissolve

    play sound quizstart
    "LET'S START"

    check_lyrics l "audio/Hana_ni_Bourei.mp3" "Type in the lyrics afterwards, no space needed" sing_retry "あせをぬぐってなつめく" "aseonuguttenatsumeku"
    play sound correctchoice
    pi "Correct! Next!"
    check_lyrics l "audio/mousouzei.mp3" "Type in the lyrics afterwards, no space needed" sing_retry "でかいけつさせましょう" "dekaiketsusasemashou"
    play sound correctchoice
    pi "Correct! Next!"
    check_lyrics l "audio/cherry.mp3" "Type in the lyrics afterwards, no space needed" sing_retry "ゆびさきでおくるきみへのめっせじ" "yubisakideokurukimienomesseji"
    play sound correctchoice
    pi "Correct! Next!"
    check_lyrics l "audio/jikoshoukai.mp3" "Type in the lyrics afterwards, no space needed" sing_retry "きょうのためいっしょけんめいがんばった" "kyounotameisshokenmeiganbatta"
    play sound correctchoice
    pi "Correct! Next!"
    check_lyrics l "audio/SAKURA.mp3" "Type in the lyrics afterwards, no space needed" sing_retry "いまはるにつつまれていくよ" "imaharunitsutsumareteikuyo"
    play sound correctchoice
    pi "Correct! Next!"
    check_lyrics l "audio/Kokoronashi.mp3" "Type in the lyrics afterwards, no space needed" sing_retry "でもぼくはそんざいしないからじゃあせめてここにきてよ" "demobokuwasonzaishinaikarajaasemetekokonikiteyo"
    play sound correctchoice

    jump r3_end

label sing_retry:
    scene bg sing

    show lios front at lios_right
    show hitona3 sad hat at hitona_left

    pi "Lios…come on Lios…"

    l "Who said it was easy?"

    pi "I’m sorry!"

    l "Fine, you can try again if you want. I am nice today"

    show hitona3 surprised1 hat

    pi "THANK YOU!"

    pi "Let’s try again Hitona!"

    menu:
        "What should I do?"
        "Try Again":
            return ""
        "Give up":
            return "sing_fail"

label sing_fail:
    scene black with fade

    "Let's try again okay"

    return
