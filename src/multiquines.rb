S="DATA";L=S.split("\0");I=L.index(ARGV[0]);print L[I+1]+S.gsub(/[\0\n"\\]/,"\0"=>'\0',"\n"=>'\n','"'=>'\"','\\'=>'\\\\')+L[I+2]
