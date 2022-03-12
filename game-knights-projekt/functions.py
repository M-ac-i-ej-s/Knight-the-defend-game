import pygame


def add_to_scoreboard(score, scoreboard):
    if scoreboard[1] <= score:
        k = len(scoreboard)
        while 2 <= k:
            scoreboard[k] = scoreboard[k - 1]
            k -= 1
        scoreboard[1] = score
        return scoreboard
    for i in range(1, len(scoreboard) + 1):
        if scoreboard[i] < score:
            k = len(scoreboard)
            while i <= k:
                scoreboard[k] = scoreboard[k - 1]
                k -= 1
            scoreboard[i] = score
            return scoreboard


def all_time_score(scoreboard):
    score_txt = open("aa_scores.txt", "r")
    i = 1
    for line in score_txt:
        scoreboard[i] = int(line)
        i += 1
    return scoreboard


def player_all_time():
    player_txt = open("player.txt", "r", encoding="utf-8")
    return player_txt.read()


def update_player(player):
    score_txt = open("player.txt", "w")
    score_txt.write(player)
    score_txt.close()


def update_file_scoreboard(scoreboard):
    lines = [
        str(scoreboard[1]),
        "\n",
        str(scoreboard[2]),
        "\n",
        str(scoreboard[3]),
        "\n",
        str(scoreboard[4]),
        "\n",
        str(scoreboard[5]),
    ]
    score_txt = open("aa_scores.txt", "w")
    score_txt.writelines(lines)
    score_txt.close()


def is_hovering(something):
    mouse = pygame.mouse.get_pos()
    if something.collidepoint(mouse):
        return True
    else:
        return False


def scoreboard_reset(scoreboard):
    scoreboard[1] = 0
    scoreboard[2] = 0
    scoreboard[3] = 0
    scoreboard[4] = 0
    scoreboard[5] = 0
    return scoreboard


def reset_player_manually(player):
    player = ""
    return player


def reset_player(player, score, scoreboard, first_element):
    if score > scoreboard[first_element]:
        player = ""
        return player
