import arcade
import ctypes
# screen settings
width = 800
height = 600
user32 = ctypes.windll.user32
monitor_width = user32.GetSystemMetrics(0)
monitor_height = user32.GetSystemMetrics(1)

def window_to_screenx(x):
    return (monitor_width/2 - x)
def window_to_screeny(y, h):
    return (y - monitor_height/2 + h)
class BouncingBall(arcade.Window):
    def __init__(self):
        super().__init__(width, height, "ball", resizable=True)
        self.ball_screen_x = width // 2
        self.ball_screen_y = height // 2
        self.ball_radius = 20
        self.dx = 1
        self.dy = 1
        self.set_update_rate(1/600)
        arcade.enable_timings()

    def on_draw(self):
        arcade.Window.clear(self)
        global window_x
        global window_y
        window_x, window_y = self.get_location()
        global blaheight
        blaheight = self.get_size()
        arcade.draw_circle_filled(window_to_screenx(window_x + self.ball_screen_x), window_to_screeny(window_y - self.ball_screen_y, blaheight[1]), self.ball_radius, arcade.color.RED)
        #print(str(window_y) + " window position Y")
        #print(str(blaheight[1]) + " window height")
    def on_update(self, _delta_time):
        winx, winy = self.get_location()
        self.ball_screen_x += self.dx
        self.ball_screen_y += self.dy
        blahnine = self.get_size()
        posx = window_to_screenx(winx + self.ball_screen_x)
        posy = window_to_screeny(winy - self.ball_screen_y, blahnine[1])
        # bounce on screen edges
        twidth, theight = self.get_size()
        if posx > twidth - self.ball_radius:
           self.dx = self.dx * -1
        if posx < 0 + self.ball_radius:
            self.dx = self.dx * -1
        if posy > theight - self.ball_radius:
            self.dy = self.dy * -1
        if posy < 0 + self.ball_radius:
            self.dy = self.dy * -1
if __name__ == "__main__":
    game = BouncingBall()
    arcade.run()
