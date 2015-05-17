import sys;S="DATA";L=S.split('\0');I=L.index(sys.argv[1]);print(L[I+1]+S.translate({0:'\\0',10:'\\n',34:'\\"',92:'\\\\'})+L[I+2],end='')
