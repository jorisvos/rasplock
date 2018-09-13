from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

def show_message(message, background_color=(0, 0, 0), foreground_color=(255, 255, 255), speed=0.10):
    sense.show_message(message, text_colour=foreground_color, back_colour=background_color, scroll_speed=speed)
