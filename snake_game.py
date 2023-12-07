import pygame, sys, random

# color and font codes
BG_COLOR = (0, 0, 0)
DIFF_FONT_COLOR = (0, 255, 0)
FONT_COLOR = (255, 255, 255)
START_MENU_FONT = 40
GAME_OVER_FONT = 40
FONT_SMALL = 35
FONT_SMALLEST = 28

# dimension constants
INITIAL_WIDTH = 420
INITIAL_HEIGHT = 420
SQUARE_SIZE = 28
INITIAL_TRAIL_X = 56
INITIAL_TRAIL_Y = 196


# difficulty classes to specify conditional constants
class EasyConstants:
    def __init__(self):
        self.snake_color = (0, 255, 0)
        self.apple_color = (255, 0, 0)
        self.speed = 4


class MediumConstants:
    def __init__(self):
        self.snake_color = (255, 255, 0)
        self.apple_color = (255, 0, 0)
        self.speed = 7


class HardConstants:
    def __init__(self):
        self.snake_color = (255, 0, 0)
        self.apple_color = (0, 255, 255)
        self.speed = 10


def draw_start_menu():
    start_menu_font = pygame.font.SysFont("bauhaus93", START_MENU_FONT)
    start_text_diff = "Select Difficulty"
    easy_text = "Easy"
    medium_text = "Medium"
    hard_text = "Hard"

    start_diff_surf = start_menu_font.render(start_text_diff, 0, DIFF_FONT_COLOR)
    easy_surf = start_menu_font.render(easy_text, 0, FONT_COLOR)
    medium_surf = start_menu_font.render(medium_text, 0, FONT_COLOR)
    hard_surf = start_menu_font.render(hard_text, 0, FONT_COLOR)

    start_diff_rect = start_diff_surf.get_rect(center=(INITIAL_WIDTH // 2, INITIAL_HEIGHT // 2 - 125))
    easy_rect = easy_surf.get_rect(center=(INITIAL_WIDTH // 2, INITIAL_HEIGHT // 2 - 10))
    medium_rect = medium_surf.get_rect(center=(INITIAL_WIDTH // 2, INITIAL_HEIGHT // 2 + 50))
    hard_rect = hard_surf.get_rect(center=(INITIAL_WIDTH // 2, INITIAL_HEIGHT // 2 + 110))

    screen.blit(start_diff_surf, start_diff_rect)
    screen.blit(easy_surf, easy_rect)
    screen.blit(medium_surf, medium_rect)
    screen.blit(hard_surf, hard_rect)


def draw_game_over(win):
    screen.fill(BG_COLOR)
    game_over_font = pygame.font.SysFont("bauhaus93", GAME_OVER_FONT)
    game_over_font_small = pygame.font.SysFont("bauhaus93", FONT_SMALL)
    game_over_font_smallest = pygame.font.SysFont("bauhaus93", FONT_SMALLEST)

    if win:
        end_text = "You Win!"
    else:
        end_text = "You Lose!"

    end_surf = game_over_font.render(end_text, 0, difficulty.snake_color)
    end_rect = end_surf.get_rect(center=(INITIAL_WIDTH // 2, INITIAL_HEIGHT // 2 - 125))
    screen.blit(end_surf, end_rect)

    score_text = f"Score: {score}"
    score_surf = game_over_font_small.render(score_text, 0, FONT_COLOR)
    score_rect = score_surf.get_rect(center=(INITIAL_WIDTH // 2, INITIAL_HEIGHT // 2 - 75))
    screen.blit(score_surf, score_rect)

    high_score_text = f"High Score: {high_score}"
    high_score_surf = game_over_font_small.render(high_score_text, 0, FONT_COLOR)
    high_score_rect = high_score_surf.get_rect(center=(INITIAL_WIDTH // 2, INITIAL_HEIGHT // 2 - 35))
    screen.blit(high_score_surf, high_score_rect)

    restart_text = "Press r to play again"
    restart_surf = game_over_font_smallest.render(restart_text, 0, FONT_COLOR)
    restart_rect = restart_surf.get_rect(center=(INITIAL_WIDTH // 2, INITIAL_HEIGHT // 2 + 50))
    screen.blit(restart_surf, restart_rect)

    difficult_select_text = "Press c to change the difficulty"
    difficult_select_surf = game_over_font_smallest.render(difficult_select_text, 0, FONT_COLOR)
    difficult_select_rect = difficult_select_surf.get_rect(center=(INITIAL_WIDTH //2, INITIAL_HEIGHT // 2 + 125))
    screen.blit(difficult_select_surf, difficult_select_rect)


if __name__ == "__main__":
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((INITIAL_WIDTH, INITIAL_HEIGHT))
    pygame.display.set_caption("Snake Game")
    screen.fill(BG_COLOR)
    draw_start_menu()

    # game state variables
    high_score = 0
    system_running = True
    start_running = True
    game_running = False
    game_over = False

    # event loop
    while system_running:
        while start_running and not game_over:
            for event in pygame.event.get():
                # quit condition
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # create game state variables
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 150 < x < 250 and 170 < y < 230:
                        difficulty = EasyConstants()
                        game_running = True
                        start_running = False
                    elif 140 < x < 280 and 230 < y < 290:
                        difficulty = MediumConstants()
                        game_running = True
                        start_running = False
                    elif 150 < x < 250 and 290 < y < 350:
                        difficulty = HardConstants()
                        game_running = True
                        start_running = False

            pygame.display.update()

        # game state variables
        screen.fill(BG_COLOR)

        snake = pygame.Surface((50, 50))
        snake_rect = snake.get_rect()
        snake.fill(difficulty.snake_color)

        trail = pygame.Surface((50, 50))
        trail_rect = trail.get_rect()
        trail.fill(BG_COLOR)

        apple = pygame.Surface((50, 50))
        apple_rect = apple.get_rect()
        apple.fill(difficulty.apple_color)

        direction = "right"
        current_direction = "right"
        x_coordinate = 84
        y_coordinate = 196
        apple_x = 336
        apple_y = 196
        score = 0
        game_over = False
        eat_apple = False
        win = False

        # rects created to detect if a button is pressed
        pygame.draw.rect(screen, difficulty.snake_color, (INITIAL_TRAIL_X + 2, INITIAL_TRAIL_Y + 2, SQUARE_SIZE - 4, SQUARE_SIZE - 4))
        pygame.draw.rect(screen, difficulty.snake_color, (x_coordinate + 2, y_coordinate + 2, SQUARE_SIZE - 4, SQUARE_SIZE - 4))
        pygame.draw.rect(screen, difficulty.apple_color, (apple_x, apple_y, SQUARE_SIZE, SQUARE_SIZE))

        # list of snake square positions in order to reprint snake each frame
        snake_position_list = [(84, 196), (INITIAL_TRAIL_X, INITIAL_TRAIL_Y)]
        grid_positions_starter = [[i for i in range(0, 393, 28)] for j in range(0, 393, 28)]
        grid_positions_list = []
        y_index = -1
        for i in grid_positions_starter:
            y_index += 1
            for j in i:
                coord_tuple = (j, (y_index * 28))
                grid_positions_list.append(coord_tuple)

        while game_running and not start_running and not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and current_direction != "right":
                        direction = "left"
                        current_direction = "left"
                        break
                    if event.key == pygame.K_RIGHT and current_direction != "left":
                        direction = "right"
                        current_direction = "right"
                        break
                    if event.key == pygame.K_UP and current_direction != "down":
                        direction = "up"
                        current_direction = "up"
                        break
                    if event.key == pygame.K_DOWN and current_direction != "up":
                        direction = "down"
                        current_direction = "down"
                        break

            if direction == "left":
                x_coordinate -= SQUARE_SIZE
            elif direction == "right":
                x_coordinate += SQUARE_SIZE
            elif direction == "up":
                y_coordinate -= SQUARE_SIZE
            elif direction == "down":
                y_coordinate += SQUARE_SIZE

            new_position = (x_coordinate, y_coordinate)

            # game ends and player loses if snake moves into any walls or collides with itself
            if (x_coordinate < 0 or x_coordinate > 392 or y_coordinate < 0 or y_coordinate > 392
                    or new_position in snake_position_list):
                game_over = True
            # checks if any grid positions are still available for the player to move in, if not, they win
            if set(snake_position_list) == set(grid_positions_list):
                game_over = True
                win = True
            if game_over:
                pygame.time.delay(750)
                if score > high_score:
                    high_score = score
                break

            snake_position_list.insert(0, new_position)

            if new_position == (apple_x, apple_y):
                eat_apple = True
                score += 1
                pygame.draw.rect(screen, difficulty.snake_color, (apple_x, apple_y, SQUARE_SIZE, SQUARE_SIZE))
                pos_difference_set = set(grid_positions_list).difference(set(snake_position_list))
                pos_difference_list = list(pos_difference_set)
                apple_x, apple_y = pos_difference_list[random.randrange(0, len(pos_difference_set))]
                pygame.draw.rect(screen, difficulty.apple_color, (apple_x, apple_y, SQUARE_SIZE, SQUARE_SIZE))

            pygame.draw.rect(screen, difficulty.snake_color, (x_coordinate + 2, y_coordinate + 2, SQUARE_SIZE - 4, SQUARE_SIZE - 4))

            if not eat_apple:
                trail_coord = snake_position_list.pop()
                pygame.draw.rect(screen, BG_COLOR, (trail_coord[0], trail_coord[1], SQUARE_SIZE, SQUARE_SIZE))

            eat_apple = False

            pygame.time.Clock().tick(difficulty.speed)
            pygame.display.update()

        draw_game_over(win)
        pygame.display.update()
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and game_over:
                        screen.fill((BG_COLOR))
                        direction = "right"
                        current_direction = "right"
                        x_coordinate = 84
                        y_coordinate = 196
                        apple_x = 336
                        apple_y = 196
                        score = 0
                        game_over = False
                        eat_apple = False
                        win = False

                        pygame.draw.rect(screen, difficulty.snake_color,
                                         (INITIAL_TRAIL_X + 2, INITIAL_TRAIL_Y + 2, SQUARE_SIZE - 4, SQUARE_SIZE - 4))
                        pygame.draw.rect(screen, difficulty.snake_color,
                                         (x_coordinate + 2, y_coordinate + 2, SQUARE_SIZE - 4, SQUARE_SIZE - 4))
                        pygame.draw.rect(screen, difficulty.apple_color, (apple_x, apple_y, SQUARE_SIZE, SQUARE_SIZE))

                        snake_position_list = [(84, 196), (INITIAL_TRAIL_X, INITIAL_TRAIL_Y)]
                    if event.key == pygame.K_c and game_over:
                        screen.fill(BG_COLOR)
                        draw_start_menu()
                        start_running = True
                        game_running = False
                        game_over = False
            pygame.display.update()





