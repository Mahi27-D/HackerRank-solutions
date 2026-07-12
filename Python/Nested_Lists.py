if __name__ == '__main__':
    s = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        s[name]=score
    values_list = list(s.values())
    values_list.sort()
    
    unique_numbers = list(set(values_list))
    a=unique_numbers[1]
    
    #a=values_list[1];
    matching_keys = [key for key, value in s.items() if value == a]
    matching_keys.sort()
    for i in matching_keys:
        print(i)