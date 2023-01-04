#include "lists.h"

/**
 * *insert_node - pointer of the new node.
 * @head: pointer to the list of the pointer.
 * @number: data to add to the list.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prt = *head, *new;

	new = malloc(sizeof(listint_t));
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		return (0);

	if (ptr->n >= number || ptr == NULL)
	{
		new = ptr->next;
		*head = new;
		return (new);
	}
	while (ptr && ptr->next && ptr->next->n < number)
		ptr = ptr->next;
	new->next = ptr->next;
	ptr->next = new;

	return (new);
}
		
