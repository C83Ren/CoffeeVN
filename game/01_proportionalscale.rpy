init python:
    def ProportionalScale(img, maxwidth, maxheight):
        currentwidth, currentheight = get_size(img)
        xscale = float(maxwidth) / float(currentwidth)
        yscale = float(maxheight) / float(currentheight)

        if xscale < yscale:
            minscale = xscale
        else:
            minscale = yscale

        return im.FactorScale(img,minscale,minscale)

