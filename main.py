import time


def main():
    maximum_number_degree = int(input())
    coefficients_of_numbers = [int(input()) for i in range(maximum_number_degree + 1)]
    start_time = time.time()
    polinom = ""
    count_of_degree = 0
    for i in range(len(coefficients_of_numbers)):
        polinom += build(coefficients_of_numbers[i], maximum_number_degree - count_of_degree,
                         count_of_degree)
        count_of_degree += 1
    print("время выполнения: ")
    print(time.time() - start_time)
    if polinom == "":
        print(0)
    else:
        print(polinom)


def zero_coeffic():
    return ""


def first_monom(coeffic, max_deg):
    result = ""
    if coeffic < 0:
        result += "-"
    if coeffic != 1:
        result += str(coeffic)
    if max_deg != 0:
        if result != "":
            result += " * "
        result += f'x{degrees(max_deg, coeffic)}'

    return result


def degrees(degree, coeffic):
    if degree > 1:
        return "^" + str(degree)
    if degree == 1:
        return ""
    if degree == 0:
        return degree_zero(coeffic)


def degree_zero(coeffic):
    return " " + plus_or_minus(coeffic) + " " + str(abs(int(coeffic)))


def plus_or_minus(coeffic):
    if coeffic > 0:
        return "+"
    if coeffic < 0:
        return "-"
    else:
        zero_coeffic()


def one_coeffic(coeffic, degree):
    if degree != 0:
        return " " + plus_or_minus(coeffic) + " " + "x" + degrees(degree, coeffic)
    else:
        return degree_zero(coeffic)


def big_coeffic(coeffic, degree):
    if degree != 0:
        return " " + plus_or_minus(coeffic) + " " + str(abs(coeffic)) + " " + "*" + " " + "x" + degrees(degree,
                                                                                                        coeffic)
    else:
        return degree_zero(coeffic)


def build(coeffic, degree, cnt_deg):
    if cnt_deg == 0:
        return first_monom(coeffic, degree)
    elif coeffic == 0:
        return zero_coeffic()
    elif coeffic == 1:
        return one_coeffic(coeffic, degree)
    elif coeffic > 1:
        return big_coeffic(coeffic, degree)
    elif coeffic < -1:
        return big_coeffic(coeffic, degree)
    elif coeffic == -1:
        return one_coeffic(coeffic, degree)


if __name__ == "__main__":
    main()
