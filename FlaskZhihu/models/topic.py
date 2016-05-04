# -*- coding: utf-8 -*-
__author__ = 'shn7798'

from FlaskZhihu.extensions import db


class Topic(db.Model):
    __tablename__ = 'topic'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column('create_time', db.DateTime)
    update_time = db.Column('update_time', db.DateTime)
    name = db.Column('name', db.String(60))
    description = db.Column('description', db.String(1024))
    avatar_url = db.Column('avatar_url', db.String(200))

    questions = db.relationship(u'Question', secondary='topic_and_question', backref='topics')
    user_on_topic = db.relationship(u'UserOnTopic', backref='topic')

    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, self.name)



class TopicAndQuestion(db.Model):
    __tablename__ = 'topic_and_question'

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    topic_id = db.Column('topic_id', db.ForeignKey(u'topic.id'), nullable=False, index=True)
    question_id = db.Column('question_id', db.ForeignKey(u'question.id'), nullable=False, index=True)
