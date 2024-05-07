import threading
from пітон.ядро.фіксовані_значення import *

class Потік(threading.Thread):
    """A class that represents a thread of control.

    This class can be safely subclassed in a limited fashion. There are two ways
    to specify the activity: by passing a callable object to the constructor, or
    by overriding the run() method in a subclass.

    """

    def __init__(свій, група=Жоден, ціль=Жоден, імя=Жоден,
                 арг=(), ксарг=Жоден, *, демон=Жоден):
        super().__init__(group=група, target=ціль, name=імя, args=арг, kwargs=ксарг, daemon=демон)

    def запустити(свій):
        свій.start()

    def приєднати(свій, тайм_аут=Жоден):
        """Wait until the thread terminates.

        This blocks the calling thread until the thread whose join() method is
        called terminates -- either normally or through an unhandled exception
        or until the optional timeout occurs.

        When the timeout argument is present and not None, it should be a
        floating point number specifying a timeout for the operation in seconds
        (or fractions thereof). As join() always returns None, you must call
        is_alive() after join() to decide whether a timeout happened -- if the
        thread is still alive, the join() call timed out.

        When the timeout argument is not present or None, the operation will
        block until the thread terminates.

        A thread can be join()ed many times.

        join() raises a RuntimeError if an attempt is made to join the current
        thread as that would cause a deadlock. It is also an error to join() a
        thread before it has been started and attempts to do so raises the same
        exception.

        """

        свій.join(timeout=тайм_аут)
