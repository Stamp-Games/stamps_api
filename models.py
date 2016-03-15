#!/flask/bin/python
# from sqlalchemy import Column, String, Integer, Float
# from db_create import Base
#
#
# class Stamp(Base):
#     __tablename__ = 'stamp'
#     id = Column(Integer, primary_key=True, index=True)
#     state = Column(String(30))
#     state_abbr = Column(String(2))
#     stamp_name = Column(String(100))
#     blurb = Column(String(500))
#     date_issued = Column(String(20))
#     country = Column(String(20))
#     value = Column(Float(10))
#
#     def to_dict(self):
#         return {"id": self.id, "state": self.state,
#                 "state_abbr": self.state_abbr, "stamp_name": self.stamp_name,
#                 "blurb": self.blurb, "date_issued": self.date_issued,
#                 "country": self.country, "value": self.value}
