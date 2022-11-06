# Recognition

### Локальная разработка
Клонируем репозиторий
```
git clone https://github.com/m-a-r-a-t/recognition.git
```
Зависимости
```
pip install -r requirements.txt
```
Запускаем находясь в корне
```
python -m app.main
```
### Build .exe файла под windows
Зависимости
```
pip install -r requirements.txt
```
```
pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew kivy.deps.gstreamer kivy
```
```
pip install --upgrade pyinstaller
```
##### Этап 1:

```
python -m PyInstaller --onefile --name digitalcode app\main.py
```
##### Этап 2: добавляем в файл digitalcode.spec то что выделено

 -*- mode: python ; coding: utf-8 -*-
```from kivy_deps import sdl2, glew```

block_cipher = None


a = Analysis(
    ['app\\main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz, ```Tree('app\\'),```
     a.scripts,
     a.binaries,
     a.zipfiles,
     a.datas,
     ```*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],```
     upx=True,
     name='touchtracer',
    ```console=False,```
)

##### Этап 3: 
```
python -m PyInstaller digitalcode.spec
```

##### Этап 4: из папки app копируем файл my.kv в папку dist

##### Этап 5: запускаем файл ```digitalcode.exe```