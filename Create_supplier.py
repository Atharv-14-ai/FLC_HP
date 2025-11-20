# add_supplier.py
import sys
import os
from app import app, db, User, bcrypt
from datetime import datetime, timezone

# Enable UTF-8 encoding in Windows console
if sys.stdout.encoding != 'utf-8':
    os.system('chcp 65001 > nul')  # Change to UTF-8 code page

USERNAME = "Supplier"
PLAINTEXT = "123"

with app.app_context():
    db.create_all()

    existing = User.query.filter_by(username=USERNAME).first()
    if existing:
        print("User already exists. Updating password for:", USERNAME)
        existing.password = bcrypt.generate_password_hash(PLAINTEXT).decode('utf-8')
        existing.role = 'Supplier'
        existing.created_at = existing.created_at or datetime.now(timezone.utc)
        db.session.commit()
        print(" Password updated for", USERNAME)
    else:
        hashed = bcrypt.generate_password_hash(PLAINTEXT).decode('utf-8')
        u = User(username=USERNAME, password=hashed, role='Supplier', created_at=datetime.now(timezone.utc))
        db.session.add(u)
        db.session.commit()
        print(" Supplier created: Username=", USERNAME, " Password=", PLAINTEXT)