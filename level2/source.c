#include <stdio.h>

void p(void)
{
  void *retaddr;
  char buffer[76];
  
  fflush(stdout);
  gets(buffer);
  if (((unsigned int)retaddr & 0xb0000000) == 0xb0000000) {
    printf("(%p)\n",retaddr);
    exit(1);
  }
  puts(buffer);
  strdup(buffer);
  return;
}

void main(void)
{
  p();
  return;
}