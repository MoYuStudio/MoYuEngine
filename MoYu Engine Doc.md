
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
>>>> #### `Window.set`
>>>>>```
>>>>>win.set()
>>>>>```
>>> ### `surface` surface 图层模块<br/>
>>>>
>>> ### `event` event 事件(点击/触摸/交互)模块<br/>
>>>
>>>> #### `Event`<br/>
>>>>>```
>>>>>最小系统
>>>>>ev = c.event.Event()
>>>>>```
>>>> #### `Event.quit`
>>>>>```
>>>>>ev.quit()
>>>>>```
>>> ### `save` save 保存模块<br/>
>>>
>>>> #### `Save`<br/>
>>>>>```
>>>>>最小系统
>>>>>save = c.save.Save()
>>>>>接口
>>>>>save = c.save.Save(path='moyu_engine/save/',slot_name='save',write_data={})
>>>>>
>>>>>path 保存路径 = str 字符串
>>>>>slot_name 存档名 = str 字符串
>>>>>write_data 需要保存的数据 = 字典
>>>>>```
>>>> #### `Save.write`
>>>>>```
>>>>>save.write()
>>>>>```
>>>> #### `Save.read`
>>>>>```
>>>>>save.read()
>>>>>save.read_data 读出存档的数据
>>>>>```