from faker import Faker


class GenerateUser:
    @staticmethod
    def creat_user():
        fake = Faker()
        user = {"email": fake.email(),
                   "password": fake.password(),
                   "name": fake.user_name()}
        return user
