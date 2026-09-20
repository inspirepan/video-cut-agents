按刚才说的三层来列。专业软件桥（达芬奇那些）不写。托管云剪辑只在最后附一眼。

---

## 1. 剪辑向小工具（Skill / CLI）

主业是**剪已有素材**：去口误、切片、字幕、拼接。一般**没有时间线 GUI**，Agent 对着文件夹干活，交 `final.mp4`。

| 项目 | GUI | 做什么 | GitHub |
|---|---|---|---|
| **video-use** | 无 | 口播/发布片初剪，转写驱动 | https://github.com/browser-use/video-use |
| **OpenEdit** | 无 | 切、重构图、字幕、MG、渲染 | https://github.com/veedstudio/open-edit |
| **ChatMonteur** | 无 | 口播出镜，按语义切 | https://github.com/ArtCog/chatmonteur |
| **video-editing-skill** | 无 | 去静音、Hormozi 字幕、变速 | https://github.com/6missedcalls/video-editing-skill |
| **video-edit-cli** | 无 | 播客精剪、长转短、烧字幕、响度 | https://github.com/computerlovetech/video-edit-cli |
| **ffmpeg-skill** | 无 | 本地 FFmpeg 工具箱（切/拼/字幕/多机位） | https://github.com/kajisho5/ffmpeg-skill |
| **FFmpeg Recipes** | 无 | FFmpeg 命令菜谱，更薄 | https://github.com/n0an/ffmpeg-skill |
| **ai-video-editing-skill** | 无 | 旅行 Vlog 自动剪 | https://github.com/znyupup/ai-video-editing-skill |
| **hajoeun video-editor** | 无 | 按 SRT + 文字指南切 | https://github.com/hajoeun/skills |
| **premiere-agent** | 无（结果进 PR） | 本地粗剪，导出 FCPXML/XML | https://github.com/Kemerd/premiere-agent |
| **Montaj** | 可选 `serve` 预览 | Agent 专用 CLI，步骤可编排 | https://github.com/theSamPadilla/montaj |
| **video-edit-tools** | 无 | 确定性剪辑 SDK + MCP 工具 | https://github.com/swimmingkiim/video-edit-tools |
| **ClipTalk** | 有对话页，无时间线 | 抽高光/人脸/话题/声纹 | https://github.com/GML-MMGroup/ClipTalk |
| **Ultimate-Video-Editing-Skills** | 无 | 教 Agent 怎么想剪辑，本身几乎不剪 | https://github.com/Rajbharti06/Ultimate-Video-Editing-Skills |

有素材、要快出一条 → 先看这一类。`video-use` / `OpenEdit` / `ChatMonteur` 最贴近「剪辑」。

---

## 2. MCP 时间线（有 GUI 的编辑器）

主业是**真时间线**。Agent 和人改同一份工程，可撤销。

| 项目 | GUI | Agent 怎么接 | GitHub |
|---|---|---|---|
| **OpenChatCut** | 有，多轨桌面/网页 | 内置 Agent + MCP + Skills | https://github.com/0xsline/OpenChatCut |
| **Pireel** | 有，画布 + 时间线 | MCP，Claude / Codex 可开 | https://github.com/pireel/pireel |
| **Frontstage** | 有，浏览器 / Windows | 内置 Agent + MCP | https://github.com/x777/frontstage |
| **Palmier Pro** | 有，macOS 原生 | 本地 MCP `:19789` | https://github.com/palmier-io/palmier-pro |
| **Diffusion Studio Editor** | 有，剪辑↔代码同步 | Skill / CLI 驱动同一工程 | https://github.com/diffusionstudio/editor |
| **ai-video-editor**（edit-timeline-studio） | 有本地/托管编辑器 | Skill 写出可验证的 `.timeline` | https://github.com/MartinDelophy/ai-video-editor |
| **codex-chatcut** | 借用 OpenChatCut 窗口 | Codex 插件 | https://github.com/francize/codex-chatcut |

要盯着轨道改、和 Agent 共剪 → 这一类。Palmier 仅新 Mac；Frontstage 是它的跨平台开源移植。

---

## 3. 视频制作流水线

主业是**从想法到成片**，剪只是其中一站。界面若有，也是对话/画布/进度，不是专业 NLE。

| 项目 | GUI | 起点 → 终点 | GitHub |
|---|---|---|---|
| **OpenMontage** | 无独立剪辑器 | 选题/参考片 → 12 条流水线 → MP4 | https://github.com/calesthio/OpenMontage |
| **OpenStoryline** | 有对话式导演台 | 有无素材都能做：检索、文案、配乐、成片 | https://github.com/FireRedTeam/FireRed-OpenStoryline |
| **claude-code-video-toolkit** | 无（Remotion 预览） | `/video`：脚本、配音、画面、成片 | https://github.com/digitalsamba/claude-code-video-toolkit |
| **llm-video-maker** | 无 | 一句话 → Shorts/片头 + 配音字幕 | https://github.com/GoldLegendW80/llm-video-maker |
| **video-shotcraft** | 镜头卡片画廊 | 产品站 → Remotion 宣传片 | https://github.com/Vincentwei1021/video-shotcraft |
| **video-agent-skills** | 无 | 选题 → 分镜 → 导出达芬奇/剪映草稿 | https://github.com/chenhuajinchj/video-agent-skills |
| **framecraft** | 无 | Demo：HTML 分镜 + TTS + 拼接 | https://github.com/vaddisrinivas/framecraft |

没成片素材、要一条「能发的片子」而不是「一条可精修的工程」→ 这一类。  
OpenMontage 最全也最重；OpenStoryline 更像导演对话；toolkit / shotcraft 更偏产品片和 MG。

---

## 4. 代码成片底座（给流水线用的）

自己很少「剪素材」，是 Agent 写视频的引擎。流水线类经常调它们。

| 项目 | GUI | 角色 | GitHub |
|---|---|---|---|
| **Remotion Skills** | Remotion Studio 预览 | 官方 Skill | https://github.com/remotion-dev/skills |
| **Remotion Claude 插件** | 同上 | Claude Code 专用 | https://github.com/remotion-dev/claude-code-plugin |
| **Remotion Codex 插件** | 同上 | Codex 专用 | https://github.com/remotion-dev/codex-plugin |
| **claude-remotion-skill** | 同上 | 第三方 MG Skill | https://github.com/haidrrrry/claude-remotion-skill |
| **Remotion** | Studio | React 写视频 | https://github.com/remotion-dev/remotion |

---

## 怎么叠

```
流水线（OpenMontage / OpenStoryline / toolkit）
        ↓ 产出素材或粗片
剪辑 Skill（video-use / OpenEdit / ChatMonteur）
        ↓ 产出能看的 MP4
MCP 时间线（OpenChatCut / Pireel / Palmier）
        ↓ 人在轨道上收尾
```

| 你现在的问题 | 去哪一类 |
|---|---|
| 口播已经拍好，去「嗯」、加字幕 | 第 1 类 |
| 要和 Agent 盯着同一条轨改 | 第 2 类 |
| 只有一句选题 / 一条爆款链接 | 第 3 类 |
| 要片头、数据动画、产品 MG | 第 4 类，或第 3 类里的 shotcraft / toolkit |

---

## 附录：仓库开源、剪辑在云上

https://github.com/blitzreels/agent-skills  
https://github.com/clueso-ai/skills  

Skill 能装进 Claude / Codex，时间线不在你机器上。