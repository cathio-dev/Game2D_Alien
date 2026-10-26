# Game2D_Alien
Projeto realizado em aula durante a disciplina AQS (Alta Qualidade em Software).

## Como executar
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python src/alien_invasion_refactored.py
```
Controles: setas ← → movem a nave e a barra de espaço atira.

## Testes e cobertura
```bash
pytest -v
coverage run -m pytest
coverage report
```