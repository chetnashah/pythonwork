
Recommended linter is flake8, which can be installed via pip or other ways.


Always put a setup.cfg in ur project with
[flake8] at the top.

When used with emacs, for autocompletion and other stuff, it requires to open a infereior python(REPL) within emacs


#### Checking python version running in your script

``` python
from __future__ import print_function #to make print() work in python2
import sys
print(sys.version)
```