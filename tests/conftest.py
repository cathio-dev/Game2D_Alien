import os

# Permite rodar os testes sem abrir janela (útil em servidores/CI)
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")