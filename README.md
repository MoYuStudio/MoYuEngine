###### MoYuStudio SUGT06 Dv
Not Enough Space ! 空间不足！ <br/><br/>
=======================

![](https://github.com/MoYuStudio/SUGT06/raw/main/moyu_engine/assets/graphics/tileland/tl1.png)
![](https://github.com/MoYuStudio/SUGT06/raw/main/moyu_engine/assets/graphics/tileland/tl6.png)
![](https://github.com/MoYuStudio/SUGT06/raw/main/moyu_engine/assets/graphics/tileland/tl11.png)
![](https://github.com/MoYuStudio/SUGT06/raw/main/moyu_engine/assets/graphics/tileland/tl16.png)
![](https://github.com/MoYuStudio/SUGT06/raw/main/moyu_engine/assets/graphics/tileland/tl21.png)<br/><br/>

# Game News 游戏新闻

### Game Testers News 游戏测试新闻

            游戏功能性开发已经进入尾声！准备进入内容堆料！
            
            预计 10月底 至 11月初 进行初版功能性测试 版本0.0.1
           
            2月初 开始 游戏性测试（数值调教）

### Game Developers News 游戏开发新闻

            现阶段主要需要开发的模块有（大家可以按需选取研究）：
            
            1.动画机（由@[开发] 永恒 负责，预计9月底需要解决方案或代码）
            2.Steam热更新（由@[策划&开发组长] 辰冰 负责，预计12月底需要解决方案或代码）

# Game Introduction 游戏简介
            《 Not Enough Space ! 空间不足！》是一款建筑类沙盒游戏，讲述了一片漂浮在宇宙之中的破碎之地。
            玩家在游戏中扮演一名领导者，带领人民在有限的空间内发展属于自己的帝国
            或发展科技和军事来捕捉其他碎片扩大领土[无尽模式/沙盒模式]
            或在有限的空间解决发展需求的难题[剧情模式/挑战模式]

###### `本游戏由 MoYuStudio 摸魚社® 100%原创开发`
###### `MoYuStudio 摸魚社® & C-Prismera Tech Corp 淩创科技® reserves the right of final explanation` <br/><br/>

MoYu Engine 文件检索
-------------------
>`moyu_engine` 摸鱼引擎目录（所有的游戏文件的目录)<br/>
>>
>>`assets` 资源目录（所有的 = 资源性质文件 = *贴图文件&字体文件&音乐文件 等 的目录）<br/>
>>>`font` 字体资源目录<br/>
>>>`graphics` 图像资源目录<br/>
>>>`sound` 声音资源目录<br/>
>>
>>`config` 配置目录（所有的 = 游戏运行文件 = *代码文件&存档文件&运行产生文件 等 的目录）<br/>
>>>`components` 模块目录<br/>
>>>`data` 存档目录<br/>
>>>`event` 事件目录<br/>
>>>`states` 状态机目录<br/>
>>>`surface` 窗口目录<br/>
>>>`constants.py` （变量Pyhton文件）<br/>
>>>`font.py` （字体Pyhton文件）<br/>
>>>`graphics.py` （图形Pyhton文件）<br/>
>>>`setup.py` （运行Pyhton文件）<br/>
>>>`sound.py` （声音Pyhton文件）<br/>

更新日志
-------
##### 08/31/2021 更新日志
            新增 部分GUI组件
            新增 部分金融系统
            新增 土地可种植
            新增 时间

##### 08/30/2021 更新日志
            新增 部分GUI组件
            优化 预选层显示

##### 08/27/2021 更新日志
            SUGT06a12 Dv20210827 发布
            项目 底层架构 重构

##### 08/24/2021 更新日志
            项目 底层架构 Debug
            修复 tilemap_button 的 数项 Bug
            新增 button 模块
            开始 使用 sound 模块

##### 08/23/2021 更新日志
            新增 模块 tilemap_button
            新增 模块 tilemap_button 对 tilebutton 进行重制
            修复了 tilebutton 失效 等 问题

##### 08/21/2021 更新日志
            SUGT06a12 Dv20210821 发布
            项目 底层架构 全面升级
            开始 使用 SQLite 数据库
            在 SUGT08 进行测试 模块 数值传入 and 全局变量
            对于 模块 的 重制

##### 08/20/2021 更新日志
            对 scrollbar 模块进行了重制
            修复 scrollbar 模块 移动限制 的 BUG
            新增 scrollbar 滑轮移动 功能
            优化 scrollbar 模块 函数

##### 08/17/2021 更新日志
            修复 scrollbar 输入错误 的 BUG
            新增 scrollbar 移动限制
            优化 scrollbar 模块 函数

##### 08/16/2021 更新日志
            移除 window 窗口目录 由 surface 目录 继承 原 window 窗口目录 的 显示(输出)部分
            新增 event 事件目录 继承 原 window 窗口目录 的 事件(输入)部分          

##### 08/15/2021 更新日志
            新增 scrollbar 模块
            尝试 scrollbar 应用性
            测试 display层[pygame.Surface] 功能性

##### 08/13/2021 更新日志
            SUGT06a12 Dv20210813 发布
            开始使用 display层[pygame.Surface] 逐渐替代 原先的 window层[mainwindow.blit]
            测试 线性放大 功能性

##### 08/11/2021 更新日志
            API 更换回 Pygame
            SUGT07 降级回 SUGT06

##### 08/09/2021 更新日志
            更换 API 由 Pygame 更换为 Pyglet
            SUGT06 升级 SUGT07

##### 07/26/2021 更新日志
            新增 MoYu Engine 文件检索

##### 07/25/2021 更新日志
            SUGT06a12 Dv20210725 发布
            上传 SUGT06a12 至 GitHub

<br/>

![](https://github.com/MoYuStudio/SUGT06/raw/main/moyu_engine/assets/graphics/tileland/tl1.png)
![](https://github.com/MoYuStudio/SUGT06/raw/main/moyu_engine/assets/graphics/tileland/tl6.png)
![](https://github.com/MoYuStudio/SUGT06/raw/main/moyu_engine/assets/graphics/tileland/tl11.png)
![](https://github.com/MoYuStudio/SUGT06/raw/main/moyu_engine/assets/graphics/tileland/tl16.png)
![](https://github.com/MoYuStudio/SUGT06/raw/main/moyu_engine/assets/graphics/tileland/tl21.png)<br/><br/><br/>
