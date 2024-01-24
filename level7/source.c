#include <stdio.h>
#include <time.h>

char *c;

void m(void *param_1,int param_2,char *param_3,int param_4,int param_5)
{
  time_t tVar1;
  
  tVar1 = time((time_t *)0x0);
  printf("%s - %d\n",c,tVar1);
  return;
}

int main(int ac, char **av)
{
  int *array_1;
  void *element;
  int *array_2;
  FILE *__stream;
  
  array_1 = (int *)malloc(8);
  *array_1 = 1;
  element = malloc(8);
  array_1[1] = element;
  array_2 = (int *)malloc(8);
  *array_2 = 2;
  element = malloc(8);
  array_2[1] = element;
  strcpy((char *)array_1[1],av[1]);
  strcpy((char *)array_2[1],av[2]);
  __stream = fopen("/home/user/level8/.pass","r");
  fgets(c,0x44,__stream);
  puts("~~");
  return 0;
}