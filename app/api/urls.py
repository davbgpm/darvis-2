import app.api.endpoints as e
from app.api import app_api


app_api.add_resource(e.CaptchaGen, "/captcha")
app_api.add_resource(e.Login, "/users/sign_in")
app_api.add_resource(e.ActiveUser, "/users/active")
app_api.add_resource(e.LogoutUser, "/users/active/logout")
app_api.add_resource(e.GetAllAnnouncements, "/announcements")
app_api.add_resource(e.GetAchievements, "/achievements/<string:category>/<string:region>")
app_api.add_resource(e.GetAchievementsShort, "/achievements/<string:category>/<string:region>/truncate")
app_api.add_resource(e.GetAllAchievementsShort, "/achievements/all/truncate")
app_api.add_resource(e.ImportData, "/data")
