init python:

    def store_turn(list, object):

        atk = list[object][0]
        heal = list[object][1]
        if renpy.random.randint(1,10) <= list[object][2]:
            burn = 5
        else:
            burn = 0
        if renpy.random.randint(1,10) <= list[object][3]:
            par = 2
        else:
             par = 0
        return atk, heal, burn, par

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
    "Wind Blast": [10, 0, 0, 0],
    "Wind Cutter": [15, 0, 0, 0],
    "Fire Ball": [10, 0, 2, 0],
    "Electric Bolt": [8, 0, 0, 2],
    "Wind Lance": [20, 0, 0, 0],
    "Fire Wall": [15, 0, 5, 0],
    "Lightning Strike": [12, 0, 0, 5]
    }

    item_list = {
    "Heal Orb": [0, 20, 0, 0],
    "Flamethrower": [50, 0, 5, 0],
    "Heal Aura": [0, 50, 0, 0],
    "God Blessing": [0, 100, 0, 0],
    "Paralyzing Spark": [30, 0, 0, 5]
    }

    hitona_stats = {
    "name": "Hitona",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Blast"],
    "item": [],
    "burn": 0,
    "par": 0
    }

    eve_stats = {
    "name": "Eve",
    "hp": 300,
    "hp_max": 300,
    "spell": ["Wind Blast", "Fire Ball"],
    "item": ["Heal Orb"],
    "burn": 0,
    "par": 0
    }

    soldier1_stats = {
    "name": "Soldier 1",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Blast"],
    "item": ["Heal Orb"],
    "burn": 0,
    "par": 0
    }

    soldier2_stats = {
    "name": "Soldier 1",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Blast", "Fire Ball"],
    "item": ["Heal Orb", "Paralyzing Spark"],
    "burn": 0,
    "par": 0
    }

    soldier3_stats = {
    "name": "Soldier 2",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Cutter", "Electric Bolt"],
    "item": ["Heal Orb", "God Blessing"],
    "burn": 0,
    "par": 0
    }

    king_stats = {
    "name": "King Achnost",
    "hp": 500,
    "hp_max": 500,
    "spell": ["Wind Lance", "Fire Wall", "Lightning Strike"],
    "item": ["God Blessing", "Flamethrower", "Paralyzing Spark"],
    "burn": 0,
    "par": 0
    }

    multiplier_list = [0.5, 1, 2]
    hitona_hp = hitona_stats["hp"]

screen single_stat(name, hp, hp_max, xalign):

    frame:
        xalign xalign

        vbox:
            spacing 5

            hbox:
                text "[name!t]" min_width 220

            hbox:
                text _("HP"):
                    min_width 40
                    yalign 0.5

                bar:
                    value AnimatedValue(hp, hp_max, 1.0)
                    xmaximum 180
                    ysize 26

                text " [hp]/[hp_max]":
                    yalign 0.5
screen multi_stat:
    use single_stat("Hitona", hitona_stats["hp"], hitona_stats["hp_max"], 0.0)
    use single_stat("Eve", eve_stats["hp"], eve_stats["hp_max"], 0.3)
    $ screen_num = 0.6
    for enemies in enemy_list:
        use single_stat(enemies["name"], enemies["hp"], enemies["hp_max"], screen_num)
        $ screen_num = screen_num + 0.3

label r2_fight:
    show screen multi_stat
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
                            atk, heal, burn, par = store_turn(spell_list, spell_name)
                        else:
                            spell_name = renpy.random.choice(self["item"])
                            self["item"].remove(spell_name)
                            atk, heal, burn, par = store_turn(item_list, spell_name)
                    else:
                        spell_name = renpy.random.choice(self["spell"])
                        atk, heal, burn, par = store_turn(spell_list, spell_name)

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
    menu:
        "What to do?"
        "Spell":
            jump spell_option
        "Item":
            jump item_option

label spell_option:
    menu:
        "What spell to use?"
        "Wind Blast" if "Wind Blast" in hitona_stats["spell"]:
            $ spell_name = "Wind Blast"
        "Wind Cutter" if "Wind Cutter" in hitona_stats["spell"]:
            $ spell_name = "Wind Cutter"
        "Fire Ball" if "Fire Ball" in hitona_stats["spell"]:
            $ spell_name = "Fire Ball"
        "Electric Bolt" if "Electric Bolt" in hitona_stats["spell"]:
            $ spell_name = "Electric Bolt"
        "Wind Lance" if "Wind Lance" in hitona_stats["spell"]:
            $ spell_name = "Wind Lance"
        "Fire Wall" if "Fire Wall" in hitona_stats["spell"]:
            $ spell_name = "Fire Wall"
        "Lightning Strike" if "Lightning Strike" in hitona_stats["spell"]:
            $ spell_name = "Lightning Strike"
        "Cancel":
            jump fight_option

    $ atk, heal, burn, par = store_turn(spell_list, spell_name)

    jump target_option

label item_option:
    python:
        item_menu = []
        for z in hitona_stats["item"]:
            item_menu.append((z, z))

        item_menu.append(("Cancel", "cancel"))

        item_name = renpy.display_menu(item_menu)

        if item_name == "cancel":
            item_name = 0
            renpy.jump("fight_option")
        else:
            atk, heal, burn, par = store_turn(item_list, item_name)
            renpy.jump("target_option")


label target_option:
    python:
        enemy_menu1 = enemy_list[0]["name"]
        if len(enemy_list) == 2:
            enemy_menu2 = enemy_list[1]["name"]
        if len(enemy_list) == 3:
            enemy_menu2 = enemy_list[1]["name"]
            enemy_menu3 = enemy_list[2]["name"]

    menu:
        "Who are you targeting targeting?"
        "Hitona":
            $ target = hitona_stats
        "Eve" if eve_stats in ally_list:
            $ target = eve_stats
        "[enemy_menu1]":
            $ target = enemy_list[0]
        "[enemy_menu2]" if len(enemy_list) == 2:
            $ target = enemy_list[1]
        "[enemy_menu3]" if len(enemy_list) == 3:
            $ target = enemy_list[2]
        "Cancel":
            jump spell_option

    if atk > 0 and target != hitona_stats :
        jump rock_paper_scissor
    else:
         jump fight_log

label rock_paper_scissor:
    $ janken_list = ["rock", "paper", "scissor"]
    $ opp_janken = janken_list[renpy.random.randint(0,2)]
    menu:
        "Rock paper scissor!"
        "Rock":
            $ multiplier = janken("rock", opp_janken)
        "Paper":
            $ multiplier = janken("paper", opp_janken)
        "Scissor":
            $ multiplier = janken("scissor", opp_janken)
        "Cancel":
            jump target_option

    jump fight_log

label rock_paper_scissor_enemy:
    $ janken_list = ["rock", "paper", "scissor"]
    $ opp_janken = janken_list[renpy.random.randint(0,2)]
    $ self_name = self["name"]

    "[self_name] is targeting Hitona! Let's defend!"
    menu:
        "Rock paper scissor!"
        "Rock":
            $ multiplier = janken(opp_janken, "rock")
        "Paper":
            $ multiplier = janken(opp_janken, "paper")
        "Scissor":
            $ multiplier = janken(opp_janken, "scissor")

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
            show screen multi_stat
            "[target_name] received [atk] damage"
        else:
            $ target["hp"] = target["hp"] + heal
            if target["hp"] > target["hp_max"]:
                $ target["hp"] = target["hp_max"]
            show screen multi_stat
            "[target_name] is healed for [heal]"

        if burn > 0:
            $ target["burn"] = burn
            "[target_name] got burnt for the next 5 turns"

        if par > 0:
            $ target["par"] = par
            "[target_name] got paralyzed for the next 2 turns"

        if self["burn"] > 0:
            $ self["burn"] = self["burn"] - 1
            $ self["hp"] = self["hp"] - 5
            if self["hp"] < 0:
                $ self["hp"] = 0
            show screen multi_stat
            "[self_name] received 5 damage from burn status"
    else:
        $ self["par"] = self["par"] - 1
        "[self_name] is still paralyzed!"

        if self["burn"] > 0:
            $ self["burn"] = self["burn"] - 1
            $ self["hp"] = self["hp"] - 5
            if self["hp"] < 0:
                $ self["hp"] = 0
            show screen multi_stat
            "[self_name] received 5 damage from burn status"

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
