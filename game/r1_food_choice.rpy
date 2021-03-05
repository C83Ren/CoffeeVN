##(C83's comment: should we differ this scene into 2 seprate dialogue since it has bit diffrent dialogue I think...
label r1_food_choice_purikuri:
    jump r1_food_choice

label r1_food_choice_no_purikuri:
    jump r1_food_choice

label r1_food_choice:
    menu:
        "where to go?"
        "7/11":
            jump r1_7_11
        "family restaurant":
            jump r1_famres
