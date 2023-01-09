from tinydb import TinyDB


db = TinyDB('templates.json')
db.insert({"name": "User form", "email": "email", "phone": "phone"})
db.insert({"name": "Phone message form", "phone": "phone", "message": "text", "date": "date"})
db.insert({"name": "Email message form", "email": "email", "text":  "text", "date": "date"})
db.insert({"name": "Phone call  form", "phone": "phone", "date":  "date"})
db.insert({"name": "Email conference form", "email": "email", "date": "date"})
db.insert({"name": "Publication form", "text":  "text", "date": "date"})
db.insert({"name": "Order form", "date": "date", "email": "email", "phone": "phone", "text":  "text"})
