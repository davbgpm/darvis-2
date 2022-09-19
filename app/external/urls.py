from app.external import bp
from app.external import routes as v


bp.add_url_rule("/", view_func=v.index, methods=['GET'])
bp.add_url_rule("/achievement/<int:achievement_id>", view_func=v.view_achievement)