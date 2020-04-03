from django.test import TestCase

# Create your tests here.
p = '/rbac/permission/edit/(?P<pk>\d+)/'
print(p)
ss = "ssss\\d+"
dd = {'id': 39, 'title': '删除权限', 'url': '/rbac/permission/del/(?P<pk>\\d+)/'}
cc = '/rbac/permission/del/(?P<pk>\\d+)/'
print(ss)
print(dd)
print(cc)
