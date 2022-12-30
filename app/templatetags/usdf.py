from django import template
register=template.Library()


def mahesh(value):
    return value.swapcase()
register.filter('mahesh',mahesh)

def banu(value,arg):
    return value.count(arg)
register.filter('banu',banu)


def dilip(value,arg):
    return value.replace(arg,'k')
register.filter('dilip',dilip)