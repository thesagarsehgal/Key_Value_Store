from app.flask_app import app
import unittest
import json

class FlaskTestCase(unittest.TestCase):

	def test_reset(self):
		reseter = app.test_client(self)
		response = reseter.get('/reset/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data,"Database Reset".encode())

		key = "k1"
		value = "v1"
		
		setter = app.test_client(self)
		response = setter.get('/set/?key={}&value={}'.format(key,value))
		self.assertEqual(response.data,"{}:{} stored sucessfully".format(key, value).encode())

		reseter = app.test_client(self)
		response = reseter.get('/reset/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data,"Database Reset".encode())

		getter = app.test_client(self)
		response = getter.get('/get/?key={}'.format(key))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data,"None".encode())


	def test_set_key(self):
		reseter = app.test_client(self)
		response = reseter.get('/reset/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data,"Database Reset".encode())

		key = "k1"
		value = "v1"
		
		setter = app.test_client(self)
		response = setter.get('/set/?key={}&value={}'.format(key,value))
		self.assertEqual(response.data,"{}:{} stored sucessfully".format(key, value).encode())
	
	def test_get_key_not_preset(self):
		reseter = app.test_client(self)
		response = reseter.get('/reset/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data,"Database Reset".encode())

		key = "k1"
		
		getter = app.test_client(self)
		response = getter.get('/get/?key={}'.format(key))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data,"None".encode())

	def test_get_key_preset(self):
		reseter = app.test_client(self)
		response = reseter.get('/reset/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data,"Database Reset".encode())

		key = "k1"
		value = "v1"
		
		setter = app.test_client(self)
		response = setter.get('/set/?key={}&value={}'.format(key,value))
		self.assertEqual(response.data,"{}:{} stored sucessfully".format(key, value).encode())
		
		getter = app.test_client(self)
		response = getter.get('/get/?key={}'.format(key) )
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data,"{}".format(value).encode())

if __name__ == '__main__':
    unittest.main()