with open('names.txt') as f:
    content = f.readline()

names = [name.strip('"') for name in content.split(',')]
sorted_names = sorted(names)

# loops over twice to sum letters minus 64 because ord() returns 65
name_val = [sum([ord(letters) - 64 for letters in names]) for names in sorted_names]

# loops over name_val list and add 1 position for 0 index, then multiplies position and name value
enum_list = [(pos + 1) * nv for pos, nv in enumerate(name_val)]

print sum(enum_list)













