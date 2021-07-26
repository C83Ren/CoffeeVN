init python:
    def store_turn(list, object):

        atk = list[object][0]
        heal = list[object][1]
        sfx = list[object][4]
        if renpy.random.randint(1,10) <= list[object][2]:
            burn = 5
        else:
            burn = 0
        if renpy.random.randint(1,10) <= list[object][3]:
            par = 2
        else:
             par = 0
        return atk, heal, burn, par, sfx

    def janken(player_janken, opp_janken):

        if player_janken == opp_janken:
            return float(1)
        elif player_janken == "rock" and opp_janken == "scissor":
            return float(2)
        elif player_janken == "scissor" and opp_janken == "paper":
            return float(2)
        elif player_janken == "paper" and opp_janken == "rock":
            return float(2)
        else:
            return float(0.5)

    #ATK, Heal, Burn, Paralyze
    spell_list = {
    "Wind Blast": [10, 0, 0, 0, "audio/sfx/wind_blast.mp3"],
    "Wind Cutter": [15, 0, 0, 0, "audio/sfx/wind_cutter.mp3"],
    "Fire Ball": [10, 0, 2, 0, "audio/sfx/fire_ball.mp3"],
    "Electric Bolt": [8, 0, 0, 2, "audio/sfx/electric_bolt.mp3"],
    "Wind Lance": [20, 0, 0, 0, "audio/sfx/wind_lance.mp3"],
    "Fire Wall": [15, 0, 5, 0, "audio/sfx/fire_wall.mp3"],
    "Lightning Strike": [12, 0, 0, 5, "audio/sfx/lightning_strike.mp3"]
    }

    item_list = {
    "Heal Orb": [0, 20, 0, 0, "audio/sfx/heal.mp3"],
    "Flamethrower": [50, 0, 5, 0, "audio/sfx/flamethrower.mp3"],
    "Heal Aura": [0, 50, 0, 0, "audio/sfx/heal.mp3"],
    "God Blessing": [0, 100, 0, 0, "audio/sfx/heal.mp3"],
    "Paralyzing Spark": [30, 0, 0, 5, "audio/sfx/paralyzing_spark.mp3"]
    }

    hitona_stats = {
    "name": "Hitona",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Blast"],
    "item": [],
    "burn": 0,
    "par": 0,
    "img":["images/kohi_r2/idle.png", "images/kohi_r2/hover.png"]
    }

    eve_stats = {
    "name": "Eve",
    "hp": 300,
    "hp_max": 300,
    "spell": ["Wind Blast", "Fire Ball"],
    "item": ["Heal Orb"],
    "burn": 0,
    "par": 0,
    "img":["images/kohi_r2/idle.png", "images/kohi_r2/hover.png"]
    }

    soldier1_stats = {
    "name": "Soldier 1",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Blast"],
    "item": ["Heal Orb"],
    "burn": 0,
    "par": 0,
    "img":["images/kohi_r2/idle.png", "images/kohi_r2/hover.png"]
    }

    soldier2_stats = {
    "name": "Soldier 1",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Blast", "Fire Ball"],
    "item": ["Heal Orb", "Paralyzing Spark"],
    "burn": 0,
    "par": 0,
    "img":["images/kohi_r2/idle.png", "images/kohi_r2/hover.png"]
    }

    soldier3_stats = {
    "name": "Soldier 2",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Cutter", "Electric Bolt"],
    "item": ["Heal Orb", "God Blessing"],
    "burn": 0,
    "par": 0,
    "img":["images/kohi_r2/idle.png", "images/kohi_r2/hover.png"]
    }

    king_stats = {
    "name": "King Achnost",
    "hp": 500,
    "hp_max": 500,
    "spell": ["Wind Lance", "Fire Wall", "Lightning Strike"],
    "item": ["God Blessing", "Flamethrower", "Paralyzing Spark"],
    "burn": 0,
    "par": 0,
    "img":["images/kohi_r2/idle.png", "images/kohi_r2/hover.png"]
    }

    multiplier_list = [0.5, 1, 2]
    hitona_hp = hitona_stats["hp"]

screen single_stat(name, hp, hp_max, ypos):
    frame xsize 400 ysize 110 xpadding 20 ypadding 13:
        ypos ypos

        vbox:
            hbox:
                text "[name!t]"

            hbox:
                text _("HP"):
                    min_width 40
                    yalign 0.5

                fixed xsize 6

                bar:
                    value AnimatedValue(hp, hp_max, 1.0)
                    xmaximum 180
                    ysize 26
                    yalign 0.5

                fixed xsize 6

                text " [hp]/[hp_max]":
                    yalign 0.5
                    if hp == hp_max:
                        color '#373'
                    elif float(hp) / hp_max > 0.5:
                        color '#131'
                    elif float(hp) / hp_max > 0.3333:
                        color '#bb0'
                    elif float(hp) / hp_max > 0.2:
                        color '#b70'
                    else:
                        color '#f00'
screen multi_stat():
    $ screen_num = 0
    use single_stat("Hitona", hitona_stats["hp"], hitona_stats["hp_max"], 0)
    hbox xalign 0.5 spacing 90:
        for someone in fight_list:
            use single_stat(someone["name"], someone["hp"], someone["hp_max"], 200)


screen single_sprite(image_name_idle, image_name_hover, stats):
    imagebutton:
        if stats == hit:
            idle Transform(Image(image_name_idle), zoom=0.8) at shake

        if stats["hp"] > 0:
            idle Transform(Image(image_name_idle), zoom=0.8,)
        else:
            idle Transform(Image(image_name_hover), zoom=0.8)

screen multi_sprite():
    hbox xalign 0.5 ypos 300:
        spacing 20
        for someone in fight_list:
            use single_sprite(someone["img"][0], someone["img"][1], someone)

screen battle_action():
    frame:
        xpadding 300
        ypadding 50
        xalign 0.5
        yalign 1.0
        vbox spacing 10:
            text "{b}What to do?{/b}"
            hbox spacing 30:
                textbutton "Spell" action Jump("spell_option")
                textbutton "Item" action Jump("item_option")

screen spell_action():
    frame:
        xpadding 300
        ypadding 50
        xalign 0.5
        yalign 1.0
        vbox spacing 10:
            text "{b}What spell to use?{/b}"
            for spell in hitona_stats["spell"]:
                textbutton spell action Call("load_spell", spell)
            textbutton "Cancel" action Jump("fight_option")

screen item_action():
    frame:
        xpadding 300
        ypadding 50
        xalign 0.5
        yalign 1.0
        vbox spacing 10:
            text "{b}What item to use?{/b}"
            for item in hitona_stats["item"]:
                textbutton item action Call("load_item", item)
            textbutton "Cancel":
                action Jump("fight_option")

screen target_action():
    frame:
        xpadding 300
        ypadding 50
        xalign 0.5
        yalign 1.0
        vbox spacing 10:
            text "{b}Who to target?{/b}"
            for someone in ally_list:
                textbutton someone["name"] action Call("target_option", someone)
            for someone in enemy_list:
                textbutton someone["name"] action Call("target_option", someone)
            textbutton "Cancel" action Jump("fight_option")

screen janken_action():
    frame:
        xpadding 300
        ypadding 50
        xalign 0.5
        yalign 1.0
        vbox spacing 10:
            text "{b}Rock Paper Scissor!{/b}"
            hbox spacing 30:
                textbutton "Rock" action Call("after_rock_paper_scissor", "rock")
                textbutton "Paper" action Call("after_rock_paper_scissor", "paper")
                textbutton "Scissor" action Call("after_rock_paper_scissor", "scissor")

screen janken_enemy_action():
    frame:
        xpadding 300
        ypadding 50
        xalign 0.5
        yalign 1.0
        vbox spacing 30:
            text "{b}Rock Paper Scissor!{/b}"
            hbox spacing 10:
                textbutton "Rock" action Call("after_rock_paper_scissor_enemy", "rock")
                textbutton "Paper" action Call("after_rock_paper_scissor_enemy", "paper")
                textbutton "Scissor" action Call("after_rock_paper_scissor_enemy", "scissor")

default hit = 0

label r2_fight:
    show screen multi_stat
    show screen multi_sprite
    python:
        item_name = 0
        if len(ally_list) > 0 and len(enemy_list) > 0:
            if x == 0:
                fight_order_temp = fight_order
                renpy.random.shuffle(fight_order_temp)
            if x < len(fight_order_temp) and fight_order_temp[x]["hp"] > 0:
                self = fight_order_temp[x]
                x = x + 1
                renpy.say(narrator, "It's " + self["name"] + " turn")
                if self["name"] == "Hitona":
                    renpy.jump("fight_option")
                else:
                    if len(self["item"]) > 0:
                        if renpy.random.randint(1,4) > 1:
                            spell_name = renpy.random.choice(self["spell"])
                            atk, heal, burn, par, sfx = store_turn(spell_list, spell_name)
                        else:
                            spell_name = renpy.random.choice(self["item"])
                            self["item"].remove(spell_name)
                            atk, heal, burn, par, sfx = store_turn(item_list, spell_name)
                    else:
                        spell_name = renpy.random.choice(self["spell"])
                        atk, heal, burn, par, sfx = store_turn(spell_list, spell_name)

                    if self["name"] == "Eve":
                        if atk > 0:
                            target = renpy.random.choice(enemy_list)
                            multiplier = renpy.random.choice(multiplier_list)
                        else:
                            target = renpy.random.choice(ally_list)

                    else:
                        if atk > 0:
                            target = renpy.random.choice(ally_list)
                            if target["name"] == "Hitona":
                                renpy.jump("rock_paper_scissor_enemy")
                            else:
                                multiplier = renpy.random.choice(multiplier_list)
                        else:
                            target = renpy.random.choice(enemy_list)
                    renpy.jump("fight_log")

            elif x >= len(fight_order_temp):
                x = 0
                renpy.jump("r2_fight")
        elif len(ally_list) == 0:
            renpy.jump("fight_fail")
        else:
            renpy.jump(fight_label)

label fight_option:
    $ item_name = 0
    call screen battle_action
    menu:
        "What to do?"
        "Spell":
            jump spell_option
        "Item":
            jump item_option

label spell_option:
    call screen spell_action

label load_spell(spell_name):
    $ atk, heal, burn, par, sfx = store_turn(spell_list, spell_name)
    call screen target_action

label item_option:
    call screen item_action

label load_item(item_name):
    $ atk, heal, burn, par, sfx = store_turn(item_list, item_name)
    call screen target_action

label target_option(stats):
    $ target = stats
    if atk > 0 and target != hitona_stats :
        jump rock_paper_scissor
    else:
         jump fight_log

label rock_paper_scissor:
    $ janken_list = ["rock", "paper", "scissor"]
    $ opp_janken = janken_list[renpy.random.randint(0,2)]
    "Let's double the damage!"
    call screen janken_action

label after_rock_paper_scissor(me_janken):
    $ multiplier = janken(me_janken, opp_janken)
    jump fight_log

label rock_paper_scissor_enemy:
    $ janken_list = ["rock", "paper", "scissor"]
    $ opp_janken = janken_list[renpy.random.randint(0,2)]
    $ self_name = self["name"]

    "[self_name] is targeting Hitona! Let's defend!"
    call screen janken_enemy_action

label after_rock_paper_scissor_enemy(me_janken):
    $ multiplier = janken(opp_janken, me_janken)
    jump fight_log

label fight_log:

    python:
        target_name = target["name"]
        self_name = self["name"]

    if self["par"] == 0:
        if item_name != 0:
            $ spell_name = item_name
            $ hitona_stats["item"].remove(spell_name)
            $ item_name = 0

        "[self_name] casted [spell_name] to [target_name]"

        if atk > 0:
            $ target["hp"] = target["hp"] - int((atk * multiplier))
            if target["hp"] < 0:
                $ target["hp"] = 0
            $ atk = int(atk * multiplier)
            $ hit = target
            show screen multi_stat
            play sound sfx
            "[target_name] received [atk] damage"
            $ hit = 0
        else:
            $ target["hp"] = target["hp"] + heal
            if target["hp"] > target["hp_max"]:
                $ target["hp"] = target["hp_max"]
            show screen multi_stat
            play sound sfx
            "[target_name] is healed for [heal]"

        if burn > 0:
            $ target["burn"] = burn
            play sound fireball
            $ hit = target
            play sound sfx
            "[target_name] got burnt for the next 5 turns"
            $ hit = 0

        if par > 0:
            $ target["par"] = par
            play sound paralyzingspark
            $ hit = target
            play sound sfx
            "[target_name] got paralyzed for the next 2 turns"
            $ hit = 0

        if self["burn"] > 0:
            $ self["burn"] = self["burn"] - 1
            $ self["hp"] = self["hp"] - 5
            if self["hp"] < 0:
                $ self["hp"] = 0
            show screen multi_stat
            play sound fireball
            $ hit = target
            "[self_name] received 5 damage from burn status"
            $ hit = 0
    else:
        $ self["par"] = self["par"] - 1
        play sound paralyzingspark
        "[self_name] is still paralyzed!"

        if self["burn"] > 0:
            $ self["burn"] = self["burn"] - 1
            $ self["hp"] = self["hp"] - 5
            if self["hp"] < 0:
                $ self["hp"] = 0
            show screen multi_stat
            play sound fireball
            $ hit = self
            "[self_name] received 5 damage from burn status"
            $ hit = 0

    if target["hp"] <= 0:
        if target in ally_list:
            $ ally_list.remove(target)
        else:
            $ enemy_list.remove(target)

        $ fight_order.remove(target)

        "[target_name] fainted!"

    if self["hp"] <= 0:
        if self in ally_list:
            $ ally_list.remove(self)
        else:
            $ enemy_list.remove(self)

        $ fight_order.remove(self)

        "[self_name] fainted!"

    jump r2_fight

label fight_fail:
    "You lost the fight, never to see the Kingdom save..."

    return
