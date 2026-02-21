import sys
import os
from PySide6.QtWidgets import QApplication
from ui.components.notification_bubble import NotificationBubble

def test_bubble():
    # Creamos la aplicación (necesaria para cualquier widget de Qt)
    app = QApplication(sys.argv)
    
    print("Lanzando burbuja de prueba...")
    # Creamos la burbuja con info de prueba
    bubble = NotificationBubble(
        title="🧪 Prueba de Burbuja",
        message="¡Hola! Soy la nueva burbuja flotante.\nPuedes arrastrarme por la pantalla o cerrarme en la X."
    )
    
    # Mostramos la burbuja
    bubble.show()
    
    print("Burbuja mostrada. La prueba terminará cuando cierres la burbuja o pasen 15 segundos.")
    
    # Salir automáticamente después de 15 segundos por seguridad
    from PySide6.QtCore import QTimer
    QTimer.singleShot(15000, app.quit)
    
    sys.exit(app.exec())

if __name__ == "__main__":
    # Aseguramos que el path incluya la carpeta raíz del proyecto
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    test_bubble()
