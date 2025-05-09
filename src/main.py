import sys
import os

# Adiciona o diretório raiz (onde está o diretório 'src') ao sys.path dinamicamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import argparse
from pathlib import Path
from src.parser import collect_logs
from src.analyzer import analyze_logs
from src.reporter import generate_html_report

def get_distro():
    try:
        with open("/etc/os-release", "r") as f:
            for line in f:
                if line.startswith("ID="):
                    return line.strip().split("=")[1].strip('"')
    except Exception:
        return "ubuntu"  # fallback padrão

def main():
    parser = argparse.ArgumentParser(description="Ferramenta de análise de logs Linux.")
    parser.add_argument('--distro', help='Informe a distribuição Linux (ex: ubuntu, debian, centos)', default=get_distro())
    parser.add_argument('--custom-path', help='Caminho personalizado para logs', default=None)
    parser.add_argument('--output-dir', help='Diretório de saída para os logs coletados', default="logs_raw")

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    collect_logs(distro=args.distro, custom_path=args.custom_path, output_dir=args.output_dir)

    # Análise dos logs
    log_summary = analyze_logs(args.output_dir)
    
    # Verificar se a análise dos logs trouxe resultados
    if not log_summary:
        print("Nenhum log foi analisado.")
        return

    # Gerar relatório HTML
    generate_html_report(log_summary, args.output_dir)
    print("Relatório HTML gerado com sucesso.")

if __name__ == "__main__":
    main()
