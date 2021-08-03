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
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
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
            [0, 0, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
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

        def can_move_left(m, x, y):
            return y > 0 and m[x][y - 1]

        def can_move_right(m, x, y):
            return y < len(m[0]) - 1 and m[x][y + 1]

        def move_forward(m, x, y):
            return m, x - 1, y

        def turn_left(m, x, y):
            return rotate(m, x, y)

        def turn_right(m, x, y):
            return rotate(*rotate(*rotate(m, x, y)))

        def move_backward(m, x, y):
            #m, x, y = rotate(m, x + 1, y)
            return rotate(*rotate(m, x + 1, y))

        def at_finish(m, x, y):
            return m[x][y] == 2

        def at_finish_secret(m, x, y):
            return m[x][y] == 3

label bomb_mechanic_init():
    $ maze_num = 2
    $ maze = maze2
    $ player_x, player_y = 14, 2
    $ img_maze = 'yes yes yes'
    $ old_img_maze = 'yes yes yes'
    $ time_remain = 120
    $ sleep_time = 0
    $ bomb_choice_counter = 0
    $ time_start = 0
    $ forward = right = left = 'yes'
    $ time_now = 0
    return

screen bomb_movement(can_move_forward, time_left):
    imagebutton xalign 0.5 yalign 0.3:
        if can_move_forward == 'yes':
            idle 'images/maze/forward idle.png'
            action Call("handle_bomb_movement", what="forward")
        else:
            idle 'images/maze/forward disabled.png'
        focus_mask 'images/maze/forward idle.png'
        hover 'images/maze/forward hover.png'
    imagebutton xalign 0.2 yalign 0.7:
        idle 'images/maze/left idle.png'
        focus_mask 'images/maze/left idle.png'
        hover 'images/maze/left hover.png'
        action Call("handle_bomb_movement", what="left")
    imagebutton xalign 0.8 yalign 0.7:
        idle 'images/maze/right idle.png'
        focus_mask 'images/maze/right idle.png'
        hover 'images/maze/right hover.png'
        action Call("handle_bomb_movement", what="right")
    timer time_left action Jump("bomb_mechanic_exit")

# Show a countdown for 120 seconds.
image countdown = DynamicDisplayable(countdown, length=120)

label bomb_mechanic:
    scene black

    python:
        maze_num = renpy.random.randint(1,4)
        if not persistent.first_bomb_done:
            persistent.first_bomb_done = True
            maze_num = 2
        if maze_num == 1:
            maze = maze1
            player_x, player_y = 17, 11
        elif maze_num == 2:
            maze = maze2
            player_x, player_y = 14, 2
        elif maze_num == 3:
            maze = maze3
            player_x, player_y = 11, 8
        else:
            maze = maze4
            player_x, player_y = 12, 7
        img_maze = None

    image bomb map = "images/maze/bomb map[maze_num] " + str(_preferences.language) + ".png"

    play sound takecard
    $ _skipping = False
    show bomb map:
        zoom 0.75, xalign 0.5, yalign 0.5
    l "Memorize it well~"
    play sound takecard
    hide bomb map

    show countdown at Position(xalign=.1, yalign=.1)
    #$ _skipping = False
    $ time_remain = 120
    $ sleep_time = 0
    $ bomb_choice_counter = 0

label bomb_choice:

    if time_remain <= 0:
        jump bomb_mechanic_exit

    python:
        time_start = renpy.time.time()
        forward = 'yes' if can_move_forward(maze, player_x, player_y) else 'no'
        right = 'yes' if can_move_right(maze, player_x, player_y) else 'no'
        left = 'yes' if can_move_left(maze, player_x, player_y) else 'no'
        if img_maze:
            old_img_maze, img_maze = img_maze, "%s %s %s" % (forward, right, left)
        else:
            old_img_maze = img_maze = "%s %s %s" % (forward, right, left)
        if forward == 'yes' and maze[player_x - 1][player_y] > 1:
            img_maze = img_maze + ' final'

    play sound mazewalk

    image bomb_maze = "images/maze/[img_maze].png"
    show bomb_maze behind countdown:
        truecenter zoom 1.5
    if sleep_time > 0.6:
        $ renpy.transition(Fade(0.3, sleep_time - 0.6, 0.3))
    else:
        $ renpy.transition(Dissolve(sleep_time))
    $ renpy.pause(delay=sleep_time, hard=True)
    stop sound

    $ time_now = renpy.time.time()
    $ time_remain = time_remain - (time_now - time_start)
    $ time_start = time_now
    if time_remain <= 0:
        jump bomb_mechanic_exit

    show screen bomb_movement(forward, time_remain) with dissolve
    window hide
    $ renpy.pause(hard=True)

    hide screen bomb_movement with dissolve
    $ time_remain = time_remain - (renpy.time.time() - time_start)
    if bomb_choice_counter < 10:
        $ sleep_time = 0.1 + 0.015 * bomb_choice_counter
    elif bomb_choice_counter < 35:
        $ sleep_time = 0.25 + 0.015 * (bomb_choice_counter - 10) ** 1.6
    else:
        $ sleep_time = 2.84 + 0.1 * (bomb_choice_counter - 35) ** 0.9
    $ bomb_choice_counter += 1

    if at_finish(maze, player_x, player_y):
        hide countdown
        $ _skipping = True
        jump r3_end
    elif at_finish_secret(maze, player_x, player_y):
        hide countdown
        $ _skipping = True
        $ r3_secret = True
        jump r3_end
    else:
        jump bomb_choice

label handle_bomb_movement(what):
    if what == "forward":
        $ maze, player_x, player_y = move_forward(maze, player_x, player_y)
    elif what == "left":
        $ maze, player_x, player_y = turn_left(maze, player_x, player_y)
    elif what == "right":
        $ maze, player_x, player_y = turn_right(maze, player_x, player_y)
    return

label bomb_mechanic_exit:
    hide screen bomb_movement with dissolve
    $ _skipping = True
    jump bomb_fail
