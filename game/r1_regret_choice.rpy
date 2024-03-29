label r1_regret_choice_init():
    $ regret_choice = "Nope, nothing at all"
    return

label r1_regret_choice:

    s "[player_name] onee-chan, do you have any regrets today?" id r1_regret_choice_3bfec0a0

    p "{i}What’s this girl is asking about... she asked the weirdest things.{/i}"

    p "{i}But I guess she is still a child after all.{/i}"

    menu:
        "Do I have any regrets?"

        "Yeah, I regret something":
            $ regret_choice = "Yeah, I regret something"

        "Nope, nothing at all":
            $ regret_choice = "Nope, nothing at all"

    p "[regret_choice!t]"

    s "Is that so?"

    if shoppingflag == "suit":
        hide hitona1

        "After a while, I changed back and we left the shop."

        p "{i}It feels like I’m forgetting something...{/i}"

        p "{i}Oh well.{/i}"

    elif shoppingflag == "dress":
        scene bg shop with dissolve

        "We changed back to our clothes and left the shop."

    # Background: Intersection (Afternoon)

    scene bg shop with fade

    stop music fadeout 1.0

    "The sun is starting to set."

    p "{i}We better start heading back.{/i}"

    if movieflag == 1:
        show hitona1 idle1 with dissolve
    else:
        show hitona1 idle3 with dissolve

    s "[player_name] nee-chan! Let’s go to the park!" id r1_regret_choice_de5812ac

    p "{i}Well, there’s still some time before nightfall.{/i}"

    p "Okay! Let’s go to the park then!"

    jump r1_park_end
