import statistics
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    y = x.split(",")
    input_list = list(map(float, y))
    return input_list

def calc_average(input_list):
     average = sum (input_list) / len(input_list)
     return average

def find_min_max(input_list):
    minimum = min(input_list)
    maximum = max(input_list)
    return [minimum, maximum]

def sort_temperature(input_list):
    sorted_temp = sorted(input_list)
    return sorted_temp

def calc_median_temperature(input_list):
    median = statistics.median(input_list)
    return median

def main():
    display_main_menu()
    num_list = get_user_input()
    ave_value = calc_average(num_list)
    print("average = " + str(ave_value))
    min, max = find_min_max(num_list)
    print("min = " + str(min))
    print("max = " + str(max))
    sort_temp = sort_temperature(num_list)
    print("Asending = " + str(list(sort_temp)))
    median_temp = calc_median_temperature(num_list)
    print("Median = " + str(median_temp))

if __name__ == "__main__":
    main()