#include <iostream>
#include <cstring>
#define P std::cout<<
#define F for(;*l++;);P l
int main(int,char**A){const char*S="DATA",*e;char*L=strcpy((char*)malloc(LENGTH+1),S),*l=L;for(;*L;++L)if(*L==9){*L=0;if(strcmp(l,A[1]))l=L+1;}F;for(;*S;++S){for(e="t\tn\n\"\"\\\\";*e&&*(e+1)!=*S;e+=2);*e?(P'\\'<<*e):(P*S);}F;}
