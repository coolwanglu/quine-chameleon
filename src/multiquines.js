P=process;S="DATA";L=S.split('\t');I=L.indexOf(P.argv[2]);P.stdout.write(L[I+1]+JSON.stringify(S).slice(1,-1)+L[I+2])
