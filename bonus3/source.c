#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, const char **argv) {
  char ptr[132];
  FILE *v5;

  v5 = fopen("/home/user/end/.pass", "r");
  memset(ptr, 0, sizeof(ptr));
  if ( !v5 || argc != 2 )
    return -1;
  fread(ptr, 1, 0x42, v5);
  ptr[65] = 0;
  ptr[atoi(argv[1])] = 0;
  fread(&ptr[66], 1, 0x41, v5);
  fclose(v5);
  if ( !strcmp(ptr, argv[1]) )
    execl("/bin/sh", "sh", 0);
  else
    puts(&ptr[66]);
  return 0;
}