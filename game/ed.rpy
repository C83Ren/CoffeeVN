init 0:
    image ed Placeholder = "images/sing room.png"

    image ed 1 = "ed Placeholder"
    define ed_title_1 = _("Support End")
    image ed 2 = "ed Placeholder"
    define ed_title_2 = _("Joy End")
    image ed 3 = "ed Placeholder"
    define ed_title_3 = _("Memories End")
    image ed 4 = "ed Placeholder"
    define ed_title_4 = _("True End")

init +1 python:
    for i in range(4):
        renpy.image("ed %d thumbnail" % (i + 1), im.Scale(ImageReference("ed %d" % (i + 1)), 384, 216))
    renpy.image("ed locked", im.Scale(Image("cg locked.png"), 384, 216))

