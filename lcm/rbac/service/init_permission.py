#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf import settings


def init_permission(current_user, request):
    """
    用户权限的初始化
    :param current_user: 当前用户对象
    :param request: 请求相关所有数据
    :return:
    """
    # 2. 权限信息初始化
    # 根据当前用户信息获取此用户所拥有的所有权限，并放入session。
    # 当前用户所有权限

    # 获 用户对应的Role 表中 permission 字段不为空的
    permission_queryset = current_user.roles.filter(permissions__isnull=False).values("permissions__id",
                                                                                      "permissions__title",
                                                                                      "permissions__url",
                                                                                      "permissions__name",
                                                                                      "permissions__pid_id",  # 父权限id
                                                                                      "permissions__pid__title",  # 父权限title
                                                                                      "permissions__pid__url",  # 父权限url
                                                                                      "permissions__menu_id",  # 该权限的菜单id， 不是菜单则为None
                                                                                      "permissions__menu__title",  # 以上
                                                                                      "permissions__menu__icon"  # 以上
                                                                                      ).distinct()
    print(type(permission_queryset))
    print(permission_queryset)

    # 3. 获取权限+菜单信息
    permission_dict = {}

    menu_dict = {}

    for item in permission_queryset:
        permission_dict[item['permissions__name']] = {
            'id': item['permissions__id'],
            'title': item['permissions__title'],
            'url': item['permissions__url'],
            'pid': item['permissions__pid_id'],
            'p_title': item['permissions__pid__title'],
            'p_url': item['permissions__pid__url'],
        }

        menu_id = item['permissions__menu_id']
        if not menu_id:
            continue
        node = {'id': item['permissions__id'], 'title': item['permissions__title'], 'url': item['permissions__url']}

        if menu_id in menu_dict:
            menu_dict[menu_id]['children'].append(node)
        else:
            menu_dict[menu_id] = {
                'title': item['permissions__menu__title'],
                'icon': item['permissions__menu__icon'],
                'children': [node, ]
            }
    print(permission_dict)
    print(menu_dict)

    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.MENU_SESSION_KEY] = menu_dict
# {
#     2: {'title': '用户管理', 'icon': 'fa-id-card-o', 'children': [{'id': 1, 'title': '用户列表', 'url': '/user/list/'}]},
#     1: {'title': '主机管理', 'icon': 'fa-hdd-o', 'children': [{'id': 2, 'title': '主机列表', 'url': '/host/list/'}]},
#     4: {'title': '角色管理', 'icon':'card-o', 'children': [{'id': 26, 'title': '角色列表', 'url': '/rbac/role/list/'}]},
#     3: {'title': '菜单管理', 'icon': 'fa-wrench', 'children': [
#         {'id': 30, 'title': '菜单列表', 'url': '/rbac/menu/list/'},
#         {'id': 37, 'title': '添加权限', 'url': '/rbac/permission/add/(d>\\d+)/'},
#         {'id': 38, 'title': '编辑权限', 'url': '/rbac/permission/edit/(?P<pk>\\d+)/'},
#         {'id': 39, 'title': '删除权限', 'url': '/rbac/permission/del/(?P<pk>\\d+)/'},
#         {'id': 41, 'title': '批量删除权限', 'url': '/rbac/multi/permissions/del/(?P<pk>\\d+)/'}]}, 7: {', 'icon': 'fa-image', 'children': [{'id': 42, 'title': '权限管理', 'url': '/rbac/distribute/permissions/'}]}}
# 
