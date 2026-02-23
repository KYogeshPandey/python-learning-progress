questions = [
    ["Which of the following is not a valid variable name in Python?", "1. my_variable", "2. 2nd_variable", "3. _variable", "4. variable_name", "4"],
    ["who is the prime minister of india?", "1. Narendra Modi", "2. Rahul Gandhi", "3. Arvind Kejriwal", "4. Manmohan Singh", "4"],
    ["who is the president of india?", "1. Ram Nath Kovind", "2. Pranab Mukherjee", "3. A.P.J Abdul Kalam", "4. Smt. Indira Gandhi", "4"],
    ["who is the founder of python?", "1. Guido van Rossum", "2. James Gosling", "3. Bjarne Stroustrup", "4. Dennis Ritchie", "4"],
    ["which of the following is not a programming language?", "1. Python", "2. Java", "3. HTML", "4. C++", "4"],
    ["which of the following is not a data type in python?", "1. int", "2. float", "3. string", "4. character", "4"],
    ["which of the following is not a loop in python?", "1. for", "2. while", "3. do-while", "4. None of the above", "4"],
    ["which of the following is not a conditional statement in python?", "1. if", "2. else", "3. elif", "4. switch", "4"],
    ["which of the following is not a built-in function in python?", "1. print()", "2. input()", "3. len()", "4. sqrt()", "4"],
    ["which of the following is not a keyword in python?", "1. if", "2. else", "3. elif", "4. function", "4"],
    ["which of the following is not a valid operator in python?", "1. +", "2. -", "3. *", "4. ^", "4"],
    ["which of the following is not a valid data structure in python?", "1. list", "2. tuple", "3. set", "4. array", "4"],
]

level=[10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]

money=0


for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\n question for rs.{level[i]} is :")
    print(f" {question[1]}  ,      {question[2]}")
    print(f" {question[3]}  ,      {question[4]}")

    answer=int(input("enter the answer(1-4):"))
    if answer==int(question[5]):
        print("congratulations! you have won Rs.",level[i])
        if(i==4):
            money=80000
        elif(i==9):
            money=2500000
        elif(i==11):
            money=10000000
        elif(i==12):
            money=7000000

    else:
        print("sorry! wrong answer")
        break

print(f"you have won Rs.{money}")

