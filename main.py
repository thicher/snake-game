import pygame
import sys
from snake import Snake
from food import Food
from score import Score
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('贪吃蛇 - Snake Game')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        self.game_over = False

        self.snake = Snake()
        self.food = Food()
        self.score = Score()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()

            if not self.paused and not self.game_over:
                self.update()

            self.draw()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False

                elif event.key == pygame.K_SPACE:
                    self.paused = not self.paused

                elif event.key == pygame.K_r and self.game_over:
                    self.reset_game()

                elif not self.paused and not self.game_over:
                    self.snake.handle_key(event.key)

    def update(self):
        if not self.snake.move():
            self.game_over = True
            self.score.save_high_score()
            return

        if self.snake.get_head_position() == self.food.position:
            self.snake.grow()
            self.food.randomize_position()
            self.score.add()

            while self.food.position in self.snake.positions:
                self.food.randomize_position()

    def draw(self):
        self.screen.fill(BG_COLOR)

        if self.game_over:
            self.draw_game_over()
        elif self.paused:
            self.draw_paused()
        else:
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.score.draw(self.screen)

        pygame.display.flip()

    def draw_paused(self):
        font = pygame.font.Font(None, 48)
        text = font.render('游戏暂停 - Press SPACE', True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.screen.blit(text, text_rect)

    def draw_game_over(self):
        font = pygame.font.Font(None, 48)
        game_over_text = font.render('游戏结束!', True, RED)
        score_text = font.render(f'最终得分: {self.score.score}', True, WHITE)
        restart_text = font.render('按 R 重新开始', True, YELLOW)
        quit_text = font.render('按 Q 退出', True, GRAY)

        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 60))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 90))

        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(restart_text, restart_rect)
        self.screen.blit(quit_text, quit_rect)

    def reset_game(self):
        self.snake.reset()
        self.food.randomize_position()
        self.score.reset()
        self.game_over = False
        self.paused = False


if __name__ == '__main__':
    game = Game()
    game.run()
