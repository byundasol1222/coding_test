# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때,
# 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오.
# "abadabac" # 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!


input = "abadabac"


def find_not_repeating_first_character(string):
    array = [0] * 26
    not_repeated_array = []
    for char in string:
        idx = ord(char) - ord('a')
        array[idx] += 1
    for idx, value in enumerate(array):
        if value == 1:
            not_repeated_array.append(chr(idx + ord('a')))

    for char in string:
        if char in not_repeated_array:
            return char
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
