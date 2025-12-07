#!/usr/bin/env python3
"""
Windows CMD Command Database
Comprehensive documentation for Windows Command Prompt commands
"""

CMD_COMMAND_DB = {
    # File and Directory Management
    'dir': {
        'desc': 'Display list of files and subdirectories',
        'common_flags': {
            '/A': 'Display files with specified attributes',
            '/B': 'Bare format (no heading or summary)',
            '/S': 'Display files in current directory and subdirectories',
            '/P': 'Pause after each screenful',
            '/W': 'Wide list format',
            '/O:N': 'Sort by name alphabetically',
            '/O:S': 'Sort by size (smallest first)',
            '/O:D': 'Sort by date/time (oldest first)',
            '/O:-D': 'Sort by date/time (newest first)',
            '/T:C': 'Display/sort by creation time',
            '/T:A': 'Display/sort by last access time',
            '/T:W': 'Display/sort by last written time'
        },
        'examples': [
            'dir                    # List current directory',
            'dir /S                 # List recursively',
            'dir /O:-D              # Sort by date, newest first',
            'dir /A:D               # List directories only',
            'dir *.txt              # List .txt files'
        ],
        'category': 'File Operations',
        'alias': ['ls']  # PowerShell alias
    },
    
    'cd': {
        'desc': 'Change the current directory',
        'common_flags': {
            '/D': 'Change drive and directory',
            '..': 'Move to parent directory',
            '\\': 'Move to root directory'
        },
        'examples': [
            'cd C:\\Windows         # Change to Windows directory',
            'cd ..                 # Move up one directory',
            'cd \\                 # Go to root',
            'cd /D D:\\Data        # Change to different drive'
        ],
        'category': 'File Operations',
        'alias': ['chdir']
    },
    
    'copy': {
        'desc': 'Copy one or more files to another location',
        'common_flags': {
            '/Y': 'Suppress prompting to confirm overwrite',
            '/V': 'Verify that new files are written correctly',
            '/A': 'Copy files as ASCII text',
            '/B': 'Copy files as binary',
            '/D': 'Allow encrypted files to be copied as decrypted'
        },
        'examples': [
            'copy file.txt backup.txt        # Copy file',
            'copy *.txt D:\\Backup\\          # Copy all .txt files',
            'copy /Y file.txt dest\\          # Overwrite without prompt',
            'copy file1+file2 combined.txt   # Concatenate files'
        ],
        'category': 'File Operations',
        'alias': []
    },
    
    'xcopy': {
        'desc': 'Copy files and directory trees (advanced)',
        'common_flags': {
            '/S': 'Copy directories and subdirectories (not empty)',
            '/E': 'Copy directories and subdirectories (including empty)',
            '/Y': 'Suppress prompting to confirm overwrite',
            '/I': 'Assume destination is directory if copying multiple files',
            '/D': 'Copy only newer files',
            '/H': 'Copy hidden and system files',
            '/R': 'Overwrite read-only files',
            '/V': 'Verify each file',
            '/F': 'Display full source and destination file names',
            '/Q': 'Quiet mode (no file names displayed)'
        },
        'examples': [
            'xcopy C:\\Source D:\\Dest /E   # Copy all including empty dirs',
            'xcopy /S /Y *.doc D:\\Backup   # Copy .doc files, no prompt',
            'xcopy /D /E source dest        # Copy only newer files'
        ],
        'category': 'File Operations',
        'alias': []
    },
    
    'move': {
        'desc': 'Move files or rename files and directories',
        'common_flags': {
            '/Y': 'Suppress prompting to confirm overwrite',
            '/-Y': 'Prompt to confirm overwrite'
        },
        'examples': [
            'move file.txt D:\\Dest\\        # Move file',
            'move oldname.txt newname.txt   # Rename file',
            'move *.txt D:\\TextFiles\\      # Move all .txt files'
        ],
        'category': 'File Operations',
        'alias': ['mv', 'ren']
    },
    
    'del': {
        'desc': 'Delete one or more files',
        'common_flags': {
            '/P': 'Prompt for confirmation before deleting',
            '/F': 'Force delete read-only files',
            '/S': 'Delete from subdirectories',
            '/Q': 'Quiet mode (no confirmation)',
            '/A': 'Select files based on attributes'
        },
        'examples': [
            'del file.txt           # Delete file',
            'del /P *.tmp           # Delete with confirmation',
            'del /S /Q *.bak        # Delete .bak files recursively, no confirm',
            'del /F /A:R readonly.txt  # Force delete read-only'
        ],
        'category': 'File Operations',
        'alias': ['erase']
    },
    
    'mkdir': {
        'desc': 'Create a directory',
        'common_flags': {},
        'examples': [
            'mkdir NewFolder        # Create directory',
            'mkdir "New Folder"    # Create with spaces',
            'mkdir Parent\\Child    # Create nested directories'
        ],
        'category': 'File Operations',
        'alias': ['md']
    },
    
    'rmdir': {
        'desc': 'Remove a directory',
        'common_flags': {
            '/S': 'Remove directory and all subdirectories/files',
            '/Q': 'Quiet mode (no confirmation)'
        },
        'examples': [
            'rmdir OldFolder        # Remove empty directory',
            'rmdir /S /Q Folder     # Remove directory and contents, no confirm'
        ],
        'category': 'File Operations',
        'alias': ['rd']
    },
    
    'ren': {
        'desc': 'Rename a file or directory',
        'common_flags': {},
        'examples': [
            'ren oldname.txt newname.txt    # Rename file',
            'ren OldFolder NewFolder         # Rename directory',
            'ren *.txt *.bak                # Rename all .txt to .bak'
        ],
        'category': 'File Operations',
        'alias': ['rename']
    },
    
    'type': {
        'desc': 'Display contents of a text file',
        'common_flags': {},
        'examples': [
            'type file.txt          # Display file contents',
            'type file.txt | more   # Display with paging'
        ],
        'category': 'File Operations',
        'alias': ['cat']
    },
    
    'more': {
        'desc': 'Display output one screen at a time',
        'common_flags': {
            '/E': 'Enable extended features',
            '/C': 'Clear screen before displaying page',
            '/P': 'Expand FormFeed characters',
            '/S': 'Squeeze multiple blank lines into one'
        },
        'examples': [
            'type file.txt | more   # Page through file',
            'dir /S | more          # Page through directory listing'
        ],
        'category': 'File Operations',
        'alias': []
    },
    
    # Text Processing
    'find': {
        'desc': 'Search for a text string in files',
        'common_flags': {
            '/V': 'Display lines NOT containing the string',
            '/C': 'Display only the count of matching lines',
            '/N': 'Display line numbers',
            '/I': 'Ignore case'
        },
        'examples': [
            'find "text" file.txt       # Search for text',
            'find /I "error" log.txt    # Case-insensitive search',
            'find /C "error" *.log      # Count occurrences',
            'dir /S | find "pattern"    # Search in dir output'
        ],
        'category': 'Text Processing',
        'alias': []
    },
    
    'findstr': {
        'desc': 'Search for strings in files using regular expressions',
        'common_flags': {
            '/I': 'Case-insensitive search',
            '/R': 'Use regular expressions',
            '/S': 'Search subdirectories',
            '/N': 'Print line numbers',
            '/M': 'Print only filename if file contains match',
            '/C:': 'Use specified string literally'
        },
        'examples': [
            'findstr "pattern" file.txt         # Search for pattern',
            'findstr /I /S "error" *.log        # Recursive case-insensitive',
            'findstr /R "^Error.*" log.txt      # Regex search',
            'findstr /M "TODO" *.cs             # List files containing TODO'
        ],
        'category': 'Text Processing',
        'alias': []
    },
    
    'sort': {
        'desc': 'Sort input and display results',
        'common_flags': {
            '/R': 'Reverse sort order',
            '/+n': 'Start sorting at column n',
            '/M': 'Specify memory to use (in KB)'
        },
        'examples': [
            'sort file.txt           # Sort file',
            'dir | sort              # Sort directory listing',
            'sort /R file.txt        # Reverse sort'
        ],
        'category': 'Text Processing',
        'alias': []
    },
    
    # System Information
    'systeminfo': {
        'desc': 'Display detailed configuration information',
        'common_flags': {
            '/S': 'Specify remote system',
            '/FO': 'Format output (TABLE, LIST, CSV)',
            '/NH': 'No headers in output'
        },
        'examples': [
            'systeminfo              # Display system info',
            'systeminfo /FO CSV      # Output as CSV',
            'systeminfo | findstr /I "total"  # Find memory info'
        ],
        'category': 'System Information',
        'alias': []
    },
    
    'ver': {
        'desc': 'Display Windows version',
        'common_flags': {},
        'examples': [
            'ver                     # Show Windows version'
        ],
        'category': 'System Information',
        'alias': []
    },
    
    'hostname': {
        'desc': 'Display computer name',
        'common_flags': {},
        'examples': [
            'hostname                # Show computer name'
        ],
        'category': 'System Information',
        'alias': []
    },
    
    'whoami': {
        'desc': 'Display current username and domain',
        'common_flags': {
            '/USER': 'Display user information',
            '/GROUPS': 'Display group membership',
            '/PRIV': 'Display security privileges',
            '/ALL': 'Display all information'
        },
        'examples': [
            'whoami                  # Show current user',
            'whoami /GROUPS          # Show group membership',
            'whoami /PRIV            # Show privileges'
        ],
        'category': 'System Information',
        'alias': []
    },
    
    # Process Management
    'tasklist': {
        'desc': 'Display list of running processes',
        'common_flags': {
            '/FI': 'Apply filter (e.g., "STATUS eq RUNNING")',
            '/FO': 'Format output (TABLE, LIST, CSV)',
            '/NH': 'No headers',
            '/V': 'Verbose information',
            '/M': 'List modules/DLLs',
            '/SVC': 'List services in each process'
        },
        'examples': [
            'tasklist                         # List all processes',
            'tasklist /FI "IMAGENAME eq chrome.exe"  # Filter by name',
            'tasklist /SVC                    # Show services',
            'tasklist /V                      # Verbose output'
        ],
        'category': 'Process Management',
        'alias': []
    },
    
    'taskkill': {
        'desc': 'Terminate processes by PID or image name',
        'common_flags': {
            '/PID': 'Specify process ID',
            '/IM': 'Specify image name',
            '/F': 'Force termination',
            '/T': 'Terminate process tree'
        },
        'examples': [
            'taskkill /PID 1234              # Kill by process ID',
            'taskkill /IM notepad.exe        # Kill by name',
            'taskkill /F /IM chrome.exe      # Force kill',
            'taskkill /F /T /IM process.exe  # Kill process tree'
        ],
        'category': 'Process Management',
        'alias': []
    },
    
    'start': {
        'desc': 'Start a program or command in a new window',
        'common_flags': {
            '/MIN': 'Start minimized',
            '/MAX': 'Start maximized',
            '/WAIT': 'Wait for program to finish',
            '/B': 'Start without new window',
            '/HIGH': 'Start with HIGH priority',
            '/LOW': 'Start with LOW priority'
        },
        'examples': [
            'start notepad.exe       # Start Notepad',
            'start /MAX calc.exe     # Start Calculator maximized',
            'start /WAIT setup.exe   # Wait for setup to finish',
            'start https://google.com  # Open URL in browser'
        ],
        'category': 'Process Management',
        'alias': []
    },
    
    # Network Commands
    'ping': {
        'desc': 'Test network connectivity',
        'common_flags': {
            '-t': 'Ping until stopped (Ctrl+C)',
            '-n': 'Number of echo requests (default 4)',
            '-l': 'Send buffer size',
            '-w': 'Timeout in milliseconds',
            '-a': 'Resolve addresses to hostnames'
        },
        'examples': [
            'ping google.com         # Ping 4 times',
            'ping -t google.com      # Continuous ping',
            'ping -n 10 192.168.1.1  # Ping 10 times',
            'ping -a 192.168.1.1     # Resolve hostname'
        ],
        'category': 'Network',
        'alias': []
    },
    
    'ipconfig': {
        'desc': 'Display IP network configuration',
        'common_flags': {
            '/all': 'Display full configuration',
            '/release': 'Release DHCP IP address',
            '/renew': 'Renew DHCP IP address',
            '/flushdns': 'Flush DNS cache',
            '/displaydns': 'Display DNS cache'
        },
        'examples': [
            'ipconfig                # Show IP configuration',
            'ipconfig /all           # Detailed information',
            'ipconfig /flushdns      # Clear DNS cache',
            'ipconfig /renew         # Renew IP address'
        ],
        'category': 'Network',
        'alias': []
    },
    
    'netstat': {
        'desc': 'Display network connections and statistics',
        'common_flags': {
            '-a': 'Display all connections and listening ports',
            '-n': 'Display addresses and ports numerically',
            '-o': 'Display owning process ID',
            '-b': 'Display executable creating connection',
            '-r': 'Display routing table',
            '-p': 'Show connections for protocol (TCP, UDP)'
        },
        'examples': [
            'netstat -a              # All connections',
            'netstat -ano            # All with PIDs',
            'netstat -b              # Show executables',
            'netstat -r              # Show routing table'
        ],
        'category': 'Network',
        'alias': []
    },
    
    'nslookup': {
        'desc': 'Query DNS servers for domain information',
        'common_flags': {
            '-type=': 'Query type (A, MX, NS, etc.)'
        },
        'examples': [
            'nslookup google.com     # DNS lookup',
            'nslookup -type=MX google.com  # Mail server lookup',
            'nslookup 8.8.8.8        # Reverse lookup'
        ],
        'category': 'Network',
        'alias': []
    },
    
    'tracert': {
        'desc': 'Trace route to destination',
        'common_flags': {
            '-d': 'Do not resolve addresses to hostnames',
            '-h': 'Maximum hops',
            '-w': 'Timeout for each reply'
        },
        'examples': [
            'tracert google.com      # Trace route',
            'tracert -d 8.8.8.8      # Trace without DNS',
            'tracert -h 15 google.com  # Max 15 hops'
        ],
        'category': 'Network',
        'alias': []
    },
    
    'net': {
        'desc': 'Network services and resources management',
        'common_flags': {
            'user': 'Manage user accounts',
            'share': 'Manage shared resources',
            'use': 'Connect/disconnect shared resources',
            'view': 'Display computers or resources',
            'start': 'Start a service',
            'stop': 'Stop a service'
        },
        'examples': [
            'net user                # List users',
            'net user username /add  # Add user',
            'net share               # List shares',
            'net use Z: \\\\server\\share  # Map network drive',
            'net start "service"     # Start service',
            'net stop "service"      # Stop service'
        ],
        'category': 'Network',
        'alias': []
    },
    
    # Disk Management
    'chkdsk': {
        'desc': 'Check disk for errors',
        'common_flags': {
            '/F': 'Fix errors on disk',
            '/R': 'Locate bad sectors and recover data',
            '/X': 'Force volume to dismount first',
            '/V': 'Display full path and name of files'
        },
        'examples': [
            'chkdsk C:               # Check C: drive',
            'chkdsk C: /F            # Check and fix errors',
            'chkdsk C: /R            # Check, fix, and recover'
        ],
        'category': 'Disk Management',
        'alias': []
    },
    
    'diskpart': {
        'desc': 'Disk partition management utility',
        'common_flags': {},
        'examples': [
            'diskpart                # Start diskpart utility',
            'diskpart /s script.txt  # Run script'
        ],
        'category': 'Disk Management',
        'alias': []
    },
    
    'format': {
        'desc': 'Format a disk',
        'common_flags': {
            '/FS:': 'File system (NTFS, FAT32, exFAT)',
            '/Q': 'Quick format',
            '/V:': 'Volume label',
            '/A:': 'Allocation unit size'
        },
        'examples': [
            'format D: /FS:NTFS      # Format as NTFS',
            'format D: /Q            # Quick format',
            'format D: /FS:NTFS /V:Data  # Format with label'
        ],
        'category': 'Disk Management',
        'alias': []
    },
    
    # Compression
    'compact': {
        'desc': 'Display or alter file compression',
        'common_flags': {
            '/C': 'Compress files',
            '/U': 'Uncompress files',
            '/S': 'Perform on subdirectories',
            '/I': 'Ignore errors',
            '/F': 'Force compression'
        },
        'examples': [
            'compact /C file.txt     # Compress file',
            'compact /U file.txt     # Uncompress file',
            'compact /C /S           # Compress all files recursively'
        ],
        'category': 'Compression',
        'alias': []
    },
    
    # System Management
    'shutdown': {
        'desc': 'Shutdown or restart computer',
        'common_flags': {
            '/s': 'Shutdown computer',
            '/r': 'Restart computer',
            '/l': 'Log off',
            '/h': 'Hibernate',
            '/t': 'Time delay in seconds',
            '/f': 'Force running applications to close',
            '/a': 'Abort shutdown'
        },
        'examples': [
            'shutdown /s /t 0        # Shutdown immediately',
            'shutdown /r /t 60       # Restart in 60 seconds',
            'shutdown /a             # Cancel shutdown',
            'shutdown /s /f /t 0     # Force shutdown now'
        ],
        'category': 'System Management',
        'alias': []
    },
    
    'sfc': {
        'desc': 'System File Checker - scan and repair system files',
        'common_flags': {
            '/scannow': 'Scan all system files and repair',
            '/verifyonly': 'Scan but do not repair',
            '/scanfile': 'Scan specific file'
        },
        'examples': [
            'sfc /scannow            # Scan and repair system files'
        ],
        'category': 'System Management',
        'alias': []
    },
    
    'reg': {
        'desc': 'Registry console tool for reading/writing registry',
        'common_flags': {
            'query': 'Query registry values',
            'add': 'Add registry entry',
            'delete': 'Delete registry entry',
            'copy': 'Copy registry entry',
            'export': 'Export registry to file',
            'import': 'Import registry from file'
        },
        'examples': [
            'reg query HKLM\\Software  # Query registry key',
            'reg export HKCU\\Software backup.reg  # Export',
            'reg import backup.reg    # Import'
        ],
        'category': 'System Management',
        'alias': []
    },
    
    # Environment
    'set': {
        'desc': 'Display, set, or remove environment variables',
        'common_flags': {
            '/A': 'Expression is numeric',
            '/P': 'Prompt user for input'
        },
        'examples': [
            'set                     # Display all variables',
            'set PATH                # Display PATH variable',
            'set MYVAR=value         # Set variable',
            'set /P NAME="Enter name: "  # Prompt for input'
        ],
        'category': 'Environment',
        'alias': []
    },
    
    'path': {
        'desc': 'Display or set search path for executable files',
        'common_flags': {},
        'examples': [
            'path                    # Display current PATH',
            'path C:\\Tools;%PATH%   # Add to PATH temporarily'
        ],
        'category': 'Environment',
        'alias': []
    },
    
    # Batch Scripting
    'echo': {
        'desc': 'Display messages or turn command echoing on/off',
        'common_flags': {
            'on': 'Turn command echoing on',
            'off': 'Turn command echoing off'
        },
        'examples': [
            'echo Hello              # Display message',
            'echo off                # Turn echoing off',
            'echo %PATH%             # Display variable',
            'echo. > file.txt        # Create empty file'
        ],
        'category': 'Batch Scripting',
        'alias': []
    },
    
    'if': {
        'desc': 'Conditional processing in batch files',
        'common_flags': {
            'EXIST': 'Check if file exists',
            'ERRORLEVEL': 'Check error level',
            'EQU': 'Equal to',
            'NEQ': 'Not equal to',
            'LSS': 'Less than',
            'GTR': 'Greater than'
        },
        'examples': [
            'if exist file.txt del file.txt',
            'if %var%==value echo Match',
            'if errorlevel 1 echo Error occurred'
        ],
        'category': 'Batch Scripting',
        'alias': []
    },
    
    'for': {
        'desc': 'Run a command for each file in a set',
        'common_flags': {
            '/D': 'Process directories instead of files',
            '/R': 'Recursive',
            '/L': 'Loop with start, step, end',
            '/F': 'Parse file contents or command output'
        },
        'examples': [
            'for %i in (*.txt) do type %i',
            'for /R %i in (*.log) do del %i',
            'for /L %i in (1,1,10) do echo %i'
        ],
        'category': 'Batch Scripting',
        'alias': []
    },
    
    'goto': {
        'desc': 'Direct batch program to labeled line',
        'common_flags': {},
        'examples': [
            'goto :label             # Jump to :label',
            ':label                  # Define label',
            'goto :eof               # Jump to end of file'
        ],
        'category': 'Batch Scripting',
        'alias': []
    },
    
    'call': {
        'desc': 'Call one batch program from another',
        'common_flags': {},
        'examples': [
            'call other.bat          # Call another batch file',
            'call :subroutine        # Call label as subroutine'
        ],
        'category': 'Batch Scripting',
        'alias': []
    },
    
    'pause': {
        'desc': 'Suspend processing and display message',
        'common_flags': {},
        'examples': [
            'pause                   # Display "Press any key..."'
        ],
        'category': 'Batch Scripting',
        'alias': []
    },
    
    'cls': {
        'desc': 'Clear the screen',
        'common_flags': {},
        'examples': [
            'cls                     # Clear screen'
        ],
        'category': 'Batch Scripting',
        'alias': ['clear']
    },
    
    'exit': {
        'desc': 'Exit the command interpreter',
        'common_flags': {
            '/B': 'Exit batch file only (not entire cmd.exe)'
        },
        'examples': [
            'exit                    # Close command prompt',
            'exit /B                 # Exit batch script',
            'exit /B 1               # Exit with error code'
        ],
        'category': 'Batch Scripting',
        'alias': []
    },
    
    # Help and Documentation
    'help': {
        'desc': 'Display help information for commands',
        'common_flags': {},
        'examples': [
            'help                    # List all commands',
            'help dir                # Help for DIR command',
            'dir /?                  # Command-specific help'
        ],
        'category': 'Help',
        'alias': []
    },
    
    # Attributes
    'attrib': {
        'desc': 'Display or change file attributes',
        'common_flags': {
            '+R': 'Set read-only attribute',
            '-R': 'Clear read-only attribute',
            '+H': 'Set hidden attribute',
            '-H': 'Clear hidden attribute',
            '+S': 'Set system attribute',
            '/S': 'Process subdirectories',
            '/D': 'Process folders as well'
        },
        'examples': [
            'attrib file.txt         # Show attributes',
            'attrib +R file.txt      # Set read-only',
            'attrib -H *.* /S        # Remove hidden from all files'
        ],
        'category': 'File Operations',
        'alias': []
    },
    
    # Comparison
    'fc': {
        'desc': 'Compare two files and display differences',
        'common_flags': {
            '/B': 'Binary comparison',
            '/C': 'Ignore case',
            '/L': 'Compare as ASCII text',
            '/N': 'Display line numbers',
            '/W': 'Compress whitespace'
        },
        'examples': [
            'fc file1.txt file2.txt  # Compare text files',
            'fc /B file1.exe file2.exe  # Binary compare'
        ],
        'category': 'Text Processing',
        'alias': []
    },
    
    # Time and Date
    'time': {
        'desc': 'Display or set system time',
        'common_flags': {
            '/T': 'Display time without prompting'
        },
        'examples': [
            'time                    # Display and prompt for time',
            'time /T                 # Display time only'
        ],
        'category': 'System Information',
        'alias': []
    },
    
    'date': {
        'desc': 'Display or set system date',
        'common_flags': {
            '/T': 'Display date without prompting'
        },
        'examples': [
            'date                    # Display and prompt for date',
            'date /T                 # Display date only'
        ],
        'category': 'System Information',
        'alias': []
    },
}
