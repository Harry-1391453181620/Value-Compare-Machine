def compare_values():
    x = []
    while True:
        user_input = input('Please input a number, stop to end.  ')
        if user_input.lower() == 'stop':
            break
        if user_input.isdigit():
            try:
                x.append(int(user_input))
            except ValueError:
                print('Invalid input'.upper())
        else:
            str_length = len(user_input)
            x.append(str_length)

    F = None
    while F != 0:
        F = 0
        C = 0
        while C < len(x) - 1:
            if x[C] < x[C + 1]:
                T = x[C]
                x[C] = x[C + 1]
                x[C + 1] = T
                F = 1
            C = C + 1
    choice = str(input('Do you want the output to have [] or not?\n'
                       'Use "no" to get rid of the [], "yes" to remain the [].  ')).lower()
    if choice == 'no':
        for i in range(len(x)):
            if i != len(x) - 1:
                print(x[i], end=' ')
            else:
                print(x[i])
    elif choice == 'yes':
        print(x)
    else:
        print("Invalid Choice.")
        print(x)
if __name__ == "__main__":
    compare_values()