#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>
#pragma warning(disable : 4996)
#pragma warning(disable : 6031)
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
	
	char answer[2001];
	int l = strlen(s);
	if (l == 1)
	{
		return 1;
	}
	int ll = strlen(s) / 2;
	char prev[1001];
	int ret = l;
	for (int i = 1; i <= ll; i++)
	{
		strncpy(prev, s, i);
		prev[i] = '\0';
		int count = 1;
		strcpy(answer, "");
		for (int j = i; j < l; j += i)
		{
			if (strncmp(prev, s + j, i) == 0)
			{
				count++;
			}
			else
			{
				if (count > 1)
				{
					char tmp[3];
					sprintf(tmp, "%d", count);
					strcat(answer, tmp);
					strcat(answer, prev);
				}
				else
				{
					strcat(answer, prev);
				}
				count = 1;
				strncpy(prev, s+j, i);
				prev[i] = '\0';
			}
		}
		if (count > 1)
		{
			char tmp[3];
			sprintf(tmp, "%d", count);
			strcat(answer, tmp);
			strcat(answer, prev);
		}
		else
		{
			strcat(answer, prev);
		}
		strcat(answer, "\0");
		int local_ret = strlen(answer);
		if (ret > local_ret)
		{
			ret = local_ret;
		}

	}


	

	return ret;
}

int main(void) {
	/*
	const char* s = "hello world this is C";
	char *tmp = (char *)calloc(strlen(s)+1,sizeof(char));
	strcpy(tmp, s);
	char* elem = strtok(tmp, " ");
	while (elem != NULL) {
		printf("%s\n", elem);
		elem = strtok(NULL, " ");
	}
	*/

	const char* test1 = "aabbaccc";
	/*
	const char* test2 = "ababcdcdababcdcd";
	const char* test3 = "abcabcdede";
	const char* test4 = "abcabcabcabcdededededede";
	const char* test5 = "xababcdcdababcdcd";
	*/

	// 결과 확인 (기대값: 7, 9, 8, 14, 17)
	printf("Test 1: %d\n", solution(test1));
	/*
	printf("Test 2: %d\n", solution(test2));
	printf("Test 3: %d\n", solution(test3));
	printf("Test 4: %d\n", solution(test4));
	printf("Test 5: %d\n", solution(test5));
	*/

	return 0;
	
	
}