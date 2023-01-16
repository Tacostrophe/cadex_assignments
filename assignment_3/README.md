# Assignment 3. Cross-platform build script

## Описание поставленной задачи

1. Create cross-platform build script for the simplest C/C++ program (triangle surface area computation). The code is provided below – it contains an intentional error (bug) inside the code.
Make sure to find it and fix it.

2. The build script must be based on cmake, qmake, GNU make or any other type at your discretion.

3. The application must be made in the form of a shared library (.dll, .so, .dylib) and executable (.exe).

### Инструкции по применению (рекомендации)

Перед запуском должен быть установлен [cmake](https://cmake.org/)

Перед запуском скрипта для компиляции рекомендуется создать в папке /assignment_3 папку /build и перейти в нее

Из папки /build

```bash
cmake ../sources
make
```

Для повторной компиляци в случае изменения программы следует из папки /build выполнить команду

```bash
make
```

В папке /build будет создан ряд файлов в том числе файл **project** (project.exe для windows) - исполняемый файл.
