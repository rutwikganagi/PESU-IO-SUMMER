n=int(input("Enter a number:"));
sum=0;

while(n!=0):
    d=n%10;
    sum=sum+d;
    n=n//10;

print("Sum of digits=",sum);
