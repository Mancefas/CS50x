#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string s = get_string("Text: ");
    int letters = count_letters(s);
    int words = count_words(s);
    int sentences = count_sentences(s);
    float avg_letters = ((float) letters / words) * 100;
    float avg_sentences = ((float) sentences / words) * 100;
    int grade_index = round(0.0588 * avg_letters - 0.296 * avg_sentences - 15.8);

    if (grade_index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade_index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade_index);
    }
}

int count_letters(string text)
{
    int letters = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        };
    }

    return letters;
}

int count_words(string text)
{
    int words = 1;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == 32)
        {
            words++;
        };
    }
    return words;
}

int count_sentences(string text)
{
    int sentences = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            sentences++;
        };
    }
    return sentences;
}