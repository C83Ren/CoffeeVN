define credits_names = {
    'rabbit': _('BlackRabbit13'),
    'kosa': _('Kosakyun'),
    'luttii': _('Luttii'),
    'wari': _('超エライひまわり'),
    'gabu': _('Gabuccino'),
    'cryo': _('Cryo83 (C83Ren)'),
    'pupu': _('pupu'),
    'nep': _('Nepelz_AR'),
    'lemon': _('ILLimN'),
    'lobster': _('lobster'),
    'xn': _('xn'),

    'company': _('Black Rabbit Black Company'),

    'dova': _('DOVA-SYNDROME'),
    'zap': _('zap'),

    'kohi': _('kohi'),

    'artist0': _('???'),
    'artist1': _('???'),
    'artist2': _('???'),

    'message0': _('???'),
    'message1': _('???'),
    'message2': _('???'),
    'message3': _('???'),
    'message4': _('???'),
    'message5': _('???'),
    'message6': _('???'),
    'message7': _('???'),
    'message8': _('???'),
    'message9': _('???'),
    'message10': _('???'),
    'message11': _('???'),
    'message12': _('???'),
    'message13': _('???'),
    'message14': _('???'),
    'message15': _('???'),
    'message16': _('???'),
    'message17': _('???'),
}

define credits_font = 'tl/japanese/SourceHanSansLite.ttf'

screen credits_centered_text(t):
    text t xalign 0.5 color '#FFF' font credits_font

screen credits_space(space):
    fixed xsize 1920 ysize space

screen credits_entry(what, who, trailing_spaces=True):
    vbox:
        use credits_centered_text(what)
        use credits_space(75)
        $ first = True
        for person in who:
            if first:
                $ first = False
            else:
                use credits_space(15)
            use credits_centered_text(credits_names[person])
        if trailing_spaces:
            use credits_space(315)

screen credits_message(who, message, img):
    vbox:
        use credits_space(180)
        fixed xsize 1300 ysize 20
        fixed xsize 1300 ysize 500:
            use credits_centered_text(message)
            vbox xalign 1.0 yalign 0.5:
                $ t = '———' + __(credits_names[who])
                text t xalign 1.0 color '#FFF' font credits_font
        if img:
            fixed xalign 0.5 ysize 300:
                image img xalign 0.5 yalign 0.0
            use credits_space(100)
        else:
            use credits_space(400)

screen credits_display():
    vbox:
        use credits_space(125)
        use credits_entry(_("Planning"), ["company"])
        use credits_entry(_("Scenario"), ["rabbit"])
        use credits_entry(_("Translation"), ["kosa", "xn"])
        use credits_entry(_("Editing"), ["xn"])
        use credits_entry(_("Illustration"), ["nep", "lobster", "lemon", "gabu", "wari", "rabbit", "artist0", "artist1", "artist2"])
        use credits_entry(_("Music"), ["luttii", "dova"])
        use credits_entry(_("Sound"), ["zap"])
        use credits_entry(_("Programming"), ["rabbit", "cryo", "xn"])
        use credits_entry(_("Support"), ["pupu"])
        use credits_entry(_("Messages"), ["message%d" % i for i in range(18)])
        fixed xsize 1920 ysize 1080:
            vbox xalign 0.5 yalign 0.5:
                use credits_entry(_("Special Thanks"), ["kohi"], trailing_spaces=False)
        fixed xsize 1920 ysize 1080:
            vbox xalign 0.5 yalign 0.5:
                use credits_centered_text(_("Congratulations on your second anniversary!"))

define credits_messages = [
    ('rabbit', 'Test Test Test\n\nテストテストテスト', None),
    ('kosa', 'テストテストテスト', 'images/stamp idle.png'),
]

default credits_message_index = 0
screen credits_message_display:
    use credits_message(*credits_messages[credits_message_index])

define credits_scroll_time = 60.0
define credits_message_display_time = 5.0
define credits_height = 8678

transform credits_scroll:
    xalign 0.5
    ypos 1080

    linear credits_scroll_time ypos -credits_height + 1080

screen credits_scroll_screen:
    fixed at credits_scroll:
        use credits_display()

image credits_bg = 'images/credits/bg.png'

label credits:
    stop music
    stop sound
    $ _skipping = False
    $ _game_menu_screen, _old_game_menu_screen = None, _game_menu_screen
    window hide

    scene credits_bg with dissolve

    show screen credits_scroll_screen
    $ renpy.pause(credits_scroll_time + 2, hard=True)
    hide screen credits_scroll_screen with dissolve

    $ credits_message_index = 0
    while credits_message_index < len(credits_messages):
        show screen credits_message_display with dissolve
        pause credits_message_display_time
        hide screen credits_message_display with dissolve
        $ credits_message_index += 1

    $ _game_menu_screen = _old_game_menu_screen
    $ _skipping = True

    return
