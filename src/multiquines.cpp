#include <iostream>
#include <cstring>
#define F while(*s++)
#define P std::cout<<
#define Q F;P s
int main(int,char**A){const char*S="DATA",*s=S,*e;for(;strcmp(s,A[1]);)F;Q;for(;*S||*(S+1);++S){for(e="\\\\n\n\"\"0\0";*e&&*(e+1)!=*S;e+=2);*e?(P'\\'<<*e):(P*S);}P"\\0";Q;}
