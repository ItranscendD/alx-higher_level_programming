#include "100-operations.h"

/**
 * add - Adds two integers
 * @a: first integer
 * @b: second integer
 * Return: sum of a and b
 */
int add(int a, int b)
{
    return (a + b);
}

/**
 * sub - Subtracts two integers
 * @a: first integer
 * @b: second integer
 * Return: difference of a and b
 */
int sub(int a, int b)
{
    return (a - b);
}

/**
 * mul - Multiplies two integers
 * @a: first integer
 * @b: second integer
 * Return: product of a and b
 */
int mul(int a, int b)
{
    return (a * b);
}

/**
 * div - Divides two integers
 * @a: first integer (dividend)
 * @b: second integer (divisor)
 * Return: result of division of a by b
 */
int div(int a, int b)
{
    return (a / b);
}

/**
 * mod - Calculates the modulo of two integers
 * @a: first integer (dividend)
 * @b: second integer (divisor)
 * Return: remainder of the division of a by b
 */
int mod(int a, int b)
{
    return (a % b);
}

/**
 * init_ops - Initializes the ops_t structure
 * Return: ops_t structure with function pointers
 */
ops_t *init_ops(void)
{
    ops_t *operations = malloc(sizeof(ops_t));

    if (operations == NULL)
        return (NULL);

    operations->add = add;
    operations->sub = sub;
    operations->mul = mul;
    operations->div = div;
    operations->mod = mod;

    return (operations);
}
