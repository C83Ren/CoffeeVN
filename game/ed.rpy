init 0:
    image ed Placeholder = "gui/main_menu.png"

    image ed 1 = "ed Placeholder"
    define ed_title_1 = _("End 1")
    image ed 2 = "ed Placeholder"
    define ed_title_2 = _("End 2")
    image ed 3 = "ed Placeholder"
    define ed_title_3 = _("End 3")
    image ed 4 = "ed Placeholder"
    define ed_title_4 = _("True End")
    image ed 5 = "ed Placeholder"
    define ed_title_5 = _("Bad End 1")
    image ed 6 = "ed Placeholder"
    define ed_title_6 = _("Bad End 2")

init +1 python:
    for i in range(6):
        print(i)
        renpy.image("ed %d thumbnail" % (i + 1), im.Scale(ImageReference("ed %d" % (i + 1)), 384, 216))
    renpy.image("ed locked", im.Scale(Image("cg locked.png"), 384, 216))

