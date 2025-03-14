import os
from web_summarizer.summarizer import Summarizer

def main():
	"""Execute this script to summarize a webpage"""
	os.system("cls" if os.name == "nt" else "clear")
	while True:
		print("¡Bienvenido al resumidor de páginas web!\n\n")
		summarizer = Summarizer()
		url = input("Escribe la url de la web: ")
		style = input("Escribe el estilo del resumen (Opcional): ")
		if style != "": 
			print("\n" + summarizer.summarize_web(web_url=url) + "\n")
		else:
			print("\n" + summarizer.summarize_web(web_url=url, style=style) + "\n")
		user_response = input("Pulsa cualquier tecla para continuar o escribe 'salir' para terminar.\n")
		if user_response in ["salir", "exit", "quit"]:
			print("Gracias por usar la herramienta!")
			break

if __name__ == "__main__":
    main() 