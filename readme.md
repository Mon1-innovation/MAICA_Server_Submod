<h1 align="center">MAICA Illuminator compact</h1>
<div align="center">
<img src="https://maica.monika.love/assets/maica-text-finish-p.png" width=150>
</div>

***

<p align="center">中文 | <a href="/README_EN.md">English</a></p>

本页面是MAICA的指引页面, 当前位置是MAICA子模组前端仓库.

MAICA项目的详细介绍页是https://maica.monika.love/.

要快速开始或了解授权, 请参阅https://maica.monika.love/tos.

MAICA的后端仓库地址是https://github.com/Mon1-innovation/MAICA.

MAICA的子模组前端仓库地址是https://github.com/Mon1-innovation/MAICA_ChatSubmod.

MAICA LIA分支的模型地址是https://huggingface.co/edgeinfinity/MAICAv0-LIA-72B.

MAICA LOA分支的模型地址是https://huggingface.co/edgeinfinity/MAICAv0-LOA-7B.

MAICA的基本数据集仓库位于https://huggingface.co/datasets/edgeinfinity/MAICA_ds_basis.

MAICA的相关文档存储于https://github.com/Mon1-innovation/MAICA/tree/main/document.

请理解由于人力有限, 我们不在此对项目作额外介绍. 如需了解MAICA, 请前往上述详细介绍页面.

-------------------------

# MAICA Illuminator compact

Illuminator compact 是 MAICA 的轻量化后端, 为方便用户本地部署的子模组.

本页面的介绍是十分简短的. 如果这是你首次接触 MAICA, 请阅读介绍页 https://maica.monika.love/ 中的详细说明.



## 安装

1. 确保使用的是最新汉化版本MAS.  
2. 从[Release](https://github.com/Mon1-innovation/MAICA_ChatSubmod/releases)处下载最新的MAICA Blessland.    
3. 从[Release](https://github.com/Mon1-innovation/MAICA_Server_Submod/releases)处下载最新的版本.  
4. 关闭游戏, 将zip中的文件合并到您的`DDLC`/`MAS_CN001***/Monika After Story`文件夹内, 或者是`DDLC.exe`/`MAS.exe`所在的位置
  > 你不能直接将文件解压至Submods文件夹! 打开压缩包, 并根据文件夹结构合并.

## 使用

> 这不是开箱即用的子模组, 在下载后, 你需要在API keys界面进行配置

> 使用该子模组, 你必须安装[MAICA Blessland](https://github.com/Mon1-innovation/MAICA_ChatSubmod/releases)

* 你需要自行部署好可用的模型后端, 并且支持openai api格式
* 在API Keys界面输入与`MAICA Server`相关的配置
  > 你可以在[这里](https://github.com/Mon1-innovation/MAICA/blob/main/maica/env_example)找到配置示例.
* 在子模组界面中启动服务器, 并重新检测可用性
* 系统Prompt位于`system_prompt.rpy`, 你可以优化prompt来提高模型的表现.

