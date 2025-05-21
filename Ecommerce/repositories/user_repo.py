class UserRepository:

    users = {} 
    logged_in_users = set()

    @classmethod
    def create_user(cls, email: str, password: str, full_name: str, username: str):
        if email in cls.users:
            raise Exception("User Already Exists")
        cls.users[email] = {"email": email, "password": password, "full_name": full_name, "username": username} 
        print(cls.users)
    
    @classmethod
    def get_user(cls, email: str):
        try: 
            if(cls.users.get(email)):
                return cls.users[email]
        except:
            raise Exception("User Not Found")
        
    @classmethod
    def add_logged_in_user(cls, user_id: str):
        cls.logged_in_users.add(user_id)

    @classmethod
    def is_logged_in(cls, user_id: str):
        return user_id in cls.logged_in_users