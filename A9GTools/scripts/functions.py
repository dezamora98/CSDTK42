import os
import sys 
import ctypes
import shutil
import subprocess

def get_project_addr(name):
    if name == "." or name == "":
        return os.getcwd()
    else:
       return os.path.abspath(name)
   
def CSDTK42_DIR():
    csdtk42_path = os.getenv('GPRS_CSDTK42_PATH')
    if csdtk42_path is None: 
        raise EnvironmentError('GPRS_CSDTK42_PATH variable is not set, please execute "A9GTools install"')
    csdtk42_path = csdtk42_path.replace('\\', '/')
    return csdtk42_path

    
def build_project(project_addr):
    app_dir = os.path.join(CSDTK42_DIR(),"SDK/app")

    if os.path.exists(app_dir):
        shutil.rmtree(app_dir)

    os.makedirs(app_dir, exist_ok=True)

    src_pro = get_project_addr(project_addr)
    if not os.path.exists(src_pro):
        print("The project path does not exist")
        return
    
    if not os.path.exists(os.path.join(src_pro,"include/sdk_config.h")):
        print("The project needs the file <projectName>/include/sdk_config.h in order to be built.")
        return
    else:
        shutil.copy2(os.path.join(src_pro,"include/sdk_config.h"),os.path.join(CSDTK42_DIR(),"SDK/include/sdk_config.h"))

    for item in os.listdir(src_pro):
        item_path =  os.path.join(src_pro, item)

        if item.startswith(".") or item.startswith("hex"):
            continue

        if os.path.isfile(item_path):
            shutil.copy2(item_path, app_dir)
        elif os.path.isdir(item_path):
            shutil.copytree(item_path, os.path.join(app_dir, item)) 

    os.chdir(os.path.join(CSDTK42_DIR(),"SDK"))
    os.system("build.bat app")
    os.chdir(src_pro)

    hex_path = os.path.join(CSDTK42_DIR(),"SDK/hex/app")
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
    
    os.chdir(os.path.join(CSDTK42_DIR(),"SDK/"))
    os.system("build.bat clean all")
    if os.path.exists(os.path.join(CSDTK42_DIR(),"SDK/app")):
        shutil.rmtree(os.path.join(CSDTK42_DIR(),"SDK/app"))
    
    os.chdir(src_pro)
    
def open_coolwatcher():
    subprocess.Popen(
        os.path.join(CSDTK42_DIR(),"cooltools/coolwatcher.exe"),
        shell=True,
        close_fds=True
        )
    return

def create_project(name):
    project_dir = os.path.abspath(name)  

    source_dir = os.path.join(CSDTK42_DIR(),"SDK/demo/helloword")

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

def create_fota_pack(project_addr):
    src_pro = get_project_addr(project_addr)
    if not os.path.exists(src_pro):
        print("The project path does not exist")
        return
    
    hex_path = os.path.join(src_pro,"hex")
    if not os.path.exists(os.path.join(hex_path,"app_B2130_debug.lod")):
        print("The project hex file does not exist")
        return

    old_file = os.path.join(hex_path,"app_B2130_debug_old.lod")
    new_file = os.path.join(hex_path,"app_B2130_debug.lod")

    os.rename(new_file, old_file)

    build_project(project_addr)

    if not os.path.exists(new_file):
        print("Error creating FOTA package (new LOD file does not exist)")
        return

    fota_pach = os.path.join(src_pro,"hex/fota.pack")
    os.chdir(os.path.join(CSDTK42_DIR(),"SDK/"))
    os.system(f"build.bat fota {old_file} {new_file} {fota_pach}")
    os.remove(old_file)


