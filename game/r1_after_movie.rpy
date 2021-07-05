label r1_after_movie:
    p "Yeah definitely!"

    show hitona1 happy1

    s "Yaaay! It's a promise okay Hitona nee-chan!"

    p "Yeah sure"

    hide

    "We walked out from the cinema then"

    show hitona1 smile1

    s "Hitona nee-chan, did you have something you regretted doing today?"

    "What's this girl is asking about, she asked the weirdest things"

    "But I guess that's what it means becoming a kid"

    "Hmm do I regret something today"

    menu:
        extend ""

        "Yeah I regret something":
            $ r1_regret_choice = "Yeah I regret something"

        "Nope, nothing at all":
            $ r1_regret_choice = "Nope, nothing at all"

    p "[r1_regret_choice]"

    s "Is that so?"

    # Background: Intersection (Afternoon)

    "The sun is setting we probably should go back"

    s "Hitona nee-chan! Let's go to the park!"

    "Or not"

    p "Okay let's go to the park then"

    jump r1_park_end
