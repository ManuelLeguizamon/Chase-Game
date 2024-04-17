import pygame as pg
pg.font.init()

#--------------------------------------------------------------------------------V
win_height, win_width = 650, 1200
WIN = pg.display.set_mode((win_width,win_height))
pg.display.set_caption("La mancha")

#--------------------------------------------------------------------------------V
    #Constantes

win_color = (0, 0, 0)
pj1_color = (179, 179, 179) #Gris
pj2_color = (255, 120, 0) #Rojo
txt = pg.font.SysFont("Rockwell", 30)
colorGris = (140, 140, 140)
BARRA = pg.rect.Rect(0,240,7,140)
#--------------------------------------------------------------------------------V
    # Cuando hay un ganador

def Ganador(pj_ganador,color):
    win_txt = txt.render(f"HA GANADO {pj_ganador}",1,color)
    WIN.blit(win_txt,(win_width//2-160, win_height//2 - 150))
    pg.display.update()
    pg.time.delay(2000)

#--------------------------------------------------------------------------------V
    # Coliciones de los pj  

def Colicion(pj1,pj2,pj1_score):
    if pj1.colliderect(pj2):
        txt_render = txt.render("Punto para la mancha",1,colorGris)
        WIN.blit(txt_render,(win_width//2-170, win_height//2 -250))
        pg.display.update()
        pg.time.delay(500)
        pj1_score += 1
#Para reiniciar reasigno las posiciones de los jugadores
        pj1.x, pj1.y = 30, 300
        pj2.x, pj2.y = 1130, 300
    return pj1_score
        
def Pj2Colicion(BARRA,pj2,pj2_score):
    if pj2.colliderect(BARRA):
        txt_render = txt.render("Punto para el naranja",1,pj2_color)
        WIN.blit(txt_render,(win_width//2-170, win_height//2 -250))
        pg.display.update()
        pg.time.delay(500)
        pj2_score += 1
        pj1.x, pj1.y = 30, 300
        pj2.x, pj2.y = 1130, 300
    return pj2_score

#--------------------------------------------------------------------------------V
class Jugador(pg.Rect):
    def __init__(self, x,y):
        super().__init__(x, y, 30, 30)
    
    def move(self,teclaPresionada,left,right,up,down):
        if teclaPresionada[left] and self.x > 0:
            self.x -= velocidad
        if teclaPresionada[right] and self.x < win_width - 30:
            self.x += velocidad
        if teclaPresionada[up] and self.y > 5:
            self.y -= velocidad
        if teclaPresionada[down] and self.y < win_height - 35:
            self.y += velocidad

 
velocidad = 10
pj1=Jugador(30,300)    
pj2=Jugador(1130, 300)
#--------------------------------------------------------------------------------V
def verPantalla(pj1_score,pj2_puntos):
    WIN.fill(win_color)
    pg.draw.rect(WIN,pj1_color,pj1)
    pg.draw.rect(WIN,pj2_color,pj2)
    pg.draw.rect(WIN,pj2_color,BARRA)
    puntos_pj1= txt.render(f"Puntos: {pj1_score}", 1 ,pj1_color)
    WIN.blit(puntos_pj1, (20,10))
    puntos_pj2 = txt.render(f"Puntos: {pj2_puntos}",1,pj2_color)
    WIN.blit(puntos_pj2,(1040,10))

    pg.display.update()

#--------------------------------------------------------------------------------V
def main():
    clock = pg.time.Clock()
    pj1_score,pj2_score = 0,0  
    while True:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                   
            if pj1.colliderect(pj2): 
                pj1_score+=1

        teclaPresionada = pg.key.get_pressed()
        pj1.move(teclaPresionada, pg.K_a,pg.K_d,pg.K_w,pg.K_s)
        pj2.move(teclaPresionada, pg.K_LEFT,pg.K_RIGHT,pg.K_UP,pg.K_DOWN)
        verPantalla(pj1_score,pj2_score)
        pj1_score = Colicion(pj1, pj2, pj1_score)
        pj2_score = Pj2Colicion(BARRA,pj2,pj2_score)
        
# Caso de pj1 GANADOR!!!!!!!!!<----------------------------------------------------------V
        if pj1_score==5:
            pj1_win="EL GRIS"
            Ganador(pj1_win,pj1_color)
            pj1_score=0
            pj2_score=0
        elif pj2_score==5:
            pj2_win="EL NARANJA"
            Ganador(pj2_win,pj2_color)
            pj1_score=0
            pj2_score=0
    
#--------------------------------------------------------------------------------V
if __name__ == "__main__":
    main()