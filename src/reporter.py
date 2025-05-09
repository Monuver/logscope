import os

def generate_html_report(log_summary, output_dir):
    report_path = os.path.join(output_dir, "log_analysis_report.html")
    
    with open(report_path, "w") as f:
        f.write("<html><head><title>Relatório de Análise de Logs</title></head><body>")
        f.write("<h1>Relatório de Análise de Logs</h1>")
        f.write("<table border='1'><tr><th>Arquivo</th><th>ERROR</th><th>WARNING</th></tr>")
        
        for log_file, counts in log_summary.items():
            f.write(f"<tr><td>{log_file}</td><td>{counts.get('ERROR', 0)}</td><td>{counts.get('WARNING', 0)}</td></tr>")
        
        f.write("</table></body></html>")

    print(f"✅ Relatório gerado: {report_path}")
