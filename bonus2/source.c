
#include <stdint.h>
#include <string.h>
#include <unsitd.h>

typedef __int128 int128_t;

int language = 0;
char str[19] = {
  0xC3, 0x76, 0x79, 0x48, 0x20, 0xA4, 0xC3, 0xA4, 0x69,
  0xA4, 0xC4, 0X70, 0xC3, 0xA4, 0xC3, 0x76, 0x20, 0xA4, 0x0
};
int greetuser(char *src) {
  char[19] dest;
  switch (language) {
  case 1:
    strcpy(dest, str);
    break;
  case 2:
    strcpy(dest, "Goedemiddag! ");
    break;
  case 0:
    strcpy(dest, "Hello ");
    break;
  }
  strcat(dest, src);
  return puts(dest);
}

int main(int argc, const char **argv) {
  char v4[76];
  char dest[76];
  char *v6;
  if (argc != 3)
    return 1;
  memset(dest, 0, sizeof(dest));
  strncpy(dest, argv[1], 0x28);
  strncpy(&dest[40], argv[2], 0x20);
  v6 = getenv("LANG");
  if (v6) {
    if (!memcmp(v6, "fi", 2))
      language = 1;
    else if (!memcmp(v6, "nl", 2))
      language = 2;
  }
  memcpy(v4, dest, sizeof(v4));
  return greetuser(v4);
}
