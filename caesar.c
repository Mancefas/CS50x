#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string text);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // Take argument from command line, and check if that numbers is only a number and only one argument is provided
    if (argc > 2 || argc == 1 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        // Got command line argument is a string, so convert it to number
        int shifting_key = atoi(argv[1]);

        // If got argument is OK - ask user for text
        string user_text = get_string("plaintext: ");

        for (int i = 0, n = strlen(user_text); i < n; i++)
        {
            user_text[i] = rotate(user_text[i], shifting_key);
        }

        // return new caesar text
        printf("ciphertext: %s\n", user_text);
        return 0;
    }
}

bool only_digits(string text)
{
    bool is_a_number = false;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isdigit(text[i]) == 0)
        {
            return false;
        }
        else
        {
            is_a_number = true;
        }
    }
    return is_a_number;
}

// Make logic to shift every letter by provided number form command line argument
char rotate(char c, int n)
{
    if (isalpha(c))
    {
        int lower_or_upper_letter = isupper(c) ? 65 : 97;

        char different_c_value = c - lower_or_upper_letter;
        char shifted_c = (different_c_value + n) % 26;
        char new_c = shifted_c + lower_or_upper_letter;
        return new_c;
    }
    else
    {
        return c;
    }
}