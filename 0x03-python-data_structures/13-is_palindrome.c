#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 0 if not a palindrome, 1 if a palindrome.
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL)
        return (1);

    listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;

    // Find the middle of the linked list
    while (fast && fast->next)
    {
        fast = fast->next->next;

        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    // Adjust pointers for odd length
    if (fast)
        slow = slow->next;

    // Compare the first and second halves
    while (slow && prev)
    {
        if (slow->n != prev->n)
            return (0);

        slow = slow->next;
        prev = prev->next;
    }

    return (1);
}
