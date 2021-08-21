init python:
    _rtl_maps = {}
    # for tl strings: tl language -> None
    # assumes that all translated strings are unique within each language
    # (i.e. there's no two strings in original lang that map to same string in tl)
    def reverse_tl_map(language):
        # TODO I don't think this handles variables in string tls properly..
        if language not in _rtl_maps:
            _rtl_maps[language] = {v: k for k, v in renpy.game.script.translator.strings[language].translations.items()}
        return _rtl_maps[language]

    # expand variables, etc.
    def expand_string(what):
        return renpy.substitutions.substitute(what, scope=None, force=False, translate=False)[0]

    # tl from None language -> language
    def tl_string(what, language = None):
        if language is None:
            language = persistent.alt_language
        if language is None:
            return what
        tl_what = renpy.translation.translate_string(what, language)
        old_language, renpy.game.preferences.language = renpy.game.preferences.language, language
        tl_what = expand_string(tl_what)
        renpy.game.preferences.language = old_language
        return tl_what

    # parenthesized tl (input in None language)
    def tl_paren(what, alt_language = None, suffix = ''):
        if alt_language is None:
            alt_language = persistent.alt_language
        if alt_language is None:
            return tl_string(what, renpy.game.preferences.language) + suffix
        alt_tl = tl_string(what, alt_language)
        if alt_tl:
            return tl_string(what, renpy.game.preferences.language) + ' (' + alt_tl + ')' + suffix
        else:
            return tl_string(what, renpy.game.preferences.language) + suffix

    # tl from current language -> another language
    # get translation for a string (does not work for block tl)
    def get_alt_string_tl(what, alt_language = None):
        if alt_language is None:
            alt_language = persistent.alt_language
        if alt_language is None:
            return ''
        # what is translated, so reverse translate to None language, then translate to new language
        rtl_map = reverse_tl_map(renpy.game.preferences.language)
        if what in rtl_map:
            what = rtl_map[what]
            alt_tl_what = tl_string(what, alt_language)
        else:
            alt_tl_what = ''
        return alt_tl_what

    # get tl in another language **for the current position only**
    def get_alt_tl(what, alt_language = None):
        if alt_language is None:
            alt_language = persistent.alt_language
        if alt_language is None:
            return ''
        if renpy.game.context().translate_identifier:
            # translate identifiers map to 0+ say statements for a language
            # so we find the index we're currently at (for current language), and
            # display that same index in the alt language, if present
            index = 0
            node = renpy.game.script.translator.lookup_translate(renpy.game.context().translate_identifier)
            # what already has variables substituted in but node.what doesn't
            while not isinstance(node, renpy.ast.EndTranslate) and (not isinstance(node, renpy.ast.Say) or expand_string(node.what) != what):
                node = node.next
                index += 1
            if not isinstance(node, renpy.ast.EndTranslate):
                old_language, renpy.game.preferences.language = renpy.game.preferences.language, alt_language
                alt_tl = renpy.game.script.translator.lookup_translate(renpy.game.context().translate_identifier)
                for i in range(index):
                    alt_tl = alt_tl.next
                    if isinstance(alt_tl, renpy.ast.EndTranslate):
                        break
                if isinstance(alt_tl, renpy.ast.EndTranslate):
                    alt_tl_what = ''
                else:
                    alt_tl_what = alt_tl.what
                alt_tl_what = expand_string(alt_tl_what)
                renpy.game.preferences.language = old_language
            else:
                alt_tl_what = ''
        else:
            # if there's no translation id, this is translated through strings rather than tl blocks
            alt_tl_what = get_alt_string_tl(what)
        return alt_tl_what
