# Mindmap 节点数据契约（所有 subagent 必须遵守）

输出文件：一个 JSON 文件，顶层为 `{"branches": [Node, ...]}`。必须能被 `python3 -c "import json;json.load(open(p))"` 解析。

## Node 结构（所有字段除 id/title/summary 外可省略；省略即不显示）

```json
{
  "id": "understand",                       // kebab-case，全局唯一，只含 a-z0-9-
  "title": "原视频理解",                     // ≤ 14 个汉字，节点上直接显示
  "tag": "shared",                          // shared | interview | sports | mg | gap | atomic | pitfall | decision
  "summary": "≤ 40 字，一句话说这个节点做什么",
  "goal": "≤ 100 字：这一步要解决的问题、为什么必须有",
  "inputs": ["上游 artifact，如 ingest manifest"],
  "outputs": ["下游 artifact，如 word-level transcript JSON"],
  "interview": "≤ 80 字：长访谈侧的差异/特殊要求（不适用则省略）",
  "sports": "≤ 80 字：体育赛事侧的差异/特殊要求（不适用则省略）",
  "mg": "≤ 80 字：MG 动效制作方向（从脚本/数据/品牌生成画面，而非从素材选片）的差异/特殊要求（不适用则省略）",
  "atomic": [                               // 原子能力：这一步需要哪些可独立实现/替换的能力
    {"name": "词级 ASR", "impl": "WhisperX / Parakeet / SenseVoice", "note": "≤ 60 字：输入输出、关键参数或选择理由"}
  ],
  "pitfalls": [                             // 踩坑经验：必须有具体来源
    {"title": "≤ 20 字", "detail": "≤ 120 字：现象 → 原因 → 对策", "source": "repo-dir/path/to/file.md:LINE 或 仓库名"}
  ],
  "urls": ["https://github.com/org/repo"],  // 可选：仓库地图节点的 GitHub 地址，可多个
  "refs": [                                 // 参考实现，2–5 条
    {"repo": "video-use", "path": "video-use/SKILL.md", "line": 18, "why": "≤ 40 字：这个文件证明/实现了什么"}
  ],
  "children": [ /* 同结构 Node */ ]
}
```

## 硬性规则

1. 语言：中文正文，代码标识符/模型名/字段名保留英文。短句，主动语态，一句一个意思。
2. `refs[].path` 必须是 `/Users/panjx/code/video-agent/` 下真实存在的相对路径。写之前用 `ls` 或 `test -f` 核对。`line` 用 grep 找到的真实行号；找不到就写 null。
3. 不允许编造仓库没有的能力。所有仓库都没有的能力：`tag` 写 `gap`，并在 goal 里写“现有仓库无完整实现，需自研”。
4. 内容要比 `research/video-editing-agent-deep-dive-v2.md` 更具体：给出真实参数（抽帧率、阈值、fade 毫秒、BPM 范围）、schema 字段名、命令名、模型名、prompt 中的硬规则。deep-dive 只是框架，不要复述它。
5. 层级：你负责的每个 L1 branch 下放 3–7 个 L2 children；L2 下最多 4 个 L3 children，L3 只在确有必要时加。深度不超过 L3。细节放字段里，不要靠加层级。
6. 每个 L1/L2 节点尽量都有 `atomic` 和 `pitfalls`；L1 至少 3 条 pitfalls，L2 至少 1 条。
7. 访谈与赛事：凡是两个方向要求不同的节点，都写 `interview` 和 `sports` 两个字段。第三方向 MG 动效制作用 `mg` 字段，只在 MG 确实与集锦不同时写。
8. 输出只写 JSON 文件；最终回复只需 200 字以内的摘要（写了哪些 branch、几个节点、有无无法核实的点）。
