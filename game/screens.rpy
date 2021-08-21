################################################################################
## Initialization
################################################################################

init offset = -1

init python:
    _game_menu_screen = 'history'

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        if textbox_menu:
            hbox:
                fixed:
                    if persistent.alt_language:
                        xsize 0.3
                    text what id "what":
                        line_spacing -5

                if persistent.alt_language:
                    $ alt_tl = get_alt_tl(what)
                    $ alt_tl = '(%s)' % alt_tl if alt_tl else ''
                    fixed:
                        text "[alt_tl]":
                            style "say_dialogue"
                            font gui.tl_fonts[persistent.alt_language]
                            slow_cps preferences.text_cps
                            line_spacing -5
        else:
            text what id "what":
                line_spacing -5

            if persistent.alt_language:
                $ alt_tl = get_alt_tl(what)
                text alt_tl:
                    style "say_dialogue"
                    font gui.tl_fonts[persistent.alt_language]
                    slow_cps preferences.text_cps
                    line_spacing -5
                    yoffset 105


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input" copypaste True

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    if textbox_menu:
        style_prefix "say"
        vbox:
            xpos gui.dialogue_xpos + 20
            ypos 1080 - gui.textbox_height + gui.dialogue_ypos + 60
            hbox:
                for i, item in enumerate(items[::2]):
                    $ caption = tl_paren(item.caption)
                    textbutton caption:
                        action [Function(add_choice_to_history, expand_string(item.caption)), item.action]
                        xsize (gui.dialogue_width - 120) / ((len(items) + 1) / 2)
                        text_size gui.choice_button_text_size
                        text_xalign gui.dialogue_text_xalign
            hbox:
                for i, item in enumerate(items[1::2]):
                    $ caption = tl_paren(item.caption)
                    textbutton caption:
                        action [Function(add_choice_to_history, expand_string(item.caption)), item.action]
                        xsize (gui.dialogue_width - 120) / ((len(items) + 1) / 2)
                        text_size gui.choice_button_text_size
                        text_xalign gui.dialogue_text_xalign
    else:
        style_prefix "choice"
        vbox:
            for i in items:
                $ caption = tl_paren(i.caption)
                textbutton caption action [Function(add_choice_to_history, expand_string(i.caption)), i.action]

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

## When this is true, choices will be displayed in 2x4 layout in the text box.
default textbox_menu = False


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.9876

            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action If(save_enabled, ShowMenu('save'))
            textbutton _("Load") action If(save_enabled, ShowMenu('load'))
            textbutton _("Prefs") action ShowMenu('preferences')

default quick_menu = True
default save_enabled = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

style nav_button is button:
    # hover_background "#eaffd966"
    hover_background "gui/nav_button hover.png"
    selected_background "gui/nav_button selected.png"
    xminimum 365
    ymaximum 50

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.75

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start() style "nav_button"

        else:

            textbutton _("History") action ShowMenu("history") style "nav_button"

            textbutton _("Save") action If(save_enabled, ShowMenu("save")) style "nav_button"

        textbutton _("Load") action If(save_enabled, ShowMenu("load")) style "nav_button"

        if main_menu:
            textbutton _("CG") action ShowMenu("cg") style "nav_button"

            textbutton _("Endings") action ShowMenu("ed") style "nav_button"

            textbutton _("Music") action ShowMenu("music_room") style "nav_button"

        textbutton _("Preferences") action ShowMenu("preferences") style "nav_button"

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True) style "nav_button"

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu() style "nav_button"

        if main_menu:
            textbutton _("About") action ShowMenu("about") style "nav_button"

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help") style "nav_button"

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu) style "nav_button"


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    use main_menu_background()

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

screen main_menu_background():
    if persistent.ed_unlocked_4:
        add gui.main_menu_background_final
        add gui.main_menu_background_final xpos 0.15
    else:
        add gui.main_menu_background_initial
        fixed xalign 1.0 yalign 1.0 ysize 300 xsize 800:
            for i in range(1, 4):
                fixed ysize 275 xsize 250 xpos 250 * (i - 1):
                    if getattr(persistent, 'ed_unlocked_%d' % i):
                        image Transform(Image('images/keys/note_r%d.png' % i), rotate=-10, xpos=120, ypos=110)
                        image Transform(Image('images/keys/key_r%d hover.png' % i), zoom=0.3, rotate=35)

    if _preferences.language == 'simplified_chinese':
        image Transform(Image(gui.title_image_zh), zoom=0.3) xalign 1.0 yalign 0.0
    else:
        image Transform(Image(gui.title_image), zoom=0.3) xalign 1.0 yalign 0.0

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        use main_menu_background()

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.game_menu_header_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton "<" action FilePagePrevious()

                if config.has_autosave:
                    textbutton "{#auto_page}A" action FilePage("auto")

                if config.has_quicksave:
                    textbutton "{#quick_page}Q" action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton ">" action FilePageNext(max=9)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences
init python:
    @renpy.pure
    class Language(Action, DictEquality):
        alt = _("Language [text]")

        def __init__(self, language, alt_language = None):
            self.language = language
            self.alt_language = alt_language

        def __call__(self):
            renpy.change_language(self.language)
            persistent.alt_language = self.alt_language
            renpy.restart_interaction()

        def get_selected(self):
            return _preferences.language == self.language and persistent.alt_language == self.alt_language

        def get_sensitive(self):
            return (self.language in renpy.known_languages() or self.language is None) and \
                   (self.alt_language in renpy.known_languages() or self.alt_language is None)


screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton "{font=DejaVuSans.ttf}English{/font}" action Language(None)
                    textbutton "{font=tl/japanese/SourceHanSansLite.ttf}日本語{/font}" action Language("japanese")
                    textbutton "{font=tl/simplified_chinese/ui.ttf}简体中文{/font}" action Language("simplified_chinese")
                    textbutton "{font=tl/japanese/SourceHanSansLite.ttf}日本語{/font}+{font=tl/simplified_chinese/ui.ttf}简体中文{/font}" action [Language("japanese", "simplified_chinese")]

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3
    ymaximum 60

style pref_label_text:
    yalign 1.0
    ymaximum 60

style pref_vbox:
    xsize 338
    ymaximum 60

style radio_vbox:
    spacing gui.pref_button_spacing
    ymaximum 50

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    ymaximum 50

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    ymaximum 50

style check_vbox:
    spacing gui.pref_button_spacing
    ymaximum 50

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    ymaximum 50

style check_button_text:
    properties gui.button_text_properties("check_button")
    ymaximum 50

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    if "italic" in h.what_args:
                        italic True
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


screen alert(message):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Close") action Function(renpy.hide_screen, "alert")

    key "game_menu" action Function(renpy.hide_screen, "alert")


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, dialogue_tl, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:
            # TODO dual tl not supported
            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue, is_tl=False)
        elif persistent.alt_language:
            vbox:
                fixed ysize 540:
                    vbox spacing gui.nvl_spacing:
                        use nvl_dialogue(dialogue, is_tl=False)
                fixed ysize 540:
                    vbox spacing gui.nvl_spacing:
                        use nvl_dialogue(dialogue_tl, is_tl=True)
        else:
            use nvl_dialogue(dialogue, is_tl=False)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue, is_tl=False):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id
                    if d.what_id == 'what_tl':
                        slow_cps preferences.text_cps
                    if is_tl:
                        font gui.tl_fonts[persistent.alt_language]


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900


################################################################################
## CG
################################################################################

init python:
    persistent.cg_page = persistent.cg_page or 1

    class CGPage(Action):
        def __init__(self, page):
            self.page = page

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent.cg_page = self.page
            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page is not None and self.page != persistent.cg_page

    class CGPagePrevious(CGPage):
        def __init__(self):
            super(CGPagePrevious, self).__init__(persistent.cg_page - 1 if persistent.cg_page and persistent.cg_page > 1 else None)

    class CGPageNext(CGPage):
        def __init__(self, mx):
            super(CGPageNext, self).__init__(persistent.cg_page + 1 if persistent.cg_page and persistent.cg_page < mx else None)

screen cg():

    tag menu
    use game_menu(_("CG")):

        fixed:
            order_reverse True

            $ page = int(persistent.cg_page) - 1
            $ rows = 2
            $ cols = 3 if page < 3 else 2

            grid cols rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(cols * rows):
                    $ slot = page * 6 + i + 1
                    $ s = "cg %d" % slot
                    button:
                        if getattr(persistent, 'cg_unlocked_%d' % slot):
                            action Function(renpy.show_screen, 'replay_cg', which=slot)
                        else:
                            action Function(renpy.show_screen, 'alert', message=globals()['cg_hint_%d' % slot])

                        has vbox

                        if getattr(persistent, 'cg_unlocked_%d' % slot):
                            add ImageReference(s + " thumbnail") xalign 0.5
                        else:
                            add ImageReference("cg locked") xalign 0.5

                for i in range(cols * rows):
                    $ slot = page * 6 + i + 1

            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton "<" action CGPagePrevious()

                for page in range(1, 5):
                    textbutton "[page]" action CGPage(page)

                textbutton ">" action CGPageNext(4)

################################################################################
## End List
################################################################################

init python:
    persistent.ed_page = persistent.ed_page or 1

    class EDPage(Action):
        def __init__(self, page):
            self.page = page

        def __call__(self):
            if not self.get_sensitive():
                return

            persistent.ed_page = self.page
            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page is not None and self.page != persistent.ed_page

    class EDPagePrevious(EDPage):
        def __init__(self):
            super(EDPagePrevious, self).__init__(persistent.ed_page - 1 if persistent.ed_page and persistent.ed_page > 1 else None)

    class EDPageNext(EDPage):
        def __init__(self, mx):
            super(EDPageNext, self).__init__(persistent.ed_page + 1 if persistent.ed_page and persistent.ed_page < mx else None)


screen ed():

    tag menu
    use game_menu(_("Endings")):

        fixed:
            order_reverse True

            $ persistent.ed_page = 1
            $ page = int(persistent.ed_page) - 1

            grid 3 2:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(3):
                    $ slot = 0 * 6 + i + 1
                    $ s = "ed %d thumbnail" % slot
                    button:
                        if getattr(persistent, 'ed_unlocked_%d' % slot):
                            action Replay('end_%d' % slot)
                        else:
                            action Function(renpy.show_screen, 'alert', message=globals()['ed_hint_%d' % slot])

                        has vbox

                        if getattr(persistent, 'ed_unlocked_%d' % slot):
                            add ImageReference(s) xalign 0.5
                            text globals()['ed_title_%d' % slot] style "slot_time_text"
                        else:
                            add ImageReference("ed locked") xalign 0.5
                            text _("???") style "slot_time_text"

                for i in range(3):
                    vbox

            grid 2 2:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(2):
                    vbox

                for i in range(3, 5):
                    $ slot = 0 * 6 + i + 1
                    $ s = "ed %d thumbnail" % slot
                    button:
                        if getattr(persistent, 'ed_unlocked_%d' % slot):
                            action Replay('end_%d' % slot)
                        else:
                            action Function(renpy.show_screen, 'alert', message=globals()['ed_hint_%d' % slot])

                        has vbox

                        if getattr(persistent, 'ed_unlocked_%d' % slot):
                            add ImageReference(s) xalign 0.5
                            text globals()['ed_title_%d' % slot] style "slot_time_text"
                        else:
                            add ImageReference("ed locked") xalign 0.5
                            text _("???") style "slot_time_text"


            #hbox:
                #style_prefix "page"

                #xalign 0.5
                #yalign 1.0

                #spacing gui.page_spacing

                #textbutton "<" action EDPagePrevious()

                #for page in range(1, 2):
                    #textbutton "[page]" action EDPage(page)

                #textbutton ">" action EDPageNext(1)

################################################################################
## Music Room
################################################################################

screen music_room():

    tag menu
    use game_menu(_("Music")):
        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"

            hbox:
                vbox xsize 700:
                    for tag, author, file in tracks[:9]:
                        textbutton tag action mr.Play(file) ymaximum 53
                vbox xsize 700:
                    for tag, author, file in tracks[9:]:
                        textbutton tag action mr.Play(file) ymaximum 53

            null height 40
            hbox:
                text _("Now Playing")
                null width 40
                text [tag for tag, author, file in tracks if renpy.music.get_playing('music').replace('_loop.', '_intro.') == file][0]:
                    color gui.selected_color
                null width 40
                text '(' + __([author for tag, author, file in tracks if renpy.music.get_playing('music').replace('_loop.', '_intro.') == file][0]) + ')'

        on "replace" action mr.Play()

################################################################################
## Combination Lock
################################################################################
default combination_lock = [0, 0, 0, 0]
init python:
    correct_combination = [1, 3, 0, 7]

    class LockButtonAction(Action):
        def __call__(self):
            combination_lock[self.slot] = (combination_lock[self.slot] + self.offset + 10) % 10
            renpy.restart_interaction()

        def get_sensitive(self):
            return True

    class LockDown(LockButtonAction):
        def __init__(self, slot):
            self.slot = slot
            self.offset = -1

    class LockUp(LockButtonAction):
        def __init__(self, slot):
            self.slot = slot
            self.offset = 1

screen lock_buttons():
    fixed xalign 0.5 yalign 0.5 xsize 1480 ysize 699:
        frame:
            background "images/combo_lock/pane.png"
            hbox:
                vbox:
                    fixed xsize 380 ysize 192
                    fixed xsize 380 ysize 314:
                        imagebutton auto 'images/combo_lock/button %s.png' xalign 0.5:
                            focus_mask 'images/combo_lock/button idle.png'
                            if lock_active:
                                if combination_lock == correct_combination:
                                    action Jump('combination_lock_correct')
                                else:
                                    action Jump('combination_lock_wrong')
                    fixed xsize 380 ysize 193
                vbox xpos -17:
                    fixed xsize 273 ysize 25
                    fixed xsize 273 ysize 138:
                        imagebutton auto 'images/combo_lock/arrow up %s.png':
                            focus_mask 'images/combo_lock/arrow up hover.png'
                            if lock_active:
                                action LockUp(0)
                    fixed xsize 273 ysize 356:
                        image 'images/combo_lock/numbers/[combination_lock[0]].png' xalign 0.5 yalign 0.5
                    fixed xsize 273 ysize 138:
                        imagebutton auto 'images/combo_lock/arrow down %s.png':
                            focus_mask 'images/combo_lock/arrow down hover.png'
                            if lock_active:
                                action LockDown(0)
                vbox xpos -25:
                    fixed xsize 273 ysize 25
                    fixed xsize 273 ysize 138:
                        imagebutton auto 'images/combo_lock/arrow up %s.png':
                            focus_mask 'images/combo_lock/arrow up hover.png'
                            if lock_active:
                                action LockUp(1)
                    fixed xsize 273 ysize 356:
                        image 'images/combo_lock/numbers/[combination_lock[1]].png' xalign 0.5 yalign 0.5
                    fixed xsize 273 ysize 138:
                        imagebutton auto 'images/combo_lock/arrow down %s.png':
                            focus_mask 'images/combo_lock/arrow down hover.png'
                            if lock_active:
                                action LockDown(1)
                vbox xpos -34:
                    fixed xsize 273 ysize 25
                    fixed xsize 273 ysize 138:
                        imagebutton auto 'images/combo_lock/arrow up %s.png':
                            focus_mask 'images/combo_lock/arrow up hover.png'
                            if lock_active:
                                action LockUp(2)
                    fixed xsize 273 ysize 356:
                        image 'images/combo_lock/numbers/[combination_lock[2]].png' xalign 0.5 yalign 0.5
                    fixed xsize 273 ysize 138:
                        imagebutton auto 'images/combo_lock/arrow down %s.png':
                            focus_mask 'images/combo_lock/arrow down hover.png'
                            if lock_active:
                                action LockDown(2)
                vbox xpos -40:
                    fixed xsize 273 ysize 25
                    fixed xsize 273 ysize 138:
                        imagebutton auto 'images/combo_lock/arrow up %s.png':
                            focus_mask 'images/combo_lock/arrow up hover.png'
                            if lock_active:
                                action LockUp(3)
                    fixed xsize 273 ysize 356:
                        image 'images/combo_lock/numbers/[combination_lock[3]].png' xalign 0.5 yalign 0.5
                    fixed xsize 273 ysize 138:
                        imagebutton auto 'images/combo_lock/arrow down %s.png':
                            focus_mask 'images/combo_lock/arrow down hover.png'
                            if lock_active:
                                action LockDown(3)

default lock_active = False

################################################################################
## Map
################################################################################
screen map_buttons():
    vbox xalign 0.5 yalign 0.1:
        imagebutton auto 'images/stamp %s.png':
            if map_active:
                action Jump("map_choice1")

    vbox xalign 0.2 yalign 0.8:
        imagebutton auto 'images/stamp %s.png':
            if map_active:
                action Jump("map_choice2")

    vbox xalign 0.8 yalign 0.8:
        imagebutton auto 'images/stamp %s.png':
            if map_active:
                action Jump("map_choice3")

default map_active = False
