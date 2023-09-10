#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for user input with how height it need to be
    int n;
    do
    {
        n = get_int("Positive number for height: ");
    }
    while (n < 1 || n > 8);

    // Building pyramids
    for (int i = 0; i < n; i++)
    {
        for (int k = n; k > i + 1; k--)
        {
            printf(" ");
        }

        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}