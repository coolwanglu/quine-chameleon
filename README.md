# Quine Chameleon

A polymorphic program that transforms itself into different languages.

### Why

I'd like to learn new programming languages and I'm bored with Hello World's.

### Languages

<!--LANGUAGES-BEGIN-->
\# | Language | Size | Suffix
--- | --- | --- | ---
1 | Ruby | 3641 | rb
2 | Python | 3661 | py
3 | Perl | 3669 | pl
4 | AWK | 3686 | awk
5 | CoffeeScript | 3692 | coffee
6 | JavaScript | 3694 | js
7 | Emacs Lisp | 3723 | el
8 | Scala | 3732 | scala
9 | Lua | 3761 | lua
10 | C# | 3771 | cs
11 | Java | 3800 | java
12 | Vala | 3831 | vala
13 | C++ | 3848 | cpp
14 | C | 3885 | c
<!--LANGUAGES-END-->

### How to Play

*Dancing Chameleon*

`make dance` - Press `ctrl-c` to stop 

*Crawling Chameleon*

`make crawl`

### Dependencies
 
Python3 is required. While you need the other compilers/interpreters to run various output.  

Here's a quick install-all command for Ubuntu 15.04:

`sudo apt-get install gawk coffeescript emacs24-nox g++ gcc lua5.2 mono-mcs nodejs openjdk-7-jdk perl6 python3 ruby scala valac`

Note: Scala 2.9.2 does not work with Java 8

### Variants 

- `make ouroboros`: languages are went through in alphabetical order
- `make random-ouroboros`: languages are went through in a random order
- `make multiquines`: [Multiquines](http://en.wikipedia.org/wiki/Quine_%28computing%29#Multiquines). The target language is specified through command-line. (See rules below)

### My Testing Environment

Ubuntu 15.04 with the following compilers/interpreters

- CoffeeScript 1.4.0
- GNU Awk 4.1.1
- GNU Emacs 24.4.1
- GCC 4.9.2
- Lua 5.2.3
- Mono 3.2.8
- Node.js 0.10.25
- OpenJDK 7
- Python 3.4.3
- Rakudo 2014.07
- Ruby 2.1.2
- Scala 2.9.2
- Vala 0.26.2

### Rules (beta)

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
  - No definition as compiler flags
    * `-D` for gcc, g++, valac
  - stdin is not closed
    * Use `BEGIN` instead of `END` in AWK
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
