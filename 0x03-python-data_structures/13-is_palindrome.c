#include "lists.h"
/**
 * is_palindrome - Entry point
 * @head: Head
 * Return: Return 0 on success
 */

int is_palindrome(listint_t **head)
{
	int len = count_list(*head);
	int *array_int = malloc(len * sizeof(int));
	int i = 0;
	listint_t *h = *head;
	listint_t *k = *head;
	bool test = true;
	int j = len - 1;

	if (array_int == NULL)
	{
		return (-1);
	}

	while (h != NULL)
	{
		array_int[i] = h->n;
		i++;
		h = h->next;
	}

	while (j >= 0)
	{
		if (array_int[j] != k->n)
		{
			test = false;
		}
		k = k->next;
		j--;
	}
	free(array_int);
	if (test)
	{
		return (1);
	}
	else
	{
		return (0);
	}

}

/**
 * count_list - A function that counts the number of item in a list
 * @head: The head list
 * Return: Return the number of item in a list
 */
int count_list(listint_t *head)
{
	int i = 0;
	listint_t *t = head;

	while (t != NULL)
	{
		i++;
		t = t->next;
	}
	return (i);
}

