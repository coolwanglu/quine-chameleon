import std.algorithm,std.stdio,std.string;void main(string[]A){auto S="DATA",L=find(S.split("\t"),A[1]);write(L[1]~translate(S,['\t':r"\t",'\n':r"\n",'"':"\\\"",'\\':r"\\"])~L[2]);}
