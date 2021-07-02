python early:
    def add_choice_to_history(choice):
        narrator.add_history(kind="nvl", who="", what=__(choice), what_args={"italic": True})

