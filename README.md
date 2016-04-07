#Unix
**Saving a Remote File with a Different Name with curl -o:**
```curl -o [shortname] [url] ```

**Rename file:**
```mv old-file-name new-file-name```



#Python

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
