from string import digits


class User:
    def __init__(self, login, password):
        """Чтобы запустить все проверки setter при инициализации экземпляра класса
        Нужно вместо self.__password использовать свойства setter  def password(self, value): """
        self.login = login
        # self.__password = password не свойство
        self.password = password #свойство проперти!!!

    @property
    def password(self):
        print("getter")
        return self.__password

    @staticmethod
    def is_include_number(password):
        """Проверка есть ли в наличии цыфры в паролле!
        Чтобы экземпляр класса не принимался мы вместо
        self ставим password и ставим декоратор статикметод!"""
        for i in digits:
            if i in password:
                return True
        return False

    @password.setter
    def password(self, value):
        """Проверка на Len(password),on str(password)"""
        print("setter")
        if not isinstance(value, str):
            raise TypeError('Password need be string!')
        if len(value) < 4:
            raise ValueError('len password dont big! min password >= 4')
        if len(value) > 12:
            raise ValueError('Len password very big! max password <= 12')
        if not User.is_include_number(value):  # Если наша функция не сработает,тоесть даст Фолс!
            raise ValueError('Password needs min(one number)')
        self.__password = value

