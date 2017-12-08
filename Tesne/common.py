#!/usr/bin/env python
# -*- coding:utf-8 -*-
# arthur:Dear
# 2017-12-05 10:18:51


def is_login(session):
    if session:
        def _wrapper(func):
            def __wrapper(*args, **kwargs):
                result = func()
                return result
            return __wrapper
    else:
        print('please login first')
    return _wrapper
