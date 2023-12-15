#ifndef _100_OPERATIONS_H_
#define _100_OPERATIONS_H_

/**
 * struct ops - Structure to hold function pointers
 * @add: pointer to the addition function
 * @sub: pointer to the subtraction function
 * @mul: pointer to the multiplication function
 * @div: pointer to the division function
 * @mod: pointer to the modulo function
 */
typedef struct ops
{
    int (*add)(int a, int b);
    int (*sub)(int a, int b);
    int (*mul)(int a, int b);
    int (*div)(int a, int b);
    int (*mod)(int a, int b);
} ops_t;

#endif /* _100_OPERATIONS_H_ */
