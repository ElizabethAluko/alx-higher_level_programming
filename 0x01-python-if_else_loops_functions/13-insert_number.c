#include "lists.h"
#include <stdlib.h>

/**
 * *insert_node - pointer of the new node.
 * @head: pointer to the list of the pointer.
 * @number: data to add to the list.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;

	if (ptr->n >= number || ptr == NULL)
	{
		new->next = ptr;
		*head = new;
		return (new);
	}
	while (ptr && ptr->next && ptr->next->n < number)
		ptr = ptr->next;
	new->next = ptr->next;
	ptr->next = new;

	return (new);
}
		
