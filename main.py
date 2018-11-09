import random

import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_ENEMY = 0.4
SPRITE_SCALING_SHOT = 0.08

MOVEMENT_SPEED = 3
ENEMY_MOVEMENT_SPEED = 120
ENEMY_SCREEN_SPACING = 40

SHOT_MOVEMENT_SPEED = 200

# ENEMY_GENERATION_SPEED = 10
ENEMY_GENERATION_PROBABILITY = 0.01


class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class Enemy(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Shot(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        # self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.shot_list = arcade.SpriteList()

        self.player_sprite = Player("img/player.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 150
        self.player_sprite.center_y = 50


    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.player_sprite.draw()

        for enemy in self.enemy_list:
            enemy.draw()
        for shot in self.shot_list:
            shot.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.player_sprite.update()
        for enemy in self.enemy_list:
            enemy.change_x = - ENEMY_MOVEMENT_SPEED * delta_time
            enemy.change_y = 0

            enemy.update()

        for shot in self.shot_list:
            shot.change_x = SHOT_MOVEMENT_SPEED * delta_time
            shot.change_y = 0
            shot.update()

        if random.random() < ENEMY_GENERATION_PROBABILITY:
            enemy_sprite = Enemy("img/enemy.png", SPRITE_SCALING_ENEMY)
            self.enemy_list.append(enemy_sprite)
            enemy_sprite.center_x = SCREEN_WIDTH
            enemy_sprite.center_y = random.randint(ENEMY_SCREEN_SPACING, SCREEN_HEIGHT-ENEMY_SCREEN_SPACING)

        for enemy in self.enemy_list:
            for shot in self.shot_list:
                if (arcade.check_for_collision(enemy, shot)):
                    self.enemy_list.remove(enemy)
                    self.shot_list.remove(shot)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            shot_sprite = Shot("img/shot.png", SPRITE_SCALING_SHOT)
            shot_sprite.center_x = self.player_sprite.center_x + self.player_sprite.width/2
            shot_sprite.center_y = self.player_sprite.center_y
            self.shot_list.append(shot_sprite)


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
