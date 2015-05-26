S<-"DATA";L<-strsplit(S,"\t")[[1]];I<-{{{chameleon:1+sample(0:LANGCOUNT-1,1)[[1]]*FIELDCOUNT}}}{{{ouroboros:ENTRYINDEX+1}}};S<-deparse(S);cat(L[[I]]);cat(substr(S,2,nchar(S)-1));cat(L[[I+1]])
