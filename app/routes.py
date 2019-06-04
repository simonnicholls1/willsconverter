from flask import render_template, flash, redirect, request
from app import app
from app.forms import ConverterForm

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = ConverterForm()
        form.types.data = ''
        return render_template('converter.html', form=form)
    else:
        form = ConverterForm()
        if form.validate_on_submit():
            print('here')
            if form.types.data == 'Kgs':
                kg = float(form.value.data)
                lbs = float(form.value.data) / 2.20462
                return render_template('converter.html', form=form, conversionKg=kg, conversionLb=round(lbs,2))
            if form.types.data == 'Lbs':
                kg = float(form.value.data) / 0.453592
                lbs = float(form.value.data)
                return render_template('converter.html', form=form, conversionKg=round(kg,2), conversionLb=lbs)
        else:
            flash('Try again big man, something wrong with your numbers...')
            return redirect('/')


