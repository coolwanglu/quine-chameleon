object qc{def main(A:Array[String]){var S="DATA";var L=S.split("\0");var I=L.indexOf(A(0));print(L(I+1)+S.replace("\\","\\\\").replace("\0","\\0").replace("\n","\\n").replace("\"","\\\"")+L(I+2))}}
