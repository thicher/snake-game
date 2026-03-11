# Snake Game

一个用 Python 编写的经典贪吃蛇游戏，适合学习编程和游戏开发基础。

## 游戏预览

```
┌─────────────────────────────┐
│ 得分: 0 │
│                     ┌─────────────────────────┐ │
│ │                         │ │
│ │     🐍 →               │ │
│ │                         │ │
│ │              🍎         │ │
│ │                         │ │
│ └─────────────────────────┘ │
└─────────────────────────────┘
```

## 运行游戏

```bash
# 安装依赖
pip install -r requirements.txt

# 运行游戏
python main.py
```

## 控制方式

- **方向键 (↑↓←→)**: 控制蛇的移动方向
- **空格键**: 暂停/继续游戏
- **Q**: 退出游戏

## 项目结构

```
snake-game/
├── main.py          # 游戏主程序
├── snake.py         # 蛇的类定义
├── food.py          # 食物类定义
├── score.py         # 计分板
├── constants.py     # 游戏常量配置
├── requirements.txt # Python 依赖
└── README.md        # 项目说明
```

## 学习路线

想通过这个项目学习编程和 Git 版本控制？可以按以下顺序探索：

### 第一阶段：运行和理解代码

1. **先运行游戏** - 了解游戏基本玩法
2. **阅读 `main.py`** - 理解游戏主循环
3. **阅读 `snake.py`** - 了解蛇是如何移动的
4. **阅读 `food.py`** - 了解食物是如何生成和碰撞检测的

### 第二阶段：修改和实验

尝试以下练习：
- [ ] 修改蛇的移动速度（修改 `SPEED` 常量）
- [ ] 修改游戏窗口大小
- [ ] 添加新的食物类型
- [ ] 修改蛇的颜色

### 第三阶段：Git 版本控制学习

查看 Git 历史，了解每次提交做了什么修改：

```bash
# 查看提交历史
git log

# 查看某个文件的历史
git log --follow main.py

# 比较不同版本
git diff HEAD~1 main.py
```

### 第四阶段：参与贡献

1. Fork 这个仓库
2. 创建新分支: `git checkout -b feature/your-idea`
3. 提交修改: `git commit -m "Add your feature"`
4. 推送到分支: `git push origin feature/your-idea`
5. 创建 Pull Request

## 技术栈

- **Python 3.x**: 编程语言
- **pygame**: 游戏开发库

## 许可证

MIT License
