python early:
    in_check_lyrics = False
    def normalize_input(s):
        s = s.replace('"', '').replace('　', '').replace('・', '').replace('。', '').replace('、', '').replace(' ', '')
        return s

    def ask_and_check_lyrics(lyrics_prompt, *accepted_answers):
        input_lyrics = ''
        while not input_lyrics:
            input_lyrics = renpy.input(__(lyrics_prompt), length=50)
            input_lyrics = normalize_input(input_lyrics)
        return any(input_lyrics.startswith(normalize_input(a)) for a in accepted_answers)

    def parse_check_lyrics(lex):
        who = lex.simple_expression()
        filename = lex.string()
        lyrics_prompt = lex.string()
        wrong_call = lex.label_name()
        answer = []
        while not lex.eol():
            answer.append(lex.string())
        return (who, filename, lyrics_prompt, wrong_call, answer)

    def execute_check_lyrics(o):
        global quick_menu, in_check_lyrics

        who, filename, lyrics_prompt, wrong_call, answer = o

        if in_check_lyrics and _return:
            in_check_lyrics = False
            renpy.jump(_return)

        in_check_lyrics = True

        renpy.music.set_pause(True)
        renpy.music.play([filename], channel="sound", loop=False, fadeout=1.0, fadein=1.0)
        _window_hide()
        quick_menu = False
        while renpy.music.is_playing("sound"):
            renpy.pause(1, hard=True)
        quick_menu = True
        _window_show()

        successful = ask_and_check_lyrics(lyrics_prompt, *answer)
        if not successful:
            renpy.call(wrong_call, from_current=True)

        in_check_lyrics = False

    def lint_check_lyrics(o):
        if len(o) != 5:
            renpy.error("Expected 5 arguments to check_lyrics")
            return

        who, filename, lyrics_prompt, wrong_call, answer = o
        try:
            eval(who)
        except:
            renpy.error("Character not defined: %s" % who)

    def translation_strings_check_lyrics(o):
        who, filename, lyrics_prompt, wrong_call, answer = o
        return [lyrics_prompt]

    renpy.register_statement(
        "check_lyrics",
        parse=parse_check_lyrics,
        execute=execute_check_lyrics,
        lint=lint_check_lyrics,
        translation_strings=translation_strings_check_lyrics,
    )
