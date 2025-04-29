# TODO Напишите функцию find_common_participants
def find_common_participants(group1: str, group2: str, delimiter: str = ',') -> list:
    set1 = set(group1.split(delimiter))
    set2 = set(group2.split(delimiter))

    common_participants = sorted(set1.intersection(set2))

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, delimiter='|'))