from django.test import TestCase, Client

class AppTest(TestCase):
    def test_200_route(self):
        '''
        Check if route is accessible
        '''
        #arrange
        client = Client()
        
        #act
        response = client.get("/hola")
        
        #assert
        self.assertEquals(200, response.status_code)