from unittest import runner
import pygame
import sys
import time

# 初期化
pygame.init()

# ウィンドウのサイズ
width = 1500
height = 1000

# ウィンドウの作成
screen = pygame.display.set_mode((width, height))

# ウィンドウのタイトル
pygame.display.set_caption("ボールバウンス")

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ボールの設定
ball_radius = 10
ball_speed_x = 13
ball_speed_y = 13
# ボールの位置とサイズを設定
# Rectは四角形を表すクラスでその中にボールが収まるようになっている
ball = pygame.Rect(width // 2, height // 2, ball_radius * 2, ball_radius * 2) 


running = True # running はゲームのループを継続するかどうかを管理するフラグ
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # ウィンドウの×ボタンが押されたらゲームを終了
            pygame.quit() # ゲームの終了
            sys.exit() # プログラムの終了

    # ボールの移動
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # ボールの壁との衝突
    if ball.left <= 0 or ball.right >= width: # ボールの左端もしくは右端が壁に接したら
        ball_speed_x = -ball_speed_x # ボールの速度を反転
    if ball.top <= 0 or ball.bottom >= height: # ボールの上端もしくは下端が壁に接したら
        ball_speed_y = -ball_speed_y # ボールの速度を反転

    # 画面の描画
    screen.fill(BLACK)
    # ボールの描画
    pygame.draw.ellipse(screen, WHITE, ball)
    # 画面の更新
    pygame.display.update()
    # 0.01秒待つ
    time.sleep(0.01)

pygame.quit()