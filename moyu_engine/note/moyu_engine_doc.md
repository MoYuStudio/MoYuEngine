
### MoYu Engine Documentation
# 摸鱼引擎官方文档

## 安装引擎依赖项

    Pyhton

    Unix/MacOS/Linux
        pip3 install -r moyu_engine/data/moyu_engine_package

    Windows
        pip install -r moyu_engine/data/moyu_engine_package


## API引索

> `moyu_engine` 摸鱼引擎<br/>
>
>> [`components`](#components) 模块<br/>
>>
>>> [`window`](#window) 窗口<br/>
>>> [`surface`](#surface) 图层<br/>
>>> [`page`](#page) 页面<br/>
>>> [`ui`](#ui) ui<br/>
>>> [`event`](#event) 事件(点击/触摸/交互)<br/>
>>> [`tile`](#tile) 瓷砖<br/>
>>> [`tilemap`](#tilemap) 瓷砖地图<br/>
>>> [`assets`](#assets) 资源<br/>
>>> [`data`](#data) 数据<br/>
>>> [`save`](#save) 保存<br/>
>>
>> [`system`](#system) 系统<br/>
>>
>>> [`gui_system`](#gui_system) gui交互界面<br/>
>>> [`map_system`](#map_system) 地图<br/>
>>

## API

### <span id = 'components'>`components`</span> 模块 === 积木块

    `components` 模块 是对于SDL2(计算机图形接口)以及Pygame(Python对于SDL2接口的绑定) 与 `moyu_engine` 摸鱼引擎功能的绑定

    其中 `window` 窗口模块 是游戏的最小系统(即弹出一个默认的窗口)
    开发者 可以通过 `模块的接口` 与 `模块沟通` 以达到 `客制化`

    接口使用举例

        `xxx.config['title'] = 'test'`

        `xxx`是开发者创建的`实例`(`实例`即 这个积木块的复制品，在引擎中的积木块为样品，开发者每当要使用即复制一块)

        `config` 是 window 这个积木的数据 格式始终为 `config`

        `['title']` 是 window 这个积木的接口 一般没有特别说明即有默认设置 如果不需要修改则无需使用接口

        `'test'` 是 ['title'] 这个接口 要更改的设置 该设置的数据类型可以在文档对应的地方找到
        

### <span id = 'window'>`window`</span> 窗口

    'icon':icon1
    'title':'MoYu Engine'
    'size':[320,180]
    'resizable':True

### <span id = 'surface'>`surface`</span> 图层

    'blit_window':'',
    'blit_surface':'',
    'surface_size':[1920,1080],
    'background_size':[1920,1080],
    'info_size':[1920,1080],
    'gui_size':[1920,1080],
    'popup_size':[1920,1080],
    'transition_size':[1920,1080],
    'window_size':[1920,1080],

### <span id = 'page'>`page`</span> 页面

    'page':'page_data',

### <span id = 'ui'>`ui`</span> ui

    'blit_window':'',
    'button_image':'',
    'ui_event_preview':False,
    'motion_pos':[-1,-1],
    'click_pos':[-1,-1],
    'display_pos':[0,0],
    'button_width':64,
    'button_hight':64,

### <span id = 'event'>`event`</span> 事件(点击/触摸/交互)

    'move':[0,0],
    'zoom':0,
    'move_speed':10,

### <span id = 'tile'>`tile`</span> 瓷砖

### <span id = 'tilemap'>`tilemap`</span> 瓷砖地图

    'tilemap':[],
    'boarder':64,
    'tile_size':64,
    'time_speed':100,
    'octaves':2,
    'freq':12,
    'seed':0,

### <span id = 'assets'>`assets`</span> 资源

    path = 'moyu_engine/assets'

### <span id = 'data'>`data`</span> 数据

    'xlsx_path' : r'C:\Users\WilsonVinson\Documents\GitHub\SUGT06\moyu_engine\data\tile.xlsx',
    'nrows_or_ncols' : 'ncols',

### <span id = 'save'>`save`</span> 保存

    'path':'moyu_engine/data/',
    'slot_name':'save',
    'write_data':{},

### <span id = 'system'>`system`</span> 系统 === 积木堆

    `system` 系统 是 `components` 模块 的 功能化打包

### <span id = 'gui_system'>`gui_system`</span> gui交互界面

### <span id = 'map_system'>`map_system`</span> 地图