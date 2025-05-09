import os

def analyze_logs(log_dir):
    log_summary = {}

    # Analisar os logs e contar as ocorrências de ERROR e WARNING
    for root, dirs, files in os.walk(log_dir):
        for file in files:
            log_file_path = os.path.join(root, file)
            if log_file_path.endswith(".gz"):  # Pular arquivos compactados
                continue

            error_count = 0
            warning_count = 0
            
            with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    if 'ERROR' in line:
                        error_count += 1
                    if 'WARNING' in line:
                        warning_count += 1

            log_summary[file] = {"ERROR": error_count, "WARNING": warning_count}

    return log_summary
