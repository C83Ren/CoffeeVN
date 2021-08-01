python early:
    in_check_lyrics = False
    def normalize_input(s):
        replacements = {
            # punctuation
            '"': '',
            "'": '',
            ' ': '',
            '.': '',
            ',': '',
            '!': '',
            '?': '',
            '　': '',
            '。': '',
            '、': '',
            '！': '',
            '？': '',
            '・': '',
            # alternative en input
            'tu': 'tsu',
            'z': 'j',
            'si': 'shi',
            'sy': 'sh',
            'he': 'e',
            'jy': 'j',
            'ha': 'wa',
            'wo': 'o',
            # limited kanji
            '汗': 'あせ',
            '拭': 'ぬぐ',
            '夏': 'なつ',
            '解決': 'かいけつ',
            '指先': 'ゆびさき',
            '指': 'ゆび',
            '送': 'おく',
            '君': 'きみ',
            '今日': 'きょう',
            '今': 'いま',
            '為': 'ため',
            '一所': 'いっしょ',
            '一生': 'いっしょう',
            '懸命': 'けんめい',
            '頑張': 'がんば',
            '春': 'はる',
            '包': 'つつ',
            '行': 'い',
            '僕': 'ぼく',
            '名前': 'なまえ',
            '存在': 'そんざい',
            '無': 'な',
            '攻': 'せ',
            '此処': 'ここ',
            '来': 'き',
            '星': 'ほし',
            '重': '重',
            # katakana
            'ア': 'あ',
            'イ': 'い',
            'ウ': 'う',
            'エ': 'え',
            'オ': 'お',
            'カ': 'か',
            'キ': 'き',
            'ク': 'く',
            'ケ': 'け',
            'コ': 'こ',
            'ガ': 'が',
            'ギ': 'ぎ',
            'グ': 'ぐ',
            'ゲ': 'げ',
            'ゴ': 'ご',
            'サ': 'さ',
            'シ': 'し',
            'ス': 'す',
            'セ': 'せ',
            'ソ': 'そ',
            'ザ': 'ざ',
            'ジ': 'じ',
            'ズ': 'ず',
            'ゼ': 'ぜ',
            'ゾ': 'ぞ',
            'タ': 'た',
            'チ': 'ち',
            'ツ': 'つ',
            'テ': 'て',
            'ト': 'と',
            'ダ': 'だ',
            'ヂ': 'ぢ',
            'ヅ': 'づ',
            'デ': 'で',
            'ド': 'ど',
            'ナ': 'な',
            'ニ': 'に',
            'ヌ': 'ぬ',
            'ネ': 'ね',
            'ノ': 'の',
            'ハ': 'は',
            'ヒ': 'ひ',
            'フ': 'ふ',
            'ヘ': 'へ',
            'ホ': 'ほ',
            'パ': 'ぱ',
            'ピ': 'ぴ',
            'プ': 'ぷ',
            'ペ': 'ぺ',
            'ポ': 'ぽ',
            'バ': 'ば',
            'ビ': 'び',
            'ブ': 'ぶ',
            'ベ': 'べ',
            'ボ': 'ぼ',
            'マ': 'ま',
            'ミ': 'み',
            'ム': 'む',
            'メ': 'め',
            'モ': 'も',
            'ヤ': 'や',
            'ユ': 'ゆ',
            'ヨ': 'よ',
            'ラ': 'ら',
            'リ': 'り',
            'ル': 'る',
            'レ': 'れ',
            'ロ': 'ろ',
            'ワ': 'わ',
            'ヲ': 'を',
            'ン': 'ん',
            'ッ': 'っ',
            'ァ': 'ぁ',
            'ィ': 'ぃ',
            'ゥ': 'ぅ',
            'ェ': 'ぇ',
            'ォ': 'ぉ',
            'ャ': 'ゃ',
            'ゅ': 'ュ',
            'ョ': 'ょ',
        }
        s = s.lower()
        for k, v in replacements.items():
            s = s.replace(k, v)
        last = {'': None}
        def handle(c):
            if last[''] is not None and c in ('-', 'ー'):
                if last[''] in 'あたさなはまやらわ':
                    return 'ぁ'
                elif last[''] in 'いちしにひみり':
                    return 'ぃ'
                elif last[''] in 'うつすぬふむゆる':
                    return 'ぅ'
                elif last[''] in 'えてせねへめれ':
                    return 'ぇ'
                elif last[''] in 'おとそのほもよろを':
                    return 'ぉ'
                return last['']
            last[''] = c
            return c
        return ''.join(map(handle, s))

    def ask_and_check_lyrics(lyrics_prompt, *accepted_answers):
        input_lyrics = ''
        while not input_lyrics:
            input_lyrics = renpy.input(__(lyrics_prompt), length=50)
            input_lyrics = normalize_input(input_lyrics)
        return any(input_lyrics.startswith(normalize_input(a)) for a in accepted_answers), any(normalize_input(a).startswith(input_lyrics) for a in accepted_answers)

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

        successful, partial = ask_and_check_lyrics(lyrics_prompt, *answer)
        if not successful:
            renpy.call(wrong_call, partial, from_current=True)

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
