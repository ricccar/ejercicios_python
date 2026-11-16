import pathlib

p = pathlib.Path().resolve()        # Donde estoy
print(p)

mi_path = pathlib.Path("D:\Curso_PY_2026\ejercicios_python")
print(mi_path)
print(mi_path / "clase07")
