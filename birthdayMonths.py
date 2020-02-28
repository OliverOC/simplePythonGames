import json
from collections import Counter
import matplotlib.pyplot as plt
from enum import Enum


class MonthEnum(Enum):
    """Enum with the ordered months."""
    __order__ = 'month1 month2 month3 month4 month5 month6 month7 month8 month9 month10 month11 month12'
    month1 = 'Jan'
    month2 = 'Feb'
    month3 = 'Mar'
    month4 = 'Apr'
    month5 = 'May'
    month6 = 'Jun'
    month7 = 'Jul'
    month8 = 'Aug'
    month9 = 'Sep'
    month10 = 'Oct'
    month11 = 'Nov'
    month12 = 'Dec'

def month_number_to_word_converter(month):
    if month == 1:
        month_output = "Jan"
    if month == 2:
        month_output = "Feb"
    if month == 3:
        month_output = "Mar"
    if month == 4:
        month_output = "Apr"
    if month == 5:
        month_output = "May"
    if month == 6:
        month_output = "Jun"
    if month == 7:
        month_output = "Jul"
    if month == 8:
        month_output = "Aug"
    if month == 9:
        month_output = "Sep"
    if month == 10:
        month_output = "Oct"
    if month == 11:
        month_output = "Nov"
    if month == 12:
        month_output = "Dec"
    return month_output


def add_zero_count_months_dict(dictionary):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for ii in months:
        if ii not in dictionary:
            dictionary[ii] = 0
        else:
            pass


# def add_zero_count_months_lists(keys_list, values_list):
#     months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#     for ii in months:
#         if ii not in keys_list:
#             keys_list.append(ii)
#             values_list.append(0)
#         else:
#             pass

# def reorder_dict_to_lists(dictionary2):
#     list1 = []
#     months1 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#     for entry in months1:
#         list1.append(dictionary2[entry])
#         return list1


if __name__ == "__main__":
    with open("birthdays.json", "r") as f:
        birthdays = json.load(f)

    birthday_dates = birthdays.values()
    birthday_months = []

    for i in range(len(birthday_dates)):
        birthday_months.append(int(birthday_dates[i][3:5]))

    birthday_months_words = []

    for i in birthday_months:
        # birthday_months_words.append(month_number_to_word_converter(i))
        birthday_months_words.append(month_number_to_word_converter(i))

    month_counter = Counter(birthday_months_words)
    add_zero_count_months_dict(month_counter)
    print(month_counter)

    month_counter_keys = month_counter.keys()
    month_counter_values = month_counter.values()

    months1 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    l_month = [(months1.index(key), val) for key, val in month_counter.items()]
    print(list(month_counter.keys()))
    print(l_month)
    l_month.sort()
    print(l_month)

    x_pos = [i for i, _ in enumerate(month_counter.keys())]
    plt.bar([idx for idx, val in l_month], [val for idx, val in l_month], align="center")
    plt.xticks([idx for idx, val in l_month], months1)
    plt.yticks([i for i in range((max(month_counter_values))+2)])
    plt.xlabel("Month")
    plt.ylabel("Count")
    plt.title("Number of Birthdays Occurring in Each Month")
    plt.show()
