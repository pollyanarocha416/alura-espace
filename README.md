####
#sequencia de comandos
python manage.py collectstatic
Pra criar o app: python manage.py startapp galeria
ajuda: python manage.py help
iniciar a venv: .\.venv\Scripts\activate
versoes necessarias: pip freeze
pra que isso seja salvo em um arquivo: pip freeze > requirements.txt
pra que vc nao mande pro git partes sensiveis do codigo: pip install python-dotenv
vc coloca a chave SECRET_KEY la dentro ela nao vai pro git
buscar no gitignore.io o q colocar no gitignore