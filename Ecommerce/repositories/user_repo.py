class UserRepository:

    def __init__(self, users):
        self.users = users

    def create_user(self, email: str, password: str, full_name: str, username: str):
        if email in self.users:
            raise Exception("User Already Exists")
        self.users[email] = {"email": str, "password": str, "full_name": str, "username": str} 
    
    def get_usert(self, email: str):
        try: 
            if(self.users.get(email)):
                return self.users.get(email)
        except:
            raise Exception("User Not Found")