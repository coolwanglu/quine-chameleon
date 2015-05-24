#lang racket
(require json)(let*((S"DATA")(L(list-tail(string-split S"\t"){{{chameleon:(*(random LANGCOUNT)FIELDCOUNT)}}}{{{ouroboros:ENTRYINDEX}}}))(S(jsexpr->string S)))(display(string-append(car L)(substring S 1(-(string-length S)1))(cadr L))))
