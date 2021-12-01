###### MoYuStudio SUGT06 Dv
Tinyland 弹丸之地 <br/><br/>
=======================

![](https://github.com/MoYuStudio/SUGT06/raw/moyu_engine/assets/graphics/readme/snap2021-10-08-17-41-47.png)<br/><br/>

# Game News 游戏新闻

            For some reason back to the Pygame
            
# Game Introduction 游戏简介
            《 Tinyland 弹丸之地 》是一款建筑类沙盒游戏，讲述了一片漂浮在宇宙之中的破碎之地。
            玩家在游戏中扮演一名领导者，带领人民在有限的空间内发展属于自己的帝国
            或发展科技和军事来捕捉其他碎片扩大领土[无尽模式/沙盒模式]
            或在有限的空间解决发展需求的难题[剧情模式/挑战模式]

###### `本游戏由 MoYuStudio 摸魚社® 100%原创开发`
###### `MoYuStudio 摸魚社® & C-Prismera Tech Corp 淩创科技® reserves the right of final explanation` <br/><br/>

### Game Doc 游戏文档
            移动视角：W A S D & 方向键 上下左右
            缩放视角：Q E
            还原视角：Z
            随机重制地图(测试使用)：X
            建造：B
            收获：R
            保存：M

### 项目组 QQ群
            837240160

### 项目组 资源中心
            https://shimo.im/sheets/h9QPG6HQCgGgQQHx/uj0ib/

Update Log 更新日志
-------
##### 11/30/2021 Update Log
            MoYu Engine Documentation 摸鱼引擎官方文档 上线
            MoYu Engine 摸鱼引擎 新增 window 模块
            MoYu Engine 摸鱼引擎 新增 event 模块
            MoYu Engine 摸鱼引擎 新增 surface 模块
            MoYu Engine 摸鱼引擎 新增 save 模块

##### 10/20/2021 Update Log
            For some reason back to the Pygame
            
##### 10/08/2021 更新日志
            GOOD NEWS : 3D IS COMMING !!!
            框架API由 Pygame 更改为 Panda 3D
            
##### 09/29/2021 更新日志
            WindowsSystem 视窗系统 更新
            
##### 09/29/2021 更新日志
            AssetsSystem 资源系统 更新

##### 09/25/2021 更新日志
            SUGT06a17 引擎框架己更新
            更改框架运行逻辑
            由面向过程更新为面向对象
            字典化Data池，优化引用
            开始使用System类封装数个函数
            多线程并发，提升运行速度

##### 09/23/2021 更新日志
            SUGT06a16 底层架构搭建
            SUGT06a16 基于 SUGT06a12 的 面向过程 和 SUGT06a13 的 面向对象 进行了整合
            
##### 09/20/2021 更新日志
            SUGT06a15 底层架构搭建

##### 09/16/2021 更新日志
            building 模块 移植
            
##### 09/15/2021 更新日志
            main menu 移植

##### 09/13/2021 更新日志
            SUGT06a13 底层架构搭建

##### 09/14/2021 更新日志
            SUGT06 企划书 发布
            
##### 09/13/2021 更新日志
            SUGT06a13 开始开发

##### 09/10/2021 更新日志
            开始使用 MoYu命名法 替代 老变量
            优化 MoYu自研引擎 底层架构

##### 09/09/2021 更新日志
            MoYu命名法 上线
            新增 black_field 模块
            优化 MoYu自研引擎 架构

##### 09/07/2021 更新日志
            柏林噪声 随机地图生成 上线
            引入 pickle 生成 二进制 游戏存档
            新增 save_data 模块
            新增 read_data 模块
            新增 menu_createmap_surface 模块
            新增 menu_createmap_event 模块

##### 09/06/2021 更新日志
            新增 perlin_noise 模块

##### 09/04/2021 更新日志
            新增 menu_about surface 模块
            新增 menu_about event 模块
            优化 menu_main 启动界面
            优化 MoYu自研引擎 架构

##### 09/03/2021 更新日志
            Tinyland Preview20210903 MacOS 发布
            Tinyland Preview20210903 WinOS 发布

##### 09/02/2021 更新日志
            WindowsOS 打包测试
            引入 perlin noise 柏林噪声 算法
            测试 柏林噪声 随机地图生成 模块
            新增 menu_main 启动界面
            新增 menu_stop surface 模块
            新增 menu_stop event 模块
            新增 menu_setting surface 模块
            新增 menu_setting event 模块
            优化 MoYu自研引擎 架构

##### 09/01/2021 更新日志
            MacOS 打包测试
            新增 init 牵引文件 模块
            新增 menu_main surface 模块
            新增 menu_main event 模块
            优化 MoYu自研引擎 架构

##### 08/31/2021 更新日志
            SUGT06a12 Dv20210831 发布
            新增 部分GUI组件
            新增 部分GUI音效
            新增 BGM背景音乐
            新增 金融系统
            新增 建造系统
            新增 土地种植系统
            新增 土地收获系统
            新增 时间维度
            新增 预选层判断
            新增 游戏文档
            优化 MoYu自研引擎 架构

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

![](https://github.com/MoYuStudio/SUGT06/raw/main/moyu_engine/assets/graphics/tileland/tl21.png)<br/><br/><br/>
