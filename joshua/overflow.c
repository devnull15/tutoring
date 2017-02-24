#include <stdio.h>
#include <string.h>

#define BUF_LEN 42

void fun(char * s){

  char *p;
  char buf[BUF_LEN];
  int i;

  for( i=0, p=s ; *p ; i++,p++ ){
    buf[i]=*p;
  }

  return;
}

int main(int argc, char *argv[]){

  if(argc < 2){
    fprintf(stderr, "ERROR: Require argument\n");
    return 1;
  }

  fun(argv[1]);

  return 0;
}
