import os
import sys
import time
import json
import platform
from itertools import cycle
from threading import Thread
import subprocess
import ctypes
import shutil
import re
import colorama
import tempfile


class Spinner:
    def __init__(self):
        self.spinner = cycle(["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"])
        self.running = False
        self.thread = None

    def spin(self):
        while self.running:
            sys.stdout.write(next(self.spinner))
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write("\b")

    def start(self):
        self.running = True
        self.thread = Thread(target=self.spin)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
        sys.stdout.write(" \b")


class A9gtools:
    _instance = None
    _config = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(A9gtools, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        try:
            # Get the path of the current script directory
            script_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(script_dir, "config.json")

            # Load the configuration file
            with open(config_path, "r") as file:
                config = json.load(file)

            # Assign the complete configuration
            self._config = config

            # Get the value of GPRS_CSDTK42_PATH
            csdtk_path = os.getenv("GPRS_CSDTK42_PATH")
            if not csdtk_path or not os.path.exists(csdtk_path):
                self.install()
                csdtk_path = os.getenv("GPRS_CSDTK42_PATH")
                if not csdtk_path or not os.path.exists(csdtk_path):
                    print(
                        "Error: The environment variable 'GPRS_CSDTK42_PATH' is not defined or the path does not exist after installation."
                    )
                    sys.exit(1)

            # Update GPRS_CSDTK42_PATH in the configuration
            self._config["GPRS_CSDTK42_PATH"] = csdtk_path

            # Format all config values that reference GPRS_CSDTK42_PATH
            for key, value in self._config.items():
                if isinstance(value, str):
                    self._config[key] = value.format(**self._config)

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def get(self, key):
        try:
            value = self._config[key]
            if value is None:
                raise KeyError
            return value
        except AttributeError:
            print(f"Error: The key '{key}' was not found in the configuration.")
            sys.exit(1)

    def install(self):
        system = platform.system().lower()
        print(system)
        variable_name = "GPRS_CSDTK42_PATH"
        variable_value = os.path.dirname(os.path.dirname(sys.executable))
        variable_value = (
            variable_value.replace("/", "\\") if system == "windows" else variable_value
        )

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

        print("Creating environment variables for A9GTools.")

        if system == "windows":
            # Command to set the environment variable at the system level
            command = f'/c setx {variable_name} "{variable_value}" /M'
            # Request elevated permissions and execute the command
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", "cmd.exe", command, None, 1
            )
        elif system == "linux":
            # Command to set the environment variable at the system level
            subprocess.run(
                [
                    "sudo",
                    "sh",
                    "-c",
                    f'echo "export {variable_name}={variable_value}" >> /etc/environment',
                ],
                check=True,
            )
        else:
            print("Error: A9GTools is not supported on this system.")
            sys.exit()

        print(
            "A9GTools will be ready to use in any project path after closing this terminal."
        )
        input("Press Enter to exit...")  # Wait for user input before exiting

    def _run_command(self, command):
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
        return result.stdout.strip()

    def _get_color(self, porcentaje):
        if porcentaje < 50:
            return colorama.Fore.GREEN  # Bajo uso
        elif 50 <= porcentaje < 80:
            return colorama.Fore.YELLOW  # Uso moderado
        else:
            return colorama.Fore.RED  # Alto uso

    def _get_project_addr(self, name):
        if name == "." or name == "":
            return os.getcwd()
        else:
            return os.path.abspath(name)

    def make(self, project_addr, mode):
        src_pro = self._get_project_addr(project_addr)

        if not os.path.exists(src_pro):
            print("The project path does not exist")
            return

        sdk_config_path = os.path.join(src_pro, "config")
        # dst_sdk_config_path = os.path.join(self.get("SDK_PATH"), 'include/config')

        if not os.path.exists(os.path.join(sdk_config_path, "sdk_config.h")):
            print(
                f"Error: {os.path.join(sdk_config_path, 'sdk_config.h')} does not exist."
            )
            sys.exit(1)

        os.environ["INCLUDE_CONFIG_PATH"] = sdk_config_path.replace("\\", "/")

        # if os.path.exists(dst_sdk_config_path):
        #    shutil.rmtree(dst_sdk_config_path)
        #
        # shutil.copytree(sdk_config_path, dst_sdk_config_path)

        build_path = os.path.join(src_pro, "build")
        pro_name = os.path.basename(os.path.normpath(src_pro)).replace("/", "")
        log_file = f"{build_path}\\{pro_name}.log"

        if not os.path.exists(build_path):
            os.mkdir(build_path)

        os.environ["PATH"] = (
            f"{self.get('ptemp')};"
            f"{self.get('make')};"
            f"{self.get('perl')};"
            f"{self.get('gcc')};"
            f"{os.getenv('PATH')}"
        )

        os.environ["SOFT_WORKDIR"] = self.get("SDK_PATH").replace("\\", "/")
        os.environ["LOG_FILE"] = log_file
        os.environ["PROJ_NAME"] = pro_name
        os.environ["OBJECT_DIR"] = src_pro.replace("\\", "/")
        os.environ["HEX_PATH"] = build_path.replace("\\", "/")
        os.environ["BINARY_PATH"] = f"{os.getenv('HEX_PATH')}/bin"
        os.environ["CT_RELEASE"] = mode

        print(
            f"Project ({pro_name}) => {os.getenv('OBJECT_DIR')}\n"
            f"Compile mode => {mode}\n"
            f"CSDTK({self.get('CSDTK')}) => {self.get('CSDTK_PATH')}\n"
            f"SOFT_WORKDIR (SDK) => {os.getenv('SOFT_WORKDIR')}\n"
            f"BINARY_PATH => {os.getenv('BINARY_PATH')}\n"
        )

        # os.chdir(os.getenv("SOFT_WORKDIR"))
        os.system(f"make -r -j {os.cpu_count()}  2>&1  | tee %LOG_FILE%")

        comp_status = False

        with open(log_file, "rb") as file:
            file_str = file.read()
        patron = re.compile(rb"Combine sucessful*", re.IGNORECASE)
        if re.search(patron, file_str):
            comp_status = True

        if comp_status:
            map_file_path = f"{build_path}\\{pro_name}.map"
            memd_def_path = self.get("memd")

            # Obtener los valores necesarios mediante grep y awk
            ram_total = self._run_command(
                f"grep -n 'USER_RAM_SIZE' {memd_def_path} | gawk '{{print $3}}'"
            )
            rom_total = self._run_command(
                f"grep -n 'USER_ROM_SIZE' {memd_def_path} | gawk '{{print $3}}'"
            )
            use_ram_size = self._run_command(
                f"grep -n '__user_rw_size = (__user_rw_end - __user_rw_start)' {map_file_path} | gawk '{{print $2}}'"
            )
            use_rom_size = self._run_command(
                f"grep -n '__rom_size = (__user_rw_lma - __rom_start)' {map_file_path} | gawk '{{print $2}}'"
            )
            use_rom_bss_size = self._run_command(
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

            colorama.init()

            color_rom = self._get_color(porcentaje_rom)
            color_ram = self._get_color(porcentaje_ram)

            # Imprimir los resultados con colores y porcentajes
            print("-------------------------------------------------")
            print(
                f"ROM  total: {rom_total} Bytes  used: {rom_use} Bytes  ({color_rom}{porcentaje_rom:.2f}%{colorama.Style.RESET_ALL})"
            )
            print(
                f"RAM  total: {ram_total} Bytes  used: {ram_use} Bytes  ({color_ram}{porcentaje_ram:.2f}%{colorama.Style.RESET_ALL})"
            )
            print("-------------------------------------------------")

        os.chdir(src_pro)

    def run_fota(self, old_lod_path: str, new_lod_path: str, output_pack_path: str):
        """
        Create a FOTA from LOD files

        Args:
            old_lod_path (str): old LOD path
            new_lod_path (str): new LOD path
            output_pack_path (str): final FOTA path
        """
        if not os.path.exists(old_lod_path) or not os.path.exists(new_lod_path):
            print(f"The LOD file {old_lod_path} or {new_lod_path} do not exist")
            return

        if not os.path.exists(os.path.dirname(output_pack_path)):
            print(f"The output file addres does not exist ({old_lod_path})")
            return

        print("[OTA] Waiting for making FOTA pack...")
        print("This will take a few minutes...")

        spinner = Spinner()

        try:
            spinner.start()
            tmp_dir = tempfile.mkdtemp(prefix="A9GTools_temp_folder")

            old_ota_lod = os.path.join(tmp_dir, "old_ota_lod.lod")
            new_ota_lod = os.path.join(tmp_dir, "new_ota_lod.lod")

            lodtool = self.get("lodtool")
            fotaCreate = self.get("fotacreate")

            subprocess.check_call(
                [
                    "python",
                    lodtool,
                    "gen_ota",
                    "--lod",
                    old_lod_path,
                    "--out",
                    old_ota_lod,
                ],
                shell=True,
            )

            subprocess.check_call(
                [
                    "python",
                    lodtool,
                    "gen_ota",
                    "--lod",
                    new_lod_path,
                    "--out",
                    new_ota_lod,
                ],
                shell=True,
            )

            # Crear paquete FOTA
            subprocess.check_call(
                [
                    fotaCreate,
                    "4194304",
                    "65536",
                    old_ota_lod,
                    new_ota_lod,
                    output_pack_path,
                ],
                shell=True,
            )

        except:
            print(f"FOTA creation error")
        finally:
            # Limpiar directorio temporal
            if os.path.exists(tmp_dir):
                shutil.rmtree(tmp_dir)
            spinner.stop()

    def clean_project(self, project_addr):
        src_pro = self._get_project_addr(project_addr)

        if not os.path.exists(src_pro):
            print("The project path does not exist")
            return

        if os.path.exists(os.path.join(src_pro, "build")):
            shutil.rmtree(os.path.join(src_pro, "build"))

    def open_coolwatcher(self):
        subprocess.Popen(
            self.get("coolwatcher"),
            shell=True,
            close_fds=True,
        )
        return

    def create_project(self, name, micropython):
        project_dir = self._get_project_addr(name)

        try:
            os.makedirs(project_dir, exist_ok=True)
            print(f"Project directory created at: {project_dir}")

            source_dir = (
                os.path.join(self.get("demo_mp"), "helloword")
                if micropython
                else os.path.join(self.get("demo_c"), "helloword")
            )

            shutil.copytree(source_dir, project_dir, dirs_exist_ok=True)
            print(f"Project {project_dir} created")
            if micropython:
                os.system(f"code {project_dir}")
            else:
                os.system(f"code {project_dir}")

        except Exception as e:
            print(f"An error occurred: {e}")
