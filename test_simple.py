import sys
import os
print("Iniciando script...")
try:
    from core.storage import StorageManager
    print("StorageManager importado")
    from core.voice import VoiceManager
    print("VoiceManager importado")
    from core.scheduler import ReminderScheduler
    print("ReminderScheduler importado")
except Exception as e:
    print(f"Error en imports: {e}")
    sys.exit(1)

print("Todo importado correctamente.")
