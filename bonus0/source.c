#include <string.h>
#include <unistd.h>
#include <stdio.h>

char *p(char *dest, char *s) {
  char buf[4104];

  puts(s);
  read(0, buf, 0x1000);
  *strchr(buf, '\n') = 0;
  return strncpy(dest, buf, 0x14);
}

char *pp(char *dest) {
  char src[20];
  char v3[28];

  p(src, " - ");
  p(v3, " - ");
  strcpy(dest, src);
  return strcat(dest, v3);
}

int main(void) {
  char s[42];

  pp(s);
  puts(s);
  return 0;
}
