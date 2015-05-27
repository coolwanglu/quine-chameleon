class QC{static public function main(){var S="DATA",L=S.split('\t'),I=Lambda.indexOf(L,Sys.args()[0]);S=haxe.Json.stringify(S);Sys.stdout().writeString(L[I+1]+S.substring(1,S.length-1)+L[I+2]);}}
