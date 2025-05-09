import os
import shutil

def collect_logs(distro, custom_path, output_dir):
    # Define o caminho padrão para os logs, caso não tenha sido fornecido
    if custom_path:
        logs_path = custom_path
    else:
        logs_path = "/var/log"

    # Lista de logs para serem coletados, incluindo os logs comuns em distribuições baseadas em Linux
    log_files = [
        "auth.log", "kern.log", "syslog", "dmesg", "messages", "apache2/*.log", "nginx/*.log"
    ]
    
    # Adiciona logs padrão da distribuição
    if distro == "debian" or distro == "ubuntu":
        log_files += ["dpkg.log", "cloud-init.log"]

    # Coleta os logs
    print(f"🔍 Coletando logs padrão para {distro}")
    
    for log_file in log_files:
        log_file_path = os.path.join(logs_path, log_file)
        
        # Verifica se o log existe e copia
        if os.path.exists(log_file_path):
            log_file_dest = os.path.join(output_dir, os.path.basename(log_file))
            print(f"📁 Logs de {log_file} copiados para {log_file_dest}")
            if os.path.isdir(log_file_path):
                shutil.copytree(log_file_path, log_file_dest)
            else:
                shutil.copy(log_file_path, log_file_dest)
