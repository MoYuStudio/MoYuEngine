
### MoYu Engine Documentation
# 摸鱼引擎官方文档

## 安装引擎依赖项

    Unix/MacOS/Linux
        pip3 install -r moyu_engine/moyu_engine_package

    Windows
        pip install -r moyu_engine/moyu_engine_package

## API

> # `moyu_engine` 摸鱼引擎<br/>
>
>> ## `components` 模块<br/>
>>
>>> ### `window` window 窗口模块<br/>
>>>
>>>> #### `Window`<br/>
>>>>>
>>>>>```
>>>>>最小系统
>>>>>win = c.window.Window()
>>>>>接口
>>>>>win = c.window.Window(icon=icon1,title='MoYu Engine',size=[320,180],resizable=True)
>>>>>
>>>>>icon 窗口图标 = pygame bit 比特图
>>>>>title 窗口标题 = str 字符串
>>>>>size 窗口尺寸 = [宽，高] 数组
>>>>>resizable 窗口尺寸可否改变 = True/False 布尔值
>>>>>```
>>>>>
>>>> #### `Window.set`
>>>>>```
>>>>>win.set()
>>>>>```
>>> ### `surface` surface 图层模块<br/>
>>>>
>>> ### `event` event 事件(点击/触摸/交互)模块<br/>
>>>>
>>> ### `save` save 保存模块<br/>
>>>>