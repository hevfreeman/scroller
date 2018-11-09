import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_ENEMY = 0.4

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

        # self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("img/player.png", SPRITE_SCALING_PLAYER)
        self.enemy_sprite = arcade.Sprite("img/enemy.png", SPRITE_SCALING_ENEMY)

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
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
