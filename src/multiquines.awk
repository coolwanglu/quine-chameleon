BEGIN{S="DATA";split(S,L,"\t");for(I in L)if(L[I]==ARGV[1]){gsub(/\\/,"\\\\",S);gsub(/\t/,"\\t",S);gsub(/\n/,"\\n",S);gsub(/\"/,"\\\"",S);printf("%s",L[I+1] S L[I+2])}}
