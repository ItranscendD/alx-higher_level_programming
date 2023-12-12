#include "main.h"

/**
 * _strcpy - Copies a string (including the null byte) to another string
 * @dest: The destination string
 * @src: The source string
 *
 * Return: The pointer to the destination string
 */
char *_strcpy(char *dest, char *src) {
    char *cpy = dest;

    while ((*dest++ = *src++))
        ;

    return cpy;
}
