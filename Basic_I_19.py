string = input("Your string: ")
# def new_string(string):
#     alter_string = string.split()
#     if alter_string[0] == "Is":
#         alter_string = ' '.join(alter_string)
#         return alter_string
#     else:
#         alter_string = ' '.join(alter_string)
#         alter_string = "Is " + alter_string
#         return alter_string
#
#
# print(new_string(string))

def new_string(string):
    if len(string) >= 2 and string.lower()[:2] == "is":
        return string
    return "Is " + string


print(new_string(string))
