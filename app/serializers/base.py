from pydantic import BaseModel


class SerializerError(Exception):
    pass


class BaseSerializer(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errorss = None

    def validation(self) -> bool:
        return True

    def is_valid(self):
        try:
            self.validation()
            return True
        except SerializerError as err:
            self.errorss = err.args
            return False

    def to_dict(self):
        return super().__dict__

    def errors(self):
        return self._errorss


class User(BaseSerializer):
    user_id: int
    username: str

    def validation(self) -> bool:
        if self.user_id == 0:
            raise SerializerError("Invalid User id")
        return True


a = User(username='sayan', user_id=1)
print(a.errors)
print(a.is_valid())
print(a.errors)
print(a.to_dict())
