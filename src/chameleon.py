import json{{{chameleon:,random}}};S="DATA";L=S.split('\t');I={{{chameleon:random.randint(0,LANGCOUNT-1)*FIELDCOUNT}}}{{{ouroboros:ENTRYINDEX}}};print(L[I]+json.dumps(S)[1:-1]+L[I+1],end='')
