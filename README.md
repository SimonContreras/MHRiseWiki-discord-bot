<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** SimonContreras, MHRiseWiki-discord-bot, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<p align="center">
  <a href="https://github.com/SimonContreras/MHRiseWiki-discord-bot/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/Build-passing-success" alt="Build">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/Coverage-30%25-critical" alt="Coverage">
  </a>
   <a href="">
    <img src="https://img.shields.io/badge/Tests-passing-success" alt="Tests">
  </a>
</p>
<p align="center">
  <a href="https://www.python.org/downloads/">
    <img alt="PyPI - Python Version" 
        src="https://img.shields.io/badge/Python-3.8.3-blue">
  </a>
  <a href="https://discordpy.readthedocs.io">
    <img alt="Discordpy" 
        src="https://img.shields.io/badge/Discord-py-blue">
  </a>
  <a href="https://docs.docker.com/">
    <img src="https://img.shields.io/badge/Docker-10.10.5-blue" alt="Docker">
  </a>
   <a href="https://docs.docker.com/compose/">
    <img src="https://img.shields.io/badge/DockerCompose-1.28.5-blue" alt="Docker Compose">
  </a>
</p>



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/SimonContreras/MHRiseWiki-discord-bot">
    <img src="assets/bot-icon/hinoa_circle.png" alt="Logo" width="150" height="150">
  </a>

  <h2 align="center">Hinoa</h2>

  <p align="center">
    Monster Hunter Rise Wiki Discord bot
    <br/>
    <a href="https://github.com/SimonContreras/MHRiseWiki-discord-bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!--<a href="https://github.com/SimonContreras/MHRiseWiki-discord-bot">View Demo</a>-->
    ·
    <a href="https://github.com/SimonContreras/MHRiseWiki-discord-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/SimonContreras/MHRiseWiki-discord-bot/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
Hinoa is a built-in wiki integrated in a Discord bot, for the game Monster Hunter Rise, that will be release on March 26, 2021. The main objective of this project is bring a simple interface via discord commands to search information about the game. Hinoa' ll be multilanguage, with **spanish** as his main/default language.

### Built With

* [Python 3.8.3](https://www.python.org/downloads/)
* [Discordpy](https://discordpy.readthedocs.io)
* [Pony ORM](https://docs.ponyorm.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://docs.docker.com/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Docker
  - For information about **docker** installation go to: [Docker Docs](https://docs.docker.com/engine/install/) 
* Docker Compose
  - For information about **docker compose** installation go to: [Docker Compose Docs](https://docs.docker.com/compose/install/)
    

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/SimonContreras/MHRiseWiki-discord-bot.git
   ```
2. Set environment variables in Dockerfile. You can use the default environment variables on Dockerfile, but you **MUST** put your own discord token. For more info about this visit: [Discord Dev.](https://discord.com/developers/docs/intro)
  
   ```Dockerfile
    ENV DISCORD_TOKEN={PUT YOUR DISCORD TOKEN HERE}
    ENV PROVIDER_DB=postgres
    ENV USER_DB=bot_mhrise
    ENV PASSWORD_DB=Wvwd3Vu3YrxKPWsvd7EK
    ENV HOST_DB=bot_db
    ENV PORT_DB=5432
    ENV DATABASE_NAME=mh_rise_wiki
    ENV THUMBNAIL_ROUTE=./assets/thumbnail/
   ```
3. Build
    ```bash
    > docker-compose build
    ```
4. Run
    ```bash
    > docker-compose up
    ```
    2.1 **ONLY** First time to populate database, with supported languages and wiki info. Open another console and type:
    ```bash
    > docker exec -d [id or container name of the bot] python fixture/populate_db.py
    ```

<!-- USAGE EXAMPLES -->
## Usage

**Invite Link**: [Discord Bot Invite](https://discord.com/api/oauth2/authorize?client_id=807761086677385266&permissions=1074192448&scope=bot)

There are two types of scopes for commands, ***anyone*** and ***admin***. ***Anyone*** commands are related directly to the wiki itself, meanwhile ***admin*** commands are related to prefix and language management.
### Commands available to anyone:
* **?ayuda**
  * Lista comandos disponibles en la wiki
* **?monstruo [nombre-monstruo]**
  * Lista información básica del monstruo.
* **?item [nombre-item]**
  * Lista información del item.
* **?armadura [nombre-armadura]**
  * Muestra información en detalle de la parte/set de armadura.
* **?hab [nombre-skill]**
  * Muestra información de la habilidad.
* **?arma [nombre-arma]**
  * Muestra información detallada del arma.
* **?hitzones [nombre-monstruo]**
  * Lista información numérica detallada del monstruo.
* **?mats [nombre-monstruo] [rango]**
  * Muestra materiales que da como recompensa un monstruo en un rango específico (alto/bajo).

### Commands available to admins:

* **?ayudaAdmin**
  * Lista commandos de administración disponibles
* **?cambiarIdioma [sigla-idioma]**
  * Cambiar Idioma del bot.
* **?cambiarPrefijo [nuevo-prefijo]**
  * Cambia prefijo para el bot.

_For commands in **another language** and more info, please refer to the [Wiki](https://github.com/SimonContreras/MHRiseWiki-discord-bot/wiki)_

<!-- ROADMAP -->
## Roadmap
- Working on the following commands:
  -  location 
  -  hitzones
  -  talisman
- Waiting for datamined data to populate database.
- New commands will be implemented based on new mechanics added to the game.
- See the [open issues](https://github.com/SimonContreras/MHRiseWiki-discord-bot/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Licensed under the [MIT License](https://github.com/SimonContreras/MHRiseWiki-discord-bot/blob/main/LICENSE),
you may not use this repo except in compliance with the License. See `LICENSE` for details.

<!-- CONTACT -->
## Contact

Via Discord -> [Boomerang_CL#3556](https://discord.com/) on Discord

Project Link: [https://github.com/SimonContreras/MHRiseWiki-discord-bot](https://github.com/SimonContreras/MHRiseWiki-discord-bot)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
Thanks to:
* [Gatheringhallstudios](https://github.com/gatheringhallstudios) , Relational model based in [MHWorldData](https://github.com/gatheringhallstudios/MHWorldData) and ported to Pony ORM
