python early:
    listen_again = "Listen again"
    enter_again = "Guess again"

    def normalize_input(s):
        s = s.replace('"', '').replace('　', '').replace('・', '').replace('。', '').replace('、', '').replace(' ', '')
        return s

    def ask_and_check_lyrics(lyrics_prompt, *accepted_answers):
        input_lyrics = ''
        while not input_lyrics:
            input_lyrics = renpy.input(__(lyrics_prompt), length=20)
            input_lyrics = normalize_input(input_lyrics)
        return any(input_lyrics.startswith(normalize_input(a)) for a in accepted_answers)

    def parse_check_lyrics(lex):
        who = lex.simple_expression()
        filename = lex.string()
        lyrics_prompt = lex.string()
        wrong_text = lex.string()
        answer = lex.string()
        lex.expect_eol()
        return (who, filename, lyrics_prompt, wrong_text, answer)

    def execute_check_lyrics(o):
        global quick_menu

        who, filename, lyrics_prompt, wrong_text, answer = o

        successful = False
        action = "listen"
        while not successful:
            if action == "listen":
                renpy.music.set_pause(True)
                renpy.music.play([filename], channel="sound", loop=False, fadeout=1.0, fadein=1.0)
                _window_hide()
                quick_menu = False
                while renpy.music.is_playing("sound"):
                    renpy.pause(1, hard=True)
                quick_menu = True
                _window_show()

            successful = ask_and_check_lyrics(lyrics_prompt, answer)
            if not successful:
                renpy.say(eval(who), __(wrong_text))
                action = renpy.display_menu([(__(listen_again), "listen"), (__(enter_again), "enter")])


    def lint_check_lyrics(o):
        if len(o) != 5:
            renpy.error("Expected 5 arguments to check_lyrics")
            return

        who, filename, lyrics_prompt, wrong_text, answer = o
        try:
            eval(who)
        except:
            renpy.error("Character not defined: %s" % who)

    def translation_strings_check_lyrics(o):
        who, filename, lyrics_prompt, wrong_text, answer = o
        return [lyrics_prompt, wrong_text, listen_again, enter_again]

    renpy.register_statement(
        "check_lyrics",
        parse=parse_check_lyrics,
        execute=execute_check_lyrics,
        lint=lint_check_lyrics,
        translation_strings=translation_strings_check_lyrics,
    )
