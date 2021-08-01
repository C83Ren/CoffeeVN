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

label battle_mechanic_setup():
    #ATK, Heal, Burn, Paralyze
    $ spell_list = {
    "Wind Blast": [10, 0, 0, 0, "audio/sfx/wind_blast.mp3"],
    "Wind Cutter": [15, 0, 0, 0, "audio/sfx/wind_cutter.mp3"],
    "Fire Ball": [10, 0, 2, 0, "audio/sfx/fire_ball.mp3"],
    "Electric Bolt": [8, 0, 0, 2, "audio/sfx/electric_bolt.mp3"],
    "Wind Lance": [20, 0, 0, 0, "audio/sfx/wind_lance.mp3"],
    "Fire Wall": [15, 0, 5, 0, "audio/sfx/fire_wall.mp3"],
    "Lightning Strike": [12, 0, 0, 5, "audio/sfx/lightning_strike.mp3"]
    }

    $ item_list = {
    "Heal Orb": [0, 20, 0, 0, "audio/sfx/heal.mp3"],
    "Flamethrower": [50, 0, 5, 0, "audio/sfx/flamethrower.mp3"],
    "Heal Aura": [0, 50, 0, 0, "audio/sfx/heal.mp3"],
    "God Blessing": [0, 100, 0, 0, "audio/sfx/heal.mp3"],
    "Paralyzing Spark": [30, 0, 0, 5, "audio/sfx/paralyzing_spark.mp3"]
    }

    $ hitona_stats = {
    "name": "Hitona",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Blast"],
    "item": [],
    "burn": 0,
    "par": 0,
    "img":["images/kohi_r2/idle.png", "images/kohi_r2/ko.png", 200],
    "silent_death": False,
    }

    $ eve_stats = {
    "name": "Eve",
    "hp": 200,
    "hp_max": 200,
    "spell": ["Wind Blast", "Fire Ball"],
    "item": ["Heal Orb"],
    "burn": 0,
    "par": 0,
    "img":["images/kohi_r2/angry.png", "images/kohi_r2/ko.png", 200],
    "silent_death": False,
    }

    $ soldier1_stats = {
    "name": "Soldier",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Blast"],
    "item": ["Heal Orb"],
    "burn": 0,
    "par": 0,
    "img":["images/wizard_idle.png", "images/wizard_ko.png", 200],
    "silent_death": False,
    }

    $ soldier2_stats = {
    "name": "Soldier 1",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Blast", "Fire Ball"],
    "item": ["Heal Orb", "Paralyzing Spark"],
    "burn": 0,
    "par": 0,
    "img":["images/wizard_idle.png", "images/wizard_ko.png", 200],
    "silent_death": False,
    }

    $ soldier3_stats = {
    "name": "Soldier 2",
    "hp": 100,
    "hp_max": 100,
    "spell": ["Wind Cutter", "Electric Bolt"],
    "item": ["Heal Orb", "God Blessing"],
    "burn": 0,
    "par": 0,
    "img":["images/wizard_idle.png", "images/wizard_ko.png", 200],
    "silent_death": False,
    }

    $ king_stats = {
    "name": "King Achnost",
    "hp": 500,
    "hp_max": 500,
    "spell": ["Wind Lance", "Fire Wall", "Lightning Strike"],
    "item": ["God Blessing", "Flamethrower", "Paralyzing Spark", "Flamethrower", "Paralyzing Spark", "Paralyzing Spark", "Flamethrower"],
    "burn": 0,
    "par": 0,
    "img":["images/king_idle.png", "images/king_ko.png", 0],
    "silent_death": True,
    }

    $ multiplier_list = [0.5, 1, 2]
    $ janken_list = ["rock", "paper", "scissor"]
    $ hitona_hp = hitona_stats["hp"]
    $ item_name = 'Flamethrower'
    $ multiplier = 1.0
    $ ally_list = [hitona_stats, eve_stats]
    $ enemy_list = []
    $ fight_order = [hitona_stats, eve_stats]
    $ fight_order_temp = [hitona_stats, eve_stats]
    $ self = hitona_stats
    $ spell_name = 'Wind Lance'
    $ target = hitona_stats
    $ atk, heal, burn, par, sfx = 0, 0, 0, 0, "audio/sfx/fire_ball.mp3"
    $ my_janken = 'rock'
    $ self_name = 'Hitona'
    $ opp_janken = 'rock'
    $ hit = 0
    $ heal = 0
    $ x = 1
    return

screen single_stat(name, hp, hp_max, ypos):
    frame xsize 400 ysize 110 xpadding 20 ypadding 13:
        ypos ypos

        vbox:
            hbox:
                text "[name!t]"

            hbox:
                text "HP":
                    min_width 40
                    yalign 0.5

                fixed xsize 6

                bar:
                    value AnimatedValue(hp, hp_max, 1.0)
                    xmaximum 150
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
            use single_stat(someone["name"], someone["hp"], someone["hp_max"], someone["img"][2])


screen single_sprite(image_name_idle, image_name_hover, stats):
    imagebutton:
        if stats == hit:
            idle Transform(Image(image_name_idle), zoom=0.65) at shake

        if stats["hp"] > 0:
            idle Transform(Image(image_name_idle), zoom=0.65)
        else:
            idle Transform(Image(image_name_hover), zoom=0.65)

screen multi_sprite():
    hbox xalign 0.5 yalign 1.0:
        spacing 40
        for someone in fight_list:
            hbox yalign 1.0:
                use single_sprite(someone["img"][0], someone["img"][1], someone)

screen rps_picker():
    vbox xalign 0.5 yalign 0.1:
        imagebutton:
            idle 'images/rps/rock player idle.png'
            focus_mask 'images/rps/rock player idle.png'
            hover 'images/rps/rock player hover.png'
            action Call("handle_rps_pick", what="rock")

    vbox xalign 0.2 yalign 0.8:
        imagebutton:
            idle 'images/rps/paper player idle.png'
            focus_mask 'images/rps/paper player idle.png'
            hover 'images/rps/paper player hover.png'
            action Call("handle_rps_pick", what="paper")

    vbox xalign 0.8 yalign 0.8:
        imagebutton:
            idle 'images/rps/scissor player idle.png'
            focus_mask 'images/rps/scissor player idle.png'
            hover 'images/rps/scissor player hover.png'
            action Call("handle_rps_pick", what="scissor")

transform rps_before(left):
    truecenter rotate 0
    xoffset (-100 if left else 100)
    yoffset -100
    linear 0.2 truecenter rotate (90 if left else -90) xoffset 0 yoffset 0
    linear 0.2 truecenter rotate 0 xoffset (-100 if left else 100) yoffset -100
    pause 0.5
    linear 0.2 truecenter rotate (90 if left else -90) xoffset 0 yoffset 0
    linear 0.2 truecenter rotate 0 xoffset (-100 if left else 100) yoffset -100
    pause 0.5
    linear 0.1 truecenter rotate (30 if left else -30) xoffset (-50 if left else 50) yoffset -50
    alpha 0

transform rps_after(left):
    alpha 0
    pause 1.9
    alpha 1
    truecenter rotate (30 if left else -30)
    xoffset (-50 if left else 50)
    yoffset -50
    linear 0.1 truecenter rotate (60 if left else -60) xoffset 0 yoffset 0

screen rps_result(me, opp):
    vbox xalign 0.2 yalign 0.5:
        image 'images/rps/rock player idle.png' at rps_before(True)
    vbox xalign 0.2 yalign 0.5:
        image 'images/rps/' + me + ' player idle.png' at rps_after(True)
    vbox xalign 0.8 yalign 0.5:
        image 'images/rps/rock opponent idle.png' at rps_before(False)
    vbox xalign 0.8 yalign 0.5:
        image 'images/rps/' + opp + ' opponent idle.png' at rps_after(False)

default hit = 0

label r2_fight:
    show screen multi_stat
    show screen multi_sprite
    python:
        textbox_menu = True
        save_enabled = False
        item_name = 0
        multiplier = 1.0
        if len(ally_list) > 0 and len(enemy_list) > 0:
            if x == 0:
                fight_order_temp = fight_order
                renpy.random.shuffle(fight_order_temp)
            if x < len(fight_order_temp) and fight_order_temp[x]["hp"] > 0:
                self = fight_order_temp[x]
                x = x + 1
                renpy.say(narrator, __("It's {color=#00c}%s{/color}'s turn.") % __(self["name"]))
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
            textbox_menu = False
            save_enabled = True
            renpy.jump("fight_fail")
        else:
            textbox_menu = False
            save_enabled = True
            renpy.jump(fight_label)

label fight_option:
    $ item_name = 0
    menu:
        "What to do?"
        "Use Spell":
            jump spell_option
        "Use Item":
            jump item_option

label spell_option:
    menu:
        set set(spell_list.keys()).difference(hitona_stats["spell"])
        "What spell to use?"
        "Wind Blast":
            call load_spell("Wind Blast") from _call_load_spell
        "Wind Cutter":
            call load_spell("Wind Cutter") from _call_load_spell_1
        "Fire Ball":
            call load_spell("Fire Ball") from _call_load_spell_2
        "Electric Bolt":
            call load_spell("Electric Bolt") from _call_load_spell_3
        "Wind Lance":
            call load_spell("Wind Lance") from _call_load_spell_4
        "Fire Wall":
            call load_spell("Fire Wall") from _call_load_spell_5
        "Lightning Strike":
            call load_spell("Lightning Strike") from _call_load_spell_6
        "Cancel":
            jump fight_option
    jump target_action

label load_spell(spell):
    $ spell_name = spell
    $ atk, heal, burn, par, sfx = store_turn(spell_list, spell_name)
    return

label item_option:
    menu:
        set set(item_list.keys()).difference(hitona_stats["item"])
        "What item to use?"
        "Heal Orb":
            call load_item("Heal Orb") from _call_load_item
        "Flamethrower":
            call load_item("Flamethrower") from _call_load_item_1
        "Heal Aura":
            call load_item("Heal Aura") from _call_load_item_2
        "God Blessing":
            call load_item("God Blessing") from _call_load_item_3
        "Paralyzing Spark":
            call load_item("Paralyzing Spark") from _call_load_item_4
        "Cancel":
            jump fight_option
    jump target_action

label load_item(item):
    $ item_name = item
    $ atk, heal, burn, par, sfx = store_turn(item_list, item_name)
    return

label target_action:
    menu:
        set {"Hitona", "Eve", "Soldier", "Soldier 1", "Soldier 2", "King Achnost"}.difference([s["name"] for s in ally_list + enemy_list])
        "Who are you targeting?"
        "Hitona":
            $ target = [s for s in ally_list if s["name"] == "Hitona" ][0]
        "Eve":
            $ target = [s for s in ally_list if s["name"] == "Eve"][0]
        "Soldier":
            $ target = [s for s in enemy_list if s["name"] == "Soldier"][0]
        "Soldier 1":
            $ target = [s for s in enemy_list if s["name"] == "Soldier 1"][0]
        "Soldier 2":
            $ target = [s for s in enemy_list if s["name"] == "Soldier 2"][0]
        "King Achnost":
            $ target = [s for s in enemy_list if s["name"] == "King Achnost"][0]
        "Cancel":
            jump fight_option
    jump target_option

label target_option:
    if atk > 0 and target != hitona_stats :
        jump decide_rock_paper_scissor
    else:
        jump fight_log

label decide_rock_paper_scissor:
    menu:
        "Attempt to double your damage by playing rock paper scissors?"
        "Yes":
            jump rock_paper_scissor
        "No":
            jump fight_log

label rock_paper_scissor:
    "Let's double the damage!"
    call do_janken(False) from _call_do_janken
    jump fight_log

label rock_paper_scissor_enemy:
    $ self_name = self["name"]
    "{color=#00c}[self_name]{/color} is targeting {color=#00c}Hitona{/color}! Let's defend!"
    call do_janken(True) from _call_do_janken_1
    jump fight_log

label handle_rps_pick(what):
    $ my_janken = what
    return

label do_janken(reverse):
    $ opp_janken = janken_list[renpy.random.randint(0,2)]

    $ _skipping = False
    window hide
    show screen rps_picker with dissolve
    $ renpy.pause(hard=True)
    hide screen rps_picker
    $ _skipping = True

    show screen rps_result(my_janken, opp_janken)
    pause 2.3
    if reverse:
        $ multiplier = janken(opp_janken, my_janken)
        if multiplier < 1:
            "You won! Damage taken has been halved!"
        elif multiplier > 1:
            "You lost! Damage taken has been doubled!"
        else:
            "It's a tie!"
    else:
        $ multiplier = janken(my_janken, opp_janken)
        if multiplier > 1:
            "You won! Damage dealt has been doubled!"
        elif multiplier < 1:
            "You lost! Damage dealt has been halved!"
        else:
            "It's a tie!"
    hide screen rps_result
    return

label fight_log:
    python:
        target_name = target["name"]
        self_name = self["name"]

    if self["par"] == 0:
        if item_name != 0:
            $ spell_name = item_name
            $ hitona_stats["item"].remove(spell_name)
            $ item_name = 0

        "{color=#00c}[self_name]{/color} casted {color=#909}[spell_name]{/color} on {color=#00c}[target_name]{/color}!"

        if atk > 0:
            $ atk = min(target["hp"], int(atk * multiplier))
            $ target["hp"] = target["hp"] - atk
            $ hit = target
            show screen multi_stat
            window hide
            $ renpy.play(sfx, channel='sound')
            $ renpy.pause(2.0, hard=True)
            "{color=#00c}[target_name]{/color} took {color=#d00}[atk]{/color} damage!"
            $ hit = 0
        else:
            $ heal = min(target["hp_max"] - target["hp"], heal)
            $ target["hp"] = target["hp"] + heal
            show screen multi_stat
            window hide
            $ renpy.play(sfx, channel='sound')
            $ renpy.pause(2.0, hard=True)
            "{color=#00c}[target_name]{/color} has been healed {color=#090}[heal]{/color} HP!"

        if burn > 0 and target["hp"] > 0:
            $ target["burn"] = burn
            #play sound fireball
            $ hit = target
            window hide
            $ renpy.play(audio.fireball, channel='sound')
            $ renpy.pause(2.0, hard=True)
            "{color=#00c}[target_name]{/color} got burnt for the next 5 turns!"
            $ hit = 0

        if par > 0 and target["hp"] > 0:
            $ target["par"] = par
            #play sound paralyzingspark
            $ hit = target
            window hide
            $ renpy.play(audio.paralyzingspark, channel='sound')
            $ renpy.pause(delay=2.0, hard=True)
            "{color=#00c}[target_name]{/color} got paralyzed for the next 2 turns!"
            $ hit = 0

        if self["burn"] > 0:
            $ self["burn"] = self["burn"] - 1
            $ self["hp"] = self["hp"] - 5
            if self["hp"] < 0:
                $ self["hp"] = 0
            show screen multi_stat
            #play sound fireball
            window hide
            $ renpy.play(audio.fireball, channel='sound')
            $ renpy.pause(1.0, hard=True)
            $ hit = self
            "{color=#00c}[self_name]{/color} took {color=#d00}5{/color} damage from the burn!"
            $ hit = 0
    else:
        $ self["par"] = self["par"] - 1
        #play sound paralyzingspark
        window hide
        $ renpy.play(audio.paralyzingspark, channel='sound')
        $ renpy.pause(2.0, hard=True)
        "{color=#00c}[self_name]{/color} is still paralyzed!"

        if self["burn"] > 0:
            $ self["burn"] = self["burn"] - 1
            $ self["hp"] = self["hp"] - 5
            if self["hp"] < 0:
                $ self["hp"] = 0
            show screen multi_stat
            #play sound fireball
            $ renpy.play(audio.fireball, channel='sound')
            $ renpy.pause(2.0, hard=True)
            $ hit = self
            "{color=#00c}[self_name]{/color} took {color=#d00}5{/color} damage from the burn!"
            $ hit = 0

    if target["hp"] <= 0:
        if target in ally_list:
            $ ally_list.remove(target)
        else:
            $ enemy_list.remove(target)

        $ fight_order.remove(target)

        if not target["silent_death"]:
            "{color=#00c}[target_name]{/color} has been defeated!"

    if self["hp"] <= 0:
        if self in ally_list:
            $ ally_list.remove(self)
        else:
            $ enemy_list.remove(self)

        $ fight_order.remove(self)

        if not self["silent_death"]:
            "{color=#00c}[self_name]{/color} has been defeated!"

    jump r2_fight

label fight_fail:
    "Having lost the fight, you’ve become unable to save the kingdom."

    return
