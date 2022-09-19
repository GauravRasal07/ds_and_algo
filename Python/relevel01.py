#Problem 2:
'''
Bootcamp
Problem Statement

You are given N students and an array of size N. The knowledge of the i-th student is a[i]. You are also given an integer X. You want to create some boot camps to teach them about coding. Since you want to make the maximum profit, you have to create the maximum number of boot camps possible. To create a bootcamp the product of the number of students in the bootcamp and the student with the least knowledge should be greater than twice of X. Also a student can be a member of only one bootcamp and a few students might not be a part of any bootcamp.
Count the maximum number of boot camps possible.

Constraints

All the input values are integers
1<=t<=100
1<=N<=10^5
1<=X<=10^9
1<=a[i]<=10^8
Input :

The first contains the integer t the number of test cases.
The first line of each test case contains N and X where N is the number of students and X is an integer
The second line of each test case contains the N elements of the array

Output :

Print the maximum number of boot camps you can make.

Sample Input :

2

10 6

7 1 8 2 7 6 4 1 9 1

4 7

9 7 4 7

Sample Output :

2

1

Sample Explanation :

In the first test case you can make first boot camp with 1st student and 3rd student and the second boot camp with the 5th and 9th student

In the second test case you can make a bootcamp with all the four students'''


def solution1(n, x, arr):
    res = 0
    boot_camps = []

    for i in arr:
        if i >= 0:
            pass



#Problem 1:
'''
Which Classroom
Problem Statement

Many students have joined the Berland University this year and it’s not possible to accommodate all these students in a single classroom.
So the school decided to put these students in N classrooms. To do this the school principal first arranged all the students in a line and put A1 students in the first classroom, A2 students in the second classroom, and so on.
Now to easily locate the students in the school he wants to develop an optimized algorithm to answer which classroom the ith student belongs to.
For the task, they have hired the best coder of all times(you). You have developed the algorithm and for testing your algorithm the school principal will ask Q queries from you.
In each query, he will give you an integer i, and you have to answer in which classroom the ith student belongs to.

Input Format

First line contains a single integer denoting N.
Next line contains N space separated integers denoting the elements of array A.
Next line contains a single integer denoting Q.
Next line contains Q space separated integers denoting the value of i in each query.
Output Format

For each query, print in which classroom the ith student belongs to in a separate line.
Constraints

1<=N<=105
1<=Ai<=104
1<=Q<=105
1<=i<=A1+A2+...AN
Sample Input 1

3

2 1 7

5

1 10 3 2 5

Sample Output 1

1

3

2

1

3

Explanation of Sample 1

The students belong to the classroom as 1, 1, 2, 3, 3, 3, 3, 3, 3, 3.

Here we can see that the 1st student belongs to the 1st classroom, 10th student belongs to the 3rd classroom, 3rd student to 2nd classroom, 2nd student to 1st classroom, 5th student to 3rd classroom.''' 



print(solution1(10, 6, [7, 1, 8, 2, 7, 6, 4, 1, 9, 1]))



a = 3
b = [2, 1, 7]
c = 5
d = [1, 10, 3, 2, 5]

def solution2():
    s = sum(b)

