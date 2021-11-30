
# MoYu Engine Documentation
# 摸鱼引擎官方文档

## 安装引擎依赖项

    Unix/MacOS/Linux
        pip3 install -r moyu_engine/moyu_engine_package

    Windows
        pip install -r moyu_engine/moyu_engine_package

## API

>`moyu_engine` 摸鱼引擎<br/>
>><br/>
>>>`components` 模块<br/>
>>><br/>
>>>>`window` window 窗口模块<br/>
>>>>><br/>
>>>>>`Window`<br/>
>>>>>最小系统<br/>
>>>>>win = c.window.Window()<br/>
>>>>>接口<br/>
>>>>>win = c.window.Window(icon=icon1,title='MoYu Engine',size=[320,180],resizable=True)<br/>
>>>>><br/>
>>>>><br/>
>>>>>`Window.set`<br/>
>>>>>win.set()<br/>
>>>>><br/>
>>>>`surface` surface 图层模块<br/>
>>>>><br/>
>>>>`event` event 事件(点击/触摸/交互)模块<br/>
>>>>><br/>
>>>>`save` save 保存模块<br/>
>>>>><br/>
