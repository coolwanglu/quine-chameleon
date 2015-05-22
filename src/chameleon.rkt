#lang racket
(let*((S"DATA")(L(list-tail(string-split S"\t"){{{chameleon:(*(random LANGCOUNT)FIELDCOUNT)}}}{{{ouroboros:ENTRYINDEX}}})))(display(string-append(car L)(string-replace(string-replace(string-replace(string-replace S"\\""\\\\")"\t""\\t")"\n""\\n")"\"""\\\"")(cadr L))))
