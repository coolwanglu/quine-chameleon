#import <stdio.h>
#import <string.h>
#import <stdlib.h>
#define P printf
#define F for(;*l++;);P("%s",l)
int main(int C,char**A){char*S="DATA",*L=strcpy(malloc(LENGTH+1),S),*l=L,*e;for(;*L;++L)if(*L==9){*L=0;if(strcmp(l,A[1]))l=L+1;}F;for(;*S;++S){for(e="t\tn\n\"\"\\\\";*e&&*(e+1)!=*S;e+=2);*e?P("\\%c",*e):P("%c",*S);}F;return 0;}
