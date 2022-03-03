
import moyu_engine

G = moyu_engine.config.global_config
# 改变窗口的大小 (推荐更改全局变量)
G.window_size = [320*2,180*2]

window = moyu_engine.window.Window()
# 生产出一个图层
surface = moyu_engine.surface.Surface()

# 改变窗口的名字
window.title = 'MY FIRST GAME 我的第一个游戏'

# 生产出的图层
def BackgroundPage():

    # 把这个图层填充成奶绿色 (颜色使用RGB)
    surface.surface.fill((154,255,154))
    # 你想把这个图层绘制的地方 (可以是窗口，可以是另一个图层)
    surface.blit(window.screen)

# 将图层绘制到窗口上 (同一时间只可以绘制一个图层，你可以将多个图层绘制到同一个图层来实现多个图层的效果)
window.blit = BackgroundPage
window.set()
