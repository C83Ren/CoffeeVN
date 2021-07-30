init python:
    famresflag = 0

label r1_famres:
    # Family Restaurant
    #
    # Music: Happy excited, doesn’t loop, > 3 minutes (same as before)
    # Background: Family Restaurant
    #
    # They arrived at the family restaurant. They took  their seats.
    # The place seems fairly crowded, nothing so much that you would call it packed.
    # “You can order anything you want” said Hitona.
    # Heard that Shiraishi asked back, “Can I order more than one?”
    # “Sure”.
    # The waitress came, Hitona ordered pasta and fries on the side.
    # Shiraishi then proceeded with ordering omellete rice, beef bowl, and hamburger steak.
    # When Hitona heard that her brain couldn’t processed it, when the waitress left then it clicked.
    # “Eeeeeeeh?! You’re going to eat all that?!”. Shiraishi just smiled
    # When the food came Shiraishi asked, “Hitona neechan can you eat one of these?”
    # “….EEEEH?!” With such face Hitona just couldn’t say no.
    # So which one will you choose?

    "We walked to a nearby family restaurant."

    scene bg famres

    "We took our seats and looked at the menu."

    p "You can get whatever you want, Shiraishi."

    show hitona1 happy2

    s "Really? Can I order more than one?"

    p "You sure are hungry! Sure, go right ahead, order whatever you want~"

    show hitona1 idle2

    "Shiraishi flipped through the menu focusedly, choosing what to order."

    p "Done choosing?"

    s "Yes!"

    show hitona1 smile2

    p "Let’s call the waitress then."

    "Waitress" "Are you ready to order?"

    p "I’d like the carbonara pasta and fries. What about you, Shiraishi?"

    show hitona1 smile1

    s "Shiraishi wants omurice, beef bowl, and hamburger steak!"

    p "..."

    "Waitress" "Carbonara pasta, fries, omurice, beef bowl, and hamburger steak, right? Thank you for your order; please wait a bit."

    "The waitress left."

    p "..."

    p "Ehhhhhhhh?!! You’re going to eat all that, Shiraishi??!"

    "Shiraishi just replied with a bright smile."

    "Not long after, the food came."

    p "As expected... this is really a lot..."

    show hitona1 idle2

    s "Hitona onee-chan~"

    p "Hmmm?"

    s "Can Hitona onee-chan eat one of these?"

    p "..."

    p "..."

    p "EHHHHH!?"

    p "W...Wait a second...!"

    show hitona1 stareyes1

    "Shiraishi looked at me pleadingly with eyes full of hope."

    p "...Okay fine."

    show hitona1 happy3

    s "Pick one, Hitona onee-chan!"

    menu:
        "Which dish should I eat?"
        "Omurice":
            $ famires_food = "Omurice"
        "Beef Bowl":
            $ famires_food = "Beef Bowl"
        "Hamburger Steak":
            $ famires_food = "Hamburger Steak"
    $ add_choice_to_history(famires_food)

    p "I’ll have the [famires_food!t] then."

    show hitona1 idle2

    if famires_food == "Omurice":
        s "Hitona onee-chan, Shiraishi has something to ask."

        p "What is it?"

        s "Do people become taller if they eat omurice?"

        p "{i}Where did that come from??{/i}"

        p "Eh? I don’t think so."

        p "Usually people ask if drinking milk makes you grow taller, but omurice? That’s a new one."

        p "You want to become taller, Shiraishi?"

        show hitona1 idle1

        s "Yes! Shiraishi wants to become tall and beautiful just like Hitona onee-chan!"

        p "{i}Ahh, what a precious response...{/i}"
    elif famires_food == "Hamburger Steak":
        s "Hitona onee-chan, does Hamburger Steak make you more energetic?"

        p "It’s meat... so I guess so? Why?"

        show hitona1 idle1

        s "Shiraishi heard of a really energetic person who loves hamburger steak!"

        s "Shiraishi thought that maybe hamburger steaks were the reason that she’s always so energetic!"

        p "{i}What a cute thought... for some reason, it reminds me of a certain someone though.{/i}"

        p "Well, I guess whenever you eat your favourite foods you become a bit happier."

        show hitona1 idle2

        s "Does that mean that hamburger steak is Hitona onee-chan’s favourite food?"

        p "Uhhh... no, not really..."

        s "Is that so?"
    else:
        s "Hitona onee-chan, are you planning to play something tonight?"

        p "Uhh... I don’t have any plans, so not really."

        s "Hitona onee-chan, do you like beef bowls?"

        p "I guess so?"

        s "When Hitona onee-chan chose the beef bowl, Shiraishi thought that Hitona onee-chan was planning to play a horror game tonight!"

        p "That’s oddly specific, why did you think so?"

        show hitona1 idle1

        s "Fortune telling!"

        p "That’s some impressive fortune telling alright...."

    "We somehow managed to finish eating the mountain of food that we (Shiraishi) ordered."

    p "Ugghhh, I ate too much..."

    show hitona1 happy3

    s "It was yummy!"

    p "I can’t believe you managed to eat all of that by yourself!"

    p "You might have even been able to eat all three of them..."

    show hitona1 smile2

    s "No way! Shiraishi can’t eat three; it’s because of Hitona onee-chan that we finished!"

    p "{i}Then don’t order three in the first place...{/i}"

    $ famresflag = 1

    jump r1_post_meal
    # # Shiraishi seemed very happy after all that.
    # # It’s still noon, what should we do?
    # menu:
    #     "where to go?"
    #     "movie":
    #         jump r1_movie
    #     "shopping":
    #         jump r1_shopping
