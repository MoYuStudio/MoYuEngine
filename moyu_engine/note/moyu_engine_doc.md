
### MoYu Engine Documentation
# 摸鱼引擎官方文档

## 目录
[`初次使用`](#FirstTimeUse)

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

## 你的第一个游戏

### 创建一个窗口

    ```

    import moyu_engine

    window = moyu_engine.components.window.Window()

    window.set()

    ```

## API引索