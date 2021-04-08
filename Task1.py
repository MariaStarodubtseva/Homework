class Date:
    def __init__(self, date_str):
        self.date_str = date_str
    @classmethod
    def convert(cls, date_str):
        return tuple(map(int, date_str.split('-')))

    @staticmethod
    def validate(date):
        if date[0] <= 0 or date[0] > 31:
            return

        if date[1] <= 0 or date[1] > 12:
            return

        if len(str(date[2])) != 4:
            return

        return True

for date_str in ['05-04-2021', '05-24-2021', '75-04-2021', '05-04-55']:
    date = Date(date_str)
    # print(f'date_str = {date.date_str}')

    converted_date = Date.convert(date.date_str)
    # print(f'converted_date = {converted_date}')

    is_valid = Date.validate(converted_date)
    print(f'{date_str} - ', end='')
    print('Дата валидна' if is_valid else 'Дата не валидна')