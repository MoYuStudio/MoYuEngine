
### MoYu Engine Documentation
# 摸鱼引擎官方文档

## 安装引擎依赖项

    Pyhton

    Unix/MacOS/Linux
        pip3 install -r moyu_engine/moyu_engine_package

    Windows
        pip install -r moyu_engine/moyu_engine_package


## API引索

> `moyu_engine` 摸鱼引擎<br/>
>
>> [`components`](#components) 模块<br/>
>>
>>> `window` 窗口模块<br/>
>>> `surface` 图层模块<br/>
>>> `page` 页模块<br/>
>>> `event` 事件(点击/触摸/交互)模块<br/>
>>> `tilemap` 瓷砖地图模块<br/>
>>> `assets` 资源模块<br/>
>>> `save` 保存模块<br/>
>>
>> `system` 系统<br/>
>>
>>> `gui_system` gui交互界面系统<br/>
>>> `map_system` 地图系统<br/>
>>

## API

### <span id = 'components'>`components`</span> 模块 === 积木块<br/>

    `components` 模块 是对于SDL2(计算机图形接口)以及Pygame(Python对于SDL2接口的绑定) 与 `moyu_engine` 摸鱼引擎功能的绑定

    其中 `window` 窗口模块 是游戏的最小系统(即弹出一个默认的窗口)
    开发者 可以通过 `模块的接口` 与 `模块沟通` 以达到 `客制化`

    接口使用举例

        `xxx.window_data['title'] = 'test'`

        `xxx`是开发者创建的`实例`(`实例`即 这个积木块的复制品，在引擎中的积木块为样品，开发者每当要使用即复制一块)

        `window_data` 是 window 这个积木的数据 格式始终为 `积木名_data`

        `['title']` 是 window 这个积木的接口 一般没有特别说明即有默认设置 如果不需要修改则无需使用接口

        `'test'` 是 ['title'] 这个接口 要更改的设置 该设置的数据类型可以在文档对应的地方找到

### <span id = 'components1'>`components`</span> 模块 === 积木块<br/>