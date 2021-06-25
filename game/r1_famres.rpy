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

    "We walked to a nearby family restaurant"

    scene bg famres

    "We took our seats"

    p "You can get whatever you want Shiraishi"

    show hitona1 happy2

    s "Really? Can I order more than one?"

    p "You sure are hungry, sure go ahead"

    show hitona1 idle2

    "Shiraishi was flipping the menu with focus, choosing what to order"

    p "Done choosing?"

    s "Yes!"

    show hitona1 smile2

    p "Let’s call the waitress then"

    "Waitress" "What would you like to order?"

    p "I’d like carbonara pasta and fries, what about you Shiraishi?"

    show hitona1 smile1

    s "Shiraishi wants omellete rice, beef bowl, and hamburger steak!"

    p "..."

    "Waitress" "Thank you for your order, please wait a bit"

    "The waitress left"

    p "..."

    p "Eeeeeeeh?!! You’re going to eat all that Shiraishi??!"

    "Shiraishi just smiled"

    "Not long after the food came"

    p "As expected…this is a lot…"

    show hitona1 idle2

    s "Hitona nee-chan~"
    
    p "Hmmm?"

    s "Can Hitona nee-chan eat one of these?"

    p "..."

    p "..."

    p "EEEEEH?! But!"

    show hitona1 stareyes1

    "Shiraishi was showing such a sweet hopeful begging eyes… She’s too bright!"

    p "...Okay"

    show hitona1 happy3

    s "Pick one Hitona nee-chan!"

    menu:
        "Which one should I pick…"
        "Omellete Rice":
            p "I'll have Omellete Rice"

            show hitona1 idle2
            
            s "Hitona nee-chan, Shiraishi wants to ask"
            
            p "What is it?"
            
            s "Would Shiraishi become taller if she eats omelette rice?"
            
            "Where did that come from??"
            
            p "Eh? I don't think so"
            
            p "Usually people ask if milk is going to make you taller, but omelette rice? That's a first one"
            
            p "You want to become taller Shiraishi?"
            
            show hitona1 idle1
            
            s "Yes Shiraishi wants to become tall and beautiful like Hitona nee-chan"
            
            "What a cute response~ I want to pat her"

        "Hamburger Steak":
            p "I'll have Hamburger Steak"
            
            show hitona1 idle2
            
            s "Hitona nee-chan, does Hamburger Steak make you energetic?"
            
            p "It's meat…I guess so? Why ask?"
            
            show hitona1 idle1
            
            s "Shiraishi heard a really energetic person who loves hamburger steak"
            
            s "Shiraishi thought hamburger steak is the reason she is so energetic"
            
            "What a cute thought...that reminds me of someone though..."
            
            p "Well whenever you eat your favourite food you'll become energetic!"
            
            show hitona1 idle2
            
            s "Does that mean hamburger steak is Hitona nee-chan's favourite food?"
            
            p "Uuuh...No, not really"
            
            s "Is that so?"

        "Beef Bowl":
            p "I'll have Beef Bowl"
            
            show hitona1 idle2
            
            s "Hitona nee-chan, are you planning to play something tonight?"
            
            p "I didn't plan for anything, so not really"
            
            s "Does Hitona nee-chan like beef bowl?"
            
            p "Yeah I guess so?"
            
            s "When Hitona nee-chan chose beef bowl, Shiraishi thought Hitona nee-chan will be playing a horror game tonight"
            
            p "That's quite specific, how so?"
            
            show hitona1 idle1
            
            s "There was a fortune telling about it!"
            
            p "That's some fortune telling alright..."

    "We ate the mountain of food that we (Shiraishi) ordered and somehow managed to finish it"

    p "Ugghhh that was a lot…"
    
    show hitona1 happy3
    
    s "It was yummy!"
    
    p "I can’t believe you managed to eat all of that by yourself"
    
    p "You might even be able to eat all 3…"
    
    show hitona1 smile2
    
    s "No! Shiraishi can’t eat 3, Hitona nee-chan helped"
    
    "Don’t order 3 in the first place…"

    # Shiraishi seemed very happy after all that.
    # It’s still noon, what should we do?
    menu:
        "where to go?"
        "movie":
            jump r1_movie
        "shopping":
            jump r1_shopping
