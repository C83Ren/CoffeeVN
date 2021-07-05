python early:
    def input_with_history(prompt, default=None):
        narrator.add_history(kind="nvl", who="", what=__(prompt))
        input_value = ''
        while not input_value:
            input_value = renpy.input(__(prompt), default=__(default))
        narrator.add_history(kind="nvl", who="", what=__(input_value), what_args={"italic": True})
        return input_value
