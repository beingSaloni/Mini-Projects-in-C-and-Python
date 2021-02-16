#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    int number , guess ,times = 0 ;
    srand(time(0));
    number = rand() % 100 + 1 ; //Generate random no. between 1 to 100 
    // printf("The number is %d" , number);
     printf("Guess the no. between 1 to 100 \n");
    do {
       
        scanf("%d" , &guess);
        times ++ ;

        if (guess > number ){
            printf("Lower the number please !\n") ;
        }
        else if (guess  < number ){
            printf(" Higher the number please ! \n");
            }
        else {
            printf ( " You are correct . You guess in %d chances" , times );
        }
    }while(guess != number);
    return 0;
}