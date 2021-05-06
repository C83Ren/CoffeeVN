label true_end:
label end_14:
    $ persistent.ed_unlocked_14 = True

    scene bg shop with dissolve

    "While heading to the park..."

    play audio phonecall loop
    pause 3.0

    "...my phone started to ring."

    stop audio

    sn "Kohi~"

    p "Ah senpai, I'm on my way there now."

    sn "Hmmm? I'm in front of your place though..."

    sn "I kept waiting but you didn’t come, so I decided to go to you instead."

    p "Eh? But it hasn’t even been 5 minutes..."

    p "Did we pass by each other somehow???"

    sn "Well, I'll wait here then. You also wanted to ask about the safe right?"

    p "I...okay, I'll head back now."

    "I just left though...weird. How did I not see her??"

    scene bg intersection day with dissolve

    "When I arrived back at my place, senpai was standing in front of the door."

    sn "Hiya Kohiii! It's been a while hasn't it?"

    p "Ah senpaaai!"

    p "You should've told me you were coming instead!"

    sn "But you were taking so long, I just had to come to you."

    p "But...I headed straight for the park right after you called!"

    sn "Eh...but I waited so long though..."

    p "Weird..."

    "I opened the door, and the two of us went inside."

    scene bg room with dissolve

    sn "About the safe though, here is the last key. You left it in your room."

    p "Huh? What are you talking...about...?"

    "I only remember having 3 pieces of paper and 3 keys..."

    "I took three keys and slips of paper out from my drawer."

    "4 keys, and three sheets of papers with 1, 0, and 1 written on them."

    sn "Try opening the safe."

    label true_end_combination:
        # TODO implement
        menu:
            "It's a combination lock with 4 digits."
            "wrong passcode":
                "It's not opening...probably the wrong code. Let's try again."
                jump true_end_combination
            "correct passcode":
                pass

    p "Oh it opened!"

    "There’s a letter inside and...another safe with a keyhole."

    "\"Hitona! This is our gift to you. Open each safe with each key!\""

    "insert key"

    call show_cg("BirthdayKohi")

    "\"First of all, we want to tell you that your fans are always there behind you! No matter when or where, across time and space, we will always be there for you!\""

    "There's another locked safe inside, and there are three keys left."

    "insert key"

    # call show_cg("")

    "\"Second! Keep being yourself! That is Hitona's unique charm! Let loose!\""

    "There's another locked safe inside, and there are two keys left."

    "insert key"

    # call show_cg("")

    "\"Third! The memories that you have made all this time are irreplaceable!\""

    "\"We want Hitona to keep on making more memories from now on!\""

    "There's another locked safe inside, and there is one key left."

    "insert key"

    # call show_cg("")

    # credits, etc.

    return
