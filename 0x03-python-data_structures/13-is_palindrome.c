#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks for a palindrome linked list
 * @head: pointer to pointer to the head node of list
 * Return: 1 if list is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	int listint_values[SIZE];
	listint_t *nodes;
	int i, j;

	nodes = *head;

	/* If list is empty or has only one node */
	if (*head == NULL || nodes->next == NULL)
		return (1); /* It is a palindrome */

	/* Copying the integers values of node into array buffer */
	i = 0;
	while (nodes != NULL)
	{
		listint_values[i++] = nodes->n;
		nodes = nodes->next;
	}

	i -= 1;
	/* Checking each index at same opposite position for equality */
	for (j = 0; i > j; i--, j++)
	{
		if (listint_values[i] != listint_values[j])
			return (0); /* Not a palindrome */
	}

	return (1); /* Is a palindrome */
}
