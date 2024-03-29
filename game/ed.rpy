init 0:
    image ed Placeholder = "images/sing room.png"

    image ed 1 = "images/bg playground.png"
    define ed_title_1 = _("Support End")
    define ed_hint_1 = _("Select {color=#00c}Support{/color} during the poll at the start of the game.")
    image ed 2 = "images/CG/grand_spell.png"
    define ed_title_2 = _("Joy End")
    define ed_hint_2 = _("Select {color=#00c}Joy{/color} during the poll at the start of the game.")
    image ed 3 = "images/CG/hitona_memory.png"
    define ed_title_3 = _("Memories End")
    define ed_hint_3 = _("Select {color=#00c}Memories{/color} during the poll at the start of the game.")
    image ed 4 = "images/CG/truehitona.png"
    define ed_title_4 = _("True End")
    define ed_hint_4 = _("Play through all three routes, then select {color=#00c}All of the above{/color}\nduring the poll at the start of the game.")
    image ed 5 = "images/rabbitco_endcard.png"
    define ed_title_5 = _("Extra")
    define ed_hint_5 = _("During the Memories route, escape the maze using the\nexit marked {color=#707}???{/color} instead of the normal exit.")

init +1 python:
    for i in range(5):
        renpy.image("ed %d thumbnail" % (i + 1), im.Scale(ImageReference("ed %d" % (i + 1)), 384, 216))
    renpy.image("ed locked", im.Scale(Image("cg locked.png"), 384, 216))

label bad_end:
    window hide
    $ _skipping = False
    if _preferences.language == 'simplified_chinese':
        show image 'images/bad_end_c.png' with dissolve
    else:
        show image 'images/bad_end.png' with dissolve
    $ renpy.pause(1.0, hard=True)
    pause
    $ _skipping = True
    return
