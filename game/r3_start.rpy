label r3_start_init():
    $ passcode_r3 = '0000'
    return

label r3_start:
    scene bg room with fade

    "???" "Haa...haa..."

    "Someone is standing in front of my door."

    p "{i}What kind of costume is that...?{/i}"

    p "{i}Ah yeah, it’s a detective costume.{/i}"

    p "Uhhh, are you okay?"

    show hitona3 sad hat with dissolve

    "???" "Uh yeah...I’m okay..."

    "???" "...wait, that’s not the problem!"

    p "Eh??"

    "The suspicious person wearing a detective costume looked carefully at me."

    p "Huh? Can I help you?"

    "???" "Kohigashi! Phantom Thief Lios has stolen something from you!"

    p "Ehhhhh?"

    p "When??"

    p "What do you mean???"

    "There are so many questions I want to ask right now."

    "???" "Lios has stolen something that’s very important to you!"

    p "Seriously, what are you taking about???"

    p "In the first place, who are you even???"

    "Completely ignoring what I said, she instead took out and showed me a card."

    hide hitona3

    play sound takecard

    nvl_narrator "“Hitona Kohigashi!”"

    nvl_narrator "“I, Phantom Thief Lios, have stolen one of your most precious possessions!”"

    nvl_narrator "“If you wish to take it back, type in the month and day when the mermaid princess has her yearly celebration!”"

    nvl clear

    play sound takecard

    p "What’s all this about?"

    show hitona3 idle hat

    "???" "Look at your computer!"

    "I looked at my computer, and on the screen, it prompted me to enter a 4 digit passcode."

    "{i}Is this what the card was talking about?{/i}"

    p "Is this some sort of prank?"

    "???" "I assure you it’s not! Really!"

    p "Haa..."

    p "{i}Well, I guess there’s nothing wrong with going along with this for now.{/i}"

label room_passcode1:
    python:
        passcode_r3 = renpy.input(__("Please type in the passcode."), length=4, allow="0123456789")

    if passcode_r3 == "0504":
        play sound correctchoice
        jump r3_hub
    else:
        play sound falsechoice_short
        jump room_tryagain

label room_tryagain:
    "{b}“Wrong Passcode.”{/b}"

    "{i}Huh? I guess that was wrong...{/i}"

    show hitona3 smile hat

    "???" "You can always try again!"

    menu:
        "Try to enter the password again?"
        "Try again":
            jump room_passcode1
        "Give up":
            jump room_giveup1

label room_giveup1:
    p "Nope, I’m good."

    show hitona3 sad hat

    "???" "Ehhhhh? Don’t be like that!"

    "???" "A hint! If you continue I’ll give you a hint!"

    menu:
        "This girl is practically on her knees begging."
        "Try again":
            jump room_passcode2
        "Give up":
            jump room_passcode_badend

label room_passcode2:
    p "Okay fine! Geez, I’ll try again! Give me the hint then."

    show hitona3 smug hat

    "???" "The hint is {b}“the birthday of the mermaid princess”{/b}."

    p "{i}If you know it, why don’t you just enter it yourself.{/i}"

    python:
        passcode_r3 = renpy.input(__("Please type in the passcode."), length=4, allow="0123456789")

    if passcode_r3 == "0504":
        play sound correctchoice
        jump r3_hub
    else:
        play sound falsechoice_short
        jump room_tryagain

label room_passcode_badend:
    p "Ah I’m done with this"

    show hitona3 pout hat

    "???" "Ehhhh, wait!"

    p "Nope, I’m officially done with this."

    "???" "Fine, okay, let’s meet later."

    show hitona3 angry hat

    "???" "I’ll keep coming back until you want to do it again!"

    "???" "Bye for now then."

    p "No, please don’t come back again..."

    hide hitona3

    "The suspicious person left the building."

    p "{i}I really hope she’s not serious...maybe I should move again...{/i}"

    p "{i}Ah, geez, she didn’t even close the door...{/i}"

    p "{i}...AAAAAAAA!!!{/i}"

    p "{i}THIS IS BAD!!!{/i}"

    p "{i}I FORGOT!!!{/i}"

    p "{i}SENPAI IS WAITING FOR ME RIGHT NOW!!!{/i}"

    "I rushed out of my room in a hurry to meet senpai."

    scene black

    "While running towards the park, the words of that strange girl kept ringing in my head."

    "What in the world was that all about? What could possibly have been stolen?"

    "It’s already too late to regret it. I guess I will never be able to understand what she was talking about."

    jump bad_end
