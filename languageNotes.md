
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

### Inheritance in Python

Unlike Java, Python does have multiple inheritance.
