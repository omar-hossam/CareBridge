from datetime import datetime, timezone
from decimal import Decimal
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id            = db.Column(db.Integer, primary_key=True)
    fullname 	  = db.Column(db.String(64), nullable=False)
    username      = db.Column(db.String(64),  unique=True, nullable=False)
    email         = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role          = db.Column(db.String(20),  default="donor", nullable=False)  # donor | admin
    is_active     = db.Column(db.Boolean, default=True, nullable=False)
    created_at    = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    @property
    def is_admin(self) -> bool:
        return self.role == "admin"


class Hospital(db.Model):
    __tablename__ = "hospitals"

    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(120), nullable=False)
    email        = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    address      = db.Column(db.String(255), nullable=True)
    is_verified  = db.Column(db.Boolean, default=False, nullable=False)
    is_active    = db.Column(db.Boolean, default=True, nullable=False)
    created_at   = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    requests = db.relationship("HospitalRequest", back_populates="hospital", lazy="dynamic")

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)


class HospitalRequest(db.Model):
    __tablename__ = "hospital_requests"

    id            = db.Column(db.Integer, primary_key=True)
    hospital_id   = db.Column(db.Integer, db.ForeignKey("hospitals.id"), nullable=False)
    title         = db.Column(db.String(140), nullable=False)
    description   = db.Column(db.Text, nullable=False)
    goal_amount   = db.Column(db.Numeric(10, 2), nullable=False)
    raised_amount = db.Column(db.Numeric(10, 2), default=Decimal("0.00"), nullable=False)
    status        = db.Column(db.String(20), default="active", nullable=False)  # active | completed | cancelled
    is_deleted    = db.Column(db.Boolean, default=False, nullable=False)  # soft delete
    created_at    = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    hospital  = db.relationship("Hospital", back_populates="requests")
    donations = db.relationship("Donation", back_populates="hospital_request", lazy="dynamic")
    documents = db.relationship("Document", back_populates="hospital_request", lazy="dynamic")

    @property
    def progress_pct(self) -> float:
        if not self.goal_amount:
            return 0.0
        return float(self.raised_amount / self.goal_amount * 100)


class AnonymousRequest(db.Model):
    __tablename__ = "anonymous_requests"

    id                = db.Column(db.Integer, primary_key=True)
    name              = db.Column(db.String(64),  nullable=True)   # optional
    description       = db.Column(db.Text,         nullable=False)
    goal_amount       = db.Column(db.Numeric(10, 2), nullable=False)
    raised_amount     = db.Column(db.Numeric(10, 2), default=Decimal("0.00"), nullable=False)
    contact_link      = db.Column(db.String(255),  nullable=True)   # full wa.me/... or t.me/... link
    contact_link_hash = db.Column(db.String(256),  nullable=True)   # hashed version, no one reads this
    show_contact      = db.Column(db.Boolean, default=False, nullable=False)  # admin flips this
    status            = db.Column(db.String(20),   default="active", nullable=False)  # active | completed | cancelled
    urgent            = db.Column(db.String(20), default="High", nullable=False)
    is_deleted        = db.Column(db.Boolean, default=False, nullable=False)  # soft delete
    created_at        = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    donations = db.relationship("Donation", back_populates="anonymous_request", lazy="dynamic")
    # documents = db.relationship("Document", back_populates="anonymous_request", lazy="dynamic")
    # the anonymous documents will be sent privately on WhatsApp or Telegram etc..
    
    @property
    def progress_pct(self) -> float:
        if not self.goal_amount:
            return 0.0
        return float(self.raised_amount / self.goal_amount * 100)


class Donation(db.Model):
    __tablename__ = "donations"

    id                   = db.Column(db.Integer, primary_key=True)
    donor_id             = db.Column(db.Integer, db.ForeignKey("users.id"),              nullable=False)
    hospital_request_id  = db.Column(db.Integer, db.ForeignKey("hospital_requests.id"),  nullable=True)
    anonymous_request_id = db.Column(db.Integer, db.ForeignKey("anonymous_requests.id"), nullable=True)
    amount               = db.Column(db.Numeric(10, 2), nullable=False)
    message              = db.Column(db.String(300), nullable=True)
    donated_at           = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Relationships — two-way bridges back to both request types
    donor            = db.relationship("User",            backref="donations")
    hospital_request  = db.relationship("HospitalRequest",  back_populates="donations")
    anonymous_request = db.relationship("AnonymousRequest", back_populates="donations")


class Document(db.Model):
    __tablename__ = "documents"

    id                   = db.Column(db.Integer, primary_key=True)
    filename             = db.Column(db.String(255), nullable=False)  # stored filename on disk
    original_filename    = db.Column(db.String(255), nullable=False)  # original name user uploaded
    hospital_request_id  = db.Column(db.Integer, db.ForeignKey("hospital_requests.id"),  nullable=True)
    anonymous_request_id = db.Column(db.Integer, db.ForeignKey("anonymous_requests.id"), nullable=True)
    uploaded_at          = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships
    hospital_request  = db.relationship("HospitalRequest",  back_populates="documents")
