
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

#### Dir management

Get current directory with 
``` python
import os
os.getcwd()
```
and change directories with
``` python
import os
os.chdir('destdir')
```


### Jupyter Notebooks

#### To write/save
```
%%writefile myfile.py
```
write/save cell contents into myfile.py (use -a to append). Another alias: %%file myfile.py

#### To run
```
%run myfile.py
```
run myfile.py and output results in the current cell

#### To load/import
```
%load myfile.py
```
load "import" myfile.py into the current cell
**Note** : Load just populates the cell, does not execute it, to do that use %run

#### For more magic and help
```
%lsmagic
```
list all the other cool cell magic commands.

#### Help on a command name
```
%COMMAND-NAME?
```
for help on how to use a certain command. i.e. %run?
Note

#### Using unix commands from notebook
Beside the cell magic commands, IPython notebook (now Jupyter notebook) is so cool that it allows you to use any unix command right from the cell (this is also equivalent to using the %%bash cell magic command).

To run a unix command from the cell, just precede your command with ! mark. for example:
```
!python --version see your python version
!python myfile.py run myfile.py 
```
and output results in the current cell, just like %run (see the difference between !python and %run in the comments below).