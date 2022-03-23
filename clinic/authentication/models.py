from django.db import connection

def create_user(email, username, password, user_type):
    '''
    Used to create a new user.
    '''
    with connection.cursor() as cursor:
        cursor.execute('INSERT INTO "Users" ("Email", "Username", "Password", "User_type") VALUES(%s,%s,%s,%s)', (email, username, password, user_type))
        # session.get("user_id") -> 123
        
        
def get_user_data(id):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM "Users" WHERE "UserID" = %s', (id))
        row = cursor.fetchone()
        
    return row
    