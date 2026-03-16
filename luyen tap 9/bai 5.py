class User:
    def __init__(self, id_value):
        self._id = id_value

    @property
    def id(self):
        """Getter cho id, cho phép đọc giá trị nhưng không cho phép gán lại từ bên ngoài"""
        return self._id

user1 = User("U1001")
print(f"ID của user là: {user1.id}")