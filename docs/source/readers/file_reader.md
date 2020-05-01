### Plain text files
For instance, consider this plain text file.
```
Hola, esta
es una cadena
de texto
```
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
