object qc{def main(A:Array[String]){var S="DATA";var L=S.split("\t");var I=L.indexOf(A(0));print(L(I+1)+S.replace("\\","\\\\").replace("\t","\\t").replace("\n","\\n").replace("\"","\\\"")+L(I+2))}}
