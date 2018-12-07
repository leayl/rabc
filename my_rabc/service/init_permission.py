from ..models import User, Menu


def init_permission(request, user):
    """
    初始化用户权限，写入session
    :param request:
    :param user:
    :return:
    """
    # 获取user的所有角色对应的权限的url，title，menu_id字段，values后接字段名
    # 在多对多表中，查询对应多表的字段可以用_直接取值，如下“permission_url”
    permission_item_list = user.roles.values("permissions_url",
                                             "permissions_title",
                                             "permission_menu_id")
    # 用户权限url列表，用于中间件验证用户权限
    permission_url_list = []
    # 用户权限url所属菜单列表[{"title":xxx,"url":xxx,"menu":xxx},{},]
    permission_menu_list = []
    for item in permission_item_list:
        permission_url_list.append(item["permission_url"])
        if item["permission_menu_id"]:
            temp = {"title": item["permission_title"],
                    "url": item["permission_url"],
                    "menu_id": item["permission_menu_id"]}
            permission_menu_list.append(temp)

    # session在存储时，会先对数据进行序列化，因此对于Queryset对象写入session，加list()
    # 转为可序列化对象
    menu_list = list(Menu.objects.values("id", "title", "parent_id"))
    from django.conf import settings
    # 保存用户权限url列表
    request.session[settings.SESSION_PERMISSION_URL_KEY] = permission_url_list
    # 保存权限菜单和所有菜单，用户登录后作菜单展示使用
    request.session[settings.SESSION_MENU_KEY] = {
        settings.ALL_MENU_KEY:menu_list,
        settings.PERMISSION_MENU_KEY:permission_menu_list
    }