# learning-notes

张雨婷 的编程 / 数据学习仓库（南京农业大学 · 统计学 · 大一起点）。

按 `大一上学期每周待办.md` 推进，每两周至少提交一次，毕业时这里就是简历上的作品集。

## 仓库结构
- `demo.py` — 环境验证脚本（标准库计算描述统计）
- `week-log/` — 每周学习记录（W1.md、W2.md ……）
- `exercises/` — Excel / SQL / Python 练习文件
- `projects/` — 迷你项目 / 正式项目（大二起填充）

## 本地环境
- **Python**：WorkBuddy 托管运行时 3.13.12
  - 路径：`C:\Users\x\.workbuddy\binaries\python\versions\3.13.12\python.exe`
- **编辑器**：VS Code（把上面的 python.exe 设为 Python 解释器即可）
- **包管理**：需要 pandas / numpy 时再装，前期用标准库够用
- `demo.py` 已验证可运行，输出 `均值 86.8 / 中位数 88.5 / 标准差 5.78`

## 推送到 GitHub（本地已就绪，只差 3 步）

本地已 `git init` + `commit` + 设好 remote：`origin = https://github.com/xx895/learning-notes.git`

1. https://github.com/new 建空仓库 `learning-notes`（Public，**不勾** README / .gitignore / license）
2. 首次认证：`gh auth login`（或 PAT，详见 `个人主页/README.md`）
3. 推送：`git push -u origin main`

之后每周：
```bash
git add . && git commit -m "W1 周记" && git push
```
