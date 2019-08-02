print("Welcome to the special recruitment program, please answer the following questions: ")

CV = {}

Name = input("name:")
CV.update({'Name': Name })


age = input("Age:")
CV.update({'Age' : age})

experience =input("how many years of experience do you have?: ")
CV.update({'experience':experience})
#print(CV)


skills = ["pyhton", "c++" ,"javascript","juggling", "running","eating"]
print("Skills: ")
for i in skills:
 index = skills.index(i) +1
 print(str(index)+"- "+i)

CV.update({'Skills':[]})
#print(CV)
choice1 =int(input("choose a skill from above: "))
choice2 =int(input("choose another skill from above: "))

choice1 = skills[choice1-1]
choice2 = skills[choice2-1]
 
CV.update({'Skills': [choice1,choice2]})
if 25<int(age) and int(age)<40 and int(experience)>3 and "pyhton" in CV['Skills']:
   print("you have been accepted, ",CV['Name'])
else:
   print("Sorry, You are not accepted, ",CV['Name'] )


