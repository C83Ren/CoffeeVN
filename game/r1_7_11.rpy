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

    scene bg conbini

    "We walked to the best place ever for getting food! 7/11~"

    show hitona1 smile2

    "It was clear that Shiraishi was very excited but now she kept holding my hand"

    s "Hitona nee-chan what will I be having for lunch?"

    p "Anything you want Shiraishi~"

    show hitona1 happy2

    s "I want Hitona nee-chan’s recommendation!"

    P "Is that so? Shiraishi wants the opinion of the (not) official 7/11 ambassador! Okay then~"

    menu:
        "What should I recommend to her?"
        "7/11 Soba Meshi":
            p "How about Soba Meshi?"

            show hitona1 happy3

            s "Sounds yummy! Shiraishi can’t wait!"

            "We took two of Soba Meshi and I paid for them. Went out to find a place to sit"
            
            show hitona1 idle1

            p "Let’s Eat!" (multiple=2)

            s "Let’s Eat!" (multiple=2)

            "Nom nom nom"

            show hitona1 happy1

            s "It's good!"

            p "Well I'm glad"

            p "There's soba, chicken and cabbage there. A perfect combo!"

            s "There's no cabbage though… but there's sesame seed!"

            p "Oh really? I forgot about that"

            s "The soba feels like soba too!"

            p "What does that even mean… but glad you like it~"

        "7/11 Seven Premium Gold Hamburger Steak":
            p "How about Seven Premium Gold Hamburger Steak?"

            show hitona1 happy3

            s "Sounds yummy! Shiraishi can’t wait!"

            "We took two of Seven Premium Gold Hamburger Steak and I paid for them. Went out to find a place to sit"

            show hitona1 idle1

            p "Let’s Eat!" (multiple=2)

            s "Let’s Eat!" (multiple=2)

            "Nom nom nom"

            show hitona1 happy1
            
            s "It's delicious!"
            
            s "The sauce is delicious~"

            p "Right! It's supposed to be 100 % beef" 

            s "The beef essence is really coming through"
            
            "I have no idea what is she talking about but"

            p "Is that so? Well there's this another one called Japanese style which I think has a better sauce"

            s "Heee?"

            p "But definitely the steak is better here"

            s "Well Shiraishi likes it!"

            p "Glad you like it~"

        "7/11 Spaghetti Neapolitan":
            p "How about Spaghetti Neapolitan?"

            show hitona1 happy3

            s "Sounds yummy! Shiraishi can’t wait!"

            "We took two of Spaghetti Neapolitan and I paid for them. Went out to find a place to sit"

            show hitona1 idle1

            p "Let’s Eat!" (multiple=2)

            s "Let’s Eat!" (multiple=2)

            "Nom nom nom"
            
            show hitona1 happy1

            s "It's yummy~ And there's a lot!"

            p "Yup~ there are green onion, green pepper, garlic, tomato paste, sausage"

            s "But there's no mushroom…"

            p "Were you expecting some…?"

            s "Shiraishi just thought there would be some"

            s "But there are green pepper, yummy~"

            p "I love the ketchup flavor in there"

            s "Shiraishi too!"

            p "The one who created Neapolitan is a genius~"
    
    # “Sounds yummy!”. They proceed buying the goods, found somewhere to sit and eat the goodies.
    # The choices will reflect on whether it is good okay or bad. Shiraishi will mention about the stream regardless.
    # “Eh? Stream? What do you mean?”
    # “Hitona neechan streams about reviewing food right? I love those! Gush talk~”
    # “Did I ever mention about streaming?”. Shiraishi just smiled and continued eating what she had.
    # Both of them stuffed themselves with food.
    # Now it seemed that Shiraishi had calmed down, it even looks like she was feeling sleepy.
    # What should I do?
    
    show hitona1 idle2

    s "But Hitona nee-chan already mentioned it before in her stream~"

    p "Eh? Stream? What do you mean?"

    show hitona1 happy3

    s "Hitona nee-chan streams about reviewing food right? I love those!"

    s "Those streams make Shiraishi wonder how many snacks Shiraishi hasn’t tried! Everything looks so delicious! And Hitona nee-chan reaction is priceless! Makes Shiraishi watch it over and over again! With how some snacks made Hitona nee-chan so excited while others oddly have no taste, Shiraishi couldn’t wait for Hitona nee-chan’s rating! It’s also funny how the rating sometimes is 5 stars max while other times it’s 3 stars max. It’s a fun stream!"

    p "Eh? Did I ever mention about streaming?"

    show hitona1 idle3

    "Shiraishi just smiled and continued eating"

    "Oh well…"

    show hitona1 bliss4

    menu:
        "We finished our food and Shiraishi looked rather satisfied. She even looked sleepy, What should we do?"
        "Accompany her home":
            jump r1_home_bad_end
        "Go to the park":
            $ r1_regrets = False
            jump r1_park_end
