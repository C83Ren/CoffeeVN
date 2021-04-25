python early:
    def add_choice_to_history(choice):
        narrator.add_history(kind="nvl", who="", what=_(choice), what_args={"italic": True})

