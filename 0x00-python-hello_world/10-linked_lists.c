#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all the elements of a listint_t list
 * @h: pointer to the starting node
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	unsigned long int num_of_nodes = 0;

	while (h)
	{
		num_of_nodes++;
		printf("%d\n", h->n);
		h = h->next;
	}
	return (num_of_nodes);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to the list
 * Return: Nothing
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head)
	{
		current = head;
		head = head->next;
		free(current);
	}
}

/**
 * add_nodeint - adds a node at the beginning of a listint_t list
 * @head: Double pointer to the headnode of the list
 * @n: value to be inputed into new node created
 * Return: pointer to the new node created
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}
