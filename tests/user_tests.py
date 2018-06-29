import unittest
from services import ServiceAPI

class TestUserData(unittest.TestCase):
    location = 25753
    user_test = 517135

    def test_list_location(self):
        serv = ServiceAPI()
        local = serv.list_location()
        self.assertEquals(local is not None)

    def test_list_users(self):
        c = ServiceAPI()
        users = c.list_users(self.location)
        self.assertEquals(users is not None)

    def test_get_user_by_id(self):
        c = ServiceAPI()
        users = c.get_users_data(self.user_test)
        self.assertEquals(users is not None)

    def test_list_time_punches(self):
        c = ServiceAPI()
        times = c.get_time_punches()
        self.assertEquals(times is not None)