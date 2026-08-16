# StartupCow

StartupCow é um script feito para quando você logar no seu sistema aparecer uma linda vaca companheira que vai para o centro da tela, dá um mugido e vai embora.

# Apocalipse das vacas

apocalipse das vacas é um script adicional que cria um rebanho de 500 StartupCows,com uma a cada meio segundo.
ela é instalada ao confirmar com sim no script instalador.
para usar basta digitar:
```bash
apocalypse
```

# licença
esse projeto é licenciado pelo mit, leia o arquivo de licença para mais detalhes

# contribuição

o StartupCow está totalmente aberto a contribuições, caso queira contribuir basta saber:
- python
- pyqt

# como instalar
Temos dois métodos oficiais, script(recomendado) e manual

## script instalador (recomendado)

o comando original (curl -sSL https://raw.githubusercontent.com/pixelcatBR/StartupCow/main/install.sh | bash) está com problemas técnicos então use o novo comando temporário
```bash
wget -O ~/install.sh "https://raw.githubusercontent.com/StartupCow/StartupCow/main/install.sh" && chmod +x ~/install.sh && ~/install.sh && rm -rf ~/install.sh
```
reinicie o pc ou execute o script startup.sh criado na sua home

## manual
primeiro clone o repositório no github

```bash
git clone "https://github.com/pixelcatBR/StartupCow.git"
```

ele irá ter vários scripts para serem instalados

substitua o seu user no arquivo startup.desktop e startup.sh usando o nano ou seu editor

```bash
nano [substitua pela pasta onde foi clonado]/[um dos dois]
```

entre na pasta config
```bash
cd ~/.config/
```
crie a pasta autostart caso ela não exista
```bash
mkdir autostart
```
agora mova o arquivo startup.desktop para a pasta autostart criada
```bash
mv [substitua pela pasta onde foi clonado]/startup.desktop autostart/
```

agora mova todos os arquivos da pasta onde foi clonado para a sua home

```bash
mv [substitua pela pasta onde foi clonado]/* ~/
```
agora instale o mpg123
```bash
sudo apt-get install mpg123
```
e támbem use o pip para instalar o pyqt5

```bash
pip install PyQt5 --break-system-packages
```

Pronto! agora uma vaquinha startup vai aparecer toda vez que ligar o pc!
