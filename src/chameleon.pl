my $S=q:b"DATA";my @L=$S.split("\t");my $I={{{chameleon:LANGCOUNT.rand.Int*FIELDCOUNT}}}{{{ouroboros:ENTRYINDEX}}};print @L[$I]~$S.trans(["\t","\n",'"',"\\"]=>['\t','\n','\\"',"\\\\"])~@L[$I+1];
