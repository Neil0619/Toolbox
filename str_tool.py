# coding=utf-8

import re


def json_hump2underline(hump_json_str, ptn=r'"\s*(\w+)\s*"\s*:'):
    """
    将命名为驼峰格式的转为下划线
    :param hump_json_str:
    :param ptn 正则pattern
    :return:
    """
    attr_ptn = re.compile(ptn)

    # 使用hump2underline函数作为re.sub函数第二个参数的回调函数
    sub = re.sub(attr_ptn, lambda x: '"' + hump2underline(x.group(1)) + '" :', hump_json_str)
    return sub


def json_underline2hump(underline_json_str):
    """
    将命名为下划线规则的转为驼峰格式
    :param underline_json_str:
    :return:
    """
    attr_ptn = re.compile(r'"\s*(\w+)\s*"\s*:')
    sub = re.sub(attr_ptn, lambda x: '"' + underline2hump(x.group(1)) + '" :', underline_json_str)
    return sub


def underline2hump(underline_str):
    # 这里re.sub()函数第二个替换参数用到了一个匿名回调函数，回调函数的参数x为一个匹配对象，返回值为一个处理后的字符串
    sub = re.sub(r'(_\w)', lambda x: x.group(1)[1].upper(), underline_str)
    return sub


def hump2underline(hunp_str):
    # 匹配正则，匹配小写字母和大写字母的分界位置
    p = re.compile(r'([a-z]|\d)([A-Z])')
    # 这里第二个参数使用了正则分组的后向引用
    sub = re.sub(p, r'\1_\2', hunp_str).lower()
    return sub


def params_underline2hump(underline_url_params):
    """
    将命名为下划线规则的转为驼峰格式
    :param underline_url_params:
    :return:
    """
    attr_ptn = re.compile(r'(\w+)=')
    sub = re.sub(attr_ptn, lambda x: underline2hump(x.group(1)) + '=', underline_url_params)
    return sub
