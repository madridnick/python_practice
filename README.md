#Unix
**Saving a Remote File with a Different Name with curl -o:**
```curl -o [shortname] [url] ```

**Rename file:**
```mv old-file-name new-file-name```



#Python

**Get current working directory**
```python
import os
os.getcwd()
```

**Open a data file**
```python
import os
os.listdir("/Users/my_data_file")
```

**Read a csv file and print rows**
```python
import csv
with open('file_name.csv', 'rb') as csvfile:
    rest = csv.reader(csvfile, delimiter=',')
    for row in rest:
        print row
```

**Get each row as a `dict` with `csv.DictReader`**
```python
import csv
with open('/Users/nickmadrid/Desktop/open_data/berkeley_salaries_2013.csv', 'rb') as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    for row in data:
        employee_name = row["Employee Name"]
        job_title = row["Job Title"]
    print row
```

**Pandas read csv file with `pd.read_csv`**
```python
import pandas as pd
df = pd.read_csv('/Users/nickmadrid/Desktop/open_data/berkeley_salaries_2013.csv')
df #prints entire dataframe
df.head() #prints first 5 rows
df.dtypes #verify datatypes
print df.columns #print columns
```

**New dataframe without the first three rows**
```python
df2 = df.ix[3:]
```

**Create a new file, write to that file, delete that file**
```python
import os

#create new file in a specific directory, print the name and close the file
new_file = open('/Users/name/Desktop/directory/new_file.txt', 'w')
#Windows: new_file = open(r'C:\Users\name\directory\new_file.txt', 'w')

#verify the file was created
print new_file

#write to newly created file
new_file.write('text to go in the new file\n')

#close file
new_file.close()

#remove file
os.remove('/Users/name/Desktop/directory/new_file.txt')
```

**Execute shell commands in Python**
```python
import subprocess

#list files
subprocess.check_output('ls', shell=True)

#Windows: subprocess.check_output('dir', shell=True)
```

