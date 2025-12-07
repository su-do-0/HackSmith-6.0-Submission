#!/usr/bin/env python3
"""
JSON to cmdhelp Converter
Converts man_commands.json to Python database format for cmdhelp
"""

import json
import sys

def escape_python_string(s):
    """Escape string for Python code"""
    if not s:
        return ""
    s = str(s)
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    s = s.replace('"', '\\"')
    s = s.replace('\n', '\\n')
    s = s.replace('\r', '')
    return s

def convert_json_to_python(json_file, output_file):
    """Convert JSON commands to Python database format"""
    print(f"📦 Loading {json_file}...")
    
    with open(json_file, 'r') as f:
        commands = json.load(f)
    
    print(f"✓ Loaded {len(commands)} commands")
    print(f"\n📝 Converting to Python format...")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write('#!/usr/bin/env python3\n')
        f.write('"""\n')
        f.write('Comprehensive Linux Command Database\n')
        f.write(f'Converted from JSON - {len(commands)} commands\n')
        f.write('Compatible with cmdhelp\n')
        f.write('"""\n\n')
        f.write('COMPREHENSIVE_COMMAND_DB = {\n')
        
        # Process each command
        for i, (cmd_name, cmd_info) in enumerate(commands.items(), 1):
            if i % 100 == 0:
                print(f"  Processed {i}/{len(commands)}...")
            
            # Get description
            desc = cmd_info.get('desc', f"Command: {cmd_name}").strip()
            desc_escaped = escape_python_string(desc)
            
            # Get flags
            flags = cmd_info.get('common_flags', {})
            
            # Get examples
            examples = cmd_info.get('examples', [])
            
            # Determine category
            category = cmd_info.get('category', 'Other')
            
            # Write command entry
            f.write(f"    '{cmd_name}': {{\n")
            f.write(f"        'desc': '{desc_escaped}',\n")
            
            # Write flags
            f.write(f"        'common_flags': {{\n")
            if flags:
                flag_items = list(flags.items())
                for j, (flag, flag_desc) in enumerate(flag_items):
                    flag_escaped = escape_python_string(flag)
                    flag_desc_escaped = escape_python_string(str(flag_desc))
                    comma = ',' if j < len(flag_items) - 1 else ''
                    f.write(f"            '{flag_escaped}': '{flag_desc_escaped}'{comma}\n")
            f.write(f"        }},\n")
            
            # Write examples
            f.write(f"        'examples': [\n")
            for j, example in enumerate(examples):
                example_escaped = escape_python_string(str(example))
                comma = ',' if j < len(examples) - 1 else ''
                f.write(f"            '{example_escaped}'{comma}\n")
            f.write(f"        ],\n")
            
            # Write category
            f.write(f"        'category': '{category}'\n")
            f.write(f"    }},\n")
        
        # Close dictionary
        f.write('}\n')
    
    print(f"\n✅ Conversion complete!")
    print(f"   Output: {output_file}")
    
    import os
    size_kb = os.path.getsize(output_file) / 1024
    print(f"   Size: {size_kb:.2f} KB")
    print(f"   Commands: {len(commands)}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python json_to_cmdhelp.py <input.json> <output_database.py>")
        print()
        print("Examples:")
        print("  python json_to_cmdhelp.py man_commands.json command_database.py")
        print("  python json_to_cmdhelp.py man_commands_complete.json linux_commands.py")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    convert_json_to_python(input_file, output_file)
    
    print()
    print("🚀 Next steps:")
    print(f"   1. Copy {output_file} to your cmdhelp directory")
    print(f"   2. Use it with cmdhelp:")
    print(f"      python cmdhelp ls")
    print(f"      python cmdhelp grep")

if __name__ == '__main__':
    main()
