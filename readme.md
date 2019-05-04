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
### Quick Links
[Create custom map-reduce][L3]   
[Generators][L4]   
[Working with counters][L5]   
[Python Collection Modules][L6]

### References
[Tutorial Points: Database Access using python 3][L1]   
[Multi-Threading][L2]
