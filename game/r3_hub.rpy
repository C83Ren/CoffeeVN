label r3_hub:
    scene bg room

    stop music

    "{b}“Correct Passcode.”{/b}"

    p "Oh, that was the correct one."

    show hitona3 smile hat

    "The girl standing next to me grabbed my arm."

    "???" "Let’s go!"

    p "What? Where..."

    scene black with fade

    "Before I could finish my words, I lost consciousness."

    "???" "Ooooi, [player_last_name]!" id r3_hub_1abc0be7

    "???" "Ooooi, wake up already!"

    p "Huh? Where... am I..."

    scene bg hub with Fade(1.0, 1.0, 2.0)
    play music lios_bgm fadein 3.0 fadeout 3.0

    "I woke up in an enclosed room."

    "It was a really huge room full of...something."

    "It’s difficult to describe it in words."

    show hitona3 smile hat with dissolve

    "???" "This is a virtual world."

    p "Virtual world?"

    "???" "Yeah, you could call it the space inside the computer. This is Lios’ domain."

    "???" "He steals various things and brings them here."

    p "...I...see..."

    show hitona3 laugh hat

    "???" "Oh right, sorry, I haven’t introduced myself. I’m Pierrot! No, not Poirot but Pierrot! The Master Detective Pierrot!"

    p "Okay...uhh...I’m [player_name], [player_full_name]." id r3_hub_7e235c7e

    p "But...you somehow knew that, it seems."

    pi "Don’t mind the small details! Welcome to Lios’ Domain! "

    show hitona3 idle hat

    p "Why did we come here again?"

    pi "You want to get back the thing Lios stole from you, right?"

    p "What? Ahhh..."

    p "In the first place, I don’t even know what he stole though..."

    show hitona3 smug hat

    pi "Well, let’s take it back anyways!"

    "???" "You’ve come back again..."

    p "Eh? Did you say something, Pierrot?"

    show hitona3 idle hat

    pi "That’s Lios’ voice."

    l "Make my job easier, won’t you Pierrot..."

    "Pierrot just shrugged"

    l "Well, whatever. Welcome to my domain, the place where you can find things I stole!"

    p "What did you steal from me anyways?"

    l "I’m not telling you that."

    l "That’s for you to find out."

    show hitona3 laugh hat

    pi "Let’s go, [player_last_name], let’s go!" id r3_hub_bb65e94c

    "This is all so confusing but...it seems a bit fun, so might as well follow along."

    hide hitona3 with dissolve

    p "{i}Wait...wasn’t there something I was supposed to do...? Oh well...{/i}"

    "We walked through the area looking around."

    l "So, Pierrot, are you prepared to fail again?"

    show hitona3 smug hat

    pi "Wahahahaha! Lios, underestimating me now is the worst mistake you can possibly make!"

    pi "I have grown, this time for sure [player_last_name] will get back what you have stolen!" id r3_hub_f2051d80

    hide hitona3

    p "Uhhh...so, where exactly do we find these things that were stolen...?"

    l "This is my domain, little one."

    l "While I could return it right away, that’s boring!"

    l "Complete all my challenges and I’ll return it..."

    l "However! If you fail even one..."

    l "I’ll ban you from my domain!"

    p "This is getting to be more and more tedious..."

    show hitona3 smug hat

    pi "Don’t worry, [player_last_name]! The great detective Pierrot is here by your side!" id r3_hub_f3845a1d

    play sound lightswitch

    scene black

    $ renpy.pause(1.0)

    "The room suddenly darkened."

    p "Eh?!"

    jump r3_quiz
