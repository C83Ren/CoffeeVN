
label r1_regret_choice:

    s "Hitona nee-chan, did you have something you regretted doing today?"

    p "(What's this girl is asking about… she asked the weirdest things)"

    p "(But I guess she is still a child after all.)"

    "Hmm do I regret something today"

    menu:
        extend ""

        "Yeah I regret something":
            $ regret_choice = "Yeah I regret something"

        "Nope, nothing at all":
            $ regret_choice = "Nope, nothing at all"

    p "[regret_choice]"

    s "Is that so?"

    hide hitona1

    if shoppingflag == "suit":
        
        "After a while, I changed back and we left the shop."
        
        p "(It feels like I’m forgetting something…)"
        
        p "(Oh well.)"

    elif shoppingflag == "dress":

        "We changed back to our clothes and left the shop."

    # Background: Intersection (Afternoon)

    "The sun is starting to set."

    p "(We better start heading back.)"

    #need branching verification
    if movieflag == 1:
        show hitona1 idle1
    elif shoppingflag == "suit" or shoppingflag == "dress":
        show hitona1 idle3

    s "Hitona nee-chan! Let's go to the park!"

    p "(Well, there’s still some time before nightfall.)"

    p "Okay let's go to the park then"

    jump r1_park_end
