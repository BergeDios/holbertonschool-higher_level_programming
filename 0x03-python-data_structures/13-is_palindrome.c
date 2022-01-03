#include "lists.h"
#include <stdio.h>

/**
 * add_nodeint - add a node at the beggining
 * @head: pointer to head node of the list
 * @n: const int for n data in node
 * Return: address of the new element or NULL
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;

	return (*head);
}
/**
 * is_palindrome - checks if a linked list is a palindrome or not
 * @head: head to linked list
 * Return: 1 is palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed, *tmp;
	int count = 0, i = 0;

	reversed = malloc(sizeof(listint_t));
	if (!reversed)
		return (-1);
	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	tmp = *head;
	while (tmp != NULL)
	{
		add_nodeint(&reversed, tmp->n);
		tmp = tmp->next;
		count++;
	}
	while (i < count)
	{
		if ((*head)->n == reversed->n)
			i++;
		else
			return (0);
	}
	return (1);
}
