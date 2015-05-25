#load "str.cma"
let s="DATA"
let l=Array.of_list(Str.split(Str.regexp"\t")s);;Array.iteri(fun i j->if j=Sys.argv.(1)then print_string(l.(i+1)^(String.escaped s)^l.(i+2)))l
