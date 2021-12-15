import unittest

from main import *

one_to_many = [(oper.name, oper.salary, lang.name)
								 for lang in languages
								 for oper in operators
								 if oper.lang_id == lang.id]

many_to_many_temp = [(lang.name, ol.oper_id, ol.lang_id)
										 for lang in languages
										 for ol in opers_langs
										 if lang.id == ol.lang_id]

many_to_many = [(oper.name, oper.salary, lang_name)
								for lang_name, _, lang_id in many_to_many_temp
								for oper in operators if oper.lang_id == lang_id]


class Tests(unittest.TestCase):
	def test_filter_letter(self):
		self.assertEqual(filter_letter(one_to_many, 'A'), [('Rebekka', 300, 'AspectJ'), ('Dima', 500, 'Ada')])

	def test_sorted_max_salary(self):
		self.assertEqual(sorted_max_salary(one_to_many), [('C', 3000), ('C++', 2500), ('Java', 2000), ('Python', 1500),
																											('Ada', 500), ('AspectJ', 300)])

	def test_links_sorted_langs(self):
		self.assertEqual(links_sorted_langs(many_to_many), [('Rebekka', 300, 'AspectJ'), ('Rebekka', 300, 'AspectJ'),
																											 ('Rebekka', 300, 'AspectJ'), ('Viktor', 3000, 'C'),
																											 ('Viktor', 3000, 'C'), ('Andrey', 2000, 'Java'),
																											 ('Andrey', 2000, 'Java'), ('Maxim', 1000, 'Python'),
																											 ('Daniel', 1500, 'Python'), ('Maxim', 1000, 'Python'),
																											 ('Daniel', 1500, 'Python'), ('Maxim', 1000, 'Python'),
																											 ('Daniel', 1500, 'Python')])


if __name__ == '__main__':
	unittest.main()