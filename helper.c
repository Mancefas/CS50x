#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to green color

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            if (pixel.rgbtRed == 0x00 && pixel.rgbtGreen == 0x00 && pixel.rgbtBlue == 0x00)
            {
                pixel.rgbtGreen = 0xff;
                image[i][j] = pixel;
            }
        }
    }
}