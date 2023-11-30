#ifndef LIST_H
#define LIST_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct list_s - singly linked list
 * @n: integer data
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct list_s
{
    int n;
    struct list_s *next;
} list_t;

size_t print_list(const list_t *h);
list_t *add_node(list_t **head, const int n);
void free_list(list_t *head);
list_t *add_node_end(list_t **head, const int n);
void print_before_main(void) __attribute__((constructor));

#endif /* LIST_H */
