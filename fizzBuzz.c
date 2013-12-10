#include <stdio.h>
#include <stdlib.h>

int fizzBuzz(int begin, int end) {
  if(begin <= end) {
    if(!(begin % 3))
      printf("Fizz");
    if(!(begin % 5))
      printf("Buzz");
    if(begin % 3 && begin % 5)
      printf("%d", begin);
    printf("\n");
    fizzBuzz(++begin, end);
  }
}

main(int argc, char *argv[]) {

	int begin = atoi(argv[1]);
	int end = atoi(argv[2]);
	
	fizzBuzz(begin, end);
}
