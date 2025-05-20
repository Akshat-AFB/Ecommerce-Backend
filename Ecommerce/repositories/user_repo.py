class UserRepository:

    users = {} 

    @classmethod
    def create_user(cls, email: str, password: str, full_name: str, username: str):
        if email in cls.users:
            raise Exception("User Already Exists")
        cls.users[email] = {"email": str, "password": str, "full_name": str, "username": str} 
    
    @classmethod
    def get_user(cls, email: str):
        try: 
            if(cls.users.get(email)):
                return cls.users.get(email)
        except:
            raise Exception("User Not Found")