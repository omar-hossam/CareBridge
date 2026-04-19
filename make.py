import platform
import subprocess
import sys

def run(cmd, shell=False):
    if isinstance(cmd, str) and shell:
        subprocess.run(cmd, shell=True, check=True)
    else:
        subprocess.run(cmd, check=True)


def create_venv():
    print("📦 Creating virtual environment...")

    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to create virtual environment.")
        sys.exit(1)

    print("✅ Virtual environment created successfully!")

    if platform.system() == "Windows":
        activate_cmd = "venv\\Scripts\\activate"
        reactivate_msg = "venv\\Scripts\\activate"
    else:
        activate_cmd = "source venv/bin/activate"
        reactivate_msg = "source venv/bin/activate"

    print(f"\n🔓 To activate it NOW, run:")
    print(f"   {activate_cmd}")
    print(f"\n💡 After closing the terminal, reactivate with:")
    print(f"   {reactivate_msg}")
    print(f"\n📦 Then run: python make.py setup")


if "init" in sys.argv:
    create_venv()

elif "setup" in sys.argv:
    print("📦 Installing dependencies...")
    run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

elif "lint" in sys.argv:
    run("isort . --skip venv --skip make.py && black . --exclude \"(venv|make.py)\" && flake8 . --exclude venv,make.py", shell=True)

elif "test" in sys.argv:
    run("mypy --ignore-missing-imports run.py config.py app/", shell=True)

elif "run" in sys.argv:
    run("flask run --debug", shell=True)

else:
    print("Usage: python make.py [init|setup|lint|test|run]")
    print("  init  - create virtual environment")
    print("  setup - install dependencies")
    print("  lint  - run linter")
    print("  test  - run mypy")
    print("  run   - start flask server")