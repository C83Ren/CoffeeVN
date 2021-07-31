init python:
    combiniflag = 0

label r1_7_11:
    # 7/11
    #
    # Music: Happy excited, doesn’t loop, > 3 minutes (same as before)
    # Background: Convenience Store
    #
    # Hitona and Shiraishi arrived at 7/11.
    # Similar with before, Shiraishi was very excited but this time she kept holding Hitona’s hand.
    # Shiraishi asked “What will be having for lunch Hitona nee chan?”.
    # “Whatever you like~”. “I want to have Hitona neechan’s recommendation!”.
    # What will you give?

    stop music fadeout 1.0
    scene bg konbini with Fade(0.5, 0.5, 0.5)

    play music hitona_theme volume 0.2 fadein 1.0

    $ conbiniflag = 1

    "We walked to the best place ever for getting food! Of course, it’s 7/*1!"

    show hitona1 smile2

    "Shiraishi was always very excited, but she was now even more excited than ever, happily grasping onto my hand."

    s "Hitona onee-chan what will we be having for lunch?"

    p "Anything you want! Pick whatever you like!"

    show hitona1 happy2

    s "I want Hitona onee-chan’s recommendation!"

    p "Is that so? Shiraishi wants the opinion of the (not) official 7/11 ambassador? Understood!"

    menu:
        "What should I recommend to her?"
        "7/*1 P*young Sobameshi":
            $ conbini_food = "7/*1 P*young Sobameshi"
        "Sev*n Pr*mium Gold Hamburg Steak":
            $ conbini_food = "Sev*n Pr*mium Gold Hamburg Steak"
        "Sev*n Pr*mium Spaghetti Neapolitan":
            $ conbini_food = "Sev*n Pr*mium Spaghetti Neapolitan"

    p "I recommend getting the [conbini_food!t]!"

    show hitona1 happy3

    s "Sounds yummy! Shiraishi can’t wait!"

    "We took two [conbini_food!t]s and went to pay for them."

    "After buying them, we found empty seats in the eat-in corner."

    show hitona1 idle1

    "Nom nom nom"

    show hitona1 happy1

    if conbini_food == "7/*1 P*young Sobameshi":
        s "It’s good!"

        p "That’s good to hear!"

        p "There’s soba, chicken and cabbage there. A perfect combo!"

        s "There’s no cabbage though... but there’s sesame seed!"

        p "Oh really? I must have forgotten about it."

        s "The soba feels like soba too!"

        p "What does that even... anyways, I’m glad you like it!"

    elif conbini_food == "7/11 Seven Premium Gold Hamburger Steak":
        s "It’s so delicious!"

        s "The sauce is amazing!"

        p "Right? This is supposed to be 100%% beef."

        s "The beef’s essence is really coming through!"

        "I have no idea what she is talking about."

        p "Is that so? By the way, there’s also a Japanese-style Hamburg Steak sold here! I think the sauce on that one is tastier!"

        s "Ohh?"

        p "But the meat is definitely tastier in this one."

        s "Shiraishi likes it!"

        p "That’s good to hear!"

    else:
        s "It’s yummy~! And there’s so much of it!"

        p "Yup! There’s onion, green pepper, garlic, tomato paste, ketchup, and sausage in it."

        s "But there’s no mushroom..."

        p "Were you expecting there to be some?"

        s "Shiraishi just thought there would be some."

        s "But oh well, there’s green pepper!"

        s "So tasty!"

        p "I love the tomato flavor!"

        s "Shiraishi prefers tomato sauces on pasta too!"

        p "The person who invented Spaghetti Neapolitan is really a genius!"

    # “Sounds yummy!”. They proceed buying the goods, found somewhere to sit and eat the goodies.
    # The choices will reflect on whether it is good okay or bad. Shiraishi will mention about the stream regardless.
    # “Eh? Stream? What do you mean?”
    # “Hitona neechan streams about reviewing food right? I love those! Gush talk~”
    # “Did I ever mention about streaming?”. Shiraishi just smiled and continued eating what she had.
    # Both of them stuffed themselves with food.
    # Now it seemed that Shiraishi had calmed down, it even looks like she was feeling sleepy.
    # What should I do?

    show hitona1 idle2

    s "Come to think of it, Hitona onee-chan tried eating this in a stream before~!"

    p "Eh? In a stream? What do you mean?"

    show hitona1 happy3

    s "Hitona onee-chan streams food reviews, right?"

    s "I love those streams!"

    s """
    Whenever Shiraishi watches those streams, Shiraishi always thinks about how many snacks Shiraishi hasn’t tried yet!

    Everything always looks so delicious! And Hitona onee-chan’s reactions are priceless! It makes Shiraishi want to watch it over and over again!

    With how some snacks make Hitona onee-chan really excited, while others oddly have no taste, Shiraishi can never wait for Hitona onee-chan’s rating!

    It’s also funny how the rating sometimes is out of 5 stars while other times it’s out of 3 stars!

    It’s always a fun stream!
    """

    p "{i}Eh? Did I ever mention anything about streaming...?{/i}"

    show hitona1 idle3

    "Shiraishi just smiled and continued eating without saying another word."

    p "{i}Ah, whatever.{/i}"

    show hitona1 bliss4

    jump r1_post_meal
    # menu:
    #     "We finished our food and Shiraishi looked rather satisfied. She even looked sleepy, What should we do?"
    #     "Accompany her home":
    #         jump r1_home_bad_end
    #     "Go to the park":
    #         $ r1_regrets = False
    #         jump r1_park_end
