def install(self):
    system = platform.system().lower()
    print(f"Detected operating system: {system}")

    variable_name = "GPRS_CSDTK42_PATH"
    variable_value = os.path.dirname(os.path.dirname(sys.executable))
    variable_value = variable_value.replace("/", "\\") if system == "windows" else variable_value

    # Check if the script is running with administrator privileges in Windows
    if system == "windows":
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        except:
            is_admin = False
        if not is_admin:
            print("Administrator privileges are required to modify system environment variables.")
            # Restart the script with elevated privileges
            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                sys.executable,
                " ".join([sys.argv[0]] + sys.argv[1:]),
                None,
                1
            )
            sys.exit()

    # Check if the environment variable already exists and has the same value
    existing_value = os.environ.get(variable_name)
    if existing_value == variable_value:
        print(f'The environment variable "{variable_name}" is already set to: {variable_value}')
    else:
        print(f'Setting the environment variable "{variable_name}"...')

    # Execute command to set the environment variable and update the PATH in a single statement
    if system == "windows":
        # Command to add the environment variable and update the PATH
        command = f'''
        setx {variable_name} "{variable_value}" /M && setx PATH "%PATH%;{variable_value}" /M
        '''
        # Execute the command
        subprocess.run(command, shell=True)
    elif system == "linux":
        # Command to add the environment variable and update the PATH
        command = f'''
        sudo sh -c 'echo "export {variable_name}=\\"{variable_value}\\"" >> /etc/environment && \
        sed -i "/^PATH=/ s|$|:{variable_value}|g" /etc/environment'
        '''
        # Execute the command
        subprocess.run(command, shell=True, executable='/bin/bash')
    else:
        print("Error: A9GTools is not supported on this system.")
        sys.exit()

    print("A9GTools will be ready to use in any project path after restarting the terminal.")
    input("Press Enter to exit...")  # Wait for user input before exiting
    sys.exit()