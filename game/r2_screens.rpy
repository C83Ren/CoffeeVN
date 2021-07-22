# Screen for r2

screen village_map():
    add "r2_maps/r2_village/village.png"

    imagebutton:
        xpos 81
        ypos 519
        idle "r2_maps/r2_village/house1_idle.png"
        hover "r2_maps/r2_village/house1_hover.png"
        action Jump ("village_house_1")

    imagebutton:
        xpos 895
        ypos 101
        idle "r2_maps/r2_village/house2_idle.png"
        hover "r2_maps/r2_village/house2_hover.png"
        action Jump ("village_house_2")

    imagebutton:
        xpos 1104
        ypos 594
        idle "r2_maps/r2_village/house3_idle.png"
        hover "r2_maps/r2_village/house3_hover.png"
        action Jump ("village_house_3")

    imagebutton:
        xpos 1648
        ypos 660
        idle "r2_maps/r2_village/house1_idle.png"
        hover "r2_maps/r2_village/house1_hover.png"
        action Jump ("village_house_4")

    imagebutton:
        xpos 1620
        ypos 350
        idle "r2_maps/r2_village/announcement_idle.png"
        hover "r2_maps/r2_village/announcement_hover.png"
        action Jump ("village_announcement")

    if v_house4 > 0:
        imagebutton:
            xpos 478
            ypos 118
            idle "arrow/arrow_up_idle.png"
            hover "arrow/arrow_up_hover.png"
            action Jump ("r2_map_2")

screen turmoil_map():
    add "r2_maps/r2_turmoil/turmoil.png"

    imagebutton:
        xpos 659
        ypos 648
        idle "r2_maps/r2_turmoil/pillar_idle.png"
        hover "r2_maps/r2_turmoil/pillar_hover.png"
        action Jump ("turmoil_pillar")

    imagebutton:
        xpos 659
        ypos 162
        idle "r2_maps/r2_turmoil/pillar_idle.png"
        hover "r2_maps/r2_turmoil/pillar_hover.png"
        action Jump ("turmoil_pillar")

    imagebutton:
        xpos 1150
        ypos 650
        idle "r2_maps/r2_turmoil/pillar_idle.png"
        hover "r2_maps/r2_turmoil/pillar_hover.png"
        action Jump ("turmoil_pillar")

    imagebutton:
        xpos 1150
        ypos 162
        idle "r2_maps/r2_turmoil/pillar_idle.png"
        hover "r2_maps/r2_turmoil/pillar_hover.png"
        action Jump ("turmoil_pillar")

    imagebutton:
        xpos 846
        ypos 460
        idle "r2_maps/r2_turmoil/tablet_idle.png"
        hover "r2_maps/r2_turmoil/tablet_hover.png"
        action Jump ("turmoil_tablet")

    imagebutton:
        xpos 900
        ypos 900
        idle "arrow/arrow_down_idle.png"
        hover "arrow/arrow_down_hover.png"
        action Jump ("turmoil_world_map")
