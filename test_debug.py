import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from core.models import Task, TaskStatus, TaskPriority
from core.storage import StorageManager
from core.voice import VoiceManager
from core.scheduler import ReminderScheduler
from datetime import datetime

def test():
    print("Creando QApplication...")
    app = QApplication(sys.argv)
    
    print("Creando StorageManager...")
    storage = StorageManager()
    
    print("Creando VoiceManager...")
    voice = VoiceManager()
    
    print("Creando ReminderScheduler...")
    scheduler = ReminderScheduler(storage=storage, voice=voice, interval=1)
    
    # Crear tarea para el minuto actual
    now = datetime.now()
    due_time = now.strftime("%H:%M")
    due_date = now.strftime("%Y-%m-%d")
    
    t = Task(description="Prueba", date=due_date, time=due_time, voice_reminder=True)
    storage.add_task(t)
    print(f"Tarea creada para {due_time}")
    
    def on_reminded(tid):
        print("¡RECORDATORIO DISPARADO!")
        app.quit()
        
    scheduler.task_reminded.connect(on_reminded)
    
    print("Iniciando scheduler...")
    scheduler.start()
    
    print("Ejecutando app (esperando 10s)...")
    QTimer.singleShot(10000, app.quit)
    app.exec()
    print("Prueba finalizada.")

if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    test()
