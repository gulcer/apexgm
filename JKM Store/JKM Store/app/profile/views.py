from . import profile
from flask import render_template, redirect, session, url_for, g, flash, request, json
from .forms import LoginForm
from flask_login import current_user, login_user, logout_user

from .models import User
@profile.route('/')
def about():
    return render_template("index.html", name = NAME)


@profile.route('/main_page/<int:user_id>/')
def main_page(user_id):
    user = User.objects(user_id = user_id).first()
    return render_template("lc.html", user = user)
NAME = 'Sergey'
@profile.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user is None:
            flash('Invalid username')
            return redirect(url_for('profile.login'))
        login_user(user)
        return redirect(url_for('profile.main_page'))
    return render_template('login.html', form=form)


@profile.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.about'))
#
# @profile.route('/about/')
# @profile.route('/')
# def about():
#     return render_template("about.html", name=NAME)
#
#
# @profile.route('/main_page/')
# def main_page():
#     items = Item.objects[:20]
#     return render_template("shop.html", items=items)
#
#
# @profile.route('/item/<int:it_id>')
# def item(it_id):
#     item = Item.objects(item_id=it_id).first()
#     return render_template("item.html", item=item)
#
#
# @profile.route('/categories/')
# def categories():
#     cat_dict = {}
#     for category in Categories.objects():
#         item = Item.objects(category=category.name).first()
#         cat_dict[category.name] = item.photo_hash
#     return render_template("categories.html", cat_dict=cat_dict)
#
#
# @profile.route('/category/<string:categ>')
# def category(categ):
#     items = Item.objects(category=categ)
#     return render_template("category.html", items=items, category=categ)
#
#
# @profile.route('/add_item/', methods=['GET', 'POST'])
# def add_item():
#     form = AddItem()
#     if form.validate_on_submit():
#
#         if Categories.objects(name=form.category.data):
#             amount = (Categories.objects(name=form.category.data).first())['count']
#             amount = int(amount)
#             Categories.objects(name=form.category.data).update(count=str(amount + 1))
#
#         else:
#             categ = Categories(
#                 name=form.category.data,
#                 count='1'
#             )
#             categ.save()
#
#         item = Item(
#             name=form.name.data,
#             cost=form.cost.data,
#             category=form.category.data,
#             description=form.description.data,
#             photo_hash=form.photo_hash.data
#         )
#         item.save()
#     return render_template("add_item.html", form=form)
