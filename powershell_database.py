#!/usr/bin/env python3
"""
PowerShell Command Database
Comprehensive documentation for PowerShell commands
"""

POWERSHELL_COMMAND_DB = {
    # File and Directory Management
    'Get-ChildItem': {
        'desc': 'Get items in a location (like ls/dir)',
        'common_flags': {
            '-Path': 'Specifies a path to one or more locations',
            '-Recurse': 'Gets items in all subdirectories',
            '-Force': 'Shows hidden and system files',
            '-File': 'Gets only files',
            '-Directory': 'Gets only directories',
            '-Filter': 'Specifies a filter to qualify the Path',
            '-Include': 'Includes only the specified items',
            '-Exclude': 'Excludes the specified items',
            '-Name': 'Gets only the names of items',
            '-Depth': 'Specifies recursion depth'
        },
        'examples': [
            'Get-ChildItem                    # List current directory',
            'Get-ChildItem -Recurse           # List recursively',
            'Get-ChildItem -Filter *.txt      # List .txt files',
            'Get-ChildItem -Directory         # List only directories',
            'gci -Recurse -Force              # Alias: show all including hidden'
        ],
        'alias': ['gci', 'ls', 'dir']
    },
    'Set-Location': {
        'desc': 'Set the current working location (like cd)',
        'common_flags': {
            '-Path': 'Specifies the path to the new location',
            '-PassThru': 'Returns a PathInfo object',
            '-StackName': 'Specifies a location stack'
        },
        'examples': [
            'Set-Location C:\\Windows          # Change directory',
            'Set-Location ..                  # Go up one level',
            'cd ~                             # Go to home directory'
        ],
        'alias': ['cd', 'chdir', 'sl']
    },
    'Copy-Item': {
        'desc': 'Copy an item from one location to another',
        'common_flags': {
            '-Path': 'Specifies the path to items being copied',
            '-Destination': 'Specifies the path to the new location',
            '-Recurse': 'Copies all subdirectories and files',
            '-Force': 'Forces the command to run without confirmation',
            '-Container': 'Preserves container objects',
            '-Filter': 'Specifies a filter',
            '-Include': 'Specifies items to copy',
            '-Exclude': 'Specifies items to exclude'
        },
        'examples': [
            'Copy-Item file.txt backup.txt         # Copy file',
            'Copy-Item -Path C:\\Source -Destination C:\\Dest -Recurse  # Copy folder',
            'copy file.txt D:\\                    # Copy to different drive'
        ],
        'alias': ['copy', 'cp', 'cpi']
    },
    'Move-Item': {
        'desc': 'Move an item from one location to another',
        'common_flags': {
            '-Path': 'Specifies the path to items being moved',
            '-Destination': 'Specifies the path to the new location',
            '-Force': 'Forces the command without confirmation',
            '-Filter': 'Specifies a filter',
            '-Include': 'Specifies items to move',
            '-Exclude': 'Specifies items to exclude'
        },
        'examples': [
            'Move-Item file.txt C:\\Dest           # Move file',
            'Move-Item *.log C:\\Logs              # Move all .log files',
            'mv oldname.txt newname.txt          # Rename file'
        ],
        'alias': ['move', 'mv', 'mi']
    },
    'Remove-Item': {
        'desc': 'Delete files and folders',
        'common_flags': {
            '-Path': 'Specifies a path to items being removed',
            '-Recurse': 'Deletes items in subdirectories',
            '-Force': 'Forces deletion of read-only/hidden items',
            '-Confirm': 'Prompts for confirmation',
            '-WhatIf': 'Shows what would happen',
            '-Include': 'Specifies items to remove',
            '-Exclude': 'Specifies items to exclude'
        },
        'examples': [
            'Remove-Item file.txt                 # Delete file',
            'Remove-Item -Path C:\\Folder -Recurse  # Delete folder and contents',
            'del *.tmp                            # Delete all .tmp files'
        ],
        'alias': ['del', 'erase', 'rd', 'rm', 'rmdir', 'ri']
    },
    'New-Item': {
        'desc': 'Create a new item (file or directory)',
        'common_flags': {
            '-Path': 'Specifies the path of the new item',
            '-ItemType': 'Specifies the type (File, Directory)',
            '-Value': 'Specifies the value of the new item',
            '-Force': 'Forces creation'
        },
        'examples': [
            'New-Item -ItemType File -Path file.txt     # Create file',
            'New-Item -ItemType Directory -Path NewDir  # Create directory',
            'ni test.txt                                # Create empty file'
        ],
        'alias': ['ni']
    },
    'Rename-Item': {
        'desc': 'Rename an item',
        'common_flags': {
            '-Path': 'Specifies the path to the item',
            '-NewName': 'Specifies the new name',
            '-Force': 'Forces renaming',
            '-PassThru': 'Returns object representing renamed item'
        },
        'examples': [
            'Rename-Item file.txt newfile.txt    # Rename file',
            'ren oldname.txt newname.txt         # Rename using alias'
        ],
        'alias': ['ren', 'rni']
    },
    
    # Text Processing and Search
    'Select-String': {
        'desc': 'Search for text patterns in strings and files (like grep)',
        'common_flags': {
            '-Pattern': 'Specifies the text to find',
            '-Path': 'Specifies files to search',
            '-CaseSensitive': 'Makes search case-sensitive',
            '-SimpleMatch': 'Uses simple string matching',
            '-Quiet': 'Returns boolean instead of matches',
            '-Context': 'Captures lines before/after match',
            '-List': 'Returns only first match per file',
            '-NotMatch': 'Finds lines that do not match'
        },
        'examples': [
            'Select-String -Path *.log -Pattern "error"      # Search in files',
            'Get-Content file.txt | Select-String "pattern"  # Search in content',
            'sls -Pattern "error" -Path *.log -Recurse       # Recursive search'
        ],
        'alias': ['sls']
    },
    'Get-Content': {
        'desc': 'Get the content of a file (like cat)',
        'common_flags': {
            '-Path': 'Specifies the path to items',
            '-TotalCount': 'Gets specified number of lines',
            '-Tail': 'Gets specified number of lines from end',
            '-Wait': 'Waits for new content (like tail -f)',
            '-Raw': 'Returns entire content as single string',
            '-Encoding': 'Specifies file encoding'
        },
        'examples': [
            'Get-Content file.txt                 # Display file content',
            'Get-Content file.txt -TotalCount 10  # First 10 lines',
            'Get-Content file.txt -Tail 20        # Last 20 lines',
            'Get-Content log.txt -Wait            # Follow file (tail -f)',
            'gc file.txt                          # Using alias'
        ],
        'alias': ['cat', 'gc', 'type']
    },
    'Set-Content': {
        'desc': 'Write or replace content in a file',
        'common_flags': {
            '-Path': 'Specifies the path to items',
            '-Value': 'Specifies the new content',
            '-Force': 'Overrides read-only attribute',
            '-Encoding': 'Specifies file encoding'
        },
        'examples': [
            'Set-Content file.txt "Hello World"   # Write to file',
            '"Line 1" | Set-Content file.txt      # Write via pipeline',
            'sc file.txt "Content"                # Using alias'
        ],
        'alias': ['sc']
    },
    'Add-Content': {
        'desc': 'Append content to a file',
        'common_flags': {
            '-Path': 'Specifies the path to items',
            '-Value': 'Specifies the content to add',
            '-Force': 'Overrides read-only attribute',
            '-Encoding': 'Specifies file encoding'
        },
        'examples': [
            'Add-Content file.txt "New line"      # Append to file',
            '"Another line" | Add-Content file.txt # Append via pipeline',
            'ac file.txt "Text"                   # Using alias'
        ],
        'alias': ['ac']
    },
    'Out-File': {
        'desc': 'Send output to a file',
        'common_flags': {
            '-FilePath': 'Specifies the path to the output file',
            '-Append': 'Appends to existing content',
            '-Force': 'Overwrites read-only files',
            '-Encoding': 'Specifies file encoding',
            '-Width': 'Specifies line width',
            '-NoClobber': 'Prevents overwriting existing files'
        },
        'examples': [
            'Get-Process | Out-File processes.txt     # Output to file',
            'dir | Out-File -Append log.txt           # Append output',
            'command | out file.txt                   # Using alias'
        ],
        'alias': ['out']
    },
    
    # Process Management
    'Get-Process': {
        'desc': 'Get processes running on local or remote computer',
        'common_flags': {
            '-Name': 'Specifies process names',
            '-Id': 'Specifies process IDs',
            '-ComputerName': 'Specifies remote computers',
            '-Module': 'Gets modules loaded by processes',
            '-FileVersionInfo': 'Gets file version info'
        },
        'examples': [
            'Get-Process                          # List all processes',
            'Get-Process -Name chrome             # Get specific process',
            'Get-Process | Sort-Object CPU -Descending  # Sort by CPU',
            'gps chrome                           # Using alias'
        ],
        'alias': ['gps', 'ps']
    },
    'Stop-Process': {
        'desc': 'Stop one or more running processes',
        'common_flags': {
            '-Name': 'Specifies process names',
            '-Id': 'Specifies process IDs',
            '-Force': 'Stops without confirmation',
            '-PassThru': 'Returns object representing process'
        },
        'examples': [
            'Stop-Process -Name notepad           # Stop by name',
            'Stop-Process -Id 1234                # Stop by ID',
            'Get-Process chrome | Stop-Process    # Stop via pipeline',
            'kill -Name chrome                    # Using alias'
        ],
        'alias': ['kill', 'spps']
    },
    'Start-Process': {
        'desc': 'Start one or more processes',
        'common_flags': {
            '-FilePath': 'Specifies the program to run',
            '-ArgumentList': 'Specifies parameters/arguments',
            '-WorkingDirectory': 'Specifies working directory',
            '-Verb': 'Specifies action (RunAs for admin)',
            '-WindowStyle': 'Specifies window state',
            '-Wait': 'Waits for process to complete',
            '-PassThru': 'Returns process object'
        },
        'examples': [
            'Start-Process notepad                # Start notepad',
            'Start-Process powershell -Verb RunAs # Run as admin',
            'Start-Process cmd -ArgumentList "/c", "dir"  # With arguments',
            'saps notepad                         # Using alias'
        ],
        'alias': ['saps', 'start']
    },
    
    # Service Management
    'Get-Service': {
        'desc': 'Get the status of services',
        'common_flags': {
            '-Name': 'Specifies service names',
            '-DisplayName': 'Specifies display names',
            '-ComputerName': 'Gets services on remote computer',
            '-DependentServices': 'Gets dependent services',
            '-RequiredServices': 'Gets required services'
        },
        'examples': [
            'Get-Service                          # List all services',
            'Get-Service -Name w32time            # Get specific service',
            'Get-Service | Where-Object {$_.Status -eq "Running"}  # Running only',
            'gsv                                  # Using alias'
        ],
        'alias': ['gsv']
    },
    'Start-Service': {
        'desc': 'Start one or more stopped services',
        'common_flags': {
            '-Name': 'Specifies service names',
            '-DisplayName': 'Specifies display names',
            '-PassThru': 'Returns service object'
        },
        'examples': [
            'Start-Service -Name w32time          # Start service',
            'Start-Service -DisplayName "Windows Time"  # By display name',
            'sasv w32time                         # Using alias'
        ],
        'alias': ['sasv']
    },
    'Stop-Service': {
        'desc': 'Stop one or more running services',
        'common_flags': {
            '-Name': 'Specifies service names',
            '-DisplayName': 'Specifies display names',
            '-Force': 'Stops dependent services',
            '-PassThru': 'Returns service object'
        },
        'examples': [
            'Stop-Service -Name w32time           # Stop service',
            'Stop-Service -Force -Name Spooler    # Force stop with dependents',
            'spsv w32time                         # Using alias'
        ],
        'alias': ['spsv']
    },
    'Restart-Service': {
        'desc': 'Stop and start one or more services',
        'common_flags': {
            '-Name': 'Specifies service names',
            '-DisplayName': 'Specifies display names',
            '-Force': 'Forces restart',
            '-PassThru': 'Returns service object'
        },
        'examples': [
            'Restart-Service -Name w32time        # Restart service',
            'Restart-Service -Force -Name Spooler # Force restart'
        ],
        'alias': []
    },
    
    # Network
    'Test-Connection': {
        'desc': 'Send ICMP echo requests (ping)',
        'common_flags': {
            '-ComputerName': 'Specifies computers to ping',
            '-Count': 'Number of echo requests',
            '-Quiet': 'Returns boolean result',
            '-Source': 'Specifies source computer',
            '-Delay': 'Delay between pings'
        },
        'examples': [
            'Test-Connection google.com           # Ping host',
            'Test-Connection -ComputerName server -Count 2  # 2 pings',
            'Test-Connection google.com -Quiet    # Boolean result'
        ],
        'alias': ['ping']
    },
    'Invoke-WebRequest': {
        'desc': 'Get content from a web page',
        'common_flags': {
            '-Uri': 'Specifies the URI',
            '-Method': 'Specifies the method (GET, POST, etc.)',
            '-Headers': 'Specifies request headers',
            '-Body': 'Specifies request body',
            '-OutFile': 'Saves response to file',
            '-UseBasicParsing': 'Uses basic parsing',
            '-TimeoutSec': 'Specifies timeout'
        },
        'examples': [
            'Invoke-WebRequest -Uri "https://example.com"    # GET request',
            'Invoke-WebRequest -Uri "url" -OutFile file.html # Download file',
            'iwr https://example.com                         # Using alias'
        ],
        'alias': ['iwr', 'curl', 'wget']
    },
    'Invoke-RestMethod': {
        'desc': 'Send HTTP/HTTPS request to RESTful web service',
        'common_flags': {
            '-Uri': 'Specifies the URI',
            '-Method': 'Specifies the method',
            '-Headers': 'Specifies request headers',
            '-Body': 'Specifies request body',
            '-ContentType': 'Specifies content type'
        },
        'examples': [
            'Invoke-RestMethod -Uri "https://api.example.com"  # GET API',
            'Invoke-RestMethod -Method POST -Uri "url" -Body $data  # POST',
            'irm https://api.example.com                       # Using alias'
        ],
        'alias': ['irm']
    },
    'Get-NetIPAddress': {
        'desc': 'Get IP address configuration',
        'common_flags': {
            '-AddressFamily': 'Specifies IPv4 or IPv6',
            '-InterfaceAlias': 'Specifies network adapter',
            '-IPAddress': 'Specifies IP address'
        },
        'examples': [
            'Get-NetIPAddress                     # All IP addresses',
            'Get-NetIPAddress -AddressFamily IPv4 # IPv4 only',
            'Get-NetIPAddress -InterfaceAlias "Ethernet"  # Specific adapter'
        ],
        'alias': []
    },
    
    # System Information
    'Get-ComputerInfo': {
        'desc': 'Get system information',
        'common_flags': {
            '-Property': 'Specifies properties to get'
        },
        'examples': [
            'Get-ComputerInfo                     # All system info',
            'Get-ComputerInfo | Select-Object OsName, OsVersion  # Specific properties'
        ],
        'alias': []
    },
    'Get-WmiObject': {
        'desc': 'Get WMI class instances',
        'common_flags': {
            '-Class': 'Specifies WMI class',
            '-ComputerName': 'Specifies remote computer',
            '-Filter': 'Specifies a WMI query filter',
            '-Property': 'Specifies properties to retrieve'
        },
        'examples': [
            'Get-WmiObject -Class Win32_OperatingSystem  # OS info',
            'Get-WmiObject -Class Win32_LogicalDisk      # Disk info',
            'gwmi Win32_ComputerSystem                   # Using alias'
        ],
        'alias': ['gwmi']
    },
    'Get-CimInstance': {
        'desc': 'Get CIM class instances (newer than WMI)',
        'common_flags': {
            '-ClassName': 'Specifies CIM class name',
            '-ComputerName': 'Specifies remote computer',
            '-Filter': 'Specifies a filter',
            '-Property': 'Specifies properties'
        },
        'examples': [
            'Get-CimInstance -ClassName Win32_OperatingSystem  # OS info',
            'Get-CimInstance -ClassName Win32_LogicalDisk      # Disk info',
            'gcim Win32_ComputerSystem                         # Using alias'
        ],
        'alias': ['gcim']
    },
    'Get-Host': {
        'desc': 'Get host program information',
        'common_flags': {},
        'examples': [
            'Get-Host                             # PowerShell host info',
            '$PSVersionTable                      # PowerShell version'
        ],
        'alias': []
    },
    'Get-EventLog': {
        'desc': 'Get events from event log',
        'common_flags': {
            '-LogName': 'Specifies the event log',
            '-Newest': 'Gets specified number of newest entries',
            '-After': 'Gets events after specified date/time',
            '-Before': 'Gets events before specified date/time',
            '-EntryType': 'Specifies entry type (Error, Warning, etc.)'
        },
        'examples': [
            'Get-EventLog -LogName System -Newest 20      # Last 20 system events',
            'Get-EventLog -LogName Application -EntryType Error  # Application errors'
        ],
        'alias': []
    },
    
    # User and Security
    'Get-LocalUser': {
        'desc': 'Get local user accounts',
        'common_flags': {
            '-Name': 'Specifies user names'
        },
        'examples': [
            'Get-LocalUser                        # All local users',
            'Get-LocalUser -Name Administrator    # Specific user'
        ],
        'alias': []
    },
    'Get-LocalGroup': {
        'desc': 'Get local security groups',
        'common_flags': {
            '-Name': 'Specifies group names'
        },
        'examples': [
            'Get-LocalGroup                       # All local groups',
            'Get-LocalGroup -Name Administrators  # Specific group'
        ],
        'alias': []
    },
    'Get-Acl': {
        'desc': 'Get security descriptor (permissions)',
        'common_flags': {
            '-Path': 'Specifies path to item',
            '-Filter': 'Specifies a filter'
        },
        'examples': [
            'Get-Acl C:\\File.txt                  # Get file permissions',
            'Get-Acl C:\\Folder | Format-List      # Detailed permissions'
        ],
        'alias': []
    },
    
    # Variables and Objects
    'Get-Variable': {
        'desc': 'Get PowerShell variables',
        'common_flags': {
            '-Name': 'Specifies variable names',
            '-Scope': 'Specifies the scope',
            '-ValueOnly': 'Gets only the value'
        },
        'examples': [
            'Get-Variable                         # All variables',
            'Get-Variable -Name HOME              # Specific variable',
            'gv PATH                              # Using alias'
        ],
        'alias': ['gv']
    },
    'Set-Variable': {
        'desc': 'Set the value of a variable',
        'common_flags': {
            '-Name': 'Specifies the variable name',
            '-Value': 'Specifies the value',
            '-Scope': 'Specifies the scope',
            '-Option': 'Sets variable options'
        },
        'examples': [
            'Set-Variable -Name myVar -Value 10   # Set variable',
            '$myVar = 10                          # Direct assignment',
            'sv myVar 10                          # Using alias'
        ],
        'alias': ['sv', 'set']
    },
    'Get-Member': {
        'desc': 'Get properties and methods of objects',
        'common_flags': {
            '-InputObject': 'Specifies objects to examine',
            '-MemberType': 'Specifies member types to get',
            '-Name': 'Specifies member names',
            '-Static': 'Gets static members'
        },
        'examples': [
            'Get-Process | Get-Member             # Process object members',
            '"string" | Get-Member                # String methods',
            'Get-Date | gm                        # Using alias'
        ],
        'alias': ['gm']
    },
    'Select-Object': {
        'desc': 'Select properties of objects',
        'common_flags': {
            '-Property': 'Specifies properties to select',
            '-First': 'Gets first N objects',
            '-Last': 'Gets last N objects',
            '-Skip': 'Skips N objects',
            '-Unique': 'Eliminates duplicates',
            '-ExpandProperty': 'Expands specified property'
        },
        'examples': [
            'Get-Process | Select-Object Name, CPU  # Select properties',
            'Get-ChildItem | Select-Object -First 10  # First 10 items',
            'dir | select Name                    # Using alias'
        ],
        'alias': ['select']
    },
    'Where-Object': {
        'desc': 'Filter objects based on property values',
        'common_flags': {
            '-Property': 'Specifies property name',
            '-FilterScript': 'Specifies filter expression'
        },
        'examples': [
            'Get-Process | Where-Object {$_.CPU -gt 10}  # Filter by CPU',
            'Get-Service | Where-Object Status -eq "Running"  # Running services',
            'dir | where Length -gt 1MB           # Using alias'
        ],
        'alias': ['where', '?']
    },
    'Sort-Object': {
        'desc': 'Sort objects by property values',
        'common_flags': {
            '-Property': 'Specifies properties to sort by',
            '-Descending': 'Sorts in descending order',
            '-Unique': 'Eliminates duplicates',
            '-Top': 'Gets top N objects',
            '-Bottom': 'Gets bottom N objects'
        },
        'examples': [
            'Get-Process | Sort-Object CPU        # Sort by CPU',
            'Get-ChildItem | Sort-Object Length -Descending  # Largest first',
            'dir | sort Name                      # Using alias'
        ],
        'alias': ['sort']
    },
    'ForEach-Object': {
        'desc': 'Perform operation on each object in collection',
        'common_flags': {
            '-Process': 'Specifies operation to perform',
            '-Begin': 'Runs before processing',
            '-End': 'Runs after processing'
        },
        'examples': [
            '1..10 | ForEach-Object {$_ * 2}      # Multiply each by 2',
            'Get-ChildItem | ForEach-Object {$_.Name}  # Get names',
            'dir | foreach {$_.Length}            # Using alias'
        ],
        'alias': ['foreach', '%']
    },
    'Measure-Object': {
        'desc': 'Calculate numeric properties of objects',
        'common_flags': {
            '-Property': 'Specifies properties to measure',
            '-Sum': 'Calculates sum',
            '-Average': 'Calculates average',
            '-Maximum': 'Finds maximum',
            '-Minimum': 'Finds minimum',
            '-Line': 'Counts lines',
            '-Word': 'Counts words',
            '-Character': 'Counts characters'
        },
        'examples': [
            'Get-ChildItem | Measure-Object -Property Length -Sum  # Total size',
            'Get-Content file.txt | Measure-Object -Line  # Count lines',
            'dir | measure                        # Using alias'
        ],
        'alias': ['measure']
    },
    'Group-Object': {
        'desc': 'Group objects by property values',
        'common_flags': {
            '-Property': 'Specifies properties to group by',
            '-NoElement': 'Omits members from results',
            '-AsHashTable': 'Returns hashtable',
            '-AsString': 'Converts hashtable keys to strings'
        },
        'examples': [
            'Get-Process | Group-Object Name      # Group by name',
            'Get-Service | Group-Object Status    # Group by status',
            'dir | group Extension                # Using alias'
        ],
        'alias': ['group']
    },
    
    # Format Output
    'Format-Table': {
        'desc': 'Format output as table',
        'common_flags': {
            '-Property': 'Specifies properties to display',
            '-AutoSize': 'Adjusts column sizes',
            '-GroupBy': 'Groups output by property',
            '-Wrap': 'Wraps text in column'
        },
        'examples': [
            'Get-Process | Format-Table Name, CPU  # Table format',
            'Get-Service | Format-Table -AutoSize  # Auto-sized columns',
            'dir | ft Name, Length                 # Using alias'
        ],
        'alias': ['ft']
    },
    'Format-List': {
        'desc': 'Format output as list',
        'common_flags': {
            '-Property': 'Specifies properties to display',
            '-GroupBy': 'Groups output by property'
        },
        'examples': [
            'Get-Process | Format-List *           # All properties',
            'Get-Service wuauserv | Format-List    # Service details',
            'dir | fl Name, Length                 # Using alias'
        ],
        'alias': ['fl']
    },
    'Format-Wide': {
        'desc': 'Format output as wide table',
        'common_flags': {
            '-Property': 'Specifies property to display',
            '-Column': 'Specifies number of columns',
            '-AutoSize': 'Adjusts column sizes'
        },
        'examples': [
            'Get-Process | Format-Wide Name        # Wide format',
            'Get-ChildItem | Format-Wide -Column 3 # 3 columns',
            'dir | fw Name                         # Using alias'
        ],
        'alias': ['fw']
    },
    
    # Modules and Commands
    'Get-Command': {
        'desc': 'Get all commands',
        'common_flags': {
            '-Name': 'Specifies command names',
            '-Module': 'Gets commands from modules',
            '-CommandType': 'Specifies command types',
            '-Verb': 'Specifies command verbs',
            '-Noun': 'Specifies command nouns'
        },
        'examples': [
            'Get-Command                          # All commands',
            'Get-Command -Name Get-*              # Commands starting with Get',
            'Get-Command -Module ActiveDirectory  # Module commands',
            'gcm *process*                        # Using alias'
        ],
        'alias': ['gcm']
    },
    'Get-Help': {
        'desc': 'Display information about commands',
        'common_flags': {
            '-Name': 'Specifies command name',
            '-Full': 'Displays full help',
            '-Detailed': 'Displays detailed help',
            '-Examples': 'Displays only examples',
            '-Online': 'Opens online help',
            '-ShowWindow': 'Displays help in window'
        },
        'examples': [
            'Get-Help Get-Process                 # Command help',
            'Get-Help Get-Process -Examples       # Show examples',
            'Get-Help Get-Process -Full           # Full help',
            'help Get-Process                     # Using alias'
        ],
        'alias': ['help', 'man']
    },
    'Get-Module': {
        'desc': 'Get loaded modules',
        'common_flags': {
            '-Name': 'Specifies module names',
            '-ListAvailable': 'Lists available modules',
            '-All': 'Gets all modules'
        },
        'examples': [
            'Get-Module                           # Loaded modules',
            'Get-Module -ListAvailable            # Available modules',
            'gmo                                  # Using alias'
        ],
        'alias': ['gmo']
    },
    'Import-Module': {
        'desc': 'Add module to current session',
        'common_flags': {
            '-Name': 'Specifies module names',
            '-Force': 'Reloads module',
            '-Global': 'Imports into global scope'
        },
        'examples': [
            'Import-Module ActiveDirectory        # Import module',
            'Import-Module MyModule -Force        # Force reload',
            'ipmo ActiveDirectory                 # Using alias'
        ],
        'alias': ['ipmo']
    },
    
    # Execution and Scripts
    'Invoke-Expression': {
        'desc': 'Run commands or expressions',
        'common_flags': {
            '-Command': 'Specifies command to run'
        },
        'examples': [
            'Invoke-Expression "Get-Process"      # Run command from string',
            '$cmd = "dir"; Invoke-Expression $cmd # Run from variable',
            'iex "Get-Date"                       # Using alias'
        ],
        'alias': ['iex']
    },
    'Invoke-Command': {
        'desc': 'Run commands on local and remote computers',
        'common_flags': {
            '-ScriptBlock': 'Specifies commands to run',
            '-ComputerName': 'Specifies computers',
            '-FilePath': 'Runs script file',
            '-Credential': 'Specifies credentials',
            '-Session': 'Runs in PSSession'
        },
        'examples': [
            'Invoke-Command -ComputerName Server -ScriptBlock {Get-Process}  # Remote',
            'Invoke-Command -FilePath script.ps1  # Run script',
            'icm -ComputerName Server {Get-Date}  # Using alias'
        ],
        'alias': ['icm']
    },
    
    # Clipboard
    'Get-Clipboard': {
        'desc': 'Get content from clipboard',
        'common_flags': {
            '-Format': 'Specifies clipboard format',
            '-Raw': 'Gets raw content'
        },
        'examples': [
            'Get-Clipboard                        # Get clipboard text',
            'Get-Clipboard | Out-File clip.txt    # Save to file'
        ],
        'alias': ['gcb']
    },
    'Set-Clipboard': {
        'desc': 'Set content to clipboard',
        'common_flags': {
            '-Value': 'Specifies value to copy',
            '-Append': 'Appends to clipboard'
        },
        'examples': [
            'Set-Clipboard "Hello World"          # Copy text',
            'Get-Content file.txt | Set-Clipboard # Copy file content',
            'scb "Text"                           # Using alias'
        ],
        'alias': ['scb']
    },
    
    # Compression
    'Compress-Archive': {
        'desc': 'Create compressed archive (ZIP)',
        'common_flags': {
            '-Path': 'Specifies files to compress',
            '-DestinationPath': 'Specifies archive file path',
            '-CompressionLevel': 'Specifies compression level',
            '-Update': 'Updates existing archive',
            '-Force': 'Overwrites existing archive'
        },
        'examples': [
            'Compress-Archive -Path C:\\Files -DestinationPath archive.zip  # Create ZIP',
            'Compress-Archive -Path *.log -DestinationPath logs.zip  # Compress logs'
        ],
        'alias': []
    },
    'Expand-Archive': {
        'desc': 'Extract files from archive (ZIP)',
        'common_flags': {
            '-Path': 'Specifies archive file',
            '-DestinationPath': 'Specifies extraction path',
            '-Force': 'Overwrites existing files'
        },
        'examples': [
            'Expand-Archive -Path archive.zip -DestinationPath C:\\Extract  # Extract',
            'Expand-Archive archive.zip                            # Extract to current dir'
        ],
        'alias': []
    },
    
    # Hash and Security
    'Get-FileHash': {
        'desc': 'Compute hash value for file',
        'common_flags': {
            '-Path': 'Specifies file path',
            '-Algorithm': 'Specifies algorithm (SHA256, MD5, etc.)',
            '-InputStream': 'Specifies input stream'
        },
        'examples': [
            'Get-FileHash file.txt                # SHA256 hash',
            'Get-FileHash file.txt -Algorithm MD5 # MD5 hash',
            'Get-FileHash *.exe | Format-Table    # Hash multiple files'
        ],
        'alias': []
    },
    
    # Registry
    'Get-ItemProperty': {
        'desc': 'Get properties of item (registry, file, etc.)',
        'common_flags': {
            '-Path': 'Specifies item path',
            '-Name': 'Specifies property names'
        },
        'examples': [
            'Get-ItemProperty HKLM:\\SOFTWARE\\Microsoft\\Windows  # Registry',
            'Get-ItemProperty -Path file.txt                       # File properties'
        ],
        'alias': ['gp']
    },
    'Set-ItemProperty': {
        'desc': 'Set property of item',
        'common_flags': {
            '-Path': 'Specifies item path',
            '-Name': 'Specifies property name',
            '-Value': 'Specifies property value'
        },
        'examples': [
            'Set-ItemProperty -Path HKLM:\\Path -Name Key -Value "Value"  # Registry',
            'Set-ItemProperty file.txt -Name IsReadOnly -Value $true      # File property'
        ],
        'alias': ['sp']
    },
}

if __name__ == '__main__':
    print(f"PowerShell Command Database loaded")
    print(f"Total commands: {len(POWERSHELL_COMMAND_DB)}")
    total_flags = sum(len(cmd['common_flags']) for cmd in POWERSHELL_COMMAND_DB.values())
    print(f"Total parameters documented: {total_flags}")
    
    # Count aliases
    total_aliases = sum(len(cmd.get('alias', [])) for cmd in POWERSHELL_COMMAND_DB.values())
    print(f"Total aliases: {total_aliases}")
