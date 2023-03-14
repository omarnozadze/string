user_text= input("What is the quote? ")

mylist = ["These aren't the droids","Keep awayo from people who try to belittle your ambitions","There is only one plot-things are not they seem.","life is never fair, and perhaps it is a good thing for most of us that it is not"]
mylist2=["Obi-Wan Kenobi","Mark Twain","Jim Thompson","Oscar Wilde"]
if user_text==mylist2[0]:
    print(mylist[0])
elif user_text==mylist2[1]:
     print(mylist[1])
elif user_text==mylist2[2]:
     print(mylist[2])
elif user_text==mylist2[3]:
     print(mylist[3])   
else:
    print("Try Again")