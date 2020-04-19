# Python's standard method resolution order(MRO)

[l1]: http://python-history.blogspot.com/2010/06/method-resolution-order.html
[Method resolution order history][l1].

- It follows ordering from Depth first left to right pattern. 
- There are cases when conflict arises then python will simply throw the error

```python
class A(object): pass
class B(object): pass
class X(A, B): pass
class Y(B, A): pass
class Z(X, Y): pass
```

- For example in above class, Class X says A should come before B while class Y says B should come before A
- Then when class Z inherits X and then Y. then order sets as follows:
- Z X A object B object Y B object A object

- As per the article ", in Python 2.3, we abandoned my home-grown 2.2 MRO algorithm in favor of the academically vetted C3 algorithm. One outcome of this is that **Python will now reject any inheritance hierarchy that has an inconsistent ordering of base classes**. For instance, in the previous example, there is an ordering conflict between class X and Y. For class X, there is a rule that says class A should be checked before class B. However, for class Y, the rule says that class B should be checked before A. In isolation, this discrepancy is fine, but if X and Y are ever combined together in the same inheritance hierarchy for another class (such as in the definition of class Z), that class will be rejected by the C3 algorithm. This, of course, matches the Zen of Python's "errors should never pass silently" rule."
