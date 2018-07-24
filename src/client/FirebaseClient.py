import firebase_admin
from firebase_admin import db, credentials
from src.config.config import FirebaseConfig
from src.constants.DatabaseConstants import DatabaseConstants

class FirebaseClient:

    def __init__(self):
        self.SDK_PATH = FirebaseConfig.SDK_PATH

        self.cred = credentials.Certificate(self.SDK_PATH)
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': FirebaseConfig.DATABASE_URL
        })
        self.db = db.reference()

    def add_user(self, user):
        self.db.push(DatabaseConstants.USERS, user)

    def set_user(self, user):
        self.db.child(DatabaseConstants.USERS + '/' + user).set(user)

    def get_usertemp0(self, user):
        return self.db.get(DatabaseConstants.USERS + '/' + user)
    def get_usertemp1(self, user):
        return self.db.child(DatabaseConstants.USERS + '/' + user)

    def delete_usertemp0(self, user):
        self.get_usertemp0(user).delete()

    def delete_usertemp1(self, user):
        self.get_usertemp1(user).delete()


    def add_workout(self, user, workout):
        self.db.push(DatabaseConstants.USERS + '/' +  user + '/' + DatabaseConstants.WORKOUTS, workout)

    def set_workout(self, user, workout):
        self.db.child(DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS).set(workout)

    def get_workouttemp0(self, user):
        return self.db.get(DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS)

    def get_workouttemp1(self,user):
        return self.db.child(DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS)

    def delete_workout(self, user):
        self.get_workout(user).delete()

    def add_workout(self, user, workout):
        self.db.push(DatabaseConstants.USERS + user + DatabaseConstants.WORKOUTS, workout)

    def set_exercise(self, user, workout, exercise):
        self.db.child(
            DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS + '/' + workout + '/' + DatabaseConstants.EXERCISES).set(
            exercise)

    def get_exercise(self, user, workout):
        return self.db.get(
            DatabaseConstants.USERS + '/' + user + '/' + DatabaseConstants.WORKOUTS + '/' + workout + '/' + DatabaseConstants)

    def delete_exercise(self, user, workout):
        self.get_exercise(user, workout).delete()



