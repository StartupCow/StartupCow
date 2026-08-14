#!/usr/bin/env python3
import sys
import time
import subprocess
import os
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

processo_audio = None
apocalipse_autorizado = False

class Overlay(QWidget):
    def __init__(self, texto="O APOCALIPSE DE VACAS ESTÁ CHEGANDO!"):
        super().__init__()
        self.texto = texto
        self.initUI()
        
    def initUI(self):
        self.setWindowFlags(
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint | 
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.label = QLabel(self.texto, self)
        self.label.setAlignment(Qt.AlignCenter)
        
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
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        tela = QApplication.primaryScreen().availableGeometry()
        self.setGeometry(0, 0, tela.width(), tela.height())
        
        self.show()
        self.raise_()
        self.activateWindow()

def mostrar_dialogo_confirmacao():
    global apocalipse_autorizado
    
    try:
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
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
        
        botao_confirmar = msg_box.addButton("SIM, LIBERAR AS VACAS!", QMessageBox.YesRole)
        botao_cancelar = msg_box.addButton("NÃO, SALVE-ME!", QMessageBox.RejectRole)
        msg_box.setDefaultButton(botao_cancelar)
        
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
        
        resposta = msg_box.exec_()
        
        if msg_box.clickedButton() == botao_confirmar:
            apocalipse_autorizado = True
            return True
        else:
            apocalipse_autorizado = False
            return False
            
    except Exception as e:
        apocalipse_autorizado = True
        return True

def tocar_audio():
    global processo_audio
    
    try:
        if not os.path.exists("alerta.mp3"):
            return False
        
        subprocess.run("pkill -f mpg123 2>/dev/null", shell=True)
        time.sleep(0.2)
        
        processo_audio = subprocess.Popen(
            ["mpg123", "-q", "--loop", "-1", "alerta.mp3"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        return True
        
    except Exception as e:
        return False

def parar_audio():
    global processo_audio
    
    try:
        subprocess.run("pkill -9 -f mpg123 2>/dev/null", shell=True)
        
        if processo_audio:
            try:
                processo_audio.kill()
                processo_audio.wait(timeout=1)
            except:
                pass
            processo_audio = None
        
        return True
    except:
        return False

def executar_vacas():
    global apocalipse_autorizado
    
    if not apocalipse_autorizado:
        parar_audio()
        return
    
    try:
        for i in range(500):
            subprocess.Popen(
                ["python3", "cow.py"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            
            time.sleep(0.5)
            
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        parar_audio()
        sys.exit(0)
    except Exception as e:
        parar_audio()

def main():
    global processo_audio, apocalipse_autorizado
    
    app = QApplication(sys.argv)
    
    autorizado = mostrar_dialogo_confirmacao()
    
    if not autorizado:
        sys.exit(0)
    
    overlay = Overlay()
    
    tocar_audio()
    
    def fechar_overlay():
        overlay.close()
        overlay.deleteLater()
        
        thread_vacas = threading.Thread(target=executar_vacas, daemon=True)
        thread_vacas.start()
    
    QTimer.singleShot(5000, fechar_overlay)
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        parar_audio()

if __name__ == '__main__':
    main()
