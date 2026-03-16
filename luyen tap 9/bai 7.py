class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    @classmethod
    def from_string(cls, data_string):
        """
        Tạo đối tượng Person từ chuỗi có định dạng 'name-age'
        """
        name, age = data_string.split('-')
        return cls(name, age)
nguoi1 = Person.from_string("Nam-20")
print(f"Tên: {nguoi1.name}, Tuổi: {nguoi1.age}")