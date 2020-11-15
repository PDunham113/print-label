# print-label

This package contains utilities to design & print labels using a variety of
different methods. Label generation, translation, and printing are separated
into discrete steps, making this package easily expandable to cover a variety
of scenarios.

Label generation is (mostly) printer-independent, although some label elements
may require certain features not available on certain printers. The following
printer dialects and print methods are supported:

Dialects:
-   JSON
-   ZPL

Print Methods:
-   File
-   Network
