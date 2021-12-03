
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
>>> [`window`](#window) 窗口模块<br/>
>>> [`surface`](#surface) 图层模块<br/>
>>> [`page`](#page) 书页模块<br/>
>>> [`event`](#event) 事件(点击/触摸/交互)模块<br/>
>>> [`tilemap`](#tilemap) 瓷砖地图模块<br/>
>>> [`assets`](#assets) 资源模块<br/>
>>> [`save`](#save) 保存模块<br/>
>>
>> [`system`](#system) 系统<br/>
>>
>>> [`gui_system`](#gui_system) gui交互界面系统<br/>
>>> [`map_system`](#map_system) 地图系统<br/>
>>

## API

### <span id = 'components'>`components`</span> 模块 === 积木块

    `components` 模块 是对于SDL2(计算机图形接口)以及Pygame(Python对于SDL2接口的绑定) 与 `moyu_engine` 摸鱼引擎功能的绑定

    其中 `window` 窗口模块 是游戏的最小系统(即弹出一个默认的窗口)
    开发者 可以通过 `模块的接口` 与 `模块沟通` 以达到 `客制化`

    接口使用举例

        `xxx.window_data['title'] = 'test'`

        `xxx`是开发者创建的`实例`(`实例`即 这个积木块的复制品，在引擎中的积木块为样品，开发者每当要使用即复制一块)

        `window_data` 是 window 这个积木的数据 格式始终为 `积木名_data`

        `['title']` 是 window 这个积木的接口 一般没有特别说明即有默认设置 如果不需要修改则无需使用接口

        `'test'` 是 ['title'] 这个接口 要更改的设置 该设置的数据类型可以在文档对应的地方找到
        

### <span id = 'window'>`window`</span> 窗口模块

    'icon':icon1
    'title':'MoYu Engine'
    'size':[320,180]
    'resizable':True

### <span id = 'surface'>`surface`</span> 图层模块

    'blit_window':'',
    'blit_surface':'',
    'surface_size':[1920,1080],
    'background_size':[1920,1080],
    'info_size':[1920,1080],
    'gui_size':[1920,1080],
    'popup_size':[1920,1080],
    'transition_size':[1920,1080],
    'window_size':[1920,1080],

### <span id = 'page'>`page`</span> 书页模块

    'page':'page_data',

### <span id = 'event'>`event`</span> 事件(点击/触摸/交互)模块

### <span id = 'tilemap'>`tilemap`</span> 瓷砖地图模块

    'tilemap':[],
    'boarder':64,
    'tile_size':64,
    'time_speed':100,
    'octaves':2,
    'freq':12,
    'seed':0,

### <span id = 'assets'>`assets`</span> 资源模块

    path = 'moyu_engine/assets'

### <span id = 'save'>`save`</span> 保存模块

    path='moyu_engine/data/',
    slot_name='save',
    write_data={}

### <span id = 'system'>`system`</span> 系统 === 积木堆

    `system` 系统 是 `components` 模块 的 功能化打包

### <span id = 'gui_system'>`gui_system`</span> gui交互界面系统

### <span id = 'map_system'>`map_system`</span> 地图系统