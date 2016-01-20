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
		name = 'BEEVA'
		self.assertEqual(name.lower(), 'beeva')
