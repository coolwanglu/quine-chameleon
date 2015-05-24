package main;import(."fmt";."os";."strconv";."strings");func main(){S:="DATA";L:=Split(S,"\t");for I,s:=range L{if s==Args[1]{S=Quote(S);Print(L[I+1]+S[1:len(S)-1]+L[I+2]);}}}
