
![image](https://github.com/user-attachments/assets/9a5e47e3-8a2f-4e11-bd09-073d59ff8c08)


# Discord Bot for Collecting Messages

Este projeto é um bot para Discord que coleta mensagens de canais de texto, threads e fóruns de um servidor e armazena essas informações em um banco de dados MongoDB.

## Nova funcionalidade adicionada

✨Agora o bot pode extrair mensagens de um único canal de texto e armazenar essas mensagens em uma collection no banco de dados MongoDB, facilitando a análise de dados e o monitoramento das conversas.

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
        <img src="https://media.licdn.com/dms/image/v2/D4D03AQFhg6aT98EYyQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1697061290400?e=1735171200&v=beta&t=I7QymWDGwsoAsobMDPcCba6KiP3cvSA8LnWUF2G9nzU" width="100px;" alt="Fabricio Rosa"/><br>
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
    <td align="center">
      <a href="#">
        <img src="https://media.licdn.com/dms/image/v2/D4E03AQGi_MKVj3IA5Q/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1718247588625?e=1735171200&v=beta&t=lrjO5njNVwsJQfyTMU_hkemv59cTfZxhGE6rNgCstxI" width="100px;" alt="Eduardo Bortoli"/><br>
        <sub>
          <b>Gabrielle Rosa</b>
        </sub>
      </a>
    </td>
</table>
