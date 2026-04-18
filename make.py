# make.py
import platform
import subprocess
import sys


def run(cmd):
    subprocess.run(cmd, shell=True, check=True)


def create_venv():
    if platform.system() == "Windows":
        venv_cmd = f"{sys.executable} -m venv venv"
        activate_cmd = "venv\\Scripts\\activate"
        reactivate_msg = f"venv\\Scripts\\activate"
    else:
        venv_cmd = f"{sys.executable} -m venv venv"
        activate_cmd = "source venv/bin/activate"
        reactivate_msg = "source venv/bin/activate"

    print("📦 Creating virtual environment...")
    run(venv_cmd)

    print("\n✅ Virtual environment created!")
    print(f"🔓 To activate it NOW, run:")
    print(f"   {activate_cmd}")
    print(f"\n💡 After closing terminal, reactivate with same command:")
    print(f"   {reactivate_msg}")
    print(f"\n📦 Then run: python make.py setup")


if "init" in sys.argv:
    create_venv()

elif "setup" in sys.argv:
    run(f"{sys.executable} -m pip install -r requirements.txt")

elif "lint" in sys.argv:
    run('isort . --skip venv --skip make.py && black . --exclude "(venv|make.py)" && flake8 . --exclude venv,make.py')

elif "test" in sys.argv:
    run("mypy --ignore-missing-imports run.py config.py app/")

elif "run" in sys.argv:
    run("flask run --debug")

else:
    print("Usage: python make.py [init|setup|test|run]")
    print("  init  - create virtual environment")
    print("  setup - install dependencies")
    print("  test  - run mypy")
    print("  run   - start flask server")
