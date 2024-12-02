![alt text](image.png)
# Discord Bot for Collecting Messages

Este projeto é um bot para Discord que coleta mensagens de canais de texto, threads e fóruns de um servidor e armazena essas informações em um banco de dados MongoDB.

## Funcionalidades

- Coleta de mensagens de canais de texto, threads e fóruns.
- Armazenamento das mensagens coletadas em um banco de dados MongoDB.
- Suporte para fusos horários (com `pytz`).
- Registro de informações detalhadas sobre as mensagens, como autor, data e canal.

## Requisitos

- Python 3.9+
- Discord.py (`discord.py`)
- Pandas (`pandas`)
- Pytz (`pytz`)
- PyMongo (`pymongo`)
- Python-dotenv (`python-dotenv`)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt

3. Defina o token do bot do Discord e a URI do MongoDB no arquivo .env:

   ```bash
   DISCORD_TOKEN=seu_token_aqui
   MONGODB_URI=sua_uri_aqui

4. Execute o bot:

   ```bash
   python main.py

## Como usar

1. O bot será iniciado e ficará pronto para coletar mensagens.
2. O bot irá percorrer todos os canais e threads do servidor especificado, coletando mensagens a partir de uma data específica (yyyy-MM-dd).
3. As mensagens coletadas serão armazenadas em sua colletions no database MongoDB.

<h2 id="colab">🤝 Colaboradores</h2>

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://media.licdn.com/dms/image/v2/D4D03AQGBx3C-ojHIHA/profile-displayphoto-shrink_200_200/B4DZODqTlhHcAc-/0/1733080726338?e=1738800000&v=beta&t=WrvetVRh35RfwSTe3LGSh7RQoPzLbxr3TE6p2dllYU4" width="100px;" alt="Fabricio Rosa"/><br>
        <sub>
          <b>Fabrício Rosa</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://media.licdn.com/dms/image/v2/D4D03AQE-5o3qpWIN9g/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1710954940792?e=1735171200&v=beta&t=7vLCKrr7DJio8MREsd9pBijdp8TjUFA5RdkCJpetsS0" width="100px;" alt="Eduardo Bortoli"/><br>
        <sub>
          <b>Eduardo Bortoli</b>
        </sub>
      </a>
    </td>
 
