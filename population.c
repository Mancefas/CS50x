#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int startingPopulation;
    do
    {
        startingPopulation = get_int("How many llamas starting with? ");
    }
    while (startingPopulation < 9);

    // TODO: Prompt for end size
    int wantedPopulation;
    do
    {
        wantedPopulation = get_int("How many llamas looking for at the end? ");
    }
    while (wantedPopulation < startingPopulation);

    // TODO: Calculate number of years until we reach threshold
    int yearsNeeded = 0;
    while (startingPopulation < wantedPopulation)
    {
        startingPopulation = startingPopulation + (startingPopulation / 3) - (startingPopulation / 4);
        yearsNeeded++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", yearsNeeded);
}