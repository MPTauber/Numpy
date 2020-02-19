'''
new_list= []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i)) '''  ## this is the "old" way to do it

### List comprehension ("new") way:
# new_list = [expression(i) for i in old_list if filter(i)]
comp_list = [x for x in range(1,11)]
print(comp_list)

squares = [i**2 for i in range(1,11)]  ##### prints the squares of the integers for the exisiting integers in the range (1,11)
print(squares)

list1 = [3,4,5]

multiplied = [i*3 for i in list1] ##multiplies every item in list1 by 3
print(multiplied)

words = ["this", "is", "a", "list" , "of", "words"]
new_words = [i[0] for i in words]
print(new_words)

item = [x.upper() for x in ["1","b","c"]]
print(item)

new_range = [i*i for i in range(5) if i%2 == 0] ## i%2 == 0 meant that it only show numbers that have a remainder of 0 if they are
## divided by 2. This means they are even. So this statement gives the even multiplied numbers of the numbers in range(5)
print(new_range)

string = "Hello 12345 World"
string_new = [i for i in string if i.isdigit()] ## only grabs the numbers
print(string_new)
string_new = [i for i in string if i.isalpha()] ## only grabs letters
print(string_new)
string_new = [i for i in string if not i.isdigit()] ## this works too for letters, BUT also grabs spaces
print(string_new)

infile = open("test.txt", 'r')
result = [i.rstrip('\n') for i in infile if "line 3" in i]  ### this goes to the text file and grabs the whole line that includes "line 3"
print(result)

def double(x):  ## defines new function
    return x*2

print(double(10))  # function works (result is 20)

newlist = [double(x) for x in range(10)]
print(newlist)

newlist = [x+y for x in [10,20,30] for y in [20,40,60]]
print(newlist)