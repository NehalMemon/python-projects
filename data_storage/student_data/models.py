from mongoengine import Document, fields

class Student(Document):
    name = fields.StringField(required=True)
    father_name = fields.StringField(required=True)
    student_id = fields.StringField(required=True)
    contact_number = fields.StringField(required=True)
