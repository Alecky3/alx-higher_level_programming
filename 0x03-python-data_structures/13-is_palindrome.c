#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palidrome.
 * @@head: the head of the list
 * Return: 0 if it is not a palidrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *tail;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		temp = temp->next;
	}

	tail = temp;
	temp = *head;

	while (temp)
	{
		if (temp->n != tail->n)
			return (0);
		temp = temp->next;
	}

	return (1);
}
