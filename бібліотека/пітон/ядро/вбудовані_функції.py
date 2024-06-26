import enum

from .типи_данних import *
from .фіксовані_значення import *

class СтильДруку(enum.Enum):
    СТАНДАРТНИЙ = '\033[0m'
    STANDARD = '\033[0m'
    ЗЕЛЕНИЙ = '\033[92m'
    ЧЕРВОНИЙ = '\033[31m'
    ЖОВТИЙ = '\033[93m'
    СИНІЙ = '\033[94m'
    БЛАКИТНИЙ = '\033[94m'

    GREEN = ЗЕЛЕНИЙ
    RED = ЧЕРВОНИЙ
    YELLOW = ЖОВТИЙ
    BLUE = СИНІЙ

    WARNING = ЧЕРВОНИЙ

    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def за_замовчуванням():
        return СтильДруку.СТАНДАРТНИЙ

    @staticmethod
    def отримати(стиль):
        if стиль is Жоден:
            обраний_стиль = СтильДруку.за_замовчуванням()
        elif є_екземпляром(стиль, СтильДруку):
            обраний_стиль = стиль
        else:
            підготовлена_назва = стиль.upper()

            обраний_стиль = отримати_атрибут(СтильДруку, підготовлена_назва, Жоден)
            if обраний_стиль is Жоден:
                обраний_стиль = СтильДруку.за_замовчуванням()
        return обраний_стиль

PrintStyle = СтильДруку

def надрукувати(текст, *арг, розд=' ', закінчення='\n', файл = Жоден, стиль = Жоден):
    """
    Друк значень до потоку, чи до sys.stdout через default


    Необов'язкові ключі-аргументи:

    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """

    if стиль is not Жоден:
        стиль_друку = СтильДруку.отримати(стиль)

        текст = стиль_друку.value + текст + СтильДруку.СТАНДАРТНИЙ.value

    print(текст, *арг, sep=розд, end=закінчення, file=файл)


def є_екземпляром(змінна, тип_данних):  # real signature unknown; restored from __doc__
    """
    Повертає "істина" якщо "змінна" є екземляром класу або підкласу вказаному у "тип_даних"
    """
    return isinstance(змінна, тип_данних)


def отримати_атрибут(обєкт, імя, за_замовчуванням=Жоден):  # known special case of getattr
    """
    getattr(обєкт, імя[, за_замовчанням]) -> значення

    Отримання значення атрибуту за його ім'ям;
    отримати_атрибут(x, 'y') еквівалентне до x.y

    При наявності аргументу "за_замовчуванням" функція повертає його при відсутності.
    Інакше викликається переривання.
    """
    return getattr(обєкт, імя, за_замовчуванням)
