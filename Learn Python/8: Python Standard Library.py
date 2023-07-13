# Working with Paths

from pathlib import Path
# Path(r"C:\Program Files\Microsoft")
# Path("/usr/local//bin")
# Path()
# Path() / "ecommerce" / "__init__.py"
# Path.home()

path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
print(path.absolute())


# Working with Directories
from pathlib import Path

path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# Working with Files
from pathlib import Path
from time import ctime

path - Path("ecommerce/__init__.py")
print(path.stat())


path.read_text()
