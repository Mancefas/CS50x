#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{

    // Ensure proper usage
    // TODO #1
    if (argc < 3)
    {
        printf("Should be 2 arguments: input file and output file\n");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE *provided_file = fopen(argv[1], "r");
    if (provided_file == NULL)
    {
        printf("Input file did not open correctly\n");
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, provided_file);

    // Use check_format to ensure WAV format
    // TODO #4
    if (check_format(header) == 0)
    {
        printf("File is not correct format\n");
        return 1;
    }

    // Open output file for writing
    // TODO #5
    FILE *output_file = fopen(argv[2], "w");

    if (output_file == NULL)
    {
        printf("Output file did not open correctly\n");
        return 1;
    }

    // Write header to file
    // TODO #6
    fwrite(&header, sizeof(WAVHEADER), 1, output_file);

    // Use get_block_size to calculate size of block
    // TODO #7
    int block_size = get_block_size(header);

    // Write reversed audio to file
    // TODO #8

    // temporary place block
    BYTE temp_block[block_size];

    // moving the pointer in file to the end
    fseek(provided_file, 0, SEEK_END);

    long audio_size_no_header = ftell(provided_file) - sizeof(WAVHEADER);
    // need int, because the block should be whole number (can't be part of block)
    int audio_blocks_count = (int) audio_size_no_header / block_size;
    // add 1 if after dividing there is some numbers after coma
    if (audio_size_no_header % block_size != 0)
    {
        audio_blocks_count++;
    }

    // writing block from provided file to output file, since the pointer in provided file is reversed with it should write reversed
    for (int i = audio_blocks_count - 1; i >= 0; i--)
    {
        fseek(provided_file, sizeof(WAVHEADER) + i * block_size, SEEK_SET);
        fread(temp_block, block_size, 1, provided_file);
        fwrite(temp_block, block_size, 1, output_file);
    }

    // closing the opened files
    fclose(provided_file);
    fclose(output_file);
}

int check_format(WAVHEADER header)
{
    // TODO #4
    if (strncmp((char *) header.format, "WAVE", 4) == 0)
    {
        return 1;
    }
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return header.numChannels * header.bitsPerSample / 8;
}