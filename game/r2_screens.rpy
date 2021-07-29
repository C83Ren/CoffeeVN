# Screen for r2

screen village_map():
    add "r2_maps/r2_village/village.png"

    imagebutton auto 'images/r2_maps/talk ' + str(_preferences.language) + ' %s.png':
        xpos 94
        ypos 73
        action Jump ("village_talk")

    imagebutton auto "images/r2_maps/r2_village/house1_%s.png":
        xpos 81
        ypos 519
        action Jump ("village_house_1")

    imagebutton auto "images/r2_maps/r2_village/house1_%s.png":
        xpos 895
        ypos 101
        action Jump ("village_house_2")

    imagebutton auto "images/r2_maps/r2_village/house2_%s.png":
        xpos 1104
        ypos 594
        action Jump ("village_house_3")

    imagebutton auto "images/r2_maps/r2_village/house1_%s.png":
        xpos 1648
        ypos 660
        action Jump ("village_house_4")

    imagebutton auto "images/r2_maps/r2_village/announcement_%s.png":
        xpos 1620
        ypos 350
        action Jump ("village_announcement")

    if v_house4 > 0:
        imagebutton auto "arrow/arrow_up_%s.png":
            xpos 478
            ypos 118
            action Jump ("r2_map_2")

screen turmoil_map():
    add "r2_maps/r2_turmoil/turmoil.png"

    imagebutton auto "images/r2_maps/r2_turmoil/pillar_%s.png":
        xpos 659
        ypos 648
        action Jump ("turmoil_pillar")

    imagebutton auto "images/r2_maps/r2_turmoil/pillar_%s.png":
        xpos 659
        ypos 162
        action Jump ("turmoil_pillar")

    imagebutton auto "images/r2_maps/r2_turmoil/pillar_%s.png":
        xpos 1150
        ypos 650
        action Jump ("turmoil_pillar")

    imagebutton auto "images/r2_maps/r2_turmoil/pillar_%s.png":
        xpos 1150
        ypos 162
        action Jump ("turmoil_pillar")

    imagebutton auto "images/r2_maps/r2_turmoil/tablet_%s.png":
        xpos 846
        ypos 460
        action Jump ("turmoil_tablet")

    imagebutton auto "images/arrow/arrow_down_%s.png":
        xpos 900
        ypos 900
        action Jump ("turmoil_world_map")

screen forest_map():
    add "images/r2_maps/r2_forest/forest.png"

    imagebutton auto "images/r2_maps/r2_forest/hut1_%s.png":
        xpos 555
        ypos 321
        action Jump ("forest_hut_1")

    imagebutton auto "images/r2_maps/r2_forest/hut2_%s.png":
        xpos 1380
        ypos 570
        action Jump ("forest_hut_2")

    imagebutton auto "images/r2_maps/r2_forest/tree_%s.png":
        xpos 381
        ypos 673
        action Jump ("forest_spot_2")

    imagebutton auto "images/r2_maps/r2_forest/bush_%s.png":
        xpos 465
        ypos 282
        action Jump ("forest_spot_1")

    imagebutton auto "images/arrow/arrow_up_%s.png":
        xpos 1140
        ypos 99
        action Jump ("forest_exit")

screen world_map():
    add "r2_maps/r2_world_map/world_map.png"

    if v_house4 > 0:
        imagebutton auto 'images/r2_maps/talk ' + str(_preferences.language) + ' %s.png':
            xpos 94
            ypos 73
            action Jump ("map_talk")

        imagebutton auto "images/r2_maps/r2_world_map/village_%s.png":
            xpos 141
            ypos 817
            action Jump ("village_menu")

        imagebutton auto "images/r2_maps/r2_world_map/tranquility_%s.png":
            xpos 0
            ypos 335
            action Jump ("map_tranquility")

        imagebutton auto "images/r2_maps/r2_world_map/turmoil_%s.png":
            xpos 937
            ypos 889
            action Jump ("map_turmoil")

        imagebutton auto "images/r2_maps/r2_world_map/rage_%s.png":
            xpos 1169
            ypos 180
            action Jump ("map_rage")

        imagebutton auto "images/r2_maps/r2_world_map/castle_%s.png":
            xpos 1695
            ypos 356
            action Jump ("map_castle")
    else:
        imagebutton auto "images/r2_maps/r2_world_map/village_%s.png":
            xpos 141
            ypos 817
            action Jump ("on_to_village")
