
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


### Python Data Model

### Inheritance in Python

Unlike Java, Python does have multiple inheritance.
