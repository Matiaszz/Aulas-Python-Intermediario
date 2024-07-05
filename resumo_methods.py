

class Connection:
    def __init__(self, host='LocalHost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def set_default(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection  # fiz praticamente um self com cls


c1 = Connection.set_default('Usuario', 123)

# c1.set_user('Allan')
# c1.set_password(f'Opa{3}opa')

print(c1.user, 'senha:', c1.password)
