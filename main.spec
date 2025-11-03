# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py','utils/every_tools.py',
    'utils/global_variable.py','utils/hwnd_utils.py',
    'utils/key_tool.py','utils/md5_encryption.py',
    'utils/utils_tools.py','business/qjrj.py','business/table.py','business/task_xyyb_theory.py'],
    pathex=[],
    binaries=[
    ('D:\\project\\9yinHs\\models\\dd.54900.dll', 'models'),
    ('D:\\project\\9yinHs\\business','business'),
    ('D:\\project\\9yinHs\\utils','utils')
    ],
    datas=[('D:\project\9yinHs\models\9yinHs.ui', 'models' )],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
