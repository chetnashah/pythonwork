### What is a module in python?

Any python file(.py file) is a python module.
Any module can load stuff from any other module.

### What is a package in python?

 A package is a collection of Python modules: while a module is a single Python file, a package is a directory of Python modules containing an additional `__init__.py` file, to distinguish a package from a directory that just happens to contain a bunch of Python scripts. Packages can be nested to any depth, provided that the corresponding directories contain their own `__init__.py` file.

 An example file organization can look like:

 ```
 sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py

 ```

### Naming conventions

* module names and package names should be lowercase and concise, e.g. foo.py and sounds/

* Use a leading underscore for modules that are meant to be private or internal e.g. _internals.py

* Don't use same names as stdlib module names like math etc.

### What is role of `sys.path` i.e Module Search Path?

``` sh
>>> import sys
>>> sys.path #... long path where python will looks for imports by default e.g all the pip packages you installed, they lie in some path that must be present in sys.path for import to work successfully
```

### What does importing a module do?

When a module is imported, all of statements in the module execute from top to bottom, and the variable bindings are namespaced inside the module name.

Variations on import statement, e.g. from does not affect execution, import always executes the entire file.

### Module loading and caching

### Import statements

Assume PointDocStrins.py file/module exists

1. Simple import (the module)

 ``` python
 import PointDocStrings # PointDocStrings.py is a file/module

# runs PointDocStrings.py from top to bottom
 # use all bindings of PointDocStrings which are namespaced under it
 p1 = PointDocStrings.Point()
 ```

2. Simple import (the module) with renaming
Namespace preserved but renamed.
``` python
import numpy as np
zeros = np.zeros(2,5)
```

3. from Module import Binding

``` python
# Note : Point loses namespace
from PointDocStrings import Point
p1 = Point()
```

4. from Module import Binding renamed via (as)

``` python
# Note : Point loses namespace
from PointDocStrings import Point as Pt
p1 = Pt()
```

**Below: Usage with packages**

5. import Package.Module
PointDocStrings.py module sits inside directory/package named Geometry

``` python
from Geometry import PointDocStrings
p1 = PointDocStrings.Point()
```

6. from Package import Module
PointDocStrings.py module sits inside directory/package named Geometry

``` python
from Geometry import PointDocStrings
p1 = PointDocStrings.Point()
```

### Role of `__init.py` in packages

export bindings for package,
Kind of converts package into a module by specifyig what binding it exports in `__init__.py`,
This is also seen in many javascript libraries folders' index.js where a lot of stuff inside the directory is imported, and re-exported.

### Explicit Relative Imports vs Relative Imports vs Absolute Imports

### Talks 
https://www.youtube.com/watch?v=0oTh1CXRaQ0