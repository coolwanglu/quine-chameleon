# Quine Chameleon

<img src="http://fc06.deviantart.net/fs70/f/2012/250/6/3/chameleon_by_kukon-d5dunm8.jpg" width="300"></img>

A polymorphic program that transforms itself into different languages.

### Why

I'd like to learn new programming languages and I'm bored with Hello World's.

### Languages

<!--LANGUAGES-BEGIN-->
\# | Language | Size | Suffix
--- | --- | --- | ---
1 | Ruby | 5246 | rb
2 | Octave | 5271 | octave
3 | CoffeeScript | 5280 | coffee
4 | JavaScript | 5287 | js
5 | Python | 5288 | py
6 | Vala | 5290 | vala
7 | R | 5303 | R
8 | Perl | 5310 | pl
9 | AWK | 5322 | awk
10 | Clojure | 5322 | clj
11 | Go | 5334 | go
12 | OCaml | 5338 | ml
13 | F# | 5347 | fs
14 | D | 5352 | d
15 | Haxe | 5352 | hx
16 | Racket | 5363 | rkt
17 | Emacs Lisp | 5376 | el
18 | Scala | 5378 | scala
19 | C# | 5404 | cs
20 | Lua | 5406 | lua
21 | Haskell | 5420 | hs
22 | Java | 5453 | java
23 | C++ | 5501 | cpp
24 | Objective C | 5513 | m
25 | C | 5516 | c
<!--LANGUAGES-END-->

### How to Play

*Dancing Chameleon*

`make dance` - Press `ctrl-c` to stop 

*Crawling Chameleon*

`make crawl` - Each step it outputs itself in a random language

### Dependencies
 
Python3 is required. You will also need other compilers/interpreters to run various output.  

Here's a quick install-all command for Ubuntu 15.04:

`sudo apt-get install clojure1.6 coffeescript emacs24-nox fsharp g++ gawk gcc gdc ghc gobjc golang-go haxe libghc-random-dev libghc-regex-compat-dev lua5.2 mono-mcs nodejs ocaml octave openjdk-7-jdk perl6 python3 r-base racket ruby scala valac`

Note: Scala 2.9.2 does not work with Java 8

### Variants 

- `make ouroboros`: languages are went through in alphabetical order
- `make random-ouroboros`: languages are went through in a random order
- `make multiquines`: [Multiquines](http://en.wikipedia.org/wiki/Quine_%28computing%29#Multiquines). The target language is specified through command-line. E.g. `python3 multiquines.py cpp` (See rules below)

### My Testing Environment

Ubuntu 15.04 with the following compilers/interpreters

- CoffeeScript 1.4.0
- fsharp 3.1.1.26
- GCC 4.9.2
- GHC 7.6.3
- GNU Awk 4.1.1
- GNU Emacs 24.4.1
- GNU Octave 3.8.2
- Go 1.3.3
- Haxe 3.0.0
- Lua 5.2.3
- Mono 3.2.8
- Node.js 0.10.25
- OCaml 4.01.0
- OpenJDK 7
- Python 3.4.3
- R 3.1.2
- Racket 6.1
- Rakudo 2014.07
- Ruby 2.1.2
- Scala 2.9.2
- Vala 0.26.2

### Rules (beta)

- Source
  - No undefined behaviors
  - No compiler/interpreter warnings
  - As short as possible
  - The main class/module name must be `QC`, if required
- Behavior 
  - Random sequence should not remain the same
    * Set random seed when necessary
  - Use only standard libraries
  - No file operations
    * `#!/bin/cat` - Bash
  - No source inspections
    * `.toSource()` - JavaScript
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
- `S`: compact data string

### License

The MIT License (MIT)

Copyright (c) 2015 Lu Wang <coolwanglu@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

The chameleon image is by [kukon@deviantART](http://kukon.deviantart.com/art/Chameleon-325596176), which is distributed under [CC BY-NC-ND 3.0](http://creativecommons.org/licenses/by-nc-nd/3.0/).

### See Also

This project is inspired by:
- [mame/quine-relay](https://github.com/mame/quine-relay)
- [rvantonder/pentaquine](https://github.com/rvantonder/pentaquine)
