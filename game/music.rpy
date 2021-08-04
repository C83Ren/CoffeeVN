define tracks = [
    (_('Main Theme'), _('DOVA-SYNDROME'), 'audio/Route_1_-_movie_theme.mp3'),
    (_('Support - Shiraishi Theme'), _('DOVA-SYNDROME'), 'audio/Route_1_-_Track_1.ogg'),
    (_('Support - Hitona Theme'), _('DOVA-SYNDROME'), 'audio/Route_1_-_hitona_theme.mp3'),
    (_('Support - Game Arcade'), _('DOVA-SYNDROME'), 'audio/Route_1_-_game_arcade.mp3'),
    (_('Support - Horror'), _('DOVA-SYNDROME'), 'audio/Route_1_-_horror_theme.mp3'),
    (_('Support - End'), _('DOVA-SYNDROME'), 'audio/Route_1_-_End_Theme.mp3'),
    (_('Joy - Adventure'), _('Luttii'), 'audio/Route_2_-_Adventure.ogg'),
    (_('Joy - Battle'), _('Luttii'), 'audio/Route_2_-_Battle_Theme.mp3'),
    (_('Joy - Final Battle'), _('Luttii'), 'audio/Route_2_-_Before_Final_intro.ogg'),
    (_('Joy - King Theme'), _('Luttii'), 'audio/Route_2_-_King_intro.ogg'),
    (_('Joy - End'), _('DOVA-SYNDROME'), 'audio/Route_2_-_End_Theme.mp3'),
    (_('Memories - Lios Theme'), _('DOVA-SYNDROME'), 'audio/Route_3_-_Track_1.mp3'),
    (_('Memories - Final Challenge'), _('Luttii'), 'audio/Route_3_-_Track_2.ogg'),
    (_('Memories - Labyrinth'), _('Luttii'), 'audio/Route_3_-_Track_3.ogg'),
    (_('Memories - End'), _('DOVA-SYNDROME'), 'audio/Route_3_-_End_Theme.mp3'),
    (_('Bad End'), _('DOVA-SYNDROME'), 'audio/Route_2_-_Bad_End.mp3'),
    (_('True End - Present'), _('DOVA-SYNDROME'), 'audio/true_end.mp3'),
]

init python:
    mr = MusicRoom(fadeout=1.0, loop=True, single_track=True)

    for tag, author, file in tracks:
        mr.add(file)
