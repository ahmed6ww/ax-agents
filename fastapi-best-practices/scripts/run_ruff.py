import subprocess
import sys
import shutil

# Ensure ruff is installed
if not shutil.which("ruff"):
    subprocess.run([sys.executable, "-m", "pip", "install", "ruff"], check=True)

# Run cleanup on current directory
# F401: Unused imports, F841: Unused variables
print("🧹 Running Ruff Cleanup...")
subprocess.run(["ruff", "check", "--select", "I,F401,F841", "--fix", "."], check=False)
subprocess.run(["ruff", "format", "."], check=False)
print("✨ Done.")
