init python:
    g = Gallery()
    cg_list = ["bg map", "bg map", "BirthdayKohi", "bg map", "bg map", "bg map", "bg map", "bg map", "bg map", "bg map"]

    for i, cg in enumerate(cg_list):
        g.button("cg %d" % (i + 1))
        g.condition("persistent.cg_unlocked_%d" % (i + 1))
        g.image(Image("%s.png" % cg))
        g.transform(Transform(xzoom=0.5, yzoom=0.5))

init +1 python:
    for i, cg in enumerate(cg_list):
        renpy.image("cg %d thumbnail" % (i + 1), im.Scale(Image("%s.png" % cg), 384, 216))
    renpy.image("cg locked", im.Scale(Image("cg locked.png"), 384, 216))

label show_cg(which):
    $ i = cg_list.index(which)
    $ _which_cg = which
    $ setattr(persistent, 'cg_unlocked_%d' % (i + 1), True)
    image cg = "[_which_cg].png"
    scene cg:
        zoom 0.5

    $ quick_menu = False
    with Dissolve(0.5)
    pause
    $ quick_menu = True

    return

