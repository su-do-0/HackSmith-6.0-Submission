#!/usr/bin/env python3
"""
CMD Command Scraper
Scrapes Windows CMD commands using the built-in help system
"""

import subprocess
import re
import sys

def run_cmd(command):
    """Execute a CMD command and return output"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return None
    except Exception as e:
        print(f"  Error: {e}")
        return None

def escape_python_string(s):
    """Escape string for Python"""
    if not s:
        return ""
    s = str(s)
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    s = s.replace('"', '\\"')
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '')
    return s

def get_all_commands():
    """Get list of all CMD commands from help"""
    print("Getting CMD commands from help...")
    
    output = run_cmd('help')
    if not output:
        return []
    
    # Parse command list from help output
    commands = []
    lines = output.split('\n')
    
    for line in lines:
        # Look for command names (usually at start of line, uppercase)
        match = re.match(r'^([A-Z]+)\s+', line)
        if match:
            cmd = match.group(1).strip()
            if len(cmd) > 1:  # Skip single letters
                commands.append(cmd)
    
    # Add common commands that might not show in help
    additional = ['cls', 'exit', 'echo', 'set', 'path', 'title', 'color', 
                  'date', 'time', 'ver', 'vol', 'label', 'prompt']
    
    for cmd in additional:
        if cmd.upper() not in [c.upper() for c in commands]:
            commands.append(cmd)
    
    commands = sorted(set([c.lower() for c in commands]))
    print(f"Found {len(commands)} commands")
    return commands

def get_command_help(command):
    """Get help for a specific command"""
    # Try multiple methods
    outputs = []
    
    # Method 1: help <command>
    output1 = run_cmd(f'help {command}')
    if output1 and 'not recognized' not in output1.lower():
        outputs.append(output1)
    
    # Method 2: <command> /?
    output2 = run_cmd(f'{command} /?')
    if output2 and 'not recognized' not in output2.lower():
        outputs.append(output2)
    
    # Use longest output
    if outputs:
        return max(outputs, key=len)
    return None

def parse_help_text(help_text):
    """Parse help text to extract description and flags"""
    if not help_text:
        return None, {}
    
    lines = help_text.split('\n')
    
    # Get description (usually first few lines)
    description_lines = []
    for line in lines[:10]:
        clean = line.strip()
        if clean and not clean.startswith('Usage:') and not clean.startswith('['):
            description_lines.append(clean)
            if len(description_lines) >= 3:
                break
    
    description = ' '.join(description_lines)
    if len(description) > 200:
        description = description[:197] + "..."
    
    # Extract flags (lines starting with / or -)
    flags = {}
    for line in lines:
        # Match patterns like "/A" or "/A:attributes"
        match = re.match(r'\s*(/[A-Z][\w:]*|-[a-z][\w]*)\s+(.+)', line, re.IGNORECASE)
        if match:
            flag = match.group(1).strip()
            desc = match.group(2).strip()
            if len(desc) > 150:
                desc = desc[:147] + "..."
            flags[flag] = desc
    
    return description, flags

def generate_examples(command, description, flags):
    """Generate basic examples for a command"""
    examples = []
    
    # Basic usage
    examples.append(f"{command}  # {description[:50] if description else 'Basic usage'}")
    
    # Common patterns
    if command in ['dir']:
        examples.extend([
            "dir /w  # Wide list format",
            "dir /p  # Pause after each screen",
            "dir *.txt  # List only .txt files"
        ])
    elif command in ['copy', 'xcopy']:
        examples.extend([
            f"{command} source.txt dest.txt  # Copy file",
            f"{command} *.txt D:\\backup\\  # Copy multiple files"
        ])
    elif command in ['del', 'erase']:
        examples.extend([
            f"{command} file.txt  # Delete file",
            f"{command} /p *.tmp  # Delete with prompt"
        ])
    elif command in ['cd', 'chdir']:
        examples.extend([
            "cd \\  # Go to root",
            "cd ..  # Go up one level"
        ])
    elif command in ['md', 'mkdir']:
        examples.extend([
            f"{command} newfolder  # Create directory"
        ])
    elif command in ['rd', 'rmdir']:
        examples.extend([
            f"{command} /s folder  # Remove directory and contents"
        ])
    elif command in ['type']:
        examples.extend([
            "type file.txt  # Display file contents"
        ])
    elif command in ['find', 'findstr']:
        examples.extend([
            f'{command} "text" file.txt  # Search in file'
        ])
    elif command in ['echo']:
        examples.extend([
            'echo Hello World  # Print text',
            'echo %PATH%  # Display variable'
        ])
    elif command in ['set']:
        examples.extend([
            'set  # Display all variables',
            'set VAR=value  # Set variable'
        ])
    
    # Add flag examples if available
    if flags and len(examples) < 5:
        for flag in list(flags.keys())[:2]:
            examples.append(f"{command} {flag}  # {flags[flag][:40]}")
    
    return examples[:5]  # Limit to 5 examples

def get_category(command):
    """Categorize command"""
    categories = {
        'File Operations': ['dir', 'copy', 'xcopy', 'move', 'del', 'erase', 'ren', 'rename', 
                           'type', 'more', 'fc', 'comp', 'attrib', 'tree'],
        'Directory Operations': ['cd', 'chdir', 'md', 'mkdir', 'rd', 'rmdir', 'pushd', 'popd'],
        'Disk Operations': ['diskpart', 'format', 'chkdsk', 'label', 'vol'],
        'Text Processing': ['find', 'findstr', 'sort', 'more'],
        'System': ['cls', 'cmd', 'exit', 'ver', 'date', 'time', 'title', 'color', 'prompt'],
        'Environment': ['set', 'path', 'setlocal', 'endlocal'],
        'Network': ['ping', 'ipconfig', 'netstat', 'tracert', 'nslookup', 'net'],
        'Process': ['tasklist', 'taskkill', 'start'],
        'Batch': ['echo', 'rem', 'pause', 'goto', 'if', 'for', 'call'],
    }
    
    for category, commands in categories.items():
        if command.lower() in commands:
            return category
    
    return 'Other'

def main():
    print("=" * 70)
    print("CMD Command Scraper")
    print("=" * 70)
    print()
    
    # Check if running on Windows
    import platform
    if platform.system() != 'Windows':
        print("WARNING: This scraper is designed for Windows CMD")
        print("Some commands may not work on other platforms")
        print()
    
    # Get all commands
    commands = get_all_commands()
    if not commands:
        print("ERROR: Could not get command list")
        sys.exit(1)
    
    total = len(commands)
    print(f"\nProcessing {total} commands...\n")
    
    # Build database
    database = {}
    processed = 0
    skipped = 0
    
    for i, command in enumerate(commands, 1):
        percent = int((i / total) * 100)
        print(f"[{i}/{total}] ({percent}%) {command}")
        
        try:
            # Get help text
            help_text = get_command_help(command)
            
            if not help_text:
                print(f"  Skipped: No help available")
                skipped += 1
                continue
            
            # Parse help
            description, flags = parse_help_text(help_text)
            
            if not description:
                description = f"CMD command: {command}"
            
            # Generate examples
            examples = generate_examples(command, description, flags)
            
            # Get category
            category = get_category(command)
            
            # Build entry
            database[command] = {
                'desc': description,
                'common_flags': flags,
                'examples': examples,
                'category': category
            }
            
            processed += 1
            print(f"  Processed: {len(flags)} flags, {len(examples)} examples")
            
        except KeyboardInterrupt:
            print("\n\nInterrupted by user!")
            break
        except Exception as e:
            print(f"  Error: {e}")
            skipped += 1
    
    # Write to file
    print()
    print("=" * 70)
    print("Writing to file...")
    print("=" * 70)
    
    output_file = "cmd_scraped_database.py"
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # Header
            from datetime import datetime
            f.write('#!/usr/bin/env python3\n')
            f.write('"""\n')
            f.write('CMD Command Database - Auto-generated from help\n')
            f.write(f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
            f.write(f'Total commands: {len(database)}\n')
            f.write('"""\n\n')
            f.write('CMD_COMMAND_DB = {\n')
            
            # Write commands
            cmd_list = list(database.items())
            for i, (cmd_name, cmd_data) in enumerate(cmd_list):
                f.write(f"    '{escape_python_string(cmd_name)}': {{\n")
                f.write(f"        'desc': '{escape_python_string(cmd_data['desc'])}',\n")
                
                # Flags
                f.write(f"        'common_flags': {{\n")
                if cmd_data['common_flags']:
                    flag_items = list(cmd_data['common_flags'].items())
                    for j, (flag, flag_desc) in enumerate(flag_items):
                        comma = ',' if j < len(flag_items) - 1 else ''
                        f.write(f"            '{escape_python_string(flag)}': "
                               f"'{escape_python_string(flag_desc)}'{comma}\n")
                f.write(f"        }},\n")
                
                # Examples
                f.write(f"        'examples': [\n")
                for j, example in enumerate(cmd_data['examples']):
                    comma = ',' if j < len(cmd_data['examples']) - 1 else ''
                    f.write(f"            '{escape_python_string(example)}'{comma}\n")
                f.write(f"        ],\n")
                
                # Category
                f.write(f"        'category': '{cmd_data['category']}'\n")
                
                comma = ',' if i < len(cmd_list) - 1 else ''
                f.write(f"    }}{comma}\n")
            
            f.write('}\n')
        
        print(f"Successfully wrote to {output_file}")
        
        # Validate
        print()
        print("Validating output...")
        try:
            with open(output_file, 'r') as f:
                code = f.read()
            compile(code, output_file, 'exec')
            print("Validation: PASSED")
        except SyntaxError as e:
            print(f"Validation FAILED: {e}")
            sys.exit(1)
        
    except Exception as e:
        print(f"ERROR writing file: {e}")
        sys.exit(1)
    
    # Statistics
    print()
    print("=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print()
    print("Statistics:")
    print(f"  Total commands found: {total}")
    print(f"  Successfully processed: {processed}")
    print(f"  Skipped: {skipped}")
    print()
    print(f"Output file: {output_file}")
    
    import os
    if os.path.exists(output_file):
        size = os.path.getsize(output_file) / 1024
        print(f"  Size: {size:.2f} KB")
    
    print()
    print("Next steps:")
    print(f"  1. Review the file: {output_file}")
    print(f"  2. Copy to cmdhelp directory:")
    print(f"     copy {output_file} cmd_database.py")
    print(f"  3. Test with: python cmdhelp dir")
    print()

if __name__ == '__main__':
    main()
