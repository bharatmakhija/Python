# Welcome to Python

If you want to learn python, coming from a java paradigm and have more of java coding style in your blood! You have just landed on right page :-).
- Here a folder structure is followed to handle different use-cases one struggles through like how classes are created, how to achive inheritance and create abstract classes, what are generators and why we should use them, some best practices etc etc. 
- All of these things are folder names only. Go inside the topic you want to learn , there is a readme prepared specifically for that topic to boost up your learning then if you feel like you can check out the code as well. Happy Learning!!

<h4>What this is not?</h4>
- This is not a beginners to advanced type of tutorials. This is basically a topic wise tutorial which can be a folder name, this can be a best practice or some "how to" or some boiler plate  which can be another folder name and so on.
- I have intentionally kept the design open as many topics can depend on one another and some things should go together to make sense out of it. 

# A note for you :)
I add content in this in my free time(mostly weekends) or sometimes in weekdays when i am early from office. This is still in progress and lots of things are yet to be added. 
Please feel free to fork and add back something valuable, will really appretiate that!! Meanwhile I will keep adding and updating the content.


<h3>Some basics to keep here: </h3>
<h4> Popular Python runtimes<h4>

CPython
Jython
IronPython PyPy
- computers come with multiple versions of standard CPython pre-installed.

<h4> Check python version: </h4>

````
$python --version
````
<h4> Python3 verison: </h4>

````
python3 --version
````

<h4> Creating virtual environment: </h4>

````
python3 -m venv myenv
````

- here myenv is the name of virtual environment, we can give any name.

- Then activate the virtual environment

```
source myenv/bin/activate

#After this command, virtual env should start reflecting in 
#terminal like this

# (myenv) at the leftmost corner
```

- Deactivating a virtual environment:

```
deactivate
```

<h4>Install requirements in virtual environment using pip</h4>

- before this upgrade pip using following command:

```
pip install --upgrade pip
```


- After this install requirements from requirements.txt file:
- make sure your virtual env is activated.

```
pip install -r requirements.txt
```

- here -r is for recursive.

Once requirements are installed, we are good to go. 

<h4> Creating requirements.txt file</h4>

- on the go if we change requirements or add new dependencies we need to keep modifying this file.

- we can generate this file from venv directly using following command:

```
pip freeze > requirements.txt
```

- make sure venv is active so that dependencies are being picked from there only rather than global python packages.

[L1]: https://www.tutorialspoint.com/python3/python_database_access.htm
[L2]: https://www.tutorialspoint.com/python3/python_multithreading.htm
[L3]: https://github.com/bharatmakhija/Python/tree/master/CustomMapReduce
[L4]: https://github.com/bharatmakhija/Python/tree/master/Generators
[L5]: https://github.com/bharatmakhija/Python/blob/master/PythonCollectionModule/my_counter.ipynb
[L6]: https://github.com/bharatmakhija/Python/blob/master/PythonCollectionModule/
[L7]: https://github.com/bharatmakhija/Python/tree/master/Closures
[L8]: https://github.com/bharatmakhija/Python/tree/master/ClassMethodsInPython
[L9]: https://github.com/bharatmakhija/Python/tree/master/Inheritance
[L10]: https://github.com/bharatmakhija/Python/tree/master/MixInClasses
[L11]: https://github.com/bharatmakhija/Python/tree/master/Iterators
[L12]: https://github.com/bharatmakhija/Python/tree/master/Comprehension
[L13]: https://github.com/bharatmakhija/Python/tree/master/ConvertClassToDictionary
[L14]: https://github.com/bharatmakhija/Python/tree/master/CreatingAClass
[L15]: https://github.com/bharatmakhija/Python/tree/master/CustomContainerClasses
[L16]: https://github.com/bharatmakhija/Python/tree/master/CreatingAbstactClass
[L17]: https://github.com/bharatmakhija/Python/tree/master/DateTime
[L18]: https://github.com/bharatmakhija/Python/tree/master/Decorators
[L19]: https://github.com/bharatmakhija/Python/tree/master/DownloadFileFromUrl
[L20]: https://github.com/bharatmakhija/Python/tree/master/FileHandling
[L21]: https://github.com/bharatmakhija/Python/tree/master/Functions
[L22]: https://github.com/bharatmakhija/Python/tree/master/GenerateRandomNumber
[L23]: https://github.com/bharatmakhija/Python/tree/master/None_Zero_EmptyString
[L24]: https://github.com/bharatmakhija/Python/tree/master/OptionalParameters
[L25]: https://github.com/bharatmakhija/Python/tree/master/PublicVsPrivateAttributes
[L26]:https://github.com/bharatmakhija/Python/tree/master/RaisingExceptions
[L27]: https://github.com/bharatmakhija/Python/tree/master/ReturnExceptionThanNone
[L28]: https://github.com/bharatmakhija/Python/tree/master/Sorting
[L29]: https://github.com/bharatmakhija/Python/tree/master/Splitwise
[L30]: https://github.com/bharatmakhija/Python/tree/master/SshWithPython
[L31]: https://github.com/bharatmakhija/Python/tree/master/StandardMethodResolutionOrder
[L32]: https://github.com/bharatmakhija/Python/tree/master/Strings
[L33]: https://github.com/bharatmakhija/Python/tree/master/Threading
[L34]: https://github.com/bharatmakhija/Python/tree/master/WorkingWithOsPackage

### Quick Links
<h4>A</h4>
[Abstract Class][L16]
[Attributes][L25]
<h4>B</h4>
[Best Practice: Return exception than None][L27]
<h4>C</h4>
[Comprehension][L12]
[Closures][L7]
[Class Methods][L8]
[counters][L5]
[Collection Modules][L6]
[Class to Dictionary converter][L13]
[Class Creation][L14]
[Container classes][L15]

<h4>D</h4>
[Decorators][L18]
[Datetime in python][L17]
[Download file from url][L19]
<h4>E</h4>
[Empty String handling][L23]
[Exceptions raising][L26]
[Returning Exceptions][L27]
<h4>F</h4>
[Functions][L21]
[File Handling][L20]
<h4>G</h4>
[Generators][L4]
<h4>H</h4>
<h4>I</h4>
[Iterators][L11]
[Inheritance][L9]
<h4>J</h4>
<h4>K</h4>
<h4>L</h4>
<h4>M</h4>
[MixInClasses][L10]
[custom map-reduce][L3] 
<h4>N</h4>
[Non Zero empty string handling][L23]
<h4>O</h4>
[OOP Basic][L14]
[Optional Parameters][L24]
[OS Package python][L34]
<h4>P</h4>
[Public vs Private attributes][L25]
<h4>Q</h4>
<h4>R</h4>
[Random Number generator][L22]
<h4>S</h4>
[Strings][L32]
[Sorting][L28]
[Splitwise: Python App][L29]
[SSH with Python][L30]
[StandardMethodResolutionOrder][L31]
<h4>T</h4>
[Threading][L33]
<h4>U</h4>
<h4>V</h4>
<h4>W</h4>
<h4>X</h4>
<h4>Y</h4>
<h4>Z</h4>  



   
   




### References
[Tutorial Points: Database Access using python 3][L1]   
[Multi-Threading][L2]
