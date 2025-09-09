<h1 align="center">MAICA Illuminator compact</h1>
<div align="center">
<img src="https://maica.monika.love/assets/maica-text-finish-p.png" width=150>
</div>

***

<p align="center"><a href="/README.md">中文</a> | English</p>

This is the introduction page of MAICA Submod backend.

MAICA contains multiple subprojects, find menu at https://github.com/Mon1-innovation/MAICA.

Please pardon for not putting an full instruction here, since it's too complicated. To know more about MAICA, navigate to instruction pages mentioned above.

-------------------------

# MAICA Illuminator compact

Illuminator compact is the compact version of MAICA backend(Illuminator), for convenience of using MAICA with various LLMs.

This repository introduction is very brief. If this is your first contact with MAICA, consider navigating to the introduction page at https://maica.monika.love/.

## Notice

* You don't have to install this if you're using MAICA official service. Just install [frontend](https://github.com/Mon1-innovation/MAICA_ChatSubmod).
* This submod functions as backend middleware, which does not come with models. You have to provide external model APIs.
* For developing or packing yourself with compact branch, refer to [Illuminator compact core repository](https://github.com/PencilMario/MAICA).
  > For developing or production deploying MAICA, use the [full version](https://github.com/Mon1-innovation/MAICA).

## Installation

> This submod supports only MAS Windows natively.

1. Use the latest version of MAS.  
2. Install latest verion of Blessland from [frontend Release](https://github.com/Mon1-innovation/MAICA_ChatSubmod/releases).
3. Download latest version of Illuminator compact at [Release](https://github.com/Mon1-innovation/MAICA_Server_Submod/releases).
4. Quit the game, unzip and copy-paste the folders into `DDLC`/`MAS_CN001***/Monika After Story` folder, which is where `DDLC.exe`/`MAS.exe` lies in.
  > Do not unzip directly into Submods! You must merge it into the game's base path.

## Usage

> Configurations required! Set up through in-game API keys section after installation.

> Make sure you've installed [MAICA Blessland](https://github.com/Mon1-innovation/MAICA_ChatSubmod/releases) in advance.

* Provide self hosted or third party LLM APIs, which should be compatible with OpenAI >= 1.0.
* Configure other variables of `MAICA Server` through API keys section.
  > Example and explainations [here](https://github.com/Mon1-innovation/MAICA/blob/main/maica/env_example).
  > For explaination of concepts of MAICA, refer to [documents](https://github.com/Mon1-innovation/MAICA/tree/main/document).
* Start server in Submods section, and request Blessland to reinitialize.
* Switch Blessland's provider to local.
* System prompt of core model is at `system_prompt.rpy`. Consider tweakering if your model wasn't trained according to MAICA standard.
