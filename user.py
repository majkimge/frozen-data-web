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
  
  def build_request(id):
    id = int(id)
    return "SELECT id,username FROM users WHERE id=%(id)s;", {'id':id}

  def get_id(self):
    return self.id

  