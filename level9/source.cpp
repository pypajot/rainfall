void N::N(int param) {
  *this = &operator_plus;
  *(this + 0x68)= param;
  return;
}

void N::setAnnotation(char *param) {
  size_t n = strlen(param);

  memcpy(this + 4,param,n);
  return;
}

void main(int ac,char) {
  if (ac < 2) {
    exit(1);
  }
  N* class1 = new N(5);
  N* class2 = new N(6);
  N::setAnnotation(class1,av[1]); //copy the payload into memory (overwrite class1 and class2 memory)
  //We can discard the argument passed, we dont need them
  (***class2)(class2,class1); //dereference vtables to call our shellcode
  return;
}
