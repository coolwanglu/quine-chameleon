S<-"DATA";L<-strsplit(S,"\t")[[1]];I<-match(commandArgs(1)[[1]],L);S<-deparse(S);cat(L[[I+1]]);cat(substr(S,2,nchar(S)-1));cat(L[[I+2]]);
