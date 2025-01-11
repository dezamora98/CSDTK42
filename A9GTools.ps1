param (
    [switch]$install
)

$CSDTK42_PATH = Split-Path -Parent $PSCommandPath

# Check if the install parameter is passed
if ($install) {
    # Check if running as administrator
    $principal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
    if (-not $principal.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)) {
        # Restart script with elevated permissions and install parameter
        Start-Process powershell.exe -ArgumentList "-ExecutionPolicy Bypass -File `"$PSCommandPath`" -Install" -Verb RunAs
        exit
    }

    Write-Output "The environment variable GPRS_CSDTK42_PATH is not defined. Creating it..."
    [Environment]::SetEnvironmentVariable("GPRS_CSDTK42_PATH", $CSDTK42_PATH, [EnvironmentVariableTarget]::Machine)
    Write-Output "Environment variable GPRS_CSDTK42_PATH created with value: $CSDTK42_PATH"
    Write-Output "A9Gtools will be ready to be used in any project path after closing this terminal."
    Read-Host -Prompt "Press Enter to continue..."
    taskkill /IM powershell.exe /F
    exit
}

# Check if the environment variable GPRS_CSDTK42_PATH is defined
if (-not (Test-Path env:GPRS_CSDTK42_PATH)) {
    Write-Output "The environment variables required for A9GTools are not set. Please run the script with the parameter '-install' to set the environment variables."
    exit
}

$VENV_PATH = "$CSDTK42_PATH\A9GTools"
$PYTHON_EXE = "$VENV_PATH\bin\python.exe"
$SCRIPT_PATH = "$VENV_PATH\scripts\main.py"

if (Test-Path $VENV_PATH) {
    & $PYTHON_EXE $SCRIPT_PATH @args
} else {
    Write-Host "A9GTools not found."
}
