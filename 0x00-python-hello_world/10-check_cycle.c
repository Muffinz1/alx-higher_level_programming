#include "list.h"
/**
 * check_cycle - a function that checks for the cycle in the linked list
 *
 * @list: input list
 * Return: 1 if there is a cycle , 0 (success)
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
