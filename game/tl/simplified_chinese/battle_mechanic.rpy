# game/battle_mechanic.rpy:384
translate simplified_chinese rock_paper_scissor_0e7c8ad7:

    # "Let's double the damage!"
    "让伤害翻倍吧！"

# game/battle_mechanic.rpy:392
translate simplified_chinese rock_paper_scissor_enemy_1c5d07bd:

    # "{color=#00c}[self_name]{/color} is targeting {color=#00c}Hitona{/color}! Let's defend!"
    "{color=#00c}[self_name!t]{/color}对人鱼发起了攻击！做好防御吧！"

# game/battle_mechanic.rpy:414
translate simplified_chinese do_janken_85daf20e:

    # "You won! Damage taken has been halved!"
    "赢了！受到的伤害减半！"

# game/battle_mechanic.rpy:416
translate simplified_chinese do_janken_fa54bbe4:

    # "You lost! Damage taken has been doubled!"
    "输了！受到的伤害加倍！"

# game/battle_mechanic.rpy:418
translate simplified_chinese do_janken_420e7190:

    # "It's a tie!"
    "平局！"

# game/battle_mechanic.rpy:422
translate simplified_chinese do_janken_f03ca9f7:

    # "You won! Damage dealt has been doubled!"
    "赢了！给予的伤害加倍！"

# game/battle_mechanic.rpy:424
translate simplified_chinese do_janken_3dece721:

    # "You lost! Damage dealt has been halved!"
    "输了！给予的伤害减半！"

# game/battle_mechanic.rpy:426
translate simplified_chinese do_janken_420e7190_1:

    # "It's a tie!"
    "平局！"

# game/battle_mechanic.rpy:443
translate simplified_chinese fight_log_3c965ad1:

    # "{color=#00c}[self_name]{/color} casted {color=#909}[spell_name]{/color} on {color=#00c}[target_name]{/color}!"
    "{color=#00c}[self_name!t]{/color}使用{color=#909}[spell_name!t]{/color}对{color=#00c}[target_name!t]{/color}进行了攻击！"

# game/battle_mechanic.rpy:455
translate simplified_chinese fight_log_a97f6bbd:

    # "{color=#00c}[target_name]{/color} took {color=#d00}[atk]{/color} damage!"
    $ fw_atk = to_full_width(atk)
    "{color=#00c}[target_name!t]{/color}受到了{color=#d00}[fw_atk]{/color}点伤害！"


# game/battle_mechanic.rpy:465
translate simplified_chinese fight_log_c0cbab48:

    # "{color=#00c}[target_name]{/color} has been healed {color=#090}[heal]{/color} HP!"
    $ fw_heal = to_full_width(heal)
    "{color=#00c}[target_name!t]{/color}回复了{color=#090}[fw_heal]{/color}点HP！"

# game/battle_mechanic.rpy:474
translate simplified_chinese fight_log_47106935:

    # "{color=#00c}[target_name]{/color} got burnt for the next 5 turns!"
    "{color=#00c}[target_name!t]{/color}被赋予了五回合的{color=#a30}《烧伤》{/color}状态！"

# game/battle_mechanic.rpy:484
translate simplified_chinese fight_log_80481860:

    # "{color=#00c}[target_name]{/color} got paralyzed for the next 2 turns!"
    "{color=#00c}[target_name!t]{/color}被赋予了两回合的{color=#a80}《麻痺》{/color}状态！"

# game/battle_mechanic.rpy:521
translate simplified_chinese fight_log_4db3e0b0_1:

    # "{color=#00c}[self_name]{/color} took {color=#d00}5{/color} damage from the burn!"
    "{color=#00c}[self_name!t]{/color}由于{color=#a30}《烧伤》{/color}受到了{color=#d00}５{/color}点伤害！"

# game/battle_mechanic.rpy:506
translate simplified_chinese fight_log_e2b8eb5b:

    # "{color=#00c}[self_name]{/color} is still paralyzed!"
    "{color=#00c}[self_name!t]{/color}正处于{color=#a80}《麻痺》{/color}状态！"

# game/battle_mechanic.rpy:518
translate simplified_chinese fight_log_4db3e0b0:

    # "{color=#00c}[self_name]{/color} took {color=#d00}5{/color} damage from the burn!"
    "{color=#00c}[self_name!t]{/color}由于{color=#a30}《火傷》{/color}受到了{color=#d00}５{/color}点伤害！"

# game/battle_mechanic.rpy:529
translate simplified_chinese fight_log_cf1d9358:

    # "{color=#00c}[target_name]{/color} has been defeated!"
    "{color=#00c}[target_name!t]{/color}倒下了！"

# game/battle_mechanic.rpy:539
translate simplified_chinese fight_log_6abcf0dd:

    # "{color=#00c}[self_name]{/color} has been defeated!"
    "{color=#00c}[self_name!t]{/color}倒下了！"

# game/battle_mechanic.rpy:542
translate simplified_chinese fight_fail_9e95cf3b:

    # "Having lost the fight, you’ve become unable to save the kingdom."
    "战斗失败，没能拯救王国。"

translate simplified_chinese strings:

    # game/battle_mechanic.rpy:248
    old "It's {color=#00c}%s{/color}'s turn."
    new "到{color=#00c}%s{/color}的回合了。"

    # game/battle_mechanic.rpy:294
    old "What to do?"
    new "要做什么？"

    # game/battle_mechanic.rpy:294
    old "Use Spell"
    new "使用魔法"

    # game/battle_mechanic.rpy:294
    old "Use Item"
    new "使用道具"

    # game/battle_mechanic.rpy:302
    old "What spell to use?"
    new "要使用哪种魔法？"

    # game/battle_mechanic.rpy:302
    old "Wind Blast"
    new "《暴风》"

    # game/battle_mechanic.rpy:302
    old "Wind Cutter"
    new "《风刃》"

    # game/battle_mechanic.rpy:302
    old "Fire Ball"
    new "《火球》"

    # game/battle_mechanic.rpy:302
    old "Electric Bolt"
    new "《雷击》"

    # game/battle_mechanic.rpy:302
    old "Wind Lance"
    new "《风之长枪》"

    # game/battle_mechanic.rpy:302
    old "Fire Wall"
    new "《火之围墙》"

    # game/battle_mechanic.rpy:302
    old "Lightning Strike"
    new "《落雷》"

    # game/battle_mechanic.rpy:329
    old "What item to use?"
    new "要使用哪个道具？"

    # game/battle_mechanic.rpy:329
    old "Heal Orb"
    new "《回复珠》"

    # game/battle_mechanic.rpy:329
    old "Flamethrower"
    new "《火焰喷射器》"

    # game/battle_mechanic.rpy:329
    old "Heal Aura"
    new "《回复灵光》"

    # game/battle_mechanic.rpy:329
    old "God Blessing"
    new "《诸神之恩赐》"

    # game/battle_mechanic.rpy:329
    old "Paralyzing Spark"
    new "《麻痹之电光》"

    # game/battle_mechanic.rpy:352
    old "Who are you targeting?"
    new "要对谁使用？"

    # game/battle_mechanic.rpy:352
    old "Soldier 1"
    new "士兵１"

    # game/battle_mechanic.rpy:352
    old "Soldier 2"
    new "士兵２"

    # game/battle_mechanic.rpy:352
    old "King Achnost"
    new "阿克诺斯特王"

    # game/battle_mechanic.rpy:376
    old "Attempt to double your damage by playing rock paper scissors?"
    new "要通过猜拳让伤害加倍吗？"

init python:
    def to_full_width(n):
        return (''.join(list('０１２３４５６７８９')[int(x)] for x in str(n)))
