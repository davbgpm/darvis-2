from app.fids import bp
from app.fids import routes as v


bp.add_url_rule("/", view_func=v.list_, methods=['GET'])
bp.add_url_rule("/add", view_func=v.add, methods=['GET', 'POST'])
bp.add_url_rule("/<int:id>/edit", view_func=v.edit, methods=['GET', 'POST'])
bp.add_url_rule("/<int:id>/delete", view_func=v.delete, methods=['GET', 'POST'])