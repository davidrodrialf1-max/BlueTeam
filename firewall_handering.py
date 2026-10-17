# blue_team/firewall_hardening.py
import subprocess
import sys

def apply_firewall_hardening():
    print("=== BLUE TEAM: ENDURECIMIENTO DE FIREWALL (WINDOWS) ===")
    print("[*] Aplicando políticas de seguridad y reglas restrictivas...\n")
    
    # Comandos para interactuar con el Firewall de Windows (netsh)
    commands = [
        # 1. Asegurar que el Firewall esté activo en todos los perfiles (Dominio, Privado, Público)
        'netsh advfirewall set allprofiles state on',
        
        # 2. Bloquear por defecto todo el tráfico de entrada no autorizado
        'netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound',
        
        # 3. Regla opcional: Crear regla para permitir SSH solo cuando sea necesario
        'netsh advfirewall firewall add rule name="Allow_SSH_BlueTeam" dir=in action=allow protocol=TCP localport=22'
    ]
    
    for cmd in commands:
        try:
            print(f"[*] Ejecutando: {cmd}")
            # Se ejecuta con shell=True para enviar el comando a Windows
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print("    [+] Regla aplicada con éxito.")
            else:
                print(f"    [!] Advertencia o requiere Administrador: {result.stderr.strip()}")
        except Exception as e:
            print(f"    [!] Error al aplicar regla: {e}")
            
    print("\n[+] Endurecimiento de Firewall completado.")

if __name__ == "__main__":
    apply_firewall_hardening()