if __name__ == '__main__':
    line = input()
    #result = split_and_join(line)
    line=line.split()
    result="-".join(line)
    print(result)