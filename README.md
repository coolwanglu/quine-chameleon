# Quine Chameleon

A polymorphic program that transforms itself into different languages.

### Languages

<!--LANGUAGES-BEGIN-->
\# | Language | Size | Suffix
--- | --- | --- | ---
1 | Ruby | 2812 | rb
2 | Python | 2832 | py
3 | Perl | 2842 | pl
4 | CoffeeScript | 2864 | coffee
5 | JavaScript | 2865 | js
6 | Emacs Lisp | 2894 | el
7 | Lua | 2936 | lua
8 | C# | 2942 | cs
9 | Java | 2971 | java
10 | C++ | 2979 | cpp
11 | C | 3029 | c
<!--LANGUAGES-END-->

### How to Play

*Dancing Chameleon*

1. Install compilers/interpreters you like
2. `make dance`
  - Press `ctrl-c` to stop 

*Crawling Chameleon*

1. `make crawl`

### Dependencies
 
Python3 is required. While you need the other compilers/interpreters to run various output.  

Here's a quick install-all command for Ubuntu 15.04:

`sudo apt-get install coffeescript emacs24-nox g++ gcc lua5.2 mono-mcs nodejs openjdk-8-jdk python3 perl6 ruby`

### Variants 

- `make ouroboros`: languages are went through in alphabetical order
- `make random-ouroboros`: languages are went through in a random order
- `make multiquines`: [Multiquines](http://en.wikipedia.org/wiki/Quine_%28computing%29#Multiquines). The target language is specified through command-line. (See rules below)

### My Testing Environment

Ubuntu 15.04 with the following compilers/interpreters

- CoffeeScript 1.4.0
- GNU Emacs 24.4.1
- GCC 4.9.2
- Lua 5.2.3
- Mono 3.2.8
- Node.js 0.10.25
- OpenJDK 8
- Python 3.4.3
- Rakudo 2014.07
- Ruby 2.1.2

### Rules

- Source
  - No compiler warnings
  - As short as possible
  - The main class/module name must be `qc`, if required
- Behavior 
  - Do not crash for any commandline arguments 
  - Random sequence should not remain same
    * Set random seed when necessary
  - Use only standard libraries
  - No file operations
    * `#!/bin/cat` - Bash
  - No source inspections
    * `.toSource()` - JavaScript
  - No self interpretations/evaluation
    * `eval` - Ruby, JavaScript
    * `exec` - Python
- Language
  - Use languages available to Ubuntu 15.04 
    * Or _easily_ obtainable
  - Use latest standard if not compatible
    * Python3 vs Python2
    * Perl6 vs Perl5
- Multiquines
  - A valid language suffix must be specified as the only command-line argument
    * Otherwise the behavior is undefined

### Naming Convention

For readability, here are some common variables names used, with exceptions:

- `A`: command line arguments 
- `I`: index of specified language (in the language array)
- `L`: data array by splitting `S`
- `P`: routine to output a string
- `S`: compact data string

### License

The MIT License (MIT)

Copyright (c) 2015 Lu Wang <coolwanglu@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### See Also

This project is inspired by:
- [mame/quine-relay](https://github.com/mame/quine-relay)
- [rvantonder/pentaquine](https://github.com/rvantonder/pentaquine)
