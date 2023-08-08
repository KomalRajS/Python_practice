age = int(input("Enter your age : "))

if age<18:
    print("Sorry, you're ineligible to vote")
else:
    name = input("Enter your name : ")
    if name=="":
        print("Oops! You didn't enter your name")
    elif name ==" ":
        print("Oops! You didn't enter a valid name")
    else:
        print(f"Hello {name}, you're voting for the class leader election!")
        vote = (input("R - Rohan\nP - Prerana\nEnter your vote :"))
        print("Thank you for voting")
        if vote=="R" or vote=="P":
            isVoted = True
        else:
            isVoted = False
        
        if isVoted:
            print(f"{name} voted {vote}")
        else:
            print(f"{name} entered invalid vote")

