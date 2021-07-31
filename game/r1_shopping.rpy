init python:
    shoppingflag = None

label r1_shopping:
    scene bg shop with fade
    #bgm 星海

    if famresflag == 1:
        "I paid for the meal, and then we went to the shopping district."
    else:
        "We went to the shopping district."

    p "Ahh, walks are great."

    p "Nothing better than a nice walk after a nice... uhh... meal."

    "That meal really was something, all right."

    p "Don’t you think so too, Shiraishi?"

    show hitona1 bliss3 with dissolve

    s "Napping is also nice though..."

    p "You got a point..."

    "We walked around the shops."

    show hitona1 smile1

    p "{i}Now that I look closely, Shiraishi really looks like me, doesn’t she...{/i}"

    "Shiraishi suddenly stopped in front of a certain shop. It’s a costume shop."

    show hitona1 stareyes3

    "Shiraishi turned and looked at me with hopeful eyes."

    p "You want to try something on?"

    show hitona1 stareyes4

    s "Yes!"

    p "Okay, let’s go in!"

    hide hitona1

    "We wandered inside the store and looked at all sorts of costumes on show."

    "There were many outfits on display, such as nurse outfits, maid outfits, suits, and all sorts of dresses."

    p "{i}Now that we’re here... I want to dress Shiraishi up!!{/i}"

    "I am fired up!"

    p "Shiraishi!"

    show hitona1 smile1

    s "Hmmm?"

    p "How about we pick each other’s outfits!"

    show hitona1 stareyes3

    s "Really??"

    p "Yeah!"

    s "Okay!"

    hide hitona1 with dissolve

    "With that said, Shiraishi left on her own to pick an outfit for me."

    "For some reason I feel like I’ll regret that decision. But this is a chance to dress Shiraishi up!"

    "No way I’m letting this chance go!"

    "What would she look nice in... this is going to be hard."

    "Shiraishi is so pure and innocent, that a contrasting color might work well, like say... black!"

    "Yes, black is truly the perfect color for someone that pure!"

    "Maybe a goth lolita dress would look good."

    "A long black dress would also be dashing!"

    "Hmmm, but I want to emphasize her childishness as well..."

    p "{i}Oh! This might be it...!{/i}"

    window hide
    pause 1.0

    p "Shiraishi! Are you done choosing?"

    s "I’ve decided!"

    "Shiraishi was smiling and looking at... wedding outfits."

    show hitona1 stareyes4 with dissolve

    s "They look so beautiful!"

    p "Are you perhaps choosing a wedding dress for me?"

    s "Yes, Hitona onee-chan!"

    s "But I don’t know which one to pick, they all look so good!"

    "Suddenly, I got an idea..."

    p "Shiraishi, how about you let me choose from these?"

    s "Ehhh? But Shiraishi wanted to choose for Hitona onee-chan!"

    "I showed the outfit I picked for Shiraishi."

    show hitona1 stareyes1

    s "Oooh! It’s so cute!"

    p "Don’t worry, I’ll make sure to pick something as good as this, okay?"

    p "So just go and change into this first?"

    show hitona1 pout2

    s "If Hitona onee-chan says so..."

    hide hitona1 with dissolve

    "Shiraishi took the costume I picked and went to change."

    "She looks a bit upset, but I’ll show her what I can do!"

    menu:
        "Which outfit should I change into?"

        "Suit":
            $ shoppingflag = "suit"
            jump r1_shopping_suit

        "Dress":
            $ shoppingflag = "dress"
            jump r1_shopping_dress

label r1_shopping_suit:
    "I picked up a black suit and changed into it."

    "After changing, I found Shiraishi standing in front of another changing room."

    "It seems that she has not changed her clothes yet."

    show hitona1 idle2 with dissolve

    "Well, it doesn’t seem like she noticed me yet."

    "I prepared my deeper voice and called out to her."

    p "Hello, little kitten~. Did you wait long?"

    "Shiraishi looked at me."

    "She seemed puzzled at first, but soon understood."

    show hitona1 stareyes1

    s "Hitona onee-chan?!"

    p "Was I so cool that you lost your memory?"

    "Shiraishi looks amused."

    "Using this voice hurts my throat a bit, so I dropped the act."

    p "How was it?"

    s "Hitona onee-chan is so cool!"

    p "Right~?"

    p "Did I make your heart skip a beat?"

    s "You did!"

    s "Shiraishi was really surprised!"

    p "I wanted to surprise Shiraishi a bit, so I’m glad it worked!"

    s "Shiraishi wants to be patted!"

    "I decided to go along with her sudden request, and patted her head."

    show hitona1 bliss3

    "Shiraishi looked really happy, so I decided to continue for a while."

    jump r1_regret_choice

label r1_shopping_dress:
    "I picked up a beautiful wedding dress, and went into a changing room."

    "After changing, I met up with Shiraishi again, and..."

    scene cg hitonadress with Fade(1.0, 2.0, 1.0)
    $ renpy.pause(2.0)

    p "AAAAAAH!!! SHIRAISHI, YOU’RE SO CUUUTE!!!!"

    "Standing in front of the neighbouring changing room was Shiraishi, wearing the witch’s outfit I picked for her."

    "As expected, the black color emphasized her innocent appearance, while the witch outfit made her childishness shine even more!"

    p "{i}Ahh! She’s really so cute...{/i}"

    s "Hitona onee-chan is so beautiful..."

    p "Hehe, right!"

    p "I told you not to worry!"

    p "Don’t underestimate my fashion sense!"

    s "I want Hitona onee-chan to pick all of my outfits from now on!"

    p "Haha that’s a bit much."

    p "But still... Shiraishi you look so CUUUTE!"

    "Shiraishi clinged on my arm as we looked into the mirror."

    s "Ehehehe."

    "Seeing Shiraishi so happy, I couldn’t help but smile."

    jump r1_regret_choice
