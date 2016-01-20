from django.test import TestCase

# Create your tests here.

class ExampleTestCase(TestCase):
	"""
	TestCase example
	"""
	def setUp(self):
		"""
		Initialize test data
		"""
		pass

	def test_name_is_beeva(self):
		"""
		Dummy test
		"""
		name = 'BEEVA'
		self.assertEqual(name.lower(), 'beeva')
