import java.io.*;
import java.util.*;
public class palindrome
{
public static void main(String args[])
{
System.out.println("enter the value");
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
while(n>0)
{
num=num%10;
r=r*10+num;
n=n/10;
}
if(num==r)
{
System.out.println("palindrome");
}
else
{
System.out.println("not a palindrome");
}
}
}

