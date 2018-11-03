import sys
import pickle
def open_file(file_name, mode):
    try:
        the_file =open(file_name, mode, encoding='ISO-8859-1')
    except IOError as e:
        print("Unable to open the file", file_name, ". Ending program. \n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct =  next_line(the_file)
    if correct:
        correct = correct[0]
    try:
        nominal = int(next_line(the_file))
    except ValueError:
        nominal = 0
    explanation = next_line(the_file)
    return category, question, answers, correct, nominal, explanation

def welcome(title):
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

def main():
    main_file = open_file(r"C:\python\chapter7.txt", "r")
    title = next_line(main_file)
    welcome(title)
    score = 0
    count = 1
    category, question, answers, correct, nominal, explanation = next_block(main_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1,  "-", answers[i])
        answer =  input("Your answer: ")
        if answer == correct:
            print("\nRight!", end=" ")
            score += nominal
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score: ", score, "\n\n")
        category, question, answers, correct, nominal, explanation = next_block(main_file)
    main_file.close()
    print("That was the last question!")
    print("You're final score is ", score)
    name = input("Input your name: ")
    record = [name,score]
    save_record = open("records.dat", "wb")
    pickle.dump(record, save_record)
    save_record.close()
    print("List of records:")
    save_record = open("records.dat", "rb")
    while count <= 10:
        try:
            record = pickle.load(save_record)
            print(record)
            count +=1
        except EOFError:
            record = ""
        
main()
input("\n\nНажмите Enter, чтобы выйти.")
