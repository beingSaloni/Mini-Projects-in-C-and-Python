#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){
    
    int number , guess ,times, ys = 0 ;
    int sc = 0 ;
    
    srand(time(0));
    
    //Generate random no. between 1 to 100 
    // printf("The number is %d" , number);
    //  printf("Guess the no. between 1 to 100 \n");
    printf("Choose your option:-\n 1. STONE \n 2. PAPER \n 0. SCISSOR \n  4. EXIT \n 5. Your score \n");
    do {
        scanf("%d" , &guess);
        number = rand() % 3 ; 
        if (guess == 5)
        {
            printf("SCORES ARE :- \n");
            printf("YOURS :- %d \n " , ys );
            printf("Computer's :- %d \n " , sc );

        }
        if (guess !=5 )
        {
            printf("Computer choosed :- %d\n" , number );
        }
        

        if (guess ==1)
        {
            if (number ==1)
            {
                printf("It's a draw\n");
            }
            if (number ==2)
            {
                printf("You lose !\n");
                sc++;
            }
            if (number ==0)
            {
                printf("You won !\n");
                ys++;
            }
        }
        if (guess ==2)
        {
            if (number ==2)
            {
                printf("It's a draw\n");
            }
            if (number ==0)
            {
                printf("You lose !\n");
                sc++;
            }
            if (number ==1)
            {
                printf("You won !\n");
                ys++;
            }
        }
        if (guess ==3)
        {
            if (number ==0)
            {
                printf("It's a draw\n");
            }
            if (number ==1)
            {
                printf("You lose !\n");
                sc++;
            }
            if (number ==2)
            {
                printf("You won !\n");
                ys++;
            }

           
        }
        

        // if (guess > number ){
        //     printf("Lower the number please !\n") ;
        // }
        // else if (guess  < number ){
        //     printf(" Higher the number please ! \n");
        //     }
        // else {
        //     printf ( " You are correct . You guess in %d chances" , times );
        // }
    }while(guess!=4);
    printf("EXITED\n");

    int exists(const char *fname)
    {
        FILE *file ;
        if ((file = fopen(fname , "r")))
        {
            fclose(file);
            return 1;
        }
        return 0 ;
        
    }
    FILE *ptr1 ;

    if (exists("High_Score.txt") == 1)
    {
        ptr1 = fopen("High_Score.txt" , "w+");
        int c ;
        fscanf(ptr1, "%d" , &c);
        int s = ys - sc ;
        
        if (c < s)
       {
           fprintf(ptr1, "%d\n" ,s );
       }
       else
       {
           fprintf(ptr1, "%d\n" ,c );
       }
        fclose(ptr1);

        
    }
    else
    {
        ptr1 = fopen("High_Score.txt" , "w");
        int s = ys - sc ;
        fprintf(ptr1, "%d\n" ,s );
    }
    printf("High score is based on  = Comp. score - yours !! \n");
    ptr1 = fopen("High_Score.txt" , "r");
        int c ;
        fscanf(ptr1, "%d" , &c);
        fclose(ptr1);
        printf("%d" , c);
    return 0;
}