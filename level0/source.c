#define _GNU_SOURCE

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int main(int ac, char **av)
{
  int nbr_arg = atoi(av[1]);
  if (nbr_arg == 423) {
    int command = strdup("/bin/sh");
    int group_id = getegid();
    int user_id = geteuid();
    setresgid(group_id,group_id,group_id);
    setresuid(user_id,user_id,user_id);
    execv("/bin/sh",&command);
  }
  else {
    fwrite("No !\n",1,5,(FILE *)stderr);
  }
  return 0;
}