init +1 python:
    g = Gallery()

    for i in range(22):
        g.button("cg %d" % (i + 1))
        g.condition("persistent.cg_unlocked_%d" % (i + 1))
        g.image(ImageReference("cg %d" % (i + 1)))

init +2 python:
    for i in range(22):
        renpy.image("cg %d thumbnail" % (i + 1), im.Scale(ImageReference("cg %d unscaled" % (i + 1)), 384, 216))
    renpy.image("cg locked", im.Scale(Image("cg locked.png"), 384, 216))

transform cg_center:
    xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5

label show_cg(which, if_unlocked):
    $ i = cg_list.index(which) + 1
    $ _which_cg = which
    if if_unlocked and not getattr(persistent, 'cg_unlocked_%d' % i):
        return
    $ setattr(persistent, 'cg_unlocked_%d' % i, True)
    image cg:
        xsize 1920
        ysize 1080
        contains:
            "#000"
        contains:
            "cg [i]"
            cg_center
    scene cg

    $ quick_menu = False
    $ _skipping = False
    with Dissolve(0.5)
    pause
    $ quick_menu = True
    $ _skipping = True

    return


transform cg_fade_in:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

screen replay_cg(which):
    modal True
    button xpadding 0 ypadding 0:
        at cg_fade_in
        frame xsize 1920 ysize 1080 xpadding 0 ypadding 0:
            background "#000"
            image "cg [which]":
                xalign 0.5
                yalign 0.5
                xanchor 0.5
                yanchor 0.5
        action Function(renpy.hide_screen, "replay_cg")
    key "game_menu" action Function(renpy.hide_screen, "replay_cg")

