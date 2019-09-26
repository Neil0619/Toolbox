# coding=utf-8

try:
    import typing  # noqa
    from typing import cast

    _ObjectDictBase = typing.Dict[str, typing.Any]
except ImportError:
    _ObjectDictBase = dict

    def cast(typ, x):
        return x
else:
    pass


class ObjectDict(_ObjectDictBase):
    """Makes a dictionary behave like an object, with attribute-style access.

    1. 当访问的 key 不存在时返回 None

    例
    判断一个 key 是否存在，
    以前需要   `'key' in object_dict and object_dict.key`
    现在只需要 `object_dict.key`

    2. 初始化时将内嵌的所有 dict 都改成 ObjectDict
    例
    d = {'a': 1, 'b': {'c': 2}}
    dd = ObjectDict(d)
    print(dd.b.c)  => 2
    """
    def __init__(self, *args, **kwargs):
        super(ObjectDict, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for t in arg.items():
                    self[t[0]] = (
                        self.__class__(t[1]) if isinstance(t[1], dict)
                        else t[1])
        if kwargs:
            for t in kwargs.items():
                self[t[0]] = self.__class__(t[1]) if isinstance(t[1], dict) \
                    else t[1]

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            return None

    def __setattr__(self, name, value):
        self[name] = value
