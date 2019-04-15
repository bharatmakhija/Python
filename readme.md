# Popular Python runtimes

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

