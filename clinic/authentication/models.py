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
        cursor.execute('SELECT "Password", "UserID", "User_type" FROM "Users" WHERE "Users"."Username" = %s', [username])
        row = cursor.fetchone()
        
    return row
    
def get_all_user_data(user_id):
    '''
    Return a row of user data.
    '''
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Users" WHERE "Users"."UserID" = %s', [user_id])
        row = cursor.fetchone()
        
    return row