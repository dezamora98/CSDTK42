import os
import sys
import ctypes
import shutil
import subprocess
import tempfile
from git import Repo
import re
from colorama import init, Fore, Style
from utils import Spinner

def get_project_addr(name):
    if name == "." or name == "":
        return os.getcwd()
    else:
        return os.path.abspath(name)
    
def CSDTK42_DIR():
    csdtk42_path = os.getenv("GPRS_CSDTK42_PATH")
    if csdtk42_path is None:
        raise EnvironmentError(
            'GPRS_CSDTK42_PATH variable is not set, please execute "A9GTools install"'
        )
    csdtk42_path = csdtk42_path.replace("\\", "/")
    return csdtk42_path

def make(project_addr, mode = "debug"):
    src_pro = get_project_addr(project_addr)

    if not os.path.exists(src_pro):
        print("The project path does not exist")
        return

    build_path = os.path.join(src_pro, "build")
    pro_name = os.path.basename(os.path.normpath(src_pro)).replace("/", "")
    log_file = f"{build_path}\\{pro_name}.log"
    n_cpu = os.cpu_count()

    if not os.path.exists(build_path):
        os.mkdir(build_path)

    os.environ["USER_CSDTK"] = f"{os.getenv('GPRS_CSDTK42_PATH')}"
    os.environ["CSDTK4INSTALLDIR"] = os.getenv("USER_CSDTK")
    os.environ["ptemp"] = (
        f"{os.getenv('CSDTK4INSTALLDIR')}\\SDK\\platform\\compilation\\win32"
    )
    os.environ["CSDTKVER"] = "4"
    os.environ["CSDTKVERSION"] = "4.2"

    os.environ["CSDTKMAKEDIR"] = f"{os.getenv('CSDTK4INSTALLDIR')}\\make64"
    os.environ["PATH"] = (
        f"{os.getenv('ptemp')};"
        f"{os.getenv('CSDTKMAKEDIR')};"
        f"{os.getenv('CSDTK4INSTALLDIR')}\\perl\\bin;"
        #f"{os.getenv('CSDTK4INSTALLDIR')}\\python27;"
        f"{os.getenv('CSDTK4INSTALLDIR')}\\mips-elf-4.4.2\\bin;"
       # f"{os.getenv('CSDTK4INSTALLDIR')}\\nanopb-0.3.9;"
        f"{os.getenv('PATH')}"
    )

    os.environ["PROJECT_PATH"] = src_pro
    os.environ["SOFT_WORKDIR"] = f"{os.getenv('USER_CSDTK')}\\SDK".replace("\\", "/")
    os.environ["BUILD_PATH"] = build_path.replace("\\", "/")
    os.environ["LOCAL_SHADOW_PATH"] = build_path.replace("\\", "/")
    os.environ["compileMode"] = mode
    os.environ["LOG_FILE"] = log_file
    os.environ["PROJECT_DIR"] = src_pro.replace("\\", "/")
    os.environ["LOCAL_NAME"] = pro_name
    os.environ["PROJ_NAME"] = pro_name
    os.environ["OBJECT_DIR"] = src_pro.replace("\\", "/")
    os.environ["HEX_PATH"] = build_path.replace("\\", "/")

    print(
        f"Project ({os.getenv('LOCAL_NAME')}) => {os.getenv('PROJECT_DIR')}\n"
        f"Compile mode => {os.getenv('compileMode')}\n"
        f"CSDTK({os.getenv('CSDTKVERSION')}) => {os.getenv('USER_CSDTK')}\n"
        f"SOFT_WORKDIR (SDK) => {os.getenv('SOFT_WORKDIR')}\n"
        f"HEX_PATH => {os.getenv('HEX_PATH')}\n"
    )

    os.chdir(os.getenv("SOFT_WORKDIR"))
    os.system(f"make -r -j {n_cpu} CT_RELEASE={mode}  2>&1 | tee %LOG_FILE%")

    def check_compilation_status(log_file_path):
        with open(log_file_path, "rb") as file:
            file_str = file.read()
        patron = re.compile(rb"Combine sucessful*", re.IGNORECASE)
        if re.search(patron, file_str):
            return True
        return False

    if check_compilation_status(log_file):
        map_file_path = f"{build_path}\\{pro_name}.map"
        memd_def_path = f"{os.getenv('USER_CSDTK')}\\SDK\\platform\\csdk\\memd.def"

        # Función para ejecutar un comando y capturar su salida
        def run_command(command):
            result = subprocess.run(
                command, shell=True, stdout=subprocess.PIPE, text=True
            )
            return result.stdout.strip()

        # Obtener los valores necesarios mediante grep y awk
        ram_total = run_command(
            f"grep -n 'USER_RAM_SIZE' {memd_def_path} | gawk '{{print $3}}'"
        )
        rom_total = run_command(
            f"grep -n 'USER_ROM_SIZE' {memd_def_path} | gawk '{{print $3}}'"
        )
        use_ram_size = run_command(
            f"grep -n '__user_rw_size = (__user_rw_end - __user_rw_start)' {map_file_path} | gawk '{{print $2}}'"
        )
        use_rom_size = run_command(
            f"grep -n '__rom_size = (__user_rw_lma - __rom_start)' {map_file_path} | gawk '{{print $2}}'"
        )
        use_rom_bss_size = run_command(
            f"grep -n '__user_bss_size = (__user_bss_end - __user_bss_start)' {map_file_path} | gawk '{{print $2}}'"
        )

        # Convertir los valores a enteros
        ram_total = int(ram_total, 16)
        rom_total = int(rom_total, 16)
        use_ram_size = int(use_ram_size, 16)
        use_rom_size = int(use_rom_size, 16)
        use_rom_bss_size = int(use_rom_bss_size, 16)

        # Calcular los usos de RAM y ROM
        ram_use = use_ram_size + use_rom_bss_size
        rom_use = use_rom_size + use_rom_bss_size

        # Calcular porcentajes de uso
        porcentaje_rom = (rom_use / rom_total) * 100
        porcentaje_ram = (ram_use / ram_total) * 100

        init()

        def obtener_color(porcentaje):
            if porcentaje < 50:
                return Fore.GREEN  # Bajo uso
            elif 50 <= porcentaje < 80:
                return Fore.YELLOW  # Uso moderado
            else:
                return Fore.RED  # Alto uso

        color_rom = obtener_color(porcentaje_rom)
        color_ram = obtener_color(porcentaje_ram)

        # Imprimir los resultados con colores y porcentajes
        print("-------------------------------------------------")
        print(
            f"ROM  total: {rom_total} Bytes  used: {rom_use} Bytes  ({color_rom}{porcentaje_rom:.2f}%{Style.RESET_ALL})"
        )
        print(
            f"RAM  total: {ram_total} Bytes  used: {ram_use} Bytes  ({color_ram}{porcentaje_ram:.2f}%{Style.RESET_ALL})"
        )
        print("-------------------------------------------------")
        
    os.chdir(src_pro)

def run_fota(old_lod_path: str, new_lod_path: str, output_pack_path: str) -> None:
    """
    Create a FOTA from LOD files
    
    Args:
        old_lod_path (str): old LOD path
        new_lod_path (str): new LOD path
        output_pack_path (str): final FOTA path
    """
    if not os.path.exists(old_lod_path) or not os.path.exists(new_lod_path):
        print(f"LOD file {old_lod_path} or {new_lod_path} do not exist")
        return

    print("[OTA] Waiting for making FOTA pack...")
    print("This will take a few minutes...")

    spinner = Spinner()

    try:
        spinner.start()
        tmp_dir = tempfile.mkdtemp(prefix='A9GTools_temp_folder')

        # Generar archivos LOD temporales
        old_ota_lod = os.path.join(tmp_dir, "old_ota_lod.lod")
        new_ota_lod = os.path.join(tmp_dir, "new_ota_lod.lod")

        # Ejecutar comandos de generación LOD
        lodtool = f"{os.getenv('GPRS_CSDTK42_PATH')}\\SDK\\platform\\compilation\\lodtool.py"
        fotaCreate = f"{os.getenv('GPRS_CSDTK42_PATH')}\\SDK\\platform\\compilation\\fota\\fotacreate.exe"

        subprocess.check_call(
            ["python", lodtool, "gen_ota", 
             "--lod", old_lod_path, "--out", old_ota_lod],
            shell=True
        )
        
        subprocess.check_call(
            ["python", lodtool, "gen_ota", 
             "--lod", new_lod_path, "--out", new_ota_lod],
            shell=True
        )

        # Crear paquete FOTA
        subprocess.check_call(
            [fotaCreate, "4194304", "65536",
             old_ota_lod, new_ota_lod, output_pack_path],
            shell=True
        )

    except subprocess.CalledProcessError as e:
        print(f"Error durante la creación del paquete FOTA: {e}")
        raise
    finally:
        # Limpiar directorio temporal
        if os.path.exists(tmp_dir):
            shutil.rmtree(tmp_dir)
        spinner.stop()

def clean_project(project_addr):
    src_pro = get_project_addr(project_addr)

    if not os.path.exists(src_pro):
        print("The project path does not exist")
        return

    if os.path.exists(os.path.join(src_pro, "build")):
        shutil.rmtree(os.path.join(src_pro, "build"))

    os.chdir(src_pro)

def open_coolwatcher():
    subprocess.Popen(
        os.path.join(CSDTK42_DIR(), "cooltools/coolwatcher.exe"),
        shell=True,
        close_fds=True,
    )
    return

def create_project(name, micropython):
    project_dir = os.path.abspath(name)

    try:
        os.makedirs(project_dir, exist_ok=True)
        print(f"Project directory created at: {project_dir}")

        if micropython:
            os.makedirs(os.path.join(project_dir, "lib"), exist_ok=True)
            os.makedirs(os.path.join(project_dir, "tests"), exist_ok=True)
            os.makedirs(os.path.join(project_dir, "config"), exist_ok=True)

            with open(os.path.join(project_dir, "main.py"), "w") as f:
                f.write(
                    "import time\n"
                    "def main():\n"
                    '    print("Hello World!")\n'
                    "    while True:\n"
                    "        time.sleep(1)\n\n"
                    'if __name__ == "__main__":\n'
                    "    main()\n"
                )
            with open(os.path.join(project_dir, "boot.py"), "w") as f:
                f.write("")
            with open(os.path.join(project_dir, "README.md"), "w") as f:
                f.write("")
            print(f"MicroPython project {name} created at {project_dir}")
            os.system(f"code ./{name}")
        else:
            source_dir = os.path.join(CSDTK42_DIR(), "SDK/demo/helloword")
            shutil.copytree(source_dir, project_dir, dirs_exist_ok=True)
            print(
                f"Project {name} created at {project_dir} with content from {source_dir}"
            )
            os.system(f"code ./{name}/.vscode/A9GTools.code-workspace")

    except Exception as e:
        print(f"An error occurred: {e}")

def update_v0():
    try:
        repo_path = CSDTK42_DIR()
        repo = Repo(repo_path)

        assert not repo.bare

        commits_behind = list(repo.iter_commits("HEAD..origin/master"))

        if commits_behind:
            print("Changes for origin/master:")
            for commit in commits_behind:
                print(f"- {commit.hexsha} {commit.message.strip()}")

            user_input = (
                input("Do you want to update the repository? (y/n): ").strip().lower()
            )
            if user_input in ["y", "yes"]:
                try:
                    result = subprocess.run(
                        ["git", "pull", "origin", "master"],
                        cwd=repo_path,
                        text=True,
                        capture_output=True,
                    )
                    if result.returncode == 0:
                        print(
                            f"Repository at {repo_path} has been updated successfully."
                        )
                    else:
                        print(
                            f"Failed to update the repository at {repo_path}. Error details:\n{result.stderr}"
                        )
                except Exception as e:
                    error_message = str(e)
                    print(
                        f"Failed to update the repository at {repo_path}. Error details:\n{error_message}"
                    )
            else:
                print("Update cancelled by the user.")
        else:
            print("No changes to pull.")
    except Exception as e:
        print(f"Failed to update the repository at {repo_path}. Error: {e}")

def install():
    variable_name = "GPRS_CSDTK42_PATH"
    variable_value = os.path.dirname(
        os.path.dirname((os.path.dirname(sys.executable)))
    ).replace("/", "\\")

    # Check if the environment variable already exists and has the same value
    existing_value = os.environ.get(variable_name)
    if existing_value == variable_value:
        print(
            f'The environment variable "{variable_name}" is already set to: {variable_value}'
        )
        return
    elif existing_value:
        print(
            f'The environment variable "{variable_name}" already exists with a different value: {existing_value}'
        )
    else:
        print(f'The environment variable "{variable_name}" does not exist.')

    print("Creating A9GTools environment variables.")

    # Command to set the environment variable at the system level
    command = f'/c setx {variable_name} "{variable_value}" /M'

    # Request elevated permissions and execute the command
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", command, None, 1)

    print(
        "A9Gtools will be ready to use in any project path after closing this terminal."
    )
    input("Press Enter to exit...")  # Wait for user input before exiting
