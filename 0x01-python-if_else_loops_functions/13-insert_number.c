#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to the head of the list
 * @number: Integer to include in the sorted list
 *
 * Return: pointer to the new node created, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new; /* new node to insert */
	listint_t *current;
	listint_t *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL) /* If failed */
		return (NULL);

	new->n = number; /* integer member */
	current = *head;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	else
	{
		if (new->n < current->n)
		{
			new->next = *head;
			*head = new;
		}
		else
		{
			while (current != NULL)
			{
				if (new->n > current->n)
				{
					prev = current;
					current = current->next;
				}
				else
					break;
			}
			prev->next = new;
			new->next = current;
		}
	}
	return (new);
}
