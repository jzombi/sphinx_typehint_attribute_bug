from mymodule.a.b.c.d import D

class Bad:
    """
    :param d: This is my parameter.
    """

    d: D  #: My attribute

    def __init__(self, d: D):
        self.d = d
