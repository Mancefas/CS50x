#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string("What is your name? ");
    printf("hello %s\n", s);
}