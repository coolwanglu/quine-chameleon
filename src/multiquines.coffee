P=process;S="DATA";L=S.split '\t';I=L.indexOf P.argv[2];P.stdout.write L[I+1]+S.replace(/\\/g,'\\\\').replace(/\t/g,'\\t').replace(/\n/g,'\\n').replace(/"/g,'\\"')+L[I+2]
