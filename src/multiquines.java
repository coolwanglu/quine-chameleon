import java.util.*;public class QC{public static void main(String[]A){String S="DATA";List L=Arrays.asList(S.split("\t"));int I=L.indexOf(A[0]);System.out.print(L.get(I+1)+S.replace("\\","\\\\").replace("\t","\\t").replace("\n","\\n").replace("\"","\\\"")+L.get(I+2));}}
