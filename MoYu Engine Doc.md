
### MoYu Engine Documentation
# 摸鱼引擎官方文档

## 安装引擎依赖项

    Unix/MacOS/Linux
        pip3 install -r moyu_engine/moyu_engine_package

    Windows
        pip install -r moyu_engine/moyu_engine_package

## API

### `moyu_engine` 摸鱼引擎<br/>

* #### `components` 模块<br/>

* + ##### `window` window 窗口模块<br/>

* + - ###### `Window`<br/>

    最小系统
    win = c.window.Window()
    接口
    win = c.window.Window(icon=icon1,title='MoYu Engine',size=[320,180],resizable=True)

* + - ###### `Window.set`

    win.set()

* + ##### `surface` surface 图层模块<br/>

* + ##### `event` event 事件(点击/触摸/交互)模块<br/>

* + ##### `save` save 保存模块<br/>
