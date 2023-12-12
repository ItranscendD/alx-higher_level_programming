#include "main.h"

/**
 * _strcat - Concatenates two strings
 * @dest: The destination string
 * @src: The source string
 *
 * Return: The pointer to the destination string
 */
char *_strcat(char *dest, char *src) {
    char *concat = dest;

    while (*dest)
        dest++;

    while ((*dest++ = *src++))
        ;

    return concat;
}
