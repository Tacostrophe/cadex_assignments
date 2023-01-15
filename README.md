# cadex_assignments

### Assignment 1. 3D curves evaluation application.

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


### Assignment 2. Compute triangulation on cylinder using CAD Exchanger tools.

1. Using CAD Exchanger SDK (see documentation at https://docs.cadexchanger.com/sdk/, download here) develop a small application in C++, C# or Java that would create a part consisting of a solid cylinder.)

a. Hint: refer to a list of SDK examples to reuse their functionality.

2. Generate a triangulation (triangular mesh)

3. Compute programmatically a number of triangles.

4. Export the model to an STL file.

5. Open that STL file in CAD Exchanger Cloud (https://cloud.cadexchanger.com) and make sure it is successfully loaded.


### Assignment 3. Cross-platform build script.

1. Create cross-platform build script for the simplest C/C++ program (triangle surface area computation). The code is provided below – it contains an intentional error (bug) inside the code.

Make sure to find it and fix it.

2. The build script must be based on cmake, qmake, GNU make or any other type at your discretion.

3. The application must be made in the form of a shared library (.dll, .so, .dylib) and executable (.exe).


### Assignment 4. Using script languages.

1. Using a script language of your choice (.bat, .sh, Perl, etc) demonstrate some sophisticated automation task (processing folders and files, working with strings or expressions, etc).

2. There is intentionally no prescribed scenario. It is up to you to select the scenario and demonstrate your skills at their best.


### Assignment 5. Any software development project at all.

1. You can demonstrate any development project (from your prior experience, own education, some another test assignment, etc) that you believe can demonstrate your technical skills. Web programming or computer vision, machine learning or “hello world” .bash scripts, Python or Javascript, GUI or Linux kernel – really anything.

2. Just make sure it really shows the best of you.
