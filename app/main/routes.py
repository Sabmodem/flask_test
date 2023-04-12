import datetime

from flask import render_template, redirect, url_for, flash
from app.extensions import db
from app.main import bp
from app.main.forms import AppointmentForm
from app.main.models import Appointment


@bp.route('/', methods=['POST', 'GET'])
@bp.route('/index', methods=['POST', 'GET'])
def index():
    return render_template('main/index.html')


@bp.route('/appointment', methods=['POST', 'GET'])
def appointment():
    form = AppointmentForm()
    try:
        if form.validate_on_submit():
            new_appointment = Appointment(
                name=form.name.data,
                phone=form.phone.data,
                direction=form.direction.data,
                doctor=form.doctor.data,
                date=form.date.data,
                time=datetime.time(hour=int(form.time.data[:2]))
            )
            db.session.add(new_appointment)
            print(form.date.data)
            db.session.commit()
            flash('Вы успешно записались на прием', 'success')
            return redirect(url_for('main.appointment'))
    except Exception as e:
        flash(str(e), 'danger')
    return render_template('main/appointment.html', form=form)


@bp.route('/admin', methods=['POST', 'GET'])
def admin():
    appointments = Appointment.query.all()
    return render_template('main/admin.html', appointments=appointments)