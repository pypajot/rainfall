#define _GNU_SOURCE

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

int main(int ac, char **av)
{
  int iVar1;
  int command;
  int useless;
  int user_id;
  int group_id;
  
  iVar1 = atoi(av[1]);
  if (iVar1 == 423) {
    command = strdup("/bin/sh");
    useless = 0;
    group_id = getegid();
    user_id = geteuid();
    setresgid(group_id,group_id,group_id);
    setresuid(user_id,user_id,user_id);
    execv("/bin/sh",&command);
  }
  else {
    fwrite("No !\n",1,5,(FILE *)stderr);
  }
  return 0;
}