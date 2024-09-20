import os
import shutil
from datetime import datetime
from pathlib import Path


def create_backup():
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = Path("backups")
    backup_dir.mkdir(parents=True, exist_ok=True)

    backup_path = backup_dir / f"library_backup_{agora}.db"

    db_path = os.path.join('data', 'library.db')

    if db_path:
        shutil.copy(db_path, backup_path)
        print(f"Backup criado com sucesso: {backup_path}")
    else:
        print(f"Erro: O arquivo de banco de dados {db_path} não foi encontrado.")


def clean_backups():
    backup_dir = Path('my_library/backups')

    if backup_dir.exists():
        backups = sorted(backup_dir.glob('*.db'), key=lambda x: x.stat().st_mtime)

        while len(backups) > 5:
            backups[0].unlink()
            backups.pop(0)

        print("Limpeza de backups antigos realizada.")
    else:
        print("Diretório de backups não existe.")