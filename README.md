# TaskApp — Gestión de Tareas y Recordatorios

## Requisitos
- Python 3.10+
- pip

## Instalación
```bash
cd TaskApp
pip install -r requirements.txt
```

## Ejecución
```bash
# Verificar imports primero
python test_imports.py

# Ejecutar la aplicación
python main.py
```

## Estructura del proyecto
- `core/`      → Lógica de negocio (modelos, storage, voz, scheduler)
- `ui/`        → Interfaz gráfica PySide6
- `data/`      → Almacenamiento JSON de tareas
- `utils/`     → Utilidades generales

## Funcionalidades
- ✅ Crear, editar y eliminar tareas
- ✅ Recordatorios por voz (pyttsx3)
- ✅ Reprogramación inteligente con sugerencias
- ✅ Filtros por estado, prioridad y búsqueda
- ✅ Informes con gráficos estadísticos
- ✅ Exportación CSV y TXT
- ✅ Interfaz moderna oscura con PySide6
- ✅ **Nuevas funcionalidades v1.2:**
  - 🔄 Tareas recurrentes con frecuencias predefinidas (diaria, semanal, quincenal, mensual, trimestral, anual)
  - ⚙️ Frecuencia personalizada (cada N días)
  - 📎 Archivos adjuntos por tarea (imágenes, documentos, texto)
  - 🖼️ Previsualización de imágenes en miniatura
  - 🗂️ Drag & drop de archivos al formulario
  - ♻️ Auto-creación de siguiente instancia al completar tarea recurrente
  - 🔢 Control de máximo de repeticiones y fecha de fin de recurrencia
