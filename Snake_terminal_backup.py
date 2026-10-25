# ==============================
# SIMPLE SNAKE GAME
# ==============================
# Learn Python basics by controlling a snake,
# eating food, and growing longer!



import random
import os
import curses


# ===== Game config =====================================================
width = 30
height = 15

# ===== Directions ======================================================
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)
# ===== CLEAR ===========================================================
def clear():
    # if os.name == 'nt':
    #     os.system('cls')
    # else:
    #     os.system('clear')

    os.system('cls' if os.name == 'nt' else 'clear')
# ======== DRAW HELPERS =================================================
def draw(snake, food, score):

    clear()

    # grid = []

    # # Create the grid
    # for _ in range(height):
    #     row = []
    #     for _ in range(width):
    #         row.append(' ')
    #     grid.append(row)

    grid = [[' ' for _ in range(width)] for _ in range(height)]

# ======== WALLS ========================================================
    for x in range(width):
        grid[0][x] = '#'
        grid[height - 1][x] = '#'

    for y in range(height):
        grid[y][0] = '#'
        grid[y][width - 1] = '#'

# ======== FOOD ==========================================================
    # fx = food[0]
    # fy = food[1]
    fx, fy = food
    grid[fy][fx] = '*'

 # ======== SNAKE ========================================================
    for i, (x, y) in enumerate(snake):
        if i == 0:
            grid[y][x] = '@'
        else:
            grid[y][x] = '8'

# ======== PRINT GRID RENDER =============================================
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()
    print(f"score:  {score}")
    print("Move with WASD then pres enter (q to quite)")

# ======== FOOD ========================================================
def create_food(snake):
    while True:
        food = (
            random.randint(1, width - 2),
            random.randint(1, height - 2)
        )

        if food not in snake:
            return food
# ======== KEYBOARD CONTROLS ===========================================
def on_press(event):
    # Your keyboard control code goes here
    pass

# ======== GAME ========================================================
def game():
    snake = [
        (width // 2, height // 2),
        (width // 2 - 1, height // 2),
        (width // 2 - 2, height // 2)
    ]

    food = create_food(snake)
    direction = right
    score = 0

    while True:

        draw(snake, food, score)

        key = input("Direction (w/a/s/d): ")

        if key == 'w' and direction != down:
            direction = up
        elif key == 's'and direction != up:
            direction = down
        elif key == 'a' and direction != right:
            direction = left
        elif key == 'd' and direction != left:
            direction = right
        elif key == 'q':
            break

        # head = snake[0]
        # head_x = head[0]
        # head_y = head[1]
        head_x, head_y = snake[0]

        # dx = direction[0]
        # dy = direction[1]
        dx, dy = direction

        new_head = (head_x + dx, head_y + dy)

        #WALL COLISSION

        if(new_head[0] == 0 or new_head[0] == width - 1):
            break

        if(new_head[1] == 0 or new_head[1] == height - 1):
            break

        #self collission
        if new_head in snake:
            break

        snake.insert(0, new_head)

        #FOOD
        if new_head== food:
            #score = score + 10
            score += 10
            food = create_food(snake)
        else:
            snake.pop()


# ======== GAME OVER ================================================
    print("\n" + "#" * 35)
    print("           GAME OVER")
    print(f"         Final Score: {score}")
    print("#" * 35)

game()
