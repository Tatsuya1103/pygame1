import pygame
import sys
import random

# ゲームの初期化
pygame.init()

# ゲーム画面のサイズ
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")

# ゲームのFPS設定
clock = pygame.time.Clock()
fps = 60

# プレイヤーの設定
player_size = 50
player_pos = [screen_width/2, screen_height-2*player_size]
player_speed = 5

# 敵の設定
enemy_size = 50
enemy_pos = [random.randint(0, screen_width-enemy_size), 0]
enemy_list = [enemy_pos]
enemy_speed = 5

# スコアの設定
score = 0
font = pygame.font.SysFont("Arial", 30)

# フォント
font = pygame.font.SysFont(None, 48)

# 長押し検知用の変数
left_pressed = False
right_pressed = False

# ゲームのメインループ
game_over = False
while not game_over:

    # イベントの処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_RIGHT:
                right_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_pressed = False
            elif event.key == pygame.K_RIGHT:
                right_pressed = False

    # プレイヤーの動き
    if left_pressed:
        player_pos[0] -= player_speed
    elif right_pressed:
        player_pos[0] += player_speed

    # 敵の動き
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < screen_height:
            enemy_pos[1] += enemy_speed
        else:
            enemy_list.pop(idx)
            score += 1

        # プレイヤーと敵の衝突判定
        if abs(enemy_pos[0] - player_pos[0]) < player_size and abs(enemy_pos[1] - player_pos[1]) < player_size:
            game_over = True

        # 新しい敵の追加
        if len(enemy_list) < 3:
            x_pos = random.randint(0, screen_width-enemy_size)
            y_pos = 0
            enemy_list.append([x_pos, y_pos])

    # 画面の描画
    screen.fill((0, 0, 0))
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, (255, 0, 0), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, (0, 255, 0), (player_pos[0], player_pos[1], player_size, player_size))
    
        # スコアの表示
    score_text = "Score: " + str(score)
    score_label = font.render(score_text, 1, (255,255,255))
    screen.blit(score_label, (screen_width-200, screen_height-40))

    # プレイヤーの描画
    pygame.draw.rect(screen, (0,255,0), (player_pos[0], player_pos[1], player_size, player_size))

    # 敵の描画
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, (255,0,0), (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # 画面の更新
    pygame.display.update()

    # FPSの設定
    clock.tick(fps)

# ゲームの終了処理
pygame.quit()