# File Handling

<h4>Reading a file</h4>

- using withopen create a  file handler.
- iterate that handler and do whatever you want.

```python
with open('hello.txt','r') as f:
    for line in f:
        print(line)
```

<h4>Modes</h4> 

- 'r' - readmode. file pointer is placed at the beginning of the file. This is the default mode.

- 'w' - writeMode. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing. 

-  'r+' - both read and write mode. doesn't delete the content of the file and doesn't create a new file if such file doesn't exist.

- 'w+' - both read and write mode. deletes the content of the file and creates it if it doesn't exist. So yes, if the file already exists w+ will erase the file and give you an empty file.

- 'a': append mode. whatever is already written in file can't be changed but new content can be appended.The file pointer is at the end of the file if the file exists. 
That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

- 'a+' - for read and append mode. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

<h4>If we append 'b' in all above modes then same operations will happen in binary mode i.e file will be opened in binary format.</h4>

- 'rb', 'rb+', 'wb', 'wb+', 'ab', 'ab+'

