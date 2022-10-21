import json
import base64

from flask import request
from flask import abort
from flask_restful import (
    Resource,  
    reqparse
)

from app import db
from app.api.auth import basic_auth, generate_token, token_auth
from app.models import Announcement, Achievement
from app.api.helpers import remove_html_tags, secure_link as url_for, clickable_links
import app.achievements.roles as achievements_roles


class Login(Resource):
    decorators = [basic_auth.login_required]
    def get(self):
        user = basic_auth.current_user()
        return {
            "token": user.generate_token()
        }


class ActiveUser(Resource):
    decorators = [token_auth.login_required]
    def get(self):
        user = token_auth.current_user()
        return {
            "id": user.id,
            "uid": user.unique_id,
            "username": user.username,
            "name": user.full_name,
            "display_name": user.get_name(),
            "email": user.email
        }


class LogoutUser(Resource):
    decorators = [token_auth.login_required]
    def get(self):
        user = token_auth.current_user()
        user.generate_uid()
        db.session.commit()
        return {
                "message": "OK"
            }


class ImportData(Resource):
    decorators = [token_auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('target', type = str, required = True,
            help = 'Datatype is invalid, consult docs', location = 'json')
        self.reqparse.add_argument('b64data', type = str, required = True,
            help = 'No password provided', location = 'json')
        super().__init__()
    
    def post(self):
        user = token_auth.current_user()
        data = request.get_json()
        if data["target"] == "achievements":
            if user.can_do("achievements", "add"):
                achdata = base64.b64decode(data["b64data"]).decode("utf-8")
                # **data, "d": json.loads(achdata)}
                jdatas = json.loads(achdata)
                for jdata in jdatas:
                    ach = Achievement(
                        title = jdata["title"],
                        body = jdata["body"],
                        user_id = user.id,
                        category = data["achievement"]["category"],
                        region = data["achievement"]["region"],
                    )   
                    db.session.add(ach)
                db.session.commit()
                return "OK"
            else:
                abort(403, "Insufficient privilleges")
        elif data["target"] == "announcements":
            if user.can_do("announcements", "add"):
                adata = base64.b64decode(data["b64data"]).decode("utf-8")
                # **data, "d": json.loads(achdata)}
                jdatas = json.loads(adata)
                for jdata in jdatas:
                    a = Announcement(
                        title = jdata["title"],
                        body = jdata["body"],
                        user_id = user.id,
                    )   
                    db.session.add(a)
                db.session.commit()
                return "OK"
            else:
                abort(403, "Insufficient privilleges")
        else:
            abort(400, "No such target")


class GetAllAnnouncements(Resource):
    def get(self):
        """get 
        
        Get all the announcements, in a JSON form. Then in static site,
        we will add a parser to render like in achievements.
        """
        # return jsonify.
        return_obj = []
        for ann in Announcement.get_all():
            return_obj.append({
                "title" : ann.title,
                "body" : clickable_links(ann.body),
                "timestamp" : ann.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            })
        
        return return_obj


class GetAchievements(Resource):
    def get(self, category, region):
        """get 
        
        Get all the announcements, in a JSON form. Then in static site,
        we will add a parser to render like in achievements.
        """
        # return jsonify.
        return_obj = []
        achs = Achievement.query.filter_by(category=category, region=region)
        for ach in achs:
            return_obj.append({
                "title": ach.title,
                "body": ach.body,
                "timestamp" : ach.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            })
        
        return return_obj


class GetAchievementsShort(Resource):
    def get(self, category, region):
        """get 
        
        Get all the announcements, in a JSON form. Then in static site,
        we will add a parser to render like in achievements.
        """
        # return jsonify.
        noofwords = int(request.args.get("words", "20"))
        return_obj = []
        achs = Achievement.query.filter_by(category=category, region=region)
        for ach in achs:
            return_obj.append({
                "title": ach.title,
                "body": remove_html_tags(" ".join(ach.body.split()[:noofwords + 1])),
                "url": url_for("external.view_achievement", achievement_id=ach.id),
                "timestamp": ach.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            })
        
        return return_obj
    

class GetAllAchievementsShort(Resource):
    def get(self):
        """get 
        
        Get all the announcements, in a JSON form. Then in static site,
        we will add a parser to render like in achievements.
        """
        # return jsonify.
        noofwords = int(request.args.get("words", "20"))
        return_obj = []
        achs = Achievement.query.order_by(Achievement.timestamp.desc())
        for ach in achs:
            return_obj.append({
                "title": ach.title,
                "body": remove_html_tags(" ".join(ach.body.split()[:noofwords + 1])),
                "url": url_for("external.view_achievement", achievement_id=ach.id),
                "timestamp": ach.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            })
        
        return return_obj
