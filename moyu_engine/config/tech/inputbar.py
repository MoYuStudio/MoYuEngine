import pygame
 
 
class TextBox:
    def __init__(self, w, h, x, y, font=None, callback=None):
        """
        :param w:文本框宽度
        :param h:文本框高度
        :param x:文本框坐标
        :param y:文本框坐标
        :param font:文本框中使用的字体
        :param callback:在文本框按下回车键之后的回调函数
        """
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.text = ""  # 文本框内容
        self.callback = callback
        # 创建
        self.__surface = pygame.Surface((w, h))
        # 如果font为None,那么效果可能不太好，建议传入font，更好调节
        if font is None:
            self.font = pygame.font.Font(None, 32)  # 使用pygame自带字体
        else:
            self.font = font
 
    def draw(self, dest_surf):
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        dest_surf.blit(self.__surface, (self.x, self.y))
        dest_surf.blit(text_surf, (self.x, self.y + (self.height - text_surf.get_height())),
                       (0, 0, self.width, self.height))
 
    def key_down(self, event):
        unicode = event.unicode
        key = event.key
 
        # 退位键
        if key == 8:
            self.text = self.text[:-1]
            return
 
        # 切换大小写键
        if key == 301:
            return
 
        # 回车键
        if key == 13:
            if self.callback is not None:
                self.callback()
            return
 
        if unicode != "":
            char = unicode
        else:
            char = chr(key)
 
        self.text += char
 
 
def callback():
    print("回车测试")
 
 
def main():
    # 英文文本框demo
    pygame.init()
    winSur = pygame.display.set_mode((640, 480))
    # 创建文本框
    text_box = TextBox(200, 30, 200, 200, callback=callback)
 
    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                text_box.key_down(event)
        pygame.time.delay(33)
        winSur.fill((0, 50, 0))
        text_box.draw(winSur)
        pygame.display.flip()
 
 
if __name__ == '__main__':
    main()
