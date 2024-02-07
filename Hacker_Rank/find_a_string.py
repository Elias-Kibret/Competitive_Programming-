# https://www.hackerrank.com/challenges/find-a-string/problem


def count_substring(string, sub_string):
    count = 0
    for index, value in enumerate(string):
        if value == sub_string[0] and (index + len(sub_string)) <= len(string):
            if string[index:min(index + len(sub_string), len(string))] == sub_string:
                count += 1
    return count
        


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)