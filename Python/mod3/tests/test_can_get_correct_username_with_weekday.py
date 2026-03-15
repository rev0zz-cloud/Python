import unittest
from freezegun import freeze_time

from have_a_good_day import app

WEEKDAYS_TUPLE = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')
FEMININE_DAYS = (2, 4, 5)

DATES = [
    '2024-01-01',  # понедельник
    '2024-01-02',  # вторник
    '2024-01-03',  # среда
    '2024-01-04',  # четверг
    '2024-01-05',  # пятница
    '2024-01-06',  # суббота
    '2024-01-07',  # воскресенье
]

class TestHaveAGoodDay(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def _check_day(self, date, weekday_index):
        greeting = 'Хорошей' if weekday_index in FEMININE_DAYS else 'Хорошего'
        weekday = WEEKDAYS_TUPLE[weekday_index]
        with freeze_time(date):
            response = self.app.get('/hello-world/test_name')
            response_text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response_text.endswith(f'{greeting} {weekday}!'))

    def test_all_weekdays(self):
        for i, date in enumerate(DATES):
            with self.subTest(date=date):
                self._check_day(date, i)
