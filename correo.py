#!/usr/bin/python
from flask import Flask 
from flask import request
import smtplib
from email.MIMEText import MIMEText

app = Flask(__name__) 
@app.route('/correo') 
def correo():
	parametro = request.args.get('param','no contiene numero')

	if(int(parametro) == 1):
		emisor="arqui1seccionb2s@gmail.com"
		receptor="arqui1seccionb2s@gmail.com"
		mensaje=MIMEText("Huella No Valida, Primer intento fallido") 
		mensaje['From']=emisor
		mensaje['To']=receptor
		mensaje['Subject']="[SeguridadHogar]_HuellaIncorrecta"
		serverSMTP=smtplib.SMTP('smtp.gmail.com',587)
		serverSMTP.ehlo()
		serverSMTP.starttls()
		serverSMTP.ehlo()
		serverSMTP.login(emisor,"arqui1seccionb")
		serverSMTP.sendmail(emisor, receptor, mensaje.as_string())
		serverSMTP.close()
		return 'Intento Fallido 1'
	elif(int(parametro) == 2):
		emisor="arqui1seccionb2s@gmail.com"
		receptor="arqui1seccionb2s@gmail.com"
		mensaje=MIMEText("Huella No Valida, Segundo intento fallido") 
		mensaje['From']=emisor
		mensaje['To']=receptor
		mensaje['Subject']="[SeguridadHogar]_HuellaIncorrecta"
		serverSMTP=smtplib.SMTP('smtp.gmail.com',587)
		serverSMTP.ehlo()
		serverSMTP.starttls()
		serverSMTP.ehlo()
		serverSMTP.login(emisor,"arqui1seccionb")
		serverSMTP.sendmail(emisor, receptor, mensaje.as_string())
		serverSMTP.close()
		return 'Intento Fallido 2'
	elif(int(parametro) == 3):
		emisor="arqui1seccionb2s@gmail.com"
		receptor="arqui1seccionb2s@gmail.com"
		mensaje=MIMEText("Huella No Valida, Tercer intento fallido, CASA BLOQUEADA") 
		mensaje['From']=emisor
		mensaje['To']=receptor
		mensaje['Subject']="[SeguridadHogar]_HuellaIncorrecta"
		serverSMTP=smtplib.SMTP('smtp.gmail.com',587)
		serverSMTP.ehlo()
		serverSMTP.starttls()
		serverSMTP.ehlo()
		serverSMTP.login(emisor,"arqui1seccionb")
		serverSMTP.sendmail(emisor, receptor, mensaje.as_string())
		serverSMTP.close()
		return 'Intento Fallido 3, CASA BLOQUEADA'
	elif(int(parametro) == 4):
		emisor="arqui1seccionb2s@gmail.com"
		receptor="arqui1seccionb2s@gmail.com"
		mensaje=MIMEText("Huella Valida, CASA DESBLOQUEADA") 
		mensaje['From']=emisor
		mensaje['To']=receptor
		mensaje['Subject']="[SeguridadHogar]_HuellaCorrecta"
		serverSMTP=smtplib.SMTP('smtp.gmail.com',587)
		serverSMTP.ehlo()
		serverSMTP.starttls()
		serverSMTP.ehlo()
		serverSMTP.login(emisor,"arqui1seccionb")
		serverSMTP.sendmail(emisor, receptor, mensaje.as_string())
		serverSMTP.close()
		return 'CASA DESBLOQUEADA'
	else:
		return 'Faltan Datos'

if __name__ == '__main__':
			app.run(debug = True, host= '0.0.0.0', port = 8080)
