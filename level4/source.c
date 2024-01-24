#include <stdio.h>

int m;

void p(char *param_1)
{
  printf(param_1);
  return;
}

void n(void)
{
  char buffer [520];
  
  fgets(buffer,0x200,(FILE *)stdin);
  p(buffer);
  if (m == 0x1025544) {
    system("/bin/cat /home/user/level5/.pass");
  }
  return;
}

void main(void)
{
  n();
  return;
}