import pyray

class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def is_mouse_over(self):
        mouse_pos = pyray.get_mouse_position()
        return (
            mouse_pos.x >= self.x and
            mouse_pos.x <= self.x + self.width and
            mouse_pos.y >= self.y and
            mouse_pos.y <= self.y + self.height
        )

    def draw(self):
        if self.is_mouse_over():
            pyray.draw_rectangle(self.x, self.y, self.width, self.height, pyray.GRAY)
        else:
            pyray.draw_rectangle(self.x, self.y, self.width, self.height, pyray.DARKGRAY)

        pyray.draw_text(self.text, self.x + 20, self.y + self.height // 2 - 10, 20, pyray.WHITE)

# Button properties
button_x = 100
button_y = 100
button_w = 200
button_h = 100

# Create the button instance
button = Button(button_x, button_y, button_w, button_h, "Click Me!")

# Main game loop
pyray.init_window(800, 600, "Mouse Button Detection")

while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.clear_background(pyray.RAYWHITE)

    # Draw the button
    button.draw()

    pyray.end_drawing()

pyray.close_window()
