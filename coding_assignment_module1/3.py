nums=input("Enter the numbers:");
lis=nums.split(' ');
search=int(input("Enter the number you want to search:"));
l=0;
u=len(lis);
flag=0;
while l<=u:
    m=(l+u)//2;
    if search==int(lis[m]):
        flag=1;
        break;
    elif search>int(lis[m]):
        l=m+1;
    else:
        u=m-1;

if flag==1:
    print("The number is present");
else:
    print("The number is not present");
