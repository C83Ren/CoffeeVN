label r1_post_meal:

    "Shiraishi looks very satisfied after that meal. It’s still noon, but Shiraishi looks a bit sleepy."

    menu:
        "What should we do?"
        "Go to the movies":
            $ add_choice_to_history("Go to the movies")

            p "Do you want to go to the movies?"

            show hitona1 happy2

            s "Yes! Let’s go!"

            jump r1_movie
        "Go to the shopping district":
            $ add_choice_to_history("Go to the shopping district")

            p "Do you want to go to the shopping district?"

            show hitona1 happy2

            s "Yes! Let’s go!"

            jump r1_shopping

        "Accompany her home":
            $ add_choice_to_history("Accompany her home")

            jump r1_home_bad_end
