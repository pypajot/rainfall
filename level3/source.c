#include <stdio.h>

int m;

void v(void)
{
  char buffer [520];
  
  fgets(buffer,0x200,(FILE *)stdin);
  printf(buffer);
  if (m == 0x40) {
    fwrite("Wait what?!\n",1,0xc,(FILE *)stdout);
    system("/bin/sh");
  }
  return;
}

void main(void)
{
  v();
  return;
}