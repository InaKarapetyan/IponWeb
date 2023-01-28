#Task 1 
#Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։ Տրված n֊ի
#համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։
def prog(num1,num2, n):
    add = num2 - num1
    find = num1 + (n-1)* add
    return find

num1 = 1
num2 = 5
print(prog(1,5,4))

#Task2 
#CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների
#չեկը և ստացված շարանը տվեց Ratiorg֊ին՝ պարզելու գնված ապրանքների
#ընդհանուր թիվը: Քանի որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է այն
#ավտոմատացնել, ուստի նրան անհրաժեշտ է ծրագիր, որը կամփոփի բոլոր թվերը,
#որոնք հայտնվում են տվյալ մուտքագրում:
#Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում
#հայտնված թվերի գումարը։
def sum_up(string):
    sum = 0
    x = " "
    for num in string:
        if num.isdigit():
            x+= num
        else:
            sum += int(x)
            x = '0'
    return ("The sum is", sum + int(x))    

print(sum_up("2 apples, 12 oranges"))
print(sum_up("5 apples, 155 oranges"))

#Task3 
#Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են
#ոչ աճող կամ չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարակ
#դեպքում:
def sorted(a,b,c):
    if a<b and a<c and b<c:
        print("Sorted")
    elif a>b and b>c and a>c:
        print("Sorted")
    else:
        print("Unsorted")

sorted(1,2,3)
sorted(1,3,2)
sorted(5,0,-4)

#Task4 
#Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն կատարյալ թիվ է, թե ոչ։
def kataryal(n):
    sum = 0
    for i in range(1, n):
        if n%i == 0:
            sum = sum + i
            #print(i, end = " , ")
    #print(sum)
    if sum == n:
        print("True")
    else:
        print('False')         
 
kataryal(6)
kataryal(12)


#Task5 
#Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա էլեմենտների գումարը։
def sum_of(list):
    sum = 0
    for num in range(0, len(list)):
        sum+= list[num]
    print(sum)

sum_of([1,2,3,4])


# Task 6 
#Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ ցուցակի ամենամեծ էլեմենտը։
list = [1,2,3,100]

largest = list[3] #just to ckeck, it could be also list[2] or list[3], any list[n]
for i in list:
    if i > largest:
        largest = i
print(largest)

#Task 7 
#Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր էլեմենտները։
list = [1,2,3,4,3,2,1,3]
final = []
def remove_duplicate(list):
    for i in list:
        if i not in final:
            final.append(i)
    print(final)

remove_duplicate(list)

#Task8 
#Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր էլեմենտների արտադրյալը։
def multiple(list):
    mult = 1
    for i in list:
        mult = mult* i 
    return mult 

list = [1,2,3,4]
print(multiple(list))

#Task 9 
#Գրեք ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի բազմապատիկ է։
input = str(input("Enter your line:"))
if len(input)%4 == 0:
    input = input[::-1]
    print(input)

#Task10
#Գրեք ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ անդամը։ Խնդիրը լուծել և ռեկուրսիվ, և իտերատիվ մեթոդներով։

#recursive
def fibonacci(n):

    if n ==0:
        return 0 
    elif n<0:
        raise ValueError
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

print(fibonacci(10))


#iterative
#____________________________________________________________________________________________________

def fibonacci(n):
    prev, end = 0,1 
    if n ==0:
        return 0
    elif n ==1 or n==2:
        return end
    else:
        for num in range(2,n+1):
            output = prev + end
            prev = end
            end = output
        print(output)

fibonacci(10)

# Task 11 
#Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց ամենափոքր ընդհանուր բազմապատիկը։
def lcm(n, m):
    reminder = n%m
    if reminder == 0:
        return int(n)
    return int(n) *int(lcm(m,reminder)/reminder)
print((lcm(3,5)))

#Task 12 
#Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:
#Օրինակ 119-ի համար հաջորդ պալինդրոմը 121 է
def palindrome(n):
    return str(n) == str(n)[::-1]
n = 119 #input the number you want 
while not palindrome(n):
       n = int(n)+1
print(n)



palindrome(n)

#Task 13 
#Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա և ներկայումս գտնվում է կետում (X0,
#Y0): Կոորդինատները ամբողջ թիվ են։ Այն ստանում է N հեռակառավարման
#հրամաններ: Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման
#ստանալուց հետո ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե
#ռոբոտը սխալ հրաման է ստանում, նա պարզապես անտեսում է այն: Որտե՞ղ է
#գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:
#Ուշադրություն: աջը՝ x0+1, ձախը՝ x0-1, վերևը՝ y0+1, ներքևը՝ y0-1։
def robotik(command):
    start_X = 0
    start_Y=0

    for step in range(len(command)):
        if command[step] == 'u':
            start_Y+=1
        elif command[step]== "d":
            start_Y-=1
        elif command[step] == 'r':
            start_X+=1
        else:
            start_X-=1
    return (start_X, start_Y)
print(robotik("ulrdd"))

#Task14
#Ստուգեք, արդյոք 2 ցուցակները 1-քայլ ցիկլիկ են:

def one_cyclic(list1,list2):
    for index1 in range(len(list1)):
        for index2 in range(len(list2)):
            if list1[index1]==list2[index2+1] or list2[index2]==list1[index1+1]:
                return True
            else:
                return False

list1= [1,2,3,4,5,6]
list2=[6,1,2,3,4,5]
list3=[6,5,1,2,3]
list4=[2,3,4,5,6,1]
print(one_cyclic(list1,list2))
print(one_cyclic(list1,list3))
print(one_cyclic(list1,list4))

#Task15
#Գրել ծրագիր, որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:

def deleteDigit(n): 
        result = 0 # to compare then
        i = 1
       
        while n // i > 0:
            temp = (n//(i * 10))*i + (n % i)#deletes the smallest digit
            i *= 10
            if temp > result:
                result = temp   
        return result
   
  
n1 = 152
n2 = 1001
print(deleteDigit(n1))
print(deleteDigit(n2))

#Task 16 
#Գրեք ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple բաղկացած միայն առաջին tuple֊ի թվերից։

def check(given_tuple):
    tuple=()
    for item in given_tuple:
        if type(item) == int:
            tuple = tuple+(item,)
    return tuple

print(check((False, 3, 2 , 6.7 , "L")))

#Task17 
#Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում է ստացած արժեքը tuple մեջ։
def add(t):
    #final=()
    element = input("Enter the item to add: ")
    t = t + tuple(element)
    return t

t = (1,2,3,4)
print(add(tuple(t)))

#Task 18
#Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuplex֊ի էլեմենտները ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։
tuple = (1,2,3,4)
print('-'.join(str(t) for t in tuple))

#Task 19 
#Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց len() ֆունկցիա֊ի օգտագորձմամբ։
def length(list):
    len = 0
    for i in list:
        len+=1
    return len

print(length([1,2,3,4,5,7]))

#Task20
#Ticket numbers usually consist of an even number of digits. A ticket number is considered
#lucky if the sum of the first half of the digits is equal to the sum of the second half.
#Given a ticket number n, determine if it&#39;s lucky or not. Not using: string, list, tuple, set types.
#I wrote this very long since it was hard to write short and detailed
def lucky(n):
    count=0
    while(n>0):
        count=count+1
        n=n//10
    return count
#counts the digits of the given number

n=1230
print(lucky(n))
i=len(str(n))
if lucky(n)%2==0: #checks the number to be even
    str1 = str(n)[0:i//2]
    str2 = str(n)[i//2:]
    print("First is:" , str1)
    print("Last is:" , str2)

#sum of the first half
def sum1(str1):
    sum_1 = 0
    for x in str1:
        if x.isdigit() == True:
            y = int(x)
            sum_1 += y

    return sum_1
print(sum1(str1))

#sum of the second half
def sum2(str2):
    sum_2 = 0
    for m in str2:
        if m.isdigit() == True:
            n = int(m)
            sum_2 += n

    return sum_2    
print(sum2(str2))

#checks the luckiness
if sum1(str1) == sum2(str2): 
    print("The number is lucky")
else:
    print("The number is unlucky")

#Task 21
#Euler function
#Euler function is return a count of numbers not great than N, which are mutualy simple with N.
#Example φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6. Write a function
#which return count of numbers mutually simple with given N.

#I will use this later on the second function
def GCD(a, b):
	lower = min(a, b)
	upper = max(a, b)
	if lower == 0:
		return upper
	elif lower == 1:
		return 1
	else:
		return GCD(lower, upper%lower)

def Euler(N):
    count=0
    for n in range(1,N):
        if GCD(N, n)==1:
            count+=1
    return count
print(Euler(6))

#Task 23
#You are given an array of strings names, and an array heights that consists of distinct
#positive integers. Both arrays are of length n. For each index i, names[i] and heights[i]
#denote the name and height of the ith person. Return names sorted in descending
#order by the people's heights.
new_arr=[]
my_dict={}


def sort(names,heights):
    n=len(names)
    for person in range(n):
        if names[person] in my_dict:
            my_dict[heights[person]]=names[person]
        else:
            my_dict[heights[person]]=names[person]
    for name in sorted(my_dict.keys()):
            new_arr.append(my_dict[name])
    print(new_arr[::-1])
names = ["Mary", "John", "Emma"]
heights = [180,165,170]
sort(names,heights)