def solution(numbers):
    str_number = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in range(10):
        if str_number[i] in numbers:
            numbers = numbers.replace(str_number[i], str(i))
    return int(numbers)