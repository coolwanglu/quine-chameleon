#include <stdio.h>
#include <string.h>
#include <stdlib.h>
{{{chameleon:#include <time.h>
}}}#define P printf
int main(){{{{chameleon:srand(time(0));}}}char*S="DATA",*L=strcpy(malloc(LENGTH+1),S),*l=L,*e,I={{{chameleon:rand()%LANGCOUNT*FIELDCOUNT}}}{{{ouroboros:ENTRYINDEX}}};for(;*L;++L)if(*L==9){*L=0;if(!--I)l=L+1;}P("%s",l);for(;*S;++S){for(e="t\tn\n\"\"\\\\";*e&&*(e+1)!=*S;e+=2);*e?P("\\%c",*e):P("%c",*S);}for(;*l++;);P("%s",l);return 0;}
