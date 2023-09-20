var_name = input("camelCase: ")


for i in range(len(var_name)):
    while var_name[i].isupper():
        var_name = var_name.replace(var_name[i], "_" + var_name[i].lower())
        print(var_name)
        break
    while i == len(var_name) - 1:
        print(var_name)
        break
