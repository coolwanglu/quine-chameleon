#include <stdio.h>
#include <string.h>
#define F while(*s++)
#define p printf
#define P(s) p("%s",s)
int main(int C,char**A){char*S="DATA",*s=S,*e;for(;strcmp(s,A[1]);)F;F;P(s);for(;*S||*(S+1);++S){for(e="\\\\n\n\"\"0\0";*e&&*(e+1)!=*S;e+=2);*e?p("\\%c",*e):p("%c",*S);}P("\\0");F;P(s);return 0;}
