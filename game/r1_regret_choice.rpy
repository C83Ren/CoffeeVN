label r1_regret_choice:

    s "Hitona onee-chan, do you have any regrets today?"

    p "{i}What’s this girl is asking about... she asked the weirdest things.{/i}"

    p "{i}But I guess she is still a child after all.{/i}"

    menu:
        "Do I have any regrets?"

        "Yeah, I regret something":
            $ regret_choice = "Yeah, I regret something"

        "Nope, nothing at all":
            $ regret_choice = "Nope, nothing at all"

    p "[regret_choice]"

    s "Is that so?"

    if shoppingflag == "suit":
        hide hitona1

        "After a while, I changed back and we left the shop."

        p "{i}It feels like I’m forgetting something...{/i}"

        p "{i}Oh well.{/i}"

    elif shoppingflag == "dress":
        hide hitona1

        "We changed back to our clothes and left the shop."

    # Background: Intersection (Afternoon)

    "The sun is starting to set."

    p "{i}We better start heading back.{/i}"

    if movieflag == 1:
        show hitona1 idle1
    else:
        show hitona1 idle3

    s "Hitona nee-chan! Let’s go to the park!"

    p "{i}Well, there’s still some time before nightfall.{/i}"

    p "Okay! Let’s go to the park then!"

    jump r1_park_end
