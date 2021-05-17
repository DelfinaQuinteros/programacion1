from .. import mailsender, db
from flask import current_app, render_template, Blueprint
from flask_mail import Message
from smtplib import SMTPException
from main.models import UsuarioModels, BolsonModels
from main.auth.Decorators import admin_required


def sendMail(to, subject, template, **kwargs):
    msg = Message(subject, sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=to)
    try:
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        result = mailsender.send(msg)
    except SMTPException as e:
        print(str(e))
        return "Mail deliver failed"
    return True


mail = Blueprint('mail', __name__, url_prefix='/mail')


@mail.route('/bolsones_promocion', methods=['POST'])
@admin_required
def bolsones_promocion():
    usuarios = db.session.query(UsuarioModels).filter(UsuarioModels.role == 'cliente').all()
    bolsonesVenta = db.session.query(BolsonModels).filter(BolsonModels.aprobado == 1).all()
    try:
        for usuario in usuarios:
            sent = sendMail([usuario.mail], "Bolsones de la semana", 'bolsones_promocion', usuario=usuario,
                            bolsones=[bolson.nombre for bolson in bolsonesVenta])
    except SMTPException as e:
        print(str(e))
        return "Mail deliver failed"
    return 'Mails enviados', 200
