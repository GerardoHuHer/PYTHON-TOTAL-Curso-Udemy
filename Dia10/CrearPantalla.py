# Módulos importados
import pygame
import random
import math
from pygame import mixer

# Inicializar a pygame
pygame.init()

# Crear la pantalla
# Con esto establecemos el modo en que se muestra pygame, la pantalla en pocas palabras
pantalla = pygame.display.set_mode((800, 600))
# El tuple que tiene de parámetro es para determinar el tamaño de la pantalla, en este caso alto y ancho.

# Título e ícono
pygame.display.set_caption("Invasión Espacial") # Establece el título
icono = pygame.image.load("cohete (1).png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("cielo-estrellado.jpg")

# Agregar música

mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Jugador

# Variables del jugador
img_player = pygame.image.load("Personaje.png")
# Ya que restamos los 64 px del jugador a la mitad de los 800 de pantalla
player_x = 368
player_y = 500
player_x_change = 0

# Variables del enemigo
img_enemy = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemy.append(pygame.image.load("ovni.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 200))
    enemy_x_change.append(1)
    enemy_y_change.append(50)

# Variables de la bala
img_bullet = pygame.image.load("bala.png")
bullet_x = 0
bullet_y = 500
bullet_x_change = 0.5
bullet_y_change = 3
visible_bullet = False

# Variable puntaje
puntaje = 0
# Variabel que va a guardar una variable de pygame
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

# Texto final de juego
fuente_final = pygame.font.Font("freesansbold.ttf", 32)
texto_x_final = 100
texto_y_final = 40

# Texto final
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))

# Función texto
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Función jugador
def player(x, y):
    pantalla.blit(img_player, (x, y))

# Función enemigo
def enemy(x, y, ene):
    pantalla.blit(img_enemy[ene], (x, y))

# Función disparar
def disparar(x, y):
    global visible_bullet
    visible_bullet = True
    pantalla.blit(img_bullet, (x + 16, y + 10))

# Función detectar colisiones
def detectar_colision(x_1, y_1, x_2, y_2):
    operacion_1 = x_1 - x_2
    operacion_2 = y_1 - y_2
    distancia = math.sqrt(math.pow(operacion_1, 2) + math.pow(operacion_2, 2))
    if distancia < 27:
        return True
    else:
        return False


# Al querer que el jugador se actulice constantemente tenemos que ponerlo dentro del loop antes del update

# Loop del juego

# Con este while hacemos que mientras sea true funcione el juego y al presionar el tache se convierta en false

se_ejecuta = True

while se_ejecuta:
    # cerrando de esta manera el juego

    # RGB de la pantalla, se pone antes para asegurar que no tape a nada
    # Sirve para poder cambiar el color de fondo
    #pantalla.fill((205, 144, 228))

    # Fondo con imagen
    pantalla.blit(fondo, (0,0))

    # Iterar eventos en el loop
    for evento in pygame.event.get():

        # Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar movimiento
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                # En caso de presionar la tecla a, el jugador restará 3 px a su posición actual
                player_x_change = -0.5
            if evento.key == pygame.K_d:
                # En caso de presionar la tecla a, el jugador restará 3 px a su posición actualaa
                player_x_change = 0.5
            if evento.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound("disparo.mp3")
                bullet_sound.play()
                if not visible_bullet:
                    bullet_x = player_x
                    disparar(bullet_x, bullet_y)

        # Evento dejar de mover
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                player_x_change = 0



    # Evento modificar ubicación
    # Esto altera la posición del jugador según la tecla que presionemos sumando los pixéles que se deseen previamente
    player_x += player_x_change

    # Mantener dentro de bordes al jugador
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Esto altera la posición del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego

        if enemy_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemy_y[k] = 1000
            texto_final()
            break

        enemy_x[e] += enemy_x_change[e]

    # Mantener dentro de bordes al enemigo
        if enemy_x[e] <= 0:
            enemy_x_change[e] = 1
            enemy_y[e] += enemy_y_change[e]
        elif enemy_x[e] >= 736:
            enemy_x_change[e] = -1
            enemy_y[e] += enemy_y_change[e]

        # Colisión
        colision = detectar_colision(enemy_x[e], enemy_y[e], bullet_x, bullet_y)
        if colision:
            colision_sound = mixer.Sound("Golpe.mp3")
            colision_sound.play()
            bullet_y = 500
            visible_bullet = False
            puntaje += 1

            enemy_x[e] = random.randint(0, 736)
            enemy_y[e] = random.randint(50, 200)

        enemy(enemy_x[e], enemy_y[e], e)

    # Movimiento bala
    if bullet_y <= -64:
        bullet_y = 500
        visible_bullet = False
    if visible_bullet:
        disparar(bullet_x, bullet_y)
        bullet_y -= bullet_y_change



    player(player_x, player_y)

    # Mostrar puntaje en pantalla

    mostrar_puntaje(texto_x, texto_y)


    # Evento actualizar
    # Con este actualizamos la pantalla del juego
    pygame.display.update()