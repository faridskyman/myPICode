from sense_hat import SenseHat
from time import sleep
from random import randint
from random import choice

sense = SenseHat();
sense.set_rotation(180);

#sense.show_message("hello there");

# define all function here.

def textSample2():
    sense.show_letter("O",text_colour=[255, 0, 0])
    sleep(1)
    sense.show_letter("M",text_colour=[0, 0, 255])
    sleep(1)
    sense.show_letter("G",text_colour=[0, 255, 0])
    sleep(1)
    sense.show_letter("!",text_colour=[0, 0, 0], back_colour=[255, 255, 255])
    sleep(1)
    sense.clear()
    return


def randLetters():
    r = randint(0,255)
    sense.show_letter("O", text_colour=[r, 0, 0])
    sleep(1)

    r = randint(0,255)
    sense.show_letter("M", text_colour=[0, 0, r])
    sleep(1)

    r = randint(0,255)
    sense.show_letter("G", text_colour=[0, r, 0])
    sleep(1)

    sense.show_letter("!", text_colour=[0, 0, 0], back_colour=[255, 255, 255])
    sleep(1)
    sense.clear()
    return


def simple_image():
    sense.set_pixel(2, 2, [0, 0, 255])
    sense.set_pixel(4, 2, [0, 0, 255])
    sense.set_pixel(3, 4, [100, 0, 0])
    sense.set_pixel(1, 5, [255, 0, 0])
    sense.set_pixel(2, 6, [255, 0, 0])
    sense.set_pixel(3, 6, [255, 0, 0])
    sense.set_pixel(4, 6, [255, 0, 0])
    sense.set_pixel(5, 5, [255, 0, 0])
    sleep(2)
    sense.clear();
    return

def rainbow():
    r = [255,0,0]
    o = [255,127,0]
    y = [255,255,0]
    g = [0,255,0]
    b = [0,0,255]
    i = [75,0,130]
    v = [159,0,255]
    e = [0,0,0]

    image = [
    e,e,e,e,e,e,e,e,
    e,e,e,r,r,e,e,e,
    e,r,r,o,o,r,r,e,
    r,o,o,y,y,o,o,r,
    o,y,y,g,g,y,y,o,
    y,g,g,b,b,g,g,y,
    b,b,b,i,i,b,b,b,
    b,i,i,v,v,i,i,b
    ]

    sense.set_pixels(image)
    sleep(0.4)
    sense.clear();
    sleep(0.2);
    sense.set_pixels(image)
    sleep(0.4)
    sense.clear();
    return

def spinning_j():
    sense.show_letter("F")

    angles = [0, 90, 180, 270, 0, 90, 180, 270, 0, 90, 180, 270, 0, 90, 180, 270]
    for r in angles:
        sense.set_rotation(r)
        sleep(0.1)
    return;

def eyes():
    w = [150, 150, 150]
    b = [0, 0, 255]
    e = [0, 0, 0]

    image = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    w,w,w,e,e,w,w,w,
    w,w,b,e,e,w,w,b,
    w,w,w,e,e,w,w,w,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

    sense.set_pixels(image)

    while True:
        sleep(1)
        sense.flip_h()
    return;


def clearScreen():
    sense.clear();
    return;


def env():
    while True:
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()

        t = round(t, 1)
        p = round(p, 1)
        h = round(h, 1)

        msg = "Temp = {0}c, Pres = {1}, Hum = {2}%".format(t,p,h)

        sense.show_message(msg, scroll_speed=0.05)
    return;
        

def scroll_env():
    while True:
        t = sense.get_temperature()
        p = sense.get_pressure()
        h = sense.get_humidity()

        t = round(t, 1)
        p = round(p, 1)
        h = round(h, 1)

        if t > 18.3 and t < 26.7:
            bg = [0, 100, 0]  # green
        else:
            bg = [100, 0, 0]  # red

        msg = "Temp:{0}C, Pres:{1}, Hum:{2}%".format(t, p, h)

        sense.show_message(msg, scroll_speed=0.05, back_colour=bg)
    return

def shake():
    # this detect shake movement made and rather cool!
    while True:
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 1 or y > 1 or z > 1:
            sense.show_letter("!", text_colour=[255, 0, 0])
        else:
            sense.clear()
    return;




# this always ensures the letter J is correct no matter how the device is
#   turned, this is after i caliberate for my setup.
def rotating_j():
    sense.show_letter("J")

    while True:
        x = sense.get_accelerometer_raw()['x']
        y = sense.get_accelerometer_raw()['y']
        z = sense.get_accelerometer_raw()['z']

        x = round(x, 0)
        y = round(y, 0)

        if x == -1:
            sense.set_rotation(90)
            print("a_90")
        elif y == 1:
            sense.set_rotation(0)
            print("a_0")
        elif y == -1:
            sense.set_rotation(180)
            print("a_180")
        else:
            sense.set_rotation(270)
            print("a_270")
    return;



# game using all the sensors, but its not caliberate for my setup.
def reaction_game():
    # set up the colours (white, green, red, empty)

    w = [150, 150, 150]
    g = [0, 255, 0]
    r = [255, 0, 0]
    e = [0, 0, 0]

    # create images for three different coloured arrows

    arrow = [
    e,e,e,w,w,e,e,e,
    e,e,w,w,w,w,e,e,
    e,w,e,w,w,e,w,e,
    w,e,e,w,w,e,e,w,
    e,e,e,w,w,e,e,e,
    e,e,e,w,w,e,e,e,
    e,e,e,w,w,e,e,e,
    e,e,e,w,w,e,e,e
    ]

    arrow_red = [
    e,e,e,r,r,e,e,e,
    e,e,r,r,r,r,e,e,
    e,r,e,r,r,e,r,e,
    r,e,e,r,r,e,e,r,
    e,e,e,r,r,e,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,r,r,e,e,e
    ]

    arrow_green = [
    e,e,e,g,g,e,e,e,
    e,e,g,g,g,g,e,e,
    e,g,e,g,g,e,g,e,
    g,e,e,g,g,e,e,g,
    e,e,e,g,g,e,e,e,
    e,e,e,g,g,e,e,e,
    e,e,e,g,g,e,e,e,
    e,e,e,g,g,e,e,e
    ]

    pause = 3
    score = 0
    angle = 0
    play = True

    sense.show_message("Keep the arrow pointing up", scroll_speed=0.05, text_colour=[100,100,100])

    while play:
        last_angle = angle
        while angle == last_angle:
            angle = choice([0, 90, 180, 270])
        sense.set_rotation(angle)
        sense.set_pixels(arrow)
        sleep(pause)
        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = round(x, 0)
        y = round(y, 0)

        print(angle)
        print(x)
        print(y)

        if x == -1 and angle == 180:
            sense.set_pixels(arrow_green)
            score += 1
        elif x == 1 and angle == 0:
          sense.set_pixels(arrow_green)
          score += 1
        elif y == -1 and angle == 90:
          sense.set_pixels(arrow_green)
          score += 1
        elif y == 1 and angle == 270:
          sense.set_pixels(arrow_green)
          score += 1
        else:
          sense.set_pixels(arrow_red)
          play = False

        pause = pause * 0.95
        sleep(0.5)

    msg = "Your score was %s" % score
    sense.show_message(msg, scroll_speed=0.05, text_colour=[100, 100, 100])
    return;
        

# run all commands here.

# textSample2();
# randLetters();
# simple_image();
# rainbow();
# spinning_j();
# eyes();
# env()
# scroll_env();
# shake();
# rotating_j();
reaction_game();

clearScreen();

