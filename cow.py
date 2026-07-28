import sys
import subprocess
import os
import signal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QPoint
from PyQt5.QtGui import QPainter, QPixmap

class VacaOverlay(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configurar janela transparente
        self.setWindowFlags(
            Qt.WindowStaysOnTopHint | 
            Qt.FramelessWindowHint | 
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(200, 200)
        
        # Label para a imagem
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 200, 200)
        self.label.setAlignment(Qt.AlignCenter)
        
        # Carregar imagem
        self.carregar_imagem()
        
        # Configurar tela
        self.screen = QApplication.primaryScreen().geometry()
        
        # Posição: fora da tela à esquerda
        self.y_pos = self.screen.height() - 250
        self.x_inicial = -250
        self.move(self.x_inicial, self.y_pos)
        
        # Animação
        self.animacao = QPropertyAnimation(self, b"pos")
        self.animacao.setDuration(3000)
        self.animacao.setEasingCurve(QEasingCurve.InOutQuad)
        
        # Controle de áudio
        self.ja_mugiu = False
        self.processo_audio = None
        
        # Iniciar após 1 segundo
        QTimer.singleShot(1000, self.entrar_na_tela)
        
    def carregar_imagem(self):
        """Tenta carregar imagem PNG"""
        try:
            # Tenta carregar do arquivo
            pixmap = QPixmap("vaca.png")
            if not pixmap.isNull():
                # Redimensionar mantendo proporção
                pixmap = pixmap.scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.label.setPixmap(pixmap)
                print("✅ Imagem carregada: vaca.png")
                return True
        except:
            pass
        
        # Fallback: usar texto
        self.label.setText("🐮")
        self.label.setStyleSheet("font-size: 150px; background: transparent;")
        print("⚠ Usando emoji como fallback")
        return False
        
    def entrar_na_tela(self):
        """Entra pela esquerda até o centro"""
        centro_x = (self.screen.width() - self.width()) // 2
        
        self.animacao.setStartValue(QPoint(self.x_inicial, self.y_pos))
        self.animacao.setEndValue(QPoint(centro_x, self.y_pos))
        self.animacao.finished.connect(self.mugir)
        self.animacao.start()
        
    def mugir(self):
        """Toca o som uma única vez"""
        if self.ja_mugiu:
            return
            
        self.ja_mugiu = True
        print("🐮 Muuuu!")
        
        # Tocar som - AGORA SEM MATAR OUTROS PROCESSOS
        try:
            if os.path.exists("vaca_mugido.mp3"):
                import shutil
                if shutil.which('mpg123'):
                    self.processo_audio = subprocess.Popen(
                        ['mpg123', '-q', 'vaca_mugido.mp3'],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                    )
                    print("🔊 Áudio tocando...")
        except Exception as e:
            print(f"⚠ Erro no áudio: {e}")
        
        QTimer.singleShot(2500, self.sair_da_tela)
        
    def sair_da_tela(self):
        """Sai pela direita"""
        x_final = self.screen.width() + 200
        
        self.animacao.setStartValue(self.pos())
        self.animacao.setEndValue(QPoint(x_final, self.y_pos))
        self.animacao.setDuration(2500)
        self.animacao.finished.connect(self.fechar)
        self.animacao.start()
        
    def fechar(self):
        """Fecha a aplicação - NÃO MATA OS OUTROS PROCESSOS DE ÁUDIO"""
        print("🐄 Vaca foi embora!")
        
        # Mata APENAS o processo de áudio desta vaca
        if self.processo_audio:
            try:
                self.processo_audio.terminate()
                self.processo_audio.wait(timeout=0.5)
            except:
                try:
                    self.processo_audio.kill()
                except:
                    pass
            self.processo_audio = None
        
        # NÃO MATA TODOS OS mpg123! (Removido o pkill)
        # Agora só mata o processo específico desta vaca
        
        # Fechar a janela
        self.close()
        
        # Forçar saída do aplicativo
        QApplication.quit()
        
    def paintEvent(self, event):
        """Mantém fundo transparente"""
        painter = QPainter(self)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.fillRect(self.rect(), Qt.transparent)
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Criar a vaca
    vaca = VacaOverlay()
    vaca.show()
    
    print("🐄 Vaca overlay iniciada!")
    print("   - A vaca entra pela esquerda")
    print("   - Anda em linha reta até o centro")
    print("   - Muge uma única vez")
    print("   - Sai pela direita")
    print("   - Fecha completamente no final")
    
    exit_code = app.exec_()
    
    # NÃO MATA TODOS OS PROCESSOS - só sai
    print("👋 Vaca finalizada!")
    sys.exit(exit_code)