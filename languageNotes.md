
### Python 2 to Python3 porting process

http://portingguide.readthedocs.io/en/latest/process.html

### New style classes vs classical classes

New-style classes were introduced in Python 2.2 to unify the concepts of class and type. A new-style class is simply a user-defined type, no more, no less. If x is an instance of a new-style class, then type(x) is typically the same as x.__class__ (although this is not guaranteed – a new-style class instance is permitted to override the value returned for x.__class__).

The major motivation for introducing new-style classes is to provide a unified object model with a full meta-model. It also has a number of practical benefits, like the ability to subclass most built-in types, or the introduction of “descriptors”, which enable computed properties.

New-style classes are created by specifying another new-style class (i.e. a type) as a parent class, or the “top-level type” `object` if no other parent is needed

**Note: super() only works for new-style classes**

**Note: In Python 3, all classes are new-style: object is the default superclass,but for python2 you have to do** 
``` python
class MyNewStyleClass(object):
    pass
```

### Keyworded arguments in function

Python allows keyworded arguments in functions
e.g. here name and last are keyworded arguments
``` python
def doSomething(a, b, name, last):
    pass

doSomething(1,2, name="Ok", last="go")
```
**Note: Keyworded arguments are only allowed after unnamed arguments**
otherwise you will get error: SyntaxError: non-keyword arg after keyword arg

### Use of `*args` and `**kwargs` in function definitions

Used to pass arbitrary number of arguments to a function.

* `*args` is used to send a non-keyworded argument list, like a rest parameter
* `**kwargs` is used to send a keyworded variable e.g. `add(name="Oh", last="Hey")`, like a map

below is an example of both types combined:
``` python
def test_var_args(firstarg, *args, **kwargs):
    print "firstarg is ", firstarg
    for arg in args:
        print "arg is ", arg
    for key, value in kwargs.items():
        print "key is ", key, " value is ", value

# 
test_var_args(42, 'hi', True, 'eggs', 'foo', name="John", last="Doe")
```

### Python Data Model

Also refer http://effbot.org/zone/python-list.htm

### Copying data structures in python

In python, = is only used for reference assignment, no sort of value copying takes place using =, unless the value is a primitive value.

Use following:
``` py
import copy

newobj = copy.copy(oldobj) # shallow copy
newobj = copy.deepcopy(oldobj) # deep (recursive) copy
```

Some objects can be copied more easily.
* Dictionaries have a copy method:
``` py
newdict = olddict.copy()
```

* Sequences can be copied by slicing:
``` py
new_list = L[:] # create a copy of L
```
List comprehensions, and functions like map, filter etc also return new lists.

You can also use the list, tuple, dict, and set functions to copy the corresponding objects, and to convert between different sequence types:
``` py
new_list = list(L) # copy
new_dict = dict(olddict) # copy

new_set = set(L) # convert list to set
new_tuple = tuple(L) # convert list to tuple
```

#### Python Tuples

Python tuples are product types indexed by numbers only.
e.g.
``` py
tu = ("hey", 1, True)
t2 = "hi", 3, False   # can create tuples without parens as long as commas
print tu[1]

tu[0] = 22 # assignment not possible, crashes, they are immutable in a sense that crash happens on assignment, instead of returning of a new tuple etc.

newt = tu # newt is reference to tu, no deep copy

print tu
print newt

# tuples support destructuring/unpacking
(x, y, z) = newt
print x, y, z

#tuples support slicing, returning tuples
kk = tu[0:2]


```

### Inheritance in Python

Unlike Java, Python does have multiple inheritance.
