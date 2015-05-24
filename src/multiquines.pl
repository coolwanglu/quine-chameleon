my $S=q:b"DATA";my @L=$S.split("\t");my $I=@L.grep-index(@*ARGS[0]);print @L[$I[0]+1]~$S.trans(["\t","\n",'"',"\\"]=>['\t','\n','\\"',"\\\\"])~@L[$I[0]+2]
