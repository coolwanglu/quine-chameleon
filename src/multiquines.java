import java.util.*;public class qc{public static void main(String[]A){String S="DATA";List L=Arrays.asList(S.split("\0"));int I=L.indexOf(A[0]);System.out.print(L.get(I+1)+S.replace("\\","\\\\").replace("\0","\\0").replace("\n","\\n").replace("\"","\\\"")+L.get(I+2));}}
