# readers
[![Build Status](https://travis-ci.org/apastors/readers.png?branch=master)](https://travis-ci.org/apastors/readers)
[![codecov](https://codecov.io/gh/apastors/readers/branch/master/graph/badge.svg)](https://codecov.io/gh/apastors/readers)

Easy reading.

`readers` offers an easy way to read different kinds of files.

### Plain text files
For instance, consider this plain text file.
```
Hola, esta
es una cadena
de texto ```
It can be read directly as a `str`:
```python
text = FileReader(textfile).read()
```
or it can be iterated over as well, iterating line by line
```python
with FileReader(textfile) as file_reader:
    for line in file_reader:
        print(line)
```

Consider now the `JSONReader`, and two kinds of situations:

### JSON files
For example, consider this file
```json
{
    "key1": "value1",
    "key2": 2
}
```
In this case, the `read` method of the `JSONReader` can be used, returning a `dict` :
```python
json_record = JSONReader(textfile).read()
print(json_record.keys())

dict_keys(['key1', 'key2'])
```

We can also have these kinds of files:
```json
{"key1": "value1","key2": 1}
{"key1": "value2","key2": 2}
{"key1": "value3","key2": 3}
{"key1": "value4","key2": 4}
{"key1": "value5","key2": 5}
```
In this case, we can iterate over the file, returning a `dict` per line.
```python
with JSONReader(filename_iterable) as json_reader:
    for json_record in json_reader:
        print(json_record["key1"])
 
value1
value2
value3
value4
value5
```

For JSON files, `Filter`s can be added too:

```python
from readers.filters import Filter

f = Filter(op1='.key2', operator='ge', op2=3)

with JSONReader(filename_iterable) as json_reader:
    for json_record in json_reader:
        if f(json_record):
            print(json_record["key1"])
 
value3
value4
value5

Note: Filters provide a functionality that should be separate from filters, i.e, stored as a different library.
```
