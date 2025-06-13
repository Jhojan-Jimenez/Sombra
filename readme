# Sombra - Juego en Pygame

**Sombra** es un videojuego 2D tipo _roguelike dungeon_ con oleadas infinitas de enemigos, desarrollado con **Pygame**. El objetivo es sobrevivir la mayor cantidad de oleadas posible enfrentando enemigos de distinto tipo, usando tus habilidades y reflejos.

---

## ¿Cómo se juega?

- Controlas a un personaje en una arena cerrada.
- Sobrevive a oleadas de enemigos que aumentan progresivamente.
- Dispara, esquiva, cura y derrota enemigos hasta donde puedas.

---

## Mecánicas del juego

### Jugador

- Se mueve libremente en 4 direcciones.
- Apunta y **dispara proyectiles normales** con el **click izquierdo** del ratón.
- Usa habilidades:
  - **Q:** Lanza un proyectil más grande y más potente. Tiene un **cooldown de 5 segundos**.
  - **E:** Cura al jugador una pequeña cantidad. Tiene un **cooldown de 60 segundos**.
- La barra de vida visible se reduce al recibir daño.
- Cambia de orientación (mirando a la izquierda o derecha) dependiendo de la dirección del movimiento.

### Enemigos

- Aparecen de forma aleatoria en cada oleada.
- Tipos:
  - **MeleeEnemy:** Se acerca y ataca cuerpo a cuerpo.
  - **RangedEnemy:** Dispara proyectiles hacia el jugador.
  - **BossEnemy:** Aparece cada 5 oleadas, tiene más vida y un patrón de ataque especial.
- Cada enemigo tiene atributos únicos: salud, velocidad y comportamiento.

---

## Oleadas

- Comienzas en la oleada 1.
- En cada nueva oleada, aparece un enemigo más que en la anterior.
- **Cada 5 oleadas aparece un jefe (boss).**
- Las oleadas se generan sin que los enemigos colisionen entre sí ni con el jugador al aparecer.

---

## Interfaz

- **HUD de vida**: tanto el jugador como los enemigos muestran barras de vida con segmentos.
- **Contador de oleada** y **cooldowns** visibles.
- Música y efectos de sonido integrados (al matar enemigos, disparar, etc).

---

## Menús

- **Menú Principal**: Permite iniciar el juego o salir.
- **Menú de Pausa (ESC)**:
  - Continuar
  - Reiniciar partida
  - Volver al menú principal

---

## Gráficos y Sonido

- Entidades tienen imágenes personalizadas (ej: `assets/player.png`, `melee_enemy.png`, etc).
- Se utiliza un fondo escalado (`background.png`) para ambientación.
- Efectos de sonido y música de fondo reproducida con `pygame.mixer`.
- Todos los elementos (jugador, enemigos, proyectiles) tienen hitboxes ajustadas para precisión en colisiones.

---

## Estructura del código

- `entities/`: Contiene clases del jugador, enemigos, proyectiles.
- `core/`: Lógica principal del juego, manejo de escenas, configuraciones y control general, por ejemplo el manejo del sonido.
- `assets/`: Archivos de imagen y sonido.
- `main.py`: Entrada principal del juego.
- `scenes/`: Contiene las escnas principales del juego, como la pantalla de game_over, la del juego, el menu principal y el menu de pausa.
- Separación clara entre lógica, renderizado y control de estados.

---

## 🚀 Requisitos

- Python 3.10+
- Pygame

Instalación de dependencias:

```bash
pip install pygame
```
