# game/battle_mechanic.rpy:384
translate simplified_chinese rock_paper_scissor_0e7c8ad7:

    # "Let's double the damage!"
    "ダメージを倍しよう！"

# game/battle_mechanic.rpy:392
translate simplified_chinese rock_paper_scissor_enemy_1c5d07bd:

    # "{color=#00c}[self_name]{/color} is targeting {color=#00c}Hitona{/color}! Let's defend!"
    "{color=#00c}[self_name!t]{/color}はひとなを狙っている！防御しよう！"

# game/battle_mechanic.rpy:414
translate simplified_chinese do_janken_85daf20e:

    # "You won! Damage taken has been halved!"
    "勝ち！受けたダメージが半分になった！"

# game/battle_mechanic.rpy:416
translate simplified_chinese do_janken_fa54bbe4:

    # "You lost! Damage taken has been doubled!"
    "負け！受けたダメージが倍された！"

# game/battle_mechanic.rpy:418
translate simplified_chinese do_janken_420e7190:

    # "It's a tie!"
    "引き分け！"

# game/battle_mechanic.rpy:422
translate simplified_chinese do_janken_f03ca9f7:

    # "You won! Damage dealt has been doubled!"
    "勝ち！与えたダメージが倍された！"

# game/battle_mechanic.rpy:424
translate simplified_chinese do_janken_3dece721:

    # "You lost! Damage dealt has been halved!"
    "負け！与えたダメージが半分になった！"

# game/battle_mechanic.rpy:426
translate simplified_chinese do_janken_420e7190_1:

    # "It's a tie!"
    "引き分け！"

# game/battle_mechanic.rpy:443
translate simplified_chinese fight_log_3c965ad1:

    # "{color=#00c}[self_name]{/color} casted {color=#909}[spell_name]{/color} on {color=#00c}[target_name]{/color}!"
    "{color=#00c}[self_name!t]{/color}が{color=#909}[spell_name!t]{/color}を{color=#00c}[target_name!t]{/color}にかけた！"

# game/battle_mechanic.rpy:455
translate simplified_chinese fight_log_a97f6bbd:

    # "{color=#00c}[target_name]{/color} took {color=#d00}[atk]{/color} damage!"
    $ fw_atk = to_full_width(atk)
    "{color=#00c}[target_name!t]{/color}が{color=#d00}[fw_atk]{/color}ダメージを受けた！"


# game/battle_mechanic.rpy:465
translate simplified_chinese fight_log_c0cbab48:

    # "{color=#00c}[target_name]{/color} has been healed {color=#090}[heal]{/color} HP!"
    $ fw_heal = to_full_width(heal)
    "{color=#00c}[target_name!t]{/color}はＨＰが{color=#090}[fw_heal]{/color}回復した！"

# game/battle_mechanic.rpy:474
translate simplified_chinese fight_log_47106935:

    # "{color=#00c}[target_name]{/color} got burnt for the next 5 turns!"
    "{color=#00c}[target_name!t]{/color}が５ターンで{color=#a30}《火傷》{/color}になった！"

# game/battle_mechanic.rpy:484
translate simplified_chinese fight_log_80481860:

    # "{color=#00c}[target_name]{/color} got paralyzed for the next 2 turns!"
    "{color=#00c}[target_name!t]{/color}が２ターンで{color=#a80}《麻痺》{/color}になった！"

# game/battle_mechanic.rpy:521
translate simplified_chinese fight_log_4db3e0b0_1:

    # "{color=#00c}[self_name]{/color} took {color=#d00}5{/color} damage from the burn!"
    "{color=#00c}[self_name!t]{/color}が{color=#a30}《火傷》{/color}の{color=#d00}５{/color}ダメージを受けた"

# game/battle_mechanic.rpy:506
translate simplified_chinese fight_log_e2b8eb5b:

    # "{color=#00c}[self_name]{/color} is still paralyzed!"
    "{color=#00c}[self_name!t]{/color}が{color=#a80}《麻痺》{/color}になっている！"

# game/battle_mechanic.rpy:518
translate simplified_chinese fight_log_4db3e0b0:

    # "{color=#00c}[self_name]{/color} took {color=#d00}5{/color} damage from the burn!"
    "{color=#00c}[self_name!t]{/color}が{color=#a30}《火傷》{/color}の{color=#d00}５{/color}ダメージを受けた"

# game/battle_mechanic.rpy:529
translate simplified_chinese fight_log_cf1d9358:

    # "{color=#00c}[target_name]{/color} has been defeated!"
    "{color=#00c}[target_name!t]{/color}が倒れた！"

# game/battle_mechanic.rpy:539
translate simplified_chinese fight_log_6abcf0dd:

    # "{color=#00c}[self_name]{/color} has been defeated!"
    "{color=#00c}[self_name!t]{/color}が倒れた！"

# game/battle_mechanic.rpy:542
translate simplified_chinese fight_fail_9e95cf3b:

    # "Having lost the fight, you’ve become unable to save the kingdom."
    "戦闘を負け、王国を救うことができなくなってしまった。"

translate simplified_chinese strings:

    # game/battle_mechanic.rpy:248
    old "It's {color=#00c}%s{/color}'s turn."
    new "{color=#00c}%s{/color}のターンだ。"

    # game/battle_mechanic.rpy:294
    old "What to do?"
    new "どうする？"

    # game/battle_mechanic.rpy:294
    old "Use Spell"
    new "魔法を使う"

    # game/battle_mechanic.rpy:294
    old "Use Item"
    new "アイテムを使う"

    # game/battle_mechanic.rpy:302
    old "What spell to use?"
    new "どんな魔法を使う？"

    # game/battle_mechanic.rpy:302
    old "Wind Blast"
    new "《爆風》"

    # game/battle_mechanic.rpy:302
    old "Wind Cutter"
    new "《鎌鼬》"

    # game/battle_mechanic.rpy:302
    old "Fire Ball"
    new "《火球》"

    # game/battle_mechanic.rpy:302
    old "Electric Bolt"
    new "《雷》"

    # game/battle_mechanic.rpy:302
    old "Wind Lance"
    new "《穿て旋風》"

    # game/battle_mechanic.rpy:302
    old "Fire Wall"
    new "《火の壁》"

    # game/battle_mechanic.rpy:302
    old "Lightning Strike"
    new "《落雷》"

    # game/battle_mechanic.rpy:329
    old "What item to use?"
    new "どんなアイテムを使う？"

    # game/battle_mechanic.rpy:329
    old "Heal Orb"
    new "《回復玉》"

    # game/battle_mechanic.rpy:329
    old "Flamethrower"
    new "《火炎放射器》"

    # game/battle_mechanic.rpy:329
    old "Heal Aura"
    new "《回復オーラ》"

    # game/battle_mechanic.rpy:329
    old "God Blessing"
    new "《神々の恵み》"

    # game/battle_mechanic.rpy:329
    old "Paralyzing Spark"
    new "《麻痺のスパーク》"

    # game/battle_mechanic.rpy:352
    old "Who are you targeting?"
    new "誰にかける？"

    # game/battle_mechanic.rpy:352
    old "Soldier 1"
    new "兵士１"

    # game/battle_mechanic.rpy:352
    old "Soldier 2"
    new "兵士２"

    # game/battle_mechanic.rpy:352
    old "King Achnost"
    new "アクノスト王"

    # game/battle_mechanic.rpy:376
    old "Attempt to double your damage by playing rock paper scissors?"
    new "じゃんけんでダメージを倍しようとする？"

init python:
    def to_full_width(n):
        return (''.join(list('０１２３４５６７８９')[int(x)] for x in str(n)))
