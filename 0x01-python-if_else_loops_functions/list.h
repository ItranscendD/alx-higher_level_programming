#ifndef LIST_H
#define LIST_H

#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/* Provided functions */
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

/* Functions implemented today */
listint_t *insert_node(listint_t **head, int number);
listint_t *reverse_list(listint_t **head);
listint_t *find_loop(listint_t *head);

#endif /* LIST_H */
