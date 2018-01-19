#!/usr/bin/python3
from oda_rest.api import OdaProject

project = OdaProject("http://localhost:8000", 'mkdir', clone=True)

for s in project.Sections():
    if s.name == '.text':
        dus = project.DisplayUnits(s.vma, 10)
        for du in dus:
            print("%s:%s %s" % (du.section_name, du.vma, du.instStr))
