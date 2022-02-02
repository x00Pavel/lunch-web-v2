from datetime import datetime
from pyramid.view import view_config
from pyramid.response import Response
from lunch_web import TIME_FORMAT, weekday_name, log
from lunch_web.models.menu import Menu
from lunch_web.models.dishe import Dishe

@view_config(route_name='home', renderer='lunch_web:templates/print.jinja2')
def main_view(request):
    today = datetime.today()
    menus = Menu.get_current_menus(request.dbsession, today)
    if len(menus) == 0:
        log.warning("No menus are found for current day")
        menus = Menu.update_menus(request.dbsession, today)
    
    return {'content': menus}

# @view_config(route_name='home', renderer='lunch_web:templates/print.jinja2')
# def main_view(request):
#     today = datetime.today()
#     try:
#         request.dbsession.query(models.menu.Menu)
#     except:
#         pass
#     menus, cache = contoller.get_menu(today)
#     return {'list': menus,
#             'date': today.strftime(TIME_FORMAT),
#             'weekday': weekday_name[today.weekday()],
#             "cache": cache}
