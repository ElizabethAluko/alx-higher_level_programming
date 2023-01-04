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

	while (*ptr)
	{
		*ptr = *ptr->next;
		*new = *new->next->next
		if (*ptr->n > number)
		{
			*new = ptr->next;
			*
