def solution(quiz):
    new_quiz = []
    answer = []
    for i in range(len(quiz)):
        new_quiz.append(quiz[i].split("="))
    for i in range(len(new_quiz)):
        if eval(new_quiz[i][0]) == int(new_quiz[i][1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer