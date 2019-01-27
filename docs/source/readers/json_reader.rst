JSON files
==========

Consider now the class :py:class:`JsonReader <readers.file_readers.json_reader.JsonReader>`, and two kinds of situations:

One JSON per file
-----------------
For example, consider this file

.. code-block:: json

    {
        "key1": "value1",
        "key2": 2
    }

In this case, the :py:meth:`read <readers.file_readers.json_reader.JsonReader.read>` method of the :py:class:`JsonReader <readers.file_readers.json_reader.JsonReader>` can be used, returning a :class:`dict` :

.. code-block:: python

    json_record = JSONReader(textfile).read()
    print(json_record.keys())

    dict_keys(['key1', 'key2'])

One JSON per line
-----------------
We can also have these kinds of files:

.. code-block:: json

    {"key1": "value1","key2": 1}
    {"key1": "value2","key2": 2}
    {"key1": "value3","key2": 3}
    {"key1": "value4","key2": 4}
    {"key1": "value5","key2": 5}

In this case, we can iterate over the file, returning a `dict` per line.

.. code-block:: python

    with JSONReader(filename_iterable) as json_reader:
        for json_record in json_reader:
            print(json_record["key1"])
 
    value1
    value2
    value3
    value4
    value5
