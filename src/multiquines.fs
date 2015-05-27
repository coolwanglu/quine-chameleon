let S="DATA"
let L=S.Split '\t'
let I=Array.findIndex((=)(System.Environment.GetCommandLineArgs()).[1])L
printf"%s"(L.[I+1]+S.Replace("\\",@"\\").Replace("\t",@"\t").Replace("\n",@"\n").Replace("\"",@"\""")+L.[I+2])
