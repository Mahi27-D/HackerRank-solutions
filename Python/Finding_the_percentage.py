if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    s = student_marks[query_name]
    sum=0.0
    for i in s:
        sum=sum+i
    print(f"{sum/3.0:.2f}")
        