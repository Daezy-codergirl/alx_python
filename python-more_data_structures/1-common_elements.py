def common_elements(set_1, set_2):
    common_set = set()

    for element in set_1:
        if element in set_2:
            common_set.add(element)
    return common_set

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }

common_set = common_elements(set_1, set_2)
print(sorted(list(common_set)))