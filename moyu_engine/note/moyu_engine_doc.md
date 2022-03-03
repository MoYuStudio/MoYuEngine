
### MoYu Engine Documentation
# 摸鱼引擎官方文档

## 目录
> ### [初次使用](#FirstTimeUse)
> ### [你的第一个游戏](#UrFirstGame)
> ### [API引索](#API)

## <span id = 'FirstTimeUse'>初次使用</span>

### 安装IDE及开发环境

    安装 Pyhton 3.8.10

    安装 Visual Studio Code

    安装 Visual Studio Code 的 Python 插件

### 安装引擎依赖项

    Unix / MacOS / Linux 用户
        PyPl(国际): pip3 install -r moyu_engine\note\moyu_engine_package
        清华镜像(国内): pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r moyu_engine\note\moyu_engine_package

    Windows 用户
        PyPl(国际): pip install -r moyu_engine\note\moyu_engine_package
        清华镜像(国内): pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r moyu_engine\note\moyu_engine_package

## <span id = 'UrFirstGame'>你的第一个游戏</span>

### 创建一个窗口

    ```

    import moyu_engine

    window = moyu_engine.components.window.Window()

    window.set()

    ```

## <span id = 'API'>API</span>


### 引索

> `moyu_engine` 摸鱼引擎<br/>
>
>> [`assets`](#APIassets) 资源<br/>
>>
>> [`components`](#APIcomponents) 组件<br/>
>>
>>> [`window`](#APIwindow) 窗口<br/>
>>> [`surface`](#APIsurface) 图层<br/>
>>> [`page`](#APIpage) 页面<br/>
>>
>> [`config`](#APIconfig) 配置<br/>
>>
>>> [`global_config`](#APIglobalconfig) 全局配置<br/>
>>
>

### <span id = 'APIassets'>`assets`</span> 资源

    这一部分是引擎自带的资源，如果你对我们的引擎没有充分了解之前请勿修改以防造成严重错误！

### <span id = 'components'>`components`</span> 组件

    组件 是引擎逻辑的核心，你可以把每一个组件想象成一块块积木，游戏就是由一块块积木组成！

    配置 是每块积木的信息，比如积木的颜色/大小/形状，同一种积木正因其不同的信息拥有不同的玩法！

#### <span id = 'APIwindow'>`window`</span> 窗口

    功能： 创建一个窗口 (在玩家的电脑上弹出(创建)一个窗)

    icon = pygame.image.load('moyu_engine/assets/graphics/logo/tileland1.png')
    图标

    title = 'MoYu Engine'
    标题

    run = True
    是否运行

    size = G.window_size
    尺寸

    fps = 60

    clock = None

    resizable = True
    图标尺寸是否可更改

#### <span id = 'APIsurface'>`surface`</span> 图层

    size = [1920,1080]

    transform_window = True

#### <span id = 'APIpage'>`page`</span> 页面
        

### <span id = 'config'>`APIconfig`</span> 配置

#### <span id = 'APIglobalconfig'>`global_config`</span> 全局配置

    window_size = [320,180]
    窗口尺寸

