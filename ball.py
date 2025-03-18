import arcade
import ctypes

width = 800
height = 600
user32 = ctypes.windll.user32
monitor_width = user32.GetSystemMetrics(0)
monitor_height = user32.GetSystemMetrics(1)
window_x = 0
window_y = 0
blaheight = (0, 0)
grav = 0.1
loss = 0.9
bx = 0
by = 0
wdx = 0
wdy = 0

def window_to_screenx(x):
    return (monitor_width/2 - x)
def window_to_screeny(y, h):
    return (y - monitor_height/2 + h)
class BouncingBall(arcade.Window):
    def __init__(self):
        super().__init__(width, height, "ball", resizable=True)
        self.ball_screen_x = window_to_screenx(width // 2)
        self.ball_screen_y = window_to_screeny(height // 2, blaheight[1])
        self.ball_radius = 20
        self.dx = -4
        self.dy = -4
        self.set_update_rate(1/60)

    def on_draw(self):
        arcade.Window.clear(self)
        global bx, by
        self.ball = arcade.draw_circle_filled(bx, by, self.ball_radius, arcade.color.RED)
        self.flip()
    def on_update(self, _delta_time):
        self.dy += grav
        self.ball_screen_x += self.dx
        self.ball_screen_y += self.dy
        global window_x, window_y, blaheight
        global bx, by
        global wdx, wdy
        #all you gotta do now is track the window position over time, get the velocity of it, and check during collisions if the window is moving, then apply that force to the ball when necessary

        
        blaheight = self.get_size()
        window_x, window_y = self.get_location()
        bx, by = window_to_screenx(window_x + self.ball_screen_x), window_to_screeny(window_y - self.ball_screen_y, blaheight[1])

        twidth, theight = blaheight
        if bx > twidth - self.ball_radius:
            self.dx *= loss
            self.dx = self.dx * -1
        if bx < 0 + self.ball_radius:
            self.dx *= loss
            self.dx = self.dx * -1
        if by > theight - self.ball_radius:
            self.dy = self.dy * -1
            self.dy *= loss
        if by < 0 + self.ball_radius:
            self.dy = self.dy * -1
            self.dy *= loss
if __name__ == "__main__":
    game = BouncingBall()
    arcade.run()
