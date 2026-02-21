"""Punto de entrada principal de la aplicación TaskApp.
Orquesta la creación de servicios, ventana principal e inicio del scheduler."""

import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
from core.storage import StorageManager
from core.voice import VoiceManager
from core.scheduler import ReminderScheduler
from ui.main_window import MainWindow
from ui.styles import apply_styles

def get_app_root() -> str:
    """
    Retorna la ruta raíz de la app, compatible con:
    - Ejecución normal: python main.py
    - Bundle PyInstaller: TaskApp.exe
    """
    if getattr(sys, 'frozen', False):
        # Modo bundle PyInstaller (--onedir)
        return os.path.dirname(sys.executable)
    else:
        # Modo desarrollo
        return os.path.dirname(os.path.abspath(__file__))

# Establecer el directorio de trabajo a la raíz de la app
# Esto garantiza que todas las rutas relativas funcionen
os.chdir(get_app_root())

def setup_environment() -> None:
    """Configura variables de entorno y logging antes de crear QApplication."""
    import logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(name)s] %(levelname)s %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("taskapp.log", encoding="utf-8")
        ]
    )
    
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    
    if sys.platform == "win32":
        # Soporte para modo oscuro en Windows
        os.environ["QT_QPA_PLATFORM"] = "windows:darkmode=2"

def create_app() -> QApplication:
    """Crea y configura el objeto QApplication."""
    app = QApplication(sys.argv)
    
    # Soporte para HiDPI
    
    # Configurar fuente global
    font = QFont("Segoe UI", 10)
    font.setHintingPreference(QFont.PreferNoHinting)
    app.setFont(font)
    
    # Metadatos de la aplicación
    app.setApplicationName("TaskApp")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("TaskApp Dev")
    
    # Aplicar estilos QSS
    apply_styles(app)
    
    return app

def main() -> int:
    """Función principal que orquesta el arranque completo de la app."""
    
    # Paso 1 — Setup de entorno
    setup_environment()
    
    # Paso 2 — Crear QApplication
    app = create_app()
    
    # Paso 3 — Instanciar capas de servicio
    storage = StorageManager()
    voice = VoiceManager()
    scheduler = ReminderScheduler(storage=storage, voice=voice, interval=30)
    
    # Paso 4 — Crear y mostrar la ventana principal
    window = MainWindow(storage=storage, scheduler=scheduler, voice=voice)
    window.show()
    
    # Centrar la ventana en pantalla
    screen = app.primaryScreen().geometry()
    window_geo = window.frameGeometry()
    center = screen.center()
    window_geo.moveCenter(center)
    window.move(window_geo.topLeft())
    
    # Paso 5 — Iniciar el scheduler con delay
    # Evita condiciones de carrera esperando a que el event loop esté corriendo
    QTimer.singleShot(500, scheduler.start)
    
    # Paso 6 — Ejecutar el event loop
    try:
        return app.exec()
    except KeyboardInterrupt:
        # Asegurar limpieza en caso de interrupción por teclado
        scheduler.stop()
        voice.stop()
        return 0

if __name__ == "__main__":
    sys.exit(main())
