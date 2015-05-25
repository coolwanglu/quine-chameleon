#load "str.cma"
open Random
let s="DATA";;{{{chameleon:self_init()}}}
let l=Array.of_list(Str.split(Str.regexp"\t")s) and i={{{chameleon:FIELDCOUNT*int LANGCOUNT}}}{{{ouroboros:ENTRYINDEX}}};;print_string(l.(i)^(String.escaped s)^l.(i+1))
