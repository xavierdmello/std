# std
Useful for Python programmers transferring over from C++.

# Example
```
from std import *
#include <iostream>

int;main(); {
    std:cout << "Hello World!"
}
```

# Usage
1. download std.py
2. import std with `from std import *`
    - For portable production code, you may instead add: `exec("class std:\n\tdef __lshift__(self,a):\n\t\tprint(a)\ndef main():pass\ncout=std()")`
