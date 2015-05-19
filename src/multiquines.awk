BEGIN{S="DATA";split(S,L,"\0");for(I in L)if(L[I]==ARGV[1]){gsub(/\\/,"\\\\",S);gsub(/\0/,"\\0",S);gsub(/\n/,"\\n",S);gsub(/\"/,"\\\"",S);printf("%s",L[I+1] S L[I+2])}}
