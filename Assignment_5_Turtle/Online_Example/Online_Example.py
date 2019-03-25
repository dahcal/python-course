from turtle import*
#n,k=eval(input())
n,k=[1,10]
a=clone()
exec('a.circle(99,360*n/k);circle(99,360/k);clone().goto(a.pos());'*k)