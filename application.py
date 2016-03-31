from flask import Flask, render_template, request, redirect, \
    url_for, flash, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, Items, Users
from flask import session as login_session
import random
import string

# IMPORTS FOR  OAUTH
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('postgresql:///estatecatalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Making an API endpoint (GET request)
# Restaurant Menu JSON
"""@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])


# Menu Item JSON
@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=menuItem.serialize)"""


@app.route('/')
@app.route('/estatecatalog/')
def showCategories():
    categories = session.query(Categories).all()
    return render_template('categories.html', categories=categories)


@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newItem = Categories(
            name=request.form['name'])
        session.add(newItem)
        session.commit()
        flash("new category created!")
        return redirect(url_for('showCategories'))
    else:
        return render_template('newcategory.html')
    # return "This page will be for creating a new category"


@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    # return "This page will be for editing category %s" % category_id
    """if 'username' not in login_session:
        return redirect('/login')"""
    editedCategory=session.query(Categories).filter_by(id = category_id).one()
    # if editedRestaurant.user_id != login_session['user_id']:
        # return "<script>function myFunction() {alert('You are not authorized to edit this restaurant. Please create your own restaurant in order to edit.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            flash('Category Successfully Edited %s' % editedCategory.name)
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category = editedCategory)



@app.route('/category/<int:category_id>/delete/')
def deleteCategory(category_id):
    return "This page will be for deleting category %s" % category_id


@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/list/')
def listCategory(category_id):
    return "This page will list out all items in the category %s" % category_id


@app.route('/category/<int:category_id>/new')
def newItem(category_id):
    return "This page is for creating a new item in the category %s" % category_id


@app.route('/category/<int:category_id>/<int:item_id>/edit/')
def editItem(category_id, item_id):
    return "This page will be for editing item %s in category %s" % (item_id, category_id)


@app.route('/category/<int:category_id>/<int:item_id>/delete/')
def deleteItem(category_id, item_id):
    return "This page will be for deleting item %s in category %s" % (item_id, category_id)


@app.route('/disposition/jhh/')
@app.route('/disposition/jhh/list/')
def jhhItems():
    return "This page is for displaying all items marked for disposition to jhh."


@app.route('/disposition/am/')
@app.route('/disposition/am/list/')
def amItems():
    return "This page is for displaying all items marked for disposition to am."


@app.route('/disposition/mth/')
@app.route('/disposition/mth/list/')
def mthItems():
    return "This page is for displaying all items marked for disposition to mth."


@app.route('/disposition/mah/')
@app.route('/disposition/mah/list/')
def mahItems():
    return "This page is for displaying all items marked for disposition to mah."


@app.route('/disposition/sell/')
@app.route('/disposition/sell/list/')
def sellItems():
    return "This page is for displaying all items marked for sale."


@app.route('/disposition/donate/')
@app.route('/disposition/donate/list/')
def donateItems():
    return "This page is for displaying all items marked to donate."


"""@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)

# Task 1: Create route for newMenuItem function here


@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(
            name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("new menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

# Task 2: Create route for editMenuItem function here


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/',
           methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        flash("menu item has been edited!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template(
            'editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id,
            item=editedItem)

# Task 3: Create a route for deleteMenuItem function here


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/',
           methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deletedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        flash("menu item has been deleted!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template(
            'deletemenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id,
            item=deletedItem)"""


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
