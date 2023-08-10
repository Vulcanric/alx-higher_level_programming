#include "lists.h"

/**
 * check_cycle - function checks if a listint_t linked list has a cycle in it
 * @list: The node of the list to start checking from
 *
 * Return: 1 if it does, otherwise 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *listnode, *node;
	int occur = 0; /*
			* number of occurence of equality
			* between node & listnode
			*/

	if (list == NULL)
		return (0); /* false */

	node = list;
	while (node)
	{
		listnode = node;
		occur = 0;

		if (node->next == NULL)
			return (0); /* false */

		while (listnode != NULL)
		{
			if (node == listnode)
				occur++;
			if (node == listnode && occur >= 2)
				return (1); /* true */

			listnode = listnode->next;
		}
		node = node->next;
	}
	return (0); /* false */
}
