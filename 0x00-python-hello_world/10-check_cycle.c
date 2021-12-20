#include "lists.h"
/**
 * check_cycle - checks if a single linked list has a cycle in it
 * @list: linked list
 * Return: 0 if no cycle and 1 if it has one
 */
int check_cycle(listint_t *list)
{
	listint_t *ahead = list, *prev = list;

	if (!list)
		return (0);
	while (ahead->next != NULL && ahead->next->next != NULL)
	{
		ahead = ahead->next->next;
		prev = prev->next;

		if (ahead == prev)
			return (1);
	}
	return (0);
}
