object QC{def main(A:Array[String]){var S="DATA";var L=S.split("\t");var I=L.indexOf(A(0));print(L(I+1)+S.replaceAll("(\\\\|\\\")","\\\\$1").replace("\t","\\t").replace("\n","\\n")+L(I+2))}}
