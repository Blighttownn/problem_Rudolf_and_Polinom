maximum_number_degree = int(input())
coefficients_of_numbers = [int(input()) for i in range(maximum_number_degree + 1)]
polinom = ""
count_of_degree = 0
for number in range(len(coefficients_of_numbers)):
    if coefficients_of_numbers[number] == 0:
        count_of_degree += 1
        continue
    if maximum_number_degree - count_of_degree > 1 and maximum_number_degree - count_of_degree != maximum_number_degree:
        if coefficients_of_numbers[number] != 1 and coefficients_of_numbers[number] != -1:
            if coefficients_of_numbers[number] > 0:
                polinom += " " + "+" + " " + str(coefficients_of_numbers[number]) + " " + "*" + " " + "x" + "^" + str(
                    maximum_number_degree - count_of_degree)
            else:
                polinom += " " + "-" + " " + str(
                    abs(coefficients_of_numbers[number])) + " " + "*" + " " + "x" + "^" + str(
                    maximum_number_degree - count_of_degree)
        if coefficients_of_numbers[number] == 1:
            polinom += " " "+" + " " + "x" + "^" + str(maximum_number_degree - count_of_degree)
        if coefficients_of_numbers[number] == -1:
            polinom += " " + "-x" + "^" + str(maximum_number_degree - count_of_degree)
    #
    if maximum_number_degree - count_of_degree == maximum_number_degree:
        if coefficients_of_numbers[number] != 1 and coefficients_of_numbers[number] != -1:
            polinom += str(coefficients_of_numbers[number]) + " " + "*" + " " + "x" + "^" + str(
                maximum_number_degree - count_of_degree)
        if coefficients_of_numbers[number] == 1:
            polinom += "x" + "^" + str(maximum_number_degree - count_of_degree)
        if coefficients_of_numbers[number] == -1:
            polinom += "-" + "x" + "^" + str(maximum_number_degree - count_of_degree)
    #
    if maximum_number_degree - count_of_degree == 1:
        if coefficients_of_numbers[number] != 1 and coefficients_of_numbers[number] != -1:
            if coefficients_of_numbers[number] > 0:
                polinom += " " + "+" + " " + str(coefficients_of_numbers[number]) + " " + "*" + " " + "x"
            else:
                polinom += " " + "-" + " " + str(abs(coefficients_of_numbers[number])) + " " + "*" + " " + "x"
        else:
            if coefficients_of_numbers[number] > 0:
                polinom += "+" + "x"
            else:
                polinom += "x"
        if coefficients_of_numbers[number] == -1:
            polinom += " " + "-" + " " + "x"

    if maximum_number_degree - count_of_degree == 0:
        if coefficients_of_numbers[number] > 0:
            polinom += " " + "+" + " " + str(coefficients_of_numbers[number])
        else:
            polinom += " " + "-" + " " + str(abs(coefficients_of_numbers[number]))

    count_of_degree += 1
if polinom == "":
    print(0)
print(polinom)
