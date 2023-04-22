from flask_restful import Resource, marshal
from app.models.models import Contact
from app import request_api, db
from app.schemas import contact_field
from app.decorator import jwt_required


class Contacts(Resource):
    def get(self):
        contacts = Contact.query.all()
        return marshal(contacts, contact_field, "contacts")
    
    def post(self):
        payload = request_api.only(["name", "cellphone"])
        
        name = payload["name"]
        cellphone = payload["cellphone"]
        
        contact = Contact(name, cellphone)
        
        db.session.add(contact)
        db.session.commit()
        
        return marshal(contact, contact_field, "contact")
    
    @jwt_required
    def put(self, current_user):
        payload = request_api.only(["id", "name", "cellphone"])
        _id = payload["id"]
        name = payload["name"]
        cellphone = payload["cellphone"]
        
        contact = Contact.query.get(_id)
        
        if not contact:
            return {"message": "Contato não existe."}
        
        contact.name = name
        contact.cellphone = cellphone
        
        db.session.add(contact)
        db.session.commit()
        
        return marshal(contact, contact_field, "contact")
    
    @jwt_required
    def delete(self, current_user):
        payload = request_api.only(["id"])
        _id = payload["id"]
        
        contact = Contact.query.get(_id)
        
        if not contact:
            return {"message": "Contato não existe."}
        
        db.session.delete(contact)
        db.session.commit()
        
        return marshal(contact, contact_field, "contact")
        