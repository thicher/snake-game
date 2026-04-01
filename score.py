import pygame
from constants import *

class Score:
    def __init__(self):
        self.score = 0
        self.food_eaten = 0
        self.speed_level = 0
        self.font = pygame.font.Font(None, 36)
        self.high_score = 0
        self.load_high_score()

    def add(self, points=10):
        self.score += points
        self.food_eaten += 1
        if self.food_eaten % SPEED_INCREASE_FOOD == 0 and self.speed_level < MAX_SPEED_LEVEL:
            self.speed_level += 1
        if self.score > self.high_score:
            self.high_score = self.score

    def get_current_speed(self):
        return SPEED + (self.speed_level * SPEED_INCREASE_AMOUNT)

    def reset(self):
        self.score = 0
        self.food_eaten = 0
        self.speed_level = 0

    def load_high_score(self):
        try:
            with open('high_score.txt', 'r') as f:
                self.high_score = int(f.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as f:
                f.write(str(self.high_score))

    def draw(self, surface):
        score_text = self.font.render(f'得分: {self.score}', True, WHITE)
        high_score_text = self.font.render(f'最高分: {self.high_score}', True, YELLOW)
        speed_text = self.font.render(f'速度: {self.get_current_speed()} (等级{self.speed_level})', True, (255, 100, 100))

        surface.blit(score_text, (10, 10))
        surface.blit(high_score_text, (10, 40))
        surface.blit(speed_text, (10, 70))
