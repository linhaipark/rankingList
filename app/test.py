from app.models import db, Qidian

t1 = Qidian(name='t1', author='linhai')
db.session.add(t1)
db.session.commit()
