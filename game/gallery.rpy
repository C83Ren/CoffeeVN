init +1 python:
    g = Gallery()

    for i in range(10):
        g.button("cg %d" % (i + 1))
        g.condition("persistent.cg_unlocked_%d" % (i + 1))
        g.image(ImageReference("cg %d" % (i + 1)))

init +2 python:
    for i in range(10):
        renpy.image("cg %d thumbnail" % (i + 1), im.Scale(ImageReference("cg %d unscaled" % (i + 1)), 384, 216))
    renpy.image("cg locked", im.Scale(Image("cg locked.png"), 384, 216))

label show_cg(which):
    $ i = cg_list.index(which) + 1
    $ _which_cg = which
    $ setattr(persistent, 'cg_unlocked_%d' % i, True)
    image cg = "cg [i]"
    scene cg

    $ quick_menu = False
    with Dissolve(0.5)
    pause
    $ quick_menu = True

    return

