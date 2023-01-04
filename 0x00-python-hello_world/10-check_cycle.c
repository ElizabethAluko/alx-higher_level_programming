#include "lists.h"

/**
 * check_cycle - check for a cycle in a linkedlist.
 * @list: linked list.
 * Return: 1 if it has a cycle, and 0 if not.
 */
int check_cycle(listint_t *list)
{
	listint_t *i = list, *n = list;

	if (!list)
		return (0);
	while (i && n && n->next)
	{
		i = i->next;
		n = n->next->next;

		if (i == n)
			return (1);
	}
	return (0);
}


