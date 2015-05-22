#lang racket
(let*((S"DATA")(L(member(vector-ref(current-command-line-arguments)0)(string-split S"\t"))))(display(string-append(cadr L)(string-replace(string-replace(string-replace(string-replace S"\\""\\\\")"\t""\\t")"\n""\\n")"\"""\\\"")(caddr L))))
