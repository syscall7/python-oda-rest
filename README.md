# python-oda-rest

python-oda-rest is a library for scripting [ODA](https://onlinedisassembler.com) projects.

The library provides read and write access to the internal data structures of the project database. Some day we hope to wrap this library with an IDAPython-compatible library called ODAPython.

## Example Usage

### Example: List Function Names

In this example, we list the effective addresses and names of functions:

```
from oda_rest.api import OdaProject

project = OdaProject("http://onlinedisassembler.com", 'mkdir', clone=True)

for f in project.Functions():
    print('0x%x: %s' % (f.vma, f.name))
```

Note that in the example above, we clone an existing project instead of using one that we already created through the website.

### Example: Print Disassembly Listing of .text section

The example below prints the first 10 instructions of the .text section.

```
#!/usr/bin/python3
from oda_rest.api import OdaProject

project = OdaProject("http://localhost:8000", 'mkdir', clone=True)

for s in project.Sections():
    if s.name == '.text':
        dus = project.DisplayUnits(s.vma, 10)
        for du in dus:
            print("%s:%s %s" % (du.section_name, du.vma, du.instStr))
```
