#include <stdio.h>
#include <string.h>
{{{chameleon:#include <stdlib.h>
#include <time.h>
}}}#define F for(;*s++;)
#define p printf
#define P(s) p("%s",s)
int main(){{{{chameleon:srand(time(0));}}}char*S="DATA",*s=S,*e,I={{{chameleon:rand()%LANGCOUNT*FIELDCOUNT}}}{{{ouroboros:LANGINDEXxFIELDCOUNT}}};for(;I--;)for(;*s++;);P(s);for(;*S||*(S+1);++S){for(e="\\\\n\n\"\"0\0";*e&&*(e+1)!=*S;e+=2);*e?p("\\%c",*e):p("%c",*S);}for(P("\\0");*s++;);P(s);return 0;}
