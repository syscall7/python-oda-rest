# python-oda-rest

python-oda-rest is a library for scripting [ODA](https://onlinedisassembler.com) projects.

The library provides read and write access to the internal data structures of the project database. Some day we hope to wrap this library with an IDAPython-compatible library called ODAPython.

## example use:

### example: list function names

In this example, we list the effective addresses and names of functions:

```
from oda_rest.api import OdaProject

project = OdaProject("http://onlinedisassembler.com", 'mkdir', clone=True)

for f in project.Functions():
    print('%x: %s' % (f['offset'], f['name']))
```

Note that in the example above, we clone an existing project instead of using one that we already created through the website.


