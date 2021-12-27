import unittest
from bot import TOKEN
from handlers.food import available_burger_names, available_drink_names, available_fries_names


class TestBotWork(unittest.TestCase):
    # список еды, напитков и прочего может подгружаться из баз данных, поэтому важно знать, что список
    # возможных продуктов не пустой
    def test_bot_food_not_empty(self):
        self.assertNotEqual(0, len(available_burger_names))

    def test_bot_drinks_not_empty(self):
        self.assertNotEqual(0, len(available_drink_names))

    def test_bot_fries_not_empty(self):
        self.assertNotEqual(0, len(available_fries_names))

    # важно знать, что токен бот корректен, можно проверять его длину
    def test_bot_token_exist(self):
        self.assertEqual(len(TOKEN), 46)


if __name__ == '__main__':
    unittest.main()
