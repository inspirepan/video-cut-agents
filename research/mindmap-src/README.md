# mindmap 数据源

`../video-editing-agent-mindmap.html` 由这里的数据生成。

- `branches/*.json`：按 `CONTRACT.md` 契约写的节点数据（A 接入与理解、B 脚本与选片、C BGM 与包装、D 工程/渲染/QA/GUI、E 原子能力/踩坑/仓库地图、F 产品定位、G MG 动效制作方向）。仓库地图节点带 `urls`（GitHub 地址，来自各仓库 git remote）；`interview` / `sports` / `mg` 三个字段驱动三种视角切换。
- `template.html`：渲染引擎（纯 HTML/CSS/JS，无外部依赖）。
- `build.py`：合并、校验引用路径、注入模板。

重建：

```bash
uv run research/mindmap-src/build.py research/video-editing-agent-mindmap.html
```
