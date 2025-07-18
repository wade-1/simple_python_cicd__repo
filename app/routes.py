from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Employee

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@bp.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    position = request.form['position']
    department = request.form['department']
    
    new_employee = Employee(name=name, position=position, department=department)
    db.session.add(new_employee)
    db.session.commit()
    return redirect(url_for('main.index'))