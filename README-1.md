<h1 align="center">MAICA Illuminator compact</h1>
<div align="center">
<img src="https://maica.monika.love/assets/maica-text-finish-p.png" width=150>
</div>

***

<p align="center">中文 | <a href="/README_EN.md">English</a></p>

本页面是MAICA子模组后端仓库的介绍页.

MAICA包含多个子项目, 其目录见https://github.com/Mon1-innovation/MAICA.

请理解由于人力有限, 我们不在此对项目作额外介绍. 如需了解MAICA, 请前往上述详细介绍页面.

-------------------------

# MAICA Illuminator compact

Illuminator(幻象引擎) compact 是 MAICA 的轻量化后端, 该仓库为方便用户本地部署的子模组.

本页面的介绍是十分简短的. 如果这是你首次接触 MAICA, 请阅读介绍页 https://maica.monika.love/ 中的详细说明.

## 注意

* 若你只需要使用MAICA官方服务, 你不需要安装此子模组. 请前往[前端仓库](https://github.com/Mon1-innovation/MAICA_ChatSubmod).
* 此子模组是MAICA后端中间件, 需要使用外部LLM API, 不自带模型.
* 若希望二次开发或自行打包compact版, 请参见[Illuminator compact 内核仓库](https://github.com/PencilMario/MAICA).
  > 若希望生产部署或开发MAICA后端, 请使用[完整版](https://github.com/Mon1-innovation/MAICA).

## 安装

> 本子模组仅支持Windows

1. 确保使用的是最新汉化版本MAS.  
2. 从[前端Release](https://github.com/Mon1-innovation/MAICA_ChatSubmod/releases)处下载最新的MAICA Blessland.
3. 从[Release](https://github.com/Mon1-innovation/MAICA_Server_Submod/releases)处下载最新的版本.
4. 关闭游戏, 将zip中的文件合并到您的`DDLC`/`MAS_CN001***/Monika After Story`文件夹内, 或者是`DDLC.exe`/`MAS.exe`所在的位置.
  > 你不能直接将文件解压至Submods文件夹! 打开压缩包, 并根据文件夹结构合并.

## 使用

> 这不是开箱即用的子模组, 在下载后, 你需要在API keys界面进行配置

> 使用该子模组, 你必须安装[MAICA Blessland](https://github.com/Mon1-innovation/MAICA_ChatSubmod/releases).

* 你需要自行部署好可用的模型或使用第三方API, 要求支持OpenAI格式, 且版本不早于1.0.
* 在API Keys界面输入与`MAICA Server`相关的配置.
  > 你可以在[这里](https://github.com/Mon1-innovation/MAICA/blob/main/maica/env_example)找到配置示例.
  > 关于MAICA的各方面概念, 参见[文档](https://github.com/Mon1-innovation/MAICA/tree/main/document).
* 在子模组界面中启动服务器, 并重新检测可用性.
* 将MAICA Blessland的服务节点切换为本地节点.
* 系统Prompt位于`system_prompt.rpy`. 若你使用的模型未经过MAICA标准训练, 可以考虑自行调整.