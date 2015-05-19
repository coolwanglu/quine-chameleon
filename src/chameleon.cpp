#include <iostream>
#include <cstring>
{{{chameleon:#include <random>
}}}#define P std::cout<<
#define F for(;*s++;);P s
int main(){const char*S="DATA",*s=S,*e;int I={{{chameleon:std::random_device()()%LANGCOUNT*FIELDCOUNT}}}{{{ouroboros:LANGINDEXxFIELDCOUNT}}};for(;I--;)F;for(;*S||*(S+1);++S){for(e="\\\\n\n\"\"0\0";*e&&*(e+1)!=*S;e+=2);*e?(P'\\'<<*e):(P*S);}P"\\0";F;}
