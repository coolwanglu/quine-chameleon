let S="DATA"
let L=S.Split '\t'
let I={{{chameleon:System.Random().Next(LANGCOUNT)*FIELDCOUNT}}}{{{ouroboros:ENTRYINDEX}}}
printf"%s"(L.[I]+S.Replace("\\",@"\\").Replace("\t",@"\t").Replace("\n",@"\n").Replace("\"",@"\""")+L.[I+1])
