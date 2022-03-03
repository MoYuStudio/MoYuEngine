
import moyu_engine

moyu_engine.global_config.window_size = [320*2,180*2] # 改变窗口的大小 (推荐更改全局变量)

window = moyu_engine.Window()
surface = moyu_engine.Surface() # 生产出一个图层

window.title = 'MY FIRST GAME 我的第一个游戏' # 改变窗口的名字

def BackgroundPage(): # 生产出的图层

    surface.surface.fill((154,255,154)) # 把这个图层填充成奶绿色 (颜色使用RGB)
    surface.blit(window.screen) # 你想把这个图层绘制的地方 (可以是窗口，可以是另一个图层)

window.blit = BackgroundPage # 将图层绘制到窗口上 (同一时间只可以绘制一个图层，你可以将多个图层绘制到同一个图层来实现多个图层的效果)
window.set()
