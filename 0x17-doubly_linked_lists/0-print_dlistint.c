#include <stdio.h>
#include "dlistint.h"

/**
 * print_dlistint - Prints all elements of a dlistint_t list
 * @h: Pointer to the head of the list
 *
 * Return: The number of nodes in the list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;
	dlistint_node_t *current = h->head;

	if (current == NULL)
	{
		printf("List is empty\n");
		return (0);
	}

	while (current != NULL)
	{
		printf("%d ", current->data);
		current = current->next;
		count++;
	}

	printf("\n");
	return (count);
}
