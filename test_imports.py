"""Script de verificación de imports — ejecutar antes de main.py"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

errors = []

def try_import(module_path: str):
    try:
        __import__(module_path)
        print(f"  [OK] {module_path}")
    except Exception as e:
        errors.append((module_path, str(e)))
        print(f"  [X] {module_path}: {e}")

print("\n[BUSQUEDA] Verificando imports del proyecto TaskApp...\n")
try_import("core.models")
try_import("core.storage")
try_import("core.voice")
try_import("core.scheduler")
try_import("ui.styles")
try_import("ui.components.task_card")
try_import("ui.components.task_form")
try_import("ui.components.reschedule_dialog")
try_import("ui.components.task_list")
try_import("ui.components.notification_bubble")
try_import("ui.reports.stats_widget")
try_import("ui.reports.report_view")
try_import("ui.main_window")
try_import("core.audio")
try_import("utils.autostart")
try_import("ui.components.settings_dialog")
try_import("utils.helpers")
# v1.2 — Nuevos módulos
try_import("core.recurrence")
try_import("utils.attachments")
try_import("ui.components.recurrence_widget")
try_import("ui.components.attachment_widget")

print(f"\n{'='*45}")
if not errors:
    print("[OK] Todos los módulos importan correctamente.")
    print("   TaskApp v1.2 lista. Ejecuta: python main.py")
else:
    print(f"[ERROR] Se encontraron {len(errors)} error(es):")
    for mod, err in errors:
        print(f"   -  {mod}: {err}")
print(f"{'='*45}\n")
