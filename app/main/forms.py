import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TimeField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length
from datetime import datetime
from datetime import time

from app.main.models import Appointment


class AppointmentForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired(), Length(max=64)])
    phone = StringField('Телефон', validators=[DataRequired(), Length(min=11, max=11)])
    direction = SelectField('Направление',
                            choices=[('Поставить пломбу', 'Поставить пломбу'),
                                     ('Профессиональная чистка', 'Профессиональная чистка'),
                                     ('Удаление кариеса', 'Удаление кариеса')],
                            validators=[DataRequired()])
    doctor = SelectField('Врач',
                         choices=[('Игорь Игоревич', 'Игорь Игоревич'),
                                  ('Александр Александрович', 'Александр Александрович')],
                         validators=[DataRequired()])
    date = DateField('Дата записи', validators=[DataRequired()])
    time = SelectField('Время записи',
                       choices=[
                           ('10:00', '10:00'),
                           ('11:00', '11:00'),
                           ('12:00', '12:00'),
                           ('13:00', '13:00'),
                           ('14:00', '14:00'),
                           ('15:00', '15:00'),
                           ('16:00', '16:00'),
                           ('17:00', '17:00'),
                           ('18:00', '18:00'),
                           ('19:00', '19:00'),
                       ],
                       validators=[DataRequired()])
    submit = SubmitField('Записаться')

    def validate_phone(form, field):
        if field.data[0] != '8':
            raise ValidationError('Телефон должен начинаться с цифры 8')

    def validate_date(form, field):
        if field.data < datetime.now().date():
            raise ValidationError('Нельзя записаться на прошедшие даты')

    def validate(self, extra_validators=None):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        if Appointment.query.filter_by(
                date=self.date.data, doctor=self.doctor.data, time=time(hour=int(self.time.data[:2]))
        ).first() is not None:
            raise ValidationError('Кто то уже записан на это время')
        return True
