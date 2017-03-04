from Models import Model


class User(Model):
    def __init__(self, form):
        self.id = int(form.get('id', -1))
        self.username = form.get('username')
        self.password = form.get('password')
        self.role = int(form.get('role', 10))

    def validate_login(self):
        ms = self.all()
        b = False
        for m in ms:
            if m.username == self.username and m.password == self.password:
                b = True
        return b

    def validate_register(self):
        b = False
        if len(self.username) > 2 and len(self.password) > 2:
            b = True
        return b
