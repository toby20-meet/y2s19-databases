from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name,topic,rating):
	knowledge_object = Knowledge(
		name = name,
		topic = topic,
		rating = rating
		)
	session.add(knowledge_object)
	session.commit()
	
def query_all_articles():
	articles = session.query(Knowledge).all()
	print(articles)

def query_article_by_topic(topic):
	types = session.query(Knowledge).filter_by(topic = topic).all()
	return types

def delete_article_by_topic(topic):
	delete_dis = session.query(Knowledge).filter_by(topic = topic).delete()

def delete_all_articles():
	death = session.query(Knowledge).delete()

def edit_article_rating(name, updated_rating):
	up_me = session.query(Knowledge).filter_by(name = name).first()
	up_me.rating = updated_rating	
	session.commit()

delete_all_articles()
query_all_articles()
add_article("Tony","Tonies",10)
query_all_articles()
edit_article_rating("Tony",7)
query_all_articles()

