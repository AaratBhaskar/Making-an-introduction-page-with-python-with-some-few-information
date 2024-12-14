name=input("Enter your Name:")
age=int(input("Enter your Age:"))
marks=int(input("Please Enter Your Correct Percentage:"))
hobby=input("Tell your any 5 hobby:")
pro=input("Any skills(That you are in professional)")
stage=input("Enter your stage (Marks that you gain mostly in your carreer): ")
print(f"""Hello, My name is {name}!
I’m a dedicated and driven individual,constantly working on self-improvement and expanding my knowledge. Currently in {stage}, I enjoy exploring topics like {hobby}. I focus on achieving clarity and accuracy in everything I do, whether it’s studying, exercising, or enhancing my skills. My unique style reflects my personality—sharp, confident, and always aiming higher.""")
if(marks<90 and marks<80):
    print("My position is topper in my class")
elif(marks<80 and marks<70):
    print("I position good in marks in my carreer")
elif(marks<60 and marks<70):
    print("My Position in my class is an average student") 
else:
    print("Not much good in studies but talented")      

