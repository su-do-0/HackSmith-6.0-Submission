#!/usr/bin/env python3
"""
Comprehensive Man Page Scraper
Scrapes ALL available man pages on the system
"""

import subprocess
import re
import json
import os
from collections import defaultdict

def get_all_man_commands():
    """Get list of all commands with man pages"""
    print("📦 Finding all commands with man pages...")
    
    commands = set()
    
    # Method 1: Use apropos to get all man pages
    try:
        result = subprocess.run(
            ['apropos', '-s', '1,8', '.'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            for line in result.stdout.split('\n'):
                # Parse lines like: "ls (1) - list directory contents"
                match = re.match(r'^(\S+)\s+\((\d+)\)', line)
                if match:
                    cmd = match.group(1)
                    commands.add(cmd)
        
        print(f"  Method 1 (apropos): Found {len(commands)} commands")
    except Exception as e:
        print(f"  Method 1 failed: {e}")
    
    # Method 2: Scan /usr/bin and /bin directories
    paths = ['/usr/bin', '/bin', '/usr/sbin', '/sbin']
    path_commands = set()
    
    for path in paths:
        if os.path.exists(path):
            try:
                for cmd in os.listdir(path):
                    if os.path.isfile(os.path.join(path, cmd)):
                        # Check if it has a man page
                        result = subprocess.run(
                            ['man', '-w', cmd],
                            capture_output=True,
                            timeout=2
                        )
                        if result.returncode == 0:
                            path_commands.add(cmd)
            except Exception as e:
                print(f"  Error scanning {path}: {e}")
    
    commands.update(path_commands)
    print(f"  Method 2 (PATH scan): Found {len(path_commands)} additional commands")
    
    # Method 3: Get bash built-ins
    try:
        result = subprocess.run(
            ['bash', '-c', 'compgen -c'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            bash_commands = set()
            for cmd in result.stdout.split('\n'):
                cmd = cmd.strip()
                if cmd and not cmd.startswith('.'):
                    # Check if it has a man page
                    result = subprocess.run(
                        ['man', '-w', cmd],
                        capture_output=True,
                        timeout=2
                    )
                    if result.returncode == 0:
                        bash_commands.add(cmd)
            
            commands.update(bash_commands)
            print(f"  Method 3 (bash compgen): Found {len(bash_commands)} additional commands")
    except Exception as e:
        print(f"  Method 3 failed: {e}")
    
    # Method 4: Essential commands list (hardcoded backup)
    essential = [
        'ls', 'cat', 'cp', 'mv', 'rm', 'mkdir', 'rmdir', 'touch', 'chmod', 'chown',
        'grep', 'sed', 'awk', 'cut', 'sort', 'uniq', 'wc', 'head', 'tail', 'tr',
        'find', 'locate', 'which', 'whereis', 'file', 'stat', 'ln', 'readlink',
        'ps', 'top', 'kill', 'killall', 'pkill', 'pgrep', 'nice', 'renice',
        'df', 'du', 'mount', 'umount', 'fdisk', 'parted', 'mkfs', 'fsck',
        'tar', 'gzip', 'gunzip', 'bzip2', 'xz', 'zip', 'unzip', 'compress',
        'ssh', 'scp', 'rsync', 'ftp', 'wget', 'curl', 'nc', 'netstat', 'ping',
        'echo', 'printf', 'test', 'expr', 'bc', 'dc', 'seq', 'yes', 'true', 'false',
        'date', 'cal', 'sleep', 'time', 'timeout', 'watch', 'at', 'cron', 'crontab',
        'bash', 'sh', 'dash', 'zsh', 'tcsh', 'csh', 'ksh',
        'make', 'gcc', 'g++', 'ld', 'as', 'ar', 'nm', 'strip', 'objdump',
        'python', 'python3', 'perl', 'ruby', 'php', 'node', 'java', 'javac',
        'git', 'svn', 'hg', 'cvs', 'diff', 'patch', 'comm', 'cmp',
        'vim', 'vi', 'nano', 'emacs', 'less', 'more', 'most', 'pg',
        'tee', 'xargs', 'parallel', 'basename', 'dirname', 'realpath', 'pwd',
        'env', 'printenv', 'export', 'unset', 'alias', 'unalias', 'source',
        'mkfifo', 'mknod', 'mktemp', 'tempfile',
        'useradd', 'userdel', 'usermod', 'groupadd', 'groupdel', 'passwd', 'su', 'sudo',
        'lsblk', 'blkid', 'lsof', 'lsusb', 'lspci', 'lsmod', 'modprobe',
        'systemctl', 'service', 'journalctl', 'dmesg', 'uname', 'hostname',
        'ifconfig', 'ip', 'route', 'iptables', 'ss', 'nslookup', 'dig', 'host',
        'chroot', 'chgrp', 'id', 'who', 'w', 'whoami', 'groups', 'last', 'lastlog',
        'dd', 'sync', 'eject', 'shred', 'truncate',
        'split', 'csplit', 'join', 'paste', 'expand', 'unexpand', 'column',
        'fmt', 'fold', 'nl', 'pr', 'strings', 'od', 'hexdump', 'xxd',
    ]
    
    for cmd in essential:
        commands.add(cmd)
    
    print(f"  Method 4 (essential list): Ensured {len(essential)} essential commands")
    
    print(f"\n✓ Total unique commands found: {len(commands)}")
    return sorted(list(commands))

def parse_man_page(command):
    """Parse man page for a command"""
    try:
        # Get man page
        result = subprocess.run(
            ['man', command],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode != 0:
            return None
        
        man_text = result.stdout
        
        # Extract NAME section for description
        desc = ""
        name_match = re.search(r'NAME\s+(.*?)(?=\n[A-Z])', man_text, re.DOTALL)
        if name_match:
            name_text = name_match.group(1).strip()
            # Remove command name from description
            desc = re.sub(rf'^{re.escape(command)}\s*[-–—]\s*', '', name_text)
            desc = desc.replace('\n', ' ').strip()
            # Limit length
            if len(desc) > 200:
                desc = desc[:197] + "..."
        
        # Extract OPTIONS/FLAGS section
        flags = {}
        options_match = re.search(r'OPTIONS?\s+(.*?)(?=\n[A-Z][A-Z])', man_text, re.DOTALL | re.IGNORECASE)
        
        if options_match:
            options_text = options_match.group(1)
            # Parse individual options
            # Pattern: -x, --xxx  description
            pattern = r'^\s*((?:-[a-zA-Z0-9]|--[a-zA-Z0-9-]+)(?:,\s*(?:-[a-zA-Z0-9]|--[a-zA-Z0-9-]+))*)\s+(.*?)(?=^\s*-|\Z)'
            
            for match in re.finditer(pattern, options_text, re.MULTILINE | re.DOTALL):
                flag = match.group(1).strip()
                description = match.group(2).strip()
                description = description.replace('\n', ' ')
                description = re.sub(r'\s+', ' ', description)
                
                # Limit description length
                if len(description) > 150:
                    description = description[:147] + "..."
                
                # Take first flag if multiple
                first_flag = flag.split(',')[0].strip()
                
                if first_flag and description:
                    flags[first_flag] = description
                    
                    # Limit to 20 flags
                    if len(flags) >= 20:
                        break
        
        return {
            'desc': desc if desc else f"Command: {command}",
            'flags': flags
        }
        
    except subprocess.TimeoutExpired:
        print(f"  ⚠ Timeout for {command}")
        return None
    except Exception as e:
        print(f"  ⚠ Error parsing {command}: {e}")
        return None

def scrape_all_man_pages(output_file):
    """Scrape all man pages and save to JSON"""
    print("🚀 Comprehensive Man Page Scraper")
    print("=" * 70)
    print()
    
    # Get all commands
    commands = get_all_man_commands()
    
    print(f"\n📝 Scraping man pages for {len(commands)} commands...")
    print("This may take several minutes...\n")
    
    results = {}
    success = 0
    failed = 0
    
    for i, cmd in enumerate(commands, 1):
        if i % 50 == 0:
            print(f"  Progress: {i}/{len(commands)} ({int(i/len(commands)*100)}%)")
        
        # Parse man page
        info = parse_man_page(cmd)
        
        if info:
            results[cmd] = {
                'desc': info['desc'],
                'common_flags': info['flags'],
                'examples': []  # Will be filled by example generator
            }
            success += 1
        else:
            failed += 1
    
    print(f"\n✅ Scraping complete!")
    print(f"  Success: {success}")
    print(f"  Failed: {failed}")
    
    # Save to JSON
    print(f"\n💾 Saving to {output_file}...")
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Get file size
    size_kb = os.path.getsize(output_file) / 1024
    
    print(f"\n{'='*70}")
    print("📊 Statistics:")
    print(f"  Commands scraped: {success}")
    print(f"  Output file: {output_file}")
    print(f"  File size: {size_kb:.2f} KB")
    print(f"\n🎉 Done! Use generate_examples.py to add examples.")

def compare_with_existing(new_file, existing_file):
    """Compare new scrape with existing JSON"""
    print("\n📊 Comparing with existing file...")
    
    with open(new_file, 'r') as f:
        new_data = json.load(f)
    
    with open(existing_file, 'r') as f:
        existing_data = json.load(f)
    
    new_commands = set(new_data.keys())
    existing_commands = set(existing_data.keys())
    
    only_new = new_commands - existing_commands
    only_existing = existing_commands - new_commands
    common = new_commands & existing_commands
    
    print(f"\n  New scrape: {len(new_commands)} commands")
    print(f"  Existing: {len(existing_commands)} commands")
    print(f"  Common: {len(common)}")
    print(f"  Only in new: {len(only_new)}")
    print(f"  Only in existing: {len(only_existing)}")
    
    if only_new:
        print(f"\n  ✓ New commands found ({len(only_new)}):")
        for cmd in sorted(list(only_new))[:20]:
            print(f"    {cmd}")
        if len(only_new) > 20:
            print(f"    ... and {len(only_new) - 20} more")
    
    if only_existing:
        print(f"\n  ⚠ Commands in existing but not found ({len(only_existing)}):")
        for cmd in sorted(list(only_existing))[:20]:
            print(f"    {cmd}")
        if len(only_existing) > 20:
            print(f"    ... and {len(only_existing) - 20} more")

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  {sys.argv[0]} scrape <output_file>")
        print(f"  {sys.argv[0]} compare <new_file> <existing_file>")
        print()
        print("Examples:")
        print(f"  {sys.argv[0]} scrape complete_man_commands.json")
        print(f"  {sys.argv[0]} compare new.json man_commands.json")
        return
    
    command = sys.argv[1]
    
    if command == 'scrape':
        if len(sys.argv) != 3:
            print("Usage: scrape <output_file>")
            return
        scrape_all_man_pages(sys.argv[2])
    
    elif command == 'compare':
        if len(sys.argv) != 4:
            print("Usage: compare <new_file> <existing_file>")
            return
        compare_with_existing(sys.argv[2], sys.argv[3])
    
    else:
        print(f"Unknown command: {command}")

if __name__ == '__main__':
    main()
