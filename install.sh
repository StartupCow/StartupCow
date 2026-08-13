echo "Iniciando o Script instalador"
cd ~/
echo "[ OK ] Iniciado"
echo "Instalando dependências..."
sudo apt install -y mpg123 python3 python3-pip
pip install PyQt5 --break-system-packages
echo "[ OK ] dependências instaladas"
echo "clonando repositório oficial..."
git clone "https://github.com/pixelcatBR/StartupCow.git"
echo "[ OK ] clonado"
echo "Editando arquivo startup.desktop..."
sed -i "s|^Exec=.*|Exec=$HOME/startup.sh|" StartupCow/startup.desktop
echo "[ OK ] editado"
echo "Movendo Arquivo startup.desktop..."
cd ~/.config/
mkdir autostart
mv ~/StartupCow/startup.desktop autostart/
echo "[ OK ] arquivo .desktop movido"
echo "Movendo os Arquivos nescessários..."
mv ~/StartupCow/* ~/
echo "[ OK ] Movido"
echo "Dando permissão de execução pro script..."
chmod +x ~/startup.sh
echo "[ OK ] Arquivo com permissão"
echo "removendo a pasta antiga..."
rm -rf ~/StartupCow
echo "[ OK ] Removido"

echo "Deseja instalar o apocalipse das vacas? (s/n)"
read resposta
if [ "$resposta" = "s" ] || [ "$resposta" = "S" ] || [ "$resposta" = "sim" ] || [ "$resposta" = "SIM" ]; then
  echo "Legal! vamos preparar o rebanho..."
  sudo cp ~/cowapocalypse.py /usr/local/bin/apocalypse
  echo "- use com o comando: apocalypse."
elif [ "$resposta" = "n" ] || [ "$resposta" = "N" ] || [ "$resposta" = "nao" ] || [ "$resposta" = "NÃO" ]; then
  echo "Que pena! fique com a vaquinha normal então que por si só já é legal."
else
  echo "Não entendi o que você falou, vou assumir como não"
fi
echo "============================================================"
echo "            A instalação foi Muuuucluída"
echo "============================================================"
echo "Obrigado por baixar o StartupCow,eu estou amando desenvolver"
echo "esse projeto e mesmo que ele seja bem bestinha, eu espero que "
echo "tenha alegrado um momento do seu dia."
echo "- Feito por pixelcatBR"
echo "==========================================================="
mpg123 -q ~/vaca_mugido.mp3
