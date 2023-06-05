#include "lists.h"
/**
 * check_cycle - a function that checks for the cycle in the linked list
 *
 * @list: input list
 * Return: 1 if there is a cycle , 0 (success)
*/
int check_cycle(listint_t *list)
{
	listint_t *clean = list;
	listint_t *infected = list;

	if (list == 0)
		return (0);

	while (clean && infected && clean->next)
	{
		infected = infected->next;
		clean = clean->next->next;
		if (infected == clean)
			return (1);
	}
	return (0);
}
