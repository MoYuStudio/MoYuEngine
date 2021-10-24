import pyglet

def foo(value):
    print("I'm in a loop...")

def main():
    w = pyglet.window.Window()
    # @w.event
    # def on_draw():
    #     foo(None)
    pyglet.clock.schedule_interval(foo, 1.0)
    pyglet.app.run()

main()