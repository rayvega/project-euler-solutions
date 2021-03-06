/*
project euler problem 1
https://projecteuler.net/index.php?section=problems&id=1

description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

alogrithm:
check each value between 1 and 1000 that are divisible by 3 or 5 and add to new list. Then sum all values in that list.

*/

main()
{
  int sum_of_multiples = 0;
  int i;
  for(i = 1; i < 1000; i++)
    {
      if (i % 3 == 0 || i % 5 == 0){
          sum_of_multiples += i;         
      }
    }
  printf ("%i \n", sum_of_multiples);
}
