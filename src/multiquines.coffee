P=process;S="DATA";L=S.split '\t';I=L.indexOf P.argv[2];P.stdout.write L[I+1]+JSON.stringify(S)[1..-2]+L[I+2]
