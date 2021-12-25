question_list = [
"How many continents are there?",
"What is the capital of India?",
"NG mei kaun se course padhaya jaata hai?",
"Kon Banega Crorepati Tv show me Kon host karta hai?",
"Bahubali festival is related to?",
"Which word completes the title of this film starring Kartik Aryan,Ananya pandey,Bhumi Pednekar's Pati patni Aur?",
"Which of these names means 'moon'?",
"Which of these countries is the largest producer of coffee?"
]
options_list = [
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"],
["Akshay Kumar","Amitabh Bachchan","Deepika padukon","Alia bhatt"],
["Islam","Hinduism","Buddhism","Jainism"],
["Saali","Bai","Woh","Saas"],
["Indra","Indu","Inu","Indira"],
["Indonesia","Colombia","China","Brazil"]
]
option50_50=[["(1) Four","(3) Seven"],
["(2) Bhopal","(4) Delhi"],
["(1) Software Engineering","(2) Counselling"],
["(2) Amitabh Bachchan","(3) Deepika Padukon"],
["(1)Islam","(4)Jainism"],
["(3)","(2)"],
["(Inu)","(2)"],
["(4)","(3)"]

]
answer_list=[ 3,4,1,2,4,3,2,4]

print("Welcome To KBC !🙏")
print("Kon Banega Crorepati 💰 ")
print("Test Start 👍 ")
i=0
c=0
s=100000
while i<len(question_list):
    print(question_list[i])
    a=0
    while a<len(options_list[i]):
        k=options_list[i][a]
        print(a+1,k)
        a+=1
    if c==0:
        life_line=input("Do you want to use life line?")
        if life_line=="yes":
          c+=1
          print(option50_50[i])
          s+=100000
    Ans=int(input("Enter your option:"))
    if answer_list[i]==Ans:
        print("Your answer is correct you won",s,"rupees 🥳")
        s+=10000
    else:
        print("Your answer is wrong")
        break
    i+=1
