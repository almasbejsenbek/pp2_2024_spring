def all_true(tuple_data):
    return all(tuple_data)


tuple1 = (True, True, True)
tuple2 = (True, False, True)
print("All elements in tuple1 are True:", all_true(tuple1))
print("All elements in tuple2 are True:", all_true(tuple2))