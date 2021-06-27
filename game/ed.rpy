init 0:
    image ed Placeholder = "gui/main_menu.png"

    image ed 1 = "ed Placeholder"
    define ed_title_1 = _("Support End")
    image ed 2 = "ed Placeholder"
    define ed_title_2 = _("Purikuri Bad End")
    image ed 3 = "ed Placeholder"
    define ed_title_3 = _("Home Bad End")
    image ed 4 = "ed Placeholder"
    define ed_title_4 = _("Movie Bad End")
    image ed 5 = "ed Placeholder"
    define ed_title_5 = _("Joy End")
    image ed 6 = "ed Placeholder"
    define ed_title_6 = _("Bad End 2-1")
    image ed 7 = "ed Placeholder"
    define ed_title_7 = _("Bad End 2-2")
    image ed 8 = "ed Placeholder"
    define ed_title_8 = _("Memories End")
    image ed 9 = "ed Placeholder"
    define ed_title_9 = _("Bad End 3-1")
    image ed 10 = "ed Placeholder"
    define ed_title_10 = _("Bad End 3-2")
    image ed 11 = "ed Placeholder"
    define ed_title_11 = _("Bad End 3-3")
    image ed 12 = "ed Placeholder"
    define ed_title_12 = _("Bad End 3-4")
    image ed 13 = "ed Placeholder"
    define ed_title_13 = _("Bad End 3-5")
    image ed 14 = "ed Placeholder"
    define ed_title_14 = _("True End")

init +1 python:
    for i in range(14):
        renpy.image("ed %d thumbnail" % (i + 1), im.Scale(ImageReference("ed %d" % (i + 1)), 384, 216))
    renpy.image("ed locked", im.Scale(Image("cg locked.png"), 384, 216))

