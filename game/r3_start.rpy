label r3_start:
    scene bg room with fade

    "??" "Pant pant"

    "Someone’s is in front of my door…"

    "What kind of costume is that…Ah yeah it’s a detective costume"

    p "Uuuh are you okay?"

    show hitona3 sad hat with dissolve

    "??" "Uh yeah…I’m okay…"

    "??" "NO!"

    p "Eh??"

    "She looked up at me…"

    p "Huh?? Me???"

    "??" "Kohigashi! Phantom Thief Lios has stolen something from you!"

    p "Eeeeeh?"

    p "What???"

    p "Why do you…?"

    "I have so many questions right now…"

    "??" "Lios has stolen something very important from you!"

    p "Seriously what are you taking about???"

    p "And who are you???"

    "Not minding what I said she showed me a card"

    hide hitona3

    play sound takecard

    "\"Kohigashi Hitona, I, Phantom Thief Lios has stolen one of your most precious possession. If you want to get it back enter the date when the mermaid princess has her yearly celebration\""

    p "What’s this about?"

    show hitona3 idle hat

    "??" "Look at your computer!"

    "I looked at my computer and on the screen it prompted me to enter a 4 digit passcode of some sort"

    "Is this what the card was talking about? I have no idea"

    p "Is this some kind of prank?"

    "??" "I assure you it’s not!"

    p "Sigh"

    "I guess there’s nothing wrong with going along with this. I wonder what the passcode is~"

label room_passcode1:
    menu:
        "Okay let’s put in the code"
        "0504":
            play sound correctchoice
            jump r3_hub
        "Other than that":
            play sound falsechoice_short
            jump room_tryagain

label room_tryagain:
    "\"WRONG PASS\""

    p "Huh? I guess that was wrong"

    show hitona3 smile hat

    "??" "You can always try again"

    menu:
        "Try again?"
        "Yes":
            jump room_passcode1
        "No":
            jump room_giveup1

label room_giveup1:
    p "Nope I’m good~"

    show hitona3 sad hat

    "??" "Eeeeeh? Don’t be like that!"

    "??" "I’ll give you a hint! If you continue I’ll give you a hint!"

    menu:
        "This girl is practically begging, what should I do?"
        "Try Again!":
            jump room_passcode2
        "Give up":
            jump room_passcode_badend

label room_passcode2:
    p "Okay fine give me a hint then"

    show hitona3 smug hat

    "??" "The hint is the birthday of the mermaid princess"

    "Makes me wonder why she isn’t the one entering this passcode…"

    menu:
        "Okay let’s put in the passcode"
        "0504":
            play sound correctchoice
            jump r3_hub
        "Other than that":
            play sound falsechoice_short
            jump room_tryagain

label room_passcode_badend:
    p "Ah I’m done with this"

    show hitona3 pout hat

    "??" "Eeeeh come on!"

    p "Nope, I’m officially done with this~"

    "??" "Fine I’ll come back again later!"

    show hitona3 angry hat

    "??" "I’ll come back until you want to do it again okay!"

    "??" "Bye for now~"

    p "Eh don’t please don’t…"

    hide hitona3

    "She left the room…"

    "I really hope she’s not serious…I should considering moving again…"

    "Ah the she didn’t close the door…"

    p "AAAAAAAAAAA I FORGOT! SENPAI IS WAITING FOR MEEEE"

    "I dashed out to the park to meet senpai"

    scene black

    "While going to the park what the girl said keeps ringing in my head"

    "I wonder what was that all about"

    "Too late for regret now, I guess I will never figure out what she was talking about"

    "Bad End"

    return
