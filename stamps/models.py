#!/flask/bin/python
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from .database import Base


class Stamp(Base):
    __tablename__ = 'stamps'
    
    id = Column(Integer, primary_key=True, index=True)
    
    stamp_name = Column(String(30))
    stamp_url = Column(String(300))
    blurb = Column(String(500),default='')
    date_issued = Column(String(20),default='')
    value = Column(Float(10), default=0)
    tags = Column(String(1000))

    def to_dict(self):
        return {"id": self.id, 
                "stamp_url": self.stamp_url,
                "stamp_name": self.stamp_name,
                "blurb": self.blurb, 
                "date_issued": self.date_issued,
                "tags": self.tags.split(','), 
                "value": self.value
        }

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(20))
    image = Column(String(500))
    body = Column(String(1024))
    correct_answer = Column(String(100))
    answers = Column(String(1024))
    
    def to_dict(self):
        return {
            "id":self.id,
            "category":self.category,
            "image":self.image,
            "body":self.body,
            "correct answer":self.correct_answer,
            "answers":self.answers.split(',')
            }
        
