#!/usr/bin/env python3
import sys
import time
import subprocess
import os
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

# Variável global para controlar o áudio
processo_audio = None
apocalipse_autorizado = False

class Overlay(QWidget):
    def __init__(self, texto="O APOCALIPSE DE VACAS ESTÁ CHEGANDO!"):
        super().__init__()
        self.texto = texto
        self.initUI()
        
    def initUI(self):
        # Janela transparente SEMPRE NO TOPO
        self.setWindowFlags(
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint | 
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Label centralizado
        self.label = QLabel(self.texto, self)
        self.label.setAlignment(Qt.AlignCenter)
        
        # Fonte grande e visível
        fonte = QFont("Arial", 48, QFont.Bold)
        self.label.setFont(fonte)
        self.label.setStyleSheet("""
            QLabel {
                color: white;
                background-color: rgba(0, 0, 0, 0.3);
                padding: 20px;
                border-radius: 10px;
            }
        """)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        # Tela inteira
        tela = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(0, 0, tela.width(), tela.height())
        
        # Mostra a janela
        self.show()
        self.raise_()
        self.activateWindow()

def mostrar_dialogo_confirmacao():
    """Mostra um diálogo de confirmação antes do apocalipse"""
    global apocalipse_autorizado
    
    try:
        # Cria uma aplicação Qt separada para o diálogo
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        # Mensagem personalizada sobre as chances raras
        msg_box = QMessageBox()
        msg_box.setWindowTitle("⚠ AVISO MUITO IMPORTANTE ⚠")
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("O APOCALIPSE DAS VACAS ESTÁ PRESTES A COMEÇAR!")
        msg_box.setInformativeText(
            "ESTE É UM EVENTO EXTREMAMENTE PERIGOSO!\n\n"
            "APERTANDO O PRIMEIRO BOTÃO AS VACAS SÃO LIBERADAS!\n"
            "JÁ NO SEGUNDO BOTÃO AS VACAS FICAM PRESAS EM UMA PRISÃO DE ALTA SEGURANÇA CHAMADA DE C.E.R.C.A.D.O!\n\n"
            "Você tem certeza que deseja invocar o Apocalipse das Vacas?\n"
            "Esta ação NÃO pode ser desfeita!"
        )
        
        # Botões personalizados
        botao_confirmar = msg_box.addButton("SIM, LIBERAR AS VACAS!", QMessageBox.YesRole)
        botao_cancelar = msg_box.addButton("NÃO, SALVE-ME!", QMessageBox.RejectRole)
        msg_box.setDefaultButton(botao_cancelar)
        
        # Estilo visual
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #2b2b2b;
                color: white;
            }
            QMessageBox QLabel {
                color: white;
                font-size: 14px;
            }
            QPushButton {
                background-color: #3c3c3c;
                color: white;
                border: 2px solid #555;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #505050;
            }
        """)
        
        # Mostra o diálogo e espera a resposta
        resposta = msg_box.exec_()
        
        # Verifica qual botão foi pressionado
        if msg_box.clickedButton() == botao_confirmar:
            print("🐄 APOCALIPSE AUTORIZADO! As vacas serão liberadas!")
            apocalipse_autorizado = True
            return True
        else:
            print("❌ APOCALIPSE CANCELADO! As vacas foram salvas... por enquanto.")
            apocalipse_autorizado = False
            return False
            
    except Exception as e:
        print(f"❌ Erro ao mostrar diálogo: {e}")
        # Em caso de erro, autoriza por segurança
        apocalipse_autorizado = True
        return True

def tocar_audio():
    """Toca o áudio em loop"""
    global processo_audio
    
    try:
        # Verifica se o arquivo existe
        if not os.path.exists("alerta.mp3"):
            print("⚠ Arquivo alerta.mp3 não encontrado!")
            return False
        
        # Mata processos anteriores
        subprocess.run("pkill -f mpg123 2>/dev/null", shell=True)
        time.sleep(0.2)
        
        # Inicia o áudio em loop
        processo_audio = subprocess.Popen(
            ["mpg123", "-q", "--loop", "-1", "alerta.mp3"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        print("🎵 Áudio iniciado com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao iniciar áudio: {e}")
        return False

def parar_audio():
    """Para o áudio completamente"""
    global processo_audio
    
    try:
        # Mata TODOS os processos mpg123
        subprocess.run("pkill -9 -f mpg123 2>/dev/null", shell=True)
        
        if processo_audio:
            try:
                processo_audio.kill()
                processo_audio.wait(timeout=1)
            except:
                pass
            processo_audio = None
        
        print("🔇 Áudio parado!")
        return True
    except:
        return False

def executar_vacas():
    """Executa o script das vacas"""
    global apocalipse_autorizado
    
    # Verifica se o apocalipse foi autorizado
    if not apocalipse_autorizado:
        print("❌ Apocalipse não autorizado! Vacas permanecem em paz.")
        parar_audio()
        return
    
    print("🐄 INICIANDO APOCALIPSE DAS VACAS!")
    print("💀 O FIM ESTÁ PRÓXIMO! MUUUUUUU!")
    
    try:
        for i in range(500):
            # Executa cow.py
            subprocess.Popen(
                ["python3", "cow.py"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            
            # Mostra progresso
            if (i + 1) % 10 == 0:
                print(f"🐄 {i+1} vacas liberadas...")
            
            time.sleep(0.5)
            
        print("✅ Apocalipse finalizado!")
        print("🎵 Áudio continua tocando...")
        print("ℹ Pressione Ctrl+C para parar")
        
        # Mantém o áudio tocando
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n👋 Finalizando...")
        parar_audio()
        sys.exit(0)
    except Exception as e:
        print(f"❌ Erro: {e}")
        parar_audio()

def main():
    global processo_audio, apocalipse_autorizado
    
    # 1. Inicia a aplicação Qt
    app = QApplication(sys.argv)
    
    # 2. MOSTRA O DIÁLOGO DE CONFIRMAÇÃO PRIMEIRO!
    print("🐄 VERIFICANDO AUTORIZAÇÃO PARA APOCALIPSE...")
    autorizado = mostrar_dialogo_confirmacao()
    
    # Se não for autorizado, encerra o programa
    if not autorizado:
        print("👋 Programa encerrado. Vacas seguras!")
        sys.exit(0)
    
    # 3. Cria e mostra o overlay (só se autorizado)
    overlay = Overlay()
    print("📢 OVERLAY MOSTRADO! O APOCALIPSE COMEÇARÁ EM BREVE!")
    
    # 4. Inicia o áudio (vai tocar até pararmos manualmente)
    tocar_audio()
    
    # 5. Timer para fechar o overlay após 5 segundos
    def fechar_overlay():
        print("⏰ Fechando overlay...")
        overlay.close()
        overlay.deleteLater()
        
        # 6. Inicia o apocalipse em uma thread separada
        thread_vacas = threading.Thread(target=executar_vacas, daemon=True)
        thread_vacas.start()
    
    # Usa QTimer para maior confiabilidade
    QTimer.singleShot(5000, fechar_overlay)
    
    # 7. Loop principal do Qt
    try:
        sys.exit(app.exec_())
    except SystemExit:
        # Garante que o áudio seja parado ao sair
        parar_audio()

if __name__ == '__main__':
    main()