from collections import defaultdict

# 이것이 우리의 '입력' 데이터입니다.
texts = ["hello world", "world is beautiful", "hello everyone"]

# 'Map' 함수는 텍스트를 단어로 분리하고, 각 단어를 키로, 값 '1'을 값으로하는 키-값 쌍을 생성합니다.
def map_function(text):
    words = text.split()
    return [(word, 1) for word in words]

# 'Reduce' 함수는 동일한 키를 가진 모든 값을 합산합니다.
def reduce_function(key, values):
    return key, sum(values)

# Map 단계
mapped_values = [map_function(text) for text in texts]

# Reduce를 준비하기 위해 모든 키-값 쌍을 모읍니다.
collected_values = defaultdict(list)
for key_value_pairs in mapped_values:
    for key, value in key_value_pairs:
        collected_values[key].append(value)

# Reduce 단계
reduced_values = [reduce_function(key, value) for key, value in collected_values.items()]

print(reduced_values)
