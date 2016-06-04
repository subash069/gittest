import math #importing a module
a=2+2
print(a)
subash=['rita', 'Gita', 'poonam']
print(subash)
print(math.floor(18.7))#using a function in a module
print(math.sqrt(81))
buky=math.sqrt
print(buky(49))

# about raw inputs
#x=raw_input("Enter name: ")# raw input treats it as string
#age=input("Enter age:")# raw input treats it as expression
#print ("Hey " + x)
#age=str(age)# changing integer to string
#print(x + " is " + `age` +" years old")
#raw_input("Press<Enter>")
#
y=18
print("subash is " + `y`)
raw_input("Press<Enter>")

#about lists and sequences
print 'creating a list'
family=['mom','dad','bro','sis','son','daughter']
print family
print family[3]
print family[-1]
# strings can be treated as list
name='Subash'
print name[0]
example=[0,1,2,3,4,5,6,7,8,9]
print example
print example[4:]
print example[:-5]
print 'extracting every other number'
print example[1:8:2]#extracting every other number
print example[10:0:-2]
print example [::-2]# extracting every element backwards
raw_input('press<Enter>')
# editing asequence
print'editing a sequence'
list1=['cat','rat','dog','cow']
list2=['pegion', 'sparrow','parrot','kuku']
print list1
print list2
newlist=list1 + list2
print newlist
print 'cow'in list1
print 'cow'in list2
print 'cow'in newlist 
#more list functions
print len(newlist)
print max(newlist)

#converting string to a list
print list('subash')

# intro to list methods
face=[21,18,30]
print face
face.append(45)
print 'appendedlist'
print face
#count method
apples=['i','love','apples','apples','apples', 'now']
print apples

print (`apples.count('apples')` +' apples')
 
# extend method
one=[1,2,3]
two=[4,5,6]
print one
print two
one.extend(two)
print one

#insert method 
say= ['hey', 'now', 'brown', 'cow']
print say.index('brown')
say.insert(2,'hoss')
print say

#pop method returns value
print say.pop(1)

#remove method
say.remove('brown')
print say
#reverse method doesnot returns a value
say.reverse()
print say

#sort function doesnot returns a value
say.sort()
print say

#touples ----just like list but you cant change a tupes

top1=(44,2,6,7,8)
print top1



# using variables inside a variable
subash='hey there %s, hows your %s'
v=('panku','hair')
print subash % v

# using find() function with astring

print subash.find('hey')
 
# join()
glue='good'
print glue.join(say)

# replace() works with strings
truth="i love young women"
print truth
truth.replace('young','adult')
print truth


# creating a dictionary
print 'Creating a dictionary'
family={'Dad':'Dinesh','Mom':'Meena', 'Bro':'Manish'}
print family
print family['Mom'] + " is mother"
print family.has_key('Bro')
print family.has_key('bro')

 
