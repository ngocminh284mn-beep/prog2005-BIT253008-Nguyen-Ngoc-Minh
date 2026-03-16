class User:
    def __init__(self, id_value):
        self._id = id_value

    @property
    def id(self):
        return self._id

user1 = User("u999")
print(f"ID của user là: {user1.id}")