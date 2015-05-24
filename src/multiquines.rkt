#lang racket
(require json)(let*((S"DATA")(L(member(vector-ref(current-command-line-arguments)0)(string-split S"\t")))(S(jsexpr->string S)))(display(string-append(cadr L)(substring S 1(-(string-length S)1))(caddr L))))
