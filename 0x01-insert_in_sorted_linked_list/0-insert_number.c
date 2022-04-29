#include "lists.h"
/**
 * insert_node - insert elements on a listint_t list
 * @head: pointer to head of list
 * @number: value
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *current;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	if (!head || !(*head))
	{
		node->next = NULL, *head = node;
	}
	else if (number < (*head)->n)
	{
		node->next = *head, *head = node;
	}
	else
	{
		current = *head;
		while (current->next && current->next->n < number)
			current = current->next;

		if (!current->next)
		{
			node->next = NULL, current->next = node;
		}
		else
		{
			node->next = current->next;
			current->next = node;
		}
	}
	return (node);
}