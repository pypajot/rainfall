#include <stdio.h>

void o(void)
{
  system("/bin/sh");
  exit(1);
}

void n(void)
{
  char buffer[520];
  
  fgets(buffer,0x200,(FILE *)stdin);
  printf(buffer);
  exit(1);
}

void main(void)
{
  n();
  return;
}