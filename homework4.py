immutable_var = (["STRING"], 1, 2, True)
print(immutable_var)
#immutable_var[2] = 8 выдаст ошибку тк кортеж не поддерживает обрашение по эелементам
mutable_list = [1, 2, 3, 4, 5, "string", True]
mutable_list[0] = 4
mutable_list[5] = "hello"
mutable_list[6] = False
print(mutable_list)