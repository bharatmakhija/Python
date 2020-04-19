# Generators

- generators are used when we don't want to return full result 
alltogether instead partially in multiple iterations.

- this is used when there are chances that memory issues can happen.

for ex: we have a string we want to index :

"abcde"

what we will do is we will create a list and store its indexes there and return in one go

"abcde" -> [0,1,2,3,4]  we will return this list.

what if this string becomes of infinite length or something which cann't fit in memory to run in one shot.

"abc....infi"

In this case we can't simply generate the index list, what we should do is read this string in parts , generate results in parts and keep returning. 
This is where generators can be used.

- generators are nothing but functions that instead of using return keyword use 'yield' keyword to return results at middle of execution
and then continue execution further.


```python
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ': # we are assuming that words are seperated by single space
            yield index + 1
```
- generators prevent your programs from going out of memory and crash.
-  use generators when inputs can be of huge length.

<h4> There is a gotcha, unlike lists iterators returned by generators are stateful and can't be reused.
</h4>
