a1=str(input())

a2=str(input())

a3=str(input())

a4=str(input())

a5=str(input())

a6=str(input())

a7=str(input())

a8=str(input())

a9=str(input())

a10=str(input())

a11=str(input())

a12=str(input())

b1=str(a1+a2+a3)

b2=str(a4+a5+a6)

b3=str(a7+a8+a9)

b4=str(a10+a11+a12)

def reverse(s):

   return s[::-1]

def isPalindrome(s):
 
    rev = reverse(s)
 
    if (s == rev):
 
        print("It is a pallindrome")

    else:
        
         print("Not a pallindrome")
        


isPalindrome(b1)

isPalindrome(b2)

isPalindrome(b3)

isPalindrome(b4)
