from cx_Freeze import setup, Executable

setup(
	name = "Banco_usuarios EXECUTABLE",
	version = "1.0.0",
	description = ".py to .exe",
	executables = [Executable("Banco de usuarios.py"])
