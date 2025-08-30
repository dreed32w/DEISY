TOOL_NAME="DIESY"
DEVELOPER="Mohammed Ilkhadry"


echo -e "\e[36m==============================\e[0m"
echo -e "\e[36m       $TOOL_NAME       \e[0m"
echo -e "\e[33m   For $DEVELOPER\e[0m"
echo -e "\e[32mOpen Vulnerability Scanning Tool\e[0m"
echo -e "\e[36m==============================\e[0m"

echo -e "\nChecking required tools...\n"


if ! command -v python3 &> /dev/null; then
    echo "Installing Python3..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt update && sudo apt install -y python3 python3-pip
    fi
fi


if ! command -v nmap &> /dev/null; then
    echo "Installing Nmap..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt update && sudo apt install -y nmap
    fi
fi


echo "Installing Python dependencies..."
python3 -m pip install --quiet pyfiglet termcolor



echo -e "\nLaunching $TOOL_NAME...\n"
python3 diesy.py
