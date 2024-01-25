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
  char *dest = malloc(0x40);
  void **fn_ptr = malloc(4);

  *fn_ptr = m;
  strcpy(dest, av[1]);
  (**fn_ptr)();
  return;
}
