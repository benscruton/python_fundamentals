def longest_common_prefix(strings):
    if not len(strings):
        return ""
    prefix = strings[0]
    for i in range(1, len(strings)):
        if not prefix:
            break
        string = strings[i]
        if len(string) >= len(prefix) and string[:len(prefix)] == prefix:
            continue
        for j in range(len(string)):
            if j >= len(prefix) or prefix[j] != string[j]:
                prefix = string[:j]
                break
    return prefix

test1 = ["hello", "hello", "helloawef"]
test2 = ["a", "b", "c"]
test3 = ["flee", "flow", "flea"]

tests = [test1, test2, test3]

for test in tests:
    print(longest_common_prefix(test))
