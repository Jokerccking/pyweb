from Models import Model


class User(Model):
    def __init__(self, form):
        self.id = form.get('id', None)
        if self.id is not None:
            self.id = int(self.id)
        self.username = form.get('username')
        self.password = form.get('password')

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
