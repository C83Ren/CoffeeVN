label before_main_menu:
    if persistent.ed_unlocked_4:
        $ renpy.music.play("audio/true_end.mp3", channel="music", loop=True)
    else:
        $ renpy.music.play("audio/Route_1_-_movie_theme.mp3", channel="music", loop=True)
    return

label start:
    call r1_purikuri_init() from _call_r1_purikuri_init
    call r1_7_11_init() from _call_r1_7_11_init
    call r1_famres_init() from _call_r1_famres_init
    call r1_movie_init() from _call_r1_movie_init
    call r1_shopping_init() from _call_r1_shopping_init
    call r1_regret_choice_init()
    call battle_mechanic_setup() from _call_battle_mechanic_setup
    call r2_forest_init() from _call_r2_forest_init
    call r2_village_init() from _call_r2_village_init
    call r2_map_init() from _call_r2_map_init
    call r2_tranquility_setup() from _call_r2_tranquility_setup
    call r2_final_init()
    call r3_start_init()
    call bomb_mechanic_init()
    call quiz_mechanic_init() from _call_quiz_mechanic_init
    call quiz_pic_mechanic_init() from _call_quiz_pic_mechanic_init
    call r3_river_init() from _call_r3_river_init
    call r3_bomb_init() from _call_r3_bomb_init

    scene bg room with dissolve
    play music room_bgm fadein 1.0
    #play music "room_bgm.wav"

    p "{i}Sigh…{/i}"

    p "{i}What a hot day today is… I’m all sweaty…I’ll have to take a bath again…{/i}"

    "It was Saturday afternoon. After a series of unfortunate events, I am now just lazing around in my room."

    p "{i}I mean, I was a bit hungry so I went to the convenience store to get some food, but the moment I stepped outside my house it started raining! The weather said it’s sunny today! Not to mention that speeding car that splashed mud all over me…{/i}"

    p "{i}…geez!{/i}"

    p "{i}And right when I thought that it couldn’t get any worse, I realized I was lost because of the huge downpour!{/i}"

    p "{i}After all that, I didn’t even get to buy my favourite chips and lunch! Ugh!{/i}"

    p "{i}…wait. It’s during these times that SSRs are pulled from gacha, right?{/i}"

    p "{i}Let’s pull!!!!{/i}"

    "But in the end, not even a single SR card came out."

    p "{i}Sigh…yeah right, what was I expecting…{/i}"

    p "{i}I want this terrible day to hurry up and end already…{/i}"

    "As soon as that thought came to mind…"

    play sound doorbell
    pause 1.0

    "…the doorbell rang."

    "???" "Hello! Delivery!"

    p "{i}A delivery? I wonder what it is.{/i}"

    "Mailman" "Here is your delivery. For ummm, Hitona Kohigashi, correct? Please sign here."

    p "Ah yes, okay…"

    "Just like that, a huge box was left at the front door."

    "On top of the box was a letter. I picked it up and read it."

    play sound takecard

    nvl_narrator "“Kohi!"

    nvl_narrator "You left this in your old room! Can’t believe you forgot to bring something so big! Be thankful that you have such a reliable senpai! Hope we can meet sometime!"

    nvl_narrator "Senpai”"

    nvl clear

    p "{i}So it was from senpai…it’s been quite a while since I last met her.{/i}"

    p "{i}But really, what is she talking about? I don’t think I would forget to bring something so huge…right?{/i}"

    p "{i}Well, let’s see what’s inside first.{/i}"

    p "{i}It’s a…safe?{/i}"

    "It was a silver-coloured safe with a 4-digit lock affixed to it."

    p "{i}Hmmm, I don’t think I ever had a safe like this.{/i}"

    p "{i}Let’s just bring this inside and ask senpai what it’s all about.{/i}"

    "Thinking that, I put the rather heavy safe inside and texted senpai asking about it."

    "After sending the text, I went back to lazing in my chair and staring blankly at the monitor."

    p "{i}What to do…{/i}"

    play sound messagetone

    "As soon I got lost in thought, a message came."

    "“Kohigashiii! I found an interesting questionnaire! Hurry up and try it!”"

    p "{i}Oh?{/i}"

    p "{i}That’s kinda rare and…random.{/i}"

    p "{i}Oh well, let’s try it.{/i}"

    "I opened the questionnaire linked."

    # disable save until after questionnaire
    $ save_enabled = False

    $ player_name = input_with_history("1. Enter your name.", default="Hitona")

    menu:
        "2. Of the following, what is your most favourite color?"
        "Purple":
            $ intro_color = "Purple"
        "Pink":
            $ intro_color = "Pink"
        "Yellow":
            $ intro_color = "Yellow"
        "Black":
            $ intro_color = "Black"
        "White":
            $ intro_color = "White"
        "Red":
            $ intro_color = "Red"
        "Blue":
            $ intro_color = "Blue"

    menu:
        "3. Of the following, which is your most favourite food?"
        "Pasta":
            $ intro_food = "Pasta"
        "Yakiniku":
            $ intro_food = "Yakiniku"
        "Salad":
            $ intro_food = "Salad"

    "The questions came one by one, never seeming to end."

    "10. Your favorite day of the year?"

    p "{i}There’s so many of them though…{/i}"

    "45. When do you think you’ll meet your soulmate?"

    p "{i}It’s asking me about the future now??{/i}"

    "70. What is your favourite movie genre?"

    p "{i}It asks this 70 questions in?!{/i}"

    "155. How much time do you spend each day sitting down?"

    p "{i}Really? What does this have to do with anything?? And 155 questions in??!{/i}"

    p "{i}Why am I even still doing this…{/i}"

    "Final question."

    p "{i}Finally…{/i}"

    menu:
        "Which of these do you treasure the most? (Warning: this option determines the game route.)"
        "Support":
            $ route = 1
        "Joy":
            $ route = 2
        "Memories":
            $ route = 3
        "All of them" if persistent.ed_unlocked_1 and persistent.ed_unlocked_2 and persistent.ed_unlocked_3:
            $ route = 4

    $ save_enabled = True

    p "{i}Finally done! What’s the result of this questionnaire?{/i}"

    if intro_color == "Purple":
        if intro_food == "Pasta":
            "“You are compassionate towards yourself. A good trait to have! It’s important to care for yourself.”"
        elif intro_food == "Yakiniku":
            "“You are compassionate towards everyone else. Your friends must be lucky to have you around.”"
        else:
            "“You are compassionate towards both yourself and others. It’s good to love everyone, yourself included.”"
    elif intro_color == "Pink":
        if intro_food == "Pasta":
            "“You think you are cute. Hey, no one is judging, and you really are cute!”"
        elif intro_food == "Yakiniku":
            "“You think everyone else is cute. A lot of people are cute on the outside, but you are able to see beyond that, and appreciate the cuteness within their hearts as well.”"
        else:
            "“You think everyone is cute. When everything in the world is cute, the world becomes a better place!”"
    elif intro_color == "Yellow":
        if intro_food == "Pasta":
            "“You are a cheerful person. Always looking forward to what you’re going to do next!”"
        elif intro_food == "Yakiniku":
            "“You are especially cheerful when around others. Like a bright ray of sunshine, you’re a blessing that everyone is grateful for.”"
        else:
            "“You are an infinite source of cheerfulness. Everyone around you immediately becomes cheerful just being near you. I have no idea how, but I want one of you right here in my home!”"
    elif intro_color == "Black":
        if intro_food == "Pasta":
            "“You think deeply about yourself. You often get lost in thought about matters pertaining to yourself.”"
        elif intro_food == "Yakiniku":
            "“You think deeply about the situations of others. You are prone to getting lost in thought when thinking about others but quick and decisive about your own affairs.”"
        else:
            "“You are a deep thinker. You enjoy thinking thoroughly about anything and everything. Be careful going too deep.”"
    elif intro_color == "White":
        if intro_food == "Pasta":
            "“You are an innocent person. No one in this world is more innocent than you. White as snow, just like a baby.”"
        elif intro_food == "Yakiniku":
            "“You believe that no one is truly guilty of anything. All actions are predetermined, thus no one can be guilty.”"
        else:
            "“You believe that everyone in this world is innocent. Of course, including yourself."
            "As long as everyone is able to forgive each other and not repeat their mistakes, the world will be as pure as the driven snow.”"
    elif intro_color == "Red":
        if intro_food == "Pasta":
            "“You are very ambitious about your goals. Nothing in this world can stop you once you start working.”"
        elif intro_food == "Yakiniku":
            "“You are very ambitious when supporting others. You stop at nothing to help those around you reach their goals.”"
        else:
            "“You are a very ambitious person. No matter what it is, you always want to give it 100%%, no, 200%% effort!”"
    else:
        if intro_food == "Pasta":
            "“You are a very calm person. When it involves you, you are able to think calmly without panicking, and quickly reach a solution without struggle.”"
        elif intro_food == "Yakiniku":
            "“You are very calm when it comes to the predicaments of others. You are able to solve their problems without breaking a sweat."
            "But the opposite is true when it comes to yourself. Perhaps it’s because you are putting yourself out of the equation?”"
        else:
            "“You are a very calm person. The most calm person in the world. Nothing in the world can perturb you.”"

    p "{i}…That’s it??? After all those questions, that’s it???? Give me back my time!{/i}"

    "I looked outside and the clock, and it was already midnight."

    p "{i}How did that questionnaire took so much time…uugh…I feel sleepy…{/i}"

    p "{i}I’ll just go sleep…{/i}"

    stop music fadeout 1.5
    play sound ["<silence 5.0 loop 5.0>", phonecall] loop
    scene bg room with Fade(2.0, 4.0, 3.0)

    p "{i}Uuugh…is it a call…ughh{/i}"

    "I picked up the phone; it was senpai calling."

    stop sound channel 0
    play music ["<silence 1.0 loop 1.0>", room_bgm] fadein 3.0

    p "…Hello…Morning…"

    sn "Kohiiii! Morniiing! Can you meet me at the park right now?"

    sn "There’s something I want to give you. Well, just hurry up and come! I’ll be waiting!"

    # TODO
    # beep beep beep

    p "{i}She hung up…I didn’t even get to say a single word…{/i}"

    "Senpai seemed very excited, but she didn’t reply to my message yesterday."

    p "{i}Well, might as well meet her and ask her directly.{/i}"

    "I got ready to go out and meet senpai."

    "Before leaving, I looked around the place a bit, and caught sight of the safe."

    p "{i}Sigh…{/i}"

    p "{i}Let’s go then!{/i}"

    play sound dooropen


    if route == 1:
        jump r1_start
    elif route == 2:
        stop music fadeout 1.0
        jump r2_start
    elif route == 3:
        jump r3_start
    else:
        jump true_end
