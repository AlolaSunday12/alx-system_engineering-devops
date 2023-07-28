#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
* infinite_while - function that created 5 child processes.
* Return: 0
*/
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}

/**
* main - main function
* Return: - 0
*/
int main(void)
{
int i;
pid_t pid;

for (i = 0; i < 5; i++)
{
pid = fork();

if (pid > 0)
{
printf("Zombie process created, PID: %d\n", pid);
}
else if (pid == 0)
{
exit(0);
}
else
{
perror("Fork error");
exit(1);
}
}

infinite_while();
return (0);
}
