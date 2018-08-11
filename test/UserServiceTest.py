import unittest

import firebase_admin

from src.client.FirebaseAuthClient import FirebaseAuthClient
from src.client.FirebaseDBClient import FirebaseDBClient
from src.model.User import User
from src.service.UserService import UserService


class UserServiceTest(unittest.TestCase):
    """
    Tests for test user service methods
    """

    def setUp(self):
        self.dbClient = FirebaseDBClient()
        self.authClient = FirebaseAuthClient()
        self.test_user_service = UserService(db=self.dbClient, auth=self.authClient)

        self.is_setup = False
        self.TEST_FIRST_NAME = "test_first_name"
        self.TEST_LAST_NAME = "test_last_name"
        self.TEST_ID = "test_id"
        self.TEST_EMAIL = "TEST_EMAIL@gmail.com"
        self.TEST_PHONE_NUMBER = "+12938457449"
        self.CHANGED_NAME = "test_changed_name"
        self.TEST_PASSWORD = "test_password"

    def tearDown(self):
        firebase_admin.delete_app(firebase_admin.get_app())

    def test_initialize_user(self):
        """
        Test if user can be properly initialized
        """
        self.test_user_service.initialize_user(
            first_name=self.TEST_FIRST_NAME,
            last_name=self.TEST_LAST_NAME,
            email=self.TEST_EMAIL,
            phone_number=self.TEST_PHONE_NUMBER,
            password=self.TEST_PASSWORD
        )

        self.assertIsNotNone(self.test_user_service)

        # Check to see that user was property created.
        self.assertEqual(self.test_user_service.target_user.first_name, self.TEST_FIRST_NAME)
        self.assertEqual(self.test_user_service.target_user.last_name, self.TEST_LAST_NAME)
        self.assertIsNotNone(self.test_user_service.target_user.id)

        # Check to see that entry was created in database
        self.assertIsNotNone(self.dbClient.get_user_by_id(self.test_user_service.target_user.id))


        self.test_user_service.delete_user(self.test_user_service.target_user)

    def test_delete_user(self):

        """
        Test to see that  user can be property deleted.
        """


        #initialize user
        self.test_user_service.initialize_user(
            first_name=self.TEST_FIRST_NAME,
            last_name=self.TEST_LAST_NAME,
            email=self.TEST_EMAIL,
            phone_number=self.TEST_PHONE_NUMBER,
            password=self.TEST_PASSWORD
        )
        self.assertIsNotNone(self.test_user_service)
        self.assertEqual(self.test_user_service.target_user.first_name, self.TEST_FIRST_NAME)
        self.assertEqual(self.test_user_service.target_user.last_name, self.TEST_LAST_NAME)
        self.assertIsNotNone(self.test_user_service.target_user.id)
        #delete
        temp_user_id = self.test_user_service.target_user.id
        self.test_user_service.delete_user(self.test_user_service.target_user)
        self.assertIsNone(self.test_user_service.load_user_by_id(temp_user_id))


    def test_edit_user_info(self):
        """
        Test to see that user info can be edited correctly
        """

        target_field_name = "first_name"

        #TODO: Jake : I'll Initialize a Workout[] array later unless you get to it
        test_user = User(self.TEST_ID, self.TEST_FIRST_NAME, self.TEST_LAST_NAME, self.TEST_EMAIL, self.TEST_PHONE_NUMBER, None)
        self.test_user_service.target_user = test_user
        self.test_user_service.edit_user_info(self.TEST_ID, target_field_name, self.CHANGED_NAME)

        self.assertEqual(self.test_user_service.target_user.first_name, self.CHANGED_NAME)
        self.test_user_service.edit_user_info(self.TEST_ID, target_field_name, self.CHANGED_NAME)


