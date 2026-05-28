#!/bin/bash

# Navigate to the project directory
cd ~/orb_core || { echo "Error: Project directory not found."; exit 1; }

# Check if main.py exists before running
if [ -f "main.py" ]; then
    echo "⚡ Initializing Orb Core Workstation..."
    python main.py
else
    echo "❌ Error: main.py not found in ~/orb_core"
    exit 1
fi

#!/bin/bash

# Check if main.py (or your core script) exists right here
if [ -f "main.py" ]; then
    echo "⚡ Initializing Orb Core Workstation..."
    python main.py
else
    echo "❌ Error: Main Python file not found in this directory."
    exit 1
#!/bin/bash

# Check if pro_operator.py exists in this folder
if [ -f "pro_operator.py" ]; then
    echo "⚡ Initializing Orb Core Workstation..."
    python pro_operator.py
else
    echo "❌ Error: pro_operator.py not found in this directory."
    exit 1
fi

fi
