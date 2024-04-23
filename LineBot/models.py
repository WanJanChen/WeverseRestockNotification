from mongoengine import (Document, StringField, ListField, ReferenceField, IntField)

class Product(Document):
  SaleId = StringField(required=True)
  ArtistId = StringField(required=True)
  Name = StringField(required=True)
  TempStatus = StringField(default="")
  Status = StringField()
  
class User(Document):
  Account = StringField(required=True)
  ProductList = ListField(ReferenceField(Product)) 
  ProductListCount = IntField(default=0)

