import os
import shutil
import subprocess

def get_project_addr(name):
    if name == "." or name == "":
        return os.getcwd()
    else:
       return os.path.abspath(name)
    
def build_project(project_addr):
    app_dir = "C:/CSDTK42/SDK/app"

    if os.path.exists(app_dir):
        shutil.rmtree(app_dir)

    os.makedirs(app_dir, exist_ok=True)

    src_pro = get_project_addr(project_addr)
    if not os.path.exists(src_pro):
        print("The project path does not exist")
        return
    
    if not os.path.exists(os.path.join(src_pro,"src/sdk_config.c")):
        print("The project needs the file <projectName>/src/sdk_config.c in order to be built.")
        return

    for item in os.listdir(src_pro):
        item_path =  os.path.join(src_pro, item)

        if item.startswith(".") or item.startswith("hex"):
            continue

        if os.path.isfile(item_path):
            shutil.copy2(item_path, app_dir)
        elif os.path.isdir(item_path):
            shutil.copytree(item_path, os.path.join(app_dir, item)) 

    os.chdir("C:/CSDTK42/SDK/")
    os.system("build.bat app")
    os.chdir(src_pro)

    hex_path = "C:/CSDTK42/SDK/hex" 
    if os.path.exists(hex_path):
        shutil.copytree(hex_path, os.path.join(src_pro,"hex"), dirs_exist_ok=True)
    else: 
        print(f"The directory '{hex_path}' does not exist")

    return 

def clean_project(project_addr):
    src_pro = get_project_addr(project_addr)

    if not os.path.exists(src_pro):
        print("The project path does not exist")
        return

    if os.path.exists(os.path.join(src_pro,"hex")):
        shutil.rmtree(os.path.join(src_pro,"hex"))
    
    os.chdir("C:/CSDTK42/SDK/")
    os.system("build.bat clean all")
    os.chdir(src_pro)
    
    return


def load_project():
    subprocess.Popen(
        "C:/CSDTK42/cooltools/coolwatcher.exe",
        shell=True,
        close_fds=True
        )
    return


def create_project(name):
    project_dir = os.path.abspath(name)  

    source_dir = "C:/CSDTK42/SDK/demo/helloword"

    try:
        # Crear directorio del proyecto
        os.makedirs(project_dir, exist_ok=True)
        print(f"Project directory created at: {project_dir}")

        # Copiar contenido del directorio fuente al directorio del proyecto
        if os.path.exists(source_dir):
            shutil.copytree(source_dir, project_dir, dirs_exist_ok=True)
            print(f"Project {name} created at {project_dir} with content from {source_dir}")
        else:
            print(f"Source directory {source_dir} does not exist")
            
        os.system(f"code ./{name}/.vscode/A9GTools.code-workspace")

    except Exception as e:
        print(f"An error occurred: {e}")

    return



