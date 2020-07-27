import os

app_name = input("Name of the app: ")
app_path = input("Path to the app (default is current dir)")

if not app_path: #if app_path == ''
    app_path = os.getcwd()

os.chdir(app_path)

with open("wsgi.py", 'w') as f:
    f.write( '''
        from {app_name} import app
        
        if __name__ == "__main__"
    ''')


os.mkdir(app_name)
os.mkdir(os.path.join(app_name, "templates")

with open()