from flask_app.config.connection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        return connectToMySQL('esquema_usuarios').query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('esquema_usuarios').query_db(query)
        users = []
        for user in results:
            users.append(user)
        return users
    
    @classmethod
    def get_user(cls,data):
        query = "SELECT * FROM users where id = %(id)s;"
        results = connectToMySQL('esquema_usuarios').query_db(query,data)
        user = []
        for i in results:
            user.append(i)
        tan = len(user)-1
        for elemt in user:
            for k,v in elemt.items():
                if(k == "created_at"):
                     user[tan][k] = v.strftime("%b %d, %Y")
                if(k == "updated_at"):
                     user[tan][k] = v.strftime("%b %d, %Y %I:%M %p")
        return user
    
    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name = %(fname)s , last_name = %(lname)s, email = %(email)s, updated_at = NOW() where id =  %(id)s;"
        return connectToMySQL('esquema_usuarios').query_db(query,data)
    
    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users where id =  %(id)s;"
        return connectToMySQL('esquema_usuarios').query_db(query,data)