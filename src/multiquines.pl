my $S=q:b"DATA";my @L=$S.split("\t");my $I=@L.grep-index(@*ARGS[0]);$S~~s:g/\\/\\\\/;$S~~s:g/"\t"/\\t/;$S~~s:g/\n/\\n/;$S~~s:g/\"/\\\"/;print @L[$I[0]+1]~$S~@L[$I[0]+2]
