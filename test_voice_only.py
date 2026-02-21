import sys
import os
import time
from PySide6.QtWidgets import QApplication, QMessageBox
from core.voice import VoiceManager

def test_voice():
    app = QApplication(sys.argv)
    voice = VoiceManager()
    
    msg = "Hola. Esta es una prueba del sistema de voz de Task App. Si escuchas esto, el motor está funcionando correctamente."
    print("Iniciando prueba de voz...")
    voice.speak(msg)
    
    QMessageBox.information(None, "Prueba de Voz", "Deberías estar escuchando el mensaje ahora.\n\nSi no escuchas nada, verifica que el volumen de tu sistema esté alto.")
    
    # Esperar un poco para que termine de hablar
    time.sleep(1)
    sys.exit(0)

if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    test_voice()
