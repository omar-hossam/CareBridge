from flask import Blueprint, render_template, redirect, url_for, request, flash
from datetime import datetime
from app.models import db, User
from app.forms import SignupForm, LoginForm
from flask_login import login_user
from flask import request


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=['GET', 'POST'])
def signup_user():
    form = SignupForm()
    
    if form.validate_on_submit(): 
        existing_user = User.query.filter(
            (User.email == email) | (User.username == username)
        ).first()
        
        if existing_user:
            flash("Email or username already taken!")
            return redirect(url_for("auth.register"))
            
        new_user = User(username=username, email=email, fullname=fullname)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        flash("Account created successfully ✅")
        return redirect(url_for("main.index"))
    
    return render_template("signup.html", form=form)
    
    
@auth_bp.route("/login", methods=['GET', 'POST'])
def login_user():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if not user or not user.check_password(form.password.data):
            flash("Wrong email or password!")
            return redirect(url_for("auth.login"))
        
        login_user(user, remember=form.remember.data)
        flash("Welcome back! ✅")
        return redirect(url_for("main.index"))
    
    return render_template("login.html", form=form)
    
@auth_bp.route("/api/urgent-help", methods=["POST"])
def urgent_help():
    try:
        data = request.get_json()

        if not data:
            return {
                "status": "error",
                "message": "Invalid JSON body"
            }, 400

        required_fields = ["name", "phone", "location", "emergency_type"]

        for field in required_fields:
            if field not in data or not data[field]:
                return {
                    "status": "error",
                    "message": f"{field} is required"
                }, 400

        print("Urgent Help:", data)

        return {
            "status": "success",
            "message": "Urgent help request submitted",
            "timestamp": datetime.utcnow().isoformat(),
            "data": data
        }, 200

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500