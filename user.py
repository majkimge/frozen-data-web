from hashing import hash_password

class User:
  def __init__(self, id, username):
    self.is_active=True
    self.is_anonymous=False
    self.is_authenticated=True # TODO
    self.id = str(id)
    self.username=username

  def get(db_result):
    if len(db_result) == 0:
      return None
    else:
      return User(db_result[0][0], db_result[0][1])
  
  def user_from_id(mysql, id):
    id = int(id)
    with mysql.connect() as conn:
      with conn.cursor() as cursor:
        cursor.execute("SELECT id,username FROM users WHERE id=%(id)s;", {'id':id})
        data = cursor.fetchall()
    if len(data) == 0:
      return None
    else:
      return User(data[0][0], data[0][1])

  def get_id(self):
    return self.id

  def verify_login(mysql, username, password):
    password = hash_password(password)
    with mysql.connect() as conn:
      with conn.cursor() as cursor:
        cursor.execute("SELECT id,username FROM users WHERE username=%(username)s AND password=%(password)s", {"username":username, "password":password})
        data = cursor.fetchall()

    if len(data) == 0:
      return None
    else:
      return User(data[0][0], data[0][1])


  