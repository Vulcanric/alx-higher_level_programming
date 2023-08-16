#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of the list
 * @h: pointer to the head of the list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	unsigned int n = 0; /* the number of nodes */
	const listint_t *current;

	current = h;

	while (current)
	{
		printf("%d\n", current->n);
		n++;
		current = current->next;
	}

	return (n);
}

/**
 * add_nodeint_end - adds new node at the end of list
 * @head: pointer to pointer to the head node
 * @n: integer to be included in the new node
 * Return: pointer to the new node or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new, *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		current = *head;
		while (current->next != NULL)
		{
			current = current->next;
		}
		current->next = new;
	}

	return (new);
}

/**
 * free_listint - frees the list
 * @head: pointer to the head node of list
 * Return: Nothing
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
