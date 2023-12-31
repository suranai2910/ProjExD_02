import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1200, 700

delta = {  # 練習３　矢印での操作
    pg.K_UP: (0, -5),
    pg.K_DOWN:(0, +5),
    pg.K_LEFT:(-5, 0),
    pg.K_RIGHT:(+5, 0)
}

def check_bound(rct: pg.Rect) -> tuple[bool, bool]:
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
    引数　rct　こうかとんor爆弾SurfaceのRect
    戻り値：横方向　縦方向判定結果、（画面内：True/画面外：False）
    """
    yoko, tate = True, True
    if rct.left < 0 or WIDTH < rct.right:
        yoko = False
    if rct.top < 0 or HEIGHT < rct.bottom:
        tate = False
    return (yoko, tate)


def main():
    tmr = 21
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bom_img = pg.Surface((20,20))  # 練習１：透明なSurfaceを作る
    pg.draw.circle(bom_img, (255, 0, 0), (10, 10), 10)  # 練習１：赤い半径１０の円を描く
    bom_img.set_colorkey((0, 0, 0))  
    bom_rct = bom_img.get_rect()  # 練習1
    bom_rct.centerx = random.randint(0, WIDTH)  # 
    bom_rct.centery = random.randint(0, HEIGHT)
    vx, vy = +5, -5  # 練習２：爆弾の速度    
 
    clock = pg.time.Clock()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        
        if kk_rct.colliderect(bom_rct):
            tmr = 0
            kk_img = pg.image.load("ex02/fig/8.png")  # 演習３
            kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
            screen.blit(kk_img, kk_rct)
        if tmr == 20:
            print("Game Over")
            return

        key_lst = pg.key.get_pressed()
        sum_move = [0, 0]
        for k, tpi in delta.items():
            if key_lst[k]: # キーが押されたら
                sum_move[0] += tpi[0]
                sum_move[1] += tpi[1]

            #  演習１のとちゅう
                """if sum_move[0] == -5 and sum_move[1] == 0:  # 進む方向によって、こうかとんの画像の変更
                    kk_img = pg.transform.rotozoom(kk_img,  0, 1.0)
                    kk_rct = kk_img.get_rect()
                elif sum_move[0] == -5 and sum_move[1] == -5:  # 進む方向によって、こうかとんの画像の変更
                    kk_img = pg.transform.rotozoom(kk_img, 45, 1.0)
                    kk_rct = kk_img.get_rect()
                elif sum_move[0] ==  0 and sum_move[1] == -5:  # 進む方向によって、こうかとんの画像の変更
                    kk_img = pg.transform.rotozoom(kk_img, 90, 1.0)
                    kk_rct = kk_img.get_rect()
                elif sum_move[0] ==  5 and sum_move[1] == -5:  # 進む方向によって、こうかとんの画像の変更
                    kk_img = pg.transform.rotozoom(kk_img, 135, 1.0)
                    kk_rct = kk_img.get_rect()
                elif sum_move[0] ==  5 and sum_move[1] == 0:  # 進む方向によって、こうかとんの画像の変更
                    kk_img = pg.transform.rotozoom(kk_img, 180, 1.0)
                    kk_rct = kk_img.get_rect()
                elif sum_move[0] ==  5 and sum_move[1] ==  5:  # 進む方向によって、こうかとんの画像の変更
                    kk_img = pg.transform.rotozoom(kk_img, 225, 1.0)
                    kk_rct = kk_img.get_rect()
                elif sum_move[0] ==  0 and sum_move[1] ==  5:  # 進む方向によって、こうかとんの画像の変更
                    kk_img = pg.transform.rotozoom(kk_img, 270, 1.0)
                    kk_rct = kk_img.get_rect()
                elif sum_move[0] == -5 and sum_move[1] ==  5:  # 進む方向によって、こうかとんの画像の変更
                    kk_img = pg.transform.rotozoom(kk_img, 315, 1.0)
                    kk_rct = kk_img.get_rect()"""

        """if tmr >= 0:
            bom_img = pg.Surface((20+tmr,20+tmr))  # Surfaceの大きさを時間によって変更
            pg.draw.circle(bom_img, (255, 0, 0), (10+tmr, 10+tmr), 10+tmr)  # 大きさと中心座標の変更
            bom_img.set_colorkey((0, 0, 0))
            screen.blit(bom_img, bom_rct)"""
        
        if tmr <= 255:  # 時間にあわせた爆弾の色の変更
            pg.draw.circle(bom_img, (255-tmr, 0+tmr, 0+tmr), (10, 10), 10)
        if 256 <= tmr  <= 510:
            pg.draw.circle(bom_img, (255, 0-tmr+510, 0), (10, 10), 10)
        if 511 <= tmr <= 765:
            pg.draw.circle(bom_img, (255, 255, 0-tmr+765), (10, 10), 10)
        if tmr >=766:
            tmr =21
        
            
        screen.blit(bg_img, [0, 0])
        kk_rct.move_ip(sum_move[0], sum_move[1])
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_move[0], -sum_move[1])
        screen.blit(kk_img, kk_rct)

        bom_rct.move_ip(vx,vy)
        yoko, tate = check_bound(bom_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        screen.blit(bom_img, bom_rct)
        pg.display.update()
        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()