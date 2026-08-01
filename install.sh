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
sed -i "s/\/home\/\[seu_user\]/\/home\/$USER/g" StartupCow/startup.desktop
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
echo "============================================================"
echo "            A instalação foi Muuuucluída"
echo "============================================================"
mpg123 -q ~/vaca_mugido.mp3
