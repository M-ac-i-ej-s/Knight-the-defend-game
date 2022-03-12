import pygame
import random
import aa_functions
from pygame import mixer
from sys import exit
import time

pygame.init()
screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Knight attack")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Pixeltype.ttf", 125)
background_music = pygame.mixer.Sound("music/background_music.wav")
background_music.play(loops=-1)
effect_bow = pygame.mixer.Sound("music/bow.wav")
effect_shield = pygame.mixer.Sound("music/shield.wav")
effect_new_record = pygame.mixer.Sound("music/new_record.wav")
game_active = 0
gravity = 0
a = 0
b = 0
z = 50
x = 90
y = 130
o = 170
left = 180
score_1 = 0
scoreboard = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
aa_functions.all_time_score(scoreboard)
volume_numbers = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)
volume_number = 10
player_name = aa_functions.player_all_time()


background = pygame.image.load("graphics/background.jpg").convert()

tower_empty = pygame.image.load("graphics/tower_empty.png").convert_alpha()
tower_empty_surf = tower_empty.get_rect(bottomleft=(-5, 800))

tower_empty_1 = pygame.image.load("graphics/tower_empty_1.png").convert_alpha()
tower_empty_surf1 = tower_empty_1.get_rect(bottomright=(405, 800))

name = pygame.image.load("graphics/name.png").convert_alpha()
name_rect = name.get_rect(midtop=(205, 200))

play = pygame.image.load("graphics/play.png").convert_alpha()
play_hover = pygame.image.load("graphics/play_hover.png").convert_alpha()
play_rect = play.get_rect(center=(200, 400))

tower = pygame.image.load("graphics/tower.png").convert_alpha()
tower_surf = tower.get_rect(bottomleft=(-5, 800))

tower_1 = pygame.image.load("graphics/tower1.png").convert_alpha()
tower_surf1 = tower_1.get_rect(bottomright=(405, 800))

tower_player = pygame.image.load(
    "graphics/tower_player.png").convert_alpha()
tower_player_surf = tower_player.get_rect(midbottom=(200, 800))

score = pygame.image.load("graphics/score.png").convert_alpha()
score_rect = score.get_rect(center=(165, 200))

player = pygame.image.load("graphics/player.png").convert_alpha()
player_rect = player.get_rect(midbottom=(200, 688))

shield = pygame.image.load("graphics/shield.png").convert_alpha()
shield_rect = shield.get_rect(midleft=(205, 600))

shield1 = pygame.image.load("graphics/shield1.png").convert_alpha()
shield1_rect = shield1.get_rect(midright=(220, 600))

fire = pygame.image.load("graphics/fire.png").convert_alpha()
fire_rect = fire.get_rect(midbottom=(100, 890))

fire1 = pygame.image.load("graphics/fire1.png").convert_alpha()
fire_rect1 = fire1.get_rect(midbottom=(320, 890))

arrow = pygame.image.load("graphics/arrow.png").convert_alpha()
arrow_rect = arrow.get_rect(bottomright=(125, 411))

arrow1 = pygame.image.load("graphics/arrow1.png").convert_alpha()
arrow_rect1 = arrow1.get_rect(bottomleft=(275, 411))

controls = pygame.image.load("graphics/controls.png").convert_alpha()
controls_rect = controls.get_rect(center=(200, 520))

score_variable = test_font.render(f"{score_1}", False, "#FF9900")
score_variable_rect = score_variable.get_rect(center=(300, 250))

play_again = pygame.image.load("graphics/play_again.png").convert_alpha()
play_again_hover = pygame.image.load(
    "graphics/play_again_hover.png").convert_alpha()
play_again_rect = play_again.get_rect(midbottom=(199, 700))

game_over = pygame.image.load("graphics/game_over.png").convert_alpha()
game_over_rect = game_over.get_rect(midbottom=(200, 150))

highscore = pygame.image.load("graphics/highscore.png").convert_alpha()
highscore_hover = pygame.image.load(
    "graphics/highscore_hover.png").convert_alpha()
highscore_rect = highscore.get_rect(center=(200, 470))

highscore_1 = pygame.image.load("graphics/highscore_1.png").convert_alpha()
highscore_1_rect = highscore_1.get_rect(center=(200, 100))

menu = pygame.image.load("graphics/menu.png").convert_alpha()
menu_hover = pygame.image.load("graphics/menu_hover.png").convert_alpha()
menu_rect = menu.get_rect(center=(200, 750))

score_board = pygame.image.load("graphics/scoreboard.png").convert_alpha()
score_board_rect = score_board.get_rect(center=(100, 400))

settings = pygame.image.load("graphics/settings.png").convert_alpha()
settings_hover = pygame.image.load(
    "graphics/settings_hover.png").convert_alpha()
settings_rect = settings.get_rect(center=(200, 540))

easy = pygame.image.load("graphics/easy.png").convert_alpha()
easy_hover = pygame.image.load("graphics/easy_hover.png").convert_alpha()
easy_rect = easy.get_rect(center=(100, 150))

hard = pygame.image.load("graphics/hard.png").convert_alpha()
hard_hover = pygame.image.load("graphics/hard_hover.png").convert_alpha()
hard_rect = hard.get_rect(center=(300, 150))

mode = pygame.image.load("graphics/mode.png").convert_alpha()
mode_rect = mode.get_rect(center=(200, 75))

quit_ = pygame.image.load("graphics/quit.png").convert_alpha()
quit_hover = pygame.image.load("graphics/quit_hover.png").convert_alpha()
quit_rect = quit_.get_rect(center=(200, 610))

new_record = pygame.image.load("graphics/new_record.png").convert_alpha()
new_record_rect = settings.get_rect(center=(170, 100))

press_space = pygame.image.load("graphics/press_space.png").convert_alpha()
press_space_rect = press_space.get_rect(center=(200, 700))

reset_scores = pygame.image.load(
    "graphics/reset_scores.png").convert_alpha()
reset_scores_hover = pygame.image.load(
    "graphics/reset_scores_hover.png").convert_alpha()
reset_scores_rect = reset_scores.get_rect(center=(200, 420))

volume = pygame.image.load("graphics/volume.png").convert_alpha()
volume_rect = settings.get_rect(center=(150, 300))

volume_up = pygame.image.load("graphics/volume_up.png").convert_alpha()
volume_up_hover = pygame.image.load(
    "graphics/volume_up_hover.png").convert_alpha()
volume_up_rect = volume_up.get_rect(center=(325, 240))

volume_low = pygame.image.load("graphics/volume_low.png").convert_alpha()
volume_low_hover = pygame.image.load(
    "graphics/volume_low_hover.png").convert_alpha()
volume_low_rect = volume_low.get_rect(center=(325, 360))

volume_number_show = test_font.render(f"{volume_number}", False, "#FF9900")
volume_number_show_rect = volume_number_show.get_rect(center=(330, 310))

Best = pygame.image.load("graphics/Best.png").convert_alpha()
Best_hover = pygame.image.load("graphics/Best_hover.png").convert_alpha()
Best_rect = settings.get_rect(center=(145, 350))

score_first = test_font.render(f"{scoreboard[1]}", False, "#FF9900")
score_first_rect = score_first.get_rect(center=(175, 282))

score_second = test_font.render(f"{scoreboard[2]}", False, "#FF9900")
score_second_rect = score_second.get_rect(center=(175, 347))

score_third = test_font.render(f"{scoreboard[3]}", False, "#FF9900")
score_third_rect = score_third.get_rect(center=(175, 412))

score_fourth = test_font.render(f"{scoreboard[4]}", False, "#FF9900")
score_fourth_rect = score_fourth.get_rect(center=(175, 477))

score_fifth = test_font.render(f"{scoreboard[5]}", False, "#FF9900")
score_fifth_rect = score_fifth.get_rect(center=(175, 542))

player_name_display = test_font.render(f"{player_name}", False, "#FF9900")
player_name_display_rect = player_name_display.get_rect(midleft=(170, 360))

on = pygame.image.load("graphics/on.png").convert_alpha()
off = pygame.image.load("graphics/off.png").convert_alpha()
on_off_rect = on.get_rect(topleft=(0, 0))

angle = shield
angle_rect = shield_rect

fire_variable = fire
fire_variable1 = fire1

on_off = on
play_variable = play
highscore_variable = highscore
menu_variable = menu
play_again_variable = play_again
settings_variable = settings
volume_up_variable = volume_up
volume_low_variable = volume_low
reset_variable = reset_scores
quit_variable = quit_
hard_variable = hard
easy_variable = easy_hover
mode_one = 6
mode_two = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active == 0:
            if aa_functions.is_hovering(play_rect) == True:
                play_variable = play_hover
            else:
                play_variable = play
            if aa_functions.is_hovering(highscore_rect) == True:
                highscore_variable = highscore_hover
            else:
                highscore_variable = highscore
            if aa_functions.is_hovering(settings_rect) == True:
                settings_variable = settings_hover
            else:
                settings_variable = settings
            if aa_functions.is_hovering(quit_rect) == True:
                quit_variable = quit_hover
            else:
                quit_variable = quit_
            if event.type == pygame.MOUSEBUTTONDOWN:
                # początek gry po kliknięciu play
                if play_rect.collidepoint(event.pos):
                    gravity = 0
                    game_active = 1
                    score_1 = 0
                    b = 0
                    z = 50
                    x = 82
                    y = 130
                    o = 162
                    arrow_rect.bottomright = (125, 411)
                    score_variable_rect.center = (300, 210)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # wyświetlenie tabeli wyników po kliknięciu highscore
                if highscore_rect.collidepoint(event.pos):
                    game_active = 4
            if event.type == pygame.MOUSEBUTTONDOWN:
                # włączanie i wyłączanie muzyki poprzez klikanie grafiki głośnika
                if on_off_rect.collidepoint(event.pos):
                    if on_off == on:
                        background_music.stop()
                        on_off = off
                    else:
                        background_music.play(loops=-1)
                        on_off = on
            if event.type == pygame.MOUSEBUTTONDOWN:
                # wyświetlenie ustawień
                if settings_rect.collidepoint(event.pos):
                    game_active = 5
            if event.type == pygame.MOUSEBUTTONDOWN:
                # wyświetlenie ustawień
                if quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
        if game_active == 2:
            if event.type == pygame.KEYDOWN:
                # przesuwanie tarczy na drugą stronę (lewą)
                if event.key == pygame.K_LEFT:
                    angle = shield1
                    angle_rect = shield1_rect
                # przesuwanie tarczy na drugą stronę (prawą)
                if event.key == pygame.K_RIGHT:
                    angle = shield
                    angle_rect = shield_rect
        if game_active == 3:
            if aa_functions.is_hovering(menu_rect) == True:
                menu_variable = menu_hover
            else:
                menu_variable = menu
            if aa_functions.is_hovering(play_again_rect) == True:
                play_again_variable = play_again_hover
            else:
                play_again_variable = play_again
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    # dodanie wyniku do scoreboard
                    aa_functions.add_to_scoreboard(score_1, scoreboard)
                    # update pliku ze zdobytym wynikiem
                    aa_functions.update_file_scoreboard(scoreboard)
                    score_1 = 0
                    b = 0
                    z = 50
                    x = 82
                    y = 130
                    o = 162
                    game_active = 2
                    arrow_rect.bottomright = (125, 411)
                    score_variable_rect.center = (300, 210)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_rect.collidepoint(event.pos):
                    settings_variable = settings
                    play_variable = play
                    highscore_variable = highscore
                    aa_functions.add_to_scoreboard(
                        score_1, scoreboard
                    )  # dodanie wyniku do scoreboard
                    aa_functions.update_file_scoreboard(
                        scoreboard
                    )  # update pliku ze zdobytym wynikiem

                    game_active = 0
                    name_rect.y = 200
            if score_1 > scoreboard[1]:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if len(player_name) > 0:
                            player_name = player_name[:-1]
                            left -= 35
                    else:
                        if len(player_name) < 5:
                            player_name += event.unicode
                            left += 35
                    if event.key == pygame.K_SPACE:
                        aa_functions.update_player(player_name)
                        # dodanie wyniku do scoreboard
                        aa_functions.add_to_scoreboard(score_1, scoreboard)
                        # update pliku ze zdobytym wynikiem
                        aa_functions.update_file_scoreboard(scoreboard)
                        game_active = 0
                        name_rect.y = 200

        if game_active == 4:
            if aa_functions.is_hovering(menu_rect) == True:
                menu_variable = menu_hover
            else:
                menu_variable = menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                # przejscie do menu
                if menu_rect.collidepoint(event.pos):
                    play_variable = play
                    highscore_variable = highscore
                    settings_variable = settings
                    game_active = 0
        if game_active == 5:
            if aa_functions.is_hovering(easy_rect) == True:
                easy_variable = easy_hover
            if aa_functions.is_hovering(hard_rect) == True:
                hard_variable = hard_hover
            if aa_functions.is_hovering(volume_up_rect) == True:
                volume_up_variable = volume_up_hover
            else:
                volume_up_variable = volume_up
            if aa_functions.is_hovering(volume_low_rect) == True:
                volume_low_variable = volume_low_hover
            else:
                volume_low_variable = volume_low
            if event.type == pygame.MOUSEBUTTONDOWN:
                # ustawienie gry glosniej
                if volume_up_rect.collidepoint(event.pos):
                    volume_number += 1
                    if volume_number > 10:
                        volume_number = 10
                    background_music.set_volume(volume_numbers[volume_number])
            if event.type == pygame.MOUSEBUTTONDOWN:
                # ustawienie gry ciszej
                if volume_low_rect.collidepoint(event.pos):
                    volume_number -= 1
                    if volume_number < 0:
                        volume_number = 0
                    background_music.set_volume(volume_numbers[volume_number])
            if aa_functions.is_hovering(menu_rect) == True:
                menu_variable = menu_hover
            else:
                menu_variable = menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                # przejscie do menu
                if menu_rect.collidepoint(event.pos):
                    settings_variable = settings
                    play_variable = play
                    highscore_variable = highscore
                    game_active = 0
            if aa_functions.is_hovering(reset_scores_rect) == True:
                reset_variable = reset_scores_hover
            else:
                reset_variable = reset_scores
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_scores_rect.collidepoint(event.pos):
                    scoreboard = aa_functions.scoreboard_reset(scoreboard)
                    player_name = aa_functions.reset_player_manually(
                        player_name)
                    aa_functions.update_player(player_name)
                    aa_functions.update_file_scoreboard(scoreboard)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    mode_one = 6
                    mode_two = 2
                    easy_variable = easy_hover
                    hard_variable = hard
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hard_rect.collidepoint(event.pos):
                    mode_one = 9
                    mode_two = 3
                    easy_variable = easy
                    hard_variable = hard_hover

    if game_active == 0:
        screen.blit(background, (0, 0))
        screen.blit(tower_empty, tower_empty_surf)
        screen.blit(tower_empty_1, tower_empty_surf1)
        screen.blit(name, name_rect)
        screen.blit(play_variable, play_rect)
        screen.blit(fire_variable, fire_rect)
        screen.blit(fire_variable1, fire_rect1)
        screen.blit(highscore_variable, highscore_rect)
        screen.blit(on_off, on_off_rect)
        screen.blit(settings_variable, settings_rect)
        screen.blit(quit_variable, quit_rect)
        if a % 10 == 0:
            log = fire_variable
            fire_variable = fire_variable1
            fire_variable1 = log
        a += 1

    elif game_active == 1:
        screen.blit(background, (0, 0))
        screen.blit(tower_empty, tower_empty_surf)
        screen.blit(tower_empty_1, tower_empty_surf1)
        screen.blit(name, name_rect)
        screen.blit(play_hover, play_rect)
        screen.blit(fire_variable, fire_rect)
        screen.blit(fire_variable1, fire_rect1)
        screen.blit(highscore, highscore_rect)
        screen.blit(settings_variable, settings_rect)
        screen.blit(quit_variable, quit_rect)
        screen.blit(on_off, on_off_rect)
        if a % 10 == 0:
            log = fire_variable
            fire_variable = fire_variable1
            fire_variable1 = log
        a += 1
        gravity += 1
        name_rect.y -= gravity
        if name_rect.y <= -100:
            game_active = 2

    elif game_active == 2:
        screen.blit(background, (0, 0))
        screen.blit(tower, tower_surf)
        screen.blit(tower_1, tower_surf1)
        screen.blit(tower_player, tower_player_surf)
        screen.blit(score, score_rect)
        screen.blit(player, player_rect)
        screen.blit(angle, angle_rect)
        screen.blit(fire_variable, fire_rect)
        screen.blit(fire_variable1, fire_rect1)
        score_variable = test_font.render(f"{score_1}", False, "#FF9900")
        score_rect.center = (165, 200)

        if a % 10 == 0:
            log = fire_variable
            fire_variable = fire_variable1
            fire_variable1 = log
        a += 1
        if b == (x - 1):
            z += random.randrange(100, 120)
            x += random.randrange(100, 120)
            if z + 30 > x:
                x += 60
        if b in range(z, x):
            screen.blit(arrow, arrow_rect)
            if b == z:
                effect_bow.play()
            arrow_rect.y += mode_one
            arrow_rect.x += mode_two
            if arrow_rect.colliderect(shield1_rect) and angle == shield1:
                effect_shield.play()
                score_1 += 1
                score_variable = test_font.render(
                    f"{score_1}", False, "#FF9900")
                arrow_rect.bottomright = (2000, 2000)
                if score_1 == scoreboard[1] + 1:
                    effect_new_record.play()
        else:
            arrow_rect.bottomright = (125, 411)

        screen.blit(score_variable, score_variable_rect)

        if b == (o - 1):
            y += random.randrange(150, 170)
            o += random.randrange(150, 170)
            if y + 30 > o:
                o += 60
        if b in range(y, o):
            if b == y:
                effect_bow.play()
            screen.blit(arrow1, arrow_rect1)
            arrow_rect1.y += mode_one
            arrow_rect1.x -= mode_two
            if arrow_rect1.colliderect(shield_rect) and angle == shield:
                effect_shield.play()
                score_1 += 1
                score_variable = test_font.render(
                    f"{score_1}", False, "#FF9900")
                arrow_rect1.bottomleft = (2000, 2000)
                if score_1 == scoreboard[1] + 1:
                    effect_new_record.play()
        else:
            arrow_rect1.bottomleft = (275, 411)
        b += 1
        if arrow_rect.colliderect(player_rect) or arrow_rect1.colliderect(player_rect):
            game_active = 3
        if score_1 > scoreboard[1]:
            left = 180
            player_name = aa_functions.reset_player(
                player_name, score_1, scoreboard, 1)
            screen.blit(new_record, new_record_rect)

    elif game_active == 3:
        screen.blit(background, (0, 0))
        screen.blit(tower_empty, tower_empty_surf)
        screen.blit(tower_empty_1, tower_empty_surf1)
        screen.blit(game_over, game_over_rect)
        screen.blit(score, score_rect)
        score_variable = test_font.render(f"{score_1}", False, "#FF9900")
        screen.blit(score_variable, score_variable_rect)
        score_variable_rect.center = (300, 250)
        score_rect.center = (165, 238)
        if score_1 > scoreboard[1]:
            screen.blit(Best, Best_rect)
            player_name_display = test_font.render(
                f"{player_name}", True, "#FF9900")
            screen.blit(player_name_display, player_name_display_rect)
            screen.blit(press_space, press_space_rect)
            if time.time() % 1 > 0.5:
                pygame.draw.rect(screen, "#FF9900", (left, 322, 10, 50))
        else:
            screen.blit(play_again_variable, play_again_rect)
            screen.blit(menu_variable, menu_rect)

    elif game_active == 4:
        screen.blit(background, (0, 0))
        screen.blit(tower_empty, tower_empty_surf)
        screen.blit(tower_empty_1, tower_empty_surf1)
        screen.blit(fire_variable, fire_rect)
        screen.blit(fire_variable1, fire_rect1)
        screen.blit(highscore_1, highscore_1_rect)
        screen.blit(score_board, score_board_rect)
        screen.blit(menu_variable, menu_rect)
        score_first = test_font.render(f"{scoreboard[1]}", False, "#FF9900")
        score_second = test_font.render(f"{scoreboard[2]}", False, "#FF9900")
        score_third = test_font.render(f"{scoreboard[3]}", False, "#FF9900")
        score_fourth = test_font.render(f"{scoreboard[4]}", False, "#FF9900")
        score_fifth = test_font.render(f"{scoreboard[5]}", False, "#FF9900")
        screen.blit(Best, (10, 600))
        player_name_display = test_font.render(
            f"{player_name}", True, "#FF9900")
        screen.blit(player_name_display, (180, 600))
        screen.blit(score_first, score_first_rect)
        screen.blit(score_second, score_second_rect)
        screen.blit(score_third, score_third_rect)
        screen.blit(score_fourth, score_fourth_rect)
        screen.blit(score_fifth, score_fifth_rect)
        if a % 10 == 0:
            log = fire_variable
            fire_variable = fire_variable1
            fire_variable1 = log
        a += 1
    elif game_active == 5:
        screen.blit(background, (0, 0))
        screen.blit(tower_empty, tower_empty_surf)
        screen.blit(tower_empty_1, tower_empty_surf1)
        screen.blit(fire_variable, fire_rect)
        screen.blit(fire_variable1, fire_rect1)
        screen.blit(volume, volume_rect)
        screen.blit(volume_up_variable, volume_up_rect)
        screen.blit(volume_low_variable, volume_low_rect)
        volume_number_show = test_font.render(
            f"{round(volume_numbers[volume_number],1)}", False, "#FF9900"
        )
        screen.blit(volume_number_show, volume_number_show_rect)
        screen.blit(menu_variable, menu_rect)
        screen.blit(reset_variable, reset_scores_rect)
        screen.blit(controls, controls_rect)
        screen.blit(easy_variable, easy_rect)
        screen.blit(hard_variable, hard_rect)
        screen.blit(mode, mode_rect)
        if a % 10 == 0:
            log = fire_variable
            fire_variable = fire_variable1
            fire_variable1 = log
        a += 1

    pygame.display.update()
    clock.tick(60)
