(setq S"DATA")(setq L(nthcdr{{{chameleon:(*(random LANGCOUNT)FIELDCOUNT)}}}{{{ouroboros: LANGINDEXxFIELDCOUNT}}}(split-string S"\0")))(princ(car L))(dolist(c(split-string S""))(princ(or(cdr(assoc c'(("\0"."\\0")("\n"."\\n")("\""."\\\"")("\\"."\\\\"))))c)))(princ(cadr L))
