from django.db import connection

def create_user(email, username, password, user_type):
    '''
    Used to create a new user.
    '''
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO "Users" ("Email", "Username", "Password", "User_type") VALUES(%s,%s,%s,%s)', (email, username, password, user_type))
            
def get_user_password(username):
    '''
    Return the password hash of a user.
    '''
    with connection.cursor() as cursor:
        cursor.execute('SELECT "Password", "UserID" FROM "Users" WHERE "Users"."Username" = %s', [username])
        row = cursor.fetchone()
        
    return row
    