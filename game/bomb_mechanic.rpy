init:
    python:
        import time

        # This function will run a countdown of the given length. It will
        # be white until 5 seconds are left, and then red until 0 seconds are
        # left, and then will blink 0.0 when time is up.
        def countdown(st, at, length=0.0):

            remaining = length - st

            if remaining > 30.0:
                return Text("%.1f" % remaining, color="#fff", size=72), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=72), .1
            else:
                return anim.Blink(Text("0.0", color="#f00", size=72)), None

        maze1 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 2, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        maze2 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 3, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        maze3 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 3, 1, 0, 0, 0],
            [0, 2, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        maze4 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 3, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        def rotate(m, x, y):
            return list(zip(*m[::-1])), y, len(m) - x - 1

        def can_move_forward(m, x, y):
            return x > 0 and m[x - 1][y]

        def can_move_backward(m, x, y):
            return x < len(m) - 1 and m[x + 1][y]

        def can_move_left(m, x, y):
            return y > 0 and m[x][y - 1]

        def can_move_right(m, x, y):
            return y < len(m[0]) - 1 and m[x][y + 1]

        def move_forward(m, x, y):
            return m, x - 1, y

        def move_left(m, x, y):
            return rotate(m, x, y - 1)

        def move_right(m, x, y):
            return rotate(*rotate(*rotate(m, x, y + 1)))

        def move_backward(m, x, y):
            #m, x, y = rotate(m, x + 1, y)
            return rotate(*rotate(m, x + 1, y))

        def at_finish(m, x, y):
            return m[x][y] == 2

        def at_finish_secret(m, x, y):
            return m[x][y] == 3

    # Show a countdown for 10 seconds.
image countdown = DynamicDisplayable(countdown, length= 120)

label bomb_mechanic:
    play music bomb_bgm
    scene black

    python:
        maze_num = renpy.random.randint(1,4)
        if maze_num == 1:
            maze = maze1
            player_x, player_y = 17, 11
        elif maze_num == 2:
            maze = maze2
            player_x, player_y = 15, 2
        elif maze_num == 3:
            maze = maze3
            player_x, player_y = 11, 8
        else:
            maze = maze4
            player_x, player_y = 12, 7

    image bomb map = "images/maze/bomb map[maze_num].png"

    show bomb map:
        zoom 0.5, xalign 0.5, yalign 0.5
    "Memorize it well~"
    hide bomb map

    show countdown at Position(xalign=.1, yalign=.1)
    $ time_remain = 120

label bomb_choice:

    if time_remain <= 0:
        jump bomb_fail

    python:
        time_start = renpy.time.time()
        ui.timer(time_remain, ui.jumps("bomb_fail"))
        forward = 'yes' if can_move_forward(maze, player_x, player_y) else 'no'
        right = 'yes' if can_move_right(maze, player_x, player_y) else 'no'
        left = 'yes' if can_move_left(maze, player_x, player_y) else 'no'
        backward = 'yes' if can_move_backward(maze, player_x, player_y) else 'no'
        img_maze = "%s %s %s" % (forward, right, left)

    image bomb_maze = "images/maze/[img_maze].png"
    show bomb_maze behind countdown
    with dissolve

    menu:
        "forward" if forward == "yes":
             $ maze, player_x, player_y = move_forward(maze, player_x, player_y)
        "right" if right == "yes":
             $ maze, player_x, player_y = move_right(maze, player_x, player_y)
        "left" if left == "yes":
             $ maze, player_x, player_y = move_left(maze, player_x, player_y)
        "backward" if backward == "yes":
             $ maze, player_x, player_y = move_backward(maze, player_x, player_y)

    $ time_remain = time_remain - (renpy.time.time() - time_start)

    if at_finish(maze, player_x, player_y):
        hide countdown
        jump r3_river
    elif at_finish_secret(maze, player_x, player_y):
        hide countdown
        $ r3_secret = True
        jump r3_river
    else:
        jump bomb_choice

label bomb_start:
    menu:
        "Right":
            jump bomb_1_f
        "Left":
            jump bomb_8_f

label bomb_start_1:
    menu:
        "Straight":
            jump bomb_8_start
        "Left":
            pi "That's where we started Hitona!"

            pi "Let's find another way!"

            jump bomb_start

label bomb_start_8:
    menu:
        "Straight":
            jump bomb_1_start
        "Right":
            pi "That's where we started Hitona!"

            pi "Let's find another way!"

            jump bomb_start

label bomb_1_start:
    #hide countdown
    menu:
        "Right":
            jump bomb_2_1
        "Left":
            jump bomb_3_1
        "Straight":
            jump bomb_5_1
        "Back":
            jump bomb_start_1

label bomb_1_2:
    #hide countdown
    menu:
        "Right":
            jump bomb_5_1
        "Left":
            jump bomb_start_1
        "Straight":
            jump bomb_3_1
        "Back":
            jump bomb_2_1

label bomb_1_3:
    #hide countdown
    menu:
        "Right":
            jump bomb_start_1
        "Left":
            jump bomb_5_1
        "Straight":
            jump bomb_2_1
        "Back":
            jump bomb_3_1

label bomb_1_5:
    #hide countdown
    menu:
        "Right":
            jump bomb_3_1
        "Left":
            jump bomb_2_1
        "Straight":
            jump bomb_start_1
        "Back":
            jump bomb_5_1

label bomb_2_1:
    pi "It's a dead end..."

    pi "Let's go back quick"



label bomb_go_left:
    #hide countdown
    "..."
