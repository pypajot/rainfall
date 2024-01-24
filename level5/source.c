#include <stdio.h>

void o(void)
{
  	x("/bin/sh");
                    // WARNING: Subroutine does not return
  _exit(1);
}

void n(void)
{
  char buffer[520];
  
  fgets(buffer,0x200,(FILE *)stdin);
  printf(buffer);
                    // WARNING: Subroutine does not return
  exit(1);
}

void main(void)
{
  n();
  return;
}