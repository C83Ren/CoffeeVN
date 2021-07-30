init python:
    movieflag = 0

label r1_movie:
    # Go to the movie
    #
    # Music: Happy excited, doesn’t loop, > 3 minutes (same as before)
    # Background: Cinema
    #
    # They arrived at the cinema. Saw there were two movies that were playing today.
    # One was horror and the other was romance.
    # “Shiraishi, which one do you want to watch?”
    # “I’ll leave it to Hitona neechan~”.
    # So it’s obvious which one right?

    scene bg cinema

    $ movieflag = 1

    if famresflag:
        "I paid for the meal, and then we went to a nearby cinema."
    else:
        "We went to a nearby cinema."

    p "Here we are, the cinema!"

    p "You’ve been to a cinema before, right Shiraishi?"

    show hitona1 smile1

    s "Nope, Shiraishi has never been to a cinema before!"

    p "Really? Then Hitona onee-chan here will make this your best cinema experience ever!"

    show hitona1 happy2

    s "Yaaay!"

    "It seems there are two movies starting soon: a horror movie and a romance movie."

    p "Shiraishi, which one do you want to watch?"

    show hitona1 smile1

    s "I’ll leave it to Hitona onee-chan!"

    menu:
        "Looking at the selection, it’s pretty obvious which one we’re watching! Which movie do we watch?"

        "Horror Movie":
            $ add_choice_to_history("Horror Movie")
            $ mov = "horror"

        "Romance Movie":
            $ add_choice_to_history("Romance Movie")
            $ mov = "romance"

    menu:
        "I went to buy the ticket, but for some reason the cinema only accepts W*bMoney."

        "Buy some W*bMoney":
            $ add_choice_to_history("Buy some W*bMoney")

    "I bought some W*bMoney, then used it to buy a ticket."

    "The movie is starting soon!"

    if mov == "horror":
        "The movie is {i}ParanormalJP{/i}."

        "“The protagonists challenge a certain Haunted Street! They record it thinking it’s a game, but all of a sudden something happened...?!”"

        p "{i}Well, let’s see how it goes.{/i}"

        p "If you feel scared Shiraishi, it’s okay to close your eyes and hold my hands."

        show hitona1 smile1

        s "Okaay."

        hide hitona1

        "The movie is starting."

        "As expected from a horror movie, it’s quite dark."

        "It seems like the movie is from the cameraman’s first-person perspective."

        "The cameraman is challenging the Haunted Street with a partner named Cathy."

        show hitona1 idle2

        "Shiraishi doesn’t seem to be the slightest bit scared."

        hide hitona1

        "Cathy" "Come on, let’s go…aaAAAAAH!!! HELP!!!"

        "Cathy is being dragged away by something!"

        "Now the cameraman is all alone!"

        p "{i}Ahh, I don’t want to watch anymore...{/i}"

        "Suddenly, I felt something grabbing my hand!"

        "I was so surprised I was about to jump up in the air, but it was Shiraishi."

        p "{i}Maybe she’s also scared?{/i}"

        "Holding hands, we were able to finish watching the movie."

        show hitona1 happy1

        s "That was so fun!!"

        p "F...fun?? Ah... that’s good then."

        "Shiraishi doesn’t seem to have been scared at all."

        "Rather, it seems like she held my hand during the movie just to comfort me."

    else:
        "The movie is {i}A Fin Away{/i}."

        "“The story of a girl who wanted to run away from her daily life. One day, she meets a mysterious being, and then becomes a...?!”"

        p "{i}Well, let’s see how it goes.{/i}"

        p "This movie looks pretty interesting, doesn’t it!"

        show hitona1 idle3

        s "Shiraishi can’t wait!"

        hide hitona1

        "The movie is starting."

        "The main character is a middle schooler."

        "Even though her crush is completely oblivious to her feelings, she continues to try to get closer to him."

        p "{i}How strong-minded...!{/i}"

        "The mysterious being is here!"

        "It’s... a shark that seems to live in the aquarium?!"

        "After receiving a mask from the shark..."

        "She put the mask on and jumped into the ocean!"

        p "{i}Ehhhh?!{/i}"

        "The moment the mask touched her face, the girl transformed into a shark!"

        p "{i}Ah, I see...{/i}"

        show hitona1 stareyes1

        "Shiraishi seems to be happily engrossed in the movie."

        hide hitona1

        "After the movie ended..."

        show hitona1 happy1

        s "That was so fun!!"

        p "That was a great movie, wasn’t it! I’m glad Shiraishi also had fun!"


    # Shiraishi then asked “Would you watch a movie again someday?”.
    # Surely you know what to say

    show hitona1 smile2

    "While the credits were playing, I patted Shiraishi’s head."

    show hitona1 idle2

    "Shiraishi suddenly asked a question."

    # choice not added because it’s said aloud in the line after
    menu:
        s "Hitona onee-chan, would you like to watch a movie with Shiraishi again someday?"
        "I don’t know... I’m not sure if we can meet again later, so I can’t promise.":
            jump r1_movie_bad_end
        "Yeah, definitely!":
            jump r1_after_movie
