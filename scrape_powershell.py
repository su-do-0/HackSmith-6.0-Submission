#!/usr/bin/env python3
"""
PowerShell Command Scraper (Python version)
Extracts all PowerShell commands using Get-Help
Works by calling PowerShell and parsing the output
"""

import subprocess
import json
import re
from datetime import datetime

def run_powershell(command):
    """Execute a PowerShell command and return the output"""
    try:
        result = subprocess.run(
            ['powershell', '-Command', command],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        print(f"  ⚠ Timeout executing command")
        return None
    except Exception as e:
        print(f"  ⚠ Error: {e}")
        return None

def escape_python_string(s):
    """Escape string for Python"""
    if not s:
        return ""
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    s = s.replace('"', '\\"')
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '')
    return s

def get_all_commands():
    """Get list of all PowerShell commands"""
    print("📦 Getting all PowerShell commands...")
    
    # Get all cmdlets and functions
    ps_command = """
    Get-Command -CommandType Cmdlet,Function | 
    Where-Object { $_.Name -notlike '*:*' } | 
    Select-Object Name,CommandType | 
    ConvertTo-Json -Compress
    """
    
    output = run_powershell(ps_command)
    if not output:
        return []
    
    try:
        commands = json.loads(output)
        if isinstance(commands, dict):
            commands = [commands]
        
        command_names = [cmd['Name'] for cmd in commands]
        print(f"✓ Found {len(command_names)} commands")
        return command_names
    except json.JSONDecodeError as e:
        print(f"✗ Error parsing JSON: {e}")
        return []

def get_command_help(command_name):
    """Get help information for a specific command"""
    ps_command = f"""
    $help = Get-Help '{command_name}' -ErrorAction SilentlyContinue
    if ($help) {{
        @{{
            Synopsis = $help.Synopsis
            Description = ($help.Description.Text -join ' ')
            Parameters = @($help.Parameters.Parameter | ForEach-Object {{
                @{{
                    Name = $_.Name
                    Description = ($_.Description.Text -join ' ')
                }}
            }})
            Examples = @($help.Examples.Example | ForEach-Object {{
                @{{
                    Code = $_.Code
                    Remarks = ($_.Remarks.Text -join ' ')
                }}
            }})
        }} | ConvertTo-Json -Compress -Depth 3
    }}
    """
    
    output = run_powershell(ps_command)
    if not output or output == '':
        return None
    
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return None

def get_command_aliases(command_name):
    """Get aliases for a command"""
    ps_command = f"""
    Get-Alias | Where-Object {{ $_.Definition -eq '{command_name}' }} | 
    Select-Object -ExpandProperty Name | 
    ConvertTo-Json -Compress
    """
    
    output = run_powershell(ps_command)
    if not output or output == 'null':
        return []
    
    try:
        aliases = json.loads(output)
        if isinstance(aliases, str):
            return [aliases]
        return aliases if aliases else []
    except json.JSONDecodeError:
        return []

def get_category(command_name):
    """Determine category based on verb"""
    category_map = {
        'Get': 'Information Retrieval',
        'Set': 'Configuration',
        'New': 'Creation',
        'Remove': 'Deletion',
        'Add': 'Addition',
        'Clear': 'Clearing',
        'Start': 'Execution',
        'Stop': 'Termination',
        'Restart': 'Restart',
        'Enable': 'Enabling',
        'Disable': 'Disabling',
        'Test': 'Testing',
        'Invoke': 'Invocation',
        'Update': 'Updating',
        'Copy': 'Copy Operations',
        'Move': 'Move Operations',
        'Rename': 'Renaming',
        'Show': 'Display',
        'Import': 'Importing',
        'Export': 'Exporting',
        'Format': 'Formatting',
        'Select': 'Selection',
        'Where': 'Filtering',
        'Sort': 'Sorting',
        'Group': 'Grouping',
        'Measure': 'Measurement',
        'Compare': 'Comparison',
        'ConvertTo': 'Conversion',
        'ConvertFrom': 'Conversion',
        'Out': 'Output',
        'Write': 'Writing',
        'Read': 'Reading',
        'Connect': 'Connection',
        'Disconnect': 'Disconnection',
    }
    
    for verb, category in category_map.items():
        if command_name.startswith(f"{verb}-"):
            return category
    
    return "Other"

def main():
    print("🚀 PowerShell Command Scraper (Python)")
    print("=" * 60)
    print()
    
    # Check if PowerShell is available
    print("🔍 Checking PowerShell availability...")
    test = run_powershell("$PSVersionTable.PSVersion.Major")
    if not test:
        print("✗ PowerShell not found or not accessible")
        print("  Make sure PowerShell is installed and in PATH")
        return
    
    print(f"✓ PowerShell version: {test}")
    print()
    
    # Get all commands
    commands = get_all_commands()
    if not commands:
        print("✗ No commands found")
        return
    
    total = len(commands)
    print()
    
    # Start building the Python file
    output_file = "powershell_scraped_database.py"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write('#!/usr/bin/env python3\n')
        f.write('"""\n')
        f.write('PowerShell Command Database - Auto-generated from Get-Help\n')
        f.write(f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        f.write(f'Total commands: {total}\n')
        f.write('"""\n\n')
        f.write('POWERSHELL_COMMAND_DB = {\n')
        
        processed = 0
        skipped = 0
        
        # Process each command
        for i, command_name in enumerate(commands, 1):
            percent = int((i / total) * 100)
            print(f"[{i}/{total}] ({percent}%) Processing: {command_name}")
            
            try:
                # Get help
                help_info = get_command_help(command_name)
                
                if not help_info:
                    print(f"  ⚠ No help available, skipping")
                    skipped += 1
                    continue
                
                # Get description
                description = help_info.get('Synopsis', '').strip()
                if not description:
                    description = help_info.get('Description', '').strip()
                if not description:
                    description = f"PowerShell cmdlet: {command_name}"
                
                # Limit description length
                if len(description) > 200:
                    description = description[:197] + "..."
                
                description = escape_python_string(description)
                
                # Get category
                category = get_category(command_name)
                
                # Get parameters
                print(f"  📝 Extracting parameters...")
                parameters = {}
                if help_info.get('Parameters'):
                    for param in help_info['Parameters'][:20]:  # Limit to 20
                        param_name = f"-{param['Name']}"
                        param_desc = param.get('Description', '').strip()
                        if param_desc:
                            if len(param_desc) > 150:
                                param_desc = param_desc[:147] + "..."
                            parameters[param_name] = escape_python_string(param_desc)
                
                # Get examples
                print(f"  📚 Extracting examples...")
                examples = []
                if help_info.get('Examples'):
                    for ex in help_info['Examples'][:5]:  # Limit to 5
                        code = ex.get('Code', '').strip()
                        if code:
                            code = code.replace('PS C:\\>', '').strip()
                            remarks = ex.get('Remarks', '').strip()
                            if remarks and len(remarks) < 80:
                                code = f"{code}  # {remarks}"
                            examples.append(escape_python_string(code))
                
                # Get aliases
                aliases = get_command_aliases(command_name)
                
                # Write to file
                f.write(f"    '{command_name}': {{\n")
                f.write(f"        'desc': '{description}',\n")
                
                # Parameters
                f.write(f"        'common_flags': {{\n")
                if parameters:
                    param_items = list(parameters.items())
                    for j, (param_name, param_desc) in enumerate(param_items):
                        comma = ',' if j < len(param_items) - 1 else ''
                        f.write(f"            '{param_name}': '{param_desc}'{comma}\n")
                f.write(f"        }},\n")
                
                # Examples
                f.write(f"        'examples': [\n")
                for j, example in enumerate(examples):
                    comma = ',' if j < len(examples) - 1 else ''
                    f.write(f"            '{example}'{comma}\n")
                f.write(f"        ],\n")
                
                # Aliases
                f.write(f"        'alias': [")
                if aliases:
                    alias_str = ', '.join([f"'{a}'" for a in aliases])
                    f.write(alias_str)
                f.write("],\n")
                
                # Category
                f.write(f"        'category': '{category}'\n")
                f.write(f"    }},\n\n")
                
                processed += 1
                print(f"  ✓ Processed successfully")
                
            except Exception as e:
                print(f"  ✗ Error: {e}")
                skipped += 1
        
        # Close the dictionary
        f.write("}\n")
    
    print()
    print("=" * 60)
    print("✅ COMPLETE!")
    print("=" * 60)
    print()
    print("📊 Statistics:")
    print(f"  Total commands found: {total}")
    print(f"  Successfully processed: {processed}")
    print(f"  Skipped: {skipped}")
    print()
    print(f"📁 Output file: {output_file}")
    
    import os
    if os.path.exists(output_file):
        size = os.path.getsize(output_file) / 1024
        print(f"  Size: {size:.2f} KB")
    
    print()
    print("🔧 Next steps:")
    print("  1. Review the generated file")
    print("  2. Copy to your cmdhelp directory")
    print("  3. Replace powershell_database.py")
    print("  4. Test with: python cmdhelp Get-Process")
    print()

if __name__ == '__main__':
    main()
