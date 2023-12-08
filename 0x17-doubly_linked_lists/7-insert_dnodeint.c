#include "lists.h"

/**
 * insert_dnodeint_at_index - Inserts a new node at a given position
 * @h: Pointer to a pointer to the head of the list
 * @idx: Index where the new node should be added (starting from 0)
 * @n: Value to be assigned to the new node
 *
 * Return: Address of the new node, or NULL if it failed
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	if (h == NULL)
		return (NULL);

	if (idx == 0)
		return (insert_at_beginning(h, n));

	if (*h == NULL && idx != 0)
		return (NULL);

	return (insert_at_index(h, idx, n));
}

/**
 * insert_at_beginning - Inserts a new node at the beginning of the list
 * @h: Pointer to a pointer to the head of the list
 * @n: Value to be assigned to the new node
 *
 * Return: Address of the new node, or NULL if it failed
 */
dlistint_t *insert_at_beginning(dlistint_t **h, int n)
{
	dlistint_t *new_node = malloc(sizeof(dlistint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->prev = NULL;
	new_node->next = *h;

	if (*h != NULL)
		(*h)->prev = new_node;

	*h = new_node;

	return (new_node);
}

/**
 * insert_at_index - Inserts a new node at a specific index in the list
 * @h: Pointer to a pointer to the head of the list
 * @idx: Index where the new node should be added
 * @n: Value to be assigned to the new node
 *
 * Return: Address of the new node, or NULL if it failed
 */
dlistint_t *insert_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *new_node = malloc(sizeof(dlistint_t));
	dlistint_t *temp = *h;
	unsigned int i = 0;

	if (new_node == NULL)
		return (NULL);

	new_node->n = n;

	while (temp != NULL && i < idx - 1)
	{
		temp = temp->next;
		i++;
	}

	if (temp == NULL)
	{
		free(new_node);
		return (NULL);
	}

	new_node->prev = temp;
	new_node->next = temp->next;

	if (temp->next != NULL)
		temp->next->prev = new_node;

	temp->next = new_node;

	return (new_node);
}
