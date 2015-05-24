S<-"DATA";L<-strsplit(S,"\t")[[1]];I<-match(commandArgs(1)[[1]],L);cat(L[[I+1]]);cat(gsub("\n","\\\\n",gsub("\t","\\\\t",gsub("([\\\"\\\\])","\\\\\\1",S))));cat(L[[I+2]]);
