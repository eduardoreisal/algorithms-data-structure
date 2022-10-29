def get_avg_temperature(array):
    return sum(array) / len(array)

def fill_temperatures_array(days):
    array = []
    for i in range(1, days + 1):
        temp = int(input(f"Day {i}'s high temp: "))
        array.append(temp)
    return array

def get_days_above_avg(array, avg):
    count = 0
    for temp in array:
        if temp > avg:
            count += 1
    return count

def main():
    if __name__ == '__main__':
        days = int(input('[+] How many days temperature: '))
        temperature_array = fill_temperatures_array(days)
        avg_temp = get_avg_temperature(temperature_array)
        days_above_avg = get_days_above_avg(temperature_array, avg_temp)
        print(f'Average = {avg_temp:.2f}')
        print(f'{days_above_avg} day(s) above average')

main()
