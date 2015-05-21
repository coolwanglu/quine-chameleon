import sys;S="DATA";L=S.split('\t');I=L.index(sys.argv[1]);print(L[I+1]+S.translate({9:'\\t',10:'\\n',34:'\\"',92:'\\\\'})+L[I+2],end='')
