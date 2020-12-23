dict = {}
i = 0

while i != 1:
    try:
        number_of_priorities = int(input("Enter number of priorities: "))
    except ValueError:
        continue
    i += 1

for i in range(number_of_priorities):
    dict[i + 1] = []


def print_dict():
    for i in (dict.keys()):
        print((i, dict[i]), end = " " + "\n")

def pop_top():
    for i in (dict.keys()):
        if dict[i] == []:
            continue
        else:
            top_message = dict[i][0]
            break
    dict[i].remove(top_message)
    return top_message

def main():
    while True:
        try:
            number = int(input("Enter the priority of new message or press 0 to pop, -1 to print all: "))
        except ValueError:
            continue
        if number == 0:
            print("Top message is: " + pop_top())
            continue
        elif number == -1:
            print_dict()
            continue
        if number in dict:
            message = input("Enter message: ")
            try:
                dict[key] = list() if (number not in dict) else dict[number].append(message)
            except NameError:
                continue
        else:
            print("No priority found")

main()