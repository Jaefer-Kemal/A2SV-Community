def split_and_join(line):
    line=line.split(" ")
    return "-".join(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
# IT TOOK 2 minutes and 10 seconds