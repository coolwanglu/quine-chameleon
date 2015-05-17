my $S=q:b"DATA";my @L=$S.split("\0");my $I=@L.grep-index(@*ARGS[0]);$S~~s:g/\\/\\\\/;$S~~s:g/"\0"/\\0/;$S~~s:g/\n/\\n/;$S~~s:g/\"/\\\"/;print @L[$I[0]+1]~$S~@L[$I[0]+2]
