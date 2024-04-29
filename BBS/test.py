class Tester:

    series = ''

    def __init__(self, series):
        self.series = series

    def testSeries(self):
        print('One bit test: ' + str(self.__oneBitTest()))
        print('Subseries test: ' + str(self.__subSeriesTest()))
        print('Long subseries test: ' + str(self.__longSubSeriesTest()))
        print('Poker test: ' + str(self.__pokerTest()))

    def __oneBitTest(self):
        ones = 0
        zeros = 0
        for bit in self.series:
            if bit == '1':
                ones += 1
            else:
                zeros += 1
                    
        return 'Passed' if ones > 9725 and ones < 10275 else 'Failed'
    

    def __subSeriesTest(self):
        ranges = {
            1: [2315, 2685],
            2: [1114, 1386],
            3: [527, 723],
            4: [240, 384],
            5: [103, 209],
            6: [103, 209]
        }
        temp_series = self.series
        for i in range(6, 0, -1):
            sub_zero_series = i * '0'
            sub_one_series = i * '1'
            
            count_zero = temp_series.count(sub_zero_series)
            count_one = temp_series.count(sub_one_series)
            
            temp_series = temp_series.replace(sub_zero_series, ' ')
            temp_series = temp_series.replace(sub_one_series, ' ')

            if count_zero < ranges[i][0] or count_zero > ranges[i][1] or count_one < ranges[i][0] or count_one > ranges[i][1]:
                print(f"Subseries {i} failed")
                print(f"Zero: {count_zero}, One: {count_one}")
                return 'Failed'
        return 'Passed'
    
    def __longSubSeriesTest(self):
        if self.series.count('0' * 26) > 0 or self.series.count('1' * 26) > 0:
            return 'Failed'
        return 'Passed'

    def __pokerTest(self):
        poker_dict = {}
        for i in range(0, len(self.series), 4):
            sub_series = self.series[i:i+4]
            if sub_series in poker_dict:
                poker_dict[sub_series] += 1
            else:
                poker_dict[sub_series] = 1

        sum = 0
        for key in poker_dict:
            sum += poker_dict[key]**2
        x = 16/5000 * sum - 5000
        return 'Passed' if x < 46.17 and x > 2.16 else 'Failed'