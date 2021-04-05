class Date:
    def __init__(self, date):
        try:
            if Date.validation(date):
                self.day, self.month, self.year = Date.convert_data(date)
                self.date = date
            else:
                raise ValueError(f'{date} - is incorrect date')
        except ValueError as err:
            print(err)

    @classmethod
    def convert_data(cls, date):
        """
        Метод разбивает дату из строки на отдельные значения
        :param date: 'dd-mm-yyyy'
        :return: day, month, year
        """
        day, month, year = [int(n) for n in date.split('-')]
        return day, month, year

    @staticmethod
    def validation(date):
        """
        Метод проверяет корректетность введенной даты
        :param date:
        :return:
        """
        if len(date.split('-')) == 3 and int(date.split('-')[1]) <= 12 \
                and int(date.split('-')[0]) <= 31:
            return True
        else:
            return False


correct_date = Date('01-12-1998')
print(f'Число - {correct_date.day}, месяц - {correct_date.month}, год - {correct_date.year}')

print(Date.convert_data('15-12-2020'))
print(Date.validation('15-20-2021'))
print(Date.validation('1-07-2015'))

incorrect_date = Date('32-15-1999')