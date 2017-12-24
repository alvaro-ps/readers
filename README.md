# readers

Easy reading.

`readers` offers an easy way to read different kinds of files.

### Plain text files
For instance, consider this plain text file.
```
Hola, esta
es una cadena
de texto
```
It can be read directly as a `str`:
```python
with FileReader(textfile) as filetext:
    print(filetext)
```
or it can be iterated over as well, iterating line by line
```python
with FileReader(textfile, iterable=True) as file_reader:
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
In this case, the `JSONReader` returns a `dict` :
```python
with JSONReader(textfile) as json_record:
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
with JSONReader(filename_iterable, iterable=True) as json_reader:
    ...:     for json_record in json_reader:
    ...:         print(json_record["key1"])
    ...:         
    ...:     
value1
value2
value3
value4
value5
        
```
