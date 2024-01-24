#include <stdbool.h>
#include <stdio.h>
#include <string.h>

char *auth;
char *service;

int main(void)
{
  char *input;
  char buffer [5];
  char after_buffer [2];
  char last_buffer [125];
  
  do {
    printf("%p, %p \n", auth, service);
    input = fgets((char *)buffer, 0x80, stdin);
    if (input == (char *)0x0) {
      return 0;
    }
    if (strncmp(buffer, "auth ", 5)) {
      auth = (int *)malloc(4);
      *auth = 0;
      if (strlen(after_buffer) < 0x1f) {
        strcpy((char *)auth, after_buffer);
      }
    }
    if (strncmp(buffer, "reset", 5)) {
      free(auth);
    }
    if (strncmp(buffer, "service", 6)) {
      service = strdup(last_buffer);
    }
    if (strncmp(buffer, "login", 5)) {
      if (auth[8] == 0) {
        fwrite("Password:\n", 1, 10, stdout);
      }
      else {
        system("/bin/sh");
      }
    }
  } while( true );
}
