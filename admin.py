from Web import app, db
from flask_admin import Admin
from Web.models import Category, Product
from flask_admin.contrib.sqla import ModelView


admin = Admin(app=app, name="E-commerce Administration", template_mode='bootstrap4')

admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))