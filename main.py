import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_ENEMY = 0.4

MOVEMENT_SPEED = 3
ENEMY_MOVEMENT_SPEED = 2


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

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

        # self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_sprite = Player("img/player.png", SPRITE_SCALING_PLAYER)
        self.enemy_sprite = arcade.Sprite("img/enemy.png", SPRITE_SCALING_ENEMY)

        self.enemy_list.append(self.enemy_sprite)

        self.player_sprite.center_x = 150
        self.player_sprite.center_y = 50

        self.enemy_sprite.center_x = 500
        self.enemy_sprite.center_y = 300


    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.player_sprite.draw()
        self.enemy_sprite.draw()
        # Your drawing code goes here

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.player_sprite.update()
        for enemy in self.enemy_list:
            self.enemy_sprite.change_x = -ENEMY_MOVEMENT_SPEED
            self.enemy_sprite.change_y = 0
            enemy.update()
        pass

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
