from pathlib import Path

# Start from current working directory (cloned repo root)
project_root = Path.cwd()

# Define relative file structure
structure = [
    ".github/workflows/ci.yml",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "notebooks/1.0-eda.ipynb",
    "src/__init__.py",
    "src/data_processing.py",
    "src/train.py",
    "src/predict.py",
    "src/api/main.py",
    "src/api/pydantic_models.py",
    "tests/test_data_processing.py",
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    ".gitignore",
    "README.md"
]

# Create folders and placeholder files
for item in structure:
    file_path = project_root / item
    file_path.parent.mkdir(parents=True, exist_ok=True)
    if not file_path.exists():
        file_path.touch()
        print(f"Created: {file_path}")
    else:
        print(f"Exists:  {file_path}")

print("\n✅ Project structure is ready.")
