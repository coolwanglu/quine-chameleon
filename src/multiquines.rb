S="DATA";L=S.split("\t");I=L.index(ARGV[0]);print L[I+1]+S.gsub(/[\t\n"\\]/,"\t"=>'\t',"\n"=>'\n','"'=>'\"','\\'=>'\\\\')+L[I+2]
