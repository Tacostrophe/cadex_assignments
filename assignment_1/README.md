# Assignment 1. 3D curves evaluation application

## Описание поставленной задачи

Design a small program in C++, C#, Java or other-object oriented language that would implement support of 3D curves hierarchy.

1. Support two types of 2D geometic curves - lines and ellipses. (See details below). Each curve should be able to return a 2D point and a first derivative (2D vector) per parameter t along the curve.

2. Populate a container (e.g. vector or list) of objects of these types created with random or fixed parameters.

3. Pring coordinates of points and derivatives of all curves in the container at t=PI/4.

Requimrements to the implementation:

1. The implementation must use virtual methods.

Curve definitions:

- All curves are parametrically defind. i.e. a point is calculated using some C(t) formula.

- Line is defined by its origin point O and direction D: C(t) = O + D*t.

- Ellipse is defined by its two radii, along X and Y axes.

## Инструкция по запуску

В репозитории создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Запустить программу командой будучи в папке с /assignment_1:

```bash
python3 curves.py
```
