import sys
import os
import time
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from core.models import Task, TaskStatus, TaskPriority
from core.storage import StorageManager
from core.voice import VoiceManager
from core.scheduler import ReminderScheduler
from datetime import datetime, timedelta

def test_flow():
    app = QApplication(sys.argv)
    
    # Asegurarnos de limpiar tareas previas de prueba para no confundir
    storage = StorageManager()
    all_tasks = storage.load_all()
    storage.save_all([t for t in all_tasks if "prueba" not in t.description])
    
    voice = VoiceManager()
    # Intervalo de 1 segundo para rapidez
    scheduler = ReminderScheduler(storage=storage, voice=voice, interval=1)
    
    # Crear una tarea para YA mismo (el minuto actual)
    now = datetime.now()
    due_time = now.strftime("%H:%M")
    due_date = now.strftime("%Y-%m-%d")
    
    test_task = Task(
        description="Tarea de prueba de voz URGENTE",
        date=due_date,
        time=due_time,
        status=TaskStatus.PENDING,
        priority=TaskPriority.HIGH,
        voice_reminder=True,
        notes="Prueba de integración de voz"
    )
    
    print(f"Hora actual: {now.strftime('%H:%M:%S')}")
    print(f"Creando tarea para las {due_time}...")
    storage.add_task(test_task)
    
    # Verificar que se guardó
    saved_task = storage.get_task_by_id(test_task.id)
    if saved_task:
        print(f"Tarea guardada correctamente con ID {saved_task.id}")
    else:
        print("ERROR: La tarea no se guardó.")
        app.exit(1)

    def on_due(tid):
        if tid == test_task.id:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] SEÑAL: task_due recibida")

    def on_reminded(tid):
        if tid == test_task.id:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] SEÑAL: task_reminded recibida!")
            print("El recordatorio debería estar sonando ahora.")
            # Esperar 5 segundos para que termine de hablar antes de cerrar
            QTimer.singleShot(5000, lambda: app.exit(0))
            
    def on_voice_error(msg):
        print(f"ERROR DE VOZ: {msg}")

    scheduler.task_due.connect(on_due)
    scheduler.task_reminded.connect(on_reminded)
    voice._on_error = on_voice_error # Patch temporal para ver errores

    print("Iniciando scheduler...")
    scheduler.start()
    
    # Timeout de 15 segundos
    QTimer.singleShot(15000, lambda: app.exit(1))
    
    sys.exit(app.exec())

if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    test_flow()
