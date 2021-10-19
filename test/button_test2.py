import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *

from panda3d.core import TextNode

start_page = True
main_page = False

a = 0

if start_page == True:
    bk_text = "Start Game ?!"
    textObject = OnscreenText(text=bk_text, pos=(0,0), scale=0.1,fg=(1, 1, 1, 1), align=TextNode.ACenter, mayChange=1)

    def setText():
        global a,start_page,main_page

        bk_text = "Button Clicked"
        textObject.setText(bk_text)
        a += 100
        print(a)

        start_page = False
        main_page = True

        return a,start_page,main_page

    b = DirectButton(text=("OK", "click!", "rolling over", "disabled"),pos=(0,0,-0.5), scale=.05, command=setText)



if main_page == True:
    
    bk_text = "This is my Demo"
    textObject = OnscreenText(text=bk_text, pos=(0.95,-0.95), scale=0.07,fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter, mayChange=1)

    # def setText():
    #         global a

    #         bk_text = "Button Clicked"
    #         textObject.setText(bk_text)
    #         a += 100
    #         print(a)

    #         return a

    # b = DirectButton(text=("OK", "click!", "rolling over", "disabled"), scale=.05, command=setText)


base.run()
print(a)