import subprocess
import sys
from pathlib import Path

def run(cmd):
    print(f"\n$ {' '.join(cmd)}")
    subprocess.check_call(cmd)

if __name__ == "__main__":
    try:
        repo_root = Path(__file__).resolve().parent.parent
        tf_dir = repo_root / "terraform"
        run(["terraform", f"-chdir={tf_dir}", "destroy", "-auto-approve"])
    except subprocess.CalledProcessError as exc:
        print(f"Command failed: {exc}")
        sys.exit(exc.returncode)
