# taskapp.spec
# PyInstaller spec file para TaskApp v1.2
# Ejecutar con: pyinstaller taskapp.spec

import sys
from pathlib import Path

block_cipher = None

# Ruta raíz del proyecto
PROJECT_ROOT = Path(SPECPATH)

a = Analysis(
    # Punto de entrada principal
    [str(PROJECT_ROOT / 'main.py')],

    pathex=[str(PROJECT_ROOT)],

    binaries=[],

    # Archivos de datos que deben incluirse en el bundle
    datas=[
        # Carpeta data completa (tasks.json + attachments)
        (str(PROJECT_ROOT / 'data'), 'data'),
        # Assets (ícono, etc.)
        (str(PROJECT_ROOT / 'assets'), 'assets'),
    ],

    # Hidden imports: módulos que PyInstaller no detecta automáticamente
    hiddenimports=[
        # PySide6 módulos necesarios
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtCharts',
        'PySide6.QtSvg',
        'PySide6.QtSvgWidgets',
        'PySide6.QtNetwork',
        'PySide6.QtPrintSupport',
        # Matplotlib backend para Qt
        'matplotlib.backends.backend_qtagg',
        'matplotlib.backends.backend_qt5agg',
        'matplotlib',
        'matplotlib.pyplot',
        # pyttsx3 backends de Windows
        'pyttsx3',
        'pyttsx3.drivers',
        'pyttsx3.drivers.sapi5',
        'pyttsx3.drivers.nsss',
        'pyttsx3.drivers.espeak',
        'win32com.client',
        'win32api',
        'win32con',
        # shiboken6
        'shiboken6',
    ],

    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],

    excludes=[
        # Excluir módulos innecesarios para reducir tamaño
        'tkinter',
        'unittest',
        'email',
        'xmlrpc',
        'test',
        'distutils',
        'setuptools',
        'pkg_resources',
    ],

    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)

exe = EXE(
    pyz,
    a.scripts,
    [],                      # ← vacío para modo --onedir (recomendado con PySide6)
    exclude_binaries=True,   # ← True = modo onedir
    name='TaskApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,                # ← compresión UPX si está disponible
    console=False,           # ← SIN consola (modo windowed)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(PROJECT_ROOT / 'assets' / 'icon.ico'),
    version_file=str(PROJECT_ROOT / 'assets' / 'version_info.txt'),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='TaskApp',           # ← carpeta de salida en dist/TaskApp/
)
