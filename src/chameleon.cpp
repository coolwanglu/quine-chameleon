#include <iostream>
#include <cstring>
{{{chameleon:#include <random>
}}}#define P std::cout<<
int main(){const char*S="DATA",*e;char*L=strcpy((char*)malloc(LENGTH+1),S),*l=L,I={{{chameleon:std::random_device()()%LANGCOUNT*FIELDCOUNT}}}{{{ouroboros:ENTRYINDEX}}};for(;*L;++L)if(*L==9){*L=0;if(!--I)l=L+1;}P l;for(;*S;++S){for(e="t\tn\n\"\"\\\\";*e&&*(e+1)!=*S;e+=2);*e?(P'\\'<<*e):(P*S);}for(;*l++;);P l;}
