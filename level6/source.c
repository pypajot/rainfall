#include <stdlib.h>

void n(void)
{
  system("/bin/cat /home/user/level7/.pass");
  return;
}

void m(void *param_1,int param_2,char *param_3,int param_4,int param_5)
{
  puts("Nope");
  return;
}

void main(int ac,char **av)
{
  char *__dest;
  code **func;
  
  __dest = (char *)malloc(0x40);
  func = (code **)malloc(4);
  *func = m;
  strcpy(__dest,av[1]);
  (**func)();
  return;
}
