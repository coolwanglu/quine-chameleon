P=process;S="DATA";L=S.split '\0';I=L.indexOf P.argv[2];P.stdout.write L[I+1]+S.replace(/\\/g,'\\\\').replace(/\0/g,'\\0').replace(/\n/g,'\\n').replace(/"/g,'\\"')+L[I+2]
