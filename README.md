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
df
```

