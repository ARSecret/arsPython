from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

# Эти значения далее будут подставляться в итоговый текст, отсюда
available_burger_names = ['🐔 c курицой', '🐄 с говядиной', '🐟 с рыбой']
available_fries_names = ['фри', 'деревенский', 'волнистый']
available_drink_names = ['кола', 'кола без сахара', 'фанта', 'спрайт']