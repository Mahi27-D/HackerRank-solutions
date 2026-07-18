def swap_case(s):
    ans=""
    for i in s:
        if(i.isupper()):
            ans=ans+i.lower()
        else:
            ans=ans+i.upper()
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)