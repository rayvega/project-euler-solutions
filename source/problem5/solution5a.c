/*
project euler problem # 5
https://projecteuler.net/index.php?section=problems&id=5

description:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

algorithm:
start with 1 and increment by 1 until reach n where n is the solution number. For each number, divide by each value between 1 and 20 checking if all have remainder of zero.  Repeat this until find a number where this is true and then stop.

*/

#include <stdio.h>

int get_smallest_number(int max_num){
  printf("start with max_num == %i ... ", max_num);
  int smallest_number = 1; // 12252240  // cheat using 19 as seed
  int is_evenly_divisible = 1;
  while(1){
    //printf("%i\n", smallest_number);
    int i;
    for (i = 1; i <= max_num; i++){
      if (smallest_number % i != 0){
	is_evenly_divisible = 0;
	break;
      }
      is_evenly_divisible = 1;
    }
  
  if (is_evenly_divisible){
    return smallest_number;
  }
  smallest_number += 1;
  }
}

main(){
  //printf ("test example => %i\n", get_smallest_number(10) );  //expected value = 2520
      printf ("solution 5 => %i\n", get_smallest_number(20) ); 
}
