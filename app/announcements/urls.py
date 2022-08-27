from app.announcements import bp
from app.announcements import views as v


bp.add_url_rule("/", view_func=v.list_announcements)
bp.add_url_rule("/add", view_func=v.add_announcements, methods=['GET', 'POST'])
bp.add_url_rule("/<int:announcement_id>/edit", view_func=v.edit_announcement, methods=['GET', 'POST'])
bp.add_url_rule("/<int:announcement_id>/delete", view_func=v.delete_announcement, methods=['GET', 'POST'])