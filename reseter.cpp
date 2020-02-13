#include <stdio.h>
#include <cstdlib>
#include <cstring>
int main() 
{ 
   if (remove(strcat(std::getenv("APPDATA"),"\\Aroid\\save")) == 0) 
      printf("RESETED");
   else printf("FAILED..");
   return 0; 
} 
