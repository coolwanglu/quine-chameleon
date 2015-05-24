import json,sys;S="DATA";L=S.split('\t');I=L.index(sys.argv[1]);print(L[I+1]+json.dumps(S)[1:-1]+L[I+2],end='')
