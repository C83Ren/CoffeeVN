init 0:
    image ed Placeholder = "images/sing room.png"

    image ed 1 = "images/bg playground.png"
    define ed_title_1 = _("Support End")
    image ed 2 = "images/CG/grand_spell.png"
    define ed_title_2 = _("Joy End")
    image ed 3 = "images/CG/hitona_memory.png"
    define ed_title_3 = _("Memories End")
    image ed 4 = "images/CG/truehitona.png"
    define ed_title_4 = _("True End")
    image ed 5 = "images/rabbitco_endcard.png"
    define ed_title_5 = _("Extra")

init +1 python:
    for i in range(5):
        renpy.image("ed %d thumbnail" % (i + 1), im.Scale(ImageReference("ed %d" % (i + 1)), 384, 216))
    renpy.image("ed locked", im.Scale(Image("cg locked.png"), 384, 216))

label bad_end:
    window hide
    $ _skipping = False
    show image 'images/bad_end.png' with dissolve
    $ renpy.pause(1.0, hard=True)
    pause
    $ _skipping = True
    return
