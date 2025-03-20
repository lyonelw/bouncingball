import arcade
import ctypes
import time


width = 800
height = 600
user32 = ctypes.windll.user32
monitor_width = user32.GetSystemMetrics(0)
monitor_height = user32.GetSystemMetrics(1)
window_x = 0
window_y = 0
blaheight = (0, 0)
grav = 0.2
loss = 0.8
bx = 0
by = 0
wdx = 0
wdy = 0
wdsx = 0
wdsy = 0
maxspeed = 5
hist = [(0,0),(0,0),(0,0),(0,0),(0,0)]
histsize = [(0,0),(0,0),(0,0),(0,0),(0,0)]
collisions = 0

def window_to_screenx(x):
    return (monitor_width/2 - x)
def window_to_screeny(y, h):
    return (y - monitor_height/2 + h)
def scoot(mylist, pos):
    mylist.pop(0)
    mylist.append(pos)
    return mylist
def avglist(mylist):
    x_start, y_start = mylist[0]
    x_end, y_end = mylist[-1]

    return x_end - x_start, y_end - y_start
class BouncingBall(arcade.Window):
    def __init__(self):
        super().__init__(width, height, "ball", resizable=True)
        self.ball_screen_x = window_to_screenx(width // 2)
        self.ball_screen_y = window_to_screeny(height // 2, blaheight[1])
        self.ball_radius = 25
        self.dx = -1
        self.dy = -1
        self.set_update_rate(1/144)

    def on_draw(self):
        arcade.Window.clear(self)
        global bx, by
        self.ball = arcade.draw_circle_filled(bx, by, self.ball_radius, arcade.color.RED)
    def on_update(self, _delta_time):
        global window_x, window_y, blaheight
        global bx, by
        global wdx, wdy, hist, histsize
        global wdsx, wdsy, maxspeed, collisions
        #print(f"x: {self.dx} || y:{self.dy}")
        #FIX GRAVITY SO YOU DONT FUCKING SUCK
        self.dy += grav
        self.ball_screen_x += self.dx
        self.ball_screen_y += self.dy
        print(collisions)
        blaheight = self.get_size()
        window_x, window_y = self.get_location()
        bx, by = window_to_screenx(window_x + self.ball_screen_x), window_to_screeny(window_y - self.ball_screen_y, blaheight[1])
        hist = scoot(hist, (window_x, window_y))
        histsize = scoot(histsize, blaheight)
        wdsx, wdsy = avglist(histsize)
        wdx, wdy = avglist(hist)
        #print(f"changex: {wdsx}, changey: {wdsy}")
        twidth, theight = blaheight
        if bx > twidth - self.ball_radius:
            collisions+=1
            self.dy *= loss
            self.dx *= loss

            self.dy *= 1
            self.dx *= 1

            self.dx = self.dx * -1
            
            self.dx -= (wdx / 2)
            self.dx -= (wdsx / 2)
        if bx < 0 + self.ball_radius:
            collisions+=1

            self.dy *= loss
            self.dx *= loss

            self.dy *= 1
            self.dx *= 1
            
            self.dx = self.dx * -1
            
            self.dx -= (wdx / 2)
            self.dx -= (wdsx / 2)
        if by > theight - self.ball_radius:
            collisions+=1

            self.dy *= loss
            self.dx *= loss

            self.dy *= 1
            self.dx *= 1
            
            self.dy = self.dy * -1
            
            self.dy += (wdy / 2)
            self.dy -= (wdsy / 2)
        if by < 0 + self.ball_radius:
            collisions+=1

            self.dy *= loss
            self.dx *= loss

            self.dy *= 1
            self.dx *= 1
            
            self.dy = self.dy * -1
            
            self.dy += (wdy / 2)
            self.dy += (wdsy / 2)
if __name__ == "__main__":
    game = BouncingBall()
    arcade.run()
