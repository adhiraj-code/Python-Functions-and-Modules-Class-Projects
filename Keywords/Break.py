word = input("Enter the name of coding institute : ")

word = word.lower()

for i in word:
    if(i == 'g'):
        print("You are a Codingal student")
        break
    else:
        print("You are not a Codingal student")