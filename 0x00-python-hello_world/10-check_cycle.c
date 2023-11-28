#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - will check if linkedlist has a cycle
 * @list: singlylinked list
 * Return: for no cycle, 0 otherwise -1
 */
int check_cycle(lintint_t *list)
{
	listint_t *slow, *fast;

	if (list == Null || list->next)
		return (0)

	slow = list->next;
	fast = list->next;

	while (slow && fast && fast->next)
	{
		if (slow && fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0)
}
