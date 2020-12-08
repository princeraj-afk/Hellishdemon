'''The School №0 of the capital of Berland has n children studying in it. All the children in this school are gifted:
some of them are good at programming, some are good at maths, others are good at PE (Physical Education). Hence, for
each child we know value t i:

t i = 1, if the i-th child is good at programming,
t i = 2, if the i-th child is good at maths,
t i = 3, if the i-th child is good at PE
Each child happens to be good at exactly one of these three subjects.

The Team Scientific Decathlon Olympias requires teams of three students. The school teachers decided that the teams will
 be composed of three children that are good at different subjects. That is, each team must have one mathematician, one
  programmer and one sportsman. Of course, each child can be a member of no more than one team.

What is the maximum number of teams that the school will be able to present at the Olympiad? How should the teams be
 formed for that?

Input
The first line contains integer n (1 ≤ n ≤ 5000) — the number of children in the school. The second line contains n integers t 1, t 2, ..., t n (1 ≤ t i ≤ 3), where t i describes the skill of the i-th child.

Output
In the first line output integer w — the largest possible number of teams.

Then print w lines, containing three numbers in each line. Each triple represents the indexes of the children forming the team. You can print both the teams, and the numbers in the triplets in any order. The children are numbered from 1 to n in the order of their appearance in the input. Each child must participate in no more than one team. If there are several solutions, print any of them.

If no teams can be compiled, print the only line with value w equal to 0.'''
a = int(input())
b = list(int(x) for x in input().split())
n1 = b.count(1)
n2 = b.count(2)
n3 = b.count(3)
print(min(n1,n2,n3))
for i in range(min(n1,n2,n3)):
    print(b.index(1)+3*i+1,end= " ")
    print(b.index(2)+3*i+1,end= " ")
    print(b.index(3)+3*i+1,end= "\n")
    b.remove(1)
    b.remove(2)
    b.remove(3)