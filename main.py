
import moyu_engine

window = moyu_engine.components.window.Window()
surface = moyu_engine.components.surface.Surface()

def page1():

    surface.surface.fill((255,55,55,255))

    surface.blit(window.screen)

window.blit = page1
window.set()



