"""
## Example of Local scope
def inc(x):
    #global result
    result = x + 1
    return result
 
result = inc(5)
print(result)

"""

## Example of Global scope
def disp():
   print(x)
 
x = "Hello World"
disp()  

"""

## Example of Global scope in function
def enemy_generation(enemy_num):
    for x in range(1,enemy_num):
            enemy = Enemy()
            enemy_group.add(enemy)
            all_characters.add(enemy) 

enemy_num = 4
enemy_generation(enemy_num)

"""