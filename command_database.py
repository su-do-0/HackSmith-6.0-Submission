#!/usr/bin/env python3
"""
Comprehensive Linux Command Database
Converted from JSON - 730 commands
Compatible with cmdhelp
"""

COMPREHENSIVE_COMMAND_DB = {
    'i686-w64-mingw32-as': {
        'desc': 'the portable GNU assembler.',
        'common_flags': {
            '-a': 's include symbols',
            '--alternate': 'Begin in alternate macro mode.',
            '--compress-debug-sections': '=zlib-gnu compresses DWARF debug sections using the obsoleted zlib-gnu format. The debug sections are renamed to begin',
            '--nocompress-debug-sections': 'Do not compress DWARF debug sections. This is usually the default for all targets except the x86/x86_64, but a configure time option can be',
            '-D': 'Enable debugging in target specific backends, if supported. Otherwise ignored. Even if ignored, this option is accepted for script',
            '--debug-prefix-map': 'old=new',
            '--defsym': 'sym=value',
            '--dump-config': 'Displays how the assembler is configured and then exits.',
            '--elf-stt-common': '=yes',
            '--emulation': '=name',
            '-f': '\"fast\"---skip whitespace and comment preprocessing (assume source is compiler output).',
            '-g': '--gen-debug',
            '--gstabs': '+',
            '--gdwarf-2': 'Generate DWARF2 debugging information for each assembler line. This may help debugging assembler code, if the debugger can handle it.',
            '--gdwarf-3': 'This option is the same as the --gdwarf-2 option, except that it allows for the possibility of the generation of extra debug information as per'
        },
        'examples': [
            'i686-w64-mingw32-as  # the portable GNU assembler.',
            'i686-w64-mingw32-as -a  # Show all'
        ],
        'category': 'Other'
    },
    'wget': {
        'desc': 'The non-interactive network downloader.',
        'common_flags': {
            '--no-follow-ftp': 'is the only way to restore the factory default from the command line.',
            '-V': '--version',
            '-h': '--help',
            '-b': '--background',
            '-e': 'command',
            '--execute': 'command',
            '-o': 'logfile',
            '--output-file': '=logfile',
            '-a': 'logfile',
            '--append-output': '=logfile',
            '-d': '--debug',
            '-q': '--quiet',
            '-v': '--verbose',
            '-n': 'v',
            '--no-verbose': 'Turn off verbose without being completely quiet (use -q for that), which means that error messages and basic information still get printed.'
        },
        'examples': [
            'wget  # The non-interactive network downloader.',
            'wget https://example.com/file  # Download file',
            'wget -c url  # Continue interrupted download',
            'wget -r https://example.com/  # Recursive download'
        ],
        'category': 'Other'
    },
    'addr2line': {
        'desc': 'convert addresses or symbol+offset into file names and line numbers',
        'common_flags': {
            '-a': '--addresses',
            '-b': 'bfdname',
            '--target': '=bfdname',
            '-C': '--demangle[=style]',
            '-e': 'filename',
            '--exe': '=filename',
            '-f': '--functions',
            '-s': '--basenames',
            '-i': '--inlines',
            '-j': '--section',
            '-p': '--pretty-print',
            '-r': '-R',
            '--recurse-limit': '--no-recurse-limit',
            '--recursion-limit': '--no-recursion-limit'
        },
        'examples': [
            'addr2line  # convert addresses or symbol+offset into file names',
            'addr2line -r -f  # Recursive and forced',
            'addr2line -a  # Show all'
        ],
        'category': 'Other'
    },
    'apropos': {
        'desc': 'search the manual page names and descriptions',
        'common_flags': {
            '-d': 'Print debugging information.',
            '--debug': 'Print debugging information.',
            '-v': 'Print verbose warning messages.',
            '--verbose': 'Print verbose warning messages.',
            '-r': 'Interpret each keyword as a regular expression. This is the default behaviour. Each keyword will be matched against the page names and the',
            '--regex': 'Interpret each keyword as a regular expression. This is the default behaviour. Each keyword will be matched against the page names and the',
            '-w': 'Interpret each keyword as a pattern containing shell style wildcards. Each keyword will be matched against the page names and the descrip‐',
            '--wildcard': 'Interpret each keyword as a pattern containing shell style wildcards. Each keyword will be matched against the page names and the descrip‐',
            '-e': 'Each keyword will be exactly matched against the page names and the descriptions.',
            '--exact': 'Each keyword will be exactly matched against the page names and the descriptions.',
            '-a': 'Only display items that match all the supplied keywords. The default is to display items that match any keyword.',
            '--and': 'Only display items that match all the supplied keywords. The default is to display items that match any keyword.',
            '-l': 'Do not trim output to the terminal width. Normally, output will be truncated to the terminal width to avoid ugly results from poorly-written',
            '--long': 'Do not trim output to the terminal width. Normally, output will be truncated to the terminal width to avoid ugly results from poorly-written',
            '-s': 'list, --sections=list, --section=list'
        },
        'examples': [
            'apropos  # search the manual page names and descriptions',
            'apropos -v  # Show version',
            'apropos -v  # Verbose output',
            'apropos -a  # Show all'
        ],
        'category': 'Other'
    },
    'apt-extracttemplates': {
        'desc': 'Utility to extract debconf config and templates from Debian packages',
        'common_flags': {
            '-t': 'Temporary directory in which to write extracted debconf template files and config scripts. Configuration Item: APT::ExtractTemplates::TempDir',
            '--tempdir': 'Temporary directory in which to write extracted debconf template files and config scripts. Configuration Item: APT::ExtractTemplates::TempDir',
            '-h': 'Show a short usage summary.',
            '--help': 'Show a short usage summary.',
            '-v': 'Show the program version.',
            '--version': 'Show the program version.',
            '--audit': 'Show audit (and notice) messages. This overrides the quiet option, but only for notice messages, not progress ones.',
            '-c': 'Configuration File; Specify a configuration file to use. The program will read the default configuration file and then this configuration file.',
            '--config-file': 'Configuration File; Specify a configuration file to use. The program will read the default configuration file and then this configuration file.',
            '-o': 'Set a Configuration Option; This will set an arbitrary configuration option. The syntax is -o Foo::Bar=bar. -o and --option can be used',
            '--option': 'Set a Configuration Option; This will set an arbitrary configuration option. The syntax is -o Foo::Bar=bar. -o and --option can be used',
            '--no-color': 'Turn colors on or off. Colors are on by default on supported terminals for apt(8) and can also be disabled using the NO_COLOR or APT_NO_COLOR',
            '--color': 'Turn colors on or off. Colors are on by default on supported terminals for apt(8) and can also be disabled using the NO_COLOR or APT_NO_COLOR'
        },
        'examples': [
            'apt-extracttemplates  # Utility to extract debconf config and templates fr',
            'apt-extracttemplates -h  # Show help',
            'apt-extracttemplates -v  # Show version',
            'apt-extracttemplates -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'apt-file': {
        'desc': '- APT package searching utility -- command-line interface',
        'common_flags': {
            '-a': 'architecture[,...]',
            '--architecture': 'architecture[,...]',
            '-c': 'APT config-file',
            '--config-file': 'APT config-file',
            '-D': 'Use contents of the given .deb archives(s) as patterns. Useful for searching for file conflicts with other packages. Implies -F.',
            '--from-deb': 'Use contents of the given .deb archives(s) as patterns. Useful for searching for file conflicts with other packages. Implies -F.',
            '-f': 'Read patterns from the given file(s), one per line. Use - as filename for stdin. If no files are given, then the list will be read from stdin.',
            '--from-file': 'Read patterns from the given file(s), one per line. Use - as filename for stdin. If no files are given, then the list will be read from stdin.',
            '--filter-origins': 'origin[,...]',
            '--filter-suites': 'suite[,...]',
            '-F': 'Do not expand search pattern with generic characters at pattern\'s start and end.',
            '--fixed-string': 'Do not expand search pattern with generic characters at pattern\'s start and end.',
            '--index-names': 'type[,...], -I type[,...]',
            '-i': 'Ignore case when searching for pattern.',
            '--ignore-case': 'Ignore case when searching for pattern.'
        },
        'examples': [
            'apt-file  # - APT package searching utility -- command-line in',
            'apt-file -a  # Show all'
        ],
        'category': 'Other'
    },
    'apt-ftparchive': {
        'desc': 'Utility to generate index files',
        'common_flags': {
            '--md5': 'Generate the given checksum. These options default to on, when turned off the generated index files will not have the checksum fields where',
            '--sha1': 'Generate the given checksum. These options default to on, when turned off the generated index files will not have the checksum fields where',
            '--sha256': 'Generate the given checksum. These options default to on, when turned off the generated index files will not have the checksum fields where',
            '--sha512': 'Generate the given checksum. These options default to on, when turned off the generated index files will not have the checksum fields where',
            '-d': 'Use a binary caching DB. This has no effect on the generate command. Configuration Item: APT::FTPArchive::DB.',
            '--db': 'Use a binary caching DB. This has no effect on the generate command. Configuration Item: APT::FTPArchive::DB.',
            '-q': 'Quiet; produces output suitable for logging, omitting progress indicators. More q\'s will produce more quiet up to a maximum of 2. You can also',
            '--quiet': 'Quiet; produces output suitable for logging, omitting progress indicators. More q\'s will produce more quiet up to a maximum of 2. You can also',
            '--delink': 'Perform Delinking. If the External-Links setting is used then this option actually enables delinking of the files. It defaults to on and can be',
            '--contents': 'Perform contents generation. When this option is set and package indexes are being generated with a cache DB then the file listing will also be',
            '-s': 'Select the source override file to use with the sources command. Configuration Item: APT::FTPArchive::SourceOverride.',
            '--source-override': 'Select the source override file to use with the sources command. Configuration Item: APT::FTPArchive::SourceOverride.',
            '--readonly': 'Make the caching databases read only. Configuration Item: APT::FTPArchive::ReadOnlyDB.',
            '-a': 'Accept in the packages and contents commands only package files matching *_arch.deb or *_all.deb instead of all package files in the given path.',
            '--arch': 'Accept in the packages and contents commands only package files matching *_arch.deb or *_all.deb instead of all package files in the given path.'
        },
        'examples': [
            'apt-ftparchive  # Utility to generate index files',
            'apt-ftparchive -a  # Show all'
        ],
        'category': 'Other'
    },
    'apt-sortpkgs': {
        'desc': 'Utility to sort package index files',
        'common_flags': {
            '-s': 'Use source index field ordering. Configuration Item: APT::SortPkgs::Source.',
            '--source': 'Use source index field ordering. Configuration Item: APT::SortPkgs::Source.',
            '-h': 'Show a short usage summary.',
            '--help': 'Show a short usage summary.',
            '-v': 'Show the program version.',
            '--version': 'Show the program version.',
            '--audit': 'Show audit (and notice) messages. This overrides the quiet option, but only for notice messages, not progress ones.',
            '-c': 'Configuration File; Specify a configuration file to use. The program will read the default configuration file and then this configuration file.',
            '--config-file': 'Configuration File; Specify a configuration file to use. The program will read the default configuration file and then this configuration file.',
            '-o': 'Set a Configuration Option; This will set an arbitrary configuration option. The syntax is -o Foo::Bar=bar. -o and --option can be used',
            '--option': 'Set a Configuration Option; This will set an arbitrary configuration option. The syntax is -o Foo::Bar=bar. -o and --option can be used',
            '--no-color': 'Turn colors on or off. Colors are on by default on supported terminals for apt(8) and can also be disabled using the NO_COLOR or APT_NO_COLOR',
            '--color': 'Turn colors on or off. Colors are on by default on supported terminals for apt(8) and can also be disabled using the NO_COLOR or APT_NO_COLOR'
        },
        'examples': [
            'apt-sortpkgs  # Utility to sort package index files',
            'apt-sortpkgs -h  # Show help',
            'apt-sortpkgs -v  # Show version',
            'apt-sortpkgs -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'ar': {
        'desc': 'create, modify, and extract from archives',
        'common_flags': {
            '--output': 'dirname',
            '--help': 'Displays the list of command-line options supported by ar and then exits.',
            '--version': 'Displays the version information of ar and then exits.',
            '-X': '32_64',
            '--plugin': 'name',
            '--target': 'target',
            '--record-libdeps': 'libdeps',
            '--thin': 'Make the specified archive a thin archive. If it already exists and is a regular archive, the existing members must be present in the same'
        },
        'examples': [
            'ar  # create, modify, and extract from archives',
            'ar --help  # Show help',
            'ar --version  # Show version'
        ],
        'category': 'Other'
    },
    'as': {
        'desc': 'the portable GNU assembler.',
        'common_flags': {
            '-a': 's include symbols',
            '--alternate': 'Begin in alternate macro mode.',
            '--compress-debug-sections': '=zlib-gnu compresses DWARF debug sections using the obsoleted zlib-gnu format. The debug sections are renamed to begin',
            '--nocompress-debug-sections': 'Do not compress DWARF debug sections. This is usually the default for all targets except the x86/x86_64, but a configure time option can be',
            '-D': 'Enable debugging in target specific backends, if supported. Otherwise ignored. Even if ignored, this option is accepted for script',
            '--debug-prefix-map': 'old=new',
            '--defsym': 'sym=value',
            '--dump-config': 'Displays how the assembler is configured and then exits.',
            '--elf-stt-common': '=yes',
            '--emulation': '=name',
            '-f': '\"fast\"---skip whitespace and comment preprocessing (assume source is compiler output).',
            '-g': '--gen-debug',
            '--gstabs': '+',
            '--gdwarf-2': 'Generate DWARF2 debugging information for each assembler line. This may help debugging assembler code, if the debugger can handle it.',
            '--gdwarf-3': 'This option is the same as the --gdwarf-2 option, except that it allows for the possibility of the generation of extra debug information as per'
        },
        'examples': [
            'as  # the portable GNU assembler.',
            'as -a  # Show all'
        ],
        'category': 'Other'
    },
    'awk': {
        'desc': 'pattern scanning and text processing language',
        'common_flags': {
            '-F': 'value sets the field separator, FS, to value.',
            '-f': 'file Program text is read from file instead of from the command line. Multiple -f options are allowed.',
            '-v': 'var=value assigns value to program variable var.',
            '-W': 'version'
        },
        'examples': [
            'awk  # pattern scanning and text processing language',
            'awk \'{print $1}\' file.txt  # Print first column',
            'awk -F: \'{print $1}\' /etc/passwd  # Custom delimiter'
        ],
        'category': 'Other'
    },
    'bash': {
        'desc': 'GNU Bourne-Again SHell',
        'common_flags': {
            '-c': 'If the -c option is present, then commands are read from the first non-option argument command_string. If there are arguments after the',
            '-i': 'If the -i option is present, the shell is interactive.',
            '-l': 'Make bash act as if it had been invoked as a login shell (see INVOCATION below).',
            '-r': 'If the -r option is present, the shell becomes restricted (see RESTRICTED SHELL below).',
            '-s': 'If the -s option is present, or if no arguments remain after option processing, then commands are read from the standard input. This op‐',
            '-v': 'Print shell input lines as they are read.',
            '-x': 'Print commands and their arguments as they are executed.',
            '-D': 'A list of all double-quoted strings preceded by $ is printed on the standard output. These are the strings that are subject to language',
            '--debugger': 'Arrange for the debugger profile to be executed before the shell starts. Turns on extended debugging mode (see the description of the extde‐',
            '--dump-po-strings': 'Equivalent to -D, but the output is in the GNU gettext po (portable object) file format.',
            '--dump-strings': 'Equivalent to -D.',
            '--help': 'Display a usage message on standard output and exit successfully.',
            '--init-file': 'file',
            '--rcfile': 'file',
            '--login': 'Equivalent to -l.'
        },
        'examples': [
            'bash  # GNU Bourne-Again SHell',
            'bash --help  # Show help',
            'bash -v  # Show version',
            'bash -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'bashbug': {
        'desc': 'report a bug in bash',
        'common_flags': {
            '--help': 'Show a brief usage message and exit.',
            '--version': 'Show the version of bashbug and exit.'
        },
        'examples': [
            'bashbug  # report a bug in bash',
            'bashbug --help  # Show help',
            'bashbug --version  # Show version'
        ],
        'category': 'Other'
    },
    'bundle': {
        'desc': 'Ruby Dependency Management',
        'common_flags': {
            '--no-color': 'Print all output without color',
            '--retry': 'Specify the number of times you wish to attempt network commands',
            '-r': 'Specify the number of times you wish to attempt network commands',
            '--verbose': 'Print out additional logging information',
            '-V': 'Print out additional logging information'
        },
        'examples': [
            'bundle  # Ruby Dependency Management',
            'bundle -V  # Show version',
            'bundle --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'bundle-add': {
        'desc': 'Add gem to the Gemfile and run bundle install',
        'common_flags': {
            '--version': '=VERSION, -v=VERSION',
            '--group': '=GROUP, -g=GROUP',
            '--source': '=SOURCE, -s=SOURCE',
            '--require': '=REQUIRE, -r=REQUIRE',
            '--path': '=PATH',
            '--git': '=GIT',
            '--github': '=GITHUB',
            '--branch': '=BRANCH',
            '--ref': '=REF',
            '--glob': '=GLOB',
            '--quiet': 'Do not print progress information to the standard output.',
            '--skip-install': 'Adds the gem to the Gemfile but does not install it.',
            '--optimistic': 'Adds optimistic declaration of version.',
            '--strict': 'Adds strict declaration of version.'
        },
        'examples': [
            'bundle-add  # Add gem to the Gemfile and run bundle install',
            'bundle-add --version  # Show version'
        ],
        'category': 'Other'
    },
    'bundle-binstubs': {
        'desc': 'Install the binstubs of the listed gems',
        'common_flags': {
            '--force': 'Overwrite existing binstubs if they exist.',
            '--path': '[=PATH]',
            '--standalone': 'Makes binstubs that can work without depending on Rubygems or Bundler at runtime.',
            '--shebang': '=SHEBANG',
            '--all': 'Create binstubs for all gems in the bundle.',
            '--all-platforms': 'Install binstubs for all platforms.'
        },
        'examples': [
            'bundle-binstubs  # Install the binstubs of the listed gems',
            'bundle-binstubs --all  # Show all'
        ],
        'category': 'Other'
    },
    'bundle-cache': {
        'desc': 'Package your needed .gem files into your application',
        'common_flags': {
            '--all': 'Include all sources (including path and git).',
            '--all-platforms': 'Include gems for all platforms present in the lockfile, not only the current one.',
            '--cache-path': '=CACHE-PATH',
            '--gemfile': '=GEMFILE',
            '--no-install': 'Don\'t install the gems, only update the cache.',
            '--no-prune': 'Don\'t remove stale gems from the cache.',
            '--path': '=PATH',
            '--quiet': 'Only output warnings and errors.',
            '--frozen': 'Do not allow the Gemfile.lock to be updated after this bundle cache operation\'s install.'
        },
        'examples': [
            'bundle-cache  # Package your needed .gem files into your applicati',
            'bundle-cache --all  # Show all'
        ],
        'category': 'Other'
    },
    'bundle-check': {
        'desc': 'Verifies if dependencies are satisfied by installed gems',
        'common_flags': {
            '--dry-run': 'Locks the [Gemfile(5)][Gemfile(5)] before running the command.',
            '--gemfile': '=GEMFILE',
            '--path': '=PATH'
        },
        'examples': [
            'bundle-check  # Verifies if dependencies are satisfied by installe'
        ],
        'category': 'Other'
    },
    'bundle-clean': {
        'desc': 'Cleans up unused gems in your bundler directory',
        'common_flags': {
            '--dry-run': 'Print the changes, but do not clean the unused gems.',
            '--force': 'Forces cleaning up unused gems even if Bundler is configured to use globally installed gems. As a consequence, removes all system gems except'
        },
        'examples': [
            'bundle-clean  # Cleans up unused gems in your bundler directory'
        ],
        'category': 'Other'
    },
    'bundle-doctor': {
        'desc': 'Checks the bundle for common problems',
        'common_flags': {
            '--quiet': 'Only output warnings and errors.',
            '--gemfile': '=GEMFILE'
        },
        'examples': [
            'bundle-doctor  # Checks the bundle for common problems'
        ],
        'category': 'Other'
    },
    'bundle-exec': {
        'desc': 'Execute a command in the context of the bundle',
        'common_flags': {
            '--keep-file-descriptors': 'Passes all file descriptors to the new processes. Default is true from bundler version 2.2.26. Setting it to false is now deprecated.',
            '--gemfile': '=GEMFILE'
        },
        'examples': [
            'bundle-exec  # Execute a command in the context of the bundle'
        ],
        'category': 'Other'
    },
    'bundle-info': {
        'desc': 'Show information for the given gem in your bundle',
        'common_flags': {
            '--path': 'Print the path of the given gem',
            '--version': 'Print gem version'
        },
        'examples': [
            'bundle-info  # Show information for the given gem in your bundle',
            'bundle-info --version  # Show version'
        ],
        'category': 'Other'
    },
    'bundle-init': {
        'desc': 'Generates a Gemfile into the current working directory',
        'common_flags': {
            '--gemspec': '=GEMSPEC',
            '--gemfile': '=GEMFILE'
        },
        'examples': [
            'bundle-init  # Generates a Gemfile into the current working direc'
        ],
        'category': 'Other'
    },
    'bundle-inject': {
        'desc': 'Add named gem(s) with version requirements to Gemfile',
        'common_flags': {
            '--source': '=SOURCE',
            '--group': '=GROUP'
        },
        'examples': [
            'bundle-inject  # Add named gem(s) with version requirements to Gemf'
        ],
        'category': 'Other'
    },
    'bundle-install': {
        'desc': 'Install the dependencies specified in your Gemfile',
        'common_flags': {
            '--binstubs': '[=BINSTUBS]',
            '--clean': 'On finishing the installation Bundler is going to remove any gems not present in the current Gemfile(5). Don\'t worry, gems currently in use',
            '--deployment': 'In deployment mode, Bundler will \'roll-out\' the bundle for production or CI use. Please check carefully if you want to have this option en‐',
            '--redownload': 'Force download every gem, even if the required versions are already available locally.',
            '--force': 'Force download every gem, even if the required versions are already available locally.',
            '--frozen': 'Do not allow the Gemfile.lock to be updated after this install. Exits non-zero if there are going to be changes to the Gemfile.lock.',
            '--full-index': 'Bundler will not call Rubygems\' API endpoint (default) but download and cache a (currently big) index file of all gems. Performance can be',
            '--gemfile': '=GEMFILE',
            '--jobs': '=<number>, -j=<number>',
            '--local': 'Do not attempt to connect to rubygems.org. Instead, Bundler will use the gems already present in Rubygems\' cache or in vendor/cache. Note',
            '--prefer-local': 'Force using locally installed gems, or gems already present in Rubygems\' cache or in vendor/cache, when resolving, even if newer versions are',
            '--no-cache': 'Do not update the cache in vendor/cache with the newly bundled gems. This does not remove any gems in the cache but keeps the newly bundled',
            '--no-prune': 'Don\'t remove stale gems from the cache when the installation finishes.',
            '--path': '=PATH',
            '--quiet': 'Do not print progress information to the standard output.'
        },
        'examples': [
            'bundle-install  # Install the dependencies specified in your Gemfile'
        ],
        'category': 'Other'
    },
    'bundle-list': {
        'desc': 'List all the gems in the bundle',
        'common_flags': {
            '--name-only': 'Print only the name of each gem.',
            '--paths': 'Print the path to each gem in the bundle.',
            '--without-group': '=<list>',
            '--only-group': '=<list>'
        },
        'examples': [
            'bundle-list  # List all the gems in the bundle'
        ],
        'category': 'Other'
    },
    'bundle-lock': {
        'desc': 'Creates / Updates a lockfile without installing',
        'common_flags': {
            '--update': '[=<list>]',
            '--bundler': '[=BUNDLER]',
            '--local': 'Do not attempt to connect to rubygems.org. Instead, Bundler will use the gems already present in Rubygems\' cache or in vendor/cache. Note',
            '--print': 'Prints the lockfile to STDOUT instead of writing to the file system.',
            '--lockfile': '=LOCKFILE',
            '--full-index': 'Fall back to using the single-file index of all gems.',
            '--gemfile': '=GEMFILE',
            '--add-checksums': 'Add checksums to the lockfile.',
            '--add-platform': '=<list>',
            '--remove-platform': '=<list>',
            '--normalize-platforms': 'Normalize lockfile platforms.',
            '--patch': 'If updating, prefer updating only to next patch version.',
            '--minor': 'If updating, prefer updating only to next minor version.',
            '--major': 'If updating, prefer updating to next major version (default).',
            '--pre': 'If updating, always choose the highest allowed version, regardless of prerelease status.'
        },
        'examples': [
            'bundle-lock  # Creates / Updates a lockfile without installing'
        ],
        'category': 'Other'
    },
    'bundle-open': {
        'desc': 'Opens the source directory for a gem in your bundle',
        'common_flags': {
            '--path': '[=PATH]'
        },
        'examples': [
            'bundle-open  # Opens the source directory for a gem in your bundl'
        ],
        'category': 'Other'
    },
    'bundle-outdated': {
        'desc': 'List installed gems with newer versions available',
        'common_flags': {
            '--local': 'Do not attempt to fetch gems remotely and use the gem cache instead.',
            '--pre': 'Check for newer pre-release gems.',
            '--source': '=<list>',
            '--filter-strict': 'Only list newer versions allowed by your Gemfile requirements, also respecting conservative update flags (--patch, --minor, --major).',
            '--strict': 'Only list newer versions allowed by your Gemfile requirements, also respecting conservative update flags (--patch, --minor, --major).',
            '--update-strict': 'Strict conservative resolution, do not allow any gem to be updated past latest --patch | --minor | --major.',
            '--parseable': 'Use minimal formatting for more parseable output.',
            '--porcelain': 'Use minimal formatting for more parseable output.',
            '--group': '=GROUP',
            '--groups': 'List gems organized by groups.',
            '--minor': 'Prefer updating only to next minor version.',
            '--major': 'Prefer updating to next major version (default).',
            '--patch': 'Prefer updating only to next patch version.',
            '--filter-major': 'Only list major newer versions.',
            '--filter-minor': 'Only list minor newer versions.'
        },
        'examples': [
            'bundle-outdated  # List installed gems with newer versions available'
        ],
        'category': 'Other'
    },
    'bundle-platform': {
        'desc': 'Displays platform compatibility information',
        'common_flags': {
            '--ruby': 'It will display the ruby directive information, so you don\'t have to parse it from the Gemfile(5).'
        },
        'examples': [
            'bundle-platform  # Displays platform compatibility information'
        ],
        'category': 'Other'
    },
    'bundle-remove': {
        'desc': 'Removes gems from the Gemfile',
        'common_flags': {
            '--install': 'Runs bundle install after the given gems have been removed from the Gemfile, which ensures that both the lockfile and the installed gems on'
        },
        'examples': [
            'bundle-remove  # Removes gems from the Gemfile'
        ],
        'category': 'Other'
    },
    'bundle-show': {
        'desc': 'Shows all the gems in your bundle, or the path to a gem',
        'common_flags': {
            '--paths': 'List the paths of all gems that are required by your [Gemfile(5)][Gemfile(5)], sorted by gem name.',
            '--outdated': 'Show verbose output including whether gems are outdated.'
        },
        'examples': [
            'bundle-show  # Shows all the gems in your bundle, or the path to '
        ],
        'category': 'Other'
    },
    'bundle-update': {
        'desc': 'Update your gems to the latest available versions',
        'common_flags': {
            '--all': 'Update all gems specified in Gemfile.',
            '--group': '=<list>, -g=<list>',
            '--source': '=<list>',
            '--local': 'Do not attempt to fetch gems remotely and use the gem cache instead.',
            '--ruby': 'Update the locked version of Ruby to the current version of Ruby.',
            '--bundler': '[=BUNDLER]',
            '--full-index': 'Fall back to using the single-file index of all gems.',
            '--gemfile': '=GEMFILE',
            '--jobs': '=<number>, -j=<number>',
            '--retry': '=[<number>]',
            '--quiet': 'Only output warnings and errors.',
            '--redownload': 'Force downloading every gem.',
            '--force': 'Force downloading every gem.',
            '--patch': 'Prefer updating only to next patch version.',
            '--minor': 'Prefer updating only to next minor version.'
        },
        'examples': [
            'bundle-update  # Update your gems to the latest available versions',
            'bundle-update --all  # Show all'
        ],
        'category': 'Other'
    },
    'bundle-viz': {
        'desc': 'Generates a visual dependency graph for your Gemfile',
        'common_flags': {
            '--file': '=FILE, -f=FILE',
            '--format': '=FORMAT, -F=FORMAT',
            '--requirements': 'Set to show the version of each required dependency.',
            '-R': 'Set to show the version of each required dependency.',
            '--version': 'Set to show each gem version.',
            '-v': 'Set to show each gem version.',
            '--without': '=<list>, -W=<list>'
        },
        'examples': [
            'bundle-viz  # Generates a visual dependency graph for your Gemfi',
            'bundle-viz -v  # Show version',
            'bundle-viz -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'bundler': {
        'desc': 'Ruby Dependency Management',
        'common_flags': {
            '--no-color': 'Print all output without color',
            '--retry': 'Specify the number of times you wish to attempt network commands',
            '-r': 'Specify the number of times you wish to attempt network commands',
            '--verbose': 'Print out additional logging information',
            '-V': 'Print out additional logging information'
        },
        'examples': [
            'bundler  # Ruby Dependency Management',
            'bundler -V  # Show version',
            'bundler --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'bunzip2': {
        'desc': 'a block-sorting file compressor, v1.0.8',
        'common_flags': {
            '-c': '--stdout',
            '-d': '--decompress',
            '-z': '--compress',
            '-t': '--test',
            '-f': '--force',
            '-k': '--keep',
            '-s': '--small',
            '-q': '--quiet',
            '-v': '--verbose',
            '-h': '--help',
            '-L': '--license -V --version',
            '-1': '(or --fast) to -9 (or --best)',
            '--repetitive-fast': '--repetitive-best'
        },
        'examples': [
            'bunzip2  # a block-sorting file compressor, v1.0.8',
            'bunzip2 -h  # Show help',
            'bunzip2 -v  # Show version',
            'bunzip2 -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'busctl': {
        'desc': 'Introspect the bus',
        'common_flags': {
            '--address': '=ADDRESS',
            '--show-machine': 'When showing the list of peers, show a column containing the names of containers they belong to. See systemd-machined.service(8).',
            '--unique': 'When showing the list of peers, show only \"unique\" names (of the form \":number.number\").',
            '--acquired': 'The opposite of --unique — only \"well-known\" names will be shown.',
            '--activatable': 'When showing the list of peers, show only peers which have actually not been activated yet, but may be started automatically if accessed.',
            '--match': '=MATCH',
            '--size': '=',
            '--list': 'When used with the tree command, shows a flat list of object paths instead of a tree.',
            '-q': 'When used with the call command, suppresses display of the response message payload. Note that even if this option is specified, errors returned',
            '--quiet': 'When used with the call command, suppresses display of the response message payload. Note that even if this option is specified, errors returned',
            '--verbose': 'When used with the call or get-property command, shows output in a more verbose format.',
            '--xml-interface': 'When used with the introspect call, dump the XML description received from the D-Bus org.freedesktop.DBus.Introspectable.Introspect call instead',
            '--json': '=MODE',
            '-j': 'Equivalent to --json=pretty when invoked interactively from a terminal. Otherwise equivalent to --json=short, in particular when the output is',
            '--expect-reply': '=BOOL'
        },
        'examples': [
            'busctl  # Introspect the bus',
            'busctl --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'bzcat': {
        'desc': 'decompresses files to stdout',
        'common_flags': {
            '-c': '--stdout',
            '-d': '--decompress',
            '-z': '--compress',
            '-t': '--test',
            '-f': '--force',
            '-k': '--keep',
            '-s': '--small',
            '-q': '--quiet',
            '-v': '--verbose',
            '-h': '--help',
            '-L': '--license -V --version',
            '-1': '(or --fast) to -9 (or --best)',
            '--repetitive-fast': '--repetitive-best'
        },
        'examples': [
            'bzcat  # decompresses files to stdout',
            'bzcat -h  # Show help',
            'bzcat -v  # Show version',
            'bzcat -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'bzexe': {
        'desc': 'compress executable files in place',
        'common_flags': {
            '-d': 'Decompress the given executables instead of compressing them.'
        },
        'examples': [
            'bzexe  # compress executable files in place'
        ],
        'category': 'Other'
    },
    'bzip2': {
        'desc': 'a block-sorting file compressor, v1.0.8',
        'common_flags': {
            '-c': '--stdout',
            '-d': '--decompress',
            '-z': '--compress',
            '-t': '--test',
            '-f': '--force',
            '-k': '--keep',
            '-s': '--small',
            '-q': '--quiet',
            '-v': '--verbose',
            '-h': '--help',
            '-L': '--license -V --version',
            '-1': '(or --fast) to -9 (or --best)',
            '--repetitive-fast': '--repetitive-best'
        },
        'examples': [
            'bzip2  # a block-sorting file compressor, v1.0.8',
            'bzip2 -h  # Show help',
            'bzip2 -v  # Show version',
            'bzip2 -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'bzip2recover': {
        'desc': 'recovers data from damaged bzip2 files',
        'common_flags': {
            '-c': '--stdout',
            '-d': '--decompress',
            '-z': '--compress',
            '-t': '--test',
            '-f': '--force',
            '-k': '--keep',
            '-s': '--small',
            '-q': '--quiet',
            '-v': '--verbose',
            '-h': '--help',
            '-L': '--license -V --version',
            '-1': '(or --fast) to -9 (or --best)',
            '--repetitive-fast': '--repetitive-best'
        },
        'examples': [
            'bzip2recover  # recovers data from damaged bzip2 files',
            'bzip2recover -h  # Show help',
            'bzip2recover -v  # Show version',
            'bzip2recover -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'capsh': {
        'desc': 'capability shell wrapper',
        'common_flags': {
            '--help': 'Display the list of commands supported by capsh.',
            '--print': 'Display prevailing capability and related state.',
            '--current': 'Display prevailing capability state, 1e capabilities and IAB vector.',
            '--caps': '=cap-set',
            '--drop': '=cap-list',
            '--inh': '=cap-list',
            '--user': '=username',
            '--mode': '=<mode>',
            '--modes': 'Lists all of the libcap modes supported by --mode=<mode>.',
            '--inmode': '=<mode>',
            '--uid': '=id',
            '--cap-uid': '=<uid>',
            '--is-uid': '=<id>',
            '--gid': '=<id>',
            '--is-gid': '=<id>'
        },
        'examples': [
            'capsh  # capability shell wrapper',
            'capsh --help  # Show help'
        ],
        'category': 'Other'
    },
    'cardos-tool': {
        'desc': 'displays information about Card OS-based security tokens or format them',
        'common_flags': {
            '--format': 'Format the card or token.',
            '-f': 'Format the card or token.',
            '--help': 'Print help message on screen.',
            '-h': 'Print help message on screen.',
            '--info': 'Display information about the card or token.',
            '-i': 'Display information about the card or token.',
            '--reader': 'arg, -r arg',
            '--startkey': 'arg, -s arg',
            '--change-startkey': 'arg, -S arg',
            '--verbose': 'Causes cardos-tool to be more verbose. Specify this flag several times to enable debug output in the opensc library.',
            '-v': 'Causes cardos-tool to be more verbose. Specify this flag several times to enable debug output in the opensc library.',
            '--wait': 'Causes cardos-tool to wait for the token to be inserted into reader.',
            '-w': 'Causes cardos-tool to wait for the token to be inserted into reader.'
        },
        'examples': [
            'cardos-tool  # displays information about Card OS-based security ',
            'cardos-tool -h  # Show help',
            'cardos-tool -v  # Show version',
            'cardos-tool -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'chage': {
        'desc': 'change user password expiry information',
        'common_flags': {
            '-d': 'LAST_DAY',
            '--lastday': 'LAST_DAY',
            '-E': 'EXPIRE_DATE',
            '--expiredate': 'EXPIRE_DATE',
            '-h': 'Display help message and exit.',
            '--help': 'Display help message and exit.',
            '-i': 'When printing dates, use YYYY-MM-DD format.',
            '--iso8601': 'When printing dates, use YYYY-MM-DD format.',
            '-I': 'INACTIVE',
            '--inactive': 'INACTIVE',
            '-l': 'Show account aging information.',
            '--list': 'Show account aging information.',
            '-m': 'MIN_DAYS',
            '--mindays': 'MIN_DAYS',
            '-M': 'MAX_DAYS'
        },
        'examples': [
            'chage  # change user password expiry information',
            'chage -h  # Show help'
        ],
        'category': 'Other'
    },
    'chattr': {
        'desc': 'change file attributes on a Linux file system',
        'common_flags': {
            '-R': 'Recursively change attributes of directories and their contents.',
            '-V': 'Be verbose with chattr\'s output and print the program version.',
            '-f': 'Suppress most error messages.',
            '-v': 'version',
            '-p': 'project'
        },
        'examples': [
            'chattr  # change file attributes on a Linux file system',
            'chattr -v  # Show version',
            'chattr -v  # Verbose output',
            'chattr -R -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'chfn': {
        'desc': 'change real user name and information',
        'common_flags': {
            '-f': 'FULL_NAME',
            '--full-name': 'FULL_NAME',
            '-h': 'HOME_PHONE',
            '--home-phone': 'HOME_PHONE',
            '-o': 'OTHER',
            '--other': 'OTHER',
            '-r': 'ROOM_NUMBER',
            '--room': 'ROOM_NUMBER',
            '-R': 'CHROOT_DIR',
            '--root': 'CHROOT_DIR',
            '-u': 'Display help message and exit.',
            '--help': 'Display help message and exit.',
            '-w': 'WORK_PHONE',
            '--work-phone': 'WORK_PHONE'
        },
        'examples': [
            'chfn  # change real user name and information',
            'chfn -h  # Show help',
            'chfn -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'chmod': {
        'desc': 'change file mode bits',
        'common_flags': {
            '-c': 'like verbose but report only when a change is made',
            '--changes': 'like verbose but report only when a change is made',
            '-f': 'suppress most error messages',
            '--silent': 'suppress most error messages',
            '--quiet': 'suppress most error messages',
            '-v': 'output a diagnostic for every file processed',
            '--verbose': 'output a diagnostic for every file processed',
            '--dereference': 'affect the referent of each symbolic link, rather than the symbolic link itself',
            '-h': 'affect each symbolic link, rather than the referent',
            '--no-dereference': 'affect each symbolic link, rather than the referent',
            '--no-preserve-root': 'do not treat \'/\' specially (the default)',
            '--preserve-root': 'fail to operate recursively on \'/\'',
            '--reference': '=RFILE',
            '-R': 'change files and directories recursively',
            '--recursive': 'change files and directories recursively'
        },
        'examples': [
            'chmod  # change file mode bits',
            'chmod -h  # Show help',
            'chmod -v  # Show version',
            'chmod -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'choom': {
        'desc': 'display and adjust OOM-killer score.',
        'common_flags': {
            '-p': 'pid',
            '--pid': 'pid',
            '-n': 'value',
            '--adjust': 'value',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'choom  # display and adjust OOM-killer score.',
            'choom -h  # Show help',
            'choom --version  # Show version'
        ],
        'category': 'Other'
    },
    'chown': {
        'desc': 'change file owner and group',
        'common_flags': {
            '-c': 'like verbose but report only when a change is made',
            '--changes': 'like verbose but report only when a change is made',
            '-f': 'suppress most error messages',
            '--silent': 'suppress most error messages',
            '--quiet': 'suppress most error messages',
            '-v': 'output a diagnostic for every file processed',
            '--verbose': 'output a diagnostic for every file processed',
            '--dereference': 'affect the referent of each symbolic link (this is the default), rather than the symbolic link itself',
            '-h': 'affect symbolic links instead of any referenced file (useful only on systems that can change the ownership of a symlink)',
            '--no-dereference': 'affect symbolic links instead of any referenced file (useful only on systems that can change the ownership of a symlink)',
            '--from': '=CURRENT_OWNER:CURRENT_GROUP',
            '--no-preserve-root': 'do not treat \'/\' specially (the default)',
            '--preserve-root': 'fail to operate recursively on \'/\'',
            '--reference': '=RFILE',
            '-R': 'operate on files and directories recursively'
        },
        'examples': [
            'chown  # change file owner and group',
            'chown -h  # Show help',
            'chown -v  # Show version',
            'chown -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'chrt': {
        'desc': 'manipulate the real-time attributes of a process',
        'common_flags': {
            '-T': 'nanoseconds',
            '--sched-runtime': 'nanoseconds',
            '-P': 'nanoseconds',
            '--sched-period': 'nanoseconds',
            '-D': 'nanoseconds',
            '--sched-deadline': 'nanoseconds',
            '-R': 'Use SCHED_RESET_ON_FORK or SCHED_FLAG_RESET_ON_FORK flag. Linux-specific, supported since 2.6.31.',
            '--reset-on-fork': 'Use SCHED_RESET_ON_FORK or SCHED_FLAG_RESET_ON_FORK flag. Linux-specific, supported since 2.6.31.'
        },
        'examples': [
            'chrt  # manipulate the real-time attributes of a process'
        ],
        'category': 'Other'
    },
    'chsh': {
        'desc': 'change login shell',
        'common_flags': {
            '-h': 'Display help message and exit.',
            '--help': 'Display help message and exit.',
            '-R': 'CHROOT_DIR',
            '--root': 'CHROOT_DIR',
            '-s': 'SHELL',
            '--shell': 'SHELL'
        },
        'examples': [
            'chsh  # change login shell',
            'chsh -h  # Show help'
        ],
        'category': 'Other'
    },
    'cifsiostat': {
        'desc': 'Report CIFS statistics.',
        'common_flags': {
            '--dec': '={ 0 | 1 | 2 }',
            '-h': 'This option is equivalent to specifying --human --pretty.',
            '--human': 'Print sizes in human readable format (e.g. 1.0k, 1.2M, etc.) The units displayed with this option supersede any other default units (e.g.',
            '-k': 'Display statistics in kilobytes per second.',
            '-m': 'Display statistics in megabytes per second.',
            '--pretty': 'Make the CIFS report easier to read by a human.',
            '-t': 'Print the time for each report displayed. The timestamp format may depend on the value of the S_TIME_FORMAT environment variable (see below).',
            '-V': 'Print version number then exit.'
        },
        'examples': [
            'cifsiostat  # Report CIFS statistics.',
            'cifsiostat -h  # Show help',
            'cifsiostat -V  # Show version'
        ],
        'category': 'Other'
    },
    'clear': {
        'desc': 'clear the terminal screen',
        'common_flags': {
            '-T': 'type produces instructions suitable for the terminal type. Normally, this option is unnecessary, because the terminal type is inferred from the',
            '-V': 'reports the version of ncurses associated with this program and exits with a successful status.',
            '-x': 'prevents clear from attempting to clear the scrollback buffer.'
        },
        'examples': [
            'clear  # clear the terminal screen',
            'clear -V  # Show version'
        ],
        'category': 'Other'
    },
    'clusterdb': {
        'desc': 'cluster a PostgreSQL database',
        'common_flags': {
            '-a': '--all',
            '-e': '--echo',
            '-q': '--quiet',
            '-t': 'table',
            '--table': '=table',
            '-v': '--verbose',
            '-V': '--version',
            '--help': 'Show help about clusterdb command line arguments, and exit.',
            '-h': 'host',
            '--host': '=host',
            '-p': 'port',
            '--port': '=port',
            '-U': 'username',
            '--username': '=username',
            '-w': '--no-password'
        },
        'examples': [
            'clusterdb  # cluster a PostgreSQL database',
            'clusterdb -h  # Show help',
            'clusterdb -v  # Show version',
            'clusterdb -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'colcrt': {
        'desc': 'filter nroff output for CRT previewing',
        'common_flags': {
            '-2': 'Causes all half-lines to be printed, effectively double spacing the output. Normally, a minimal space output format is used which will suppress',
            '--half-lines': 'Causes all half-lines to be printed, effectively double spacing the output. Normally, a minimal space output format is used which will suppress',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'colcrt  # filter nroff output for CRT previewing',
            'colcrt -h  # Show help',
            'colcrt --version  # Show version'
        ],
        'category': 'Other'
    },
    'colrm': {
        'desc': 'remove columns from a file',
        'common_flags': {
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'colrm  # remove columns from a file',
            'colrm -h  # Show help',
            'colrm --version  # Show version'
        ],
        'category': 'Other'
    },
    'column': {
        'desc': 'columnate lists',
        'common_flags': {
            '-J': 'Use JSON output format to print the table. The option --table-columns is required and the option --table-name is recommended.',
            '--json': 'Use JSON output format to print the table. The option --table-columns is required and the option --table-name is recommended.',
            '-c': 'width',
            '--output-width': 'width',
            '-d': 'Omit printing the header. This option allows the use of user supplied column names on the command line, but keeps the header hidden when',
            '--table-noheadings': 'Omit printing the header. This option allows the use of user supplied column names on the command line, but keeps the header hidden when',
            '-o': 'string',
            '--output-separator': 'string',
            '-s': 'separators',
            '--separator': 'separators',
            '-S': 'number',
            '--use-spaces': 'number',
            '-t': 'Determine the number of columns the input contains and create a table. Columns are by default delimited with whitespace, or with characters',
            '--table': 'Determine the number of columns the input contains and create a table. Columns are by default delimited with whitespace, or with characters',
            '-C': 'attributes'
        },
        'examples': [
            'column  # columnate lists'
        ],
        'category': 'Other'
    },
    'corelist': {
        'desc': 'a commandline frontend to Module::CoreList',
        'common_flags': {
            '-a': 'lists all versions of the given module (or the matching modules, in case you used a module regexp) in the perls Module::CoreList knows about.',
            '-d': 'finds the first perl version where a module has been released by date, and not by version number (as is the default).',
            '--diff': 'Given two versions of perl, this prints a human-readable table of all module changes between the two. The output format may change in the',
            '-m': 'an',
            '-v': 'lists all of the perl release versions we got the CoreList for.',
            '-r': 'lists all of the perl releases and when they were released',
            '--utils': 'lists the first version of perl each named utility program was released with',
            '--feature': 'lists the first version bundle of each named feature given',
            '-f': 'lists the first version bundle of each named feature given',
            '--upstream': 'Shows if the given module is primarily maintained in perl core or on CPAN and bug tracker URL.',
            '-u': 'Shows if the given module is primarily maintained in perl core or on CPAN and bug tracker URL.'
        },
        'examples': [
            'corelist  # a commandline frontend to Module::CoreList',
            'corelist -v  # Show version',
            'corelist -v  # Verbose output',
            'corelist -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'cpan': {
        'desc': 'easily interact with CPAN from the command line',
        'common_flags': {
            '-a': 'Creates a CPAN.pm autobundle with CPAN::Shell->autobundle.',
            '-A': 'module [ module ... ]',
            '-c': 'module',
            '-C': 'module [ module ... ]',
            '-D': 'module [ module ... ]',
            '-f': 'Force the specified action, when it normally would have failed. Use this to install a module even if its tests fail. When you use this option,',
            '-i': 'module [ module ... ]',
            '-F': 'Turn off CPAN.pm\'s attempts to lock anything. You should be careful with this since you might end up with multiple scripts trying to muck in the',
            '-g': 'module [ module ... ]',
            '-G': 'module [ module ... ]',
            '-h': 'Print a help message and exit. When you specify \"-h\", it ignores all of the other options and arguments.',
            '-I': 'Load \"local::lib\" (think like \"-I\" for loading lib paths). Too bad \"-l\" was already taken.',
            '-j': 'Config.pm',
            '-J': 'Dump the configuration in the same format that CPAN.pm uses. This is useful for checking the configuration as well as using the dump as a',
            '-l': 'List all installed modules with their versions'
        },
        'examples': [
            'cpan  # easily interact with CPAN from the command line',
            'cpan -h  # Show help',
            'cpan -a  # Show all'
        ],
        'category': 'Other'
    },
    'cpan5.40-x86_64-linux-gnu': {
        'desc': 'easily interact with CPAN from the command line',
        'common_flags': {
            '-a': 'Creates a CPAN.pm autobundle with CPAN::Shell->autobundle.',
            '-A': 'module [ module ... ]',
            '-c': 'module',
            '-C': 'module [ module ... ]',
            '-D': 'module [ module ... ]',
            '-f': 'Force the specified action, when it normally would have failed. Use this to install a module even if its tests fail. When you use this option,',
            '-i': 'module [ module ... ]',
            '-F': 'Turn off CPAN.pm\'s attempts to lock anything. You should be careful with this since you might end up with multiple scripts trying to muck in the',
            '-g': 'module [ module ... ]',
            '-G': 'module [ module ... ]',
            '-h': 'Print a help message and exit. When you specify \"-h\", it ignores all of the other options and arguments.',
            '-I': 'Load \"local::lib\" (think like \"-I\" for loading lib paths). Too bad \"-l\" was already taken.',
            '-j': 'Config.pm',
            '-J': 'Dump the configuration in the same format that CPAN.pm uses. This is useful for checking the configuration as well as using the dump as a',
            '-l': 'List all installed modules with their versions'
        },
        'examples': [
            'cpan5.40-x86_64-linux-gnu  # easily interact with CPAN from the command line',
            'cpan5.40-x86_64-linux-gnu -h  # Show help',
            'cpan5.40-x86_64-linux-gnu -a  # Show all'
        ],
        'category': 'Other'
    },
    'cpio': {
        'desc': 'copy files to and from archives',
        'common_flags': {
            '--block-size': '=BLOCK-SIZE',
            '-B': 'Set the I/O block size to 5120 bytes.',
            '-c': 'Use the old portable (ASCII) archive format. This is the same as -H odc.',
            '-C': '=NUMBER',
            '--io-size': '=NUMBER',
            '-D': '=DIR',
            '--directory': '=DIR',
            '--force-local': 'Archive file is local, even if its name contains colons.',
            '-H': '=FORMAT',
            '--format': '=FORMAT',
            '-R': '=[USER][:.][GROUP]',
            '--owner': '=[USER][:.][GROUP]',
            '--quiet': 'Do not print the number of blocks copied at the end of the run.',
            '--rsh-command': '=COMMAND',
            '-v': 'Verbosely list the files processed.'
        },
        'examples': [
            'cpio  # copy files to and from archives',
            'cpio -v  # Show version',
            'cpio -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'createdb': {
        'desc': 'create a new PostgreSQL database',
        'common_flags': {
            '-D': 'tablespace',
            '--tablespace': '=tablespace',
            '-e': '--echo',
            '-E': 'encoding',
            '--encoding': '=encoding',
            '-l': 'locale',
            '--locale': '=locale',
            '--lc-collate': '=locale',
            '--lc-ctype': '=locale',
            '--builtin-locale': '=locale',
            '--icu-locale': '=locale',
            '--icu-rules': '=rules',
            '--locale-provider': '={builtin|libc|icu}',
            '-O': 'owner',
            '--owner': '=owner'
        },
        'examples': [
            'createdb  # create a new PostgreSQL database'
        ],
        'category': 'Other'
    },
    'createuser': {
        'desc': 'define a new PostgreSQL user account',
        'common_flags': {
            '-a': 'role',
            '--with-admin': '=role',
            '-c': 'number',
            '--connection-limit': '=number',
            '-d': '--createdb',
            '-D': '--no-createdb',
            '-e': '--echo',
            '-E': '--encrypted',
            '-g': 'role',
            '--member-of': '=role',
            '--role': '=role (deprecated)',
            '-i': '--inherit',
            '-I': '--no-inherit',
            '--interactive': 'Prompt for the user name if none is specified on the command line, and also prompt for whichever of the options -d/-D, -r/-R, -s/-S is not',
            '-l': '--login'
        },
        'examples': [
            'createuser  # define a new PostgreSQL user account',
            'createuser -a  # Show all'
        ],
        'category': 'Other'
    },
    'cryptoflex-tool': {
        'desc': 'utility for manipulating Schlumberger Cryptoflex data structures',
        'common_flags': {
            '--app-df': 'num, -a num',
            '--create-key-files': 'arg, -c arg',
            '--create-pin-files': 'id, -P id',
            '--exponent': 'exp, -e exp',
            '--generate-key': 'Generate a new RSA key pair',
            '-g': 'Generate a new RSA key pair',
            '--key-num': 'num, -k num',
            '--list-keys': 'Lists all keys stored in a public key file',
            '-l': 'Lists all keys stored in a public key file',
            '--modulus-length': 'length, -m length',
            '--prkey-file': 'id, -p id',
            '--pubkey-file': 'id, -u id',
            '--read-key': 'Reads a public key from the card, allowing the user to extract and store or use the public key',
            '-R': 'Reads a public key from the card, allowing the user to extract and store or use the public key',
            '--reader': 'arg, -r arg'
        },
        'examples': [
            'cryptoflex-tool  # utility for manipulating Schlumberger Cryptoflex d'
        ],
        'category': 'Other'
    },
    'curl': {
        'desc': 'transfer a URL',
        'common_flags': {
            '--show-error': 'and -v, --verbose.',
            '--stderr': 'and -v, --verbose.',
            '--styled-output': 'and -v, --verbose.',
            '--trace-ascii': 'and -v, --verbose.',
            '--trace-config': 'and -v, --verbose.',
            '--trace-ids': 'and -v, --verbose.',
            '--trace-time': 'and -v, --verbose.',
            '--trace': 'and -v, --verbose.'
        },
        'examples': [
            'curl  # transfer a URL',
            'curl https://api.example.com  # GET request',
            'curl -o output.html https://example.com  # Save to file',
            'curl -X POST -d \'data\' url  # POST request'
        ],
        'category': 'Other'
    },
    'dash': {
        'desc': 'command interpreter (shell)',
        'common_flags': {
            '-r': 'file True if file exists and is readable.',
            '-l': 'also output the PID of the group leader, and just the PID and shell commands of other members of the job.',
            '-p': 'file True if file is a named pipe (FIFO).',
            '-b': 'file True if file exists and is a block special file.',
            '-c': 'file True if file exists and is a character special file.',
            '-d': 'file True if file exists and is a directory.',
            '-e': 'file True if file exists (regardless of type).',
            '-f': 'file True if file exists and is a regular file.',
            '-g': 'file True if file exists and its set group ID flag is set.',
            '-h': 'file True if file exists and is a symbolic link.',
            '-k': 'file True if file exists and its sticky bit is set.',
            '-n': 'string True if the length of string is nonzero.',
            '-s': 'file True if file exists and has a size greater than zero.',
            '-t': 'file_descriptor',
            '-u': 'file True if file exists and its set user ID flag is set.'
        },
        'examples': [
            'dash  # command interpreter (shell)',
            'dash -h  # Show help',
            'dash -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'dbus-daemon': {
        'desc': 'Message bus daemon',
        'common_flags': {
            '--config-file': '=FILE',
            '--fork': 'Force the message bus to fork and become a daemon, even if the configuration file does not specify that it should. In most contexts the',
            '--nofork': 'Force the message bus not to fork and become a daemon, even if the configuration file specifies that it should. On Windows, the dbus-daemon',
            '--print-address': '[=DESCRIPTOR]',
            '--print-pid': '[=DESCRIPTOR]',
            '--session': 'Use the standard configuration file for the per-login-session message bus.',
            '--system': 'Use the standard configuration file for the systemwide message bus.',
            '--version': 'Print the version of the daemon.',
            '--introspect': 'Print the introspection information for all D-Bus internal interfaces.',
            '--address': '[=ADDRESS]',
            '--systemd-activation': 'Enable systemd-style service activation. Only useful in conjunction with the systemd system and session manager on Linux.',
            '--nopidfile': 'Don\'t write a PID file even if one is configured in the configuration files.',
            '--syslog': 'Force the message bus to use the system log for messages, in addition to writing to standard error, even if the configuration file does not',
            '--syslog-only': 'Force the message bus to use the system log for messages, and not duplicate them to standard error. On Unix, this uses the syslog; on Windows,',
            '--nosyslog': 'Force the message bus to use only standard error for messages, even if the configuration file specifies that it should use the system log.'
        },
        'examples': [
            'dbus-daemon  # Message bus daemon',
            'dbus-daemon --version  # Show version'
        ],
        'category': 'Other'
    },
    'dbus-monitor': {
        'desc': 'debug probe to print message bus messages',
        'common_flags': {
            '--system': 'Monitor the system message bus.',
            '--session': 'Monitor the session message bus. (This is the default.)',
            '--address': 'ADDRESS',
            '--profile': 'Use the profiling output format.',
            '--monitor': 'Use the monitoring output format. (This is the default.)'
        },
        'examples': [
            'dbus-monitor  # debug probe to print message bus messages'
        ],
        'category': 'Other'
    },
    'dbus-run-session': {
        'desc': 'start a process as a new D-Bus session',
        'common_flags': {
            '--config-file': '=FILENAME, --config-file FILENAME',
            '--dbus-daemon': '=BINARY, --dbus-daemon BINARY',
            '--help': 'Print usage information and exit.',
            '--version': 'Print the version of dbus-run-session and exit.'
        },
        'examples': [
            'dbus-run-session  # start a process as a new D-Bus session',
            'dbus-run-session --help  # Show help',
            'dbus-run-session --version  # Show version'
        ],
        'category': 'Other'
    },
    'dbus-send': {
        'desc': 'Send a message to a message bus',
        'common_flags': {
            '--dest': '=NAME',
            '--print-reply': '=literal',
            '--reply-timeout': '=MSEC',
            '--system': 'Send to the system message bus.',
            '--session': 'Send to the session message bus. (This is the default.)',
            '--bus': '=ADDRESS',
            '--peer': '=ADDRESS',
            '--sender': '=NAME',
            '--type': '=TYPE'
        },
        'examples': [
            'dbus-send  # Send a message to a message bus'
        ],
        'category': 'Other'
    },
    'dbus-update-activation-environment': {
        'desc': 'update environment used for D-Bus session services',
        'common_flags': {
            '--all': 'Set all environment variables present in the environment used by dbus-update-activation-environment.',
            '--systemd': 'Set environment variables for systemd user services as well as for traditional D-Bus session services.',
            '--verbose': 'Output messages to standard error explaining what dbus-update-activation-environment is doing.'
        },
        'examples': [
            'dbus-update-activation-environment  # update environment used for D-Bus session services',
            'dbus-update-activation-environment --verbose  # Verbose output',
            'dbus-update-activation-environment --all  # Show all'
        ],
        'category': 'Other'
    },
    'dbus-uuidgen': {
        'desc': 'Utility to generate UUIDs',
        'common_flags': {
            '--get': '[=FILENAME]',
            '--ensure': '[=FILENAME]',
            '--version': 'Print the version of dbus-uuidgen'
        },
        'examples': [
            'dbus-uuidgen  # Utility to generate UUIDs',
            'dbus-uuidgen --version  # Show version'
        ],
        'category': 'Other'
    },
    'dd': {
        'desc': 'convert and copy a file',
        'common_flags': {
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'dd  # convert and copy a file',
            'dd --help  # Show help',
            'dd --version  # Show version'
        ],
        'category': 'Other'
    },
    'debconf': {
        'desc': 'run a debconf-using program',
        'common_flags': {
            '-o': 'package, --owner=package',
            '-f': 'type, --frontend=type',
            '-p': 'value, --priority=value',
            '--terse': 'Enables terse output mode. This affects only some frontends.'
        },
        'examples': [
            'debconf  # run a debconf-using program'
        ],
        'category': 'Other'
    },
    'debconf-apt-progress': {
        'desc': 'install packages using debconf to display a progress bar',
        'common_flags': {
            '--config': 'Print environment variables necessary to start up a progress bar frontend.',
            '--start': 'Start up a progress bar, running from 0 to 100 by default. Use --from and --to to use other endpoints.',
            '--from': 'waypoint',
            '--to': 'waypoint',
            '--stop': 'Stop a running progress bar.',
            '--no-progress': 'Avoid starting, stopping, or stepping the progress bar. Progress messages from apt, media change events, and debconf questions will still be',
            '--dlwaypoint': 'percentage',
            '--logfile': 'file',
            '--logstderr': 'Send the normal output from apt to stderr. If you supply neither --logfile nor --logstderr, the normal output from apt will be discarded.'
        },
        'examples': [
            'debconf-apt-progress  # install packages using debconf to display a progre'
        ],
        'category': 'Other'
    },
    'debconf-copydb': {
        'desc': 'copy a debconf database',
        'common_flags': {
            '-p': 'pattern, --pattern pattern',
            '--owner-pattern': 'pattern',
            '-c': 'foo:bar, --config Foo:bar'
        },
        'examples': [
            'debconf-copydb  # copy a debconf database'
        ],
        'category': 'Other'
    },
    'debconf-set-selections': {
        'desc': 'insert new values into the debconf database',
        'common_flags': {
            '--verbose': 'verbose output',
            '-v': 'verbose output',
            '--checkonly': 'only check the input file format, do not save changes to database',
            '-c': 'only check the input file format, do not save changes to database'
        },
        'examples': [
            'debconf-set-selections  # insert new values into the debconf database',
            'debconf-set-selections -v  # Show version',
            'debconf-set-selections -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'debconf-show': {
        'desc': 'query the debconf database',
        'common_flags': {
            '--db': '=dbname',
            '--listowners': 'Lists all owners of questions in the database. Generally an owner is equivalent to a debian package name.',
            '--listdbs': 'Lists all available databases.'
        },
        'examples': [
            'debconf-show  # query the debconf database'
        ],
        'category': 'Other'
    },
    'delv': {
        'desc': 'DNS lookup and validation utility',
        'common_flags': {
            '-a': 'anchor-file',
            '-b': 'address',
            '-c': 'class',
            '-d': 'level',
            '-h': 'This option displays the delv help usage output and exits.',
            '-i': 'This option sets insecure mode, which disables internal DNSSEC validation. (Note, however, that this does not set the CD bit on upstream',
            '-m': 'This option enables memory usage debugging.',
            '-p': 'port#',
            '-q': 'name',
            '-t': 'type',
            '-v': 'This option prints the delv version and exits.',
            '-x': 'addr',
            '-4': 'This option forces delv to only use IPv4.',
            '-6': 'This option forces delv to only use IPv6.'
        },
        'examples': [
            'delv  # DNS lookup and validation utility',
            'delv -h  # Show help',
            'delv -v  # Show version',
            'delv -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'df': {
        'desc': 'report file system space usage',
        'common_flags': {
            '-a': 'include pseudo, duplicate, inaccessible file systems',
            '--all': 'include pseudo, duplicate, inaccessible file systems',
            '-B': '=SIZE',
            '--block-size': '=SIZE',
            '-h': 'print sizes in powers of 1024 (e.g., 1023M)',
            '--human-readable': 'print sizes in powers of 1024 (e.g., 1023M)',
            '-H': 'print sizes in powers of 1000 (e.g., 1.1G)',
            '--si': 'print sizes in powers of 1000 (e.g., 1.1G)',
            '-i': 'list inode information instead of block usage',
            '--inodes': 'list inode information instead of block usage',
            '-k': 'like --block-size=1K',
            '-l': 'limit listing to local file systems',
            '--local': 'limit listing to local file systems',
            '--no-sync': 'do not invoke sync before getting usage info (default)',
            '--output': '[=FIELD_LIST]'
        },
        'examples': [
            'df  # report file system space usage',
            'df -h  # Show help',
            'df -a  # Show all'
        ],
        'category': 'Other'
    },
    'dh_installxmlcatalogs': {
        'desc': 'install and register XML catalog files',
        'common_flags': {
            '-n': 'Do not modify postinst/postrm/prerm scripts.',
            '--noscripts': 'Do not modify postinst/postrm/prerm scripts.'
        },
        'examples': [
            'dh_installxmlcatalogs  # install and register XML catalog files'
        ],
        'category': 'Other'
    },
    'dig': {
        'desc': 'DNS lookup utility',
        'common_flags': {
            '-4': 'This option indicates that only IPv4 should be used.',
            '-6': 'This option indicates that only IPv6 should be used.',
            '-b': 'address[#port]',
            '-c': 'class',
            '-f': 'file',
            '-h': 'Print a usage summary.',
            '-k': 'keyfile',
            '-m': 'This option enables memory usage debugging.',
            '-p': 'port',
            '-q': 'name',
            '-r': 'This option indicates that options from ${HOME}/.digrc should not be read. This is useful for scripts that need predictable behavior.',
            '-t': 'type',
            '-u': 'This option indicates that print query times should be provided in microseconds instead of milliseconds.',
            '-v': 'This option prints the version number and exits.',
            '-x': 'addr'
        },
        'examples': [
            'dig  # DNS lookup utility',
            'dig -h  # Show help',
            'dig -v  # Show version',
            'dig -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-dlltool': {
        'desc': 'create files needed to build and use DLLs',
        'common_flags': {
            '-d': 'filename',
            '--input-def': 'filename',
            '-b': 'filename',
            '--base-file': 'filename',
            '-e': 'filename',
            '--output-exp': 'filename',
            '-z': 'filename',
            '--output-def': 'filename',
            '-l': 'filename',
            '--output-lib': 'filename',
            '-y': 'filename',
            '--output-delaylib': 'filename',
            '--deterministic-libraries': '--non-deterministic-libraries',
            '--export-all-symbols': 'Treat all global and weak defined symbols found in the input object files as symbols to be exported. There is a small list of symbols which are',
            '--no-export-all-symbols': 'Only export symbols explicitly listed in an input .def file or in .drectve sections in the input object files. This is the default behaviour.'
        },
        'examples': [
            'i686-w64-mingw32-dlltool  # create files needed to build and use DLLs'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-dllwrap': {
        'desc': 'Ancient tool for generating PE style dll\'s.',
        'common_flags': {
            '-h': 'Show summary of options.',
            '--help': 'Show summary of options.'
        },
        'examples': [
            'i686-w64-mingw32-dllwrap  # Ancient tool for generating PE style dll\'s.',
            'i686-w64-mingw32-dllwrap -h  # Show help'
        ],
        'category': 'Other'
    },
    'dmesg': {
        'desc': 'print or control the kernel ring buffer',
        'common_flags': {
            '-C': 'Clear the ring buffer.',
            '--clear': 'Clear the ring buffer.',
            '-c': 'Clear the ring buffer after first printing its contents.',
            '--read-clear': 'Clear the ring buffer after first printing its contents.',
            '-D': 'Disable the printing of messages to the console.',
            '--console-off': 'Disable the printing of messages to the console.',
            '-d': 'Display the timestamp and the time delta spent between messages. If used together with --notime then only the time delta without the timestamp',
            '--show-delta': 'Display the timestamp and the time delta spent between messages. If used together with --notime then only the time delta without the timestamp',
            '-E': 'Enable printing messages to the console.',
            '--console-on': 'Enable printing messages to the console.',
            '-e': 'Display the local time and the delta in human-readable format. Be aware that conversion to the local time could be inaccurate (see -T for more',
            '--reltime': 'Display the local time and the delta in human-readable format. Be aware that conversion to the local time could be inaccurate (see -T for more',
            '-F': 'file',
            '--file': 'file',
            '-f': 'list'
        },
        'examples': [
            'dmesg  # print or control the kernel ring buffer'
        ],
        'category': 'Other'
    },
    'dnie-tool': {
        'desc': 'displays information about DNIe based security tokens',
        'common_flags': {
            '--idesp': 'Show the DNIe IDESP value.',
            '-i': 'Show the DNIe IDESP value.',
            '--data': 'Show DNIe personal information. Reads and print DNIe number and User Name and SurName',
            '-d': 'Show DNIe personal information. Reads and print DNIe number and User Name and SurName',
            '--all': 'Displays every available information. This command is equivalent to -d -i -V -s',
            '-a': 'Displays every available information. This command is equivalent to -d -i -V -s',
            '--serial': 'Displays DNIe Serial Number',
            '-s': 'Displays DNIe Serial Number',
            '--version': 'Show DNIe sw version. Displays software version for in-card DNIe OS',
            '-V': 'Show DNIe sw version. Displays software version for in-card DNIe OS',
            '--pin': 'pin, -p pin',
            '--reader': 'arg, -r arg',
            '--wait': 'Causes dnie-tool to wait for the token to be inserted into reader.',
            '-w': 'Causes dnie-tool to wait for the token to be inserted into reader.',
            '--verbose': 'Causes dnie-tool to be more verbose. Specify this flag several times to enable debug output in the opensc library.'
        },
        'examples': [
            'dnie-tool  # displays information about DNIe based security tok',
            'dnie-tool --version  # Show version',
            'dnie-tool --verbose  # Verbose output',
            'dnie-tool -a  # Show all'
        ],
        'category': 'Other'
    },
    'dnsdomainname': {
        'desc': 'show the system\'s DNS domain name',
        'common_flags': {
            '-a': 'Display the alias name of the host (if used). This option is deprecated and should not be used anymore.',
            '--alias': 'Display the alias name of the host (if used). This option is deprecated and should not be used anymore.',
            '-A': 'Displays all FQDNs of the machine. This option enumerates all configured network addresses on all configured network interfaces, and trans‐',
            '--all-fqdns': 'Displays all FQDNs of the machine. This option enumerates all configured network addresses on all configured network interfaces, and trans‐',
            '-b': 'Always set a hostname; this allows the file specified by -F to be non-existent or empty, in which case the default hostname localhost will be',
            '--boot': 'Always set a hostname; this allows the file specified by -F to be non-existent or empty, in which case the default hostname localhost will be',
            '-d': 'Display the name of the DNS domain. Don\'t use the command domainname to get the DNS domain name because it will show the NIS domain name and',
            '--domain': 'Display the name of the DNS domain. Don\'t use the command domainname to get the DNS domain name because it will show the NIS domain name and',
            '-f': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '--fqdn': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '--long': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '-F': 'filename',
            '--file': 'filename',
            '-i': 'Display the network address(es) of the host name. Note that this works only if the host name can be resolved. Avoid using this option; use',
            '--ip-address': 'Display the network address(es) of the host name. Note that this works only if the host name can be resolved. Avoid using this option; use'
        },
        'examples': [
            'dnsdomainname  # show the system\'s DNS domain name',
            'dnsdomainname -a  # Show all'
        ],
        'category': 'Other'
    },
    'dnstap-read': {
        'desc': 'print dnstap data in human-readable form',
        'common_flags': {
            '-m': 'This option indicates trace memory allocations, and is used for debugging memory leaks.',
            '-p': 'This option prints the text form of the DNS message that was encapsulated in the dnstap frame, after printing the dnstap data.',
            '-t': 'This option prints long timestamps with millisecond precision.',
            '-x': 'This option prints a hex dump of the wire form of the DNS message that was encapsulated in the dnstap frame, after printing the dnstap data.',
            '-y': 'This option prints dnstap data in a detailed YAML format.'
        },
        'examples': [
            'dnstap-read  # print dnstap data in human-readable form'
        ],
        'category': 'Other'
    },
    'domainname': {
        'desc': 'show or set the system\'s NIS/YP domain name',
        'common_flags': {
            '-a': 'Display the alias name of the host (if used). This option is deprecated and should not be used anymore.',
            '--alias': 'Display the alias name of the host (if used). This option is deprecated and should not be used anymore.',
            '-A': 'Displays all FQDNs of the machine. This option enumerates all configured network addresses on all configured network interfaces, and trans‐',
            '--all-fqdns': 'Displays all FQDNs of the machine. This option enumerates all configured network addresses on all configured network interfaces, and trans‐',
            '-b': 'Always set a hostname; this allows the file specified by -F to be non-existent or empty, in which case the default hostname localhost will be',
            '--boot': 'Always set a hostname; this allows the file specified by -F to be non-existent or empty, in which case the default hostname localhost will be',
            '-d': 'Display the name of the DNS domain. Don\'t use the command domainname to get the DNS domain name because it will show the NIS domain name and',
            '--domain': 'Display the name of the DNS domain. Don\'t use the command domainname to get the DNS domain name because it will show the NIS domain name and',
            '-f': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '--fqdn': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '--long': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '-F': 'filename',
            '--file': 'filename',
            '-i': 'Display the network address(es) of the host name. Note that this works only if the host name can be resolved. Avoid using this option; use',
            '--ip-address': 'Display the network address(es) of the host name. Note that this works only if the host name can be resolved. Avoid using this option; use'
        },
        'examples': [
            'domainname  # show or set the system\'s NIS/YP domain name',
            'domainname -a  # Show all'
        ],
        'category': 'Other'
    },
    'dpkg': {
        'desc': 'package manager for Debian',
        'common_flags': {
            '--force-remove-reinstreq': '.'
        },
        'examples': [
            'dpkg  # package manager for Debian'
        ],
        'category': 'Other'
    },
    'dpkg-architecture': {
        'desc': 'set and determine the architecture for package building',
        'common_flags': {
            '-a': 'architecture',
            '--host-arch': 'architecture',
            '-t': 'gnu-system-type',
            '--host-type': 'gnu-system-type',
            '-A': 'architecture',
            '--target-arch': 'architecture',
            '-T': 'gnu-system-type',
            '--target-type': 'gnu-system-type',
            '-W': 'architecture-wildcard',
            '--match-wildcard': 'architecture-wildcard',
            '-B': 'architecture-bits',
            '--match-bits': 'architecture-bits',
            '-E': 'architecture-endianness',
            '--match-endian': 'architecture-endianness',
            '--print-format': 'format'
        },
        'examples': [
            'dpkg-architecture  # set and determine the architecture for package bui',
            'dpkg-architecture -a  # Show all'
        ],
        'category': 'Other'
    },
    'dpkg-buildapi': {
        'desc': 'returns the build API level to use during package build',
        'common_flags': {
            '-c': 'control-file'
        },
        'examples': [
            'dpkg-buildapi  # returns the build API level to use during package '
        ],
        'category': 'Other'
    },
    'dpkg-buildflags': {
        'desc': 'returns build flags to use during package build',
        'common_flags': {
            '-f': 'PIC'
        },
        'examples': [
            'dpkg-buildflags  # returns build flags to use during package build'
        ],
        'category': 'Other'
    },
    'dpkg-buildpackage': {
        'desc': 'build binary or source packages from sources',
        'common_flags': {
            '--build': '=type',
            '-g': 'Equivalent to --build=source,all (since dpkg 1.17.11).',
            '-G': 'Equivalent to --build=source,any (since dpkg 1.17.11).',
            '-b': 'Equivalent to --build=binary or --build=any,all.',
            '-B': 'Equivalent to --build=any.',
            '-A': 'Equivalent to --build=all.',
            '-S': 'Equivalent to --build=source.',
            '-F': 'Equivalent to --build=full, --build=source,binary or --build=source,any,all (since dpkg 1.15.8).',
            '--target': 'target[,...]',
            '-T': '=target[,...]',
            '--rules-target': '=target[,...]',
            '--as-root': 'Only meaningful together with --target (since dpkg 1.15.0). Requires that the target be run with root rights.',
            '-s': 'd',
            '-v': 'version',
            '-C': 'changes-description'
        },
        'examples': [
            'dpkg-buildpackage  # build binary or source packages from sources',
            'dpkg-buildpackage -v  # Show version',
            'dpkg-buildpackage -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'dpkg-checkbuilddeps': {
        'desc': 'check build dependencies and conflicts',
        'common_flags': {
            '--admindir': '=dir',
            '-A': 'Ignore Build-Depends-Arch and Build-Conflicts-Arch lines (since dpkg 1.16.4). Use when only arch-indep packages will be built, or combine with',
            '-B': 'Ignore Build-Depends-Indep and Build-Conflicts-Indep lines. Use when only arch-dep packages will be built, or combine with -A when only a',
            '-I': 'Ignore built-in build depends and conflicts (since dpkg 1.18.2). These are implicit dependencies that are usually required on a specific',
            '-d': 'build-depends-string',
            '-c': 'build-conflicts-string',
            '-a': 'arch',
            '-P': 'profile[,...]',
            '--version': 'Show the version and exit.'
        },
        'examples': [
            'dpkg-checkbuilddeps  # check build dependencies and conflicts',
            'dpkg-checkbuilddeps --version  # Show version',
            'dpkg-checkbuilddeps -a  # Show all'
        ],
        'category': 'Other'
    },
    'dpkg-deb': {
        'desc': 'Debian package archive (.deb) manipulation tool',
        'common_flags': {
            '--showformat': 'option in dpkg-query(1).',
            '-z': '=compress-level',
            '--compression-level': '=compress-level',
            '-S': '=compress-strategy',
            '--compression-strategy': '=compress-strategy',
            '-Z': '=compress-type',
            '--compression': '=compress-type',
            '--threads-max': '=threads',
            '--root-owner-group': 'Set the owner and group for each entry in the filesystem tree data to root with id 0 (since dpkg 1.19.0).',
            '--deb-format': '=format',
            '--no-check': 'Inhibits dpkg-deb --build\'s usual checks on the proposed contents of an archive. You can build any archive you want, no matter how broken, this',
            '--nocheck': 'This is an alias for --no-check.',
            '-v': 'Enables verbose output (since dpkg 1.16.1). This currently only affects --extract making it behave like --vextract.',
            '--verbose': 'Enables verbose output (since dpkg 1.16.1). This currently only affects --extract making it behave like --vextract.',
            '-D': 'Enables debugging output. This is not very interesting.'
        },
        'examples': [
            'dpkg-deb  # Debian package archive (.deb) manipulation tool',
            'dpkg-deb -v  # Show version',
            'dpkg-deb -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'dpkg-distaddfile': {
        'desc': 'add entries to debian/files',
        'common_flags': {
            '-f': 'files-list-file',
            '--version': 'Show the version and exit.'
        },
        'examples': [
            'dpkg-distaddfile  # add entries to debian/files',
            'dpkg-distaddfile --version  # Show version'
        ],
        'category': 'Other'
    },
    'dpkg-divert': {
        'desc': 'override a package\'s version of a file',
        'common_flags': {
            '--admindir': 'directory',
            '--instdir': 'directory',
            '--root': 'directory',
            '--divert': 'divert-to',
            '--local': 'Specifies that all packages\' versions of this file are diverted. This means, that there are no exceptions, and whatever package is installed,',
            '--package': 'package',
            '--quiet': 'Quiet mode, i.e. no verbose output.',
            '--rename': 'Actually move the file aside (or back). dpkg-divert will abort operation in case the destination file already exists. This is the common',
            '--no-rename': 'Specifies that the file should not be renamed while adding or removing the diversion into the database (since dpkg 1.19.1). This is intended',
            '--test': 'Test mode, i.e. don\'t actually perform any changes, just demonstrate.',
            '--version': 'Show the version and exit.'
        },
        'examples': [
            'dpkg-divert  # override a package\'s version of a file',
            'dpkg-divert --version  # Show version'
        ],
        'category': 'Other'
    },
    'dpkg-genbuildinfo': {
        'desc': 'generate Debian .buildinfo files',
        'common_flags': {
            '--build': '=type',
            '-c': 'controlfile',
            '-l': 'changelog-file',
            '-f': 'files-list-file',
            '-F': 'changelog-format',
            '-O': '[filename]',
            '-u': 'upload-files-dir',
            '--always-include-kernel': 'By default, the Build-Kernel-Version field will not be written out.',
            '--always-include-path': 'By default, the Build-Path field will only be written if the current directory starts with an allowed pattern.',
            '--admindir': '=dir',
            '-q': 'dpkg-genbuildinfo might produce informative messages on standard error. -q suppresses these messages.',
            '--version': 'Show the version and exit.'
        },
        'examples': [
            'dpkg-genbuildinfo  # generate Debian .buildinfo files',
            'dpkg-genbuildinfo --version  # Show version'
        ],
        'category': 'Other'
    },
    'dpkg-genchanges': {
        'desc': 'generate Debian .changes files',
        'common_flags': {
            '--build': '=type',
            '-g': 'Equivalent to --build=source,all (since dpkg 1.17.11).',
            '-G': 'Equivalent to --build=source,any (since dpkg 1.17.11).',
            '-b': 'Equivalent to --build=binary or --build=any,all.',
            '-B': 'Equivalent to --build=any.',
            '-A': 'Equivalent to --build=all.',
            '-S': 'Equivalent to --build=source.',
            '-s': 'd Forces the exclusion of the original source and includes only the diff.',
            '-v': 'version',
            '-C': 'changes-description',
            '-m': 'maintainer-address',
            '-e': 'maintainer-address',
            '-V': 'name=value',
            '-T': 'substvars-file',
            '-D': 'field=value'
        },
        'examples': [
            'dpkg-genchanges  # generate Debian .changes files',
            'dpkg-genchanges -v  # Show version',
            'dpkg-genchanges -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'dpkg-gencontrol': {
        'desc': 'generate Debian control files',
        'common_flags': {
            '-v': 'version',
            '-V': 'name=value',
            '-T': 'substvars-file',
            '-D': 'field=value',
            '-U': 'field',
            '-c': 'control-file',
            '-l': 'changelog-file',
            '-f': 'files-list-file',
            '-F': 'changelog-format',
            '-p': 'package',
            '-n': 'filename',
            '-i': 's, -ip, -isp',
            '-P': 'package-build-dir',
            '-O': '[filename]',
            '--version': 'Show the version and exit.'
        },
        'examples': [
            'dpkg-gencontrol  # generate Debian control files',
            'dpkg-gencontrol -v  # Show version',
            'dpkg-gencontrol -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'dpkg-gensymbols': {
        'desc': 'generate symbols files (shared library dependency information)',
        'common_flags': {
            '-P': 'package-build-dir',
            '-p': 'package',
            '-v': 'version',
            '-e': 'library-file',
            '-l': 'directory',
            '-I': 'filename',
            '-O': '[filename]',
            '-t': 'Write the symbol file in template mode rather than the format compatible with deb-symbols(5). The main difference is that in the template mode',
            '-c': '[0-4]',
            '-q': 'Keep quiet and never generate a diff between generated symbols file and the template file used as starting point or show any warnings about',
            '-a': 'arch',
            '-d': 'Enable debug mode. Numerous messages are displayed to explain what dpkg-gensymbols does.',
            '-V': 'Enable verbose mode. The generated symbols file contains deprecated symbols as comments. Furthermore in template mode, pattern symbols are',
            '--version': 'Show the version and exit.'
        },
        'examples': [
            'dpkg-gensymbols  # generate symbols files (shared library dependency ',
            'dpkg-gensymbols -v  # Show version',
            'dpkg-gensymbols -v  # Verbose output',
            'dpkg-gensymbols -a  # Show all'
        ],
        'category': 'Other'
    },
    'dpkg-mergechangelogs': {
        'desc': '3-way merge of debian/changelog files',
        'common_flags': {
            '--merge-unreleased': 'Ignore the version number when the entries are marked as UNRELEASED (since dpkg 1.21.0).',
            '-m': 'Drop the part after the last tilde in the version number when doing version comparison to identify if two entries are supposed to be the same or',
            '--merge-prereleases': 'Drop the part after the last tilde in the version number when doing version comparison to identify if two entries are supposed to be the same or',
            '--help': 'Show the usage message and exit.',
            '--version': 'Show the version and exit.'
        },
        'examples': [
            'dpkg-mergechangelogs  # 3-way merge of debian/changelog files',
            'dpkg-mergechangelogs --help  # Show help',
            'dpkg-mergechangelogs --version  # Show version'
        ],
        'category': 'Other'
    },
    'dpkg-name': {
        'desc': 'rename Debian packages to full package names',
        'common_flags': {
            '-a': 'The destination filename will not have the architecture information.',
            '--no-architecture': 'The destination filename will not have the architecture information.',
            '-k': 'Create a symlink, instead of moving.',
            '--symlink': 'Create a symlink, instead of moving.',
            '-o': 'Existing files will be overwritten if they have the same name as the destination filename.',
            '--overwrite': 'Existing files will be overwritten if they have the same name as the destination filename.',
            '-s': '[dir]',
            '--subdir': '[dir]',
            '-c': 'This option can used together with the -s option. If a target directory isn\'t found it will be created automatically.',
            '--create-dir': 'This option can used together with the -s option. If a target directory isn\'t found it will be created automatically.',
            '-v': 'Show the version and exit.',
            '--version': 'Show the version and exit.'
        },
        'examples': [
            'dpkg-name  # rename Debian packages to full package names',
            'dpkg-name -v  # Show version',
            'dpkg-name -v  # Verbose output',
            'dpkg-name -a  # Show all'
        ],
        'category': 'Other'
    },
    'dpkg-parsechangelog': {
        'desc': 'parse Debian changelog files',
        'common_flags': {
            '-l': 'changelog-file',
            '--file': 'changelog-file',
            '-F': 'changelog-format',
            '-L': 'libdir',
            '-S': 'field',
            '--show-field': 'field',
            '--version': 'Show the version and exit.',
            '--format': 'output-format',
            '--reverse': 'Include all changes in reverse order (since dpkg 1.19.1).',
            '--all': 'Include all changes. Note: Other options have no effect when this is in use.',
            '-s': 'version',
            '--since': 'version',
            '-v': 'version',
            '-u': 'version',
            '--until': 'version'
        },
        'examples': [
            'dpkg-parsechangelog  # parse Debian changelog files',
            'dpkg-parsechangelog -v  # Show version',
            'dpkg-parsechangelog -v  # Verbose output',
            'dpkg-parsechangelog --all  # Show all'
        ],
        'category': 'Other'
    },
    'dpkg-query': {
        'desc': 'a tool to query the dpkg database',
        'common_flags': {
            '--admindir': '=dir',
            '--root': '=directory',
            '--load-avail': 'Also load the available file when using the --show and --list commands, which now default to only querying the status file (since dpkg 1.16.2).',
            '--no-pager': 'Disables the use of any pager when showing information (since dpkg 1.19.2).',
            '-f': '=format',
            '--showformat': '=format',
            '-W': 'dpkg'
        },
        'examples': [
            'dpkg-query  # a tool to query the dpkg database'
        ],
        'category': 'Other'
    },
    'dpkg-realpath': {
        'desc': 'print the resolved pathname with DPKG_ROOT support',
        'common_flags': {
            '-z': 'Use a NUL byte to end output lines instead of a new line character (since dpkg 1.20.6).',
            '--zero': 'Use a NUL byte to end output lines instead of a new line character (since dpkg 1.20.6).',
            '--instdir': 'directory',
            '--root': 'directory',
            '--version': 'Show the version and exit.'
        },
        'examples': [
            'dpkg-realpath  # print the resolved pathname with DPKG_ROOT support',
            'dpkg-realpath --version  # Show version'
        ],
        'category': 'Other'
    },
    'dpkg-scanpackages': {
        'desc': 'create Packages index files',
        'common_flags': {
            '-t': 'type',
            '--type': 'type',
            '-e': 'file',
            '--extra-override': 'file',
            '-a': 'arch',
            '--arch': 'arch',
            '-h': 'hash-list',
            '--hash': 'hash-list',
            '-m': 'Include all found packages in the output.',
            '--multiversion': 'Include all found packages in the output.',
            '-M': 'id-string',
            '--medium': 'id-string',
            '--version': 'Show the version and exit.'
        },
        'examples': [
            'dpkg-scanpackages  # create Packages index files',
            'dpkg-scanpackages -h  # Show help',
            'dpkg-scanpackages --version  # Show version',
            'dpkg-scanpackages -a  # Show all'
        ],
        'category': 'Other'
    },
    'dpkg-scansources': {
        'desc': 'create Sources index files',
        'common_flags': {
            '-n': 'Do not sort the index stanzas. Normally they are sorted by source package name.',
            '--no-sort': 'Do not sort the index stanzas. Normally they are sorted by source package name.',
            '-e': 'file',
            '--extra-override': 'file',
            '-s': 'file',
            '--source-override': 'file',
            '--debug': 'Turn debugging on.',
            '--help': 'Show the usage message and exit.',
            '--version': 'Show the version and exit.'
        },
        'examples': [
            'dpkg-scansources  # create Sources index files',
            'dpkg-scansources --help  # Show help',
            'dpkg-scansources --version  # Show version'
        ],
        'category': 'Other'
    },
    'dpkg-shlibdeps': {
        'desc': 'generate shared library substvar dependencies',
        'common_flags': {
            '-e': 'executable',
            '-l': 'directory',
            '-d': 'dependency-field',
            '--package': '=package',
            '-p': 'varname-prefix',
            '-O': '[filename]',
            '-t': 'type',
            '-L': 'local-shlibs-file',
            '-T': 'substvars-file',
            '-v': 'Enable verbose mode (since dpkg 1.14.8). Numerous messages are displayed to explain what dpkg-shlibdeps does.',
            '-x': 'package',
            '-S': 'package-build-dir',
            '-I': 'package-build-dir',
            '--ignore-missing-info': 'Do not fail if dependency information can\'t be found for a shared library (since dpkg 1.14.8). Usage of this option is discouraged, all',
            '--warnings': '=[value|string[,...]]'
        },
        'examples': [
            'dpkg-shlibdeps  # generate shared library substvar dependencies',
            'dpkg-shlibdeps -v  # Show version',
            'dpkg-shlibdeps -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'dpkg-source': {
        'desc': 'Debian source package (.dsc) manipulation tool',
        'common_flags': {
            '-c': 'control-file',
            '-l': 'changelog-file',
            '-F': 'changelog-format',
            '--format': '=value',
            '-V': 'name=value',
            '-T': 'substvars-file',
            '-D': 'field=value',
            '-U': 'field',
            '-Z': 'compression, --compression=compression',
            '-z': 'level, --compression-level=level',
            '-i': '[regex], --diff-ignore[=regex]',
            '--extend-diff-ignore': '=regex',
            '-I': 'by itself adds default --exclude options that will filter out control files and directories of the most common revision control systems,',
            '--no-copy': 'Do not copy original tarballs near the extracted source package (since dpkg 1.14.17).',
            '--no-check': 'Do not check signatures and checksums before unpacking (since dpkg 1.14.17).'
        },
        'examples': [
            'dpkg-source  # Debian source package (.dsc) manipulation tool',
            'dpkg-source -V  # Show version'
        ],
        'category': 'Other'
    },
    'dpkg-split': {
        'desc': 'Debian package archive split/join tool',
        'common_flags': {
            '--depotdir': 'directory',
            '--admindir': 'directory',
            '--root': 'directory',
            '-S': 'kibibytes',
            '--partsize': 'kibibytes',
            '-o': 'complete-output',
            '--output': 'complete-output',
            '-Q': 'When doing automatic queue-or-reassembly dpkg-split usually prints a message if it is given a part that is not a binary package part. This',
            '--npquiet': 'When doing automatic queue-or-reassembly dpkg-split usually prints a message if it is given a part that is not a binary package part. This',
            '--msdos': 'Forces the output filenames generated by --split to be MSDOS-compatible.'
        },
        'examples': [
            'dpkg-split  # Debian package archive split/join tool'
        ],
        'category': 'Other'
    },
    'dpkg-statoverride': {
        'desc': 'override ownership and mode of files',
        'common_flags': {
            '--admindir': 'directory',
            '--instdir': 'directory',
            '--root': 'directory',
            '--force-things': '--no-force-things, --refuse-things',
            '--force': 'Force an action, even if a sanity check would otherwise prohibit it. This is necessary to override an existing override. This option is',
            '--update': 'Immediately try to change the path to the new owner and mode if it exists.',
            '--quiet': 'Be less verbose about what we do.'
        },
        'examples': [
            'dpkg-statoverride  # override ownership and mode of files'
        ],
        'category': 'Other'
    },
    'dpkg-trigger': {
        'desc': 'a package trigger utility',
        'common_flags': {
            '--admindir': '=dir',
            '--root': '=directory',
            '--by-package': '=package',
            '--no-await': 'This option arranges that the calling package T (if any) need not await the processing of this trigger; the interested package(s) I, will not be',
            '--await': 'This option does the inverse of --no-await (since dpkg 1.17.21). If the interested package has declared a “noawait” directive, then this option',
            '--no-act': 'Just test, do not actually change anything.'
        },
        'examples': [
            'dpkg-trigger  # a package trigger utility'
        ],
        'category': 'Other'
    },
    'dpkg-vendor': {
        'desc': 'queries information about distribution vendors',
        'common_flags': {
            '--vendor': 'vendor'
        },
        'examples': [
            'dpkg-vendor  # queries information about distribution vendors'
        ],
        'category': 'Other'
    },
    'dropdb': {
        'desc': 'remove a PostgreSQL database',
        'common_flags': {
            '-e': '--echo',
            '-f': '--force',
            '-i': '--interactive',
            '-V': '--version',
            '--if-exists': 'Do not throw an error if the database does not exist. A notice is issued in this case.',
            '--help': 'Show help about dropdb command line arguments, and exit.',
            '-h': 'host',
            '--host': '=host',
            '-p': 'port',
            '--port': '=port',
            '-U': 'username',
            '--username': '=username',
            '-w': '--no-password',
            '-W': '--password',
            '--maintenance-db': '=dbname'
        },
        'examples': [
            'dropdb  # remove a PostgreSQL database',
            'dropdb -h  # Show help',
            'dropdb -V  # Show version'
        ],
        'category': 'Other'
    },
    'dropuser': {
        'desc': 'remove a PostgreSQL user account',
        'common_flags': {
            '-i': '--interactive',
            '-e': '--echo',
            '-V': '--version',
            '--if-exists': 'Do not throw an error if the user does not exist. A notice is issued in this case.',
            '--help': 'Show help about dropuser command line arguments, and exit.',
            '-h': 'host',
            '--host': '=host',
            '-p': 'port',
            '--port': '=port',
            '-U': 'username',
            '--username': '=username',
            '-w': '--no-password',
            '-W': '--password'
        },
        'examples': [
            'dropuser  # remove a PostgreSQL user account',
            'dropuser -h  # Show help',
            'dropuser -V  # Show version'
        ],
        'category': 'Other'
    },
    'dtrust-tool': {
        'desc': 'displays information about D-Trust signature cards and remove the transport protection',
        'common_flags': {
            '--check-transport-protection': 'In the delivery state the card is locked by a so called transport protection. This option allows to check if the transport protection is still',
            '-c': 'In the delivery state the card is locked by a so called transport protection. This option allows to check if the transport protection is still',
            '--help': 'Print help message on screen.',
            '-h': 'Print help message on screen.',
            '--reader': 'arg, -r arg',
            '--pin-status': 'Show the status of the various PINs. The Card Holder PIN is used for advanced signatures and decryption. It is only defined for signature cards,',
            '-s': 'Show the status of the various PINs. The Card Holder PIN is used for advanced signatures and decryption. It is only defined for signature cards,',
            '--unlock-transport-protection': 'This command removes the transport protection. If first queries for the Transport PIN and then for the new value of the Signature PIN twice.',
            '-u': 'This command removes the transport protection. If first queries for the Transport PIN and then for the new value of the Signature PIN twice.',
            '--verbose': 'Causes dtrust-tool to be more verbose. Specify this flag several times to enable debug output in the opensc library.',
            '-v': 'Causes dtrust-tool to be more verbose. Specify this flag several times to enable debug output in the opensc library.',
            '--wait': 'Causes dtrust-tool to wait for the token to be inserted into reader.',
            '-w': 'Causes dtrust-tool to wait for the token to be inserted into reader.'
        },
        'examples': [
            'dtrust-tool  # displays information about D-Trust signature cards',
            'dtrust-tool -h  # Show help',
            'dtrust-tool -v  # Show version',
            'dtrust-tool -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'echo': {
        'desc': 'display a line of text',
        'common_flags': {
            '-n': 'do not output the trailing newline',
            '-e': 'enable interpretation of backslash escapes',
            '-E': 'disable interpretation of backslash escapes (default)',
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'echo  # display a line of text',
            'echo --help  # Show help',
            'echo --version  # Show version'
        ],
        'category': 'Other'
    },
    'editor': {
        'desc': 'Nano\'s ANOther text editor, inspired by Pico',
        'common_flags': {
            '-A': 'Make the Home key smarter. When Home is pressed anywhere but at the very beginning of non-whitespace characters on a line, the cursor jumps',
            '--smarthome': 'Make the Home key smarter. When Home is pressed anywhere but at the very beginning of non-whitespace characters on a line, the cursor jumps',
            '-B': 'When saving a file, back up the previous version of it, using the current filename suffixed with a tilde (~).',
            '--backup': 'When saving a file, back up the previous version of it, using the current filename suffixed with a tilde (~).',
            '-C': 'directory, --backupdir=directory',
            '-D': 'For the interface, use bold instead of reverse video. This can be overridden for specific elements by setting the options titlecolor,',
            '--boldtext': 'For the interface, use bold instead of reverse video. This can be overridden for specific elements by setting the options titlecolor,',
            '-E': 'Convert each typed tab to spaces — to the number of spaces that a tab at that position would take up. (Note: pasted tabs are not converted.)',
            '--tabstospaces': 'Convert each typed tab to spaces — to the number of spaces that a tab at that position would take up. (Note: pasted tabs are not converted.)',
            '-F': 'Read a file into a new buffer by default.',
            '--multibuffer': 'Read a file into a new buffer by default.',
            '-G': 'Use vim-style file locking when editing files.',
            '--locking': 'Use vim-style file locking when editing files.',
            '-H': 'Save the last hundred search strings and replacement strings and executed commands, so they can be easily reused in later sessions.',
            '--historylog': 'Save the last hundred search strings and replacement strings and executed commands, so they can be easily reused in later sessions.'
        },
        'examples': [
            'editor  # Nano\'s ANOther text editor, inspired by Pico'
        ],
        'category': 'Other'
    },
    'egk-tool': {
        'desc': 'displays information on the German electronic health card (elektronische Gesundheitskarte, eGK)',
        'common_flags': {
            '--help': 'Print help and exit.',
            '-h': 'Print help and exit.',
            '--version': 'Print version and exit.',
            '-V': 'Print version and exit.',
            '--reader': 'arg, -r arg',
            '--verbose': 'Causes egk-tool to be more verbose. Specify this flag several times to be more verbose.',
            '-v': 'Causes egk-tool to be more verbose. Specify this flag several times to be more verbose.',
            '--pd': 'Show \'Persönliche Versichertendaten\' (XML).',
            '--vd': 'Show \'Allgemeine Versichertendaten\' (XML).',
            '--gvd': 'Show \'Geschützte Versichertendaten\' (XML).',
            '--vsd-status': 'Show \'Versichertenstammdaten-Status\'.'
        },
        'examples': [
            'egk-tool  # displays information on the German electronic heal',
            'egk-tool -h  # Show help',
            'egk-tool -v  # Show version',
            'egk-tool -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'egrep': {
        'desc': 'print lines that match patterns',
        'common_flags': {
            '--help': 'Output a usage message and exit.',
            '-V': 'Output the version number of grep and exit.',
            '--version': 'Output the version number of grep and exit.',
            '-E': 'Interpret PATTERNS as extended regular expressions (EREs, see below).',
            '--extended-regexp': 'Interpret PATTERNS as extended regular expressions (EREs, see below).',
            '-F': 'Interpret PATTERNS as fixed strings, not regular expressions.',
            '--fixed-strings': 'Interpret PATTERNS as fixed strings, not regular expressions.',
            '-G': 'Interpret PATTERNS as basic regular expressions (BREs, see below). This is the default.',
            '--basic-regexp': 'Interpret PATTERNS as basic regular expressions (BREs, see below). This is the default.',
            '-P': 'Interpret PATTERNS as Perl-compatible regular expressions (PCREs). This option is experimental when combined with the -z (--null-data)',
            '--perl-regexp': 'Interpret PATTERNS as Perl-compatible regular expressions (PCREs). This option is experimental when combined with the -z (--null-data)',
            '-e': 'PATTERNS, --regexp=PATTERNS',
            '-f': 'FILE, --file=FILE',
            '-i': 'Ignore case distinctions in patterns and input data, so that characters that differ only in case match each other.',
            '--ignore-case': 'Ignore case distinctions in patterns and input data, so that characters that differ only in case match each other.'
        },
        'examples': [
            'egrep  # print lines that match patterns',
            'egrep --help  # Show help',
            'egrep --version  # Show version'
        ],
        'category': 'Other'
    },
    'eidenv': {
        'desc': 'utility for accessing visible data from electronic identity cards',
        'common_flags': {
            '--exec': 'prog, -x prog',
            '--help': 'Print help message on screen.',
            '-h': 'Print help message on screen.',
            '--print': 'Prints all data fields from the card, like validity period, document number etc.',
            '-p': 'Prints all data fields from the card, like validity period, document number etc.',
            '--reader': 'arg, -r arg',
            '--stats': 'Prints key usage statistics (only for Estonian ID card).',
            '-t': 'Prints key usage statistics (only for Estonian ID card).',
            '--version': 'Prints the version of the utility and exits.',
            '-v': 'Prints the version of the utility and exits.',
            '--wait': 'Wait for a card to be inserted',
            '-w': 'Wait for a card to be inserted'
        },
        'examples': [
            'eidenv  # utility for accessing visible data from electronic',
            'eidenv -h  # Show help',
            'eidenv -v  # Show version',
            'eidenv -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'elfedit': {
        'desc': 'update ELF header and program property of ELF files',
        'common_flags': {
            '--output-abiversion': '=version',
            '--enable-x86-feature': '.',
            '--input-mach': '=machine',
            '--output-mach': '=machine',
            '--input-type': '=type',
            '--output-type': '=type',
            '--input-osabi': '=osabi',
            '--output-osabi': '=osabi',
            '--input-abiversion': '=version',
            '--disable-x86-feature': '=feature',
            '-v': '--version',
            '-h': '--help'
        },
        'examples': [
            'elfedit  # update ELF header and program property of ELF file',
            'elfedit -h  # Show help',
            'elfedit -v  # Show version',
            'elfedit -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'eqn': {
        'desc': 'format mathematics (equations) for groff or MathML',
        'common_flags': {
            '--help': 'displays a usage message, while -v and --version show version information; all exit afterward.',
            '-C': 'Recognize .EQ and .EN even when followed by a character other than space or newline.',
            '-d': 'xy Specify delimiters x for left and y for right ends of equations not bracketed by .EQ/.EN. x and y need not be distinct. Any “delim xy”',
            '-f': 'F is equivalent to “gfont F”.',
            '-m': 'n is equivalent to “set minimum_size n”.',
            '-M': 'dir Search dir for eqnrc before those listed in section “Description” above.',
            '-N': 'Prohibit newlines within delimiters. This option allows eqn to recover better from missing closing delimiters.',
            '-p': 'n Set sub- and superscripts n points smaller than the surrounding text. This option is deprecated. eqn normally sets sub- and superscripts at',
            '-r': 'Reduce the type size of subscripts at most once relative to the base type size for the equation.',
            '-R': 'Don\'t load eqnrc.',
            '-s': 'n is equivalent to “gsize n”. This option is deprecated.',
            '-T': 'dev Prepare output for the device dev. In most cases, the effect of this is to define a macro dev with a value of 1; eqnrc uses this to provide'
        },
        'examples': [
            'eqn  # format mathematics (equations) for groff or MathML',
            'eqn --help  # Show help',
            'eqn -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'erb': {
        'desc': 'Ruby Templating',
        'common_flags': {
            '--version': 'Prints the version of erb.',
            '-E': 'external[:internal]',
            '--encoding': 'external[:internal]',
            '-P': 'Disables ruby code evaluation for lines beginning with %.',
            '-S': 'level Specifies the safe level in which eRuby script will run.',
            '-T': 'mode Specifies trim mode (default 0). mode can be one of',
            '-r': 'Load a library',
            '-U': 'can be one of Sets the default value for internal encodings (Encoding.default_internal) to UTF-8.',
            '-d': '--debug Turns on debug mode. $DEBUG will be set to true.',
            '-h': '--help Prints a summary of the options.',
            '-n': 'Used with -x. Prepends the line number to each line in the output.',
            '-v': 'Enables verbose mode. $VERBOSE will be set to true.',
            '-x': 'Converts the eRuby script into Ruby script and prints it without line numbers.'
        },
        'examples': [
            'erb  # Ruby Templating',
            'erb -h  # Show help',
            'erb -v  # Show version',
            'erb -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'erb3.3': {
        'desc': 'Ruby Templating',
        'common_flags': {
            '--version': 'Prints the version of erb.',
            '-E': 'external[:internal]',
            '--encoding': 'external[:internal]',
            '-P': 'Disables ruby code evaluation for lines beginning with %.',
            '-S': 'level Specifies the safe level in which eRuby script will run.',
            '-T': 'mode Specifies trim mode (default 0). mode can be one of',
            '-r': 'Load a library',
            '-U': 'can be one of Sets the default value for internal encodings (Encoding.default_internal) to UTF-8.',
            '-d': '--debug Turns on debug mode. $DEBUG will be set to true.',
            '-h': '--help Prints a summary of the options.',
            '-n': 'Used with -x. Prepends the line number to each line in the output.',
            '-v': 'Enables verbose mode. $VERBOSE will be set to true.',
            '-x': 'Converts the eRuby script into Ruby script and prints it without line numbers.'
        },
        'examples': [
            'erb3.3  # Ruby Templating',
            'erb3.3 -h  # Show help',
            'erb3.3 -v  # Show version',
            'erb3.3 -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'ex': {
        'desc': 'Vi IMproved, a programmer\'s text editor',
        'common_flags': {
            '-c': '{command}',
            '-A': 'If Vim has been compiled with ARABIC support for editing right-to-left oriented files and Arabic keyboard mapping, this option starts',
            '-b': 'Binary mode. A few options will be set that makes it possible to edit a binary or executable file.',
            '-C': 'Compatible. Set the \'compatible\' option. This will make Vim behave mostly like Vi, even though a .vimrc file exists.',
            '-d': '{device}, -dev {device}',
            '-D': 'Debugging. Go to debugging mode when executing the first command from a script.',
            '-e': 'Start Vim in Ex mode, just like the executable was called \"ex\".',
            '-E': 'Start Vim in improved Ex mode, just like the executable was called \"exim\".',
            '-f': 'Foreground. For the GUI version, Vim will not fork and detach from the shell it was started in. On the Amiga, Vim is not restarted to',
            '-F': 'If Vim has been compiled with FKMAP support for editing right-to-left oriented files and Farsi keyboard mapping, this option starts Vim',
            '-g': 'If Vim has been compiled with GUI support, this option enables the GUI. If no GUI support was compiled in, an error message is given',
            '-H': 'If Vim has been compiled with RIGHTLEFT support for editing right-to-left oriented files and Hebrew keyboard mapping, this option starts',
            '-i': '{viminfo}',
            '-l': 'Lisp mode. Sets the \'lisp\' and \'showmatch\' options on.',
            '-L': 'Same as -r.'
        },
        'examples': [
            'ex  # Vi IMproved, a programmer\'s text editor'
        ],
        'category': 'Other'
    },
    'expr': {
        'desc': 'evaluate expressions',
        'common_flags': {
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'expr  # evaluate expressions',
            'expr --help  # Show help',
            'expr --version  # Show version'
        ],
        'category': 'Other'
    },
    'faked': {
        'desc': 'daemon that remembers fake ownership/permissions of files manipulated by fakeroot processes.',
        'common_flags': {
            '--debug': 'Print debugging information on stderr.',
            '--foreground': 'Don\'t fork into the background.',
            '--cleanup': 'number',
            '--key': 'key-number',
            '--save-file': 'save-file',
            '--load': 'Load a previously saved environment from the standard input.',
            '--unknown-is-real': 'Use real ownership of previously-unknown files instead of setting them to root:root.',
            '--port': 'tcp-port'
        },
        'examples': [
            'faked  # daemon that remembers fake ownership/permissions o'
        ],
        'category': 'Other'
    },
    'faked-sysv': {
        'desc': 'daemon that remembers fake ownership/permissions of files manipulated by fakeroot processes.',
        'common_flags': {
            '--debug': 'Print debugging information on stderr.',
            '--foreground': 'Don\'t fork into the background.',
            '--cleanup': 'number',
            '--key': 'key-number',
            '--save-file': 'save-file',
            '--load': 'Load a previously saved environment from the standard input.',
            '--unknown-is-real': 'Use real ownership of previously-unknown files instead of setting them to root:root.',
            '--port': 'tcp-port'
        },
        'examples': [
            'faked-sysv  # daemon that remembers fake ownership/permissions o'
        ],
        'category': 'Other'
    },
    'faked-tcp': {
        'desc': 'daemon that remembers fake ownership/permissions of files manipulated by fakeroot processes.',
        'common_flags': {
            '--debug': 'Print debugging information on stderr.',
            '--foreground': 'Don\'t fork into the background.',
            '--cleanup': 'number',
            '--key': 'key-number',
            '--save-file': 'save-file',
            '--load': 'Load a previously saved environment from the standard input.',
            '--unknown-is-real': 'Use real ownership of previously-unknown files instead of setting them to root:root.',
            '--port': 'tcp-port'
        },
        'examples': [
            'faked-tcp  # daemon that remembers fake ownership/permissions o'
        ],
        'category': 'Other'
    },
    'fakeroot': {
        'desc': 'run a command in an environment faking root privileges for file manipulation',
        'common_flags': {
            '-l': 'library, --lib library',
            '--faked': 'binary',
            '-s': 'save-file',
            '-i': 'load-file',
            '-u': 'Use the real ownership of files previously unknown to fakeroot instead of pretending they are owned by root:root.',
            '--unknown-is-real': 'Use the real ownership of files previously unknown to fakeroot instead of pretending they are owned by root:root.',
            '-b': 'fd Specify fd base (TCP mode only). fd is the minimum file descriptor number to use for TCP connections; this may be important to avoid con‐',
            '-h': 'Display help.',
            '-v': 'Display version.'
        },
        'examples': [
            'fakeroot  # run a command in an environment faking root privil',
            'fakeroot -h  # Show help',
            'fakeroot -v  # Show version',
            'fakeroot -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'fakeroot-sysv': {
        'desc': 'run a command in an environment faking root privileges for file manipulation',
        'common_flags': {
            '-l': 'library, --lib library',
            '--faked': 'binary',
            '-s': 'save-file',
            '-i': 'load-file',
            '-u': 'Use the real ownership of files previously unknown to fakeroot instead of pretending they are owned by root:root.',
            '--unknown-is-real': 'Use the real ownership of files previously unknown to fakeroot instead of pretending they are owned by root:root.',
            '-b': 'fd Specify fd base (TCP mode only). fd is the minimum file descriptor number to use for TCP connections; this may be important to avoid con‐',
            '-h': 'Display help.',
            '-v': 'Display version.'
        },
        'examples': [
            'fakeroot-sysv  # run a command in an environment faking root privil',
            'fakeroot-sysv -h  # Show help',
            'fakeroot-sysv -v  # Show version',
            'fakeroot-sysv -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'fakeroot-tcp': {
        'desc': 'run a command in an environment faking root privileges for file manipulation',
        'common_flags': {
            '-l': 'library, --lib library',
            '--faked': 'binary',
            '-s': 'save-file',
            '-i': 'load-file',
            '-u': 'Use the real ownership of files previously unknown to fakeroot instead of pretending they are owned by root:root.',
            '--unknown-is-real': 'Use the real ownership of files previously unknown to fakeroot instead of pretending they are owned by root:root.',
            '-b': 'fd Specify fd base (TCP mode only). fd is the minimum file descriptor number to use for TCP connections; this may be important to avoid con‐',
            '-h': 'Display help.',
            '-v': 'Display version.'
        },
        'examples': [
            'fakeroot-tcp  # run a command in an environment faking root privil',
            'fakeroot-tcp -h  # Show help',
            'fakeroot-tcp -v  # Show version',
            'fakeroot-tcp -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'fallocate': {
        'desc': 'preallocate or deallocate space to a file',
        'common_flags': {
            '-c': 'Removes a byte range from a file, without leaving a hole. The byte range to be collapsed starts at offset and continues for length bytes. At the',
            '--collapse-range': 'Removes a byte range from a file, without leaving a hole. The byte range to be collapsed starts at offset and continues for length bytes. At the',
            '-d': 'Detect and dig holes. This makes the file sparse in-place, without using extra disk space. The minimum size of the hole depends on filesystem',
            '--dig-holes': 'Detect and dig holes. This makes the file sparse in-place, without using extra disk space. The minimum size of the hole depends on filesystem',
            '-i': 'Insert a hole of length bytes from offset, shifting existing data.',
            '--insert-range': 'Insert a hole of length bytes from offset, shifting existing data.',
            '-l': 'length',
            '--length': 'length',
            '-n': 'Do not modify the apparent length of the file. This may effectively allocate blocks past EOF, which can be removed with a truncate.',
            '--keep-size': 'is implied.',
            '-o': 'offset',
            '--offset': 'offset',
            '-p': 'Deallocates space (i.e., creates a hole) in the byte range starting at offset and continuing for length bytes. Within the specified range,',
            '--punch-hole': 'Deallocates space (i.e., creates a hole) in the byte range starting at offset and continuing for length bytes. Within the specified range,',
            '-v': 'Enable verbose mode.'
        },
        'examples': [
            'fallocate  # preallocate or deallocate space to a file',
            'fallocate -v  # Show version',
            'fallocate -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'false': {
        'desc': 'do nothing, unsuccessfully',
        'common_flags': {
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'false  # do nothing, unsuccessfully',
            'false --help  # Show help',
            'false --version  # Show version'
        ],
        'category': 'Other'
    },
    'fgrep': {
        'desc': 'print lines that match patterns',
        'common_flags': {
            '--help': 'Output a usage message and exit.',
            '-V': 'Output the version number of grep and exit.',
            '--version': 'Output the version number of grep and exit.',
            '-E': 'Interpret PATTERNS as extended regular expressions (EREs, see below).',
            '--extended-regexp': 'Interpret PATTERNS as extended regular expressions (EREs, see below).',
            '-F': 'Interpret PATTERNS as fixed strings, not regular expressions.',
            '--fixed-strings': 'Interpret PATTERNS as fixed strings, not regular expressions.',
            '-G': 'Interpret PATTERNS as basic regular expressions (BREs, see below). This is the default.',
            '--basic-regexp': 'Interpret PATTERNS as basic regular expressions (BREs, see below). This is the default.',
            '-P': 'Interpret PATTERNS as Perl-compatible regular expressions (PCREs). This option is experimental when combined with the -z (--null-data)',
            '--perl-regexp': 'Interpret PATTERNS as Perl-compatible regular expressions (PCREs). This option is experimental when combined with the -z (--null-data)',
            '-e': 'PATTERNS, --regexp=PATTERNS',
            '-f': 'FILE, --file=FILE',
            '-i': 'Ignore case distinctions in patterns and input data, so that characters that differ only in case match each other.',
            '--ignore-case': 'Ignore case distinctions in patterns and input data, so that characters that differ only in case match each other.'
        },
        'examples': [
            'fgrep  # print lines that match patterns',
            'fgrep --help  # Show help',
            'fgrep --version  # Show version'
        ],
        'category': 'Other'
    },
    'file': {
        'desc': 'determine file type',
        'common_flags': {
            '--apple': 'Causes the file command to output the file type and creator code as used by older MacOS versions. The code consists of eight letters, the',
            '-b': 'Do not prepend filenames to output lines (brief mode).',
            '--brief': 'Do not prepend filenames to output lines (brief mode).',
            '-C': 'Write a magic.mgc output file that contains a pre-parsed version of the magic file or directory.',
            '--compile': 'Write a magic.mgc output file that contains a pre-parsed version of the magic file or directory.',
            '-c': 'Cause a checking printout of the parsed form of the magic file. This is usually used in conjunction with the -m option to debug a new magic',
            '--checking-printout': 'Cause a checking printout of the parsed form of the magic file. This is usually used in conjunction with the -m option to debug a new magic',
            '-d': 'Prints internal debugging information to stderr.',
            '-E': 'On filesystem errors (file not found etc), instead of handling the error as regular output as POSIX mandates and keep going, issue an error',
            '-e': 'testname',
            '--exclude': 'testname',
            '--exclude-quiet': 'Like --exclude but ignore tests that file does not know about. This is intended for compatibility with older versions of file.',
            '--extension': 'Print a slash-separated list of valid extensions for the file type found.',
            '-F': 'separator',
            '--separator': 'separator'
        },
        'examples': [
            'file  # determine file type'
        ],
        'category': 'Other'
    },
    'find': {
        'desc': 'search for files in a directory hierarchy',
        'common_flags': {
            '-P': 'Never follow symbolic links. This is the default behaviour. When find examines or prints information about files, and the file is a sym‐',
            '-L': 'Follow symbolic links. When find examines or prints information about files, the information used shall be taken from the properties of the',
            '-H': 'Do not follow symbolic links, except while processing the command line arguments. When find examines or prints information about files, the',
            '-D': 'debugopts',
            '-O': 'level'
        },
        'examples': [
            'find  # search for files in a directory hierarchy'
        ],
        'category': 'Other'
    },
    'flock': {
        'desc': 'manage locks from shell scripts',
        'common_flags': {
            '-c': 'command',
            '--command': 'command',
            '-E': 'number',
            '--conflict-exit-code': 'number',
            '-F': 'Do not fork before executing command. Upon execution the flock process is replaced by command which continues to hold the lock. This option is',
            '--no-fork': 'Do not fork before executing command. Upon execution the flock process is replaced by command which continues to hold the lock. This option is',
            '-e': 'Obtain an exclusive lock, sometimes called a write lock. This is the default.',
            '-x': 'Obtain an exclusive lock, sometimes called a write lock. This is the default.',
            '--exclusive': 'Obtain an exclusive lock, sometimes called a write lock. This is the default.',
            '-n': 'Fail rather than wait if the lock cannot be immediately acquired. See the -E option for the exit status used.',
            '--nb': 'Fail rather than wait if the lock cannot be immediately acquired. See the -E option for the exit status used.',
            '--nonblock': 'Fail rather than wait if the lock cannot be immediately acquired. See the -E option for the exit status used.',
            '-o': 'Close the file descriptor on which the lock is held before executing command. This is useful if command spawns a child process which should not',
            '--close': 'Close the file descriptor on which the lock is held before executing command. This is useful if command spawns a child process which should not',
            '-s': 'Obtain a shared lock, sometimes called a read lock.'
        },
        'examples': [
            'flock  # manage locks from shell scripts'
        ],
        'category': 'Other'
    },
    'free': {
        'desc': 'Display amount of free and used memory in the system',
        'common_flags': {
            '-b': 'Display the amount of memory in bytes.',
            '--bytes': 'Display the amount of memory in bytes.',
            '-k': 'Display the amount of memory in kibibytes. This is the default.',
            '--kibi': 'Display the amount of memory in kibibytes. This is the default.',
            '-m': 'Display the amount of memory in mebibytes.',
            '--mebi': 'Display the amount of memory in mebibytes.',
            '-g': 'Display the amount of memory in gibibytes.',
            '--gibi': 'Display the amount of memory in gibibytes.',
            '--tebi': 'Display the amount of memory in tebibytes.',
            '--pebi': 'Display the amount of memory in pebibytes.',
            '--kilo': 'Display the amount of memory in kilobytes. Implies --si.',
            '--mega': 'Display the amount of memory in megabytes. Implies --si.',
            '--giga': 'Display the amount of memory in gigabytes. Implies --si.',
            '--tera': 'Display the amount of memory in terabytes. Implies --si.',
            '--peta': 'Display the amount of memory in petabytes. Implies --si.'
        },
        'examples': [
            'free  # Display amount of free and used memory in the syst'
        ],
        'category': 'Other'
    },
    'ftp': {
        'desc': 'Internet file transfer program',
        'common_flags': {
            '-o': 'output is recommended, to avoid writing to unexpected file names.'
        },
        'examples': [
            'ftp  # Internet file transfer program'
        ],
        'category': 'Other'
    },
    'geqn': {
        'desc': 'format mathematics (equations) for groff or MathML',
        'common_flags': {
            '--help': 'displays a usage message, while -v and --version show version information; all exit afterward.',
            '-C': 'Recognize .EQ and .EN even when followed by a character other than space or newline.',
            '-d': 'xy Specify delimiters x for left and y for right ends of equations not bracketed by .EQ/.EN. x and y need not be distinct. Any “delim xy”',
            '-f': 'F is equivalent to “gfont F”.',
            '-m': 'n is equivalent to “set minimum_size n”.',
            '-M': 'dir Search dir for eqnrc before those listed in section “Description” above.',
            '-N': 'Prohibit newlines within delimiters. This option allows eqn to recover better from missing closing delimiters.',
            '-p': 'n Set sub- and superscripts n points smaller than the surrounding text. This option is deprecated. eqn normally sets sub- and superscripts at',
            '-r': 'Reduce the type size of subscripts at most once relative to the base type size for the equation.',
            '-R': 'Don\'t load eqnrc.',
            '-s': 'n is equivalent to “gsize n”. This option is deprecated.',
            '-T': 'dev Prepare output for the device dev. In most cases, the effect of this is to define a macro dev with a value of 1; eqnrc uses this to provide'
        },
        'examples': [
            'geqn  # format mathematics (equations) for groff or MathML',
            'geqn --help  # Show help',
            'geqn -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'getent': {
        'desc': 'get entries from Name Service Switch libraries',
        'common_flags': {
            '--service': 'database:service',
            '-s': 'database:service',
            '--no-idn': '-i Disables IDN encoding in lookups for ahosts/getaddrinfo(3) (Since glibc-2.13.)',
            '--help': '-? Print a usage summary and exit.',
            '--usage': 'Print a short usage summary and exit.',
            '--version': '-V Print the version number, license, and disclaimer of warranty for getent.'
        },
        'examples': [
            'getent  # get entries from Name Service Switch libraries',
            'getent --help  # Show help',
            'getent --version  # Show version'
        ],
        'category': 'Other'
    },
    'getopt': {
        'desc': 'parse command options (enhanced)',
        'common_flags': {
            '-a': 'Allow long options to start with a single \'-\'.',
            '--alternative': 'Allow long options to start with a single \'-\'.',
            '-l': 'longopts',
            '--longoptions': 'longopts',
            '-n': 'progname',
            '--name': 'progname',
            '-o': 'shortopts',
            '--options': 'shortopts',
            '-q': 'Disable error reporting by getopt(3).',
            '--quiet': 'Disable error reporting by getopt(3).',
            '-Q': 'Do not generate normal output. Errors are still reported by getopt(3), unless you also use -q.',
            '--quiet-output': 'Do not generate normal output. Errors are still reported by getopt(3), unless you also use -q.',
            '-s': 'shell',
            '--shell': 'shell',
            '-T': 'Test if your getopt(1) is this enhanced version or an old version. This generates no output, and sets the error status to 4. Other'
        },
        'examples': [
            'getopt  # parse command options (enhanced)',
            'getopt -a  # Show all'
        ],
        'category': 'Other'
    },
    'gids-tool': {
        'desc': 'smart card utility for GIDS cards',
        'common_flags': {
            '-X': 'Initialize token.',
            '--initialize': 'Initialize token.',
            '--admin-key': 'argument',
            '--pin': 'pin',
            '--serial-number': 'argument',
            '-U': 'Unblock the user PIN after an administrator authentication.',
            '--unblock': 'Unblock the user PIN after an administrator authentication.',
            '-C': 'Change the administrator key.',
            '--change-admin-key': 'Change the administrator key.',
            '--new-admin-key': 'argument',
            '--reader': 'argument, -r argument',
            '-w': 'Wait for a card to be inserted.',
            '--wait': 'Wait for a card to be inserted.',
            '-v': 'Verbose operation. Use several times to enable debug output.',
            '--verbose': 'Verbose operation. Use several times to enable debug output.'
        },
        'examples': [
            'gids-tool  # smart card utility for GIDS cards',
            'gids-tool -v  # Show version',
            'gids-tool -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git': {
        'desc': 'the stupid content tracker',
        'common_flags': {
            '-v': 'Prints the Git suite version that the git program came from.',
            '--version': 'Prints the Git suite version that the git program came from.',
            '-h': 'Prints the synopsis and a list of the most commonly used commands. If the option --all or -a is given then all available commands are printed.',
            '--help': 'Prints the synopsis and a list of the most commonly used commands. If the option --all or -a is given then all available commands are printed.',
            '-C': '<path> is interpreted relative to the preceding -C <path>. If <path> is present but empty, e.g. -C \"\", then the current working directory is',
            '-c': '<name>=<value>',
            '--config-env': '=<name>=<envvar>',
            '--exec-path': '[=<path>]',
            '--html-path': 'Print the path, without trailing slash, where Git’s HTML documentation is installed and exit.',
            '--man-path': 'Print the manpath (see man(1)) for the man pages for this version of Git and exit.',
            '--info-path': 'Print the path where the Info files documenting this version of Git are installed and exit.',
            '-p': 'Pipe all output into less (or if set, $PAGER) if standard output is a terminal. This overrides the pager.<cmd> configuration options (see the',
            '--paginate': 'Pipe all output into less (or if set, $PAGER) if standard output is a terminal. This overrides the pager.<cmd> configuration options (see the',
            '-P': 'Do not pipe Git output into a pager.',
            '--no-pager': 'Do not pipe Git output into a pager.'
        },
        'examples': [
            'git  # the stupid content tracker',
            'git clone https://repo.git  # Clone repository',
            'git add file  # Stage file',
            'git commit -m \'message\'  # Commit changes',
            'git push origin main  # Push to remote'
        ],
        'category': 'Other'
    },
    'git-add': {
        'desc': 'Add file contents to the index',
        'common_flags': {
            '-n': 'Don’t actually add the file(s), just show if they exist and/or will be ignored.',
            '--dry-run': 'Don’t actually add the file(s), just show if they exist and/or will be ignored.',
            '-v': 'Be verbose.',
            '--verbose': 'Be verbose.',
            '-f': 'Allow adding otherwise ignored files.',
            '--force': 'Allow adding otherwise ignored files.',
            '--sparse': 'Allow updating index entries outside of the sparse-checkout cone. Normally, git add refuses to update index entries whose paths do not fit',
            '-i': 'Add modified contents in the working tree interactively to the index. Optional path arguments may be supplied to limit operation to a subset of',
            '--interactive': 'Add modified contents in the working tree interactively to the index. Optional path arguments may be supplied to limit operation to a subset of',
            '-p': 'Interactively choose hunks of patch between the index and the work tree and add them to the index. This gives the user a chance to review the',
            '--patch': 'Interactively choose hunks of patch between the index and the work tree and add them to the index. This gives the user a chance to review the',
            '-e': 'Open the diff vs. the index in an editor and let the user edit it. After the editor was closed, adjust the hunk headers and apply the patch to',
            '--edit': 'Open the diff vs. the index in an editor and let the user edit it. After the editor was closed, adjust the hunk headers and apply the patch to',
            '-u': 'Update the index just where it already has an entry matching <pathspec>. This removes as well as modifies index entries to match the working',
            '--update': 'Update the index just where it already has an entry matching <pathspec>. This removes as well as modifies index entries to match the working'
        },
        'examples': [
            'git-add  # Add file contents to the index',
            'git-add -v  # Show version',
            'git-add -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-am': {
        'desc': 'Apply a series of patches from a mailbox',
        'common_flags': {
            '-s': 'Add a Signed-off-by trailer to the commit message, using the committer identity of yourself. See the signoff option in git-commit(1) for more',
            '--signoff': 'Add a Signed-off-by trailer to the commit message, using the committer identity of yourself. See the signoff option in git-commit(1) for more',
            '-k': 'Pass -k flag to git mailinfo (see git-mailinfo(1)).',
            '--keep': 'Pass -k flag to git mailinfo (see git-mailinfo(1)).',
            '--keep-non-patch': 'Pass -b flag to git mailinfo (see git-mailinfo(1)).',
            '-c': 'Remove everything in body before a scissors line (see git-mailinfo(1)). Can be activated by default using the mailinfo.scissors configuration',
            '--scissors': 'Remove everything in body before a scissors line (see git-mailinfo(1)). Can be activated by default using the mailinfo.scissors configuration',
            '--no-scissors': 'Ignore scissors lines (see git-mailinfo(1)).',
            '--quoted-cr': '=<action>',
            '--empty': '=(drop|keep|stop)',
            '-m': 'Pass the -m flag to git mailinfo (see git-mailinfo(1)), so that the Message-ID header is added to the commit message. The am.messageid',
            '--message-id': 'Pass the -m flag to git mailinfo (see git-mailinfo(1)), so that the Message-ID header is added to the commit message. The am.messageid',
            '--no-message-id': 'Do not add the Message-ID header to the commit message. no-message-id is useful to override am.messageid.',
            '-q': 'Be quiet. Only print error messages.',
            '--quiet': 'Be quiet. Only print error messages.'
        },
        'examples': [
            'git-am  # Apply a series of patches from a mailbox'
        ],
        'category': 'Other'
    },
    'git-annotate': {
        'desc': 'Annotate file lines with commit information',
        'common_flags': {
            '-b': 'Show blank SHA-1 for boundary commits. This can also be controlled via the blame.blankBoundary config option.',
            '--root': 'Do not treat root commits as boundaries. This can also be controlled via the blame.showRoot config option.',
            '--show-stats': 'Include additional statistics at the end of blame output.',
            '-L': '<start>,<end>, -L :<funcname>',
            '-l': 'Show long rev (Default: off).',
            '-t': 'Show raw timestamp (Default: off).',
            '-S': '<revs-file>',
            '--reverse': '<rev>..<rev>',
            '--first-parent': 'Follow only the first parent commit upon seeing a merge commit. This option can be used to determine when a line was introduced to a particular',
            '-p': 'Show in a format designed for machine consumption.',
            '--porcelain': 'Show in a format designed for machine consumption.',
            '--line-porcelain': 'Show the porcelain format, but output commit information for each line, not just the first time a commit is referenced. Implies --porcelain.',
            '--incremental': 'Show the result incrementally in a format designed for machine consumption.',
            '--encoding': '=<encoding>',
            '--contents': '<file>'
        },
        'examples': [
            'git-annotate  # Annotate file lines with commit information'
        ],
        'category': 'Other'
    },
    'git-apply': {
        'desc': 'Apply a patch to files and/or to the index',
        'common_flags': {
            '--stat': 'Instead of applying the patch, output diffstat for the input. Turns off \"apply\".',
            '--numstat': 'Similar to --stat, but shows the number of added and deleted lines in decimal notation and the pathname without abbreviation, to make it more',
            '--summary': 'Instead of applying the patch, output a condensed summary of information obtained from git diff extended headers, such as creations, renames,',
            '--check': 'Instead of applying the patch, see if the patch is applicable to the current working tree and/or the index file and detects errors. Turns off',
            '--index': 'expects index entries and working tree copies for relevant paths to be identical (their contents and metadata such as file mode must',
            '--cached': 'option is used, and is incompatible with the --reject option. When used with the --cached option, any conflicts are left at higher',
            '--intent-to-add': 'When applying the patch only to the working tree, mark new files to be added to the index later (see --intent-to-add option in git-add(1)). This',
            '-3': 'Attempt 3-way merge if the patch records the identity of blobs it is supposed to apply to and we have those blobs available locally, possibly',
            '--3way': 'Attempt 3-way merge if the patch records the identity of blobs it is supposed to apply to and we have those blobs available locally, possibly',
            '--ours': 'Instead of leaving conflicts in the file, resolve conflicts favouring our (or their or both) side of the lines. Requires --3way.',
            '--theirs': 'Instead of leaving conflicts in the file, resolve conflicts favouring our (or their or both) side of the lines. Requires --3way.',
            '--union': 'Instead of leaving conflicts in the file, resolve conflicts favouring our (or their or both) side of the lines. Requires --3way.',
            '--build-fake-ancestor': '=<file>',
            '-R': 'Apply the patch in reverse.',
            '--reverse': 'Apply the patch in reverse.'
        },
        'examples': [
            'git-apply  # Apply a patch to files and/or to the index'
        ],
        'category': 'Other'
    },
    'git-archive': {
        'desc': 'Create an archive of files from a named tree',
        'common_flags': {
            '--format': '=<fmt>',
            '-l': 'Show all available formats.',
            '--list': 'Show all available formats.',
            '-v': 'Report progress to stderr.',
            '--verbose': 'Report progress to stderr.',
            '--prefix': '=<prefix>/',
            '-o': '<file>, --output=<file>',
            '--add-file': '=<file>',
            '--add-virtual-file': '=<path>:<content>',
            '--worktree-attributes': 'Look for attributes in .gitattributes files in the working tree as well (see the section called “ATTRIBUTES”).',
            '--mtime': '=<time>',
            '--remote': '=<repo>',
            '--exec': '=<git-upload-archive>'
        },
        'examples': [
            'git-archive  # Create an archive of files from a named tree',
            'git-archive -v  # Show version',
            'git-archive -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-bisect': {
        'desc': 'Use binary search to find the commit that introduced a bug',
        'common_flags': {
            '--no-checkout': 'Do not checkout the new working tree at each iteration of the bisection process. Instead just update the reference named BISECT_HEAD to make it',
            '--first-parent': 'Follow only the first parent commit upon seeing a merge commit.'
        },
        'examples': [
            'git-bisect  # Use binary search to find the commit that introduc'
        ],
        'category': 'Other'
    },
    'git-blame': {
        'desc': 'Show what revision and author last modified each line of a file',
        'common_flags': {
            '-b': 'Show blank SHA-1 for boundary commits. This can also be controlled via the blame.blankBoundary config option.',
            '--root': 'Do not treat root commits as boundaries. This can also be controlled via the blame.showRoot config option.',
            '--show-stats': 'Include additional statistics at the end of blame output.',
            '-L': '<start>,<end>, -L :<funcname>',
            '-l': 'Show long rev (Default: off).',
            '-t': 'Show raw timestamp (Default: off).',
            '-S': '<revs-file>',
            '--reverse': '<rev>..<rev>',
            '--first-parent': 'Follow only the first parent commit upon seeing a merge commit. This option can be used to determine when a line was introduced to a particular',
            '-p': 'Show in a format designed for machine consumption.',
            '--porcelain': 'Show in a format designed for machine consumption.',
            '--line-porcelain': 'Show the porcelain format, but output commit information for each line, not just the first time a commit is referenced. Implies --porcelain.',
            '--incremental': 'Show the result incrementally in a format designed for machine consumption.',
            '--encoding': '=<encoding>',
            '--contents': '<file>'
        },
        'examples': [
            'git-blame  # Show what revision and author last modified each l'
        ],
        'category': 'Other'
    },
    'git-branch': {
        'desc': 'List, create, or delete branches',
        'common_flags': {
            '-d': 'Delete a branch. The branch must be fully merged in its upstream branch, or in HEAD if no upstream was set with --track or --set-upstream-to.',
            '--delete': 'Delete a branch. The branch must be fully merged in its upstream branch, or in HEAD if no upstream was set with --track or --set-upstream-to.',
            '-D': 'Shortcut for --delete --force.',
            '--create-reflog': 'Create the branch’s reflog. This activates recording of all changes made to the branch ref, enabling use of date based sha1 expressions such as',
            '-f': 'Reset <branchname> to <start-point>, even if <branchname> exists already. Without -f, git branch refuses to change an existing branch. In',
            '--force': 'Reset <branchname> to <start-point>, even if <branchname> exists already. Without -f, git branch refuses to change an existing branch. In',
            '-m': 'Move/rename a branch, together with its config and reflog.',
            '--move': 'Move/rename a branch, together with its config and reflog.',
            '-M': 'Shortcut for --move --force.',
            '-c': 'Copy a branch, together with its config and reflog.',
            '--copy': 'Copy a branch, together with its config and reflog.',
            '-C': 'Shortcut for --copy --force.',
            '--color': '[=<when>]',
            '--no-color': 'Turn off branch colors, even when the configuration file gives the default to color output. Same as --color=never.',
            '-i': 'Sorting and filtering branches are case insensitive.'
        },
        'examples': [
            'git-branch  # List, create, or delete branches'
        ],
        'category': 'Other'
    },
    'git-bundle': {
        'desc': 'Move objects and refs by archive',
        'common_flags': {
            '--progress': 'Progress status is reported on the standard error stream by default when it is attached to a terminal, unless -q is specified. This flag forces',
            '--version': '=<version>',
            '-q': 'This flag makes the command not to report its progress on the standard error stream.',
            '--quiet': 'This flag makes the command not to report its progress on the standard error stream.'
        },
        'examples': [
            'git-bundle  # Move objects and refs by archive',
            'git-bundle --version  # Show version'
        ],
        'category': 'Other'
    },
    'git-cat-file': {
        'desc': 'Provide contents or details of repository objects',
        'common_flags': {
            '-t': 'Instead of the content, show the object type identified by <object>.',
            '-s': 'Instead of the content, show the object size identified by <object>. If used with --use-mailmap option, will show the size of updated object',
            '-e': 'Exit with zero status if <object> exists and is a valid object. If <object> is of an invalid format, exit with non-zero status and emit an error',
            '-p': 'Pretty-print the contents of <object> based on its type.',
            '--textconv': ', or --use-mailmap.',
            '--filters': ', or --use-mailmap.',
            '--path': '=<path>',
            '--batch': '=<format>',
            '--batch-check': '=<format>',
            '--batch-command': 'recognizes the following commands:',
            '--batch-all-objects': 'Instead of reading a list of objects on stdin, perform the requested batch operation on all objects in the repository and any alternate object',
            '--buffer': 'Normally batch output is flushed after each object is output, so that a process can interactively read and write from cat-file. With this',
            '--unordered': 'When --batch-all-objects is in use, visit objects in an order which may be more efficient for accessing the object contents than hash order. The',
            '--allow-unknown-type': 'Allow -s or -t to query broken/corrupt objects of unknown type.',
            '--follow-symlinks': 'With --batch or --batch-check, follow symlinks inside the repository when requesting objects with extended SHA-1 expressions of the form'
        },
        'examples': [
            'git-cat-file  # Provide contents or details of repository objects'
        ],
        'category': 'Other'
    },
    'git-check-attr': {
        'desc': 'Display gitattributes information',
        'common_flags': {
            '-a': 'List all attributes that are associated with the specified paths. If this option is used, then unspecified attributes will not be included in',
            '--all': 'List all attributes that are associated with the specified paths. If this option is used, then unspecified attributes will not be included in',
            '--cached': 'Consider .gitattributes in the index only, ignoring the working tree.',
            '--stdin': 'Read pathnames from the standard input, one per line, instead of from the command line.',
            '-z': 'The output format is modified to be machine-parsable. If --stdin is also given, input paths are separated with a NUL character instead of a',
            '--source': '=<tree-ish>'
        },
        'examples': [
            'git-check-attr  # Display gitattributes information',
            'git-check-attr -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-check-ignore': {
        'desc': 'Debug gitignore / exclude files',
        'common_flags': {
            '-q': 'Don’t output anything, just set exit status. This is only valid with a single pathname.',
            '--quiet': 'Don’t output anything, just set exit status. This is only valid with a single pathname.',
            '-v': 'Instead of printing the paths that are excluded, for each path that matches an exclude pattern, print the exclude pattern together with the',
            '--verbose': 'Instead of printing the paths that are excluded, for each path that matches an exclude pattern, print the exclude pattern together with the',
            '--stdin': 'Read pathnames from the standard input, one per line, instead of from the command-line.',
            '-z': 'The output format is modified to be machine-parsable (see below). If --stdin is also given, input paths are separated with a NUL character',
            '-n': 'Show given paths which don’t match any pattern. This only makes sense when --verbose is enabled, otherwise it would not be possible to',
            '--non-matching': 'Show given paths which don’t match any pattern. This only makes sense when --verbose is enabled, otherwise it would not be possible to',
            '--no-index': 'Don’t look in the index when undertaking the checks. This can be used to debug why a path became tracked by e.g. git add . and was not ignored'
        },
        'examples': [
            'git-check-ignore  # Debug gitignore / exclude files',
            'git-check-ignore -v  # Show version',
            'git-check-ignore -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-check-mailmap': {
        'desc': 'Show canonical names and email addresses of contacts',
        'common_flags': {
            '--stdin': 'Read contacts, one per line, from the standard input after exhausting contacts provided on the command-line.',
            '--mailmap-file': '=<file>',
            '--mailmap-blob': '=<blob>'
        },
        'examples': [
            'git-check-mailmap  # Show canonical names and email addresses of contac'
        ],
        'category': 'Other'
    },
    'git-check-ref-format': {
        'desc': 'Ensures that a reference name is well formed',
        'common_flags': {
            '--no-allow-onelevel': '.',
            '--refspec-pattern': 'Interpret <refname> as a reference name pattern for a refspec (as used with remote repositories). If this option is enabled, <refname> is',
            '--normalize': 'Normalize refname by removing any leading slash (/) characters and collapsing runs of adjacent slashes between name components into a single'
        },
        'examples': [
            'git-check-ref-format  # Ensures that a reference name is well formed'
        ],
        'category': 'Other'
    },
    'git-checkout': {
        'desc': 'Switch branches or restore working tree files',
        'common_flags': {
            '-q': 'Quiet, suppress feedback messages.',
            '--quiet': 'Quiet, suppress feedback messages.',
            '--progress': 'Progress status is reported on the standard error stream by default when it is attached to a terminal, unless --quiet is specified. This flag',
            '--no-progress': 'Progress status is reported on the standard error stream by default when it is attached to a terminal, unless --quiet is specified. This flag',
            '-f': 'When switching branches, proceed even if the index or the working tree differs from HEAD, and even if there are untracked files in the way. This',
            '--force': 'When switching branches, proceed even if the index or the working tree differs from HEAD, and even if there are untracked files in the way. This',
            '--ours': 'When checking out paths from the index, check out stage #2 (ours) or #3 (theirs) for unmerged paths.',
            '--theirs': 'When checking out paths from the index, check out stage #2 (ours) or #3 (theirs) for unmerged paths.',
            '-b': '<new-branch>',
            '-B': '<new-branch>',
            '-t': '[=(direct|inherit)]',
            '--track': '[=(direct|inherit)]',
            '--no-track': 'Do not set up \"upstream\" configuration, even if the branch.autoSetupMerge configuration variable is true.',
            '--guess': 'If <branch> is not found but there does exist a tracking branch in exactly one remote (call it <remote>) with a matching name, treat as',
            '--no-guess': 'If <branch> is not found but there does exist a tracking branch in exactly one remote (call it <remote>) with a matching name, treat as'
        },
        'examples': [
            'git-checkout  # Switch branches or restore working tree files'
        ],
        'category': 'Other'
    },
    'git-checkout-index': {
        'desc': 'Copy files from the index to the working tree',
        'common_flags': {
            '-u': 'update stat information for the checked out entries in the index file.',
            '--index': 'update stat information for the checked out entries in the index file.',
            '-q': 'be quiet if files exist or are not in the index',
            '--quiet': 'be quiet if files exist or are not in the index',
            '-f': 'forces overwrite of existing files',
            '--force': 'forces overwrite of existing files',
            '-a': 'checks out all files in the index except for those with the skip-worktree bit set (see --ignore-skip-worktree-bits). Cannot be used together',
            '--all': 'checks out all files in the index except for those with the skip-worktree bit set (see --ignore-skip-worktree-bits). Cannot be used together',
            '-n': 'Don’t checkout new files, only refresh files already checked out.',
            '--no-create': 'Don’t checkout new files, only refresh files already checked out.',
            '--prefix': '=<string>',
            '--stage': '=<number>|all',
            '--temp': 'Instead of copying the files to the working directory, write the content to temporary files. The temporary name associations will be written to',
            '--ignore-skip-worktree-bits': 'Check out all files, including those with the skip-worktree bit set.',
            '--stdin': 'Instead of taking a list of paths from the command line, read the list of paths from the standard input. Paths are separated by LF (i.e. one'
        },
        'examples': [
            'git-checkout-index  # Copy files from the index to the working tree',
            'git-checkout-index -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-cherry': {
        'desc': 'Find commits yet to be applied to upstream',
        'common_flags': {
            '-v': 'Show the commit subjects next to the SHA1s.'
        },
        'examples': [
            'git-cherry  # Find commits yet to be applied to upstream',
            'git-cherry -v  # Show version',
            'git-cherry -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-cherry-pick': {
        'desc': 'Apply the changes introduced by some existing commits',
        'common_flags': {
            '-e': 'With this option, git cherry-pick will let you edit the commit message prior to committing.',
            '--edit': 'With this option, git cherry-pick will let you edit the commit message prior to committing.',
            '--cleanup': '=<mode>',
            '-x': 'When recording the commit, append a line that says \"(cherry picked from commit ...)\" to the original commit message in order to indicate which',
            '-r': 'It used to be that the command defaulted to do -x described above, and -r was to disable it. Now the default is not to do -x so this option is a',
            '-m': '<parent-number>, --mainline <parent-number>',
            '-n': 'Usually the command automatically creates a sequence of commits. This flag applies the changes necessary to cherry-pick each named commit to',
            '--no-commit': 'Usually the command automatically creates a sequence of commits. This flag applies the changes necessary to cherry-pick each named commit to',
            '-s': 'Add a Signed-off-by trailer at the end of the commit message. See the signoff option in git-commit(1) for more information.',
            '--signoff': 'Add a Signed-off-by trailer at the end of the commit message. See the signoff option in git-commit(1) for more information.',
            '-S': '[<keyid>], --gpg-sign[=<keyid>], --no-gpg-sign',
            '--ff': 'If the current HEAD is the same as the parent of the cherry-pick’ed commit, then a fast forward to this commit will be performed.',
            '--allow-empty': 'By default, cherry-picking an empty commit will fail, indicating that an explicit invocation of git commit --allow-empty is required. This',
            '--allow-empty-message': 'By default, cherry-picking a commit with an empty message will fail. This option overrides that behavior, allowing commits with empty messages',
            '--empty': '=(drop|keep|stop)'
        },
        'examples': [
            'git-cherry-pick  # Apply the changes introduced by some existing comm'
        ],
        'category': 'Other'
    },
    'git-clean': {
        'desc': 'Remove untracked files from the working tree',
        'common_flags': {
            '-d': 'Normally, when no <pathspec> is specified, git clean will not recurse into untracked directories to avoid removing too much. Specify -d to have',
            '-f': 'If the Git configuration variable clean.requireForce is not set to false, git clean will refuse to delete files or directories unless given -f.',
            '--force': 'If the Git configuration variable clean.requireForce is not set to false, git clean will refuse to delete files or directories unless given -f.',
            '-i': 'Show what would be done and clean files interactively. See “Interactive mode” for details. Configuration variable clean.requireForce is ignored,',
            '--interactive': 'Show what would be done and clean files interactively. See “Interactive mode” for details. Configuration variable clean.requireForce is ignored,',
            '-n': 'Don’t actually remove anything, just show what would be done. Configuration variable clean.requireForce is ignored, as nothing will be deleted',
            '--dry-run': 'Don’t actually remove anything, just show what would be done. Configuration variable clean.requireForce is ignored, as nothing will be deleted',
            '-q': 'Be quiet, only report errors, but not the files that are successfully removed.',
            '--quiet': 'Be quiet, only report errors, but not the files that are successfully removed.',
            '-e': '<pattern>, --exclude=<pattern>',
            '-x': 'Don’t use the standard ignore rules (see gitignore(5)), but still use the ignore rules given with -e options from the command line. This allows',
            '-X': 'Remove only files ignored by Git. This may be useful to rebuild everything from scratch, but keep manually created files.'
        },
        'examples': [
            'git-clean  # Remove untracked files from the working tree'
        ],
        'category': 'Other'
    },
    'git-clone': {
        'desc': 'Clone a repository into a new directory',
        'common_flags': {
            '-l': 'When the repository to clone from is on a local machine, this flag bypasses the normal \"Git aware\" transport mechanism and clones the repository',
            '--local': 'When the repository to clone from is on a local machine, this flag bypasses the normal \"Git aware\" transport mechanism and clones the repository',
            '--no-hardlinks': 'Force the cloning process from a repository on a local filesystem to copy the files under the .git/objects directory instead of using hardlinks.',
            '-s': 'When the repository to clone is on the local machine, instead of using hard links, automatically setup .git/objects/info/alternates to share the',
            '--shared': 'When the repository to clone is on the local machine, instead of using hard links, automatically setup .git/objects/info/alternates to share the',
            '--reference': '[-if-able] <repository>',
            '--dissociate': 'Borrow the objects from reference repositories specified with the --reference options only to reduce network transfer, and stop borrowing from',
            '-q': 'Operate quietly. Progress is not reported to the standard error stream.',
            '--quiet': 'Operate quietly. Progress is not reported to the standard error stream.',
            '-v': 'Run verbosely. Does not affect the reporting of progress status to the standard error stream.',
            '--verbose': 'Run verbosely. Does not affect the reporting of progress status to the standard error stream.',
            '--progress': 'Progress status is reported on the standard error stream by default when it is attached to a terminal, unless --quiet is specified. This flag',
            '--server-option': '=<option>',
            '-n': 'No checkout of HEAD is performed after the clone is complete.',
            '--no-checkout': 'No checkout of HEAD is performed after the clone is complete.'
        },
        'examples': [
            'git-clone  # Clone a repository into a new directory',
            'git-clone -v  # Show version',
            'git-clone -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-column': {
        'desc': 'Display data in columns',
        'common_flags': {
            '--command': '=<name>',
            '--mode': '=<mode>',
            '--raw-mode': '=<n>',
            '--width': '=<width>',
            '--indent': '=<string>',
            '--nl': '=<string>',
            '--padding': '=<N>'
        },
        'examples': [
            'git-column  # Display data in columns'
        ],
        'category': 'Other'
    },
    'git-commit': {
        'desc': 'Record changes to the repository',
        'common_flags': {
            '-a': 'Tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected.',
            '--all': 'Tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected.',
            '-p': 'Use the interactive patch selection interface to choose which changes to commit. See git-add(1) for details.',
            '--patch': 'Use the interactive patch selection interface to choose which changes to commit. See git-add(1) for details.',
            '-C': '<commit>, --reuse-message=<commit>',
            '-c': '<commit>, --reedit-message=<commit>',
            '--fixup': '=reword:<commit> is shorthand for --fixup=amend:<commit> --only. It creates an \"amend!\" commit with only a log message (ignoring any',
            '--squash': '=<commit>',
            '--reset-author': 'When used with -C/-c/--amend options, or when committing after a conflicting cherry-pick, declare that the authorship of the resulting commit',
            '--short': 'When doing a dry-run, give the output in the short-format. See git-status(1) for details. Implies --dry-run.',
            '--branch': 'Show the branch and tracking info even in short-format.',
            '--porcelain': 'When doing a dry-run, give the output in a porcelain-ready format. See git-status(1) for details. Implies --dry-run.',
            '--long': 'When doing a dry-run, give the output in the long-format. Implies --dry-run.',
            '-z': 'When showing short or porcelain status output, print the filename verbatim and terminate the entries with NUL, instead of LF. If no format is',
            '--null': 'When showing short or porcelain status output, print the filename verbatim and terminate the entries with NUL, instead of LF. If no format is'
        },
        'examples': [
            'git-commit  # Record changes to the repository',
            'git-commit -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-commit-graph': {
        'desc': 'Write and verify Git commit-graph files',
        'common_flags': {
            '--object-dir': 'Use given directory for the location of packfiles and commit-graph file. This parameter exists to specify the location of an alternate that only'
        },
        'examples': [
            'git-commit-graph  # Write and verify Git commit-graph files'
        ],
        'category': 'Other'
    },
    'git-commit-tree': {
        'desc': 'Create a new commit object',
        'common_flags': {
            '-p': '<parent>',
            '-m': '<message>',
            '-F': '<file>',
            '-S': '[<keyid>], --gpg-sign[=<keyid>], --no-gpg-sign'
        },
        'examples': [
            'git-commit-tree  # Create a new commit object'
        ],
        'category': 'Other'
    },
    'git-count-objects': {
        'desc': 'Count unpacked number of objects and their disk consumption',
        'common_flags': {
            '-v': 'Provide more detailed reports:',
            '--verbose': 'Provide more detailed reports:',
            '-H': 'Print sizes in human readable format',
            '--human-readable': 'Print sizes in human readable format'
        },
        'examples': [
            'git-count-objects  # Count unpacked number of objects and their disk co',
            'git-count-objects -v  # Show version',
            'git-count-objects -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-credential-cache': {
        'desc': 'Helper to temporarily store passwords in memory',
        'common_flags': {
            '--timeout': '<seconds>',
            '--socket': '<path>'
        },
        'examples': [
            'git-credential-cache  # Helper to temporarily store passwords in memory'
        ],
        'category': 'Other'
    },
    'git-credential-store': {
        'desc': 'Helper to store credentials on disk',
        'common_flags': {
            '--file': '=<path>'
        },
        'examples': [
            'git-credential-store  # Helper to store credentials on disk'
        ],
        'category': 'Other'
    },
    'git-daemon': {
        'desc': 'A really simple server for Git repositories',
        'common_flags': {
            '--strict-paths': 'Match paths exactly (i.e. don’t allow \"/foo/repo\" when the real path is \"/foo/repo.git\" or \"/foo/repo/.git\") and don’t do user-relative paths.',
            '--base-path': '=<path>',
            '--base-path-relaxed': 'If --base-path is enabled and repo lookup fails, with this option git daemon will attempt to lookup without prefixing the base path. This is',
            '--interpolated-path': '=<pathtemplate>',
            '--export-all': 'Allow pulling from all directories that look like Git repositories (have the objects and refs subdirectories), even if they do not have the',
            '--inetd': 'Have the server run as an inetd service. Implies --syslog (may be overridden with --log-destination=). Incompatible with --detach, --port,',
            '--listen': '=<host-or-ipaddr>',
            '--user': 'and --group options.',
            '--port': '=<n>',
            '--init-timeout': '=<n>',
            '--timeout': '=<n>',
            '--max-connections': '=<n>',
            '--syslog': 'Short for --log-destination=syslog.',
            '--log-destination': '=<destination>',
            '--user-path': '=<path>'
        },
        'examples': [
            'git-daemon  # A really simple server for Git repositories'
        ],
        'category': 'Other'
    },
    'git-describe': {
        'desc': 'Give an object a human readable name based on an available ref',
        'common_flags': {
            '--dirty': '[=<mark>], --broken[=<mark>]',
            '--all': 'Instead of using only the annotated tags, use any ref found in refs/ namespace. This option enables matching any known branch, remote-tracking',
            '--tags': '.',
            '--contains': 'Instead of finding the tag that predates the commit, find the tag that comes after the commit, and thus contains it. Automatically implies',
            '--abbrev': '=<n>',
            '--candidates': '=<n>',
            '--exact-match': 'Only output exact matches (a tag directly references the supplied commit). This is a synonym for --candidates=0.',
            '--debug': 'Verbosely display information about the searching strategy being employed to standard error. The tag name will still be printed to standard out.',
            '--long': 'Always output the long format (the tag, the number of commits and the abbreviated commit name) even when it matches a tag. This is useful when',
            '--match': '<pattern>',
            '--exclude': 'patterns. Use --no-exclude to clear and reset the list of patterns.',
            '--always': 'Show uniquely abbreviated commit object as fallback.',
            '--first-parent': 'Follow only the first parent commit upon seeing a merge commit. This is useful when you wish to not match tags on branches merged in the history'
        },
        'examples': [
            'git-describe  # Give an object a human readable name based on an a',
            'git-describe --all  # Show all'
        ],
        'category': 'Other'
    },
    'git-diff': {
        'desc': 'Show changes between commits, commit and working tree, etc',
        'common_flags': {
            '-p': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”). This is the default.',
            '-u': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”). This is the default.',
            '--patch': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”). This is the default.',
            '-s': 'Suppress all output from the diff machinery. Useful for commands like git show that show the patch by default to squelch their output, or to',
            '--no-patch': 'Suppress all output from the diff machinery. Useful for commands like git show that show the patch by default to squelch their output, or to',
            '-U': '<n>, --unified=<n>',
            '--output': '=<file>',
            '--output-indicator-new': '=<char>, --output-indicator-old=<char>, --output-indicator-context=<char>',
            '--raw': 'Generate the diff in raw format.',
            '--patch-with-raw': 'Synonym for -p --raw.',
            '--indent-heuristic': 'Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default.',
            '--no-indent-heuristic': 'Disable the indent heuristic.',
            '--minimal': 'Spend extra time to make sure the smallest possible diff is produced.',
            '--patience': 'Generate a diff using the \"patience diff\" algorithm.',
            '--histogram': 'Generate a diff using the \"histogram diff\" algorithm.'
        },
        'examples': [
            'git-diff  # Show changes between commits, commit and working t'
        ],
        'category': 'Other'
    },
    'git-diff-files': {
        'desc': 'Compares files in the working tree and the index',
        'common_flags': {
            '-p': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”).',
            '-u': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”).',
            '--patch': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”).',
            '-s': 'Suppress all output from the diff machinery. Useful for commands like git show that show the patch by default to squelch their output, or to',
            '--no-patch': 'Suppress all output from the diff machinery. Useful for commands like git show that show the patch by default to squelch their output, or to',
            '-U': '<n>, --unified=<n>',
            '--output': '=<file>',
            '--output-indicator-new': '=<char>, --output-indicator-old=<char>, --output-indicator-context=<char>',
            '--raw': 'Generate the diff in raw format. This is the default.',
            '--patch-with-raw': 'Synonym for -p --raw.',
            '--indent-heuristic': 'Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default.',
            '--no-indent-heuristic': 'Disable the indent heuristic.',
            '--minimal': 'Spend extra time to make sure the smallest possible diff is produced.',
            '--patience': 'Generate a diff using the \"patience diff\" algorithm.',
            '--histogram': 'Generate a diff using the \"histogram diff\" algorithm.'
        },
        'examples': [
            'git-diff-files  # Compares files in the working tree and the index'
        ],
        'category': 'Other'
    },
    'git-diff-index': {
        'desc': 'Compare a tree to the working tree or index',
        'common_flags': {
            '-p': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”).',
            '-u': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”).',
            '--patch': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”).',
            '-s': 'Suppress all output from the diff machinery. Useful for commands like git show that show the patch by default to squelch their output, or to',
            '--no-patch': 'Suppress all output from the diff machinery. Useful for commands like git show that show the patch by default to squelch their output, or to',
            '-U': '<n>, --unified=<n>',
            '--output': '=<file>',
            '--output-indicator-new': '=<char>, --output-indicator-old=<char>, --output-indicator-context=<char>',
            '--raw': 'Generate the diff in raw format. This is the default.',
            '--patch-with-raw': 'Synonym for -p --raw.',
            '--indent-heuristic': 'Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default.',
            '--no-indent-heuristic': 'Disable the indent heuristic.',
            '--minimal': 'Spend extra time to make sure the smallest possible diff is produced.',
            '--patience': 'Generate a diff using the \"patience diff\" algorithm.',
            '--histogram': 'Generate a diff using the \"histogram diff\" algorithm.'
        },
        'examples': [
            'git-diff-index  # Compare a tree to the working tree or index'
        ],
        'category': 'Other'
    },
    'git-diff-tree': {
        'desc': 'Compares the content and mode of blobs found via two tree objects',
        'common_flags': {
            '-p': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”).',
            '-u': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”).',
            '--patch': 'Generate patch (see the section called “GENERATING PATCH TEXT WITH -P”).',
            '-s': 'Suppress all output from the diff machinery. Useful for commands like git show that show the patch by default to squelch their output, or to',
            '--no-patch': 'Suppress all output from the diff machinery. Useful for commands like git show that show the patch by default to squelch their output, or to',
            '-U': '<n>, --unified=<n>',
            '--output': '=<file>',
            '--output-indicator-new': '=<char>, --output-indicator-old=<char>, --output-indicator-context=<char>',
            '--raw': 'Generate the diff in raw format. This is the default.',
            '--patch-with-raw': 'Synonym for -p --raw.',
            '--indent-heuristic': 'Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default.',
            '--no-indent-heuristic': 'Disable the indent heuristic.',
            '--minimal': 'Spend extra time to make sure the smallest possible diff is produced.',
            '--patience': 'Generate a diff using the \"patience diff\" algorithm.',
            '--histogram': 'Generate a diff using the \"histogram diff\" algorithm.'
        },
        'examples': [
            'git-diff-tree  # Compares the content and mode of blobs found via t'
        ],
        'category': 'Other'
    },
    'git-difftool': {
        'desc': 'Show changes using common diff tools',
        'common_flags': {
            '-d': 'Copy the modified files to a temporary location and perform a directory diff on them. This mode never prompts before launching the diff tool.',
            '--dir-diff': 'Copy the modified files to a temporary location and perform a directory diff on them. This mode never prompts before launching the diff tool.',
            '-y': 'Do not prompt before launching a diff tool.',
            '--no-prompt': 'Do not prompt before launching a diff tool.',
            '--prompt': 'Prompt before each invocation of the diff tool. This is the default behaviour; the option is provided to override any configuration settings.',
            '--rotate-to': '=<file>',
            '--skip-to': '=<file>',
            '-t': '<tool>, --tool=<tool>',
            '--tool-help': 'Print a list of diff tools that may be used with --tool.',
            '-x': '<command>, --extcmd=<command>',
            '-g': ', --[no-]gui'
        },
        'examples': [
            'git-difftool  # Show changes using common diff tools'
        ],
        'category': 'Other'
    },
    'git-fast-export': {
        'desc': 'Git data exporter',
        'common_flags': {
            '--progress': '=<n>',
            '--signed-tags': '=(verbatim|warn|warn-strip|strip|abort)',
            '--tag-of-filtered-object': '=(abort|drop|rewrite)',
            '-M': 'Perform move and/or copy detection, as described in the git-diff(1) manual page, and use it to generate rename and copy commands in the output',
            '-C': 'Perform move and/or copy detection, as described in the git-diff(1) manual page, and use it to generate rename and copy commands in the output',
            '--export-marks': '=<file>',
            '--import-marks': '=<file>',
            '--mark-tags': 'In addition to labelling blobs and commits with mark ids, also label tags. This is useful in conjunction with --export-marks and --import-marks,',
            '--fake-missing-tagger': 'Some old repositories have tags without a tagger. The fast-import protocol was pretty strict about that, and did not allow that. So fake a',
            '--use-done-feature': 'Start the stream with a feature done stanza, and terminate it with a done command.',
            '--no-data': 'Skip output of blob objects and instead refer to blobs via their original SHA-1 hash. This is useful when rewriting the directory structure or',
            '--full-tree': 'This option will cause fast-export to issue a \"deleteall\" directive for each commit followed by a full list of all files in the commit (as',
            '--anonymize': 'Anonymize the contents of the repository while still retaining the shape of the history and stored tree. See the section on ANONYMIZING below.',
            '--anonymize-map': '=<from>[:<to>]',
            '--reference-excluded-parents': 'By default, running a command such as git fast-export master~5..master will not include the commit master~5 and will make master~4 no longer'
        },
        'examples': [
            'git-fast-export  # Git data exporter'
        ],
        'category': 'Other'
    },
    'git-fast-import': {
        'desc': 'Backend for fast Git data importers',
        'common_flags': {
            '--force': 'Force updating modified existing branches, even if doing so would cause commits to be lost (as the new commit does not contain the old commit).',
            '--quiet': 'Disable the output shown by --stats, making fast-import usually be silent when it is successful. However, if the import stream has directives',
            '--stats': 'Display some basic statistics about the objects fast-import has created, the packfiles they were stored into, and the memory used by fast-import',
            '--allow-unsafe-features': 'Many command-line options can be provided as part of the fast-import stream itself by using the feature or option commands. However, some of',
            '--cat-blob-fd': '=<fd>',
            '--date-format': '=<fmt>',
            '--done': 'Terminate with error if there is no done command at the end of the stream. This option might be useful for detecting errors that cause the',
            '--export-marks': '=<file>',
            '--import-marks': '=<file>',
            '--import-marks-if-exists': '=<file>',
            '--rewrite-submodules-from': '=<name>:<file>, --rewrite-submodules-to=<name>:<file>',
            '--active-branches': '=<n>',
            '--big-file-threshold': '=<n>',
            '--depth': '=<n>',
            '--export-pack-edges': '=<file>'
        },
        'examples': [
            'git-fast-import  # Backend for fast Git data importers'
        ],
        'category': 'Other'
    },
    'git-fetch': {
        'desc': 'Download objects and refs from another repository',
        'common_flags': {
            '-a': 'Append ref names and object names of fetched refs to the existing contents of .git/FETCH_HEAD. Without this option old data in .git/FETCH_HEAD',
            '--append': 'Append ref names and object names of fetched refs to the existing contents of .git/FETCH_HEAD. Without this option old data in .git/FETCH_HEAD',
            '--atomic': 'Use an atomic transaction to update local refs. Either all refs are updated, or on error, no refs are updated.',
            '--depth': '=<depth>',
            '--deepen': '=<depth>',
            '--shallow-since': '=<date>',
            '--shallow-exclude': '=<revision>',
            '--unshallow': 'If the source repository is complete, convert a shallow repository to a complete one, removing all the limitations imposed by shallow',
            '--update-shallow': 'By default when fetching from a shallow repository, git fetch refuses refs that require updating .git/shallow. This option updates .git/shallow',
            '--negotiation-tip': '=<commit|glob>',
            '--negotiate-only': 'Do not fetch anything from the server, and instead print the ancestors of the provided --negotiation-tip=* arguments, which we have in common',
            '--dry-run': 'Show what would be done, without making any changes.',
            '--porcelain': 'Print the output to standard output in an easy-to-parse format for scripts. See section OUTPUT in git-fetch(1) for details.',
            '-f': 'When git fetch is used with <src>:<dst> refspec, it may refuse to update the local branch as discussed in the <refspec> part below. This option',
            '--force': 'When git fetch is used with <src>:<dst> refspec, it may refuse to update the local branch as discussed in the <refspec> part below. This option'
        },
        'examples': [
            'git-fetch  # Download objects and refs from another repository',
            'git-fetch -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-fetch-pack': {
        'desc': 'Receive missing objects from another repository',
        'common_flags': {
            '--all': 'Fetch all remote refs.',
            '--stdin': 'Take the list of refs from stdin, one per line. If there are refs specified on the command line in addition to this option, then the refs from',
            '-q': 'Pass -q flag to git unpack-objects; this makes the cloning process less verbose.',
            '--quiet': 'Pass -q flag to git unpack-objects; this makes the cloning process less verbose.',
            '-k': 'Do not invoke git unpack-objects on received data, but create a single packfile out of it instead, and store it in the object database. If',
            '--keep': 'Do not invoke git unpack-objects on received data, but create a single packfile out of it instead, and store it in the object database. If',
            '--thin': 'Fetch a \"thin\" pack, which records objects in deltified form based on objects not included in the pack to reduce network traffic.',
            '--include-tag': 'If the remote side supports it, annotated tags objects will be downloaded on the same connection as the other objects if the object the tag',
            '--upload-pack': '=<git-upload-pack>',
            '--exec': '=<git-upload-pack>',
            '--depth': '=<n>',
            '--shallow-since': '=<date>',
            '--shallow-exclude': '=<revision>',
            '--deepen-relative': 'Argument --depth specifies the number of commits from the current shallow boundary instead of from the tip of each remote branch history.',
            '--refetch': 'Skips negotiating commits with the server in order to fetch all matching objects. Use to reapply a new partial clone blob/tree filter.'
        },
        'examples': [
            'git-fetch-pack  # Receive missing objects from another repository',
            'git-fetch-pack --all  # Show all'
        ],
        'category': 'Other'
    },
    'git-filter-branch': {
        'desc': 'Rewrite branches',
        'common_flags': {
            '--setup': '<command>',
            '--subdirectory-filter': '<directory>',
            '--env-filter': '<command>',
            '--tree-filter': '<command>',
            '--index-filter': '<command>',
            '--parent-filter': '<command>',
            '--msg-filter': '<command>',
            '--commit-filter': ', though the same effect can be achieved by using the provided git_commit_non_empty_tree function in a commit filter.',
            '--tag-name-filter': '<command>',
            '--prune-empty': 'Some filters will generate empty commits that leave the tree untouched. This option instructs git-filter-branch to remove such commits if they',
            '--original': '<namespace>',
            '-d': '<directory>',
            '-f': 'git filter-branch refuses to start with an existing temporary directory or when there are already refs starting with refs/original/, unless',
            '--force': 'git filter-branch refuses to start with an existing temporary directory or when there are already refs starting with refs/original/, unless',
            '--state-branch': '<branch>'
        },
        'examples': [
            'git-filter-branch  # Rewrite branches'
        ],
        'category': 'Other'
    },
    'git-fmt-merge-msg': {
        'desc': 'Produce a merge commit message',
        'common_flags': {
            '--log': '[=<n>]',
            '--no-log': 'Do not list one-line descriptions from the actual commits being merged.',
            '-m': '<message>, --message <message>',
            '--into-name': '<branch>',
            '-F': '<file>, --file <file>'
        },
        'examples': [
            'git-fmt-merge-msg  # Produce a merge commit message'
        ],
        'category': 'Other'
    },
    'git-for-each-ref': {
        'desc': 'Output information on each ref',
        'common_flags': {
            '--stdin': 'If --stdin is supplied, then the list of patterns is read from standard input instead of from the argument list.',
            '--count': '=<count>',
            '--sort': '=<key>',
            '--format': '=<format>',
            '--color': '[=<when>]',
            '--shell': 'If given, strings that substitute %(fieldname) placeholders are quoted as string literals suitable for the specified host language. This is',
            '--perl': 'If given, strings that substitute %(fieldname) placeholders are quoted as string literals suitable for the specified host language. This is',
            '--python': 'If given, strings that substitute %(fieldname) placeholders are quoted as string literals suitable for the specified host language. This is',
            '--tcl': 'If given, strings that substitute %(fieldname) placeholders are quoted as string literals suitable for the specified host language. This is',
            '--points-at': '=<object>',
            '--merged': '[=<object>]',
            '--no-merged': '[=<object>]',
            '--contains': '[=<object>]',
            '--no-contains': '[=<object>]',
            '--ignore-case': 'Sorting and filtering refs are case insensitive.'
        },
        'examples': [
            'git-for-each-ref  # Output information on each ref'
        ],
        'category': 'Other'
    },
    'git-for-each-repo': {
        'desc': 'Run a Git command on a list of repositories',
        'common_flags': {
            '--config': '=<config>',
            '--keep-going': 'Continue with the remaining repositories if the command failed on a repository. The exit code will still indicate that the overall operation was'
        },
        'examples': [
            'git-for-each-repo  # Run a Git command on a list of repositories'
        ],
        'category': 'Other'
    },
    'git-format-patch': {
        'desc': 'Prepare patches for e-mail submission',
        'common_flags': {
            '-p': 'Generate plain patches without any diffstats.',
            '--no-stat': 'Generate plain patches without any diffstats.',
            '-U': '<n>, --unified=<n>',
            '--output': '=<file>',
            '--output-indicator-new': '=<char>, --output-indicator-old=<char>, --output-indicator-context=<char>',
            '--indent-heuristic': 'Enable the heuristic that shifts diff hunk boundaries to make patches easier to read. This is the default.',
            '--no-indent-heuristic': 'Disable the indent heuristic.',
            '--minimal': 'Spend extra time to make sure the smallest possible diff is produced.',
            '--patience': 'Generate a diff using the \"patience diff\" algorithm.',
            '--histogram': 'Generate a diff using the \"histogram diff\" algorithm.',
            '--anchored': '=<text>',
            '--diff-algorithm': '=default option.',
            '--stat': '[=<width>[,<name-width>[,<count>]]]',
            '--compact-summary': 'Output a condensed summary of extended header information such as file creations or deletions (\"new\" or \"gone\", optionally \"+l\" if it’s a',
            '--numstat': 'Similar to --stat, but shows number of added and deleted lines in decimal notation and pathname without abbreviation, to make it more machine'
        },
        'examples': [
            'git-format-patch  # Prepare patches for e-mail submission'
        ],
        'category': 'Other'
    },
    'git-fsck': {
        'desc': 'Verifies the connectivity and validity of the objects in the database',
        'common_flags': {
            '--no-reflogs': 'Do not consider commits that are referenced only by an entry in a reflog to be reachable. This option is meant only to search for commits that',
            '--unreachable': 'Print out objects that exist but that aren’t reachable from any of the reference nodes.',
            '--root': 'Report root nodes.',
            '--tags': 'Report tags.',
            '--cache': 'Consider any object recorded in the index also as a head node for an unreachability trace.',
            '--full': 'Check not just objects in GIT_OBJECT_DIRECTORY ($GIT_DIR/objects), but also the ones found in alternate object pools listed in',
            '--connectivity-only': 'Check only the connectivity of reachable objects, making sure that any objects referenced by a reachable tag, commit, or tree are present. This',
            '--strict': 'Enable more strict checking, namely to catch a file mode recorded with g+w bit set, which was created by older versions of Git. Existing',
            '--verbose': 'Be chatty.',
            '--lost-found': 'Write dangling objects into .git/lost-found/commit/ or .git/lost-found/other/, depending on type. If the object is a blob, the contents are',
            '--name-objects': 'When displaying names of reachable objects, in addition to the SHA-1 also display a name that describes how they are reachable, compatible with'
        },
        'examples': [
            'git-fsck  # Verifies the connectivity and validity of the obje',
            'git-fsck --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-gc': {
        'desc': 'Cleanup unnecessary files and optimize the local repository',
        'common_flags': {
            '--aggressive': 'Usually git gc runs very quickly while providing good disk space utilization and performance. This option will cause git gc to more aggressively',
            '--auto': 'With this option, git gc checks whether any housekeeping is required; if not, it exits without performing any work.',
            '--max-cruft-size': '=<n>',
            '--prune': '=<date>',
            '--no-prune': 'Do not prune any loose objects.',
            '--quiet': 'Suppress all progress reports.',
            '--force': 'Force git gc to run even if there may be another git gc instance running on this repository.',
            '--keep-largest-pack': 'All packs except the largest non-cruft pack, any packs marked with a .keep file, and any cruft pack(s) are consolidated into a single pack. When'
        },
        'examples': [
            'git-gc  # Cleanup unnecessary files and optimize the local r'
        ],
        'category': 'Other'
    },
    'git-grep': {
        'desc': 'Print lines matching a pattern',
        'common_flags': {
            '--cached': 'Instead of searching tracked files in the working tree, search blobs registered in the index file.',
            '--untracked': 'In addition to searching in the tracked files in the working tree, search also in untracked files.',
            '--no-index': '.',
            '--no-exclude-standard': 'Also search in ignored files by not honoring the .gitignore mechanism. Only useful with --untracked.',
            '--exclude-standard': 'Do not pay attention to ignored files specified via the .gitignore mechanism. Only useful when searching files in the current directory with',
            '--recurse-submodules': 'Recursively search in each submodule that is active and checked out in the repository. When used in combination with the <tree> option the',
            '-a': 'Process binary files as if they were text.',
            '--text': 'Process binary files as if they were text.',
            '--textconv': 'Honor textconv filter settings.',
            '--no-textconv': 'Do not honor textconv filter settings. This is the default.',
            '-i': 'Ignore case differences between the patterns and the files.',
            '--ignore-case': 'Ignore case differences between the patterns and the files.',
            '-I': 'Don’t match the pattern in binary files.',
            '--max-depth': '<depth>',
            '-r': 'Same as --max-depth=-1; this is the default.'
        },
        'examples': [
            'git-grep  # Print lines matching a pattern',
            'git-grep -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-hash-object': {
        'desc': 'Compute object ID and optionally create an object from a file',
        'common_flags': {
            '-t': '<type>',
            '-w': 'Actually write the object into the object database.',
            '--stdin': 'Read the object from standard input instead of from a file.',
            '--stdin-paths': 'Read file names from the standard input, one per line, instead of from the command-line.',
            '--path': 'Hash object as if it were located at the given path. The location of the file does not directly influence the hash value, but the path is used',
            '--no-filters': 'Hash the contents as is, ignoring any input filter that would have been chosen by the attributes mechanism, including the end-of-line',
            '--literally': 'Allow --stdin to hash any garbage into a loose object which might not otherwise pass standard object parsing or git-fsck checks. Useful for'
        },
        'examples': [
            'git-hash-object  # Compute object ID and optionally create an object '
        ],
        'category': 'Other'
    },
    'git-help': {
        'desc': 'Display help information about Git',
        'common_flags': {
            '-a': 'Print all the available commands on the standard output.',
            '--all': 'Print all the available commands on the standard output.',
            '--no-external-commands': 'When used with --all, exclude the listing of external \"git-*\" commands found in the $PATH.',
            '--no-aliases': 'When used with --all, exclude the listing of configured aliases.',
            '--verbose': 'When used with --all, print description for all recognized commands. This is the default.',
            '-c': 'List all available configuration variables. This is a short summary of the list in git-config(1).',
            '--config': 'List all available configuration variables. This is a short summary of the list in git-config(1).',
            '-g': 'Print a list of the Git concept guides on the standard output.',
            '--guides': 'Print a list of the Git concept guides on the standard output.',
            '--user-interfaces': 'Print a list of the repository, command and file interfaces documentation on the standard output.',
            '--developer-interfaces': 'Print a list of file formats, protocols and other developer interfaces documentation on the standard output.',
            '-i': 'Display manual page for the command in the info format. The info program will be used for that purpose.',
            '--info': 'Display manual page for the command in the info format. The info program will be used for that purpose.',
            '-m': 'Display manual page for the command in the man format. This option may be used to override a value set in the help.format configuration',
            '--man': 'Display manual page for the command in the man format. This option may be used to override a value set in the help.format configuration'
        },
        'examples': [
            'git-help  # Display help information about Git',
            'git-help --verbose  # Verbose output',
            'git-help -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-hook': {
        'desc': 'Run git hooks',
        'common_flags': {
            '--to-stdin': 'For \"run\"; specify a file which will be streamed into the hook’s stdin. The hook will receive the entire file from beginning to EOF.',
            '--ignore-missing': 'Ignore any missing hook by quietly returning zero. Used for tools that want to do a blind one-shot run of a hook that may or may not be present.'
        },
        'examples': [
            'git-hook  # Run git hooks'
        ],
        'category': 'Other'
    },
    'git-http-fetch': {
        'desc': 'Download from a remote Git repository via HTTP',
        'common_flags': {
            '-a': 'These options are ignored for historical reasons.',
            '-c': 'These options are ignored for historical reasons.',
            '-t': 'These options are ignored for historical reasons.',
            '-v': 'Report what is downloaded.',
            '-w': '<filename>',
            '--stdin': 'Instead of a commit id on the command line (which is not expected in this case), git http-fetch expects lines on stdin in the format',
            '--packfile': '=<hash>',
            '--index-pack-args': '=<args>',
            '--recover': 'Verify that everything reachable from target is fetched. Used after an earlier fetch is interrupted.'
        },
        'examples': [
            'git-http-fetch  # Download from a remote Git repository via HTTP',
            'git-http-fetch -v  # Show version',
            'git-http-fetch -v  # Verbose output',
            'git-http-fetch -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-http-push': {
        'desc': 'Push objects over HTTP/DAV to another repository',
        'common_flags': {
            '--all': 'Do not assume that the remote repository is complete in its current state, and verify all objects in the entire local ref’s history exist in the',
            '--force': 'Usually, the command refuses to update a remote ref that is not an ancestor of the local ref used to overwrite it. This flag disables the check.',
            '--dry-run': 'Do everything except actually send the updates.',
            '--verbose': 'Report the list of objects being walked locally and the list of objects successfully sent to the remote repository.',
            '-d': 'Remove <ref> from remote repository. The specified branch cannot be the remote HEAD. If -d is specified, the following other conditions must',
            '-D': 'Remove <ref> from remote repository. The specified branch cannot be the remote HEAD. If -d is specified, the following other conditions must'
        },
        'examples': [
            'git-http-push  # Push objects over HTTP/DAV to another repository',
            'git-http-push --verbose  # Verbose output',
            'git-http-push --all  # Show all'
        ],
        'category': 'Other'
    },
    'git-imap-send': {
        'desc': 'Send a collection of patches from stdin to an IMAP folder',
        'common_flags': {
            '-v': 'Be verbose.',
            '--verbose': 'Be verbose.',
            '-q': 'Be quiet.',
            '--quiet': 'Be quiet.',
            '--curl': 'Use libcurl to communicate with the IMAP server, unless tunneling into it. Ignored if Git was built without the USE_CURL_FOR_IMAP_SEND option',
            '--no-curl': 'Talk to the IMAP server using git’s own IMAP routines instead of using libcurl. Ignored if Git was built with the NO_OPENSSL option set.'
        },
        'examples': [
            'git-imap-send  # Send a collection of patches from stdin to an IMAP',
            'git-imap-send -v  # Show version',
            'git-imap-send -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-index-pack': {
        'desc': 'Build pack index file for an existing packed archive',
        'common_flags': {
            '-v': 'Be verbose about what is going on, including progress status.',
            '-o': '<index-file>',
            '--stdin': 'When this flag is provided, the pack is read from stdin instead and a copy is then written to <pack-file>. If <pack-file> is not specified, the',
            '--fix-thin': 'Fix a \"thin\" pack produced by git pack-objects --thin (see git-pack-objects(1) for details) by adding the excluded objects the deltified objects',
            '--keep': '=<msg>',
            '--index-version': '=<version>[,<offset>]',
            '--strict': '[=<msg-id>=<severity>...]',
            '--progress-title': 'For internal use only.',
            '--check-self-contained-and-connected': 'Die if the pack contains broken links. For internal use only.',
            '--fsck-objects': '=\"missingEmail=ignore,badTagName=ignore\". See the entry for the fsck.<msg-id> configuration options in git-fsck(1) for more',
            '--threads': '=<n>',
            '--max-input-size': '=<size>',
            '--object-format': '=<hash-algorithm>',
            '--promisor': '[=<message>]'
        },
        'examples': [
            'git-index-pack  # Build pack index file for an existing packed archi',
            'git-index-pack -v  # Show version',
            'git-index-pack -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-init': {
        'desc': 'Create an empty Git repository or reinitialize an existing one',
        'common_flags': {
            '-q': 'Only print error and warning messages; all other output will be suppressed.',
            '--quiet': 'Only print error and warning messages; all other output will be suppressed.',
            '--bare': 'Create a bare repository. If GIT_DIR environment is not set, it is set to the current working directory.',
            '--object-format': '=<format>',
            '--ref-format': '=<format>',
            '--template': '=<template-directory>',
            '--separate-git-dir': '=<git-dir>',
            '-b': '<branch-name>, --initial-branch=<branch-name>',
            '--shared': '[=(false|true|umask|group|all|world|everybody|<perm>)]'
        },
        'examples': [
            'git-init  # Create an empty Git repository or reinitialize an '
        ],
        'category': 'Other'
    },
    'git-instaweb': {
        'desc': 'Instantly browse your working repository in gitweb',
        'common_flags': {
            '-l': 'Only bind the web server to the local IP (127.0.0.1).',
            '--local': 'Only bind the web server to the local IP (127.0.0.1).',
            '-d': 'The HTTP daemon command-line that will be executed. Command-line options may be specified here, and the configuration file will be added at the',
            '--httpd': 'The HTTP daemon command-line that will be executed. Command-line options may be specified here, and the configuration file will be added at the',
            '-m': 'The module path (only needed if httpd is Apache). (Default: /usr/lib/apache2/modules)',
            '--module-path': 'The module path (only needed if httpd is Apache). (Default: /usr/lib/apache2/modules)',
            '-p': 'The port number to bind the httpd to. (Default: 1234)',
            '--port': 'The port number to bind the httpd to. (Default: 1234)',
            '-b': 'The web browser that should be used to view the gitweb page. This will be passed to the git web--browse helper script along with the URL of the',
            '--browser': 'The web browser that should be used to view the gitweb page. This will be passed to the git web--browse helper script along with the URL of the'
        },
        'examples': [
            'git-instaweb  # Instantly browse your working repository in gitweb'
        ],
        'category': 'Other'
    },
    'git-interpret-trailers': {
        'desc': 'Add or parse structured information in commit messages',
        'common_flags': {
            '--in-place': 'Edit the files in place.',
            '--trim-empty': 'If the <value> part of any trailer contains only whitespace, the whole trailer will be removed from the output. This applies to existing',
            '--trailer': '<key>[(=|:)<value>]',
            '--where': '<placement>, --no-where',
            '--if-exists': 'overrides the trailer.ifExists and any applicable trailer.<keyAlias>.ifExists configuration variables and applies to all --trailer',
            '--if-missing': '<action>, --no-if-missing',
            '--only-trailers': 'Output only the trailers, not any other parts of the input.',
            '--only-input': 'Output only trailers that exist in the input; do not add any from the command-line or by applying trailer.* configuration variables.',
            '--unfold': 'If a trailer has a value that runs over multiple lines (aka \"folded\"), reformat the value into a single line.',
            '--parse': 'A convenience alias for --only-trailers --only-input --unfold. This makes it easier to only see the trailers coming from the input without',
            '--no-divider': 'Do not treat --- as the end of the commit message. Use this when you know your input contains just the commit message itself (and not an email'
        },
        'examples': [
            'git-interpret-trailers  # Add or parse structured information in commit mess'
        ],
        'category': 'Other'
    },
    'git-log': {
        'desc': 'Show commit logs',
        'common_flags': {
            '--follow': 'Continue listing the history of a file beyond renames (works only for a single file).',
            '--no-decorate': '[=short|full|auto|no]',
            '--decorate': '=short. Default to configuration value of log.decorate if configured, otherwise, auto.',
            '--decorate-refs': '=<pattern>, --decorate-refs-exclude=<pattern>',
            '--clear-decorations': 'When specified, this option clears all previous --decorate-refs or --decorate-refs-exclude options and relaxes the default decoration filter to',
            '--source': 'Print out the ref name given on the command line by which each commit was reached.',
            '--full-diff': 'Without this flag, git log -p <path>... shows commits that touch the specified paths, and diffs about the same specified paths. With this, the',
            '--log-size': 'Include a line “log size <number>” in the output for each commit, where <number> is the length of that commit’s message in bytes. Intended to',
            '-L': '<start>,<end>:<file>, -L:<funcname>:<file>',
            '--patch': '. Patch output can be suppressed using --no-patch, but other diff formats (namely --raw, --numstat, --shortstat, --dirstat, --summary,',
            '--name-only': ') are not currently implemented.',
            '--name-status': ') are not currently implemented.',
            '--check': ') are not currently implemented.',
            '--grep': '=<pattern> further limits to commits whose log message has a line that matches <pattern>), unless otherwise noted.',
            '--skip': '=<number>'
        },
        'examples': [
            'git-log  # Show commit logs'
        ],
        'category': 'Other'
    },
    'git-ls-files': {
        'desc': 'Show information about files in the index and the working tree',
        'common_flags': {
            '-c': 'Show all files cached in Git’s index, i.e. all tracked files. (This is the default if no -c/-s/-d/-o/-u/-k/-m/--resolve-undo options are',
            '--cached': 'Show all files cached in Git’s index, i.e. all tracked files. (This is the default if no -c/-s/-d/-o/-u/-k/-m/--resolve-undo options are',
            '-d': 'Show files with an unstaged deletion',
            '--deleted': 'Show files with an unstaged deletion',
            '-m': 'Show files with an unstaged modification (note that an unstaged deletion also counts as an unstaged modification)',
            '--modified': 'Show files with an unstaged modification (note that an unstaged deletion also counts as an unstaged modification)',
            '-o': '/--others.',
            '--others': 'Show other (i.e. untracked) files in the output',
            '-i': 'Show only ignored files in the output. Must be used with either an explicit -c or -o. When showing files in the index (i.e. when used with -c),',
            '--ignored': 'Show only ignored files in the output. Must be used with either an explicit -c or -o. When showing files in the index (i.e. when used with -c),',
            '-s': 'Show staged contents\' mode bits, object name and stage number in the output.',
            '--stage': 'Show staged contents\' mode bits, object name and stage number in the output.',
            '--directory': 'If a whole directory is classified as \"other\", show just its name (with a trailing slash) and not its whole contents. Has no effect without',
            '--no-empty-directory': 'Do not list empty directories. Has no effect without --directory.',
            '-u': 'Show information about unmerged files in the output, but do not show any other tracked files (forces --stage, overrides --cached).'
        },
        'examples': [
            'git-ls-files  # Show information about files in the index and the '
        ],
        'category': 'Other'
    },
    'git-ls-remote': {
        'desc': 'List references in a remote repository',
        'common_flags': {
            '-b': 'Limit to only local branches and local tags, respectively. These options are not mutually exclusive; when given both, references stored in',
            '--branches': 'Limit to only local branches and local tags, respectively. These options are not mutually exclusive; when given both, references stored in',
            '-t': 'Limit to only local branches and local tags, respectively. These options are not mutually exclusive; when given both, references stored in',
            '--tags': 'Limit to only local branches and local tags, respectively. These options are not mutually exclusive; when given both, references stored in',
            '--refs': 'Do not show peeled tags or pseudorefs like HEAD in the output.',
            '-q': 'Do not print remote URL to stderr.',
            '--quiet': 'Do not print remote URL to stderr.',
            '--upload-pack': '=<exec>',
            '--exit-code': 'Exit with status \"2\" when no matching refs are found in the remote repository. Usually the command exits with status \"0\" to indicate it',
            '--get-url': 'Expand the URL of the given remote repository taking into account any \"url.<base>.insteadOf\" config setting (See git-config(1)) and exit without',
            '--symref': 'In addition to the object pointed by it, show the underlying ref pointed by it when showing a symbolic ref. Currently, upload-pack only shows',
            '--sort': '=<key>',
            '-o': '<option>, --server-option=<option>'
        },
        'examples': [
            'git-ls-remote  # List references in a remote repository'
        ],
        'category': 'Other'
    },
    'git-ls-tree': {
        'desc': 'List the contents of a tree object',
        'common_flags': {
            '-d': 'Show only the named tree entry itself, not its children.',
            '-r': 'Recurse into sub-trees.',
            '-t': 'Show tree entries even when going to recurse them. Has no effect if -r was not passed. -d implies -t.',
            '-l': 'Show object size of blob (file) entries.',
            '--long': 'Show object size of blob (file) entries.',
            '-z': '\\0 line termination on output and do not quote filenames. See OUTPUT FORMAT below for more information.',
            '--name-only': 'List only filenames (instead of the \"long\" output), one per line. Cannot be combined with --object-only.',
            '--name-status': 'List only filenames (instead of the \"long\" output), one per line. Cannot be combined with --object-only.',
            '--object-only': 'List only names of the objects, one per line. Cannot be combined with --name-only or --name-status. This is equivalent to specifying',
            '--format': '=<format>',
            '--abbrev': '[=<n>]',
            '--full-name': 'Instead of showing the path names relative to the current working directory, show the full path names.',
            '--full-tree': 'Do not limit the listing to the current working directory. Implies --full-name.'
        },
        'examples': [
            'git-ls-tree  # List the contents of a tree object'
        ],
        'category': 'Other'
    },
    'git-mailinfo': {
        'desc': 'Extracts patch and authorship from a single e-mail message',
        'common_flags': {
            '-k': 'Usually the program removes email cruft from the Subject: header line to extract the title line for the commit log message. This option prevents',
            '-b': 'When -k is not in effect, all leading strings bracketed with [ and ] pairs are stripped. This option limits the stripping to only the pairs',
            '-u': 'The commit log message, author name and author email are taken from the e-mail, and after minimally decoding MIME transfer encoding, re-coded in',
            '--encoding': '=<encoding>',
            '-n': 'Disable all charset re-coding of the metadata.',
            '-m': 'Copy the Message-ID header at the end of the commit message. This is useful in order to associate commits with mailing list discussions.',
            '--message-id': 'Copy the Message-ID header at the end of the commit message. This is useful in order to associate commits with mailing list discussions.',
            '--scissors': 'Remove everything in body before a scissors line (e.g. \"-- >8 --\"). The line represents scissors and perforation marks, and is used to request',
            '--no-scissors': 'Ignore scissors lines. Useful for overriding mailinfo.scissors settings.',
            '--quoted-cr': '=<action>'
        },
        'examples': [
            'git-mailinfo  # Extracts patch and authorship from a single e-mail'
        ],
        'category': 'Other'
    },
    'git-mailsplit': {
        'desc': 'Simple UNIX mbox splitter program',
        'common_flags': {
            '-o': '<directory>',
            '-b': 'If any file doesn’t begin with a From line, assume it is a single mail message instead of signaling an error.',
            '-d': '<prec>',
            '-f': '<nn>',
            '--keep-cr': 'Do not remove \\r from lines ending with \\r\\n.',
            '--mboxrd': 'Input is of the \"mboxrd\" format and \"^>+From \" line escaping is reversed.'
        },
        'examples': [
            'git-mailsplit  # Simple UNIX mbox splitter program'
        ],
        'category': 'Other'
    },
    'git-maintenance': {
        'desc': 'Run tasks to optimize Git repository data',
        'common_flags': {
            '--auto': 'When combined with the run subcommand, run maintenance tasks only if certain thresholds are met. For example, the gc task runs when the number',
            '--schedule': 'When combined with the run subcommand, run maintenance tasks only if certain time conditions are met, as specified by the',
            '--quiet': 'Do not report progress or other information over stderr.',
            '--task': '=<task>',
            '--scheduler': '=auto|crontab|systemd-timer|launchctl|schtasks'
        },
        'examples': [
            'git-maintenance  # Run tasks to optimize Git repository data'
        ],
        'category': 'Other'
    },
    'git-merge': {
        'desc': 'Join two or more development histories together',
        'common_flags': {
            '--commit': 'Perform the merge and commit the result. This option can be used to override --no-commit.',
            '--no-commit': 'Perform the merge and commit the result. This option can be used to override --no-commit.',
            '--edit': 'Invoke an editor before committing successful mechanical merge to further edit the auto-generated merge message, so that the user can explain',
            '-e': 'Invoke an editor before committing successful mechanical merge to further edit the auto-generated merge message, so that the user can explain',
            '--no-edit': 'Invoke an editor before committing successful mechanical merge to further edit the auto-generated merge message, so that the user can explain',
            '--cleanup': '=<mode>',
            '--ff': 'Specifies how a merge is handled when the merged-in history is already a descendant of the current history. --ff is the default unless merging',
            '--no-ff': 'Specifies how a merge is handled when the merged-in history is already a descendant of the current history. --ff is the default unless merging',
            '--ff-only': 'Specifies how a merge is handled when the merged-in history is already a descendant of the current history. --ff is the default unless merging',
            '-S': '[<keyid>], --gpg-sign[=<keyid>], --no-gpg-sign',
            '--log': '[=<n>], --no-log',
            '--signoff': 'Add a Signed-off-by trailer by the committer at the end of the commit log message. The meaning of a signoff depends on the project to which',
            '--no-signoff': 'Add a Signed-off-by trailer by the committer at the end of the commit log message. The meaning of a signoff depends on the project to which',
            '--stat': 'Show a diffstat at the end of the merge. The diffstat is also controlled by the configuration option merge.stat.',
            '-n': 'Show a diffstat at the end of the merge. The diffstat is also controlled by the configuration option merge.stat.'
        },
        'examples': [
            'git-merge  # Join two or more development histories together'
        ],
        'category': 'Other'
    },
    'git-merge-base': {
        'desc': 'Find as good common ancestors as possible for a merge',
        'common_flags': {
            '-a': 'Output all merge bases for the commits, instead of just one.',
            '--all': 'Output all merge bases for the commits, instead of just one.'
        },
        'examples': [
            'git-merge-base  # Find as good common ancestors as possible for a me',
            'git-merge-base -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-merge-file': {
        'desc': 'Run a three-way file merge',
        'common_flags': {
            '--object-id': 'Specify the contents to merge as blobs in the current repository instead of files. In this case, the operation must take place within a valid',
            '-L': '<label>',
            '-p': 'Send results to standard output instead of overwriting <current>.',
            '-q': 'Quiet; do not warn about conflicts.',
            '--diff3': 'Show conflicts in \"diff3\" style.',
            '--zdiff3': 'Show conflicts in \"zdiff3\" style.',
            '--ours': 'Instead of leaving conflicts in the file, resolve conflicts favouring our (or their or both) side of the lines.',
            '--theirs': 'Instead of leaving conflicts in the file, resolve conflicts favouring our (or their or both) side of the lines.',
            '--union': 'Instead of leaving conflicts in the file, resolve conflicts favouring our (or their or both) side of the lines.',
            '--diff-algorithm': '={patience|minimal|histogram|myers}'
        },
        'examples': [
            'git-merge-file  # Run a three-way file merge'
        ],
        'category': 'Other'
    },
    'git-merge-index': {
        'desc': 'Run a merge for files needing merging',
        'common_flags': {
            '-a': 'Run merge against all files in the index that need merging.',
            '-o': 'Instead of stopping at the first failed merge, do all of them in one shot - continue with merging even when previous merges returned errors, and',
            '-q': 'Do not complain about a failed merge program (a merge program failure usually indicates conflicts during the merge). This is for porcelains'
        },
        'examples': [
            'git-merge-index  # Run a merge for files needing merging',
            'git-merge-index -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-merge-tree': {
        'desc': 'Perform merge without touching index or working tree',
        'common_flags': {
            '-z': 'Do not quote filenames in the <Conflicted file info> section, and end each filename with a NUL character rather than newline. Also begin the',
            '--name-only': 'In the Conflicted file info section, instead of writing a list of (mode, oid, stage, path) tuples to output for conflicted files, just provide a',
            '--allow-unrelated-histories': 'merge-tree will by default error out if the two branches specified share no common history. This flag can be given to override that check and',
            '--merge-base': '=<tree-ish>',
            '-X': '<option>, --strategy-option=<option>'
        },
        'examples': [
            'git-merge-tree  # Perform merge without touching index or working tr'
        ],
        'category': 'Other'
    },
    'git-mergetool': {
        'desc': 'Run merge conflict resolution tools to resolve merge conflicts',
        'common_flags': {
            '-t': '<tool>, --tool=<tool>',
            '--tool-help': 'Print a list of merge tools that may be used with --tool.',
            '-y': 'Don’t prompt before each invocation of the merge resolution program. This is the default if the merge resolution program is explicitly specified',
            '--no-prompt': 'Don’t prompt before each invocation of the merge resolution program. This is the default if the merge resolution program is explicitly specified',
            '--prompt': 'Prompt before each invocation of the merge resolution program to give the user a chance to skip the path.',
            '-g': 'When git-mergetool is invoked with the -g or --gui option, the default merge tool will be read from the configured merge.guitool variable',
            '--gui': 'When git-mergetool is invoked with the -g or --gui option, the default merge tool will be read from the configured merge.guitool variable',
            '--no-gui': 'This overrides a previous -g or --gui setting or mergetool.guiDefault configuration and reads the default merge tool from the configured',
            '-O': '<orderfile>'
        },
        'examples': [
            'git-mergetool  # Run merge conflict resolution tools to resolve mer'
        ],
        'category': 'Other'
    },
    'git-mktag': {
        'desc': 'Creates a tag object with extra validation',
        'common_flags': {
            '--strict': 'By default mktag turns on the equivalent of git-fsck(1) --strict mode. Use --no-strict to disable it.'
        },
        'examples': [
            'git-mktag  # Creates a tag object with extra validation'
        ],
        'category': 'Other'
    },
    'git-mktree': {
        'desc': 'Build a tree-object from ls-tree formatted text',
        'common_flags': {
            '-z': 'Read the NUL-terminated ls-tree -z output instead.',
            '--missing': 'Allow missing objects. The default behaviour (without this option) is to verify that each tree entry’s hash identifies an existing object. This',
            '--batch': 'Allow building of more than one tree object before exiting. Each tree is separated by a single blank line. The final newline is optional. Note -'
        },
        'examples': [
            'git-mktree  # Build a tree-object from ls-tree formatted text'
        ],
        'category': 'Other'
    },
    'git-multi-pack-index': {
        'desc': 'Write and verify multi-pack-indexes',
        'common_flags': {
            '--object-dir': '=<dir>',
            '--preferred-pack': '=<pack>',
            '--stdin-packs': 'Write a multi-pack index containing only the set of line-delimited pack index basenames provided over stdin.',
            '--refs-snapshot': '=<path>',
            '--incremental': 'Write an incremental MIDX file containing only objects and packs not present in an existing MIDX layer. Migrates non-incremental MIDXs to'
        },
        'examples': [
            'git-multi-pack-index  # Write and verify multi-pack-indexes'
        ],
        'category': 'Other'
    },
    'git-mv': {
        'desc': 'Move or rename a file, a directory, or a symlink',
        'common_flags': {
            '-f': 'Force renaming or moving of a file even if the <destination> exists.',
            '--force': 'Force renaming or moving of a file even if the <destination> exists.',
            '-k': 'Skip move or rename actions which would lead to an error condition. An error happens when a source is neither existing nor controlled by Git, or',
            '-n': 'Do nothing; only show what would happen',
            '--dry-run': 'Do nothing; only show what would happen',
            '-v': 'Report the names of files as they are moved.',
            '--verbose': 'Report the names of files as they are moved.'
        },
        'examples': [
            'git-mv  # Move or rename a file, a directory, or a symlink',
            'git-mv -v  # Show version',
            'git-mv -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-name-rev': {
        'desc': 'Find symbolic names for given revs',
        'common_flags': {
            '--tags': 'Do not use branch names, but only tags to name the commits',
            '--refs': '=<pattern>',
            '--exclude': '=<pattern>',
            '--all': 'List all commits reachable from all refs',
            '--annotate-stdin': 'Transform stdin by substituting all the 40-character SHA-1 hexes (say $hex) with \"$hex ($rev_name)\". When used with --name-only, substitute with',
            '--name-only': 'Instead of printing both the SHA-1 and the name, print only the name. If given with --tags the usual tag prefix of \"tags/\" is also omitted from',
            '--no-undefined': 'Die with error code != 0 when a reference is undefined, instead of printing undefined.',
            '--always': 'Show uniquely abbreviated commit object as fallback.'
        },
        'examples': [
            'git-name-rev  # Find symbolic names for given revs',
            'git-name-rev --all  # Show all'
        ],
        'category': 'Other'
    },
    'git-notes': {
        'desc': 'Add or inspect object notes',
        'common_flags': {
            '-f': 'When adding notes to an object that already has notes, overwrite the existing notes (instead of aborting).',
            '--force': 'When adding notes to an object that already has notes, overwrite the existing notes (instead of aborting).',
            '-m': '<msg>, --message=<msg>',
            '--no-stripspace': '.',
            '-F': '<file>, --file=<file>',
            '-C': '<object>, --reuse-message=<object>',
            '-c': '<object>, --reedit-message=<object>',
            '--allow-empty': 'Allow an empty note object to be stored. The default behavior is to automatically remove empty notes.',
            '--ref': '<ref>',
            '--ignore-missing': 'Do not consider it an error to request removing notes from an object that does not have notes attached to it.',
            '--stdin': 'Also read the object names to remove notes from the standard input (there is no reason you cannot combine this with object names from the',
            '-n': 'Do not remove anything; just report the object names whose notes would be removed.',
            '--dry-run': 'Do not remove anything; just report the object names whose notes would be removed.',
            '-s': '<strategy>, --strategy=<strategy>',
            '--commit': 'Finalize an in-progress git notes merge. Use this option when you have resolved the conflicts that git notes merge stored in'
        },
        'examples': [
            'git-notes  # Add or inspect object notes'
        ],
        'category': 'Other'
    },
    'git-pack-objects': {
        'desc': 'Create a packed archive of objects',
        'common_flags': {
            '--stdout': 'Write the pack contents (what would have been written to .pack file) out to the standard output.',
            '--revs': '.',
            '--unpacked': 'This implies --revs. When processing the list of revision arguments read from the standard input, limit the objects packed to those that are not',
            '--all': 'This implies --revs. In addition to the list of revision arguments read from the standard input, pretend as if all refs under refs/ are',
            '--include-tag': 'Include unasked-for annotated tags if the object they reference was included in the resulting packfile. This can be useful to send new tags to',
            '--stdin-packs': 'Read the basenames of packfiles (e.g., pack-1234abcd.pack) from the standard input, instead of object names or revision arguments. The resulting',
            '--cruft': 'Packs unreachable objects into a separate \"cruft\" pack, denoted by the existence of a .mtimes file. Typically used by git repack --cruft.',
            '--cruft-expiration': '=<approxidate>',
            '--window': '=<n>, --depth=<n>',
            '--window-memory': '=<n>',
            '--max-pack-size': '=<n>',
            '--honor-pack-keep': 'This flag causes an object already in a local pack that has a .keep file to be ignored, even if it would have otherwise been packed.',
            '--keep-pack': '=<pack-name>',
            '--incremental': 'This flag causes an object already in a pack to be ignored even if it would have otherwise been packed.',
            '--local': 'This flag causes an object that is borrowed from an alternate object store to be ignored even if it would have otherwise been packed.'
        },
        'examples': [
            'git-pack-objects  # Create a packed archive of objects',
            'git-pack-objects --all  # Show all'
        ],
        'category': 'Other'
    },
    'git-pack-redundant': {
        'desc': 'Find redundant pack files',
        'common_flags': {
            '--all': 'Processes all packs. Any filenames on the command line are ignored.',
            '--alt-odb': 'Don’t require objects present in packs from alternate object database (odb) directories to be present in local packs.',
            '--verbose': 'Outputs some statistics to stderr. Has a small performance penalty.'
        },
        'examples': [
            'git-pack-redundant  # Find redundant pack files',
            'git-pack-redundant --verbose  # Verbose output',
            'git-pack-redundant --all  # Show all'
        ],
        'category': 'Other'
    },
    'git-pack-refs': {
        'desc': 'Pack heads and tags for efficient repository access',
        'common_flags': {
            '--all': 'The command by default packs all tags and refs that are already packed, and leaves other refs alone. This is because branches are expected to be',
            '--no-prune': 'The command usually removes loose refs under $GIT_DIR/refs hierarchy after packing them. This option tells it not to.',
            '--auto': 'Pack refs as needed depending on the current state of the ref database. The behavior depends on the ref format used by the repository and may',
            '--include': '<pattern>',
            '--exclude': '<pattern>'
        },
        'examples': [
            'git-pack-refs  # Pack heads and tags for efficient repository acces',
            'git-pack-refs --all  # Show all'
        ],
        'category': 'Other'
    },
    'git-patch-id': {
        'desc': 'Compute unique ID for a patch',
        'common_flags': {
            '--verbatim': 'Calculate the patch-id of the input as it is given, do not strip any whitespace.',
            '--stable': 'Use a \"stable\" sum of hashes as the patch ID. With this option:',
            '--unstable': 'Use an \"unstable\" hash as the patch ID. With this option, the result produced is compatible with the patch-id value produced by git 1.9 and'
        },
        'examples': [
            'git-patch-id  # Compute unique ID for a patch'
        ],
        'category': 'Other'
    },
    'git-prune': {
        'desc': 'Prune all unreachable objects from the object database',
        'common_flags': {
            '-n': 'Do not remove anything; just report what it would remove.',
            '--dry-run': 'Do not remove anything; just report what it would remove.',
            '-v': 'Report all removed objects.',
            '--verbose': 'Report all removed objects.',
            '--progress': 'Show progress.',
            '--expire': '<time>'
        },
        'examples': [
            'git-prune  # Prune all unreachable objects from the object data',
            'git-prune -v  # Show version',
            'git-prune -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-prune-packed': {
        'desc': 'Remove extra objects that are already in pack files',
        'common_flags': {
            '-n': 'Don’t actually remove any objects, only show those that would have been removed.',
            '--dry-run': 'Don’t actually remove any objects, only show those that would have been removed.',
            '-q': 'Squelch the progress indicator.',
            '--quiet': 'Squelch the progress indicator.'
        },
        'examples': [
            'git-prune-packed  # Remove extra objects that are already in pack file'
        ],
        'category': 'Other'
    },
    'git-pull': {
        'desc': 'Fetch from and integrate with another repository or a local branch',
        'common_flags': {
            '-q': 'This is passed to both underlying git-fetch to squelch reporting of during transfer, and underlying git-merge to squelch output during merging.',
            '--quiet': 'This is passed to both underlying git-fetch to squelch reporting of during transfer, and underlying git-merge to squelch output during merging.',
            '-v': 'Pass --verbose to git-fetch and git-merge.',
            '--verbose': 'Pass --verbose to git-fetch and git-merge.',
            '--commit': 'Perform the merge and commit the result. This option can be used to override --no-commit. Only useful when merging.',
            '--no-commit': 'Perform the merge and commit the result. This option can be used to override --no-commit. Only useful when merging.',
            '--edit': 'Invoke an editor before committing successful mechanical merge to further edit the auto-generated merge message, so that the user can explain',
            '-e': 'Invoke an editor before committing successful mechanical merge to further edit the auto-generated merge message, so that the user can explain',
            '--no-edit': 'Invoke an editor before committing successful mechanical merge to further edit the auto-generated merge message, so that the user can explain',
            '--cleanup': '=<mode>',
            '--ff-only': 'Only update to the new history if there is no divergent local history. This is the default when no method for reconciling divergent histories is',
            '--ff': 'When merging rather than rebasing, specifies how a merge is handled when the merged-in history is already a descendant of the current history.',
            '--no-ff': 'When merging rather than rebasing, specifies how a merge is handled when the merged-in history is already a descendant of the current history.',
            '-S': '[<keyid>], --gpg-sign[=<keyid>], --no-gpg-sign',
            '--log': '[=<n>], --no-log'
        },
        'examples': [
            'git-pull  # Fetch from and integrate with another repository o',
            'git-pull -v  # Show version',
            'git-pull -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-push': {
        'desc': 'Update remote refs along with associated objects',
        'common_flags': {
            '--all': 'Push all branches (i.e. refs under refs/heads/); cannot be used with other <refspec>.',
            '--branches': 'Push all branches (i.e. refs under refs/heads/); cannot be used with other <refspec>.',
            '--prune': 'Remove remote branches that don’t have a local counterpart. For example a remote branch tmp will be removed if a local branch with the same name',
            '--mirror': 'Instead of naming each ref to push, specifies that all refs under refs/ (which includes but is not limited to refs/heads/, refs/remotes/, and',
            '-n': 'Do everything except actually send the updates.',
            '--dry-run': 'Do everything except actually send the updates.',
            '--porcelain': 'Produce machine-readable output. The output status line for each ref will be tab-separated and sent to stdout instead of stderr. The full',
            '-d': 'All listed refs are deleted from the remote repository. This is the same as prefixing all refs with a colon.',
            '--delete': 'All listed refs are deleted from the remote repository. This is the same as prefixing all refs with a colon.',
            '--tags': 'All refs under refs/tags are pushed, in addition to refspecs explicitly listed on the command line.',
            '--follow-tags': 'Push all the refs that would be pushed without this option, and also push annotated tags in refs/tags that are missing from the remote but are',
            '--no-signed': ', no signing will be attempted. If true or --signed, the push will fail if the server does not support signed pushes. If set to',
            '-o': '<option>, --push-option=<option>',
            '--receive-pack': '=<git-receive-pack>, --exec=<git-receive-pack>',
            '--force-with-lease': 'alone, without specifying the details, will protect all remote refs that are going to be updated by requiring their current'
        },
        'examples': [
            'git-push  # Update remote refs along with associated objects',
            'git-push --all  # Show all'
        ],
        'category': 'Other'
    },
    'git-quiltimport': {
        'desc': 'Applies a quilt patchset onto the current branch',
        'common_flags': {
            '-n': 'Walk through the patches in the series and warn if we cannot find all of the necessary information to commit a patch. At the time of this',
            '--dry-run': 'Walk through the patches in the series and warn if we cannot find all of the necessary information to commit a patch. At the time of this',
            '--author': 'Author Name <Author Email>',
            '--patches': '<dir>',
            '--series': '<file>',
            '--keep-non-patch': 'Pass -b flag to git mailinfo (see git-mailinfo(1)).'
        },
        'examples': [
            'git-quiltimport  # Applies a quilt patchset onto the current branch'
        ],
        'category': 'Other'
    },
    'git-range-diff': {
        'desc': 'Compare two commit ranges (e.g. two versions of a branch)',
        'common_flags': {
            '--no-dual-color': 'When the commit diffs differ, ‘git range-diff` recreates the original diffs’ coloring, and adds outer -/+ diff markers with the background being',
            '--creation-factor': '=<percent>',
            '--left-only': 'Suppress commits that are missing from the first specified range (or the \"left range\" when using the <rev1>...<rev2> format).',
            '--right-only': 'Suppress commits that are missing from the second specified range (or the \"right range\" when using the <rev1>...<rev2> format).'
        },
        'examples': [
            'git-range-diff  # Compare two commit ranges (e.g. two versions of a '
        ],
        'category': 'Other'
    },
    'git-read-tree': {
        'desc': 'Reads tree information into the index',
        'common_flags': {
            '-m': 'Perform a merge, not just a read. The command will refuse to run if your index file has unmerged entries, indicating that you have not finished',
            '--reset': 'Same as -m, except that unmerged entries are discarded instead of failing. When used with -u, updates leading to loss of working tree changes or',
            '-u': 'After a successful merge, update the files in the work tree with the result of the merge.',
            '-i': 'Usually a merge requires the index file as well as the files in the working tree to be up to date with the current head commit, in order not to',
            '-n': 'Check if the command would error out, without updating the index or the files in the working tree for real.',
            '--dry-run': 'Check if the command would error out, without updating the index or the files in the working tree for real.',
            '-v': 'Show the progress of checking files out.',
            '--trivial': 'Restrict three-way merge by git read-tree to happen only if there is no file-level merging required, instead of resolving merge for trivial',
            '--aggressive': 'Usually a three-way merge by git read-tree resolves the merge for really trivial cases and leaves other cases unresolved in the index, so that',
            '--prefix': '=<prefix>',
            '--index-output': '=<file>',
            '--no-sparse-checkout': 'Disable sparse checkout support even if core.sparseCheckout is true.',
            '--empty': 'Instead of reading tree object(s) into the index, just empty it.',
            '-q': 'Quiet, suppress feedback messages.',
            '--quiet': 'Quiet, suppress feedback messages.'
        },
        'examples': [
            'git-read-tree  # Reads tree information into the index',
            'git-read-tree -v  # Show version',
            'git-read-tree -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-rebase': {
        'desc': 'Reapply commits on top of another base tip',
        'common_flags': {
            '--continue': 'Restart the rebasing process after having resolved a merge conflict.',
            '--skip': 'Restart the rebasing process by skipping the current patch.',
            '--abort': 'Abort the rebase operation and reset HEAD to the original branch. If <branch> was provided when the rebase operation was started, then HEAD will',
            '--quit': 'Abort the rebase operation but HEAD is not reset back to the original branch. The index and working tree are also left unchanged as a result. If',
            '--edit-todo': 'Edit the todo list during an interactive rebase.',
            '--show-current-patch': 'Show the current patch in an interactive rebase or when rebase is stopped because of conflicts. This is the equivalent of git show REBASE_HEAD.'
        },
        'examples': [
            'git-rebase  # Reapply commits on top of another base tip'
        ],
        'category': 'Other'
    },
    'git-receive-pack': {
        'desc': 'Receive what is pushed into the repository',
        'common_flags': {
            '--http-backend-info-refs': 'Used by git-http-backend(1) to serve up $GIT_URL/info/refs?service=git-receive-pack requests. See --http-backend-info-refs in git-upload-'
        },
        'examples': [
            'git-receive-pack  # Receive what is pushed into the repository'
        ],
        'category': 'Other'
    },
    'git-reflog': {
        'desc': 'Manage reflog information',
        'common_flags': {
            '--all': 'Process the reflogs of all references.',
            '--single-worktree': 'By default when --all is specified, reflogs from all working trees are processed. This option limits the processing to reflogs from the current',
            '--expire': '=<time>',
            '--expire-unreachable': '=<time>',
            '--updateref': 'Update the reference to the value of the top reflog entry (i.e. <ref>@{0}) if the previous top entry was pruned. (This option is ignored for',
            '--rewrite': 'If a reflog entry’s predecessor is pruned, adjust its \"old\" SHA-1 to be equal to the \"new\" SHA-1 field of the entry that now precedes it.',
            '--stale-fix': 'Prune any reflog entries that point to \"broken commits\". A broken commit is a commit that is not reachable from any of the reference tips and',
            '-n': 'Do not actually prune any entries; just show what would have been pruned.',
            '--dry-run': 'Do not actually prune any entries; just show what would have been pruned.',
            '--verbose': 'Print extra information on screen.'
        },
        'examples': [
            'git-reflog  # Manage reflog information',
            'git-reflog --verbose  # Verbose output',
            'git-reflog --all  # Show all'
        ],
        'category': 'Other'
    },
    'git-refs': {
        'desc': 'Low-level access to refs',
        'common_flags': {
            '--ref-format': '=<format>',
            '--dry-run': 'Perform the migration, but do not modify the repository. The migrated refs will be written into a separate directory that can be inspected',
            '--strict': 'Enable stricter error checking. This will cause warnings to be reported as errors. See git-fsck(1).',
            '--verbose': 'When verifying the reference database consistency, be chatty.'
        },
        'examples': [
            'git-refs  # Low-level access to refs',
            'git-refs --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-remote': {
        'desc': 'Manage set of tracked repositories',
        'common_flags': {
            '-v': 'Be a little more verbose and show remote url after name. For promisor remotes, also show which filters (blob:none etc.) are configured. NOTE:',
            '--verbose': 'Be a little more verbose and show remote url after name. For promisor remotes, also show which filters (blob:none etc.) are configured. NOTE:'
        },
        'examples': [
            'git-remote  # Manage set of tracked repositories',
            'git-remote -v  # Show version',
            'git-remote -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-repack': {
        'desc': 'Pack unpacked objects in a repository',
        'common_flags': {
            '-a': 'Instead of incrementally packing the unpacked objects, pack everything referenced into a single pack. Especially useful when packing a',
            '--dangling': 'shows as dangling.',
            '-A': 'Same as -a, unless -d is used. Then any unreachable objects in a previous pack become loose, unpacked objects, instead of being left in the old',
            '-d': 'After packing, if the newly created packs make some existing packs redundant, remove the redundant packs. Also run git prune-packed to remove',
            '--cruft': 'Same as -a, unless -d is used. Then any unreachable objects are packed into a separate cruft pack. Unreachable objects can be pruned using the',
            '--cruft-expiration': '=<approxidate>',
            '--max-cruft-size': '=<n>',
            '--expire-to': '=<dir>',
            '-l': 'Pass the --local option to git pack-objects. See git-pack-objects(1).',
            '-f': 'Pass the --no-reuse-delta option to git-pack-objects, see git-pack-objects(1).',
            '-F': 'Pass the --no-reuse-object option to git-pack-objects, see git-pack-objects(1).',
            '-q': 'Show no progress over the standard error stream and pass the -q option to git pack-objects. See git-pack-objects(1).',
            '--quiet': 'Show no progress over the standard error stream and pass the -q option to git pack-objects. See git-pack-objects(1).',
            '-n': 'Do not update the server information with git update-server-info. This option skips updating local catalog files needed to publish this',
            '--window': '=<n>, --depth=<n>'
        },
        'examples': [
            'git-repack  # Pack unpacked objects in a repository',
            'git-repack -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-replace': {
        'desc': 'Create, list, delete refs to replace objects',
        'common_flags': {
            '-f': 'If an existing replace ref for the same object exists, it will be overwritten (instead of failing).',
            '--force': 'If an existing replace ref for the same object exists, it will be overwritten (instead of failing).',
            '-d': 'Delete existing replace refs for the given objects.',
            '--delete': 'Delete existing replace refs for the given objects.',
            '--edit': '<object>',
            '--raw': 'When editing, provide the raw object contents rather than pretty-printed ones. Currently this only affects trees, which will be shown in their',
            '--graft': '<commit> [<parent>...]',
            '--convert-graft-file': 'Creates graft commits for all entries in $GIT_DIR/info/grafts and deletes that file upon success. The purpose is to help users with',
            '-l': '<pattern>, --list <pattern>',
            '--format': '=<format>'
        },
        'examples': [
            'git-replace  # Create, list, delete refs to replace objects'
        ],
        'category': 'Other'
    },
    'git-replay': {
        'desc': 'EXPERIMENTAL: Replay commits on a new base, works with bare repos too',
        'common_flags': {
            '--onto': '<newbase>',
            '--advance': '<branch>',
            '--grep': '=<pattern>, commits whose message matches any of the given patterns are chosen (but see --all-match).',
            '--skip': '=<number>',
            '--since': '=<date>, --after=<date>',
            '--since-as-filter': '=<date>',
            '--until': '=<date>, --before=<date>',
            '--author': '=<pattern>, commits whose author matches any of the given patterns are chosen (similarly for multiple --committer=<pattern>).',
            '--grep-reflog': '=<pattern>',
            '--all-match': 'Limit the commits output to ones that match all given --grep, instead of ones that match at least one.',
            '--invert-grep': 'Limit the commits output to ones with a log message that do not match the pattern specified with --grep=<pattern>.',
            '-i': 'Match the regular expression limiting patterns without regard to letter case.',
            '--regexp-ignore-case': 'Match the regular expression limiting patterns without regard to letter case.',
            '--basic-regexp': 'Consider the limiting patterns to be basic regular expressions; this is the default.',
            '-E': 'Consider the limiting patterns to be extended regular expressions instead of the default basic regular expressions.'
        },
        'examples': [
            'git-replay  # EXPERIMENTAL: Replay commits on a new base, works '
        ],
        'category': 'Other'
    },
    'git-request-pull': {
        'desc': 'Generates a summary of pending changes',
        'common_flags': {
            '-p': 'Include patch text in the output.'
        },
        'examples': [
            'git-request-pull  # Generates a summary of pending changes'
        ],
        'category': 'Other'
    },
    'git-reset': {
        'desc': 'Reset current HEAD to the specified state',
        'common_flags': {
            '-q': 'Be quiet, only report errors.',
            '--quiet': 'Be quiet, only report errors.',
            '--refresh': 'Refresh the index after a mixed reset. Enabled by default.',
            '--no-refresh': 'Refresh the index after a mixed reset. Enabled by default.',
            '--pathspec-from-file': '=<file>',
            '--pathspec-file-nul': 'Only meaningful with --pathspec-from-file. Pathspec elements are separated with NUL character and all other characters are taken literally'
        },
        'examples': [
            'git-reset  # Reset current HEAD to the specified state'
        ],
        'category': 'Other'
    },
    'git-restore': {
        'desc': 'Restore working tree files',
        'common_flags': {
            '-s': '<tree>, --source=<tree>',
            '-p': 'Interactively select hunks in the difference between the restore source and the restore location. See the “Interactive Mode” section of git-',
            '--patch': 'Interactively select hunks in the difference between the restore source and the restore location. See the “Interactive Mode” section of git-',
            '-W': 'Specify the restore location. If neither option is specified, by default the working tree is restored. Specifying --staged will only restore the',
            '--worktree': 'Specify the restore location. If neither option is specified, by default the working tree is restored. Specifying --staged will only restore the',
            '-S': 'Specify the restore location. If neither option is specified, by default the working tree is restored. Specifying --staged will only restore the',
            '--staged': 'Specify the restore location. If neither option is specified, by default the working tree is restored. Specifying --staged will only restore the',
            '-q': 'Quiet, suppress feedback messages. Implies --no-progress.',
            '--quiet': 'Quiet, suppress feedback messages. Implies --no-progress.',
            '--progress': 'Progress status is reported on the standard error stream by default when it is attached to a terminal, unless --quiet is specified. This flag',
            '--no-progress': 'Progress status is reported on the standard error stream by default when it is attached to a terminal, unless --quiet is specified. This flag',
            '--ours': 'When restoring files in the working tree from the index, use stage #2 (ours) or #3 (theirs) for unmerged paths. This option cannot be used when',
            '--theirs': 'When restoring files in the working tree from the index, use stage #2 (ours) or #3 (theirs) for unmerged paths. This option cannot be used when',
            '-m': 'When restoring files on the working tree from the index, recreate the conflicted merge in the unmerged paths. This option cannot be used when',
            '--merge': 'When restoring files on the working tree from the index, recreate the conflicted merge in the unmerged paths. This option cannot be used when'
        },
        'examples': [
            'git-restore  # Restore working tree files'
        ],
        'category': 'Other'
    },
    'git-rev-list': {
        'desc': 'Lists commit objects in reverse chronological order',
        'common_flags': {
            '--grep': '=<pattern>, commits whose message matches any of the given patterns are chosen (but see --all-match).',
            '--skip': '=<number>',
            '--since': '=<date>, --after=<date>',
            '--since-as-filter': '=<date>',
            '--until': '=<date>, --before=<date>',
            '--max-age': '=<timestamp>, --min-age=<timestamp>',
            '--author': '=<pattern>, commits whose author matches any of the given patterns are chosen (similarly for multiple --committer=<pattern>).',
            '--grep-reflog': '=<pattern>',
            '--all-match': 'Limit the commits output to ones that match all given --grep, instead of ones that match at least one.',
            '--invert-grep': 'Limit the commits output to ones with a log message that do not match the pattern specified with --grep=<pattern>.',
            '-i': 'Match the regular expression limiting patterns without regard to letter case.',
            '--regexp-ignore-case': 'Match the regular expression limiting patterns without regard to letter case.',
            '--basic-regexp': 'Consider the limiting patterns to be basic regular expressions; this is the default.',
            '-E': 'Consider the limiting patterns to be extended regular expressions instead of the default basic regular expressions.',
            '--extended-regexp': 'Consider the limiting patterns to be extended regular expressions instead of the default basic regular expressions.'
        },
        'examples': [
            'git-rev-list  # Lists commit objects in reverse chronological orde'
        ],
        'category': 'Other'
    },
    'git-rev-parse': {
        'desc': 'Pick out and massage parameters',
        'common_flags': {
            '--parseopt': 'Use git rev-parse in option parsing mode (see PARSEOPT section below). The command in this mode can be used outside a repository or a working',
            '--sq-quote': 'Use git rev-parse in shell quoting mode (see SQ-QUOTE section below). In contrast to the --sq option below, this mode only does quoting. Nothing',
            '--keep-dashdash': 'Only meaningful in --parseopt mode. Tells the option parser to echo out the first -- met instead of skipping it.',
            '--stop-at-non-option': 'Only meaningful in --parseopt mode. Lets the option parser stop at the first non-option argument. This can be used to parse sub-commands that',
            '--stuck-long': 'Only meaningful in --parseopt mode. Output the options in their long form if available, and with their arguments stuck.',
            '--revs-only': 'Do not output flags and parameters not meant for git rev-list command.',
            '--no-revs': 'Do not output flags and parameters meant for git rev-list command.',
            '--flags': 'Do not output non-flag parameters.',
            '--no-flags': 'Do not output flag parameters.',
            '--default': '<arg>',
            '--prefix': '<arg>',
            '--verify': 'Verify that exactly one parameter is provided, and that it can be turned into a raw 20-byte SHA-1 that can be used to access the object',
            '-q': 'Only meaningful in --verify mode. Do not output an error message if the first argument is not a valid object name; instead exit with non-zero',
            '--quiet': 'Only meaningful in --verify mode. Do not output an error message if the first argument is not a valid object name; instead exit with non-zero',
            '--sq': 'Usually the output is made one line per flag and parameter. This option makes output a single line, properly quoted for consumption by shell.'
        },
        'examples': [
            'git-rev-parse  # Pick out and massage parameters'
        ],
        'category': 'Other'
    },
    'git-revert': {
        'desc': 'Revert some existing commits',
        'common_flags': {
            '-e': 'With this option, git revert will let you edit the commit message prior to committing the revert. This is the default if you run the command',
            '--edit': 'With this option, git revert will let you edit the commit message prior to committing the revert. This is the default if you run the command',
            '-m': 'parent-number, --mainline parent-number',
            '--no-edit': 'With this option, git revert will not start the commit message editor.',
            '--cleanup': '=<mode>',
            '-n': 'Usually the command automatically creates some commits with commit log messages stating which commits were reverted. This flag applies the',
            '--no-commit': 'Usually the command automatically creates some commits with commit log messages stating which commits were reverted. This flag applies the',
            '-S': '[<keyid>], --gpg-sign[=<keyid>], --no-gpg-sign',
            '-s': 'Add a Signed-off-by trailer at the end of the commit message. See the signoff option in git-commit(1) for more information.',
            '--signoff': 'Add a Signed-off-by trailer at the end of the commit message. See the signoff option in git-commit(1) for more information.',
            '--strategy': '=<strategy>',
            '-X': '<option>, --strategy-option=<option>',
            '--rerere-autoupdate': 'After the rerere mechanism reuses a recorded resolution on the current conflict to update the files in the working tree, allow it to also update',
            '--no-rerere-autoupdate': 'After the rerere mechanism reuses a recorded resolution on the current conflict to update the files in the working tree, allow it to also update',
            '--reference': 'Instead of starting the body of the log message with \"This reverts <full-object-name-of-the-commit-being-reverted>.\", refer to the commit using'
        },
        'examples': [
            'git-revert  # Revert some existing commits'
        ],
        'category': 'Other'
    },
    'git-rm': {
        'desc': 'Remove files from the working tree and from the index',
        'common_flags': {
            '-f': 'Override the up-to-date check.',
            '--force': 'Override the up-to-date check.',
            '-n': 'Don’t actually remove any file(s). Instead, just show if they exist in the index and would otherwise be removed by the command.',
            '--dry-run': 'Don’t actually remove any file(s). Instead, just show if they exist in the index and would otherwise be removed by the command.',
            '-r': 'Allow recursive removal when a leading directory name is given.',
            '--cached': 'Use this option to unstage and remove paths only from the index. Working tree files, whether modified or not, will be left alone.',
            '--ignore-unmatch': 'Exit with a zero status even if no files matched.',
            '--sparse': 'Allow updating index entries outside of the sparse-checkout cone. Normally, git rm refuses to update index entries whose paths do not fit within',
            '-q': 'git rm normally outputs one line (in the form of an rm command) for each file removed. This option suppresses that output.',
            '--quiet': 'git rm normally outputs one line (in the form of an rm command) for each file removed. This option suppresses that output.',
            '--pathspec-from-file': '=<file>',
            '--pathspec-file-nul': 'Only meaningful with --pathspec-from-file. Pathspec elements are separated with NUL character and all other characters are taken literally'
        },
        'examples': [
            'git-rm  # Remove files from the working tree and from the in',
            'git-rm -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'git-send-pack': {
        'desc': 'Push objects over Git protocol to another repository',
        'common_flags': {
            '--receive-pack': '=<git-receive-pack>',
            '--exec': '=<git-receive-pack>',
            '--all': 'Instead of explicitly specifying which refs to update, update all heads that locally exist.',
            '--stdin': 'Take the list of refs from stdin, one per line. If there are refs specified on the command line in addition to this option, then the refs from',
            '--dry-run': 'Do everything except actually send the updates.',
            '--force': 'Usually, the command refuses to update a remote ref that is not an ancestor of the local ref used to overwrite it. This flag disables the check.',
            '--verbose': 'Run verbosely.',
            '--thin': 'Send a \"thin\" pack, which records objects in deltified form based on objects not included in the pack to reduce network traffic.',
            '--atomic': 'Use an atomic transaction for updating the refs. If any of the refs fails to update then the entire push will fail without changing any refs.',
            '--no-signed': ', no signing will be attempted. If true or --signed, the push will fail if the server does not support signed pushes. If set to',
            '--push-option': '=<string>'
        },
        'examples': [
            'git-send-pack  # Push objects over Git protocol to another reposito',
            'git-send-pack --verbose  # Verbose output',
            'git-send-pack --all  # Show all'
        ],
        'category': 'Other'
    },
    'git-shortlog': {
        'desc': 'Summarize \'git log\' output',
        'common_flags': {
            '-n': 'Sort output according to the number of commits per author instead of author alphabetic order.',
            '--numbered': 'Sort output according to the number of commits per author instead of author alphabetic order.',
            '-s': 'Suppress commit description and provide a commit count summary only.',
            '--summary': 'Suppress commit description and provide a commit count summary only.',
            '-e': 'Show the email address of each author.',
            '--email': 'Show the email address of each author.',
            '--format': '[=<format>]',
            '--date': '=<format>',
            '--group': '=<type>',
            '-c': 'This is an alias for --group=committer.',
            '--committer': 'This is an alias for --group=committer.',
            '-w': '[<width>[,<indent1>[,<indent2>]]]',
            '--grep': '=<pattern> further limits to commits whose log message has a line that matches <pattern>), unless otherwise noted.',
            '--skip': '=<number>',
            '--since': '=<date>, --after=<date>'
        },
        'examples': [
            'git-shortlog  # Summarize \'git log\' output'
        ],
        'category': 'Other'
    },
    'git-show': {
        'desc': 'Show various types of objects',
        'common_flags': {
            '--pretty': '=tformat:<format> were given.',
            '--abbrev-commit': 'Instead of showing the full 40-byte hexadecimal commit object name, show a prefix that names the object uniquely. \"--abbrev=<n>\" (which also',
            '--no-abbrev-commit': 'Show the full 40-byte hexadecimal commit object name. This negates --abbrev-commit, either explicit or implied by other options such as',
            '--oneline': 'This is a shorthand for \"--pretty=oneline --abbrev-commit\" used together.',
            '--encoding': '=<encoding>',
            '--expand-tabs': '=<n>, --expand-tabs, --no-expand-tabs',
            '--notes': '[=<ref>]',
            '--no-notes': 'Do not show notes. This negates the above --notes option, by resetting the list of notes refs from which notes are shown. Options are parsed in',
            '--show-notes-by-default': 'Show the default notes unless options for displaying specific notes are given.',
            '--show-notes': '[=<ref>], --[no-]standard-notes',
            '--show-signature': 'Check the validity of a signed commit object by passing the signature to gpg --verify and show the output.'
        },
        'examples': [
            'git-show  # Show various types of objects'
        ],
        'category': 'Other'
    },
    'git-show-branch': {
        'desc': 'Show branches and their commits',
        'common_flags': {
            '-r': 'Show the remote-tracking branches.',
            '--remotes': 'Show the remote-tracking branches.',
            '-a': 'Show both remote-tracking branches and local branches.',
            '--all': 'Show both remote-tracking branches and local branches.',
            '--current': 'With this option, the command includes the current branch in the list of revs to be shown when it is not given on the command line.',
            '--topo-order': 'By default, the branches and their commits are shown in reverse chronological order. This option makes them appear in topological order (i.e.,',
            '--date-order': 'This option is similar to --topo-order in the sense that no parent comes before all of its children, but otherwise commits are ordered according',
            '--sparse': 'By default, the output omits merges that are reachable from only one tip being shown. This option makes them visible.',
            '--more': '=<n>',
            '--list': 'Synonym to --more=-1',
            '--merge-base': 'Instead of showing the commit list, determine possible merge bases for the specified commits. All merge bases will be contained in all specified',
            '--independent': 'Among the <ref>s given, display only the ones that cannot be reached from any other <ref>.',
            '--no-name': 'Do not show naming strings for each commit.',
            '--sha1-name': 'Instead of naming the commits using the path to reach them from heads (e.g. \"master~2\" to mean the grandparent of \"master\"), name them with the',
            '--topics': 'Shows only commits that are NOT on the first branch given. This helps track topic branches by hiding any commit that is already in the main line'
        },
        'examples': [
            'git-show-branch  # Show branches and their commits',
            'git-show-branch -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-show-index': {
        'desc': 'Show packed archive index',
        'common_flags': {
            '--object-format': '=<hash-algorithm>'
        },
        'examples': [
            'git-show-index  # Show packed archive index'
        ],
        'category': 'Other'
    },
    'git-show-ref': {
        'desc': 'List references in a local repository',
        'common_flags': {
            '--head': 'Show the HEAD reference, even if it would normally be filtered out.',
            '--branches': 'Limit to local branches and local tags, respectively. These options are not mutually exclusive; when given both, references stored in',
            '--tags': 'Limit to local branches and local tags, respectively. These options are not mutually exclusive; when given both, references stored in',
            '-d': 'Dereference tags into object IDs as well. They will be shown with ^{} appended.',
            '--dereference': 'Dereference tags into object IDs as well. They will be shown with ^{} appended.',
            '-s': '[=<n>]',
            '--hash': '[=<n>]',
            '--verify': 'Enable stricter reference checking by requiring an exact ref path. Aside from returning an error code of 1, it will also print an error message',
            '--exists': 'Check whether the given reference exists. Returns an exit code of 0 if it does, 2 if it is missing, and 1 in case looking up the reference',
            '--abbrev': '[=<n>]',
            '-q': 'Do not print any results to stdout. Can be used with --verify to silently check if a reference exists.',
            '--quiet': 'Do not print any results to stdout. Can be used with --verify to silently check if a reference exists.',
            '--exclude-existing': '[=<pattern>]'
        },
        'examples': [
            'git-show-ref  # List references in a local repository'
        ],
        'category': 'Other'
    },
    'git-status': {
        'desc': 'Show the working tree status',
        'common_flags': {
            '-s': 'Give the output in the short-format.',
            '--short': 'Give the output in the short-format.',
            '-b': 'Show the branch and tracking info even in short-format.',
            '--branch': 'Show the branch and tracking info even in short-format.',
            '--show-stash': 'Show the number of entries currently stashed away.',
            '--porcelain': '[=<version>]',
            '--long': 'Give the output in the long-format. This is the default.',
            '-v': 'In addition to the names of files that have been changed, also show the textual changes that are staged to be committed (i.e., like the output',
            '--verbose': 'In addition to the names of files that have been changed, also show the textual changes that are staged to be committed (i.e., like the output',
            '-u': '[<mode>], --untracked-files[=<mode>]',
            '--split-index': '), Otherwise you can use no to have git status return more quickly without showing untracked files. All usual spellings for Boolean',
            '--ignore-submodules': '[=<when>]',
            '--ignored': '[=<mode>]',
            '-z': 'Terminate entries with NUL, instead of LF. This implies the --porcelain=v1 output format if no other format is given.',
            '--column': '[=<options>], --no-column'
        },
        'examples': [
            'git-status  # Show the working tree status',
            'git-status -v  # Show version',
            'git-status -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-stripspace': {
        'desc': 'Remove unnecessary whitespace',
        'common_flags': {
            '-s': 'Skip and remove all lines starting with a comment character (default #).',
            '--strip-comments': 'Skip and remove all lines starting with a comment character (default #).',
            '-c': 'Prepend the comment character and a blank space to each line. Lines will automatically be terminated with a newline. On empty lines, only the',
            '--comment-lines': 'Prepend the comment character and a blank space to each line. Lines will automatically be terminated with a newline. On empty lines, only the'
        },
        'examples': [
            'git-stripspace  # Remove unnecessary whitespace'
        ],
        'category': 'Other'
    },
    'git-switch': {
        'desc': 'Switch branches',
        'common_flags': {
            '-c': '<new-branch>, --create <new-branch>',
            '-C': '<new-branch>, --force-create <new-branch>',
            '-d': 'Switch to a commit for inspection and discardable experiments. See the \"DETACHED HEAD\" section in git-checkout(1) for details.',
            '--detach': 'Switch to a commit for inspection and discardable experiments. See the \"DETACHED HEAD\" section in git-checkout(1) for details.',
            '--guess': 'is the default behavior. Use --no-guess to disable it.',
            '--no-guess': 'If <branch> is not found but there does exist a tracking branch in exactly one remote (call it <remote>) with a matching name, treat as',
            '-f': 'An alias for --discard-changes.',
            '--force': 'An alias for --discard-changes.',
            '--discard-changes': 'Proceed even if the index or the working tree differs from HEAD. Both the index and working tree are restored to match the switching target. If',
            '--recurse-submodules': 'is specified, submodule content is also restored to match the switching target. This is used to throw away local changes.',
            '-m': 'If you have local modifications to one or more files that are different between the current branch and the branch to which you are switching,',
            '--merge': 'If you have local modifications to one or more files that are different between the current branch and the branch to which you are switching,',
            '--conflict': '=<style>',
            '-q': 'Quiet, suppress feedback messages.',
            '--quiet': 'Quiet, suppress feedback messages.'
        },
        'examples': [
            'git-switch  # Switch branches'
        ],
        'category': 'Other'
    },
    'git-symbolic-ref': {
        'desc': 'Read, modify and delete symbolic refs',
        'common_flags': {
            '-d': 'Delete the symbolic ref <name>.',
            '--delete': 'Delete the symbolic ref <name>.',
            '-q': 'Do not issue an error message if the <name> is not a symbolic ref but a detached HEAD; instead exit with non-zero status silently.',
            '--quiet': 'Do not issue an error message if the <name> is not a symbolic ref but a detached HEAD; instead exit with non-zero status silently.',
            '--short': 'When showing the value of <name> as a symbolic ref, try to shorten the value, e.g. from refs/heads/master to master.',
            '--recurse': 'When showing the value of <name> as a symbolic ref, if <name> refers to another symbolic ref, follow such a chain of symbolic refs until the',
            '--no-recurse': 'When showing the value of <name> as a symbolic ref, if <name> refers to another symbolic ref, follow such a chain of symbolic refs until the',
            '-m': 'Update the reflog for <name> with <reason>. This is valid only when creating or updating a symbolic ref.'
        },
        'examples': [
            'git-symbolic-ref  # Read, modify and delete symbolic refs'
        ],
        'category': 'Other'
    },
    'git-tag': {
        'desc': 'Create, list, delete or verify a tag object signed with GPG',
        'common_flags': {
            '-a': 'Make an unsigned, annotated tag object',
            '--annotate': 'Make an unsigned, annotated tag object',
            '-s': 'Make a GPG-signed tag, using the default e-mail address’s key. The default behavior of tag GPG-signing is controlled by tag.gpgSign',
            '--sign': 'Make a GPG-signed tag, using the default e-mail address’s key. The default behavior of tag GPG-signing is controlled by tag.gpgSign',
            '--no-sign': 'Override tag.gpgSign configuration variable that is set to force each and every tag to be signed.',
            '-u': '<key-id>, --local-user=<key-id>',
            '-f': 'Replace an existing tag with the given name (instead of failing)',
            '--force': 'Replace an existing tag with the given name (instead of failing)',
            '-d': 'Delete existing tags with the given names.',
            '--delete': 'Delete existing tags with the given names.',
            '-v': 'Verify the GPG signature of the given tag names.',
            '--verify': 'Verify the GPG signature of the given tag names.',
            '-n': '<num>',
            '-l': 'List tags. With optional <pattern>..., e.g. git tag --list \'v-*\', list only the tags that match the pattern(s).',
            '--list': 'List tags. With optional <pattern>..., e.g. git tag --list \'v-*\', list only the tags that match the pattern(s).'
        },
        'examples': [
            'git-tag  # Create, list, delete or verify a tag object signed',
            'git-tag -v  # Show version',
            'git-tag -v  # Verbose output',
            'git-tag -a  # Show all'
        ],
        'category': 'Other'
    },
    'git-unpack-objects': {
        'desc': 'Unpack objects from a packed archive',
        'common_flags': {
            '-n': 'Dry run. Check the pack file without actually unpacking the objects.',
            '-q': 'The command usually shows percentage progress. This flag suppresses it.',
            '-r': 'When unpacking a corrupt packfile, the command dies at the first corruption. This flag tells it to keep going and make the best effort to',
            '--strict': 'Don’t write objects with broken content or links.',
            '--max-input-size': '=<size>'
        },
        'examples': [
            'git-unpack-objects  # Unpack objects from a packed archive'
        ],
        'category': 'Other'
    },
    'git-update-index': {
        'desc': 'Register file contents in the working tree to the index',
        'common_flags': {
            '--add': 'If a specified file isn’t in the index already then it’s added. Default behaviour is to ignore new files.',
            '--remove': 'If a specified file is in the index but is missing then it’s removed. Default behavior is to ignore removed files.',
            '--refresh': 'Looks at the current index and checks to see if merges or updates are needed by checking stat() information.',
            '-q': 'Quiet. If --refresh finds that the index needs an update, the default behavior is to error out. This option makes git update-index continue',
            '--ignore-submodules': 'Do not try to update submodules. This option is only respected when passed before --refresh.',
            '--unmerged': 'If --refresh finds unmerged changes in the index, the default behavior is to error out. This option makes git update-index continue anyway.',
            '--ignore-missing': 'Ignores missing files during a --refresh',
            '--cacheinfo': '<mode>,<object>,<path>, --cacheinfo <mode> <object> <path>',
            '--index-info': 'Read index information from stdin.',
            '--chmod': '=(+|-)x',
            '--really-refresh': 'Like --refresh, but checks stat information unconditionally, without regard to the \"assume unchanged\" setting.',
            '-g': 'Runs git update-index itself on the paths whose index entries are different from those of the HEAD commit.',
            '--again': 'Runs git update-index itself on the paths whose index entries are different from those of the HEAD commit.',
            '--unresolve': 'Restores the unmerged or needs updating state of a file during a merge if it was cleared by accident.',
            '--info-only': 'Do not create objects in the object database for all <file> arguments that follow this flag; just insert their object IDs into the index.'
        },
        'examples': [
            'git-update-index  # Register file contents in the working tree to the '
        ],
        'category': 'Other'
    },
    'git-update-server-info': {
        'desc': 'Update auxiliary info file to help dumb servers',
        'common_flags': {
            '-f': 'Update the info files from scratch.',
            '--force': 'Update the info files from scratch.'
        },
        'examples': [
            'git-update-server-info  # Update auxiliary info file to help dumb servers'
        ],
        'category': 'Other'
    },
    'git-upload-pack': {
        'desc': 'Send objects packed back to git-fetch-pack',
        'common_flags': {
            '--timeout': '=<n>',
            '--stateless-rpc': 'Perform only a single read-write cycle with stdin and stdout. This fits with the HTTP POST request processing model where a program may read the',
            '--http-backend-info-refs': 'Used by git-http-backend(1) to serve up $GIT_URL/info/refs?service=git-upload-pack requests. See \"Smart Clients\" in gitprotocol-http(5) and'
        },
        'examples': [
            'git-upload-pack  # Send objects packed back to git-fetch-pack'
        ],
        'category': 'Other'
    },
    'git-var': {
        'desc': 'Show a Git logical variable',
        'common_flags': {
            '-l': 'Display the logical variables. In addition, all the variables of the Git configuration file .git/config are listed as well. (However, the'
        },
        'examples': [
            'git-var  # Show a Git logical variable'
        ],
        'category': 'Other'
    },
    'git-verify-commit': {
        'desc': 'Check the GPG signature of commits',
        'common_flags': {
            '--raw': 'Print the raw gpg status output to standard error instead of the normal human-readable output.',
            '-v': 'Print the contents of the commit object before validating it.',
            '--verbose': 'Print the contents of the commit object before validating it.'
        },
        'examples': [
            'git-verify-commit  # Check the GPG signature of commits',
            'git-verify-commit -v  # Show version',
            'git-verify-commit -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-verify-pack': {
        'desc': 'Validate packed Git archive files',
        'common_flags': {
            '-v': 'After verifying the pack, show the list of objects contained in the pack and a histogram of delta chain length.',
            '--verbose': 'After verifying the pack, show the list of objects contained in the pack and a histogram of delta chain length.',
            '-s': 'Do not verify the pack contents; only show the histogram of delta chain length. With --verbose, the list of objects is also shown.',
            '--stat-only': 'Do not verify the pack contents; only show the histogram of delta chain length. With --verbose, the list of objects is also shown.'
        },
        'examples': [
            'git-verify-pack  # Validate packed Git archive files',
            'git-verify-pack -v  # Show version',
            'git-verify-pack -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-verify-tag': {
        'desc': 'Check the GPG signature of tags',
        'common_flags': {
            '--raw': 'Print the raw gpg status output to standard error instead of the normal human-readable output.',
            '-v': 'Print the contents of the tag object before validating it.',
            '--verbose': 'Print the contents of the tag object before validating it.'
        },
        'examples': [
            'git-verify-tag  # Check the GPG signature of tags',
            'git-verify-tag -v  # Show version',
            'git-verify-tag -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-version': {
        'desc': 'Display version information about Git',
        'common_flags': {
            '--build-options': 'Include additional information about how git was built for diagnostic purposes.'
        },
        'examples': [
            'git-version  # Display version information about Git'
        ],
        'category': 'Other'
    },
    'git-web--browse': {
        'desc': 'Git helper script to launch a web browser',
        'common_flags': {
            '-b': '<browser>, --browser=<browser>',
            '-t': '<browser>, --tool=<browser>',
            '-c': '<conf.var>, --config=<conf.var>'
        },
        'examples': [
            'git-web--browse  # Git helper script to launch a web browser'
        ],
        'category': 'Other'
    },
    'git-worktree': {
        'desc': 'Manage multiple working trees',
        'common_flags': {
            '-f': 'By default, add refuses to create a new worktree when <commit-ish> is a branch name and is already checked out by another worktree, or if <path>',
            '--force': 'By default, add refuses to create a new worktree when <commit-ish> is a branch name and is already checked out by another worktree, or if <path>',
            '-b': '<new-branch>, -B <new-branch>',
            '-d': 'With add, detach HEAD in the new worktree. See \"DETACHED HEAD\" in git-checkout(1).',
            '--detach': 'With add, detach HEAD in the new worktree. See \"DETACHED HEAD\" in git-checkout(1).',
            '--lock': 'Keep the worktree locked after creation. This is the equivalent of git worktree lock after git worktree add, but without a race condition.',
            '-n': 'With prune, do not remove anything; just report what it would remove.',
            '--dry-run': 'With prune, do not remove anything; just report what it would remove.',
            '--orphan': 'With add, make the new worktree and index empty, associating the worktree with a new unborn branch named <new-branch>.',
            '--porcelain': 'With list, output in an easy-to-parse format for scripts. This format will remain stable across Git versions and regardless of user',
            '-z': 'Terminate each line with a NUL rather than a newline when --porcelain is specified with list. This makes it possible to parse the output when a',
            '-q': 'With add, suppress feedback messages.',
            '--quiet': 'With add, suppress feedback messages.',
            '-v': 'With prune, report all removals.',
            '--verbose': 'With prune, report all removals.'
        },
        'examples': [
            'git-worktree  # Manage multiple working trees',
            'git-worktree -v  # Show version',
            'git-worktree -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'git-write-tree': {
        'desc': 'Create a tree object from the current index',
        'common_flags': {
            '--missing-ok': 'Normally git write-tree ensures that the objects referenced by the directory exist in the object database. This option disables this check.',
            '--prefix': '=<prefix>/'
        },
        'examples': [
            'git-write-tree  # Create a tree object from the current index'
        ],
        'category': 'Other'
    },
    'gmake': {
        'desc': 'GNU Make utility to maintain groups of programs',
        'common_flags': {
            '-b': 'These options are ignored for compatibility with other versions of make.',
            '-m': 'These options are ignored for compatibility with other versions of make.',
            '-B': 'Unconditionally make all targets.',
            '--always-make': 'Unconditionally make all targets.',
            '-C': 'dir, --directory=dir',
            '-d': 'Print debugging information in addition to normal processing. The debugging information says which files are being considered for remaking,',
            '--debug': '[=FLAGS]',
            '-e': 'Give variables taken from the environment precedence over variables from makefiles.',
            '--environment-overrides': 'Give variables taken from the environment precedence over variables from makefiles.',
            '-E': 'string, --eval string',
            '-f': 'file, --file=file, --makefile=FILE',
            '-i': 'Ignore all errors in commands executed to remake files.',
            '--ignore-errors': 'Ignore all errors in commands executed to remake files.',
            '-I': 'dir, --include-dir=dir',
            '-j': '[jobs], --jobs[=jobs]'
        },
        'examples': [
            'gmake  # GNU Make utility to maintain groups of programs'
        ],
        'category': 'Other'
    },
    'goid-tool': {
        'desc': 'smart card utility for GoID fingerprint card',
        'common_flags': {
            '--help': 'Print help message on screen.',
            '-h': 'Print help message on screen.',
            '--version': 'Print the OpenSC package release version.',
            '-V': 'Print the OpenSC package release version.',
            '--reader': 'string, -r string',
            '--verbose': 'Cause goid-tool to be more verbose. Use it multiple times to be even more verbose.',
            '-v': 'Cause goid-tool to be more verbose. Use it multiple times to be even more verbose.',
            '--verify-pin': 'Verify PIN.',
            '-p': 'Verify PIN.',
            '--verify-bio': 'Verify finger print.',
            '-b': 'Verify finger print.',
            '--verify-pin-or-bio': 'Verify PIN or finger print (user\'s choice).'
        },
        'examples': [
            'goid-tool  # smart card utility for GoID fingerprint card',
            'goid-tool -h  # Show help',
            'goid-tool -v  # Show version',
            'goid-tool -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'gpasswd': {
        'desc': 'administer /etc/group and /etc/gshadow',
        'common_flags': {
            '-a': 'user',
            '--add': 'user',
            '-d': 'user',
            '--delete': 'user',
            '-h': 'Display help message and exit.',
            '--help': 'Display help message and exit.',
            '-Q': 'CHROOT_DIR',
            '--root': 'CHROOT_DIR',
            '-r': 'Remove the password from the named group. The group password will be empty. Only group members will be allowed to use newgrp to join the named',
            '--remove-password': 'Remove the password from the named group. The group password will be empty. Only group members will be allowed to use newgrp to join the named',
            '-R': 'Restrict the access to the named group. The group password is set to \"!\". Only group members with a password will be allowed to use newgrp to',
            '--restrict': 'Restrict the access to the named group. The group password is set to \"!\". Only group members with a password will be allowed to use newgrp to',
            '-A': 'user,...',
            '--administrators': 'user,...',
            '-M': 'user,...'
        },
        'examples': [
            'gpasswd  # administer /etc/group and /etc/gshadow',
            'gpasswd -h  # Show help',
            'gpasswd -a  # Show all'
        ],
        'category': 'Other'
    },
    'gpic': {
        'desc': 'compile pictures for troff or TeX',
        'common_flags': {
            '--help': 'displays a usage message, while -v and --version show version information; all exit afterward.',
            '-c': 'Be more compatible with tpic; implies -t. Lines beginning with \\ are not passed through transparently. Lines beginning with . are passed',
            '-C': 'Recognize .PS, .PE, .PF, and .PY even when followed by a character other than space or newline.',
            '-n': 'Don\'t use groff extensions to the troff drawing commands. Specify this option if a postprocessor you\'re using doesn\'t support these exten‐',
            '-S': 'Operate in safer mode; sh commands are ignored. This mode, enabled by default, can be useful when operating on untrustworthy input.',
            '-t': 'Produce TeX output.',
            '-U': 'Operate in unsafe mode; sh commands are interpreted.',
            '-z': 'In TeX mode, draw dots using zero-length lines.',
            '-D': 'Draw all lines using the \\D escape sequence. GNU pic always does this.',
            '-T': 'dev Generate output for the troff device dev. This is unnecessary because the troff output generated by GNU pic is device-independent.'
        },
        'examples': [
            'gpic  # compile pictures for troff or TeX',
            'gpic --help  # Show help'
        ],
        'category': 'Other'
    },
    'gprofng': {
        'desc': 'The next generation GNU application profiling tool',
        'common_flags': {
            '--version': 'Print the version number and exit.',
            '--help': 'Print usage information and exit.'
        },
        'examples': [
            'gprofng  # The next generation GNU application profiling tool',
            'gprofng --help  # Show help',
            'gprofng --version  # Show version'
        ],
        'category': 'Other'
    },
    'gprofng-archive': {
        'desc': 'Archive gprofng experiment data',
        'common_flags': {
            '--version': 'Print the version number and exit.',
            '--help': 'Print usage information and exit.',
            '-a': '{off | on | ldobjects | src | usedldobjects | used[src]}',
            '-d': 'path',
            '-F': 'Force writing, or rewriting of .archive files. All archived files will be removed and recreated, except if the -n or -m option is used, or if',
            '-m': 'regex',
            '-n': 'Archive the named experiment only, not any of its descendants.',
            '-q': 'Do not write any warnings to stderr. Warnings are incorporated into the .archive file in the experiment directory. They are shown in the',
            '-r': 'path',
            '-s': 'selection'
        },
        'examples': [
            'gprofng-archive  # Archive gprofng experiment data',
            'gprofng-archive --help  # Show help',
            'gprofng-archive --version  # Show version',
            'gprofng-archive -a  # Show all'
        ],
        'category': 'Other'
    },
    'gprofng-display-html': {
        'desc': 'Generate an HTML based directory structure to browse the profiles',
        'common_flags': {
            '--version': 'Print the version number and exit.',
            '--help': 'Print usage information and exit.',
            '--verbose': 'Enable verbose mode to show diagnostic messages about the processing of the data. By default verbose mode is disabled.',
            '-d': '[db-vol-size], --debug[=db-vol-size]',
            '--highlight-percentage': '=value',
            '-o': 'dirname, --output=dirname',
            '-O': 'dirname, --overwrite=dirname',
            '-q': 'Disable the display of all warning, debug, verbose and any other messages. If enabled, the settings for verbose and debug are accepted, but',
            '--quiet': 'Disable the display of all warning, debug, verbose and any other messages. If enabled, the settings for verbose and debug are accepted, but',
            '--nowarnings': 'Disable the printing of warning messages on stdout. By default warning messages are printed.'
        },
        'examples': [
            'gprofng-display-html  # Generate an HTML based directory structure to brow',
            'gprofng-display-html --help  # Show help',
            'gprofng-display-html --version  # Show version',
            'gprofng-display-html --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'gprofng-display-src': {
        'desc': 'Display source code and optionally disassembly of the target object',
        'common_flags': {
            '--version': 'Print the version number and exit.',
            '--help': 'Print usage information and exit.',
            '-f': 'unctions',
            '-s': 'ource item tag',
            '-d': 'isasm item tag',
            '-o': 'utfile filename'
        },
        'examples': [
            'gprofng-display-src  # Display source code and optionally disassembly of ',
            'gprofng-display-src --help  # Show help',
            'gprofng-display-src --version  # Show version'
        ],
        'category': 'Other'
    },
    'gprofng-display-text': {
        'desc': 'Display the performance data in plain text format',
        'common_flags': {
            '--version': 'Print the version number and exit.',
            '--help': 'Print usage information and exit.',
            '-s': 'cript script-file'
        },
        'examples': [
            'gprofng-display-text  # Display the performance data in plain text format',
            'gprofng-display-text --help  # Show help',
            'gprofng-display-text --version  # Show version'
        ],
        'category': 'Other'
    },
    'grep': {
        'desc': 'print lines that match patterns',
        'common_flags': {
            '--help': 'Output a usage message and exit.',
            '-V': 'Output the version number of grep and exit.',
            '--version': 'Output the version number of grep and exit.',
            '-E': 'Interpret PATTERNS as extended regular expressions (EREs, see below).',
            '--extended-regexp': 'Interpret PATTERNS as extended regular expressions (EREs, see below).',
            '-F': 'Interpret PATTERNS as fixed strings, not regular expressions.',
            '--fixed-strings': 'Interpret PATTERNS as fixed strings, not regular expressions.',
            '-G': 'Interpret PATTERNS as basic regular expressions (BREs, see below). This is the default.',
            '--basic-regexp': 'Interpret PATTERNS as basic regular expressions (BREs, see below). This is the default.',
            '-P': 'Interpret PATTERNS as Perl-compatible regular expressions (PCREs). This option is experimental when combined with the -z (--null-data)',
            '--perl-regexp': 'Interpret PATTERNS as Perl-compatible regular expressions (PCREs). This option is experimental when combined with the -z (--null-data)',
            '-e': 'PATTERNS, --regexp=PATTERNS',
            '-f': 'FILE, --file=FILE',
            '-i': 'Ignore case distinctions in patterns and input data, so that characters that differ only in case match each other.',
            '--ignore-case': 'Ignore case distinctions in patterns and input data, so that characters that differ only in case match each other.'
        },
        'examples': [
            'grep  # print lines that match patterns',
            'grep \'pattern\' file.txt  # Search in file',
            'grep -r \'pattern\' directory/  # Recursive search',
            'grep -i \'pattern\' file.txt  # Case-insensitive'
        ],
        'category': 'Other'
    },
    'groff': {
        'desc': 'front end to the GNU roff document formatting system',
        'common_flags': {
            '-h': 'and --help display a usage message and exit.',
            '-D': 'enc Set fallback input encoding used by preconv(1) to enc; implies -k.',
            '-e': 'Run eqn(1) preprocessor.',
            '-g': 'Run grn(1) preprocessor.',
            '-G': 'Run grap(1) preprocessor; implies -p.',
            '-I': 'dir Works as troff\'s option (see below), but also implies -g and -s. It is passed to soelim(1) and the output driver, and grn is passed an -M',
            '-j': 'Run chem(1) preprocessor; implies -p.',
            '-k': 'Run preconv(1) preprocessor. Refer to its man page for its behavior if neither of groff\'s -K or -D options is also specified.',
            '-K': 'enc Set input encoding used by preconv(1) to enc; implies -k.',
            '-l': 'Send the output to a spooler program for printing. The “print” directive in the device description file specifies the default command to be',
            '-L': 'arg Pass arg to the print spooler program. If multiple args are required, pass each with a separate -L option. groff does not prefix an option',
            '-M': 'Works as troff\'s option (see below), but is also passed to eqn(1), grap(1), and grn(1).',
            '-N': 'Prohibit newlines between eqn delimiters: pass -N to eqn(1).',
            '-p': 'Run pic(1) preprocessor.',
            '-P': 'arg Pass arg to the postprocessor. If multiple args are required, pass each with a separate -P option. groff does not prefix an option dash to'
        },
        'examples': [
            'groff  # front end to the GNU roff document formatting syst',
            'groff -h  # Show help'
        ],
        'category': 'Other'
    },
    'grog': {
        'desc': '“groff guess”-infer the groff command a document requires',
        'common_flags': {
            '-h': 'and --help display a usage message, whereas -v and --version display version information; all exit afterward.',
            '--ligatures': 'includes the arguments -P-y -PU in the inferred groff command. These are supported only by the pdf output device.',
            '--run': 'writes the inferred command to the standard error stream and then executes it.'
        },
        'examples': [
            'grog  # “groff guess”-infer the groff command a document r',
            'grog -h  # Show help'
        ],
        'category': 'Other'
    },
    'grops': {
        'desc': 'groff output driver for PostScript',
        'common_flags': {
            '--help': 'displays a usage message, while -v and --version show version information; all exit afterward.',
            '-b': 'n Work around problems with spoolers, previewers, and older printers. Normally, grops produces output at PostScript LanguageLevel 2 that con‐',
            '-c': 'n Output n copies of each page.',
            '-F': 'dir Prepend directory dir/devname to the search path for font and device description and PostScript prologue files; name is the name of the de‐',
            '-g': 'Generate PostScript code to guess the page length. The guess is correct only if the imageable area is vertically centered on the page. This',
            '-I': 'dir Search the directory dir for files named in \\X\'ps: file\' and \\X\'ps: import\' escape sequences. -I may be specified more than once; each dir',
            '-l': 'Use landscape orientation rather than portrait.',
            '-m': 'Turn on manual feed for the document.',
            '-p': 'fmt Set physical dimensions of output medium, overriding the papersize, paperlength, and paperwidth directives in the DESC file. fmt can be any',
            '-P': 'prologue',
            '-w': 'n Draw rules (lines) with a thickness of n thousandths of an em. The default thickness is 40 (0.04 em).'
        },
        'examples': [
            'grops  # groff output driver for PostScript',
            'grops --help  # Show help'
        ],
        'category': 'Other'
    },
    'gunzip': {
        'desc': 'compress or expand files',
        'common_flags': {
            '-a': '--ascii',
            '-c': '--stdout --to-stdout',
            '-d': '--decompress --uncompress',
            '-f': '--force',
            '-h': '--help',
            '-k': '--keep',
            '-l': '--list',
            '-L': '--license',
            '-n': '--no-name',
            '-N': '--name',
            '-q': '--quiet',
            '-r': '--recursive',
            '-S': '.suf --suffix .suf',
            '--synchronous': 'Use synchronous output. With this option, gzip is less likely to lose data during a system crash, but it can be considerably slower.',
            '-t': '--test'
        },
        'examples': [
            'gunzip  # compress or expand files',
            'gunzip -h  # Show help',
            'gunzip -r -f  # Recursive and forced',
            'gunzip -a  # Show all'
        ],
        'category': 'Other'
    },
    'gzexe': {
        'desc': 'compress executable files in place',
        'common_flags': {
            '-d': 'Decompress the given executables instead of compressing them.'
        },
        'examples': [
            'gzexe  # compress executable files in place'
        ],
        'category': 'Other'
    },
    'gzip': {
        'desc': 'compress or expand files',
        'common_flags': {
            '-a': '--ascii',
            '-c': '--stdout --to-stdout',
            '-d': '--decompress --uncompress',
            '-f': '--force',
            '-h': '--help',
            '-k': '--keep',
            '-l': '--list',
            '-L': '--license',
            '-n': '--no-name',
            '-N': '--name',
            '-q': '--quiet',
            '-r': '--recursive',
            '-S': '.suf --suffix .suf',
            '--synchronous': 'Use synchronous output. With this option, gzip is less likely to lose data during a system crash, but it can be considerably slower.',
            '-t': '--test'
        },
        'examples': [
            'gzip  # compress or expand files',
            'gzip -h  # Show help',
            'gzip -r -f  # Recursive and forced',
            'gzip -a  # Show all'
        ],
        'category': 'Other'
    },
    'h2ph': {
        'desc': 'convert .h C header files to .ph Perl header files',
        'common_flags': {
            '-d': 'destination_dir',
            '-r': 'Run recursively; if any of headerfiles are directories, then run h2ph on all files in those directories (and their subdirectories, etc.). -r',
            '-a': 'Run automagically; convert headerfiles, as well as any .h files which they include. This option will search for .h files in all directories',
            '-l': 'Symbolic links will be replicated in the destination directory. If -l is not specified, then links are skipped over.',
            '-h': 'Put \'hints\' in the .ph files which will help in locating problems with h2ph. In those cases when you require a .ph file containing syntax',
            '-e': 'If an error is encountered during conversion, output file will be removed and a warning emitted instead of terminating the conversion',
            '-D': 'Include the code from the .h file as a comment in the .ph file. This is primarily used for debugging h2ph.',
            '-Q': '\'Quiet\' mode; don\'t print out the names of the files being converted.'
        },
        'examples': [
            'h2ph  # convert .h C header files to .ph Perl header files',
            'h2ph -h  # Show help',
            'h2ph -a  # Show all'
        ],
        'category': 'Other'
    },
    'h2xs': {
        'desc': 'convert .h C header files to Perl extensions',
        'common_flags': {
            '-A': 'Omit all autoload facilities. This is the same as -c but also removes the \"use AutoLoader\" statement from the .pm file.',
            '--omit-autoload': 'Omit all autoload facilities. This is the same as -c but also removes the \"use AutoLoader\" statement from the .pm file.',
            '-B': 'Use an alpha/beta style version number. Causes version number to be \"0.00_01\" unless -v is specified.',
            '--beta-version': 'Use an alpha/beta style version number. Causes version number to be \"0.00_01\" unless -v is specified.',
            '-C': 'Omits creation of the Changes file, and adds a HISTORY section to the POD template.',
            '--omit-changes': 'Omits creation of the Changes file, and adds a HISTORY section to the POD template.',
            '-F': '=addflags',
            '--cpp-flags': '=addflags',
            '-M': '=regular expression',
            '--func-mask': '=regular expression',
            '-O': 'Allows a pre-existing extension directory to be overwritten.',
            '--overwrite-ok': 'Allows a pre-existing extension directory to be overwritten.',
            '-P': 'Omit the autogenerated stub POD section.',
            '--omit-pod': 'Omit the autogenerated stub POD section.',
            '-X': 'Omit the XS portion. Used to generate a skeleton pure Perl module. \"-c\" and \"-f\" are implicitly enabled.'
        },
        'examples': [
            'h2xs  # convert .h C header files to Perl extensions'
        ],
        'category': 'Other'
    },
    'hardlink': {
        'desc': 'link multiple copies of a file',
        'common_flags': {
            '-c': 'Consider only file content, not attributes, when determining whether two files are equal. Same as -pot.',
            '--content': 'Consider only file content, not attributes, when determining whether two files are equal. Same as -pot.',
            '-b': 'size',
            '--io-size': 'size',
            '-d': 'Only try to link files with the same directory name. The top-level directory (as specified on the hardlink command line) is ignored. For',
            '--respect-dir': 'Only try to link files with the same directory name. The top-level directory (as specified on the hardlink command line) is ignored. For',
            '--respect-name': 'Only try to link files with the same (base)name. It’s strongly recommended to use long options rather than -f which is interpreted in a',
            '-f': 'Only try to link files with the same (base)name. It’s strongly recommended to use long options rather than -f which is interpreted in a',
            '-F': 'Keep files found in the earliest specified top-level directory if there are multiple identical files in different trees. For example, hardlink',
            '--prioritize-trees': 'Keep files found in the earliest specified top-level directory if there are multiple identical files in different trees. For example, hardlink',
            '-i': 'regex',
            '--include': 'regex',
            '-m': 'Among equal files, keep the file with the highest link count.',
            '--maximize': 'Among equal files, keep the file with the highest link count.',
            '-M': 'Among equal files, keep the file with the lowest link count.'
        },
        'examples': [
            'hardlink  # link multiple copies of a file'
        ],
        'category': 'Other'
    },
    'hd': {
        'desc': 'display file contents in hexadecimal, decimal, octal, or ascii',
        'common_flags': {
            '-b': 'One-byte octal display. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, zero-filled bytes of input',
            '--one-byte-octal': 'One-byte octal display. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, zero-filled bytes of input',
            '-X': 'One-byte hexadecimal display. Display the input offset in hexadecimal, followed by sixteen space-separated, two-column, zero-filled bytes of',
            '--one-byte-hex': 'One-byte hexadecimal display. Display the input offset in hexadecimal, followed by sixteen space-separated, two-column, zero-filled bytes of',
            '-c': 'One-byte character display. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, space-filled characters',
            '--one-byte-char': 'One-byte character display. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, space-filled characters',
            '-C': 'Canonical hex+ASCII display. Display the input offset in hexadecimal, followed by sixteen space-separated, two-column, hexadecimal bytes,',
            '--canonical': 'Canonical hex+ASCII display. Display the input offset in hexadecimal, followed by sixteen space-separated, two-column, hexadecimal bytes,',
            '-d': 'Two-byte decimal display. Display the input offset in hexadecimal, followed by eight space-separated, five-column, zero-filled, two-byte units',
            '--two-bytes-decimal': 'Two-byte decimal display. Display the input offset in hexadecimal, followed by eight space-separated, five-column, zero-filled, two-byte units',
            '-e': 'format_string',
            '--format': 'format_string',
            '-f': 'file',
            '--format-file': 'file',
            '-L': '[=when]'
        },
        'examples': [
            'hd  # display file contents in hexadecimal, decimal, oct'
        ],
        'category': 'Other'
    },
    'hexdump': {
        'desc': 'display file contents in hexadecimal, decimal, octal, or ascii',
        'common_flags': {
            '-b': 'One-byte octal display. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, zero-filled bytes of input',
            '--one-byte-octal': 'One-byte octal display. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, zero-filled bytes of input',
            '-X': 'One-byte hexadecimal display. Display the input offset in hexadecimal, followed by sixteen space-separated, two-column, zero-filled bytes of',
            '--one-byte-hex': 'One-byte hexadecimal display. Display the input offset in hexadecimal, followed by sixteen space-separated, two-column, zero-filled bytes of',
            '-c': 'One-byte character display. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, space-filled characters',
            '--one-byte-char': 'One-byte character display. Display the input offset in hexadecimal, followed by sixteen space-separated, three-column, space-filled characters',
            '-C': 'Canonical hex+ASCII display. Display the input offset in hexadecimal, followed by sixteen space-separated, two-column, hexadecimal bytes,',
            '--canonical': 'Canonical hex+ASCII display. Display the input offset in hexadecimal, followed by sixteen space-separated, two-column, hexadecimal bytes,',
            '-d': 'Two-byte decimal display. Display the input offset in hexadecimal, followed by eight space-separated, five-column, zero-filled, two-byte units',
            '--two-bytes-decimal': 'Two-byte decimal display. Display the input offset in hexadecimal, followed by eight space-separated, five-column, zero-filled, two-byte units',
            '-e': 'format_string',
            '--format': 'format_string',
            '-f': 'file',
            '--format-file': 'file',
            '-L': '[=when]'
        },
        'examples': [
            'hexdump  # display file contents in hexadecimal, decimal, oct'
        ],
        'category': 'Other'
    },
    'host': {
        'desc': 'DNS lookup utility',
        'common_flags': {
            '-4': 'This option specifies that only IPv4 should be used for query transport. See also the -6 option.',
            '-6': 'This option specifies that only IPv6 should be used for query transport. See also the -4 option.',
            '-a': 'The -a (\"all\") option is normally equivalent to -v -t ANY. It also affects the behavior of the -l list zone option.',
            '-A': 'The -A (\"almost all\") option is equivalent to -a, except that RRSIG, NSEC, and NSEC3 records are omitted from the output.',
            '-c': 'class',
            '-C': 'This option indicates that named should check consistency, meaning that host queries the SOA records for zone name from all the listed au‐',
            '-d': 'This option prints debugging traces, and is equivalent to the -v verbose option.',
            '-l': 'This option tells named to list the zone, meaning the host command performs a zone transfer of zone name and prints out the NS, PTR, and ad‐',
            '-N': 'ndots',
            '-p': 'port',
            '-r': 'This option specifies a non-recursive query; setting this option clears the RD (recursion desired) bit in the query. This means that the name',
            '-R': 'number',
            '-s': 'This option tells named not to send the query to the next nameserver if any server responds with a SERVFAIL response, which is the reverse of',
            '-t': 'type',
            '-T': 'This option specifies TCP or UDP. By default, host uses UDP when making queries; the -T option makes it use a TCP connection when querying'
        },
        'examples': [
            'host  # DNS lookup utility',
            'host -a  # Show all'
        ],
        'category': 'Other'
    },
    'hostname': {
        'desc': 'show or set the system\'s host name',
        'common_flags': {
            '-a': 'Display the alias name of the host (if used). This option is deprecated and should not be used anymore.',
            '--alias': 'Display the alias name of the host (if used). This option is deprecated and should not be used anymore.',
            '-A': 'Displays all FQDNs of the machine. This option enumerates all configured network addresses on all configured network interfaces, and trans‐',
            '--all-fqdns': 'Displays all FQDNs of the machine. This option enumerates all configured network addresses on all configured network interfaces, and trans‐',
            '-b': 'Always set a hostname; this allows the file specified by -F to be non-existent or empty, in which case the default hostname localhost will be',
            '--boot': 'Always set a hostname; this allows the file specified by -F to be non-existent or empty, in which case the default hostname localhost will be',
            '-d': 'Display the name of the DNS domain. Don\'t use the command domainname to get the DNS domain name because it will show the NIS domain name and',
            '--domain': 'Display the name of the DNS domain. Don\'t use the command domainname to get the DNS domain name because it will show the NIS domain name and',
            '-f': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '--fqdn': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '--long': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '-F': 'filename',
            '--file': 'filename',
            '-i': 'Display the network address(es) of the host name. Note that this works only if the host name can be resolved. Avoid using this option; use',
            '--ip-address': 'Display the network address(es) of the host name. Note that this works only if the host name can be resolved. Avoid using this option; use'
        },
        'examples': [
            'hostname  # show or set the system\'s host name',
            'hostname -a  # Show all'
        ],
        'category': 'Other'
    },
    'hostnamectl': {
        'desc': 'Control the system hostname',
        'common_flags': {
            '--static': 'If status is invoked (or no explicit command is given) and one of these switches is specified, hostnamectl will print out just this selected',
            '--transient': 'If status is invoked (or no explicit command is given) and one of these switches is specified, hostnamectl will print out just this selected',
            '--pretty': 'If status is invoked (or no explicit command is given) and one of these switches is specified, hostnamectl will print out just this selected',
            '-H': '=',
            '--host': '=',
            '-M': '=',
            '--machine': '=',
            '--no-ask-password': 'Do not query the user for authentication for privileged operations.',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.',
            '--json': '=MODE',
            '-j': 'Equivalent to --json=pretty if running on a terminal, and --json=short otherwise.'
        },
        'examples': [
            'hostnamectl  # Control the system hostname',
            'hostnamectl -h  # Show help',
            'hostnamectl --version  # Show version'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-addr2line': {
        'desc': 'convert addresses or symbol+offset into file names and line numbers',
        'common_flags': {
            '-a': '--addresses',
            '-b': 'bfdname',
            '--target': '=bfdname',
            '-C': '--demangle[=style]',
            '-e': 'filename',
            '--exe': '=filename',
            '-f': '--functions',
            '-s': '--basenames',
            '-i': '--inlines',
            '-j': '--section',
            '-p': '--pretty-print',
            '-r': '-R',
            '--recurse-limit': '--no-recurse-limit',
            '--recursion-limit': '--no-recursion-limit'
        },
        'examples': [
            'i686-w64-mingw32-addr2line  # convert addresses or symbol+offset into file names',
            'i686-w64-mingw32-addr2line -r -f  # Recursive and forced',
            'i686-w64-mingw32-addr2line -a  # Show all'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-ar': {
        'desc': 'create, modify, and extract from archives',
        'common_flags': {
            '--output': 'dirname',
            '--help': 'Displays the list of command-line options supported by ar and then exits.',
            '--version': 'Displays the version information of ar and then exits.',
            '-X': '32_64',
            '--plugin': 'name',
            '--target': 'target',
            '--record-libdeps': 'libdeps',
            '--thin': 'Make the specified archive a thin archive. If it already exists and is a regular archive, the existing members must be present in the same'
        },
        'examples': [
            'i686-w64-mingw32-ar  # create, modify, and extract from archives',
            'i686-w64-mingw32-ar --help  # Show help',
            'i686-w64-mingw32-ar --version  # Show version'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-elfedit': {
        'desc': 'update ELF header and program property of ELF files',
        'common_flags': {
            '--output-abiversion': '=version',
            '--enable-x86-feature': '.',
            '--input-mach': '=machine',
            '--output-mach': '=machine',
            '--input-type': '=type',
            '--output-type': '=type',
            '--input-osabi': '=osabi',
            '--output-osabi': '=osabi',
            '--input-abiversion': '=version',
            '--disable-x86-feature': '=feature',
            '-v': '--version',
            '-h': '--help'
        },
        'examples': [
            'i686-w64-mingw32-elfedit  # update ELF header and program property of ELF file',
            'i686-w64-mingw32-elfedit -h  # Show help',
            'i686-w64-mingw32-elfedit -v  # Show version',
            'i686-w64-mingw32-elfedit -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-ld': {
        'desc': 'The GNU linker',
        'common_flags': {
            '-W': 'l, (or whatever is appropriate for the particular compiler driver) like this:',
            '-a': 'keyword',
            '--audit': 'AUDITLIB',
            '-b': 'input-format',
            '--format': '=input-format',
            '-c': 'MRI-commandfile',
            '--mri-script': '=MRI-commandfile',
            '-d': 'p These three options are equivalent; multiple forms are supported for compatibility with other linkers. They assign space to common symbols even',
            '--depaudit': 'AUDITLIB',
            '-P': 'AUDITLIB',
            '--enable-linker-version': 'Enables the \"LINKER_VERSION\" linker script directive, described in Output Section Data. If this directive is used in a linker script and this',
            '--disable-linker-version': 'Disables the \"LINKER_VERSION\" linker script directive, so that it does not insert a version string. This is the default.',
            '--enable-non-contiguous-regions': 'This option avoids generating an error if an input section does not fit a matching output section. The linker tries to allocate the input',
            '--enable-non-contiguous-regions-warnings': 'This option enables warnings when \"--enable-non-contiguous-regions\" allows possibly unexpected matches in sections mapping, potentially leading',
            '-e': 'entry'
        },
        'examples': [
            'i686-w64-mingw32-ld  # The GNU linker',
            'i686-w64-mingw32-ld -a  # Show all'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-ld.bfd': {
        'desc': 'The GNU linker',
        'common_flags': {
            '-W': 'l, (or whatever is appropriate for the particular compiler driver) like this:',
            '-a': 'keyword',
            '--audit': 'AUDITLIB',
            '-b': 'input-format',
            '--format': '=input-format',
            '-c': 'MRI-commandfile',
            '--mri-script': '=MRI-commandfile',
            '-d': 'p These three options are equivalent; multiple forms are supported for compatibility with other linkers. They assign space to common symbols even',
            '--depaudit': 'AUDITLIB',
            '-P': 'AUDITLIB',
            '--enable-linker-version': 'Enables the \"LINKER_VERSION\" linker script directive, described in Output Section Data. If this directive is used in a linker script and this',
            '--disable-linker-version': 'Disables the \"LINKER_VERSION\" linker script directive, so that it does not insert a version string. This is the default.',
            '--enable-non-contiguous-regions': 'This option avoids generating an error if an input section does not fit a matching output section. The linker tries to allocate the input',
            '--enable-non-contiguous-regions-warnings': 'This option enables warnings when \"--enable-non-contiguous-regions\" allows possibly unexpected matches in sections mapping, potentially leading',
            '-e': 'entry'
        },
        'examples': [
            'i686-w64-mingw32-ld.bfd  # The GNU linker',
            'i686-w64-mingw32-ld.bfd -a  # Show all'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-nm': {
        'desc': 'list symbols from object files',
        'common_flags': {
            '-A': '-o',
            '--print-file-name': 'Precede each symbol by the name of the input file (or archive member) in which it was found, rather than identifying the input file once only,',
            '-a': '--debug-syms',
            '-B': 'The same as --format=bsd (for compatibility with the MIPS nm).',
            '-C': '--demangle[=style]',
            '--no-demangle': 'Do not demangle low-level symbol names. This is the default.',
            '--recurse-limit': '--no-recurse-limit',
            '--recursion-limit': '--no-recursion-limit',
            '-D': '--dynamic',
            '-f': 'format',
            '--format': '=format',
            '-g': '--extern-only',
            '-h': '--help',
            '--ifunc-chars': '=CHARS',
            '-l': '--line-numbers'
        },
        'examples': [
            'i686-w64-mingw32-nm  # list symbols from object files',
            'i686-w64-mingw32-nm -h  # Show help',
            'i686-w64-mingw32-nm -a  # Show all'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-objcopy': {
        'desc': 'copy and translate object files',
        'common_flags': {
            '-I': 'bfdname',
            '--input-target': '=bfdname',
            '-O': 'bfdname',
            '--output-target': '=bfdname',
            '-F': 'bfdname',
            '--target': '=bfdname',
            '-B': 'bfdarch',
            '--binary-architecture': '=bfdarch',
            '-j': 'sectionpattern',
            '--only-section': '=.text.* --only-section=!.text.foo',
            '-R': 'sectionpattern',
            '--remove-section': '=.text.* --remove-section=!.text.foo',
            '--keep-section': '=sectionpattern',
            '--remove-relocations': '=.text.* --remove-relocations=!.text.foo',
            '--strip-section-headers': 'Strip section header This option is specific to ELF files. Implies --strip-all and --merge-notes.'
        },
        'examples': [
            'i686-w64-mingw32-objcopy  # copy and translate object files'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-objdump': {
        'desc': 'display information from object files',
        'common_flags': {
            '-a': 'must be given.',
            '-d': 'must be given.',
            '-D': 'must be given.',
            '-e': 'must be given.',
            '-f': 'must be given.',
            '-g': 'must be given.',
            '-G': 'must be given.',
            '-h': 'must be given.',
            '-H': 'must be given.',
            '-p': 'must be given.',
            '-P': 'must be given.',
            '-r': 'must be given.',
            '-R': 'must be given.',
            '-s': 'must be given.',
            '-S': 'must be given.'
        },
        'examples': [
            'i686-w64-mingw32-objdump  # display information from object files',
            'i686-w64-mingw32-objdump -h  # Show help',
            'i686-w64-mingw32-objdump -r -f  # Recursive and forced',
            'i686-w64-mingw32-objdump -a  # Show all'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-ranlib': {
        'desc': 'generate an index to an archive',
        'common_flags': {
            '-h': '-H',
            '--help': 'Show usage information for ranlib.',
            '-v': '-V',
            '--version': 'Show the version number of ranlib.',
            '-D': 'Operate in deterministic mode. The symbol map archive member\'s header will show zero for the UID, GID, and timestamp. When this option is',
            '-t': 'Update the timestamp of the symbol map of an archive.',
            '-U': 'Do not operate in deterministic mode. This is the inverse of the -D option, above: the archive index will get actual UID, GID, timestamp, and'
        },
        'examples': [
            'i686-w64-mingw32-ranlib  # generate an index to an archive',
            'i686-w64-mingw32-ranlib -h  # Show help',
            'i686-w64-mingw32-ranlib -v  # Show version',
            'i686-w64-mingw32-ranlib -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-readelf': {
        'desc': 'display information about ELF files',
        'common_flags': {
            '-a': '--all',
            '--unwind': 'and --histogram.',
            '--section-groups': 'and --histogram.',
            '-h': '--file-header',
            '-l': '--program-headers',
            '--segments': 'Displays the information contained in the file\'s segment headers, if it has any.',
            '--quiet': 'Suppress \"no symbols\" diagnostic.',
            '-S': '--sections',
            '--section-headers': 'Displays the information contained in the file\'s section headers, if it has any.',
            '-g': '--section-groups',
            '-t': '--section-details',
            '-s': '--symbols',
            '--syms': 'Displays the entries in symbol table section of the file, if it has one. If a symbol has version information associated with it then this is',
            '--dyn-syms': 'Displays the entries in dynamic symbol table section of the file, if it has one. The output format is the same as the format used by the --syms',
            '--lto-syms': 'Displays the contents of any LTO symbol tables in the file.'
        },
        'examples': [
            'i686-w64-mingw32-readelf  # display information about ELF files',
            'i686-w64-mingw32-readelf -h  # Show help',
            'i686-w64-mingw32-readelf -a  # Show all'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-size': {
        'desc': 'list section sizes and total size of binary files',
        'common_flags': {
            '-A': '-B',
            '-G': '--format=compatibility',
            '--help': '-h',
            '-H': '-? Show a summary of acceptable arguments and options.',
            '-d': '-o',
            '-x': '--radix=number',
            '--common': 'Print total size of common symbols in each file. When using Berkeley or GNU format these are included in the bss size.',
            '-t': '--totals',
            '--target': '=bfdname',
            '-v': '-V',
            '--version': 'Display the version number of size.',
            '-f': 'Ignored. This option is used by other versions of the size program, but it is not supported by the GNU Binutils version.'
        },
        'examples': [
            'i686-w64-mingw32-size  # list section sizes and total size of binary files',
            'i686-w64-mingw32-size --help  # Show help',
            'i686-w64-mingw32-size -v  # Show version',
            'i686-w64-mingw32-size -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-strip': {
        'desc': 'discard symbols and other data from object files',
        'common_flags': {
            '-F': 'bfdname',
            '--target': '=bfdname',
            '--help': 'Show a summary of the options to strip and exit.',
            '--info': 'Display a list showing all architectures and object formats available.',
            '-I': 'bfdname',
            '--input-target': '=bfdname',
            '-O': 'bfdname',
            '--output-target': '=bfdname',
            '-R': 'sectionname',
            '--remove-section': '=.text.* --remove-section=!.text.foo',
            '--keep-section': '=sectionpattern',
            '--remove-relocations': '=.text.* --remove-relocations=!.text.foo',
            '--strip-section-headers': 'Strip section headers. This option is specific to ELF files. Implies --strip-all and --merge-notes.',
            '-s': '--strip-all',
            '-g': '-S'
        },
        'examples': [
            'i686-w64-mingw32-strip  # discard symbols and other data from object files',
            'i686-w64-mingw32-strip --help  # Show help'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-windmc': {
        'desc': 'generates Windows message resources',
        'common_flags': {
            '-a': '--ascii_in',
            '-A': '--ascii_out',
            '-b': '--binprefix',
            '-c': '--customflag',
            '-C': 'codepage',
            '--codepage_in': 'codepage',
            '-d': '--decimal_values',
            '-e': 'ext',
            '--extension': 'ext',
            '-F': 'target',
            '--target': 'target',
            '-h': 'path',
            '--headerdir': 'path',
            '-H': '--help',
            '-m': 'characters'
        },
        'examples': [
            'i686-w64-mingw32-windmc  # generates Windows message resources',
            'i686-w64-mingw32-windmc -h  # Show help',
            'i686-w64-mingw32-windmc -a  # Show all'
        ],
        'category': 'Other'
    },
    'i686-w64-mingw32-windres': {
        'desc': 'manipulate Windows resources',
        'common_flags': {
            '-i': 'filename',
            '--input': 'filename',
            '-o': 'filename',
            '--output': 'filename',
            '-J': 'format',
            '--input-format': 'format',
            '-O': 'format',
            '--output-format': 'format',
            '-F': 'target',
            '--target': 'target',
            '--preprocessor': 'option has not been specified then a default set of preprocessor arguments will be used, with any --preprocessor-arg options',
            '--preprocessor-arg': 'option',
            '-I': 'directory',
            '--include-dir': 'directory',
            '-D': 'target'
        },
        'examples': [
            'i686-w64-mingw32-windres  # manipulate Windows resources'
        ],
        'category': 'Other'
    },
    'iasecc-tool': {
        'desc': 'displays information about IAS/ECC card',
        'common_flags': {
            '--reader': 'arg,',
            '--list-applications': ',',
            '--aid': 'hex-aid,',
            '--list-sdos': 'sdo-type,',
            '--verbose': 'Causes cardos-tool to be more verbose. Specify this flag several times to enable debug output in the opensc library.',
            '-v': 'Causes cardos-tool to be more verbose. Specify this flag several times to enable debug output in the opensc library.',
            '--wait': 'Causes iasecc-tool to wait for the token to be inserted into reader.',
            '-w': 'Causes iasecc-tool to wait for the token to be inserted into reader.'
        },
        'examples': [
            'iasecc-tool  # displays information about IAS/ECC card',
            'iasecc-tool -v  # Show version',
            'iasecc-tool -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'iconv': {
        'desc': 'convert text from one character encoding to another',
        'common_flags': {
            '--from-code': '=from-encoding',
            '-f': 'from-encoding',
            '--to-code': '=to-encoding',
            '-t': 'to-encoding',
            '--list': '-l List all known character set encodings.',
            '-c': 'Silently discard characters that cannot be converted instead of terminating when encountering such characters.',
            '--output': '=outputfile',
            '-o': 'outputfile',
            '--silent': '-s This option is ignored; it is provided only for compatibility.',
            '--verbose': 'Print progress information on standard error when processing multiple files.',
            '--help': '-? Print a usage summary and exit.',
            '--usage': 'Print a short usage summary and exit.',
            '--version': '-V Print the version number, license, and disclaimer of warranty for iconv.'
        },
        'examples': [
            'iconv  # convert text from one character encoding to anothe',
            'iconv --help  # Show help',
            'iconv --version  # Show version',
            'iconv --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'infocmp': {
        'desc': 'compare or print out terminfo descriptions',
        'common_flags': {
            '-I': 'use terminfo capability codes',
            '-L': 'use “long” capability names',
            '-C': '.',
            '-r': 'with -C, include nonstandard capabilities',
            '-K': 'with -C, improve BSD compatibility',
            '-d': 'lists each capability that differs between two entries. Each capability name is followed by “:” and comma-separated capability values, then a',
            '-c': 'lists each capability that two entries have in common. infocmp ignores capabilities missing from either entry. Each capability name is fol‐',
            '-n': 'lists capabilities that are in none of the given entries. Each capability name is preceded by “!” and followed by a period.',
            '-0': 'causes the fields to be printed on one line, without wrapping.',
            '-1': 'causes the fields to be printed out one to a line. Otherwise, the fields will be printed several to a line to a maximum width of 60 charac‐',
            '-a': 'tells infocmp to retain commented-out capabilities rather than discarding them. Capabilities are commented by prefixing them with a period.',
            '-D': 'tells infocmp to print the database locations that it knows about, and exit.',
            '-E': 'Dump the capabilities of the given terminal as tables, needed in the C initializer for a TERMTYPE structure (the terminal capability structure',
            '-e': 'Dump the capabilities of the given terminal as a C initializer for a TERMTYPE structure (the terminal capability structure in the <term.h>).',
            '-F': 'compare terminfo files. This assumes that two following arguments are filenames. The files are searched for pairwise matches between entries,'
        },
        'examples': [
            'infocmp  # compare or print out terminfo descriptions',
            'infocmp -a  # Show all'
        ],
        'category': 'Other'
    },
    'ionice': {
        'desc': 'set or get process I/O scheduling class and priority',
        'common_flags': {
            '-c': 'class',
            '--class': 'class',
            '-n': 'level',
            '--classdata': 'level',
            '-p': 'PID...',
            '--pid': 'PID...',
            '-P': 'PGID...',
            '--pgid': 'PGID...',
            '-t': 'Ignore failure to set the requested priority. If command was specified, run it even in case it was not possible to set the desired scheduling',
            '--ignore': 'Ignore failure to set the requested priority. If command was specified, run it even in case it was not possible to set the desired scheduling',
            '-u': 'UID...',
            '--uid': 'UID...',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.'
        },
        'examples': [
            'ionice  # set or get process I/O scheduling class and priori',
            'ionice -h  # Show help',
            'ionice -V  # Show version'
        ],
        'category': 'Other'
    },
    'iostat': {
        'desc': 'Report Central Processing Unit (CPU) statistics and input/output statistics for devices and partitions.',
        'common_flags': {
            '-c': 'Display the CPU utilization report.',
            '--compact': 'Don\'t break the Device Utilization Report into sub-reports so that all the metrics get displayed on a single line.',
            '-d': 'Display the device utilization report.',
            '--dec': '={ 0 | 1 | 2 }',
            '-f': 'directory',
            '-g': 'group_name { device [...] | ALL }',
            '-H': 'This option must be used with option -g and indicates that only global statistics for the group are to be displayed, and not statistics for',
            '-h': 'This option is equivalent to specifying --human --pretty.',
            '--human': 'Print sizes in human readable format (e.g. 1.0k, 1.2M, etc.) The units displayed with this option supersede any other default units (e.g.',
            '-j': '{ ID | LABEL | PATH | UUID | ... } [ device [...] | ALL ]',
            '-k': 'Display statistics in kilobytes per second.',
            '-m': 'Display statistics in megabytes per second.',
            '-N': 'Display the registered device mapper names for any device mapper devices. Useful for viewing LVM2 statistics.',
            '-o': 'JSON',
            '-p': '[ { device[,...] | ALL } ]'
        },
        'examples': [
            'iostat  # Report Central Processing Unit (CPU) statistics an',
            'iostat -h  # Show help'
        ],
        'category': 'Other'
    },
    'ipcmk': {
        'desc': 'make various IPC resources',
        'common_flags': {
            '-M': 'size',
            '--shmem': 'size',
            '-m': 'size',
            '--posix-shmem': 'size',
            '-Q': 'Create a message queue.',
            '--queue': 'Create a message queue.',
            '-q': 'Create a POSIX message queue.',
            '--posix-mqueue': 'Create a POSIX message queue.',
            '-S': 'number',
            '--semaphore': 'number',
            '-s': 'Create a POSIX named semaphore.',
            '--posix-semaphore': 'Create a POSIX named semaphore.',
            '-n': 'name',
            '--name': 'name',
            '-p': 'mode'
        },
        'examples': [
            'ipcmk  # make various IPC resources'
        ],
        'category': 'Other'
    },
    'ipcrm': {
        'desc': 'remove certain IPC resources',
        'common_flags': {
            '-a': '[shm] [pshm] [msg] [pmsg] [sem] [psem]',
            '--all': '[shm] [pshm] [msg] [pmsg] [sem] [psem]',
            '-M': 'shmkey',
            '--shmem-key': 'shmkey',
            '-m': 'shmid',
            '--shmem-id': 'shmid',
            '-x': 'name',
            '--posix-shmem': 'name',
            '-Q': 'msgkey',
            '--queue-key': 'msgkey',
            '-q': 'msgid',
            '--queue-id': 'msgid',
            '-y': 'name',
            '--posix-mqueue': 'name',
            '-S': 'semkey'
        },
        'examples': [
            'ipcrm  # remove certain IPC resources',
            'ipcrm -a  # Show all'
        ],
        'category': 'Other'
    },
    'ipcs': {
        'desc': 'show information on IPC facilities',
        'common_flags': {
            '-i': 'id',
            '--id': 'id',
            '-m': 'Write information about active shared memory segments.',
            '-q': 'Write information about active message queues.',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.',
            '--shmems': 'Write information about active shared memory segments.',
            '--queues': 'Write information about active message queues.',
            '-s': 'Write information about active semaphore sets.',
            '--semaphores': 'Write information about active semaphore sets.',
            '-a': 'Write information about all three resources (default).',
            '--all': 'Write information about all three resources (default).',
            '-c': 'Show creator and owner.'
        },
        'examples': [
            'ipcs  # show information on IPC facilities',
            'ipcs -h  # Show help',
            'ipcs --version  # Show version',
            'ipcs -a  # Show all'
        ],
        'category': 'Other'
    },
    'irb': {
        'desc': 'Interactive Ruby Shell',
        'common_flags': {
            '--version': 'Prints the version of irb.',
            '-E': 'external[:internal]',
            '--encoding': 'external[:internal]',
            '-I': 'path Same as `ruby -I\' . Specifies $LOAD_PATH directory',
            '-U': 'Same as `ruby -U\' . Sets the default value for internal encodings (Encoding.default_internal) to UTF-8.',
            '-d': 'Same as `ruby -d\' . Sets $DEBUG to true.',
            '-f': 'Suppresses read of ~/.irbrc.',
            '-w': 'Same as `ruby -w\' .',
            '-W': 'Same as `ruby -W\' .',
            '-h': '--help Prints a summary of the options.',
            '-r': 'library Same as `ruby -r\'. Causes irb to load the library using require.',
            '--inspect': 'Uses `inspect\' for output (default except for bc mode)',
            '--noinspect': 'Doesn\'t use inspect for output',
            '--multiline': 'Uses multiline editor module.',
            '--nomultiline': 'Doesn\'t use multiline editor module.'
        },
        'examples': [
            'irb  # Interactive Ruby Shell',
            'irb -h  # Show help',
            'irb --version  # Show version',
            'irb -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'irb3.3': {
        'desc': 'Interactive Ruby Shell',
        'common_flags': {
            '--version': 'Prints the version of irb.',
            '-E': 'external[:internal]',
            '--encoding': 'external[:internal]',
            '-I': 'path Same as `ruby -I\' . Specifies $LOAD_PATH directory',
            '-U': 'Same as `ruby -U\' . Sets the default value for internal encodings (Encoding.default_internal) to UTF-8.',
            '-d': 'Same as `ruby -d\' . Sets $DEBUG to true.',
            '-f': 'Suppresses read of ~/.irbrc.',
            '-w': 'Same as `ruby -w\' .',
            '-W': 'Same as `ruby -W\' .',
            '-h': '--help Prints a summary of the options.',
            '-r': 'library Same as `ruby -r\'. Causes irb to load the library using require.',
            '--inspect': 'Uses `inspect\' for output (default except for bc mode)',
            '--noinspect': 'Doesn\'t use inspect for output',
            '--multiline': 'Uses multiline editor module.',
            '--nomultiline': 'Doesn\'t use multiline editor module.'
        },
        'examples': [
            'irb3.3  # Interactive Ruby Shell',
            'irb3.3 -h  # Show help',
            'irb3.3 --version  # Show version',
            'irb3.3 -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'ischroot': {
        'desc': 'detect if running in a chroot',
        'common_flags': {
            '-f': 'Exit with status 1 if the detection is not possible.',
            '--default-false': 'Exit with status 1 if the detection is not possible.',
            '-t': 'Exit with status 0 if the detection is not possible.',
            '--default-true': 'Exit with status 0 if the detection is not possible.',
            '--help': 'Print a usage message on standard output and exit successfully.',
            '--version': 'Print version information on standard output and exit successfully.'
        },
        'examples': [
            'ischroot  # detect if running in a chroot',
            'ischroot --help  # Show help',
            'ischroot --version  # Show version'
        ],
        'category': 'Other'
    },
    'join': {
        'desc': 'join lines of two files on a common field',
        'common_flags': {
            '-i': 'ignore differences in case when comparing fields',
            '--ignore-case': 'ignore differences in case when comparing fields',
            '-j': 'FIELD',
            '-o': 'FORMAT',
            '-t': 'CHAR',
            '-v': 'FILENUM',
            '-1': 'FIELD',
            '-2': 'FIELD',
            '--check-order': 'check that the input is correctly sorted, even if all input lines are pairable',
            '--nocheck-order': 'do not check that the input is correctly sorted',
            '--header': 'treat the first line in each file as field headers, print them without trying to pair them',
            '-z': 'line delimiter is NUL, not newline',
            '--zero-terminated': 'line delimiter is NUL, not newline',
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'join  # join lines of two files on a common field',
            'join --help  # Show help',
            'join -v  # Show version',
            'join -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'journalctl': {
        'desc': 'Print log entries from the systemd journal',
        'common_flags': {
            '--system': 'Show messages from system services and the kernel (with --system). Show messages from service of current user (with --user). If neither is',
            '--user': 'Show messages from system services and the kernel (with --system). Show messages from service of current user (with --user). If neither is',
            '-M': '=',
            '--machine': '=',
            '-m': 'Show entries interleaved from all available journals, including remote ones.',
            '--merge': 'Show entries interleaved from all available journals, including remote ones.',
            '-D': 'DIR, --directory=DIR',
            '-i': 'GLOB, --file=GLOB',
            '--root': '=ROOT',
            '--image': '=, see above. If not specified defaults to the \"*\" policy, i.e. all recognized file systems in the image are used.',
            '--image-policy': '=policy',
            '--namespace': '=NAMESPACE'
        },
        'examples': [
            'journalctl  # Print log entries from the systemd journal'
        ],
        'category': 'Other'
    },
    'json_pp': {
        'desc': 'JSON::PP command utility',
        'common_flags': {
            '-f': '-f from_format',
            '-t': 'Writes a data in the given format to STDOUT.',
            '-j': 'son_opt',
            '-v': 'Verbose option, but currently no action in fact.',
            '-V': 'Prints version and exits.'
        },
        'examples': [
            'json_pp  # JSON::PP command utility',
            'json_pp -v  # Show version',
            'json_pp -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'kill': {
        'desc': 'send a signal to a process',
        'common_flags': {
            '-s': '<signal>',
            '--signal': '<signal>',
            '-q': 'value',
            '--queue': 'value',
            '-l': '[signal]',
            '--list': '[signal]',
            '-L': 'List signal names in a nice table.',
            '--table': 'List signal names in a nice table.'
        },
        'examples': [
            'kill  # send a signal to a process',
            'kill PID  # Terminate process',
            'kill -9 PID  # Force kill'
        ],
        'category': 'Other'
    },
    'laptop-detect': {
        'desc': 'attempt to detect a laptop',
        'common_flags': {
            '-h': '--help',
            '-v': '--verbose',
            '-V': '--version',
            '-D': '--debug'
        },
        'examples': [
            'laptop-detect  # attempt to detect a laptop',
            'laptop-detect -h  # Show help',
            'laptop-detect -v  # Show version',
            'laptop-detect -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'ld': {
        'desc': 'The GNU linker',
        'common_flags': {
            '-W': 'l, (or whatever is appropriate for the particular compiler driver) like this:',
            '-a': 'keyword',
            '--audit': 'AUDITLIB',
            '-b': 'input-format',
            '--format': '=input-format',
            '-c': 'MRI-commandfile',
            '--mri-script': '=MRI-commandfile',
            '-d': 'p These three options are equivalent; multiple forms are supported for compatibility with other linkers. They assign space to common symbols even',
            '--depaudit': 'AUDITLIB',
            '-P': 'AUDITLIB',
            '--enable-linker-version': 'Enables the \"LINKER_VERSION\" linker script directive, described in Output Section Data. If this directive is used in a linker script and this',
            '--disable-linker-version': 'Disables the \"LINKER_VERSION\" linker script directive, so that it does not insert a version string. This is the default.',
            '--enable-non-contiguous-regions': 'This option avoids generating an error if an input section does not fit a matching output section. The linker tries to allocate the input',
            '--enable-non-contiguous-regions-warnings': 'This option enables warnings when \"--enable-non-contiguous-regions\" allows possibly unexpected matches in sections mapping, potentially leading',
            '-e': 'entry'
        },
        'examples': [
            'ld  # The GNU linker',
            'ld -a  # Show all'
        ],
        'category': 'Other'
    },
    'ld.bfd': {
        'desc': 'The GNU linker',
        'common_flags': {
            '-W': 'l, (or whatever is appropriate for the particular compiler driver) like this:',
            '-a': 'keyword',
            '--audit': 'AUDITLIB',
            '-b': 'input-format',
            '--format': '=input-format',
            '-c': 'MRI-commandfile',
            '--mri-script': '=MRI-commandfile',
            '-d': 'p These three options are equivalent; multiple forms are supported for compatibility with other linkers. They assign space to common symbols even',
            '--depaudit': 'AUDITLIB',
            '-P': 'AUDITLIB',
            '--enable-linker-version': 'Enables the \"LINKER_VERSION\" linker script directive, described in Output Section Data. If this directive is used in a linker script and this',
            '--disable-linker-version': 'Disables the \"LINKER_VERSION\" linker script directive, so that it does not insert a version string. This is the default.',
            '--enable-non-contiguous-regions': 'This option avoids generating an error if an input section does not fit a matching output section. The linker tries to allocate the input',
            '--enable-non-contiguous-regions-warnings': 'This option enables warnings when \"--enable-non-contiguous-regions\" allows possibly unexpected matches in sections mapping, potentially leading',
            '-e': 'entry'
        },
        'examples': [
            'ld.bfd  # The GNU linker',
            'ld.bfd -a  # Show all'
        ],
        'category': 'Other'
    },
    'ldd': {
        'desc': 'print shared object dependencies',
        'common_flags': {
            '--version': 'Print the version number of ldd.',
            '--verbose': '-v Print all information, including, for example, symbol versioning information.',
            '--unused': '-u Print unused direct dependencies. (Since glibc 2.3.4.)',
            '--data-relocs': '-d Perform relocations and report any missing objects (ELF only).',
            '--function-relocs': '-r Perform relocations for both data objects and functions, and report any missing objects or functions (ELF only).',
            '--help': 'Usage information.'
        },
        'examples': [
            'ldd  # print shared object dependencies',
            'ldd --help  # Show help',
            'ldd --version  # Show version',
            'ldd --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'less': {
        'desc': 'display the contents of a file in a terminal',
        'common_flags': {
            '-a': 'or --search-skip-screen',
            '-A': 'or --SEARCH-SKIP-SCREEN',
            '-b': 'n or --buffers=n',
            '-B': 'or --auto-buffers',
            '-c': 'or --clear-screen',
            '-C': 'or --CLEAR-SCREEN',
            '-d': 'or --dumb',
            '-D': 'xcolor or --color=xcolor',
            '-e': 'or --quit-at-eof',
            '-E': 'or --QUIT-AT-EOF',
            '-f': 'or --force',
            '-F': 'or --quit-if-one-screen',
            '-g': 'or --hilite-search',
            '-G': 'or --HILITE-SEARCH',
            '-h': 'n or --max-back-scroll=n'
        },
        'examples': [
            'less  # display the contents of a file in a terminal',
            'less -h  # Show help',
            'less -a  # Show all'
        ],
        'category': 'Other'
    },
    'lessecho': {
        'desc': 'expand metacharacters',
        'common_flags': {
            '-e': 'x Specifies \"x\", rather than backslash, to be the escape char for metachars. If x is \"-\", no escape char is used and arguments containing',
            '-o': 'x Specifies \"x\", rather than double-quote, to be the open quote character, which is used if the -e- option is specified.',
            '-c': 'x Specifies \"x\" to be the close quote character.',
            '-p': 'n Specifies \"n\" to be the open quote character, as an integer.',
            '-d': 'n Specifies \"n\" to be the close quote character, as an integer.',
            '-m': 'x Specifies \"x\" to be a metachar. By default, no characters are considered metachars.',
            '-n': 'n Specifies \"n\" to be a metachar, as an integer.',
            '-f': 'n Specifies \"n\" to be the escape char for metachars, as an integer.',
            '-a': 'Specifies that all arguments are to be quoted. The default is that only arguments containing metacharacters are quoted.'
        },
        'examples': [
            'lessecho  # expand metacharacters',
            'lessecho -a  # Show all'
        ],
        'category': 'Other'
    },
    'lexgrog': {
        'desc': 'parse header information in man pages',
        'common_flags': {
            '-d': 'Print debugging information.',
            '--debug': 'Print debugging information.',
            '-m': 'Parse input as man page source files. This is the default if neither --man nor --cat is given.',
            '--man': 'Parse input as man page source files. This is the default if neither --man nor --cat is given.',
            '-c': 'Parse input as preformatted man pages (“cat pages”). --man and --cat may not be given simultaneously.',
            '--cat': 'Parse input as preformatted man pages (“cat pages”). --man and --cat may not be given simultaneously.',
            '-w': 'Display the name and description from the man page\'s header, as used by apropos and whatis. This is the default if neither --whatis nor',
            '--whatis': 'Display the name and description from the man page\'s header, as used by apropos and whatis. This is the default if neither --whatis nor',
            '--filters': 'Display the list of filters needed to preprocess the man page before formatting with nroff or troff.',
            '-f': 'Display the list of filters needed to preprocess the man page before formatting with nroff or troff.',
            '-E': 'encoding, --encoding encoding',
            '--usage': 'Print a short usage message and exit.',
            '-V': 'Display version information.',
            '--version': 'Display version information.'
        },
        'examples': [
            'lexgrog  # parse header information in man pages',
            'lexgrog --version  # Show version'
        ],
        'category': 'Other'
    },
    'link': {
        'desc': 'call the link function to create a link to a file',
        'common_flags': {
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'link  # call the link function to create a link to a file',
            'link --help  # Show help',
            'link --version  # Show version'
        ],
        'category': 'Other'
    },
    'localedef': {
        'desc': 'compile locale definition files',
        'common_flags': {
            '--add-to-archive': 'Add the compiledpath directories to the locale archive file. The directories should have been created by previous runs of localedef, using',
            '--no-archive': 'Do not use the locale archive file, instead create outputpath as a subdirectory in the same directory as the locale archive file, and create',
            '--delete-from-archive': 'Delete the named locales from the locale archive file.',
            '--list-archive': 'List the locales contained in the locale archive file.',
            '-f': 'charmapfile, --charmap=charmapfile',
            '-i': 'inputfile, --inputfile=inputfile',
            '-u': 'repertoirefile, --repertoire-map=repertoirefile',
            '-A': 'aliasfile, --alias-file=aliasfile',
            '--force': '-c Write the output files even if warnings were generated about the input file.',
            '--verbose': '-v Generate extra warnings about errors that are normally ignored.',
            '--big-endian': 'Generate big-endian output.',
            '--little-endian': 'Generate little-endian output.',
            '--no-hard-links': 'Do not create hard links between installed locales.',
            '--no-warnings': '=warnings',
            '--posix': 'Conform strictly to POSIX. Implies --verbose. This option currently has no other effect. POSIX conformance is assumed if the environment'
        },
        'examples': [
            'localedef  # compile locale definition files',
            'localedef --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'locate': {
        'desc': 'find files by name, quickly',
        'common_flags': {
            '-A': 'Ignored for compatibility with mlocate(1).',
            '--all': 'Ignored for compatibility with mlocate(1).',
            '-b': 'Match only against the file name portion of the path name, ie., the directory names will be excluded from the match (but still printed). This',
            '--basename': 'Match only against the file name portion of the path name, ie., the directory names will be excluded from the match (but still printed). This',
            '-c': 'Do not print each match. Instead, count them, and print out a total number at the end.',
            '--count': 'Do not print each match. Instead, count them, and print out a total number at the end.',
            '-d': 'DBPATH',
            '--database': 'DBPATH',
            '-e': 'Print only entries that refer to files existing at the time locate is run. Note that unlike mlocate(1), symlinks are not followed by default',
            '--existing': 'Print only entries that refer to files existing at the time locate is run. Note that unlike mlocate(1), symlinks are not followed by default',
            '-i': 'Do a case-insensitive match as given by the current locale (default is case-sensitive, byte-by-byte match). Note that plocate does not sup‐',
            '--ignore-case': 'Do a case-insensitive match as given by the current locale (default is case-sensitive, byte-by-byte match). Note that plocate does not sup‐',
            '-l': 'LIMIT',
            '--limit': 'LIMIT',
            '-N': 'Print entry names without quoting. Normally, plocate will escape special characters in filenames, so that they are safe for consumption by'
        },
        'examples': [
            'locate  # find files by name, quickly',
            'locate --all  # Show all'
        ],
        'category': 'Other'
    },
    'logger': {
        'desc': 'enter messages into the system log',
        'common_flags': {
            '-d': 'Use datagrams (UDP) only. By default the connection is tried to the syslog port defined in /etc/services, which is often 514.',
            '--udp': 'Use datagrams (UDP) only. By default the connection is tried to the syslog port defined in /etc/services, which is often 514.',
            '-e': 'Ignore empty lines when processing files. An empty line is defined to be a line without any characters. Thus a line consisting only of',
            '--skip-empty': 'Ignore empty lines when processing files. An empty line is defined to be a line without any characters. Thus a line consisting only of',
            '-f': 'file',
            '--file': 'file',
            '-i': 'Log the PID of the logger process with each line.',
            '--id': '[=id]',
            '--journald': '[=file]',
            '--msgid': 'msgid',
            '-n': 'server',
            '--server': 'server',
            '--no-act': 'Causes everything to be done except for writing the log message to the system log, and removing the connection to the journal. This option can',
            '--octet-count': 'Use the RFC 6587 <https://tools.ietf.org/html/rfc6587> octet counting framing method for sending messages. When this option is not used, the',
            '-P': 'port'
        },
        'examples': [
            'logger  # enter messages into the system log'
        ],
        'category': 'Other'
    },
    'login': {
        'desc': 'begin session on the system',
        'common_flags': {
            '-p': 'Used by getty(8) to tell login to preserve the environment. See also LOGIN_ENV_SAFELIST config file item.',
            '-f': 'Used to skip a login authentication. This option is usually used by the getty(8) autologin feature.',
            '-h': 'Display help text and exit.',
            '-H': 'Used by other servers (for example, telnetd(8)) to tell login that printing the hostname should be suppressed in the login: prompt. See also',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'login  # begin session on the system',
            'login -h  # Show help',
            'login --version  # Show version'
        ],
        'category': 'Other'
    },
    'loginctl': {
        'desc': 'Control the systemd login manager',
        'common_flags': {
            '-p': '=',
            '--property': '=',
            '--value': 'When showing session/user/seat properties, only print the value, and skip the property name and \"=\".',
            '-a': 'When showing session/user/seat properties, show all properties regardless of whether they are set or not.',
            '--all': 'When showing session/user/seat properties, show all properties regardless of whether they are set or not.',
            '-l': 'Do not ellipsize process tree entries.',
            '--full': 'Do not ellipsize process tree entries.',
            '--kill-whom': '=',
            '-s': '=',
            '--signal': '=',
            '-n': '=',
            '--lines': '=',
            '-o': '=',
            '--output': '=',
            '-H': '='
        },
        'examples': [
            'loginctl  # Control the systemd login manager',
            'loginctl -a  # Show all'
        ],
        'category': 'Other'
    },
    'look': {
        'desc': 'display lines beginning with a given string',
        'common_flags': {
            '-a': 'Use the alternative dictionary file.',
            '--alternative': 'Use the alternative dictionary file.',
            '-d': 'Use normal dictionary character set and order, i.e., only blanks and alphanumeric characters are compared. This is on by default if no file is',
            '--alphanum': 'Use normal dictionary character set and order, i.e., only blanks and alphanumeric characters are compared. This is on by default if no file is',
            '-f': 'Ignore the case of alphabetic characters. This is on by default if no file is specified.',
            '--ignore-case': 'Ignore the case of alphabetic characters. This is on by default if no file is specified.',
            '-t': 'character',
            '--terminate': 'character',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'look  # display lines beginning with a given string',
            'look -h  # Show help',
            'look --version  # Show version',
            'look -a  # Show all'
        ],
        'category': 'Other'
    },
    'lsattr': {
        'desc': 'list ext2/ext3/ext4 file attributes',
        'common_flags': {
            '-R': 'Recursively list attributes of directories and their contents.',
            '-V': 'Display the program version.',
            '-a': 'List all files in directories, including files that start with `.\'.',
            '-d': 'List directories like other files, rather than listing their contents.',
            '-l': 'Print the options using long names instead of single character abbreviations.',
            '-p': 'List the file\'s project number.',
            '-v': 'List the file\'s version/generation number.'
        },
        'examples': [
            'lsattr  # list ext2/ext3/ext4 file attributes',
            'lsattr -v  # Show version',
            'lsattr -v  # Verbose output',
            'lsattr -a  # Show all'
        ],
        'category': 'Other'
    },
    'lsb_release': {
        'desc': 'print distribution-specific information (minimal implementation).',
        'common_flags': {
            '-h': 'Show a help message with a list of options and exit.',
            '--help': 'Show a help message with a list of options and exit.',
            '-v': 'Show LSB modules this system supports.',
            '--version': 'Show LSB modules this system supports.',
            '-i': 'Show distributor ID.',
            '--id': 'Show distributor ID.',
            '-d': 'Show description of this distribution.',
            '--description': 'Show description of this distribution.',
            '-r': 'Show release number of this distribution.',
            '--release': 'Show release number of this distribution.',
            '-c': 'Show code name of this distribution.',
            '--codename': 'Show code name of this distribution.',
            '-a': 'Show all of the above information.',
            '--all': 'Show all of the above information.',
            '-s': 'Show requested information in short format.'
        },
        'examples': [
            'lsb_release  # print distribution-specific information (minimal i',
            'lsb_release -h  # Show help',
            'lsb_release -v  # Show version',
            'lsb_release -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'lscpu': {
        'desc': 'display information about the CPU architecture',
        'common_flags': {
            '-a': 'Include lines for online and offline CPUs in the output (default for -e). This option may only be specified together with option -e or -p.',
            '--all': 'Include lines for online and offline CPUs in the output (default for -e). This option may only be specified together with option -e or -p.',
            '-B': 'Print the sizes in bytes rather than in a human-readable format.',
            '--bytes': 'Print the sizes in bytes rather than in a human-readable format.',
            '-b': 'Limit the output to online CPUs (default for -p). This option may only be specified together with option -e or -p.',
            '--online': 'Limit the output to online CPUs (default for -p). This option may only be specified together with option -e or -p.',
            '-C': '=NAME,ONE-SIZE or --caches=NAME,ONE-SIZE.',
            '--caches': '[=list]',
            '-c': 'Limit the output to offline CPUs. This option may only be specified together with option -e or -p.',
            '--offline': 'Limit the output to offline CPUs. This option may only be specified together with option -e or -p.',
            '--hierarchic': '[=when]',
            '-e': '[=list]',
            '--extended': '[=list]',
            '-J': 'Use JSON output format for the default summary or extended output (see --extended). For backward compatibility, JSON output follows the default',
            '--json': 'Use JSON output format for the default summary or extended output (see --extended). For backward compatibility, JSON output follows the default'
        },
        'examples': [
            'lscpu  # display information about the CPU architecture',
            'lscpu -a  # Show all'
        ],
        'category': 'Other'
    },
    'lsipc': {
        'desc': 'show information on IPC facilities currently employed in the system',
        'common_flags': {
            '-i': 'id',
            '--id': 'id',
            '-N': 'name',
            '--name': 'name',
            '-g': 'Show system-wide usage and limits of IPC resources. This option may be combined with one of the three resource options: -m, -q or -s. The',
            '--global': 'Show system-wide usage and limits of IPC resources. This option may be combined with one of the three resource options: -m, -q or -s. The',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.',
            '-m': 'Write information about active System V shared memory segments.',
            '--shmems': 'Write information about active System V shared memory segments.',
            '-M': 'Write information about active POSIX shared memory segments.',
            '--posix-shmems': 'Write information about active POSIX shared memory segments.',
            '-q': 'Write information about active System V message queues.'
        },
        'examples': [
            'lsipc  # show information on IPC facilities currently emplo',
            'lsipc -h  # Show help',
            'lsipc --version  # Show version'
        ],
        'category': 'Other'
    },
    'lslogins': {
        'desc': 'display information about known users in the system',
        'common_flags': {
            '-a': 'Display data about the date of last password change and the account expiration date (see shadow(5) for more info). (Requires root privileges.)',
            '--acc-expiration': 'Display data about the date of last password change and the account expiration date (see shadow(5) for more info). (Requires root privileges.)',
            '--btmp-file': 'path',
            '-c': 'Separate info about each user with a colon instead of a newline.',
            '--colon-separate': 'Separate info about each user with a colon instead of a newline.',
            '-e': 'Output data in the format of NAME=VALUE. See also option --shell.',
            '--export': 'Output data in the format of NAME=VALUE. See also option --shell.',
            '-f': 'Display data about the users\' last failed login attempts.',
            '--failed': 'Display data about the users\' last failed login attempts.',
            '-G': 'Show information about supplementary groups.',
            '--supp-groups': 'Show information about supplementary groups.',
            '-g': 'groups',
            '--groups': 'groups',
            '-L': 'Display data containing information about the users\' last login sessions.',
            '--last': 'Display data containing information about the users\' last login sessions.'
        },
        'examples': [
            'lslogins  # display information about known users in the syste',
            'lslogins -a  # Show all'
        ],
        'category': 'Other'
    },
    'lsmem': {
        'desc': 'list the ranges of available memory with their online status',
        'common_flags': {
            '-a': 'List each individual memory block, instead of combining memory blocks with similar attributes.',
            '--all': 'List each individual memory block, instead of combining memory blocks with similar attributes.',
            '-b': 'Print the sizes in bytes rather than in a human-readable format.',
            '--bytes': 'Print the sizes in bytes rather than in a human-readable format.',
            '-J': 'Use JSON output format.',
            '--json': 'Use JSON output format.',
            '-n': 'Do not print a header line.',
            '--noheadings': 'Do not print a header line.',
            '-o': 'list',
            '--output': 'list',
            '--output-all': 'Output all available columns.',
            '-P': 'Produce output in the form of key=\"value\" pairs. All potentially unsafe value characters are hex-escaped (\\x<code>).',
            '--pairs': 'Produce output in the form of key=\"value\" pairs. All potentially unsafe value characters are hex-escaped (\\x<code>).',
            '-r': 'Produce output in raw format. All potentially unsafe characters are hex-escaped (\\x<code>).',
            '--raw': 'Produce output in raw format. All potentially unsafe characters are hex-escaped (\\x<code>).'
        },
        'examples': [
            'lsmem  # list the ranges of available memory with their onl',
            'lsmem -a  # Show all'
        ],
        'category': 'Other'
    },
    'lzcat': {
        'desc': 'Compress or decompress .xz and .lzma files',
        'common_flags': {
            '-z': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '--compress': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '-d': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--decompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--uncompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '-t': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '--test': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '-l': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '--list': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '-k': 'Don\'t delete the input files.',
            '--keep': 'Don\'t delete the input files.',
            '-f': 'This option has several effects:',
            '--force': 'This option has several effects:',
            '-c': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.',
            '--stdout': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.'
        },
        'examples': [
            'lzcat  # Compress or decompress .xz and .lzma files'
        ],
        'category': 'Other'
    },
    'lzma': {
        'desc': 'Compress or decompress .xz and .lzma files',
        'common_flags': {
            '-z': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '--compress': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '-d': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--decompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--uncompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '-t': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '--test': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '-l': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '--list': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '-k': 'Don\'t delete the input files.',
            '--keep': 'Don\'t delete the input files.',
            '-f': 'This option has several effects:',
            '--force': 'This option has several effects:',
            '-c': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.',
            '--stdout': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.'
        },
        'examples': [
            'lzma  # Compress or decompress .xz and .lzma files'
        ],
        'category': 'Other'
    },
    'make': {
        'desc': 'GNU Make utility to maintain groups of programs',
        'common_flags': {
            '-b': 'These options are ignored for compatibility with other versions of make.',
            '-m': 'These options are ignored for compatibility with other versions of make.',
            '-B': 'Unconditionally make all targets.',
            '--always-make': 'Unconditionally make all targets.',
            '-C': 'dir, --directory=dir',
            '-d': 'Print debugging information in addition to normal processing. The debugging information says which files are being considered for remaking,',
            '--debug': '[=FLAGS]',
            '-e': 'Give variables taken from the environment precedence over variables from makefiles.',
            '--environment-overrides': 'Give variables taken from the environment precedence over variables from makefiles.',
            '-E': 'string, --eval string',
            '-f': 'file, --file=file, --makefile=FILE',
            '-i': 'Ignore all errors in commands executed to remake files.',
            '--ignore-errors': 'Ignore all errors in commands executed to remake files.',
            '-I': 'dir, --include-dir=dir',
            '-j': '[jobs], --jobs[=jobs]'
        },
        'examples': [
            'make  # GNU Make utility to maintain groups of programs'
        ],
        'category': 'Other'
    },
    'make-first-existing-target': {
        'desc': 'runs make on one of several targets',
        'common_flags': {
            '-c': 'cmd'
        },
        'examples': [
            'make-first-existing-target  # runs make on one of several targets'
        ],
        'category': 'Other'
    },
    'man-recode': {
        'desc': 'convert manual pages to another encoding',
        'common_flags': {
            '-t': 'encoding, --to-code=encoding',
            '--suffix': '=suffix',
            '--in-place': 'Overwrite each input file with the output, after removing any compression extension.',
            '-q': 'Do not issue error messages when the page cannot be converted.',
            '--quiet': 'Do not issue error messages when the page cannot be converted.',
            '-d': 'Print debugging information.',
            '--debug': 'Print debugging information.',
            '-h': 'Print a help message and exit.',
            '--help': 'Print a help message and exit.',
            '-V': 'Display version information.',
            '--version': 'Display version information.'
        },
        'examples': [
            'man-recode  # convert manual pages to another encoding',
            'man-recode -h  # Show help',
            'man-recode --version  # Show version'
        ],
        'category': 'Other'
    },
    'manconv': {
        'desc': 'convert manual page from one encoding to another',
        'common_flags': {
            '-f': 'encodings, --from-code encodings',
            '-t': 'encoding, --to-code encoding',
            '-q': 'Do not issue error messages when the page cannot be converted.',
            '--quiet': 'Do not issue error messages when the page cannot be converted.',
            '-d': 'Print debugging information.',
            '--debug': 'Print debugging information.',
            '-h': 'Print a help message and exit.',
            '--help': 'Print a help message and exit.',
            '-V': 'Display version information.',
            '--version': 'Display version information.'
        },
        'examples': [
            'manconv  # convert manual page from one encoding to another',
            'manconv -h  # Show help',
            'manconv --version  # Show version'
        ],
        'category': 'Other'
    },
    'manpath': {
        'desc': 'determine search path for manual pages',
        'common_flags': {
            '-q': 'Do not issue warnings.',
            '--quiet': 'Do not issue warnings.',
            '-d': 'Print debugging information.',
            '--debug': 'Print debugging information.',
            '-c': 'Produce a catpath as opposed to a manpath. Once the manpath is determined, each path element is converted to its relative catpath.',
            '--catpath': 'Produce a catpath as opposed to a manpath. Once the manpath is determined, each path element is converted to its relative catpath.',
            '-g': 'Produce a manpath consisting of all paths named as \"global\" within the man-db configuration file.',
            '--global': 'Produce a manpath consisting of all paths named as \"global\" within the man-db configuration file.',
            '-m': 'system[,...], --systems=system[,...]',
            '-C': 'file, --config-file=file',
            '--usage': 'Print a short usage message and exit.',
            '-V': 'Display version information.',
            '--version': 'Display version information.'
        },
        'examples': [
            'manpath  # determine search path for manual pages',
            'manpath --version  # Show version'
        ],
        'category': 'Other'
    },
    'mawk': {
        'desc': 'pattern scanning and text processing language',
        'common_flags': {
            '-F': 'value sets the field separator, FS, to value.',
            '-f': 'file Program text is read from file instead of from the command line. Multiple -f options are allowed.',
            '-v': 'var=value assigns value to program variable var.',
            '-W': 'version'
        },
        'examples': [
            'mawk  # pattern scanning and text processing language',
            'mawk -v  # Show version',
            'mawk -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'mcookie': {
        'desc': 'generate magic cookies for xauth',
        'common_flags': {
            '-f': 'file',
            '--file': 'file',
            '-m': 'number',
            '--max-size': 'number',
            '-v': 'Inform where randomness originated, with amount of entropy read from each source.',
            '--verbose': 'Inform where randomness originated, with amount of entropy read from each source.',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'mcookie  # generate magic cookies for xauth',
            'mcookie -h  # Show help',
            'mcookie -v  # Show version',
            'mcookie -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'mdig': {
        'desc': 'DNS pipelined lookup utility',
        'common_flags': {
            '-f': 'This option makes mdig operate in batch mode by reading a list of lookup requests to process from the file filename. The file contains a num‐',
            '-h': 'This option causes mdig to print detailed help information, with the full list of options, and exit.',
            '-v': 'This option causes mdig to print the version number and exit.'
        },
        'examples': [
            'mdig  # DNS pipelined lookup utility',
            'mdig -h  # Show help',
            'mdig -v  # Show version',
            'mdig -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'memusage': {
        'desc': 'profile memory usage of a program',
        'common_flags': {
            '-n': 'name, --progname=name',
            '-p': 'file, --png=file',
            '-d': 'file, --data=file',
            '-u': 'Do not buffer output.',
            '--unbuffered': 'Do not buffer output.',
            '-b': 'size, --buffer=size',
            '--no-timer': 'Disable timer-based (SIGPROF) sampling of stack pointer value.',
            '-m': 'Also trace mmap(2), mremap(2), and munmap(2).',
            '--mmap': 'Also trace mmap(2), mremap(2), and munmap(2).',
            '--usage': 'Print a short usage message and exit.',
            '-V': 'Print version information and exit.',
            '--version': 'Print version information and exit.',
            '-t': 'Use time (rather than number of function calls) as the scale for the X axis.',
            '--time-based': 'Use time (rather than number of function calls) as the scale for the X axis.',
            '-T': 'Also draw a graph of total memory use.'
        },
        'examples': [
            'memusage  # profile memory usage of a program',
            'memusage --version  # Show version'
        ],
        'category': 'Other'
    },
    'memusagestat': {
        'desc': 'generate graphic from memory profiling data',
        'common_flags': {
            '-o': 'file, --output=file',
            '-s': 'string, --string=string',
            '-t': 'Use time (rather than number of function calls) as the scale for the X axis.',
            '--time': 'Use time (rather than number of function calls) as the scale for the X axis.',
            '-T': 'Also draw a graph of total memory consumption.',
            '--total': 'Also draw a graph of total memory consumption.',
            '-x': 'size, --x-size=size',
            '-y': 'size, --y-size=size',
            '--usage': 'Print a short usage message and exit.',
            '-V': 'Print version information and exit.',
            '--version': 'Print version information and exit.'
        },
        'examples': [
            'memusagestat  # generate graphic from memory profiling data',
            'memusagestat --version  # Show version'
        ],
        'category': 'Other'
    },
    'mkdir': {
        'desc': 'make directories',
        'common_flags': {
            '-v': 'print a message for each created directory',
            '--verbose': 'print a message for each created directory',
            '-Z': 'set SELinux security context of each created directory to the default type',
            '--context': '[=CTX]',
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'mkdir  # make directories',
            'mkdir --help  # Show help',
            'mkdir -v  # Show version',
            'mkdir -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'mkpasswd': {
        'desc': 'Overfeatured front end to crypt(3)',
        'common_flags': {
            '-S': 'STRING, --salt=STRING',
            '-R': 'NUMBER, --rounds=NUMBER',
            '-m': 'TYPE, --method=TYPE',
            '-5': 'Like --method=md5crypt.',
            '-P': 'NUM, --password-fd=NUM',
            '-s': 'Like --password-fd=0.',
            '--stdin': 'Like --password-fd=0.'
        },
        'examples': [
            'mkpasswd  # Overfeatured front end to crypt(3)'
        ],
        'category': 'Other'
    },
    'more': {
        'desc': 'display the contents of a file in a terminal',
        'common_flags': {
            '-d': 'Prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal',
            '--silent': 'Prompt with \"[Press space to continue, \'q\' to quit.]\", and display \"[Press \'h\' for instructions.]\" instead of ringing the bell when an illegal',
            '-l': 'Do not pause after any line containing a ^L (form feed).',
            '--logical': 'Do not pause after any line containing a ^L (form feed).',
            '-e': 'Exit on End-Of-File, enabled by default if POSIXLY_CORRECT environment variable is not set or if not executed on terminal.',
            '--exit-on-eof': 'Exit on End-Of-File, enabled by default if POSIXLY_CORRECT environment variable is not set or if not executed on terminal.',
            '-f': 'Count logical lines, rather than screen lines (i.e., long lines are not folded).',
            '--no-pause': 'Count logical lines, rather than screen lines (i.e., long lines are not folded).',
            '-p': 'Do not scroll. Instead, clear the whole screen and then display the text. Notice that this option is switched on automatically if the executable',
            '--print-over': 'Do not scroll. Instead, clear the whole screen and then display the text. Notice that this option is switched on automatically if the executable',
            '-c': 'Do not scroll. Instead, paint each screen from the top, clearing the remainder of each line as it is displayed.',
            '--clean-print': 'Do not scroll. Instead, paint each screen from the top, clearing the remainder of each line as it is displayed.',
            '-s': 'Squeeze multiple blank lines into one.',
            '--squeeze': 'Squeeze multiple blank lines into one.',
            '-u': 'Suppress underlining. This option is silently ignored as backwards compatibility.'
        },
        'examples': [
            'more  # display the contents of a file in a terminal'
        ],
        'category': 'Other'
    },
    'mountpoint': {
        'desc': 'see if a directory or file is a mountpoint',
        'common_flags': {
            '-d': 'Show the major/minor numbers of the device that is mounted on the given directory.',
            '--fs-devno': 'Show the major/minor numbers of the device that is mounted on the given directory.',
            '-q': 'Be quiet - don’t print anything.',
            '--quiet': 'Be quiet - don’t print anything.',
            '--nofollow': 'Do not follow symbolic link if it the last element of the directory path.',
            '-x': 'Show the major/minor numbers of the given blockdevice on standard output.',
            '--devno': 'Show the major/minor numbers of the given blockdevice on standard output.',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'mountpoint  # see if a directory or file is a mountpoint',
            'mountpoint -h  # Show help',
            'mountpoint --version  # Show version'
        ],
        'category': 'Other'
    },
    'mpstat': {
        'desc': 'Report processors related statistics.',
        'common_flags': {
            '-A': 'This option is equivalent to specifying -n -u -I ALL. This option also implies specifying -N ALL -P ALL unless these options are explicitly',
            '--dec': '={ 0 | 1 | 2 }',
            '-H': 'Also detect and display statistics for physically hotplugged vCPUs.',
            '-I': '{ keyword[,...] | ALL }',
            '-N': '{ node_list | ALL }',
            '-n': 'Report summary CPU statistics based on NUMA node placement. The following values are displayed:',
            '-o': 'JSON',
            '-P': '{ cpu_list | ALL }',
            '-T': 'Display topology elements in the CPU report (see option -u below). The following elements are displayed:',
            '-u': 'Report CPU utilization. The following values are displayed:',
            '-V': 'Print version number then exit.'
        },
        'examples': [
            'mpstat  # Report processors related statistics.',
            'mpstat -V  # Show version'
        ],
        'category': 'Other'
    },
    'msfconsole': {
        'desc': 'Metasploit Framework Console',
        'common_flags': {
            '-E': 'ENVIRONMENT',
            '--environment': 'ENVIRONMENT'
        },
        'examples': [
            'msfconsole  # Metasploit Framework Console'
        ],
        'category': 'Other'
    },
    'msfvenom': {
        'desc': 'Payload Generator and Encoder',
        'common_flags': {
            '-p': '[payload] Payload to use. Specify a \'-\' or stdin to use custom payloads',
            '--payload': '[payload] Payload to use. Specify a \'-\' or stdin to use custom payloads',
            '--payload-options': 'List the payload\'s standard options',
            '-l': '[module_type]',
            '--list': '[module_type]',
            '-n': '[length]',
            '--nopsled': '[length]',
            '-f': '[format]',
            '--format': '[format]',
            '--help-formats': 'List available formats',
            '-e': '[encoder]',
            '--encoder': '[encoder]',
            '-a': '[architecture]',
            '--arch': '[architecture]',
            '--platform': '[platform]'
        },
        'examples': [
            'msfvenom  # Payload Generator and Encoder',
            'msfvenom -a  # Show all'
        ],
        'category': 'Other'
    },
    'mt': {
        'desc': 'control magnetic tape drive operation',
        'common_flags': {
            '-f': '=device',
            '--file': '=device',
            '--rsh-command': '=command',
            '-V': 'Print the version number of mt.',
            '--version': 'Print the version number of mt.'
        },
        'examples': [
            'mt  # control magnetic tape drive operation',
            'mt --version  # Show version'
        ],
        'category': 'Other'
    },
    'mt-gnu': {
        'desc': 'control magnetic tape drive operation',
        'common_flags': {
            '-f': '=device',
            '--file': '=device',
            '--rsh-command': '=command',
            '-V': 'Print the version number of mt.',
            '--version': 'Print the version number of mt.'
        },
        'examples': [
            'mt-gnu  # control magnetic tape drive operation',
            'mt-gnu --version  # Show version'
        ],
        'category': 'Other'
    },
    'mtrace': {
        'desc': 'interpret the malloc trace log',
        'common_flags': {
            '--help': 'Print help and exit.',
            '--version': 'Print version information and exit.'
        },
        'examples': [
            'mtrace  # interpret the malloc trace log',
            'mtrace --help  # Show help',
            'mtrace --version  # Show version'
        ],
        'category': 'Other'
    },
    'namei': {
        'desc': 'follow a pathname until a terminal point is found',
        'common_flags': {
            '-l': 'Use the long listing format (same as -m -o -v).',
            '--long': 'Use the long listing format (same as -m -o -v).',
            '-m': 'Show the mode bits of each file type in the style of ls(1), for example \'rwxr-xr-x\'.',
            '--modes': 'Show the mode bits of each file type in the style of ls(1), for example \'rwxr-xr-x\'.',
            '-n': 'Don’t follow symlinks.',
            '--nosymlinks': 'Don’t follow symlinks.',
            '-o': 'Show owner and group name of each file.',
            '--owners': 'Show owner and group name of each file.',
            '-v': 'Vertically align the modes and owners.',
            '--vertical': 'Vertically align the modes and owners.',
            '-x': 'Show mountpoint directories with a \'D\' rather than a \'d\'.',
            '--mountpoints': 'Show mountpoint directories with a \'D\' rather than a \'d\'.',
            '-Z': 'Show security context of the file or \"?\" if not available. The support for security contexts is optional and does not have to be compiled to the',
            '--context': 'Show security context of the file or \"?\" if not available. The support for security contexts is optional and does not have to be compiled to the',
            '-h': 'Display help text and exit.'
        },
        'examples': [
            'namei  # follow a pathname until a terminal point is found',
            'namei -h  # Show help',
            'namei -v  # Show version',
            'namei -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'nano': {
        'desc': 'Nano\'s ANOther text editor, inspired by Pico',
        'common_flags': {
            '-A': 'Make the Home key smarter. When Home is pressed anywhere but at the very beginning of non-whitespace characters on a line, the cursor jumps',
            '--smarthome': 'Make the Home key smarter. When Home is pressed anywhere but at the very beginning of non-whitespace characters on a line, the cursor jumps',
            '-B': 'When saving a file, back up the previous version of it, using the current filename suffixed with a tilde (~).',
            '--backup': 'When saving a file, back up the previous version of it, using the current filename suffixed with a tilde (~).',
            '-C': 'directory, --backupdir=directory',
            '-D': 'For the interface, use bold instead of reverse video. This can be overridden for specific elements by setting the options titlecolor,',
            '--boldtext': 'For the interface, use bold instead of reverse video. This can be overridden for specific elements by setting the options titlecolor,',
            '-E': 'Convert each typed tab to spaces — to the number of spaces that a tab at that position would take up. (Note: pasted tabs are not converted.)',
            '--tabstospaces': 'Convert each typed tab to spaces — to the number of spaces that a tab at that position would take up. (Note: pasted tabs are not converted.)',
            '-F': 'Read a file into a new buffer by default.',
            '--multibuffer': 'Read a file into a new buffer by default.',
            '-G': 'Use vim-style file locking when editing files.',
            '--locking': 'Use vim-style file locking when editing files.',
            '-H': 'Save the last hundred search strings and replacement strings and executed commands, so they can be easily reused in later sessions.',
            '--historylog': 'Save the last hundred search strings and replacement strings and executed commands, so they can be easily reused in later sessions.'
        },
        'examples': [
            'nano  # Nano\'s ANOther text editor, inspired by Pico'
        ],
        'category': 'Other'
    },
    'nasm': {
        'desc': 'the Netwide Assembler, a portable 80x86 assembler',
        'common_flags': {
            '-a': 'Causes nasm to assemble the given input file without first applying the macro preprocessor.',
            '-D': '|-d macro[=value]',
            '-E': '|-e',
            '-f': 'format',
            '-F': 'format',
            '-g': 'format',
            '-h': 'f',
            '-I': '|-i directory',
            '-l': 'listfile',
            '-M': 'P',
            '-O': 'number',
            '-o': 'outfile',
            '-P': '|-p file',
            '-s': 'Causes nasm to send its error messages and/or help text to stdout instead of stderr.',
            '-t': 'Causes nasm to assemble in SciTech TASM compatible mode.'
        },
        'examples': [
            'nasm  # the Netwide Assembler, a portable 80x86 assembler',
            'nasm -h  # Show help',
            'nasm -a  # Show all'
        ],
        'category': 'Other'
    },
    'nawk': {
        'desc': 'pattern scanning and text processing language',
        'common_flags': {
            '-F': 'value sets the field separator, FS, to value.',
            '-f': 'file Program text is read from file instead of from the command line. Multiple -f options are allowed.',
            '-v': 'var=value assigns value to program variable var.',
            '-W': 'version'
        },
        'examples': [
            'nawk  # pattern scanning and text processing language',
            'nawk -v  # Show version',
            'nawk -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'nc': {
        'desc': 'TCP/IP swiss army knife',
        'common_flags': {
            '-c': 'string specify shell commands to exec after connect (use with caution). The string is passed to /bin/sh -c for execution. See the -e option',
            '-e': 'filename specify filename to exec after connect (use with caution). See the -c option for enhanced functionality.',
            '-g': 'gateway source-routing hop point[s], up to 8',
            '-G': 'num source-routing pointer: 4, 8, 12, ...',
            '-h': 'display help',
            '-i': 'secs delay interval for lines sent, ports scanned',
            '-l': 'listen mode, for inbound connects',
            '-n': 'numeric-only IP addresses, no DNS',
            '-o': 'file hex dump of traffic',
            '-p': 'port local port number (port numbers can be individual or ranges: lo-hi [inclusive])',
            '-q': 'seconds after EOF on stdin, wait the specified number of seconds and then quit. If seconds is negative, wait forever.',
            '-b': 'allow UDP broadcasts',
            '-r': 'randomize local and remote ports',
            '-s': 'addr local source address',
            '-t': 'enable telnet negotiation'
        },
        'examples': [
            'nc  # TCP/IP swiss army knife',
            'nc -h  # Show help'
        ],
        'category': 'Other'
    },
    'nc.traditional': {
        'desc': 'TCP/IP swiss army knife',
        'common_flags': {
            '-c': 'string specify shell commands to exec after connect (use with caution). The string is passed to /bin/sh -c for execution. See the -e option',
            '-e': 'filename specify filename to exec after connect (use with caution). See the -c option for enhanced functionality.',
            '-g': 'gateway source-routing hop point[s], up to 8',
            '-G': 'num source-routing pointer: 4, 8, 12, ...',
            '-h': 'display help',
            '-i': 'secs delay interval for lines sent, ports scanned',
            '-l': 'listen mode, for inbound connects',
            '-n': 'numeric-only IP addresses, no DNS',
            '-o': 'file hex dump of traffic',
            '-p': 'port local port number (port numbers can be individual or ranges: lo-hi [inclusive])',
            '-q': 'seconds after EOF on stdin, wait the specified number of seconds and then quit. If seconds is negative, wait forever.',
            '-b': 'allow UDP broadcasts',
            '-r': 'randomize local and remote ports',
            '-s': 'addr local source address',
            '-t': 'enable telnet negotiation'
        },
        'examples': [
            'nc.traditional  # TCP/IP swiss army knife',
            'nc.traditional -h  # Show help'
        ],
        'category': 'Other'
    },
    'ndisasm': {
        'desc': 'the Netwide Disassembler, an 80x86 binary file disassembler',
        'common_flags': {
            '-h': 'Causes ndisasm to exit immediately, after giving a summary of its invocation options.',
            '-r': '|-v',
            '-o': 'origin',
            '-s': 'sync-point',
            '-e': 'hdrlen',
            '-k': 'offset,length',
            '-a': '|-i',
            '-b': 'bits',
            '-u': 'Specifies 32-bit mode, more compactly than using ‘-b 32’.',
            '-p': 'vendor'
        },
        'examples': [
            'ndisasm  # the Netwide Disassembler, an 80x86 binary file dis',
            'ndisasm -h  # Show help',
            'ndisasm -a  # Show all'
        ],
        'category': 'Other'
    },
    'netcat': {
        'desc': 'TCP/IP swiss army knife',
        'common_flags': {
            '-c': 'string specify shell commands to exec after connect (use with caution). The string is passed to /bin/sh -c for execution. See the -e option',
            '-e': 'filename specify filename to exec after connect (use with caution). See the -c option for enhanced functionality.',
            '-g': 'gateway source-routing hop point[s], up to 8',
            '-G': 'num source-routing pointer: 4, 8, 12, ...',
            '-h': 'display help',
            '-i': 'secs delay interval for lines sent, ports scanned',
            '-l': 'listen mode, for inbound connects',
            '-n': 'numeric-only IP addresses, no DNS',
            '-o': 'file hex dump of traffic',
            '-p': 'port local port number (port numbers can be individual or ranges: lo-hi [inclusive])',
            '-q': 'seconds after EOF on stdin, wait the specified number of seconds and then quit. If seconds is negative, wait forever.',
            '-b': 'allow UDP broadcasts',
            '-r': 'randomize local and remote ports',
            '-s': 'addr local source address',
            '-t': 'enable telnet negotiation'
        },
        'examples': [
            'netcat  # TCP/IP swiss army knife',
            'netcat -h  # Show help'
        ],
        'category': 'Other'
    },
    'netkey-tool': {
        'desc': 'administrative utility for Netkey E4 cards',
        'common_flags': {
            '--help': 'Displays a short help message.',
            '-h': 'Displays a short help message.',
            '--pin': 'pin, -p pin',
            '--puk': 'pin, -u pin',
            '--pin0': 'pin, -0 pin',
            '--pin1': 'pin, -1 pin',
            '--reader': 'arg, -r arg',
            '-v': 'Causes netkey-tool to be more verbose. This options may be specified multiple times to increase verbosity.'
        },
        'examples': [
            'netkey-tool  # administrative utility for Netkey E4 cards',
            'netkey-tool -h  # Show help',
            'netkey-tool -v  # Show version',
            'netkey-tool -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'networkctl': {
        'desc': 'Query or modify the status of network links',
        'common_flags': {
            '-a': '--all',
            '-s': '--stats',
            '-l': 'Do not ellipsize the output.',
            '--full': 'Do not ellipsize the output.',
            '-n': '=',
            '--lines': '=',
            '--drop-in': '=NAME',
            '--no-reload': 'When used with edit, mask, or unmask, systemd-networkd.service(8) or systemd-udevd.service(8) will not be reloaded after the operation finishes.',
            '--runtime': 'When used with edit or mask, operate on the file under /run/ instead of /etc/.',
            '--stdin': 'When used with edit, the contents of the file will be read from standard input and the editor will not be launched. In this mode, the old',
            '--no-ask-password': 'Do not query the user for authentication for privileged operations.',
            '--json': '=MODE',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'networkctl  # Query or modify the status of network links',
            'networkctl -h  # Show help',
            'networkctl --version  # Show version',
            'networkctl -a  # Show all'
        ],
        'category': 'Other'
    },
    'newgrp': {
        'desc': 'log in to a new group',
        'common_flags': {
            '-c': '=command',
            '--command': '=command',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'newgrp  # log in to a new group',
            'newgrp -h  # Show help',
            'newgrp --version  # Show version'
        ],
        'category': 'Other'
    },
    'nisdomainname': {
        'desc': 'show or set the system\'s NIS/YP domain name',
        'common_flags': {
            '-a': 'Display the alias name of the host (if used). This option is deprecated and should not be used anymore.',
            '--alias': 'Display the alias name of the host (if used). This option is deprecated and should not be used anymore.',
            '-A': 'Displays all FQDNs of the machine. This option enumerates all configured network addresses on all configured network interfaces, and trans‐',
            '--all-fqdns': 'Displays all FQDNs of the machine. This option enumerates all configured network addresses on all configured network interfaces, and trans‐',
            '-b': 'Always set a hostname; this allows the file specified by -F to be non-existent or empty, in which case the default hostname localhost will be',
            '--boot': 'Always set a hostname; this allows the file specified by -F to be non-existent or empty, in which case the default hostname localhost will be',
            '-d': 'Display the name of the DNS domain. Don\'t use the command domainname to get the DNS domain name because it will show the NIS domain name and',
            '--domain': 'Display the name of the DNS domain. Don\'t use the command domainname to get the DNS domain name because it will show the NIS domain name and',
            '-f': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '--fqdn': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '--long': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '-F': 'filename',
            '--file': 'filename',
            '-i': 'Display the network address(es) of the host name. Note that this works only if the host name can be resolved. Avoid using this option; use',
            '--ip-address': 'Display the network address(es) of the host name. Note that this works only if the host name can be resolved. Avoid using this option; use'
        },
        'examples': [
            'nisdomainname  # show or set the system\'s NIS/YP domain name',
            'nisdomainname -a  # Show all'
        ],
        'category': 'Other'
    },
    'nm': {
        'desc': 'list symbols from object files',
        'common_flags': {
            '-A': '-o',
            '--print-file-name': 'Precede each symbol by the name of the input file (or archive member) in which it was found, rather than identifying the input file once only,',
            '-a': '--debug-syms',
            '-B': 'The same as --format=bsd (for compatibility with the MIPS nm).',
            '-C': '--demangle[=style]',
            '--no-demangle': 'Do not demangle low-level symbol names. This is the default.',
            '--recurse-limit': '--no-recurse-limit',
            '--recursion-limit': '--no-recursion-limit',
            '-D': '--dynamic',
            '-f': 'format',
            '--format': '=format',
            '-g': '--extern-only',
            '-h': '--help',
            '--ifunc-chars': '=CHARS',
            '-l': '--line-numbers'
        },
        'examples': [
            'nm  # list symbols from object files',
            'nm -h  # Show help',
            'nm -a  # Show all'
        ],
        'category': 'Other'
    },
    'nmap': {
        'desc': 'Network exploration tool and security / port scanner',
        'common_flags': {
            '--ttl': '<val>: Set IP time-to-live field',
            '--spoof-mac': '<mac address/prefix/vendor name>: Spoof your MAC address',
            '--badsum': ': Send packets with a bogus TCP/UDP/SCTP checksum',
            '-o': 'A <basename>: Output in the three major formats at once',
            '-v': ': Increase verbosity level (use -vv or more for greater effect)',
            '-d': ': Increase debugging level (use -dd or more for greater effect)',
            '--reason': ': Display the reason a port is in a particular state',
            '--open': ': Only show open (or possibly open) ports',
            '--packet-trace': ': Show all packets sent and received',
            '--iflist': ': Print host interfaces and routes (for debugging)',
            '--append-output': ': Append to rather than clobber specified output files',
            '--resume': '<filename>: Resume an aborted scan',
            '--noninteractive': ': Disable runtime interactions via keyboard',
            '--stylesheet': '<path/URL>: XSL stylesheet to transform XML output to HTML',
            '--webxml': ': Reference stylesheet from Nmap.Org for more portable XML'
        },
        'examples': [
            'nmap  # Network exploration tool and security / port scann',
            'nmap -v  # Show version',
            'nmap -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'nohup': {
        'desc': 'run a command immune to hangups, with output to a non-tty',
        'common_flags': {
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'nohup  # run a command immune to hangups, with output to a ',
            'nohup --help  # Show help',
            'nohup --version  # Show version'
        ],
        'category': 'Other'
    },
    'npa-tool': {
        'desc': 'displays information on the German eID card (neuer Personalausweis, nPA).',
        'common_flags': {
            '--help': 'Print help and exit.',
            '-h': 'Print help and exit.',
            '--version': 'Print version and exit.',
            '-V': 'Print version and exit.',
            '--reader': 'arg, -r arg',
            '--verbose': 'Causes npa-tool to be more verbose. Specify this flag several times to be more verbose.',
            '-v': 'Causes npa-tool to be more verbose. Specify this flag several times to be more verbose.',
            '--pin': '[STRING], -p [STRING]',
            '--puk': '[STRING], -u [STRING]',
            '--can': '[STRING], -c [STRING]',
            '--mrz': '[STRING], -m [STRING]',
            '--env': 'Specify whether to use environment variables PIN, PUK, CAN, MRZ, and NEWPIN. You may want to clean your environment before enabling this.',
            '--new-pin': '[STRING], -N [STRING]',
            '--resume': 'Resume eID-PIN (uses CAN to activate last retry). (default=off)',
            '-R': 'Resume eID-PIN (uses CAN to activate last retry). (default=off)'
        },
        'examples': [
            'npa-tool  # displays information on the German eID card (neuer',
            'npa-tool -h  # Show help',
            'npa-tool -v  # Show version',
            'npa-tool -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'nping': {
        'desc': 'Network packet generation tool / ping utility',
        'common_flags': {
            '--ip-options': '<hex string> : Set IP options',
            '--mtu': '<size> : Set MTU. Packets get fragmented if MTU is',
            '-6': ': Use IP version 6.',
            '--IPv6': ': Use IP version 6.',
            '--dest-ip': ': Set destination IP address (used as an',
            '--hop-limit': ': Set hop limit (same as IPv4 TTL).',
            '--traffic-class': '<class> : : Set traffic class.',
            '--flow': '<label> : Set flow label.',
            '--dest-mac': '<mac> : Set destination mac address. (Disables',
            '--source-mac': '<mac> : Set source MAC address.',
            '--ether-type': '<type> : Set EtherType value.',
            '--data': '<hex string> : Include a custom payload.',
            '--data-string': '<text> : Include a custom ASCII text.',
            '--data-length': '<len> : Include len random bytes as payload.',
            '--echo-client': '<passphrase> : Run Nping in client mode.'
        },
        'examples': [
            'nping  # Network packet generation tool / ping utility'
        ],
        'category': 'Other'
    },
    'nsenter': {
        'desc': 'run program in different namespaces',
        'common_flags': {
            '-a': 'Enter all namespaces of the target process by the default /proc/[pid]/ns/* namespace paths. The default paths to the target process namespaces',
            '--all': 'Enter all namespaces of the target process by the default /proc/[pid]/ns/* namespace paths. The default paths to the target process namespaces',
            '-t': 'PID',
            '--target': 'PID',
            '-m': '[=file]',
            '--mount': '[=file]',
            '-u': '[=file]',
            '--uts': '[=file]',
            '-i': '[=file]',
            '--ipc': '[=file]',
            '-n': '[=file]',
            '--net': '[=file]',
            '-N': 'fd',
            '--net-socket': 'fd',
            '-p': '[=file]'
        },
        'examples': [
            'nsenter  # run program in different namespaces',
            'nsenter -a  # Show all'
        ],
        'category': 'Other'
    },
    'nsupdate': {
        'desc': 'dynamic DNS update utility',
        'common_flags': {
            '-4': 'This option sets use of IPv4 only.',
            '-6': 'This option sets use of IPv6 only.',
            '-A': 'tlscafile',
            '-S': '.',
            '-C': 'Overrides the default resolv.conf file. This is only intended for testing.',
            '-d': 'This option sets debug mode, which provides tracing information about the update requests that are made and the replies received from the',
            '-D': 'This option sets extra debug mode.',
            '-E': 'tlscertfile',
            '-g': 'This option enables standard GSS-TSIG mode.',
            '-H': 'tlshostname',
            '-i': 'This option forces interactive mode, even when standard input is not a terminal.',
            '-k': 'keyfile',
            '-K': 'tlskeyfile',
            '-l': 'This option sets local-host only mode, which sets the server address to localhost (disabling the server so that the server address cannot be',
            '-L': 'level'
        },
        'examples': [
            'nsupdate  # dynamic DNS update utility'
        ],
        'category': 'Other'
    },
    'objcopy': {
        'desc': 'copy and translate object files',
        'common_flags': {
            '-I': 'bfdname',
            '--input-target': '=bfdname',
            '-O': 'bfdname',
            '--output-target': '=bfdname',
            '-F': 'bfdname',
            '--target': '=bfdname',
            '-B': 'bfdarch',
            '--binary-architecture': '=bfdarch',
            '-j': 'sectionpattern',
            '--only-section': '=.text.* --only-section=!.text.foo',
            '-R': 'sectionpattern',
            '--remove-section': '=.text.* --remove-section=!.text.foo',
            '--keep-section': '=sectionpattern',
            '--remove-relocations': '=.text.* --remove-relocations=!.text.foo',
            '--strip-section-headers': 'Strip section header This option is specific to ELF files. Implies --strip-all and --merge-notes.'
        },
        'examples': [
            'objcopy  # copy and translate object files'
        ],
        'category': 'Other'
    },
    'objdump': {
        'desc': 'display information from object files',
        'common_flags': {
            '-a': 'must be given.',
            '-d': 'must be given.',
            '-D': 'must be given.',
            '-e': 'must be given.',
            '-f': 'must be given.',
            '-g': 'must be given.',
            '-G': 'must be given.',
            '-h': 'must be given.',
            '-H': 'must be given.',
            '-p': 'must be given.',
            '-P': 'must be given.',
            '-r': 'must be given.',
            '-R': 'must be given.',
            '-s': 'must be given.',
            '-S': 'must be given.'
        },
        'examples': [
            'objdump  # display information from object files',
            'objdump -h  # Show help',
            'objdump -r -f  # Recursive and forced',
            'objdump -a  # Show all'
        ],
        'category': 'Other'
    },
    'oid2name': {
        'desc': 'resolve OIDs and file nodes in a PostgreSQL data directory',
        'common_flags': {
            '-f': 'filenode',
            '--filenode': '=filenode',
            '-i': '--indexes',
            '-o': 'oid',
            '--oid': '=oid',
            '-q': '--quiet',
            '-s': '--tablespaces',
            '-S': '--system-objects',
            '-t': 'tablename_pattern',
            '--table': '=tablename_pattern',
            '-V': '--version',
            '-x': '--extended',
            '--help': 'Show help about oid2name command line arguments, and exit.',
            '-d': 'database',
            '--dbname': '=database'
        },
        'examples': [
            'oid2name  # resolve OIDs and file nodes in a PostgreSQL data d',
            'oid2name --help  # Show help',
            'oid2name -V  # Show version'
        ],
        'category': 'Other'
    },
    'openpgp-tool': {
        'desc': 'utility for accessing visible data OpenPGP smart cards and compatible tokens',
        'common_flags': {
            '--card-info': 'Show card information.',
            '-C': 'Show card information.',
            '--del-key': 'arg',
            '--do': 'arg, -d arg',
            '--erase': 'Erase (i.e. reset) the card.',
            '-E': 'Erase (i.e. reset) the card.',
            '--exec': 'prog, -x prog',
            '--gen-key': 'arg, -G arg',
            '--help': 'Print help message on screen.',
            '-h': 'Print help message on screen.',
            '--key-info': 'Show information of keys on the card.',
            '-K': 'Show information of keys on the card.',
            '--key-type': 'keytype, -t keytype',
            '--pin': 'pin',
            '--pretty': 'Print values in pretty format.'
        },
        'examples': [
            'openpgp-tool  # utility for accessing visible data OpenPGP smart c',
            'openpgp-tool -h  # Show help'
        ],
        'category': 'Other'
    },
    'opensc-asn1': {
        'desc': 'parse ASN.1 data',
        'common_flags': {
            '--help': 'Print help and exit.',
            '-h': 'Print help and exit.',
            '--version': 'Print version and exit.',
            '-V': 'Print version and exit.'
        },
        'examples': [
            'opensc-asn1  # parse ASN.1 data',
            'opensc-asn1 -h  # Show help',
            'opensc-asn1 --version  # Show version'
        ],
        'category': 'Other'
    },
    'opensc-explorer': {
        'desc': 'generic interactive utility for accessing smart card and similar security token functions',
        'common_flags': {
            '--card-driver': 'driver, -c driver',
            '--mf': 'path, -m path',
            '--reader': 'arg, -r arg',
            '--verbose': 'Cause opensc-explorer to be more verbose. Specify this flag several times to enable debug output in the opensc library.',
            '-v': 'Cause opensc-explorer to be more verbose. Specify this flag several times to enable debug output in the opensc library.',
            '--wait': 'Wait for a card to be inserted.',
            '-w': 'Wait for a card to be inserted.'
        },
        'examples': [
            'opensc-explorer  # generic interactive utility for accessing smart ca',
            'opensc-explorer -v  # Show version',
            'opensc-explorer -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'opensc-notify': {
        'desc': 'monitor smart card events and send notifications',
        'common_flags': {
            '--help': 'Print help and exit.',
            '-h': 'Print help and exit.',
            '--version': 'Print version and exit.',
            '-V': 'Print version and exit.',
            '--title': '[STRING], -t [STRING]',
            '--message': '[STRING], -m [STRING]',
            '--notify-card-inserted': 'See notify_card_inserted in opensc.conf (default=off).',
            '-I': 'See notify_card_inserted in opensc.conf (default=off).',
            '--notify-card-removed': 'See notify_card_removed in opensc.conf (default=off).',
            '-R': 'See notify_card_removed in opensc.conf (default=off).',
            '--notify-pin-good': 'See notify_pin_good in opensc.conf (default=off).',
            '-G': 'See notify_pin_good in opensc.conf (default=off).',
            '--notify-pin-bad': 'See notify_pin_bad in opensc.conf (default=off).',
            '-B': 'See notify_pin_bad in opensc.conf (default=off).'
        },
        'examples': [
            'opensc-notify  # monitor smart card events and send notifications',
            'opensc-notify -h  # Show help',
            'opensc-notify --version  # Show version'
        ],
        'category': 'Other'
    },
    'opensc-tool': {
        'desc': 'generic smart card utility',
        'common_flags': {
            '--version': 'Print the OpenSC package release version.',
            '--atr': 'Print the Answer To Reset (ATR) of the card. Output is in hex byte format',
            '-a': 'Print the Answer To Reset (ATR) of the card. Output is in hex byte format',
            '--card-driver': 'driver, -c driver',
            '--list-algorithms': ',',
            '--info': 'Print information about OpenSC, such as version and enabled components.',
            '-i': 'Print information about OpenSC, such as version and enabled components.',
            '--list-drivers': 'List all installed card drivers.',
            '-D': 'List all installed card drivers.',
            '--list-files': 'Recursively list all files stored on card.',
            '-f': 'Recursively list all files stored on card.',
            '--list-readers': 'List all configured readers.',
            '-l': 'List all configured readers.',
            '--name': 'Print the name of the inserted card (driver).',
            '-n': 'Print the name of the inserted card (driver).'
        },
        'examples': [
            'opensc-tool  # generic smart card utility',
            'opensc-tool --version  # Show version',
            'opensc-tool -a  # Show all'
        ],
        'category': 'Other'
    },
    'pager': {
        'desc': 'display the contents of a file in a terminal',
        'common_flags': {
            '-a': 'or --search-skip-screen',
            '-A': 'or --SEARCH-SKIP-SCREEN',
            '-b': 'n or --buffers=n',
            '-B': 'or --auto-buffers',
            '-c': 'or --clear-screen',
            '-C': 'or --CLEAR-SCREEN',
            '-d': 'or --dumb',
            '-D': 'xcolor or --color=xcolor',
            '-e': 'or --quit-at-eof',
            '-E': 'or --QUIT-AT-EOF',
            '-f': 'or --force',
            '-F': 'or --quit-if-one-screen',
            '-g': 'or --hilite-search',
            '-G': 'or --HILITE-SEARCH',
            '-h': 'n or --max-back-scroll=n'
        },
        'examples': [
            'pager  # display the contents of a file in a terminal',
            'pager -h  # Show help',
            'pager -a  # Show all'
        ],
        'category': 'Other'
    },
    'passwd': {
        'desc': 'change user password',
        'common_flags': {
            '-a': 'This option can be used only with -S and causes show status for all users.',
            '--all': 'This option can be used only with -S and causes show status for all users.',
            '-d': 'Delete a user\'s password (make it empty). This is a quick way to disable a password for an account. It will set the named account passwordless.',
            '--delete': 'Delete a user\'s password (make it empty). This is a quick way to disable a password for an account. It will set the named account passwordless.',
            '-e': 'Immediately expire an account\'s password. This in effect can force a user to change their password at the user\'s next login.',
            '--expire': 'Immediately expire an account\'s password. This in effect can force a user to change their password at the user\'s next login.',
            '-h': 'Display help message and exit.',
            '--help': 'Display help message and exit.',
            '-i': 'INACTIVE',
            '--inactive': 'INACTIVE',
            '-k': 'Indicate password change should be performed only for expired authentication tokens (passwords). The user wishes to keep their non-expired',
            '--keep-tokens': 'Indicate password change should be performed only for expired authentication tokens (passwords). The user wishes to keep their non-expired',
            '-l': 'Lock the password of the named account. This option disables a password by changing it to a value which matches no possible encrypted value (it',
            '--lock': 'Lock the password of the named account. This option disables a password by changing it to a value which matches no possible encrypted value (it',
            '-n': 'MIN_DAYS'
        },
        'examples': [
            'passwd  # change user password',
            'passwd -h  # Show help',
            'passwd -a  # Show all'
        ],
        'category': 'Other'
    },
    'patch': {
        'desc': 'apply a diff file to an original',
        'common_flags': {
            '-b': 'or --backup',
            '--backup-if-mismatch': 'Back up a file if the patch does not match the file exactly and if backups are not otherwise requested. This is the default unless patch is con‐',
            '--no-backup-if-mismatch': 'Do not back up a file if the patch does not match the file exactly and if backups are not otherwise requested. This is the default if patch is',
            '-B': 'pref or --prefix=pref',
            '--binary': 'Write all files in binary mode, except for standard output and /dev/tty. When reading, disable the heuristic for transforming CRLF line endings',
            '-c': 'or --context',
            '-d': 'dir or --directory=dir',
            '-D': 'define or --ifdef=define',
            '--dry-run': 'Print the results of applying the patches without actually changing any files.',
            '-e': 'or --ed',
            '-E': 'or --remove-empty-files',
            '-f': 'or --force',
            '-F': 'num or --fuzz=num',
            '-g': 'num or --get=num',
            '--help': 'Print a summary of options and exit.'
        },
        'examples': [
            'patch  # apply a diff file to an original',
            'patch --help  # Show help'
        ],
        'category': 'Other'
    },
    'perlbug': {
        'desc': 'how to submit bug reports on Perl',
        'common_flags': {
            '-a': 'Address to send the report to instead of saving to a file.',
            '-b': 'Body of the report. If not included on the command line, or in a file with -f, you will get a chance to edit the report.',
            '-C': 'Don\'t send copy to administrator when sending report by mail.',
            '-c': 'Address to send copy of report to when sending report by mail. Defaults to the address of the local perl administrator (recorded when perl',
            '-d': 'Data mode (the default if you redirect or pipe output). This prints out your configuration data, without saving or mailing anything. You',
            '-e': 'Editor to use.',
            '-f': 'File containing the body of the report. Use this to quickly send a prepared report.',
            '-F': 'File to output the results to. Defaults to perlbug.rep.',
            '-h': 'Prints a brief summary of the options.',
            '-o': 'kay As -ok except it will report on older systems.',
            '-n': 'okay As -nok except it will report on older systems.',
            '-p': 'The names of one or more patch files or other text attachments to be included with the report. Multiple files must be separated with',
            '-r': 'Your return address. The program will ask you to confirm its default if you don\'t use this option.',
            '-S': 'Save or send the report without asking for confirmation.',
            '-s': 'Subject to include with the report. You will be prompted if you don\'t supply one on the command line.'
        },
        'examples': [
            'perlbug  # how to submit bug reports on Perl',
            'perlbug -h  # Show help',
            'perlbug -r -f  # Recursive and forced',
            'perlbug -a  # Show all'
        ],
        'category': 'Other'
    },
    'perlivp': {
        'desc': 'Perl Installation Verification Procedure',
        'common_flags': {
            '-h': 'help',
            '-p': 'print preface',
            '-v': 'verbose'
        },
        'examples': [
            'perlivp  # Perl Installation Verification Procedure',
            'perlivp -h  # Show help',
            'perlivp -v  # Show version',
            'perlivp -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'perlthanks': {
        'desc': 'how to submit bug reports on Perl',
        'common_flags': {
            '-a': 'Address to send the report to instead of saving to a file.',
            '-b': 'Body of the report. If not included on the command line, or in a file with -f, you will get a chance to edit the report.',
            '-C': 'Don\'t send copy to administrator when sending report by mail.',
            '-c': 'Address to send copy of report to when sending report by mail. Defaults to the address of the local perl administrator (recorded when perl',
            '-d': 'Data mode (the default if you redirect or pipe output). This prints out your configuration data, without saving or mailing anything. You',
            '-e': 'Editor to use.',
            '-f': 'File containing the body of the report. Use this to quickly send a prepared report.',
            '-F': 'File to output the results to. Defaults to perlbug.rep.',
            '-h': 'Prints a brief summary of the options.',
            '-o': 'kay As -ok except it will report on older systems.',
            '-n': 'okay As -nok except it will report on older systems.',
            '-p': 'The names of one or more patch files or other text attachments to be included with the report. Multiple files must be separated with',
            '-r': 'Your return address. The program will ask you to confirm its default if you don\'t use this option.',
            '-S': 'Save or send the report without asking for confirmation.',
            '-s': 'Subject to include with the report. You will be prompted if you don\'t supply one on the command line.'
        },
        'examples': [
            'perlthanks  # how to submit bug reports on Perl',
            'perlthanks -h  # Show help',
            'perlthanks -r -f  # Recursive and forced',
            'perlthanks -a  # Show all'
        ],
        'category': 'Other'
    },
    'pg_amcheck': {
        'desc': 'checks for corruption in one or more PostgreSQL databases',
        'common_flags': {
            '-a': '--all',
            '-d': 'pattern',
            '--database': '=pattern',
            '-D': 'pattern',
            '--exclude-database': '=pattern',
            '-i': 'pattern',
            '--index': '=pattern',
            '-I': 'pattern',
            '--exclude-index': '=pattern',
            '-r': 'pattern',
            '--relation': '=pattern',
            '-R': 'pattern',
            '--exclude-relation': '=pattern',
            '-s': 'pattern',
            '--schema': '=pattern'
        },
        'examples': [
            'pg_amcheck  # checks for corruption in one or more PostgreSQL da',
            'pg_amcheck -a  # Show all'
        ],
        'category': 'Other'
    },
    'pg_archivecleanup': {
        'desc': 'clean up PostgreSQL WAL archive files',
        'common_flags': {
            '-b': '--clean-backup-history',
            '-d': '--debug',
            '-n': '--dry-run',
            '-V': '--version',
            '-x': 'extension',
            '--strip-extension': '=extension',
            '--help': 'Show help about pg_archivecleanup command line arguments, and exit.'
        },
        'examples': [
            'pg_archivecleanup  # clean up PostgreSQL WAL archive files',
            'pg_archivecleanup --help  # Show help',
            'pg_archivecleanup -V  # Show version'
        ],
        'category': 'Other'
    },
    'pg_backupcluster': {
        'desc': 'simple pg_basebackup and pg_dump front-end',
        'common_flags': {
            '-c': '--checkpoint=spread|fast',
            '-k': '--keep-on-error',
            '-v': '--verbose'
        },
        'examples': [
            'pg_backupcluster  # simple pg_basebackup and pg_dump front-end',
            'pg_backupcluster -v  # Show version',
            'pg_backupcluster -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'pg_basebackup': {
        'desc': 'take a base backup of a PostgreSQL cluster',
        'common_flags': {
            '-D': 'directory',
            '--pgdata': '=directory',
            '-F': 'format',
            '--format': '=format',
            '-i': 'old_manifest_file',
            '--incremental': '=old_manifest_file',
            '-R': '--write-recovery-conf',
            '-t': 'target',
            '--target': '=target',
            '-T': 'olddir=newdir',
            '--tablespace-mapping': '=olddir=newdir',
            '--waldir': '=waldir',
            '-X': 'method',
            '--wal-method': '=method',
            '-z': '--gzip'
        },
        'examples': [
            'pg_basebackup  # take a base backup of a PostgreSQL cluster'
        ],
        'category': 'Other'
    },
    'pg_buildext': {
        'desc': 'Build and install a PostgreSQL extension',
        'common_flags': {
            '-c': 'io arg',
            '-s': 'Passed to pg_virtualenv when running installcheck.',
            '-m': 'arg'
        },
        'examples': [
            'pg_buildext  # Build and install a PostgreSQL extension'
        ],
        'category': 'Other'
    },
    'pg_checksums': {
        'desc': 'enable, disable or check data checksums in a PostgreSQL database cluster',
        'common_flags': {
            '-D': 'directory',
            '--pgdata': '=directory',
            '-c': '--check',
            '-d': '--disable',
            '-e': '--enable',
            '-f': 'filenode',
            '--filenode': '=filenode',
            '-N': '--no-sync',
            '-P': '--progress',
            '--sync-method': '=method',
            '-v': '--verbose',
            '-V': '--version',
            '--help': 'Show help about pg_checksums command line arguments, and exit.'
        },
        'examples': [
            'pg_checksums  # enable, disable or check data checksums in a Postg',
            'pg_checksums --help  # Show help',
            'pg_checksums -v  # Show version',
            'pg_checksums -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'pg_combinebackup': {
        'desc': 'reconstruct a full backup from an incremental backup and dependent backups',
        'common_flags': {
            '-d': '--debug',
            '-n': '--dry-run',
            '-N': '--no-sync',
            '-o': 'outputdir',
            '--output': '=outputdir',
            '-T': 'olddir=newdir',
            '--tablespace-mapping': '=olddir=newdir',
            '--clone': 'Use efficient file cloning (also known as “reflinks” on some systems) instead of copying files to the new data directory, which can result in',
            '--copy': 'Perform regular file copy. This is the default. (See also --copy-file-range and --clone.)',
            '--copy-file-range': 'Use the copy_file_range system call for efficient copying. On some file systems this gives results similar to --clone, sharing physical disk',
            '--manifest-checksums': '=algorithm',
            '--no-manifest': 'Disables generation of a backup manifest. If this option is not specified, a backup manifest for the reconstructed backup will be written to the',
            '--sync-method': '=method',
            '-V': '--version',
            '--help': 'Shows help about pg_combinebackup command line arguments, and exits.'
        },
        'examples': [
            'pg_combinebackup  # reconstruct a full backup from an incremental back',
            'pg_combinebackup --help  # Show help',
            'pg_combinebackup -V  # Show version'
        ],
        'category': 'Other'
    },
    'pg_conftool': {
        'desc': 'read and edit PostgreSQL cluster configuration files',
        'common_flags': {
            '-b': 'Format boolean value as on or off (not for \"show all\").',
            '--boolean': 'Format boolean value as on or off (not for \"show all\").',
            '-s': 'Show only the value (instead of key = value pair).',
            '--short': 'Show only the value (instead of key = value pair).',
            '-v': 'Verbose output.',
            '--verbose': 'Verbose output.',
            '--help': 'Print help.'
        },
        'examples': [
            'pg_conftool  # read and edit PostgreSQL cluster configuration fil',
            'pg_conftool --help  # Show help',
            'pg_conftool -v  # Show version',
            'pg_conftool -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'pg_createcluster': {
        'desc': 'create a new PostgreSQL cluster',
        'common_flags': {
            '-u': 'user, --user=user',
            '-g': 'group, --group=group',
            '-d': 'dir, --datadir=dir',
            '-s': 'dir, --socketdir=dir',
            '-l': 'path, --logfile=path',
            '--locale': '=locale',
            '--lc-collate': '=locale',
            '--lc-ctype': '=locale',
            '--lc-messages': '=locale',
            '--lc-monetary': '=locale',
            '--lc-numeric': '=locale',
            '--lc-time': '=locale',
            '-e': 'encoding, --encoding=encoding',
            '-p': 'port, --port=port',
            '-q': '--quiet --no-status'
        },
        'examples': [
            'pg_createcluster  # create a new PostgreSQL cluster'
        ],
        'category': 'Other'
    },
    'pg_createsubscriber': {
        'desc': 'convert a physical replica into a new logical replica',
        'common_flags': {
            '-d': 'dbname',
            '--database': '=dbname',
            '-D': 'directory',
            '--pgdata': '=directory',
            '-n': '--dry-run',
            '-p': 'port',
            '--subscriber-port': '=port',
            '-P': 'connstr',
            '--publisher-server': '=connstr',
            '-s': 'dir',
            '--socketdir': '=dir',
            '-t': 'seconds',
            '--recovery-timeout': '=seconds',
            '-U': 'username',
            '--subscriber-username': '=username'
        },
        'examples': [
            'pg_createsubscriber  # convert a physical replica into a new logical repl'
        ],
        'category': 'Other'
    },
    'pg_ctl': {
        'desc': 'initialize, start, stop, or control a PostgreSQL server',
        'common_flags': {
            '-c': '--core-files',
            '-D': 'datadir',
            '--pgdata': '=datadir',
            '-l': 'filename',
            '--log': '=filename',
            '-m': 'mode',
            '--mode': '=mode',
            '-o': 'initdb-options',
            '--options': '=initdb-options',
            '-p': 'path',
            '-s': '--silent',
            '-t': 'seconds',
            '--timeout': '=seconds',
            '-V': '--version',
            '-w': '--wait'
        },
        'examples': [
            'pg_ctl  # initialize, start, stop, or control a PostgreSQL s',
            'pg_ctl -V  # Show version'
        ],
        'category': 'Other'
    },
    'pg_ctlcluster': {
        'desc': 'start/stop/restart/reload a PostgreSQL cluster',
        'common_flags': {
            '-f': '|--force',
            '-m': '|--mode [smart|fast|immediate]',
            '--foreground': 'Start postgres in foreground, without daemonizing via pg_ctl.',
            '--stdlog': 'When --foreground is in use, redirect stderr to the standard logfile in /var/log/postgresql/. (Default when not run in foreground.)',
            '--skip-systemctl-redirect': 'When running as root, pg_ctlcluster redirects actions to systemctl so running clusters are properly supervised by systemd. This option skips the',
            '--bindir': 'directory',
            '-o': '|--options option'
        },
        'examples': [
            'pg_ctlcluster  # start/stop/restart/reload a PostgreSQL cluster'
        ],
        'category': 'Other'
    },
    'pg_dump': {
        'desc': 'extract a PostgreSQL database into a script file or other archive file',
        'common_flags': {
            '-a': '--data-only',
            '-b': '--large-objects',
            '--blobs': '(deprecated)',
            '-B': '--no-large-objects',
            '--no-blobs': '(deprecated)',
            '-c': '--clean',
            '-C': '--create',
            '-e': 'pattern',
            '--extension': '=pattern',
            '-E': 'encoding',
            '--encoding': '=encoding',
            '-f': 'file',
            '--file': '=file',
            '-F': 'format',
            '--format': '=format'
        },
        'examples': [
            'pg_dump  # extract a PostgreSQL database into a script file o',
            'pg_dump -a  # Show all'
        ],
        'category': 'Other'
    },
    'pg_dumpall': {
        'desc': 'extract a PostgreSQL database cluster into a script file',
        'common_flags': {
            '-a': '--data-only',
            '-c': '--clean',
            '-E': 'encoding',
            '--encoding': '=encoding',
            '-f': 'filename',
            '--file': '=filename',
            '--filter': '=filename',
            '--exclude-database': '. To read from STDIN, use - as the filename. The --filter option can be specified in conjunction with --exclude-database for',
            '-g': '--globals-only',
            '-O': '--no-owner',
            '-r': '--roles-only',
            '-s': '--schema-only',
            '-S': 'username',
            '--superuser': '=username',
            '-t': '--tablespaces-only'
        },
        'examples': [
            'pg_dumpall  # extract a PostgreSQL database cluster into a scrip',
            'pg_dumpall -r -f  # Recursive and forced',
            'pg_dumpall -a  # Show all'
        ],
        'category': 'Other'
    },
    'pg_isready': {
        'desc': 'check the connection status of a PostgreSQL server',
        'common_flags': {
            '-d': 'dbname',
            '--dbname': '=dbname',
            '-h': 'hostname',
            '--host': '=hostname',
            '-p': 'port',
            '--port': '=port',
            '-q': '--quiet',
            '-t': 'seconds',
            '--timeout': '=seconds',
            '-U': 'username',
            '--username': '=username',
            '-V': '--version',
            '--help': 'Show help about pg_isready command line arguments, and exit.'
        },
        'examples': [
            'pg_isready  # check the connection status of a PostgreSQL server',
            'pg_isready -h  # Show help',
            'pg_isready -V  # Show version'
        ],
        'category': 'Other'
    },
    'pg_lsclusters': {
        'desc': 'show information about all PostgreSQL clusters',
        'common_flags': {
            '-h': 'Do not print the column header line.',
            '--no-header': 'Do not print the column header line.',
            '-j': 'Output information in JSON format. Needs JSON.pm installed. (Debian package: libjson-perl)',
            '--json': 'Output information in JSON format. Needs JSON.pm installed. (Debian package: libjson-perl)',
            '-s': 'Include start.conf information in status column.',
            '--start-conf': 'Include start.conf information in status column.',
            '--help': 'Print usage help.'
        },
        'examples': [
            'pg_lsclusters  # show information about all PostgreSQL clusters',
            'pg_lsclusters -h  # Show help'
        ],
        'category': 'Other'
    },
    'pg_receivewal': {
        'desc': 'stream write-ahead logs from a PostgreSQL server',
        'common_flags': {
            '--synchronous': 'must be specified to flush WAL data in real time. Since pg_receivewal does not apply WAL, you should not allow it to become a'
        },
        'examples': [
            'pg_receivewal  # stream write-ahead logs from a PostgreSQL server'
        ],
        'category': 'Other'
    },
    'pg_recvlogical': {
        'desc': 'control PostgreSQL logical decoding streams',
        'common_flags': {
            '--create-slot': 'and --start can be specified together. --drop-slot cannot be combined with another action.',
            '--drop-slot': 'Drop the replication slot with the name specified by --slot, then exit.',
            '--start': 'Begin streaming changes from the logical replication slot specified by --slot, continuing until terminated by a signal. If the server side',
            '-E': 'lsn',
            '--endpos': '=lsn',
            '-f': 'filename',
            '--file': '=filename',
            '-F': 'interval_seconds',
            '--fsync-interval': '=interval_seconds',
            '-I': 'lsn',
            '--startpos': '=lsn',
            '--if-not-exists': 'Do not error out when --create-slot is specified and a slot with the specified name already exists.',
            '-n': '--no-loop',
            '-o': 'name[=value]',
            '--option': '=name[=value]'
        },
        'examples': [
            'pg_recvlogical  # control PostgreSQL logical decoding streams'
        ],
        'category': 'Other'
    },
    'pg_resetwal': {
        'desc': 'reset the write-ahead log and other control information of a PostgreSQL database cluster',
        'common_flags': {
            '-D': 'datadir',
            '--pgdata': '=datadir',
            '-f': '--force',
            '-n': '--dry-run',
            '-V': '--version',
            '--help': 'Show help, then exit.',
            '-c': 'xid,xid',
            '--commit-timestamp-ids': '=xid,xid',
            '-e': 'xid_epoch',
            '--epoch': '=xid_epoch',
            '-l': 'walfile',
            '--next-wal-file': '=walfile',
            '-m': 'mxid,mxid',
            '--multixact-ids': '=mxid,mxid',
            '-o': 'oid'
        },
        'examples': [
            'pg_resetwal  # reset the write-ahead log and other control inform',
            'pg_resetwal --help  # Show help',
            'pg_resetwal -V  # Show version'
        ],
        'category': 'Other'
    },
    'pg_restore': {
        'desc': 'restore a PostgreSQL database from an archive file created by pg_dump',
        'common_flags': {
            '-a': '--data-only',
            '-c': '--clean',
            '-C': '--create',
            '-d': 'dbname',
            '--dbname': '=dbname',
            '-e': '--exit-on-error',
            '-f': 'filename',
            '--file': '=filename',
            '--filter': '=filename',
            '-F': 'format',
            '--format': '=format',
            '-I': 'index',
            '--index': '=index',
            '-j': 'number-of-jobs',
            '--jobs': '=number-of-jobs'
        },
        'examples': [
            'pg_restore  # restore a PostgreSQL database from an archive file',
            'pg_restore -a  # Show all'
        ],
        'category': 'Other'
    },
    'pg_restorecluster': {
        'desc': 'Restore from a pg_backupcluster backup',
        'common_flags': {
            '-d': '--datadir DIR',
            '-p': '--port N',
            '-s': '--start',
            '--archive': 'Configure cluster for recovery from WAL archive. This sets restore_command to retrieve WAL files from backup/../wal.',
            '--pitr': 'TIMESTAMP',
            '--recovery-target-time': 'TIMESTAMP',
            '--wal-archive': 'DIR'
        },
        'examples': [
            'pg_restorecluster  # Restore from a pg_backupcluster backup'
        ],
        'category': 'Other'
    },
    'pg_rewind': {
        'desc': 'synchronize a PostgreSQL data directory with another data directory that was forked from it',
        'common_flags': {
            '-D': 'directory',
            '--target-pgdata': '=directory',
            '--source-pgdata': '=directory',
            '--source-server': '=connstr',
            '-R': '--write-recovery-conf',
            '-n': '--dry-run',
            '-N': '--no-sync',
            '-P': '--progress',
            '-c': '--restore-target-wal',
            '--config-file': '=filename',
            '--debug': 'Print verbose debugging output that is mostly useful for developers debugging pg_rewind.',
            '--no-ensure-shutdown': 'pg_rewind requires that the target server is cleanly shut down before rewinding. By default, if the target server is not shut down cleanly,',
            '--sync-method': '=method',
            '-V': '--version',
            '--help': 'Show help, then exit.'
        },
        'examples': [
            'pg_rewind  # synchronize a PostgreSQL data directory with anoth',
            'pg_rewind --help  # Show help',
            'pg_rewind -V  # Show version'
        ],
        'category': 'Other'
    },
    'pg_test_fsync': {
        'desc': 'determine fastest wal_sync_method for PostgreSQL',
        'common_flags': {
            '-f': '--filename',
            '-s': '--secs-per-test',
            '-V': '--version',
            '--help': 'Show help about pg_test_fsync command line arguments, and exit.'
        },
        'examples': [
            'pg_test_fsync  # determine fastest wal_sync_method for PostgreSQL',
            'pg_test_fsync --help  # Show help',
            'pg_test_fsync -V  # Show version'
        ],
        'category': 'Other'
    },
    'pg_test_timing': {
        'desc': 'measure timing overhead',
        'common_flags': {
            '-d': 'duration',
            '--duration': '=duration',
            '-V': '--version',
            '--help': 'Show help about pg_test_timing command line arguments, and exit.'
        },
        'examples': [
            'pg_test_timing  # measure timing overhead',
            'pg_test_timing --help  # Show help',
            'pg_test_timing -V  # Show version'
        ],
        'category': 'Other'
    },
    'pg_upgrade': {
        'desc': 'upgrade a PostgreSQL server instance',
        'common_flags': {
            '-b': 'bindir',
            '--old-bindir': '=bindir',
            '-B': 'bindir',
            '--new-bindir': '=bindir',
            '-c': '--check',
            '-d': 'configdir',
            '--old-datadir': '=configdir',
            '-D': 'configdir',
            '--new-datadir': '=configdir',
            '-j': 'njobs',
            '--jobs': '=njobs',
            '-k': '--link',
            '-N': '--no-sync',
            '-o': 'options',
            '--old-options': 'options'
        },
        'examples': [
            'pg_upgrade  # upgrade a PostgreSQL server instance'
        ],
        'category': 'Other'
    },
    'pg_upgradecluster': {
        'desc': 'upgrade an existing PostgreSQL cluster to a new major version.',
        'common_flags': {
            '-v': 'newversion',
            '--logfile': 'filel',
            '--locale': '=locale',
            '--lc-collate': '=locale',
            '--lc-ctype': '=locale',
            '--lc-messages': '=locale',
            '--lc-monetary': '=locale',
            '--lc-numeric': '=locale',
            '--lc-time': '=locale',
            '-m': '=dump|upgrade|link|clone',
            '--method': '=dump|upgrade|link|clone',
            '-k': 'In pg_upgrade mode, use hard links instead of copying files to the new cluster. This option is merely passed on to pg_upgrade. See',
            '--link': 'In pg_upgrade mode, use hard links instead of copying files to the new cluster. This option is merely passed on to pg_upgrade. See',
            '--clone': 'In pg_upgrade mode, use efficient file cloning (also known as \"reflinks\" on some systems) instead of copying files to the new cluster. This',
            '-j': 'In pg_upgrade mode, number of simultaneous processes to use. This option is passed on to pg_upgrade. See pg_upgrade(1) for details. It is also'
        },
        'examples': [
            'pg_upgradecluster  # upgrade an existing PostgreSQL cluster to a new ma',
            'pg_upgradecluster -v  # Show version',
            'pg_upgradecluster -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'pg_verifybackup': {
        'desc': 'verify the integrity of a base backup of a PostgreSQL cluster',
        'common_flags': {
            '-e': '--exit-on-error',
            '-i': 'path',
            '--ignore': '=path',
            '-m': 'path',
            '--manifest-path': '=path',
            '-n': '--no-parse-wal',
            '-P': '--progress',
            '-q': '--quiet',
            '-s': '--skip-checksums',
            '-w': 'path',
            '--wal-directory': '=path',
            '-V': '--version',
            '--help': 'Show help about pg_verifybackup command line arguments, and exit.'
        },
        'examples': [
            'pg_verifybackup  # verify the integrity of a base backup of a Postgre',
            'pg_verifybackup --help  # Show help',
            'pg_verifybackup -V  # Show version'
        ],
        'category': 'Other'
    },
    'pg_virtualenv': {
        'desc': 'Create a throw-away PostgreSQL environment for running regression tests',
        'common_flags': {
            '-a': 'Use all PostgreSQL server versions installed.',
            '-v': 'version ...',
            '-c': 'pg_createcluster options',
            '-i': 'initdb options',
            '-o': 'guc=value',
            '-p': 'package',
            '-s': 'Launch a shell inside the virtual environment when command fails.',
            '-t': 'Install clusters in a temporary directory, even when running as root.',
            '-h': 'Show program help.'
        },
        'examples': [
            'pg_virtualenv  # Create a throw-away PostgreSQL environment for run',
            'pg_virtualenv -h  # Show help',
            'pg_virtualenv -v  # Show version',
            'pg_virtualenv -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'pg_waldump': {
        'desc': 'display a human-readable rendering of the write-ahead log of a PostgreSQL database cluster',
        'common_flags': {
            '-b': '--bkp-details',
            '-B': 'block',
            '--block': '=block',
            '-e': 'end',
            '--end': '=end',
            '-f': '--follow',
            '-F': 'fork',
            '--fork': '=fork',
            '-n': 'limit',
            '--limit': '=limit',
            '-p': 'path',
            '--path': '=path',
            '-q': '--quiet',
            '-r': 'rmgr',
            '--rmgr': '=rmgr'
        },
        'examples': [
            'pg_waldump  # display a human-readable rendering of the write-ah',
            'pg_waldump -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'pg_walsummary': {
        'desc': 'print contents of WAL summary files',
        'common_flags': {
            '-i': '--individual',
            '-q': '--quiet',
            '-V': '--version',
            '--help': 'Shows help about pg_walsummary command line arguments, and exits.'
        },
        'examples': [
            'pg_walsummary  # print contents of WAL summary files',
            'pg_walsummary --help  # Show help',
            'pg_walsummary -V  # Show version'
        ],
        'category': 'Other'
    },
    'pgbench': {
        'desc': 'run a benchmark test on PostgreSQL',
        'common_flags': {
            '---------------------------------': 'pgbench_branches 1'
        },
        'examples': [
            'pgbench  # run a benchmark test on PostgreSQL'
        ],
        'category': 'Other'
    },
    'pgrep': {
        'desc': 'look up, signal, or wait for processes based on name and other attributes',
        'common_flags': {
            '-s': 'ignal',
            '--signal': 'signal',
            '-c': 'Suppress normal output; instead print a count of matching processes. When count does not match anything, e.g. returns zero, the command will',
            '--count': 'Suppress normal output; instead print a count of matching processes. When count does not match anything, e.g. returns zero, the command will',
            '-d': 'delimiter',
            '--delimiter': 'delimiter',
            '-e': 'Display name and PID of the process being killed. (pkill only.)',
            '--echo': 'Display name and PID of the process being killed. (pkill only.)',
            '-f': 'The pattern is normally only matched against the process name. When -f is set, the full command line is used.',
            '--full': 'The pattern is normally only matched against the process name. When -f is set, the full command line is used.',
            '-g': 'pgrp,...',
            '--pgroup': 'pgrp,...',
            '-G': 'gid,...',
            '--group': 'gid,...',
            '-i': 'Match processes case-insensitively.'
        },
        'examples': [
            'pgrep  # look up, signal, or wait for processes based on na'
        ],
        'category': 'Other'
    },
    'pic': {
        'desc': 'compile pictures for troff or TeX',
        'common_flags': {
            '--help': 'displays a usage message, while -v and --version show version information; all exit afterward.',
            '-c': 'Be more compatible with tpic; implies -t. Lines beginning with \\ are not passed through transparently. Lines beginning with . are passed',
            '-C': 'Recognize .PS, .PE, .PF, and .PY even when followed by a character other than space or newline.',
            '-n': 'Don\'t use groff extensions to the troff drawing commands. Specify this option if a postprocessor you\'re using doesn\'t support these exten‐',
            '-S': 'Operate in safer mode; sh commands are ignored. This mode, enabled by default, can be useful when operating on untrustworthy input.',
            '-t': 'Produce TeX output.',
            '-U': 'Operate in unsafe mode; sh commands are interpreted.',
            '-z': 'In TeX mode, draw dots using zero-length lines.',
            '-D': 'Draw all lines using the \\D escape sequence. GNU pic always does this.',
            '-T': 'dev Generate output for the troff device dev. This is unnecessary because the troff output generated by GNU pic is device-independent.'
        },
        'examples': [
            'pic  # compile pictures for troff or TeX',
            'pic --help  # Show help'
        ],
        'category': 'Other'
    },
    'pico': {
        'desc': 'Nano\'s ANOther text editor, inspired by Pico',
        'common_flags': {
            '-A': 'Make the Home key smarter. When Home is pressed anywhere but at the very beginning of non-whitespace characters on a line, the cursor jumps',
            '--smarthome': 'Make the Home key smarter. When Home is pressed anywhere but at the very beginning of non-whitespace characters on a line, the cursor jumps',
            '-B': 'When saving a file, back up the previous version of it, using the current filename suffixed with a tilde (~).',
            '--backup': 'When saving a file, back up the previous version of it, using the current filename suffixed with a tilde (~).',
            '-C': 'directory, --backupdir=directory',
            '-D': 'For the interface, use bold instead of reverse video. This can be overridden for specific elements by setting the options titlecolor,',
            '--boldtext': 'For the interface, use bold instead of reverse video. This can be overridden for specific elements by setting the options titlecolor,',
            '-E': 'Convert each typed tab to spaces — to the number of spaces that a tab at that position would take up. (Note: pasted tabs are not converted.)',
            '--tabstospaces': 'Convert each typed tab to spaces — to the number of spaces that a tab at that position would take up. (Note: pasted tabs are not converted.)',
            '-F': 'Read a file into a new buffer by default.',
            '--multibuffer': 'Read a file into a new buffer by default.',
            '-G': 'Use vim-style file locking when editing files.',
            '--locking': 'Use vim-style file locking when editing files.',
            '-H': 'Save the last hundred search strings and replacement strings and executed commands, so they can be easily reused in later sessions.',
            '--historylog': 'Save the last hundred search strings and replacement strings and executed commands, so they can be easily reused in later sessions.'
        },
        'examples': [
            'pico  # Nano\'s ANOther text editor, inspired by Pico'
        ],
        'category': 'Other'
    },
    'pidstat': {
        'desc': 'Report statistics for Linux tasks.',
        'common_flags': {
            '-C': 'comm',
            '-d': 'Report I/O statistics (kernels 2.6.20 and later only). The following values may be displayed:',
            '--dec': '={ 0 | 1 | 2 }',
            '-e': 'program args',
            '-G': 'process_name',
            '-H': 'Display timestamp in seconds since the epoch.',
            '-h': 'Display all activities horizontally on a single line, with no average statistics at the end of the report. This is intended to make it easier',
            '--human': 'Print sizes in human readable format (e.g. 1.0k, 1.2M, etc.) The units displayed with this option supersede any other default units (e.g.',
            '-I': 'In an SMP environment, indicate that tasks CPU usage (as displayed by option -u) should be divided by the total number of processors.',
            '-l': 'Display the process command name and all its arguments.',
            '-p': '{ pid[,...] | SELF | ALL }',
            '-R': 'Report realtime priority and scheduling policy information. The following values may be displayed:',
            '-r': 'Report page faults and memory utilization.',
            '-s': 'Report stack utilization. The following values may be displayed:',
            '-T': '{ TASK | CHILD | ALL }'
        },
        'examples': [
            'pidstat  # Report statistics for Linux tasks.',
            'pidstat -h  # Show help'
        ],
        'category': 'Other'
    },
    'pidwait': {
        'desc': 'look up, signal, or wait for processes based on name and other attributes',
        'common_flags': {
            '-s': 'ignal',
            '--signal': 'signal',
            '-c': 'Suppress normal output; instead print a count of matching processes. When count does not match anything, e.g. returns zero, the command will',
            '--count': 'Suppress normal output; instead print a count of matching processes. When count does not match anything, e.g. returns zero, the command will',
            '-d': 'delimiter',
            '--delimiter': 'delimiter',
            '-e': 'Display name and PID of the process being killed. (pkill only.)',
            '--echo': 'Display name and PID of the process being killed. (pkill only.)',
            '-f': 'The pattern is normally only matched against the process name. When -f is set, the full command line is used.',
            '--full': 'The pattern is normally only matched against the process name. When -f is set, the full command line is used.',
            '-g': 'pgrp,...',
            '--pgroup': 'pgrp,...',
            '-G': 'gid,...',
            '--group': 'gid,...',
            '-i': 'Match processes case-insensitively.'
        },
        'examples': [
            'pidwait  # look up, signal, or wait for processes based on na'
        ],
        'category': 'Other'
    },
    'piv-tool': {
        'desc': 'smart card utility for HSPD-12 PIV cards',
        'common_flags': {
            '--serial': 'Print the card serial number derived from the CHUID object, if any. Output is in hex byte format.',
            '--name': 'Print the name of the inserted card (driver)',
            '-n': 'Print the name of the inserted card (driver)',
            '--admin': 'argument, -A argument',
            '--genkey': 'argument, -G argument',
            '--object': 'ContainerID, -O ContainerID',
            '--cert': 'ref, -C ref',
            '--compresscert': 'ref, -Z ref',
            '--out': 'file, -o file',
            '--in': 'file, -i file',
            '--key-slots-discovery': 'file',
            '--send-apdu': 'apdu, -s apdu',
            '--reader': 'arg, -r arg',
            '--wait': 'Wait for a card to be inserted',
            '-w': 'Wait for a card to be inserted'
        },
        'examples': [
            'piv-tool  # smart card utility for HSPD-12 PIV cards'
        ],
        'category': 'Other'
    },
    'pkcs11-register': {
        'desc': 'Simple tool to install PKCS#11 modules to known applications.',
        'common_flags': {
            '--help': 'Print help message on screen.',
            '-h': 'Print help message on screen.',
            '--version': 'Print the OpenSC package release version.',
            '-V': 'Print the OpenSC package release version.',
            '--module': 'filename, -m filename',
            '--skip-chrome': 'Don\'t install module for Chrome browser. By default, the tool attempts to install the module for Chrome browser.',
            '--skip-firefox': 'Don\'t install module for Firefox browser. By default, the tool attempts to install the module for Firefox browser.',
            '--skip-thunderbird': 'Don\'t install module for Thunderbird mail client. By default, the tool attempts to install the module for Thunderbird mail client.',
            '--skip-seamonkey': 'Don\'t install module for Seamonkey. By default, the tool attempts to install the module Seamonkey.'
        },
        'examples': [
            'pkcs11-register  # Simple tool to install PKCS#11 modules to known ap',
            'pkcs11-register -h  # Show help',
            'pkcs11-register --version  # Show version'
        ],
        'category': 'Other'
    },
    'pkcs11-tool': {
        'desc': 'utility for managing and using PKCS #11 security tokens',
        'common_flags': {
            '--attr-from': 'filename',
            '--change-pin': 'Change the user PIN on the token',
            '-c': 'Change the user PIN on the token',
            '--unlock-pin': 'Unlock User PIN (without --login unlock in logged in session; otherwise --login-type has to be \'context-specific\').',
            '--hash': 'Hash some data.',
            '-h': 'Hash some data.',
            '--hash-algorithm': 'mechanism',
            '--id': 'id, -d id',
            '--init-pin': 'Initializes the user PIN. This option differs from --change-pin in that it sets the user PIN for the first time. Once set, the user PIN can be',
            '--init-token': 'Initialize a token: set the token label as well as a Security Officer PIN (the label must be specified using --label).',
            '--input-file': 'filename, -i filename',
            '--keypairgen': 'Generate a new key pair (public and private pair.)',
            '-k': 'Generate a new key pair (public and private pair.)',
            '--keygen': 'Generate a new key.',
            '--key-type': 'specification'
        },
        'examples': [
            'pkcs11-tool  # utility for managing and using PKCS #11 security t',
            'pkcs11-tool -h  # Show help'
        ],
        'category': 'Other'
    },
    'pkcs15-crypt': {
        'desc': 'perform crypto operations using PKCS#15 smart cards',
        'common_flags': {
            '--version': ',',
            '--aid': 'aid',
            '--decipher': 'Decrypt the contents of the file specified by the --input option. The result of the decryption operation is written to the file specified by the',
            '-c': 'Decrypt the contents of the file specified by the --input option. The result of the decryption operation is written to the file specified by the',
            '--output': 'file, -o file',
            '--input': 'file, -i file',
            '--key': 'id, -k id',
            '--pin': 'pin, -p pin',
            '--pkcs1': 'By default, pkcs15-crypt assumes that input data has been padded to the correct length (i.e. when computing an RSA signature using a 1024 bit',
            '--raw': 'Outputs raw 8 bit data.',
            '-R': 'Outputs raw 8 bit data.',
            '--reader': 'arg, -r arg',
            '--md5': '--sha-1 --sha-224 --sha-256 --sha-384 --sha-512',
            '--sign': 'Perform digital signature operation on the data read from a file specified using the --input option. By default, the contents of the file are',
            '-s': 'Perform digital signature operation on the data read from a file specified using the --input option. By default, the contents of the file are'
        },
        'examples': [
            'pkcs15-crypt  # perform crypto operations using PKCS#15 smart card',
            'pkcs15-crypt --version  # Show version'
        ],
        'category': 'Other'
    },
    'pkcs15-init': {
        'desc': 'smart card personalization utility',
        'common_flags': {
            '--version': ',',
            '--card-profile': 'name, -c name',
            '--create-pkcs15': 'This tells pkcs15-init to create a PKCS #15 structure on the card, and initialize any PINs.',
            '-C': 'This tells pkcs15-init to create a PKCS #15 structure on the card, and initialize any PINs.',
            '--serial': 'SERIAL',
            '--erase-card': 'This will erase the card prior to creating the PKCS #15 structure, if the card supports it. If the card does not support erasing, pkcs15-init',
            '-E': 'This will erase the card prior to creating the PKCS #15 structure, if the card supports it. If the card does not support erasing, pkcs15-init',
            '--erase-application': 'AID',
            '--generate-key': 'keyspec, -G keyspec',
            '--pin': 'pin, --puk puk, --so-pin sopin, --so-puk sopuk',
            '--no-so-pin': ',',
            '--profile': 'name, -p name',
            '--secret-key-algorithm': 'keyspec,',
            '--store-certificate': 'filename, -X filename',
            '--store-pin': 'Store a new PIN/PUK on the card.'
        },
        'examples': [
            'pkcs15-init  # smart card personalization utility',
            'pkcs15-init --version  # Show version'
        ],
        'category': 'Other'
    },
    'pkcs15-tool': {
        'desc': 'utility for manipulating PKCS #15 data structures on smart cards and similar security tokens',
        'common_flags': {
            '--version': 'Print the OpenSC package release version.',
            '--aid': 'aid',
            '--auth-id': 'id, -a id',
            '--change-pin': 'Changes a PIN or PUK stored on the token. User authentication is required for this operation.',
            '--dump': 'List all card objects.',
            '-D': 'List all card objects.',
            '--list-info': 'List card objects.',
            '--list-applications': 'List the on-card PKCS#15 applications.',
            '--list-certificates': 'List all certificates stored on the token.',
            '-c': 'List all certificates stored on the token.',
            '--list-data-objects': 'List all data objects stored on the token. For some cards the PKCS#15 attributes of the private data objects are protected for reading and need',
            '-C': 'List all data objects stored on the token. For some cards the PKCS#15 attributes of the private data objects are protected for reading and need',
            '--list-keys': 'List all private keys stored on the token. General information about each private key is listed (eg. key name, id and algorithm). Actual private',
            '-k': 'List all private keys stored on the token. General information about each private key is listed (eg. key name, id and algorithm). Actual private',
            '--list-secret-keys': 'List all secret (symmetric) keys stored on the token. General information about each secret key is listed (eg. key name, id and algorithm).'
        },
        'examples': [
            'pkcs15-tool  # utility for manipulating PKCS #15 data structures ',
            'pkcs15-tool --version  # Show version'
        ],
        'category': 'Other'
    },
    'pkill': {
        'desc': 'look up, signal, or wait for processes based on name and other attributes',
        'common_flags': {
            '-s': 'ignal',
            '--signal': 'signal',
            '-c': 'Suppress normal output; instead print a count of matching processes. When count does not match anything, e.g. returns zero, the command will',
            '--count': 'Suppress normal output; instead print a count of matching processes. When count does not match anything, e.g. returns zero, the command will',
            '-d': 'delimiter',
            '--delimiter': 'delimiter',
            '-e': 'Display name and PID of the process being killed. (pkill only.)',
            '--echo': 'Display name and PID of the process being killed. (pkill only.)',
            '-f': 'The pattern is normally only matched against the process name. When -f is set, the full command line is used.',
            '--full': 'The pattern is normally only matched against the process name. When -f is set, the full command line is used.',
            '-g': 'pgrp,...',
            '--pgroup': 'pgrp,...',
            '-G': 'gid,...',
            '--group': 'gid,...',
            '-i': 'Match processes case-insensitively.'
        },
        'examples': [
            'pkill  # look up, signal, or wait for processes based on na'
        ],
        'category': 'Other'
    },
    'plocate': {
        'desc': 'find files by name, quickly',
        'common_flags': {
            '-A': 'Ignored for compatibility with mlocate(1).',
            '--all': 'Ignored for compatibility with mlocate(1).',
            '-b': 'Match only against the file name portion of the path name, ie., the directory names will be excluded from the match (but still printed). This',
            '--basename': 'Match only against the file name portion of the path name, ie., the directory names will be excluded from the match (but still printed). This',
            '-c': 'Do not print each match. Instead, count them, and print out a total number at the end.',
            '--count': 'Do not print each match. Instead, count them, and print out a total number at the end.',
            '-d': 'DBPATH',
            '--database': 'DBPATH',
            '-e': 'Print only entries that refer to files existing at the time locate is run. Note that unlike mlocate(1), symlinks are not followed by default',
            '--existing': 'Print only entries that refer to files existing at the time locate is run. Note that unlike mlocate(1), symlinks are not followed by default',
            '-i': 'Do a case-insensitive match as given by the current locale (default is case-sensitive, byte-by-byte match). Note that plocate does not sup‐',
            '--ignore-case': 'Do a case-insensitive match as given by the current locale (default is case-sensitive, byte-by-byte match). Note that plocate does not sup‐',
            '-l': 'LIMIT',
            '--limit': 'LIMIT',
            '-N': 'Print entry names without quoting. Normally, plocate will escape special characters in filenames, so that they are safe for consumption by'
        },
        'examples': [
            'plocate  # find files by name, quickly',
            'plocate --all  # Show all'
        ],
        'category': 'Other'
    },
    'pmap': {
        'desc': 'report memory map of a process',
        'common_flags': {
            '-x': 'Show the extended format.',
            '--extended': 'Show the extended format.',
            '-d': 'Show the device format.',
            '--device': 'Show the device format.',
            '-q': 'Do not display some header or footer lines.',
            '--quiet': 'Do not display some header or footer lines.',
            '-A': 'low,high',
            '--range': 'low,high',
            '-X': 'X Show everything the kernel provides',
            '-p': 'Show full path to files in the mapping column',
            '--show-path': 'Show full path to files in the mapping column',
            '-c': 'Read the default configuration',
            '--read-rc': 'Read the default configuration',
            '-C': 'file',
            '--read-rc-from': 'file'
        },
        'examples': [
            'pmap  # report memory map of a process'
        ],
        'category': 'Other'
    },
    'pod2man': {
        'desc': 'Convert POD data to formatted *roff input',
        'common_flags': {
            '--section': ', and --official can be used to set the headers and footers to use. If not given, Pod::Man will assume',
            '--release': ', and --official can be used to set the headers and footers to use. If not given, Pod::Man will assume',
            '--center': ', and --official can be used to set the headers and footers to use. If not given, Pod::Man will assume',
            '--date': ', and --official can be used to set the headers and footers to use. If not given, Pod::Man will assume'
        },
        'examples': [
            'pod2man  # Convert POD data to formatted *roff input'
        ],
        'category': 'Other'
    },
    'pod2text': {
        'desc': 'Convert POD data to formatted ASCII text',
        'common_flags': {
            '-a': '[1.00] Use an alternate output format that, among other things, uses a different heading style and marks \"=item\" entries with a colon in the',
            '--alt': '[1.00] Use an alternate output format that, among other things, uses a different heading style and marks \"=item\" entries with a colon in the',
            '--code': '[1.11] Include any non-POD text from the input file in the output as well. Useful for viewing code documented with POD blocks with the POD',
            '-c': '[1.00] Format the output with ANSI color escape sequences. Using this option requires that Term::ANSIColor be installed on your system.',
            '--color': '[1.00] Format the output with ANSI color escape sequences. Using this option requires that Term::ANSIColor be installed on your system.',
            '-e': 'encoding, --encoding=encoding',
            '--errors': '=style',
            '--guesswork': '=rule[,rule...]',
            '-i': 'indent, --indent=indent',
            '-h': '[1.00] Print out usage information and exit.',
            '--help': '[1.00] Print out usage information and exit.',
            '-l': '[1.00] Print a blank line after a \"=head1\" heading. Normally, no blank line is printed after \"=head1\", although one is still printed after',
            '--loose': '[1.00] Print a blank line after a \"=head1\" heading. Normally, no blank line is printed after \"=head1\", although one is still printed after',
            '-m': 'width, --left-margin=width, --margin=width',
            '--nourls': '[2.5.0] Normally, L<> formatting codes with a URL but anchor text are formatted to show both the anchor text and the URL. In other words:'
        },
        'examples': [
            'pod2text  # Convert POD data to formatted ASCII text',
            'pod2text -h  # Show help',
            'pod2text -a  # Show all'
        ],
        'category': 'Other'
    },
    'postgres': {
        'desc': 'PostgreSQL database server',
        'common_flags': {
            '-B': 'nbuffers',
            '-c': 'name=value',
            '-C': 'name',
            '-d': 'debug-level',
            '-D': 'datadir',
            '-e': 'Sets the default date style to “European”, that is DMY ordering of input date fields. This also causes the day to be printed before the month in',
            '-F': 'Disables fsync calls for improved performance, at the risk of data corruption in the event of a system crash. Specifying this option is',
            '-h': 'hostname',
            '-i': 'Allows remote clients to connect via TCP/IP (Internet domain) connections. Without this option, only local connections are accepted. This option',
            '-k': 'directory',
            '-l': 'Enables secure connections using SSL. PostgreSQL must have been compiled with support for SSL for this option to be available. For more',
            '-N': 'max-connections',
            '-p': 'port',
            '-s': 'Print time information and other statistics at the end of each command. This is useful for benchmarking or for use in tuning the number of',
            '-S': 'work-mem'
        },
        'examples': [
            'postgres  # PostgreSQL database server',
            'postgres -h  # Show help'
        ],
        'category': 'Other'
    },
    'pr': {
        'desc': 'convert text files for printing',
        'common_flags': {
            '-t': 'omit page headers and trailers; implied if PAGE_LENGTH <= 10',
            '--omit-header': 'omit page headers and trailers; implied if PAGE_LENGTH <= 10',
            '-T': 'omit page headers and trailers, eliminate any pagination by form feeds set in input files',
            '--omit-pagination': 'omit page headers and trailers, eliminate any pagination by form feeds set in input files',
            '-v': 'use octal backslash notation',
            '--show-nonprinting': 'use octal backslash notation',
            '-w': '=PAGE_WIDTH',
            '--width': '=PAGE_WIDTH',
            '-W': '=PAGE_WIDTH',
            '--page-width': '=PAGE_WIDTH',
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'pr  # convert text files for printing',
            'pr --help  # Show help',
            'pr -v  # Show version',
            'pr -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'preconv': {
        'desc': 'prepare files for typesetting with groff',
        'common_flags': {
            '-h': 'and --help display a usage message, while -v and --version show version information; all exit afterward.',
            '-d': 'Emit debugging messages to the standard error stream.',
            '-D': 'fallback-encoding',
            '-e': 'encoding',
            '-r': 'Write files “raw”; do not add .lf requests.'
        },
        'examples': [
            'preconv  # prepare files for typesetting with groff',
            'preconv -h  # Show help'
        ],
        'category': 'Other'
    },
    'printf': {
        'desc': 'format and print data',
        'common_flags': {
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'printf  # format and print data',
            'printf --help  # Show help',
            'printf --version  # Show version'
        ],
        'category': 'Other'
    },
    'prlimit': {
        'desc': 'get and set process resource limits',
        'common_flags': {
            '--noheadings': 'Do not print a header line.',
            '-o': 'list',
            '--output': 'list',
            '-p': 'PID',
            '--pid': 'PID',
            '--raw': 'Use the raw output format.',
            '--verbose': 'Verbose mode.',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'prlimit  # get and set process resource limits',
            'prlimit -h  # Show help',
            'prlimit --version  # Show version',
            'prlimit --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'prove': {
        'desc': 'Run tests through a TAP harness.',
        'common_flags': {
            '-v': 'Print all test lines. Also sets TEST_VERBOSE',
            '--verbose': 'Print all test lines. Also sets TEST_VERBOSE',
            '-l': 'Add \'lib\' to the path for your tests (-Ilib).',
            '--lib': 'Add \'lib\' to the path for your tests (-Ilib).',
            '-b': 'Add \'blib/lib\' and \'blib/arch\' to the path for',
            '--blib': 'Add \'blib/lib\' and \'blib/arch\' to the path for',
            '-s': 'Run the tests in random order.',
            '--shuffle': 'Run the tests in random order.',
            '-c': 'Colored test output (default).',
            '--color': 'Colored test output (default).',
            '--nocolor': 'Do not color test output.',
            '--count': 'Show the X/Y test count when not verbose',
            '--nocount': 'Disable the X/Y test count.',
            '-D': '--dry Dry run. Show test that would have run.',
            '-f': 'Show failed tests.'
        },
        'examples': [
            'prove  # Run tests through a TAP harness.',
            'prove -v  # Show version',
            'prove -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'psql': {
        'desc': 'PostgreSQL interactive terminal',
        'common_flags': {
            '-a': '--echo-all',
            '-A': '--no-align',
            '-b': '--echo-errors',
            '-c': 'command',
            '--command': '=command',
            '--csv': 'Switches to CSV (Comma-Separated Values) output mode. This is equivalent to \\pset format csv.',
            '-d': 'dbname',
            '--dbname': '=dbname',
            '-e': '--echo-queries',
            '-E': '--echo-hidden',
            '-f': 'filename',
            '--file': '=filename',
            '-F': 'separator',
            '--field-separator': '=separator',
            '-h': 'hostname'
        },
        'examples': [
            'psql  # PostgreSQL interactive terminal',
            'psql -h  # Show help',
            'psql -a  # Show all'
        ],
        'category': 'Other'
    },
    'ptargrep': {
        'desc': 'Apply pattern matching to the contents of files in a tar archive',
        'common_flags': {
            '--basename': '(alias -b)',
            '--ignore-case': '(alias -i)',
            '--list-only': '(alias -l)',
            '--verbose': '(alias -v)',
            '--help': '(alias -?)'
        },
        'examples': [
            'ptargrep  # Apply pattern matching to the contents of files in',
            'ptargrep --help  # Show help',
            'ptargrep --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'pwdx': {
        'desc': 'report current working directory of a process',
        'common_flags': {
            '-V': 'Output version information and exit.',
            '--version': 'Output version information and exit.',
            '-h': 'Output help screen and exit.',
            '--help': 'Output help screen and exit.'
        },
        'examples': [
            'pwdx  # report current working directory of a process',
            'pwdx -h  # Show help',
            'pwdx --version  # Show version'
        ],
        'category': 'Other'
    },
    'py3clean': {
        'desc': 'removes .pyc and .pyo files',
        'common_flags': {
            '--version': 'show program\'s version number and exit',
            '-h': 'show this help message and exit',
            '--help': 'show this help message and exit',
            '-v': 'turn verbose mode on',
            '--verbose': 'turn verbose mode on',
            '-q': 'be quiet',
            '--quiet': 'be quiet',
            '-p': 'PACKAGE, --package=PACKAGE',
            '-V': 'VERSION'
        },
        'examples': [
            'py3clean  # removes .pyc and .pyo files',
            'py3clean -h  # Show help',
            'py3clean -v  # Show version',
            'py3clean -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'py3compile': {
        'desc': 'byte compile Python 3 source files',
        'common_flags': {
            '--version': 'show program\'s version number and exit',
            '-h': 'show this help message and exit',
            '--help': 'show this help message and exit',
            '-f': 'force rebuild of byte-code files even if timestamps are up-to-date',
            '--force': 'force rebuild of byte-code files even if timestamps are up-to-date',
            '-O': 'byte-compile to .pyo files',
            '-q': 'be quiet',
            '--quiet': 'be quiet',
            '-v': 'turn verbose mode on',
            '--verbose': 'turn verbose mode on',
            '-p': 'PACKAGE, --package=PACKAGE',
            '-V': 'VRANGE',
            '-X': 'REGEXPR, --exclude=REGEXPR'
        },
        'examples': [
            'py3compile  # byte compile Python 3 source files',
            'py3compile -h  # Show help',
            'py3compile -v  # Show version',
            'py3compile -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'py3versions': {
        'desc': 'print python3 version information',
        'common_flags': {
            '-d': 'Show the default python3 version.',
            '--default': 'Show the default python3 version.',
            '-s': 'Show the supported python3 versions. List is lowest version to highest version with the default version last (e.g. python3.4 python3.6',
            '--supported': 'Show the supported python3 versions. List is lowest version to highest version with the default version last (e.g. python3.4 python3.6',
            '-r': '[<version string>|<control file>]',
            '--requested': '[<version string>|<control file>]',
            '-i': 'Show the installed supported python3 versions.',
            '--installed': 'Show the installed supported python3 versions.',
            '--min-supported': 'Show the minimum supported python3 version.',
            '--max-supported': 'Show the maximum supported python3 version.',
            '-v': 'Limit the output to the version numbers of the python3 versions.',
            '--version': 'Limit the output to the version numbers of the python3 versions.',
            '-h': 'Print a help text.',
            '--help': 'Print a help text.'
        },
        'examples': [
            'py3versions  # print python3 version information',
            'py3versions -h  # Show help',
            'py3versions -v  # Show version',
            'py3versions -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'pygettext3.13': {
        'desc': 'Python equivalent of xgettext(1)',
        'common_flags': {
            '-a': 'Extract all strings.',
            '--extract-all': 'Extract all strings.',
            '-d': '=NAME',
            '--default-domain': '=NAME',
            '-E': 'Replace non-ASCII characters with octal escape sequences.',
            '--escape': 'Replace non-ASCII characters with octal escape sequences.',
            '-D': 'Extract module, class, method, and function docstrings. These do not need to be wrapped in _() markers, and in fact cannot be for Python to',
            '--docstrings': 'Extract module, class, method, and function docstrings. These do not need to be wrapped in _() markers, and in fact cannot be for Python to',
            '-h': 'Print this help message and exit.',
            '--help': 'Print this help message and exit.',
            '-k': '=WORD',
            '--keyword': '=WORD',
            '-K': 'Disable the default set of keywords (see above). Any keywords explicitly added with the -k/--keyword option are still recognized.',
            '--no-default-keywords': 'Disable the default set of keywords (see above). Any keywords explicitly added with the -k/--keyword option are still recognized.',
            '--no-location': 'Do not write filename/lineno location comments.'
        },
        'examples': [
            'pygettext3.13  # Python equivalent of xgettext(1)',
            'pygettext3.13 -h  # Show help',
            'pygettext3.13 -a  # Show all'
        ],
        'category': 'Other'
    },
    'pygettext3': {
        'desc': 'Python equivalent of xgettext(1)',
        'common_flags': {
            '-a': 'Extract all strings.',
            '--extract-all': 'Extract all strings.',
            '-d': '=NAME',
            '--default-domain': '=NAME',
            '-E': 'Replace non-ASCII characters with octal escape sequences.',
            '--escape': 'Replace non-ASCII characters with octal escape sequences.',
            '-D': 'Extract module, class, method, and function docstrings. These do not need to be wrapped in _() markers, and in fact cannot be for Python to',
            '--docstrings': 'Extract module, class, method, and function docstrings. These do not need to be wrapped in _() markers, and in fact cannot be for Python to',
            '-h': 'Print this help message and exit.',
            '--help': 'Print this help message and exit.',
            '-k': '=WORD',
            '--keyword': '=WORD',
            '-K': 'Disable the default set of keywords (see above). Any keywords explicitly added with the -k/--keyword option are still recognized.',
            '--no-default-keywords': 'Disable the default set of keywords (see above). Any keywords explicitly added with the -k/--keyword option are still recognized.',
            '--no-location': 'Do not write filename/lineno location comments.'
        },
        'examples': [
            'pygettext3  # Python equivalent of xgettext(1)',
            'pygettext3 -h  # Show help',
            'pygettext3 -a  # Show all'
        ],
        'category': 'Other'
    },
    'python': {
        'desc': 'an interpreted, interactive, object-oriented programming language',
        'common_flags': {
            '-B': 'Don\'t write .pyc files on import. See also PYTHONDONTWRITEBYTECODE.',
            '-b': 'Issue warnings about str(bytes_instance), str(bytearray_instance) and comparing bytes/bytearray with str. (-bb: issue errors)',
            '-c': 'command',
            '--check-hash-based-pycs': 'mode',
            '-d': 'Turn on parser debugging output (for expert only, depending on compilation options).',
            '-E': 'Ignore environment variables like PYTHONPATH and PYTHONHOME that modify the behavior of the interpreter.',
            '-h': ', -? , --help',
            '--help-env': 'Prints help about Python-specific environment variables and exits.',
            '--help-xoptions': 'Prints help about implementation-specific -X options and exits.',
            '--help-all': 'Prints complete usage information and exits.',
            '-i': 'When a script is passed as first argument or the -c option is used, enter interactive mode after executing the script or the command. It',
            '-I': 'Run Python in isolated mode. This also implies -E, -P and -s. In isolated mode sys.path contains neither the script\'s directory nor the',
            '-m': 'module-name',
            '-O': 'O Do -O and also discard docstrings; change the filename for compiled (bytecode) files by adding .opt-2 before the .pyc extension.',
            '-P': 'Don\'t automatically prepend a potentially unsafe path to sys.path such as the current directory, the script\'s directory or an empty string.'
        },
        'examples': [
            'python  # an interpreted, interactive, object-oriented progr',
            'python -h  # Show help'
        ],
        'category': 'Other'
    },
    'python3': {
        'desc': 'an interpreted, interactive, object-oriented programming language',
        'common_flags': {
            '-B': 'Don\'t write .pyc files on import. See also PYTHONDONTWRITEBYTECODE.',
            '-b': 'Issue warnings about str(bytes_instance), str(bytearray_instance) and comparing bytes/bytearray with str. (-bb: issue errors)',
            '-c': 'command',
            '--check-hash-based-pycs': 'mode',
            '-d': 'Turn on parser debugging output (for expert only, depending on compilation options).',
            '-E': 'Ignore environment variables like PYTHONPATH and PYTHONHOME that modify the behavior of the interpreter.',
            '-h': ', -? , --help',
            '--help-env': 'Prints help about Python-specific environment variables and exits.',
            '--help-xoptions': 'Prints help about implementation-specific -X options and exits.',
            '--help-all': 'Prints complete usage information and exits.',
            '-i': 'When a script is passed as first argument or the -c option is used, enter interactive mode after executing the script or the command. It',
            '-I': 'Run Python in isolated mode. This also implies -E, -P and -s. In isolated mode sys.path contains neither the script\'s directory nor the',
            '-m': 'module-name',
            '-O': 'O Do -O and also discard docstrings; change the filename for compiled (bytecode) files by adding .opt-2 before the .pyc extension.',
            '-P': 'Don\'t automatically prepend a potentially unsafe path to sys.path such as the current directory, the script\'s directory or an empty string.'
        },
        'examples': [
            'python3  # an interpreted, interactive, object-oriented progr',
            'python3 -h  # Show help'
        ],
        'category': 'Other'
    },
    'python3.13': {
        'desc': 'an interpreted, interactive, object-oriented programming language',
        'common_flags': {
            '-B': 'Don\'t write .pyc files on import. See also PYTHONDONTWRITEBYTECODE.',
            '-b': 'Issue warnings about str(bytes_instance), str(bytearray_instance) and comparing bytes/bytearray with str. (-bb: issue errors)',
            '-c': 'command',
            '--check-hash-based-pycs': 'mode',
            '-d': 'Turn on parser debugging output (for expert only, depending on compilation options).',
            '-E': 'Ignore environment variables like PYTHONPATH and PYTHONHOME that modify the behavior of the interpreter.',
            '-h': ', -? , --help',
            '--help-env': 'Prints help about Python-specific environment variables and exits.',
            '--help-xoptions': 'Prints help about implementation-specific -X options and exits.',
            '--help-all': 'Prints complete usage information and exits.',
            '-i': 'When a script is passed as first argument or the -c option is used, enter interactive mode after executing the script or the command. It',
            '-I': 'Run Python in isolated mode. This also implies -E, -P and -s. In isolated mode sys.path contains neither the script\'s directory nor the',
            '-m': 'module-name',
            '-O': 'O Do -O and also discard docstrings; change the filename for compiled (bytecode) files by adding .opt-2 before the .pyc extension.',
            '-P': 'Don\'t automatically prepend a potentially unsafe path to sys.path such as the current directory, the script\'s directory or an empty string.'
        },
        'examples': [
            'python3.13  # an interpreted, interactive, object-oriented progr',
            'python3.13 -h  # Show help'
        ],
        'category': 'Other'
    },
    'rake': {
        'desc': 'make-like build utility for Ruby',
        'common_flags': {
            '-m': 'Treat all tasks as multitasks.',
            '--multitask': 'Treat all tasks as multitasks.',
            '-B': 'Build all prerequisites, including those which are up-to-date.',
            '--build-all': 'Build all prerequisites, including those which are up-to-date.',
            '-j': 'num_jobs',
            '--jobs': 'num_jobs',
            '-I': 'libdir',
            '--libdir': 'libdir',
            '-r': 'module',
            '--require': 'module',
            '-f': 'filename',
            '--rakefile': 'filename',
            '-N': 'Do not search parent directories for the Rakefile.',
            '--no-search': 'Do not search parent directories for the Rakefile.',
            '--nosearch': 'Do not search parent directories for the Rakefile.'
        },
        'examples': [
            'rake  # make-like build utility for Ruby',
            'rake -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'ranlib': {
        'desc': 'generate an index to an archive',
        'common_flags': {
            '-h': '-H',
            '--help': 'Show usage information for ranlib.',
            '-v': '-V',
            '--version': 'Show the version number of ranlib.',
            '-D': 'Operate in deterministic mode. The symbol map archive member\'s header will show zero for the UID, GID, and timestamp. When this option is',
            '-t': 'Update the timestamp of the symbol map of an archive.',
            '-U': 'Do not operate in deterministic mode. This is the inverse of the -D option, above: the archive index will get actual UID, GID, timestamp, and'
        },
        'examples': [
            'ranlib  # generate an index to an archive',
            'ranlib -h  # Show help',
            'ranlib -v  # Show version',
            'ranlib -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'rdoc': {
        'desc': 'Generate documentation from Ruby script files',
        'common_flags': {
            '--accessor': 'accessorname[,..]',
            '-A': 'accessorname[,..]',
            '--all': 'include all methods (not just public) in the output.',
            '-a': 'include all methods (not just public) in the output.',
            '--charset': 'charset',
            '-c': 'charset',
            '--debug': 'displays lots on internal stuff',
            '-D': 'displays lots on internal stuff',
            '--diagram': 'generate diagrams showing modules and classes. You need dot V1.8.6 or later to use the --diagram option correctly. Dot is available from',
            '-d': 'generate diagrams showing modules and classes. You need dot V1.8.6 or later to use the --diagram option correctly. Dot is available from',
            '--exclude': 'pattern',
            '-x': 'pattern',
            '--extension': 'new = old',
            '-E': 'new = old',
            '--fileboxes': 'classes are put in boxes which represents files, where these classes reside. Classes shared between more than one file are shown with list of'
        },
        'examples': [
            'rdoc  # Generate documentation from Ruby script files',
            'rdoc -a  # Show all'
        ],
        'category': 'Other'
    },
    'rdoc3.3': {
        'desc': 'Generate documentation from Ruby script files',
        'common_flags': {
            '--accessor': 'accessorname[,..]',
            '-A': 'accessorname[,..]',
            '--all': 'include all methods (not just public) in the output.',
            '-a': 'include all methods (not just public) in the output.',
            '--charset': 'charset',
            '-c': 'charset',
            '--debug': 'displays lots on internal stuff',
            '-D': 'displays lots on internal stuff',
            '--diagram': 'generate diagrams showing modules and classes. You need dot V1.8.6 or later to use the --diagram option correctly. Dot is available from',
            '-d': 'generate diagrams showing modules and classes. You need dot V1.8.6 or later to use the --diagram option correctly. Dot is available from',
            '--exclude': 'pattern',
            '-x': 'pattern',
            '--extension': 'new = old',
            '-E': 'new = old',
            '--fileboxes': 'classes are put in boxes which represents files, where these classes reside. Classes shared between more than one file are shown with list of'
        },
        'examples': [
            'rdoc3.3  # Generate documentation from Ruby script files',
            'rdoc3.3 -a  # Show all'
        ],
        'category': 'Other'
    },
    'readelf': {
        'desc': 'display information about ELF files',
        'common_flags': {
            '-a': '--all',
            '--unwind': 'and --histogram.',
            '--section-groups': 'and --histogram.',
            '-h': '--file-header',
            '-l': '--program-headers',
            '--segments': 'Displays the information contained in the file\'s segment headers, if it has any.',
            '--quiet': 'Suppress \"no symbols\" diagnostic.',
            '-S': '--sections',
            '--section-headers': 'Displays the information contained in the file\'s section headers, if it has any.',
            '-g': '--section-groups',
            '-t': '--section-details',
            '-s': '--symbols',
            '--syms': 'Displays the entries in symbol table section of the file, if it has one. If a symbol has version information associated with it then this is',
            '--dyn-syms': 'Displays the entries in dynamic symbol table section of the file, if it has one. The output format is the same as the format used by the --syms',
            '--lto-syms': 'Displays the contents of any LTO symbol tables in the file.'
        },
        'examples': [
            'readelf  # display information about ELF files',
            'readelf -h  # Show help',
            'readelf -a  # Show all'
        ],
        'category': 'Other'
    },
    'reindexdb': {
        'desc': 'reindex a PostgreSQL database',
        'common_flags': {
            '-a': '--all',
            '--concurrently': 'Use the CONCURRENTLY option. See REINDEX(7), where all the caveats of this option are explained in detail.',
            '-e': '--echo',
            '-i': 'index',
            '--index': '=index',
            '-j': 'njobs',
            '--jobs': '=njobs',
            '-q': '--quiet',
            '-s': '--system',
            '-S': 'schema',
            '--schema': '=schema',
            '-t': 'table',
            '--table': '=table',
            '--tablespace': '=tablespace',
            '-v': '--verbose'
        },
        'examples': [
            'reindexdb  # reindex a PostgreSQL database',
            'reindexdb -v  # Show version',
            'reindexdb -v  # Verbose output',
            'reindexdb -a  # Show all'
        ],
        'category': 'Other'
    },
    'rename.ul': {
        'desc': 'rename files',
        'common_flags': {
            '-s': 'Do not rename a symlink but change where it points.',
            '--symlink': 'Do not rename a symlink but change where it points.',
            '-v': 'Show which files were renamed, if any.',
            '--verbose': 'Show which files were renamed, if any.',
            '-n': 'Do not make any changes; add --verbose to see what would be made.',
            '--no-act': 'Do not make any changes; add --verbose to see what would be made.',
            '-a': 'Replace all occurrences of expression rather than only the first one.',
            '--all': 'Replace all occurrences of expression rather than only the first one.',
            '-l': 'Replace the last occurrence of expression rather than the first one.',
            '--last': 'Replace the last occurrence of expression rather than the first one.',
            '-o': 'Do not overwrite existing files. When --symlink is active, do not overwrite symlinks pointing to existing targets.',
            '--no-overwrite': 'Do not overwrite existing files. When --symlink is active, do not overwrite symlinks pointing to existing targets.',
            '-i': 'Ask before overwriting existing files.',
            '--interactive': 'Ask before overwriting existing files.',
            '-h': 'Display help text and exit.'
        },
        'examples': [
            'rename.ul  # rename files',
            'rename.ul -h  # Show help',
            'rename.ul -v  # Show version',
            'rename.ul -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'renice': {
        'desc': 'alter priority of running processes',
        'common_flags': {
            '-n': 'priority',
            '--priority': 'priority',
            '--relative': 'priority',
            '-g': 'Interpret the succeeding arguments as process group IDs.',
            '--pgrp': 'Interpret the succeeding arguments as process group IDs.',
            '-p': 'Interpret the succeeding arguments as process IDs (the default).',
            '--pid': 'Interpret the succeeding arguments as process IDs (the default).',
            '-u': 'Interpret the succeeding arguments as usernames or UIDs.',
            '--user': 'Interpret the succeeding arguments as usernames or UIDs.',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'renice  # alter priority of running processes',
            'renice -h  # Show help',
            'renice --version  # Show version'
        ],
        'category': 'Other'
    },
    'reset': {
        'desc': 'initialize or reset terminal state',
        'common_flags': {
            '-c': 'Set control characters and modes.',
            '-e': 'ch',
            '-I': 'Do not send the terminal or tab initialization strings to the terminal.',
            '-i': 'ch',
            '-k': 'ch',
            '-m': 'mapping',
            '-Q': 'Do not display any values for the erase, interrupt and line kill characters. Normally tset displays the values for control characters which',
            '-q': 'The terminal type is displayed to the standard output, and the terminal is not initialized in any way. The option “-” by itself is equivalent',
            '-r': 'Print the terminal type to the standard error output.',
            '-s': 'Print the sequence of shell commands to initialize the environment variable TERM to the standard output; see subsection “Setting the Environ‐',
            '-V': 'reports the version of ncurses which was used in this program, and exits.',
            '-w': 'Resize the window to match the size deduced via setupterm(3NCURSES). Normally this has no effect, unless setupterm is not able to detect the'
        },
        'examples': [
            'reset  # initialize or reset terminal state',
            'reset -V  # Show version'
        ],
        'category': 'Other'
    },
    'rev': {
        'desc': 'reverse lines characterwise',
        'common_flags': {
            '-0': 'Zero termination. Use the byte \'\\0\' as line separator.',
            '--zero': 'Zero termination. Use the byte \'\\0\' as line separator.',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'rev  # reverse lines characterwise',
            'rev -h  # Show help',
            'rev --version  # Show version'
        ],
        'category': 'Other'
    },
    'rgrep': {
        'desc': 'print lines that match patterns',
        'common_flags': {
            '--help': 'Output a usage message and exit.',
            '-V': 'Output the version number of grep and exit.',
            '--version': 'Output the version number of grep and exit.',
            '-E': 'Interpret PATTERNS as extended regular expressions (EREs, see below).',
            '--extended-regexp': 'Interpret PATTERNS as extended regular expressions (EREs, see below).',
            '-F': 'Interpret PATTERNS as fixed strings, not regular expressions.',
            '--fixed-strings': 'Interpret PATTERNS as fixed strings, not regular expressions.',
            '-G': 'Interpret PATTERNS as basic regular expressions (BREs, see below). This is the default.',
            '--basic-regexp': 'Interpret PATTERNS as basic regular expressions (BREs, see below). This is the default.',
            '-P': 'Interpret PATTERNS as Perl-compatible regular expressions (PCREs). This option is experimental when combined with the -z (--null-data)',
            '--perl-regexp': 'Interpret PATTERNS as Perl-compatible regular expressions (PCREs). This option is experimental when combined with the -z (--null-data)',
            '-e': 'PATTERNS, --regexp=PATTERNS',
            '-f': 'FILE, --file=FILE',
            '-i': 'Ignore case distinctions in patterns and input data, so that characters that differ only in case match each other.',
            '--ignore-case': 'Ignore case distinctions in patterns and input data, so that characters that differ only in case match each other.'
        },
        'examples': [
            'rgrep  # print lines that match patterns',
            'rgrep --help  # Show help',
            'rgrep --version  # Show version'
        ],
        'category': 'Other'
    },
    'ri': {
        'desc': 'Ruby API reference front end',
        'common_flags': {
            '-i': '--[no-]interactive',
            '-a': '--[no-]all Show all documentation for a class or module.',
            '-l': '--[no-]list List classes ri knows about.',
            '-T': 'Synonym for --no-pager.',
            '-w': 'WIDTH',
            '--width': '=WIDTH Set the width of the output.',
            '--server': '[=PORT]',
            '-f': 'FORMAT',
            '--format': '=FORMAT',
            '-h': '--help Show help and exit.',
            '-v': '--version Output version information and exit.',
            '-d': 'DIRNAME',
            '--doc-dir': '=DIRNAME',
            '--no-standard-docs': 'Do not include documentation from the Ruby standard library, site_lib, installed gems, or ~/.rdoc. Use with --doc-dir.',
            '--dump': '=CACHE Dump data from an ri cache or data file.'
        },
        'examples': [
            'ri  # Ruby API reference front end',
            'ri -h  # Show help',
            'ri -v  # Show version',
            'ri -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'ri3.3': {
        'desc': 'Ruby API reference front end',
        'common_flags': {
            '-i': '--[no-]interactive',
            '-a': '--[no-]all Show all documentation for a class or module.',
            '-l': '--[no-]list List classes ri knows about.',
            '-T': 'Synonym for --no-pager.',
            '-w': 'WIDTH',
            '--width': '=WIDTH Set the width of the output.',
            '--server': '[=PORT]',
            '-f': 'FORMAT',
            '--format': '=FORMAT',
            '-h': '--help Show help and exit.',
            '-v': '--version Output version information and exit.',
            '-d': 'DIRNAME',
            '--doc-dir': '=DIRNAME',
            '--no-standard-docs': 'Do not include documentation from the Ruby standard library, site_lib, installed gems, or ~/.rdoc. Use with --doc-dir.',
            '--dump': '=CACHE Dump data from an ri cache or data file.'
        },
        'examples': [
            'ri3.3  # Ruby API reference front end',
            'ri3.3 -h  # Show help',
            'ri3.3 -v  # Show version',
            'ri3.3 -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'rm': {
        'desc': 'remove files or directories',
        'common_flags': {
            '-f': 'ignore nonexistent files and arguments, never prompt',
            '--force': 'ignore nonexistent files and arguments, never prompt',
            '-i': 'prompt before every removal',
            '-I': 'prompt once before removing more than three files, or when removing recursively; less intrusive than -i, while still giving protection',
            '--interactive': '[=WHEN]',
            '--one-file-system': 'when removing a hierarchy recursively, skip any directory that is on a file system different from that of the corresponding command line ar‐',
            '--no-preserve-root': 'do not treat \'/\' specially',
            '--preserve-root': '[=all]',
            '-r': 'remove directories and their contents recursively',
            '-R': 'remove directories and their contents recursively',
            '--recursive': 'remove directories and their contents recursively',
            '-d': 'remove empty directories',
            '--dir': 'remove empty directories',
            '-v': 'explain what is being done',
            '--verbose': 'explain what is being done'
        },
        'examples': [
            'rm  # remove files or directories',
            'rm -v  # Show version',
            'rm -v  # Verbose output',
            'rm -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'rnano': {
        'desc': 'a restricted nano',
        'common_flags': {
            '-h': 'Show the available command-line options and exit.',
            '--help': 'Show the available command-line options and exit.'
        },
        'examples': [
            'rnano  # a restricted nano',
            'rnano -h  # Show help'
        ],
        'category': 'Other'
    },
    'ruby': {
        'desc': 'Interpreted object-oriented scripting language',
        'common_flags': {
            '--copyright': 'Prints the copyright notice, and quits immediately without running any script.',
            '--version': 'Prints the version of the Ruby interpreter, and quits immediately without running any script.',
            '-0': '[octal] (The digit “zero”.) Specifies the input record separator ($/) as an octal number. If no digit is given, the null character is taken',
            '-C': 'directory',
            '-X': 'directory Causes Ruby to switch to the directory.',
            '-E': 'external[:internal]',
            '--encoding': 'external[:internal]',
            '--external-encoding': '=encoding',
            '--internal-encoding': '=encoding',
            '-F': 'pattern Specifies input field separator ($;).',
            '-I': 'directory Used to tell Ruby where to load the library scripts. Directory path will be added to the load-path variable ($:).',
            '-K': 'kcode Specifies KANJI (Japanese) encoding. The default value for script encodings (__ENCODING__) and external encodings',
            '-S': 'Makes Ruby use the PATH environment variable to search for script, unless its name begins with a slash. This is used to emulate #!',
            '-T': '[level=1] Turns on taint checks at the specified level (default 1).',
            '-U': 'Sets the default value for internal encodings (Encoding.default_internal) to UTF-8.'
        },
        'examples': [
            'ruby  # Interpreted object-oriented scripting language',
            'ruby --version  # Show version'
        ],
        'category': 'Other'
    },
    'ruby3.3': {
        'desc': 'Interpreted object-oriented scripting language',
        'common_flags': {
            '--copyright': 'Prints the copyright notice, and quits immediately without running any script.',
            '--version': 'Prints the version of the Ruby interpreter, and quits immediately without running any script.',
            '-0': '[octal] (The digit “zero”.) Specifies the input record separator ($/) as an octal number. If no digit is given, the null character is taken',
            '-C': 'directory',
            '-X': 'directory Causes Ruby to switch to the directory.',
            '-E': 'external[:internal]',
            '--encoding': 'external[:internal]',
            '--external-encoding': '=encoding',
            '--internal-encoding': '=encoding',
            '-F': 'pattern Specifies input field separator ($;).',
            '-I': 'directory Used to tell Ruby where to load the library scripts. Directory path will be added to the load-path variable ($:).',
            '-K': 'kcode Specifies KANJI (Japanese) encoding. The default value for script encodings (__ENCODING__) and external encodings',
            '-S': 'Makes Ruby use the PATH environment variable to search for script, unless its name begins with a slash. This is used to emulate #!',
            '-T': '[level=1] Turns on taint checks at the specified level (default 1).',
            '-U': 'Sets the default value for internal encodings (Encoding.default_internal) to UTF-8.'
        },
        'examples': [
            'ruby3.3  # Interpreted object-oriented scripting language',
            'ruby3.3 --version  # Show version'
        ],
        'category': 'Other'
    },
    'run0': {
        'desc': 'Elevate privileges',
        'common_flags': {
            '--unit': '=',
            '--property': '=',
            '--description': '=',
            '--slice': '=',
            '--slice-inherit': 'Make the new .service unit part of the slice the run0 itself has been invoked in. This option may be combined with --slice=, in which case the',
            '--user': '=, -u, --group=, -g',
            '--nice': '=',
            '--chdir': '=, -D',
            '--setenv': '=NAME[=VALUE]',
            '--background': '=COLOR',
            '--pty': 'Request allocation of a pseudo TTY for the run0 session (in case of --pty), or request passing the caller\'s STDIO file descriptors directly',
            '--pipe': 'Request allocation of a pseudo TTY for the run0 session (in case of --pty), or request passing the caller\'s STDIO file descriptors directly',
            '--shell-prompt-prefix': '=STRING',
            '--machine': '=',
            '--no-ask-password': 'Do not query the user for authentication for privileged operations.'
        },
        'examples': [
            'run0  # Elevate privileges'
        ],
        'category': 'Other'
    },
    'runuser': {
        'desc': 'run a command with substitute user and group ID',
        'common_flags': {
            '-c': '=command',
            '--command': '=command',
            '-f': 'Pass -f to the shell, which may or may not be useful, depending on the shell.',
            '--fast': 'Pass -f to the shell, which may or may not be useful, depending on the shell.',
            '-g': '=group',
            '--group': '=group',
            '-G': '=group',
            '--supp-group': '=group',
            '-m': 'Preserve the entire environment, i.e., do not set HOME, SHELL, USER or LOGNAME. The option is ignored if the option --login is specified.',
            '-p': 'Preserve the entire environment, i.e., do not set HOME, SHELL, USER or LOGNAME. The option is ignored if the option --login is specified.',
            '--preserve-environment': 'Preserve the entire environment, i.e., do not set HOME, SHELL, USER or LOGNAME. The option is ignored if the option --login is specified.',
            '-P': 'Create a pseudo-terminal for the session. The independent terminal provides better security as the user does not share a terminal with the',
            '--pty': 'Create a pseudo-terminal for the session. The independent terminal provides better security as the user does not share a terminal with the',
            '-s': '=shell',
            '--shell': '=shell'
        },
        'examples': [
            'runuser  # run a command with substitute user and group ID'
        ],
        'category': 'Other'
    },
    'rview': {
        'desc': 'Vi IMproved, a programmer\'s text editor',
        'common_flags': {
            '-c': '{command}',
            '-A': 'If Vim has been compiled with ARABIC support for editing right-to-left oriented files and Arabic keyboard mapping, this option starts',
            '-b': 'Binary mode. A few options will be set that makes it possible to edit a binary or executable file.',
            '-C': 'Compatible. Set the \'compatible\' option. This will make Vim behave mostly like Vi, even though a .vimrc file exists.',
            '-d': '{device}, -dev {device}',
            '-D': 'Debugging. Go to debugging mode when executing the first command from a script.',
            '-e': 'Start Vim in Ex mode, just like the executable was called \"ex\".',
            '-E': 'Start Vim in improved Ex mode, just like the executable was called \"exim\".',
            '-f': 'Foreground. For the GUI version, Vim will not fork and detach from the shell it was started in. On the Amiga, Vim is not restarted to',
            '-F': 'If Vim has been compiled with FKMAP support for editing right-to-left oriented files and Farsi keyboard mapping, this option starts Vim',
            '-g': 'If Vim has been compiled with GUI support, this option enables the GUI. If no GUI support was compiled in, an error message is given',
            '-H': 'If Vim has been compiled with RIGHTLEFT support for editing right-to-left oriented files and Hebrew keyboard mapping, this option starts',
            '-i': '{viminfo}',
            '-l': 'Lisp mode. Sets the \'lisp\' and \'showmatch\' options on.',
            '-L': 'Same as -r.'
        },
        'examples': [
            'rview  # Vi IMproved, a programmer\'s text editor'
        ],
        'category': 'Other'
    },
    'rvim': {
        'desc': 'Vi IMproved, a programmer\'s text editor',
        'common_flags': {
            '-c': '{command}',
            '-A': 'If Vim has been compiled with ARABIC support for editing right-to-left oriented files and Arabic keyboard mapping, this option starts',
            '-b': 'Binary mode. A few options will be set that makes it possible to edit a binary or executable file.',
            '-C': 'Compatible. Set the \'compatible\' option. This will make Vim behave mostly like Vi, even though a .vimrc file exists.',
            '-d': '{device}, -dev {device}',
            '-D': 'Debugging. Go to debugging mode when executing the first command from a script.',
            '-e': 'Start Vim in Ex mode, just like the executable was called \"ex\".',
            '-E': 'Start Vim in improved Ex mode, just like the executable was called \"exim\".',
            '-f': 'Foreground. For the GUI version, Vim will not fork and detach from the shell it was started in. On the Amiga, Vim is not restarted to',
            '-F': 'If Vim has been compiled with FKMAP support for editing right-to-left oriented files and Farsi keyboard mapping, this option starts Vim',
            '-g': 'If Vim has been compiled with GUI support, this option enables the GUI. If no GUI support was compiled in, an error message is given',
            '-H': 'If Vim has been compiled with RIGHTLEFT support for editing right-to-left oriented files and Hebrew keyboard mapping, this option starts',
            '-i': '{viminfo}',
            '-l': 'Lisp mode. Sets the \'lisp\' and \'showmatch\' options on.',
            '-L': 'Same as -r.'
        },
        'examples': [
            'rvim  # Vi IMproved, a programmer\'s text editor'
        ],
        'category': 'Other'
    },
    'sadf': {
        'desc': 'Display data collected by sar in multiple formats.',
        'common_flags': {
            '-C': 'Tell sadf to display comments present in file.',
            '-c': 'Convert an old system activity binary datafile (version 9.1.6 and later) to current up-to-date format. Use the following syntax:',
            '-d': 'Print the contents of the data file in a format that can easily be ingested by a relational database system. The output consists of fields',
            '--dev': '=dev_list',
            '-e': '[ seconds_since_the_epoch ]',
            '--fs': '=fs_list',
            '-g': 'Print the contents of the data file in SVG (Scalable Vector Graphics) format. This option enables you to display some fancy graphs in your',
            '-H': 'Display only the header of the report (when applicable). If no format has been specified, then the header data (metadata) of the data file',
            '-h': 'When used in conjunction with option -d, all activities will be displayed horizontally on a single line.',
            '--iface': '=iface_list',
            '--int': '=int_list',
            '-j': 'Print the contents of the data file in JSON (JavaScript Object Notation) format. Timestamps can be controlled by options -T and -t.',
            '-l': 'Export the contents of the data file to a PCP (Performance Co-Pilot) archive. The name of the archive can be specified using the keyword pc‐',
            '-O': 'opts[,...]',
            '-P': '{ cpu_list | ALL }'
        },
        'examples': [
            'sadf  # Display data collected by sar in multiple formats.',
            'sadf -h  # Show help'
        ],
        'category': 'Other'
    },
    'sar': {
        'desc': 'Collect, report, or save system activity information.',
        'common_flags': {
            '-A': 'This is equivalent to specifying -bBdFHISvwWy -m ALL -n ALL -q ALL -r ALL -u ALL. This option also implies specifying -I ALL -P ALL unless',
            '-B': 'Report paging statistics. The following values are displayed:',
            '-b': 'Report I/O and transfer rate statistics. The following values are displayed:',
            '-C': 'When reading data from a file, tell sar to display comments that have been inserted by sadc.',
            '-D': 'Use saYYYYMMDD instead of saDD as the standard system activity daily data file name. This option works only when used in conjunction with op‐',
            '-d': 'Report activity for each block device. When data are displayed, the device name is displayed as it (should) appear in /dev. sar uses data',
            '--dec': '={ 0 | 1 | 2 }',
            '--dev': '=dev_list',
            '-e': '[ seconds_since_the_epoch ]',
            '-F': '[ MOUNT ]',
            '-f': '[ filename ]',
            '--fs': '=fs_list',
            '-H': 'Report hugepages utilization statistics. The following values are displayed:',
            '-h': 'This option is equivalent to specifying --pretty --human.',
            '--help': 'Display a short help message then exit.'
        },
        'examples': [
            'sar  # Collect, report, or save system activity informati',
            'sar -h  # Show help'
        ],
        'category': 'Other'
    },
    'sar.sysstat': {
        'desc': 'Collect, report, or save system activity information.',
        'common_flags': {
            '-A': 'This is equivalent to specifying -bBdFHISvwWy -m ALL -n ALL -q ALL -r ALL -u ALL. This option also implies specifying -I ALL -P ALL unless',
            '-B': 'Report paging statistics. The following values are displayed:',
            '-b': 'Report I/O and transfer rate statistics. The following values are displayed:',
            '-C': 'When reading data from a file, tell sar to display comments that have been inserted by sadc.',
            '-D': 'Use saYYYYMMDD instead of saDD as the standard system activity daily data file name. This option works only when used in conjunction with op‐',
            '-d': 'Report activity for each block device. When data are displayed, the device name is displayed as it (should) appear in /dev. sar uses data',
            '--dec': '={ 0 | 1 | 2 }',
            '--dev': '=dev_list',
            '-e': '[ seconds_since_the_epoch ]',
            '-F': '[ MOUNT ]',
            '-f': '[ filename ]',
            '--fs': '=fs_list',
            '-H': 'Report hugepages utilization statistics. The following values are displayed:',
            '-h': 'This option is equivalent to specifying --pretty --human.',
            '--help': 'Display a short help message then exit.'
        },
        'examples': [
            'sar.sysstat  # Collect, report, or save system activity informati',
            'sar.sysstat -h  # Show help'
        ],
        'category': 'Other'
    },
    'sc-hsm-tool': {
        'desc': 'smart card utility for SmartCard-HSM',
        'common_flags': {
            '--initialize': 'Initialize token, removing all existing keys, certificates and files.',
            '-X': 'Initialize token, removing all existing keys, certificates and files.',
            '--create-dkek-share': 'filename, -C filename',
            '--import-dkek-share': 'filename, -I filename',
            '--wrap-key': 'filename, -W filename',
            '--unwrap-key': 'filename, -U filename',
            '--dkek-shares': 'number-of-shares, -s number-of-shares',
            '--pin': 'pin, --so-pin sopin,',
            '--pin-retry': 'value',
            '--bio-server1': 'value',
            '--bio-server2': 'value',
            '--password': 'value',
            '--pwd-shares-threshold': 'value',
            '--pwd-shares-total': 'value',
            '--force': 'Force removal of existing key, description and certificate.'
        },
        'examples': [
            'sc-hsm-tool  # smart card utility for SmartCard-HSM'
        ],
        'category': 'Other'
    },
    'scp': {
        'desc': 'OpenSSH secure file copy',
        'common_flags': {
            '-P': 'port',
            '-p': 'Preserves modification times, access times, and file mode bits from the source file.',
            '-q': 'Quiet mode: disables the progress meter as well as warning and diagnostic messages from ssh(1).',
            '-R': 'Copies between two remote hosts are performed by connecting to the origin host and executing scp there. This requires that scp running on',
            '-r': 'Recursively copy entire directories. Note that scp follows symbolic links encountered in the tree traversal.',
            '-S': 'program',
            '-T': 'Disable strict filename checking. By default when copying files from a remote host to a local directory scp checks that the received file‐',
            '-v': 'Verbose mode. Causes scp and ssh(1) to print debugging messages about their progress. This is helpful in debugging connection, authentica‐',
            '-X': 'sftp_option'
        },
        'examples': [
            'scp  # OpenSSH secure file copy',
            'scp -v  # Show version',
            'scp -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'scp1': {
        'desc': 'secure copy (remote file copy program)',
        'common_flags': {
            '-P': 'port',
            '-p': 'Preserves modification times, access times, and modes from the original file.',
            '-q': 'Quiet mode: disables the progress meter as well as warning and diagnostic messages from ssh(1).',
            '-r': 'Recursively copy entire directories. Note that scp follows symbolic links encountered in the tree traversal.',
            '-S': 'program',
            '-v': 'Verbose mode. Causes scp and ssh(1) to print debugging messages about their progress. This is helpful in debugging connection, authentica‐'
        },
        'examples': [
            'scp1  # secure copy (remote file copy program)',
            'scp1 -v  # Show version',
            'scp1 -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'script': {
        'desc': 'make typescript of terminal session',
        'common_flags': {
            '-a': 'Append the output to file or to typescript, retaining the prior contents.',
            '--append': 'Append the output to file or to typescript, retaining the prior contents.',
            '-c': 'command',
            '--command': 'command',
            '-E': 'when',
            '--echo': 'when',
            '-e': 'Return the exit status of the child process. Uses the same format as bash termination on signal termination (i.e., exit status is 128 + the',
            '--return': 'Return the exit status of the child process. Uses the same format as bash termination on signal termination (i.e., exit status is 128 + the',
            '-f': 'Flush output after each write. This is nice for telecooperation: one person does mkfifo foo; script -f foo, and another can supervise in',
            '--flush': 'Flush output after each write. This is nice for telecooperation: one person does mkfifo foo; script -f foo, and another can supervise in',
            '--force': 'Allow the default output file typescript to be a hard or symbolic link. The command will follow a symbolic link.',
            '-B': 'file',
            '--log-io': 'file',
            '-I': 'file',
            '--log-in': 'file'
        },
        'examples': [
            'script  # make typescript of terminal session',
            'script -a  # Show all'
        ],
        'category': 'Other'
    },
    'scriptlive': {
        'desc': 're-run session typescripts, using timing information',
        'common_flags': {
            '-I': 'file',
            '--log-in': 'file',
            '-B': 'file',
            '--log-io': 'file',
            '-E': 'when',
            '--echo': 'when',
            '-t': 'file',
            '--timing': 'file',
            '-T': 'file',
            '--log-timing': 'file',
            '-d': 'number',
            '--divisor': 'number',
            '-m': 'number',
            '--maxdelay': 'number',
            '-h': 'Display help text and exit.'
        },
        'examples': [
            'scriptlive  # re-run session typescripts, using timing informati',
            'scriptlive -h  # Show help'
        ],
        'category': 'Other'
    },
    'scriptreplay': {
        'desc': 'play back typescripts, using timing information',
        'common_flags': {
            '-I': 'file',
            '--log-in': 'file',
            '-O': 'file',
            '--log-out': 'file',
            '-B': 'file',
            '--log-io': 'file',
            '-t': 'file',
            '--timing': 'file',
            '-T': 'file',
            '--log-timing': 'file',
            '-s': 'file',
            '--typescript': 'file',
            '-c': 'mode',
            '--cr-mode': 'mode',
            '-d': 'number'
        },
        'examples': [
            'scriptreplay  # play back typescripts, using timing information'
        ],
        'category': 'Other'
    },
    'setpriv': {
        'desc': 'run a program with different Linux privilege settings',
        'common_flags': {
            '--clear-groups': 'Clear supplementary groups.',
            '-d': 'Dump the current privilege state. This option can be specified more than once to show extra, mostly useless, information. Incompatible with all',
            '--dump': 'Dump the current privilege state. This option can be specified more than once to show extra, mostly useless, information. Incompatible with all',
            '--groups': 'group...',
            '--inh-caps': '(+|-)cap..., --ambient-caps (+|-)cap..., --bounding-set (+|-)cap...',
            '--keep-groups': 'Preserve supplementary groups. Only useful in conjunction with --rgid, --egid, or --regid.',
            '--init-groups': 'Initialize supplementary groups using initgroups3. Only useful in conjunction with --ruid or --reuid.',
            '--list-caps': 'List all known capabilities. This option must be specified alone.',
            '--no-new-privs': 'Set the no_new_privs bit. With this bit set, execve(2) will not grant new privileges. For example, the set-user-ID and set-group-ID bits as well',
            '--rgid': 'gid, --egid gid, --regid gid',
            '--ruid': 'uid, --euid uid, --reuid uid',
            '--securebits': '(+|-)securebit...',
            '--pdeathsig': 'keep|clear|<signal>',
            '--ptracer': 'pid|any|none',
            '--selinux-label': 'label'
        },
        'examples': [
            'setpriv  # run a program with different Linux privilege setti'
        ],
        'category': 'Other'
    },
    'setsid': {
        'desc': 'run a program in a new session',
        'common_flags': {
            '-c': 'Set the controlling terminal to the current one.',
            '--ctty': 'Set the controlling terminal to the current one.',
            '-f': 'Always create a new process.',
            '--fork': 'Always create a new process.',
            '-w': 'Wait for the execution of the program to end, and return the exit status of this program as the exit status of setsid.',
            '--wait': 'Wait for the execution of the program to end, and return the exit status of this program as the exit status of setsid.',
            '-V': 'Display version information and exit.',
            '--version': 'Display version information and exit.',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.'
        },
        'examples': [
            'setsid  # run a program in a new session',
            'setsid -h  # Show help',
            'setsid --version  # Show version'
        ],
        'category': 'Other'
    },
    'setterm': {
        'desc': 'set terminal attributes',
        'common_flags': {
            '--underline': 'and --half-bright) are hardware-dependent.',
            '--appcursorkeys': 'on|off',
            '--append': 'console_number',
            '--background': '8-color|default',
            '--blank': '[=0-60|force|poke]',
            '--bfreq': '[=number]',
            '--blength': '[=0-2000]',
            '--blink': 'on|off',
            '--bold': 'on|off',
            '--clear': '[=all|rest]',
            '--clrtabs': '[=tab1 tab2 tab3 ...]',
            '--cursor': 'on|off',
            '--default': 'Sets the terminal’s rendering options to the default values.',
            '--dump': '[=console_number]',
            '--file': 'filename'
        },
        'examples': [
            'setterm  # set terminal attributes'
        ],
        'category': 'Other'
    },
    'sftp': {
        'desc': 'OpenSSH secure file transfer',
        'common_flags': {
            '-P': 'port',
            '-p': 'Preserves modification times, access times, and modes from the original files transferred.',
            '-q': 'Quiet mode: disables the progress meter as well as warning and diagnostic messages from ssh(1).',
            '-R': 'num_requests',
            '-r': 'Recursively copy entire directories when uploading and downloading. Note that sftp does not follow symbolic links encountered in the tree',
            '-S': 'program',
            '-s': 'subsystem | sftp_server',
            '-v': 'Raise logging level. This option is also passed to ssh.',
            '-X': 'sftp_option'
        },
        'examples': [
            'sftp  # OpenSSH secure file transfer',
            'sftp -v  # Show version',
            'sftp -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'sg': {
        'desc': 'log in to a new group',
        'common_flags': {
            '-c': '=command',
            '--command': '=command',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'sg  # log in to a new group',
            'sg -h  # Show help',
            'sg --version  # Show version'
        ],
        'category': 'Other'
    },
    'sh': {
        'desc': 'command interpreter (shell)',
        'common_flags': {
            '-r': 'file True if file exists and is readable.',
            '-l': 'also output the PID of the group leader, and just the PID and shell commands of other members of the job.',
            '-p': 'file True if file is a named pipe (FIFO).',
            '-b': 'file True if file exists and is a block special file.',
            '-c': 'file True if file exists and is a character special file.',
            '-d': 'file True if file exists and is a directory.',
            '-e': 'file True if file exists (regardless of type).',
            '-f': 'file True if file exists and is a regular file.',
            '-g': 'file True if file exists and its set group ID flag is set.',
            '-h': 'file True if file exists and is a symbolic link.',
            '-k': 'file True if file exists and its sticky bit is set.',
            '-n': 'string True if the length of string is nonzero.',
            '-s': 'file True if file exists and has a size greater than zero.',
            '-t': 'file_descriptor',
            '-u': 'file True if file exists and its set user ID flag is set.'
        },
        'examples': [
            'sh  # command interpreter (shell)',
            'sh -h  # Show help',
            'sh -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'size': {
        'desc': 'list section sizes and total size of binary files',
        'common_flags': {
            '-A': '-B',
            '-G': '--format=compatibility',
            '--help': '-h',
            '-H': '-? Show a summary of acceptable arguments and options.',
            '-d': '-o',
            '-x': '--radix=number',
            '--common': 'Print total size of common symbols in each file. When using Berkeley or GNU format these are included in the bss size.',
            '-t': '--totals',
            '--target': '=bfdname',
            '-v': '-V',
            '--version': 'Display the version number of size.',
            '-f': 'Ignored. This option is used by other versions of the size program, but it is not supported by the GNU Binutils version.'
        },
        'examples': [
            'size  # list section sizes and total size of binary files',
            'size --help  # Show help',
            'size -v  # Show version',
            'size -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'skill': {
        'desc': 'send a signal or report process status',
        'common_flags': {
            '-f': 'Fast mode. This option has not been implemented.',
            '--fast': 'Fast mode. This option has not been implemented.',
            '-i': 'Interactive use. You will be asked to approve each action.',
            '--interactive': 'Interactive use. You will be asked to approve each action.',
            '-l': 'List all signal names.',
            '--list': 'List all signal names.',
            '-L': 'List all signal names in a nice table.',
            '--table': 'List all signal names in a nice table.',
            '-n': 'No action; perform a simulation of events that would occur but do not actually change the system.',
            '--no-action': 'No action; perform a simulation of events that would occur but do not actually change the system.',
            '-v': 'Verbose; explain what is being done.',
            '--verbose': 'Verbose; explain what is being done.',
            '-w': 'Enable warnings. This option has not been implemented.',
            '--warnings': 'Enable warnings. This option has not been implemented.',
            '-h': 'Display help text and exit.'
        },
        'examples': [
            'skill  # send a signal or report process status',
            'skill -h  # Show help',
            'skill -v  # Show version',
            'skill -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'slabtop': {
        'desc': 'display kernel slab cache information in real time',
        'common_flags': {
            '-d': '=N',
            '--delay': '=N',
            '-s': '=S',
            '--sort': '=S',
            '-o': 'Display the output once and then exit.',
            '--once': 'Display the output once and then exit.',
            '-V': 'Display version information and exit.',
            '--version': 'Display version information and exit.',
            '-h': 'Display usage information and exit.',
            '--help': 'Display usage information and exit.'
        },
        'examples': [
            'slabtop  # display kernel slab cache information in real time',
            'slabtop -h  # Show help',
            'slabtop --version  # Show version'
        ],
        'category': 'Other'
    },
    'sleep': {
        'desc': 'delay for a specified amount of time',
        'common_flags': {
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'sleep  # delay for a specified amount of time',
            'sleep --help  # Show help',
            'sleep --version  # Show version'
        ],
        'category': 'Other'
    },
    'snice': {
        'desc': 'send a signal or report process status',
        'common_flags': {
            '-f': 'Fast mode. This option has not been implemented.',
            '--fast': 'Fast mode. This option has not been implemented.',
            '-i': 'Interactive use. You will be asked to approve each action.',
            '--interactive': 'Interactive use. You will be asked to approve each action.',
            '-l': 'List all signal names.',
            '--list': 'List all signal names.',
            '-L': 'List all signal names in a nice table.',
            '--table': 'List all signal names in a nice table.',
            '-n': 'No action; perform a simulation of events that would occur but do not actually change the system.',
            '--no-action': 'No action; perform a simulation of events that would occur but do not actually change the system.',
            '-v': 'Verbose; explain what is being done.',
            '--verbose': 'Verbose; explain what is being done.',
            '-w': 'Enable warnings. This option has not been implemented.',
            '--warnings': 'Enable warnings. This option has not been implemented.',
            '-h': 'Display help text and exit.'
        },
        'examples': [
            'snice  # send a signal or report process status',
            'snice -h  # Show help',
            'snice -v  # Show version',
            'snice -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'soelim': {
        'desc': 'recursively interpolate source requests in roff or other text files',
        'common_flags': {
            '--help': 'displays a usage message, while -v and --version show version information; all exit afterward.',
            '-C': 'Recognize an input line starting with .so even if a character other than a space or newline follows.',
            '-I': 'dir Search the directory dir path for input- and included-files. -I may be specified more than once; each dir is searched in the given order.',
            '-r': 'Write files “raw”; do not add lf requests.',
            '-t': 'Emit TeX comment lines starting with “%” indicating the current file and line number, rather than lf requests for the same purpose.'
        },
        'examples': [
            'soelim  # recursively interpolate source requests in roff or',
            'soelim --help  # Show help'
        ],
        'category': 'Other'
    },
    'sprof': {
        'desc': 'read and display shared object profiling data',
        'common_flags': {
            '--call-pairs': '-c Print a list of pairs of call paths for the interfaces exported by the shared object, along with the number of times each path is used.',
            '--flat-profile': '-p Generate a flat profile of all of the functions in the monitored object, with counts and ticks.',
            '--graph': '-q Generate a call graph.',
            '--help': '-? Display a summary of command-line options and arguments and exit.',
            '--usage': 'Display a short usage message and exit.',
            '--version': '-V Display the program version and exit.'
        },
        'examples': [
            'sprof  # read and display shared object profiling data',
            'sprof --help  # Show help',
            'sprof --version  # Show version'
        ],
        'category': 'Other'
    },
    'sq': {
        'desc': 'A command-line frontend for Sequoia, an implementation of OpenPGP',
        'common_flags': {
            '--batch': 'Prevents any kind of prompting',
            '--cert-store': '=PATH',
            '--cli-version': '=CLI_VERSION',
            '-h': 'Print help (see a summary with \'-h\')',
            '--help': 'Print help (see a summary with \'-h\')',
            '--home': '=PATH',
            '--key-store': '=PATH',
            '--keyring': '=PATH',
            '--known-notation': '=NOTATION',
            '--overwrite': 'Overwrite existing files',
            '--password-file': '=FILE',
            '--policy-as-of': '=TIME',
            '-q': 'Be more quiet',
            '--quiet': 'Be more quiet',
            '--time': '=TIME'
        },
        'examples': [
            'sq  # A command-line frontend for Sequoia, an implementa',
            'sq -h  # Show help'
        ],
        'category': 'Other'
    },
    'sq-cert-export': {
        'desc': 'Export certificates from the local certificate store',
        'common_flags': {
            '--all': 'Export all certificates',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-domain': '=DOMAIN',
            '--cert-email': '=EMAIL',
            '--cert-grep': '=PATTERN',
            '--cert-userid': '=USERID',
            '--local': 'Export local (non-exportable) signatures',
            '--output': '=FILE'
        },
        'examples': [
            'sq-cert-export  # Export certificates from the local certificate sto',
            'sq-cert-export --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-cert-lint': {
        'desc': 'Check certificates for issues',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-domain': '=DOMAIN',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-grep': '=PATTERN',
            '--cert-userid': '=USERID',
            '--fix': 'Attempts to fix certificates, when possible',
            '--output': '=FILE'
        },
        'examples': [
            'sq-cert-lint  # Check certificates for issues'
        ],
        'category': 'Other'
    },
    'sq-cert-list': {
        'desc': 'List certificates and user IDs',
        'common_flags': {
            '--amount': '=AMOUNT',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-domain': '=DOMAIN',
            '--cert-email': '=EMAIL',
            '--cert-grep': '=PATTERN',
            '--cert-userid': '=USERID',
            '--certification-network': 'Treats the network as a certification network',
            '--gossip': 'Treats all certificates as unreliable trust roots',
            '--show-paths': 'Show why a binding is authenticated',
            '--unusable': 'Show bindings that are unusable'
        },
        'examples': [
            'sq-cert-list  # List certificates and user IDs'
        ],
        'category': 'Other'
    },
    'sq-config-template': {
        'desc': 'Write a template configuration file',
        'common_flags': {
            '--output': '=FILE'
        },
        'examples': [
            'sq-config-template  # Write a template configuration file'
        ],
        'category': 'Other'
    },
    'sq-decrypt': {
        'desc': 'Decrypt a message',
        'common_flags': {
            '--dump-session-key': 'Print the session key to stderr',
            '--output': '=FILE',
            '--recipient-file': '=KEY_FILE',
            '--session-key': '=SESSION-KEY',
            '--signatures': '=N',
            '--signer': '=FINGERPRINT|KEYID',
            '--signer-domain': '=DOMAIN',
            '--signer-email': '=EMAIL',
            '--signer-file': '=PATH',
            '--signer-userid': '=USERID'
        },
        'examples': [
            'sq-decrypt  # Decrypt a message'
        ],
        'category': 'Other'
    },
    'sq-download': {
        'desc': 'Download and authenticate the data',
        'common_flags': {
            '--cleartext': 'Verify a cleartext-signed message',
            '--message': 'Verify an inline signed message',
            '--output': '=FILE',
            '--signature-url': '=URL',
            '--signatures': '=N',
            '--signer': '=FINGERPRINT|KEYID',
            '--signer-domain': '=DOMAIN',
            '--signer-email': '=EMAIL',
            '--signer-file': '=PATH',
            '--signer-userid': '=USERID',
            '--url': '=URL'
        },
        'examples': [
            'sq-download  # Download and authenticate the data'
        ],
        'category': 'Other'
    },
    'sq-encrypt': {
        'desc': 'Encrypt a message',
        'common_flags': {
            '--binary': 'Emit binary data',
            '--compression': '=KIND',
            '--encrypt-for': '=PURPOSE',
            '--for': '=FINGERPRINT|KEYID',
            '--for-email': '=EMAIL',
            '--for-file': '=PATH',
            '--for-self': 'Encrypt the message for yourself',
            '--for-userid': '=USERID',
            '--output': '=FILE',
            '--profile': '=PROFILE',
            '--set-metadata-filename': '=SET_METADATA_FILENAME',
            '--signature-notation': 'NAME VALUE',
            '--signer': '=FINGERPRINT|KEYID',
            '--signer-email': '=EMAIL',
            '--signer-file': '=PATH'
        },
        'examples': [
            'sq-encrypt  # Encrypt a message'
        ],
        'category': 'Other'
    },
    'sq-inspect': {
        'desc': 'Inspect data, like file(1)',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-domain': '=DOMAIN',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-grep': '=PATTERN',
            '--cert-userid': '=USERID',
            '--certifications': 'Print third-party certifications',
            '--dump-bad-signatures': 'Dump signatures that are definitively bad'
        },
        'examples': [
            'sq-inspect  # Inspect data, like file(1)'
        ],
        'category': 'Other'
    },
    'sq-key-approvals-list': {
        'desc': 'Lists third-party certifications and their approval status',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--email': '=EMAIL',
            '--pending': 'List unapproved certifications',
            '--userid': '=USERID'
        },
        'examples': [
            'sq-key-approvals-list  # Lists third-party certifications and their approva'
        ],
        'category': 'Other'
    },
    'sq-key-approvals-update': {
        'desc': 'Approves of third-party certifications allowing for their distribution',
        'common_flags': {
            '--add-all': 'Approve of all pending certifications',
            '--add-authenticated': 'Approve of all certifications by authenticated certifiers',
            '--add-by': '=FINGERPRINT|KEYID',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--email': '=EMAIL',
            '--output': '=FILE',
            '--remove-all': 'Remove all prior approvals',
            '--remove-by': '=FINGERPRINT|KEYID',
            '--userid': '=USERID'
        },
        'examples': [
            'sq-key-approvals-update  # Approves of third-party certifications allowing fo'
        ],
        'category': 'Other'
    },
    'sq-key-delete': {
        'desc': 'Delete a certificate\'s secret key material',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--output': '=FILE'
        },
        'examples': [
            'sq-key-delete  # Delete a certificate\'s secret key material'
        ],
        'category': 'Other'
    },
    'sq-key-expire': {
        'desc': 'Change a certificate\'s expiration time',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--expiration': '=EXPIRATION',
            '--output': '=FILE'
        },
        'examples': [
            'sq-key-expire  # Change a certificate\'s expiration time'
        ],
        'category': 'Other'
    },
    'sq-key-export': {
        'desc': 'Export keys from the key store',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-domain': '=DOMAIN',
            '--cert-email': '=EMAIL',
            '--cert-grep': '=PATTERN',
            '--cert-userid': '=USERID',
            '--output': '=FILE'
        },
        'examples': [
            'sq-key-export  # Export keys from the key store'
        ],
        'category': 'Other'
    },
    'sq-key-generate': {
        'desc': 'Generate a new key',
        'common_flags': {
            '--allow-non-canonical-userids': 'Don\'t reject user IDs that are not in canonical form',
            '--can-authenticate': 'Add an authentication-capable subkey (default)',
            '--can-encrypt': '=PURPOSE',
            '--can-sign': 'Add a signing-capable subkey (default)',
            '--cannot-authenticate': 'Don\'t add an authentication-capable subkey',
            '--cannot-encrypt': 'Don\'t add an encryption-capable subkey',
            '--cannot-sign': 'Don\'t add a signing-capable subkey',
            '--cipher-suite': '=CIPHER-SUITE',
            '--email': '=ADDRESS',
            '--expiration': '=EXPIRATION',
            '--name': '=NAME',
            '--new-password-file': '=PASSWORD_FILE',
            '--no-userids': 'Create a key without any user IDs',
            '--output': '=FILE',
            '--own-key': 'Mark the key as one\'s own key'
        },
        'examples': [
            'sq-key-generate  # Generate a new key'
        ],
        'category': 'Other'
    },
    'sq-key-list': {
        'desc': 'List keys managed by the key store',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-domain': '=DOMAIN',
            '--cert-email': '=EMAIL',
            '--cert-grep': '=PATTERN',
            '--cert-userid': '=USERID'
        },
        'examples': [
            'sq-key-list  # List keys managed by the key store'
        ],
        'category': 'Other'
    },
    'sq-key-password': {
        'desc': 'Change the password protecting secret key material',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--clear-password': 'Clear the password protecting the secret key material',
            '--new-password-file': '=PASSWORD_FILE',
            '--output': '=FILE'
        },
        'examples': [
            'sq-key-password  # Change the password protecting secret key material'
        ],
        'category': 'Other'
    },
    'sq-key-revoke': {
        'desc': 'Revoke a certificate',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--message': '=MESSAGE',
            '--output': '=FILE',
            '--reason': '=REASON',
            '--revoker': '=FINGERPRINT|KEYID',
            '--revoker-email': '=EMAIL',
            '--revoker-file': '=PATH',
            '--revoker-userid': '=USERID',
            '--signature-notation': 'NAME VALUE'
        },
        'examples': [
            'sq-key-revoke  # Revoke a certificate'
        ],
        'category': 'Other'
    },
    'sq-key-rotate': {
        'desc': 'Rotate a certificate',
        'common_flags': {
            '--can-authenticate': 'Add an authentication-capable subkey',
            '--can-encrypt': '=PURPOSE',
            '--can-sign': 'Add a signing-capable subkey',
            '--cannot-authenticate': 'Don\'t add an authentication-capable subkey',
            '--cannot-encrypt': 'Don\'t add an encryption-capable subkey',
            '--cannot-sign': 'Don\'t add a signing-capable subkey',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--cipher-suite': '=CIPHER-SUITE',
            '--expiration': '=EXPIRATION',
            '--new-password-file': '=PASSWORD_FILE',
            '--output': '=FILE',
            '--own-key': 'Mark the key as one\'s own key'
        },
        'examples': [
            'sq-key-rotate  # Rotate a certificate'
        ],
        'category': 'Other'
    },
    'sq-key-subkey-add': {
        'desc': 'Add a new subkey to a certificate',
        'common_flags': {
            '--can-authenticate': 'Add an authentication-capable subkey',
            '--can-encrypt': '=PURPOSE',
            '--can-sign': 'Add a signing-capable subkey',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--cipher-suite': '=CIPHER-SUITE',
            '--expiration': '=EXPIRATION',
            '--new-password-file': '=PASSWORD_FILE',
            '--output': '=FILE',
            '--without-password': 'Don\'t protect the subkey\'s secret key material with a password'
        },
        'examples': [
            'sq-key-subkey-add  # Add a new subkey to a certificate'
        ],
        'category': 'Other'
    },
    'sq-key-subkey-bind': {
        'desc': 'Bind keys from one certificate to another',
        'common_flags': {
            '--allow-broken-crypto': 'Allow adopting keys from certificates using broken cryptography',
            '--can-authenticate': 'Set the authentication-capable flag',
            '--can-encrypt': '=PURPOSE',
            '--can-sign': 'Set the signing-capable flag',
            '--cannot-authenticate': 'Don\'t set the authentication-capable flag',
            '--cannot-encrypt': 'Don\'t set the encryption-capable flag',
            '--cannot-sign': 'Don\'t set the signing-capable flag',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--creation-time': '=CREATION_TIME',
            '--expiration': '=EXPIRATION',
            '--key': '=KEY',
            '--output': '=FILE'
        },
        'examples': [
            'sq-key-subkey-bind  # Bind keys from one certificate to another'
        ],
        'category': 'Other'
    },
    'sq-key-subkey-delete': {
        'desc': 'Delete a certificate\'s secret key material',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--key': '=FINGERPRINT|KEYID',
            '--output': '=FILE'
        },
        'examples': [
            'sq-key-subkey-delete  # Delete a certificate\'s secret key material'
        ],
        'category': 'Other'
    },
    'sq-key-subkey-expire': {
        'desc': 'Change a subkey\'s expiration time',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--expiration': '=EXPIRATION',
            '--key': '=FINGERPRINT|KEYID',
            '--output': '=FILE'
        },
        'examples': [
            'sq-key-subkey-expire  # Change a subkey\'s expiration time'
        ],
        'category': 'Other'
    },
    'sq-key-subkey-export': {
        'desc': 'Export secret key material from the secret key store',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-userid': '=USERID',
            '--key': '=FINGERPRINT|KEYID',
            '--output': '=FILE'
        },
        'examples': [
            'sq-key-subkey-export  # Export secret key material from the secret key sto'
        ],
        'category': 'Other'
    },
    'sq-key-subkey-password': {
        'desc': 'Change the password protecting secret key material',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--clear-password': 'Clear the password protecting the secret key material',
            '--key': '=FINGERPRINT|KEYID',
            '--new-password-file': '=PASSWORD_FILE',
            '--output': '=FILE'
        },
        'examples': [
            'sq-key-subkey-password  # Change the password protecting secret key material'
        ],
        'category': 'Other'
    },
    'sq-key-subkey-revoke': {
        'desc': 'Revoke a subkey',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--key': '=FINGERPRINT|KEYID',
            '--message': '=MESSAGE',
            '--output': '=FILE',
            '--reason': '=REASON',
            '--revoker': '=FINGERPRINT|KEYID',
            '--revoker-email': '=EMAIL',
            '--revoker-file': '=PATH',
            '--revoker-userid': '=USERID',
            '--signature-notation': 'NAME VALUE'
        },
        'examples': [
            'sq-key-subkey-revoke  # Revoke a subkey'
        ],
        'category': 'Other'
    },
    'sq-key-userid-add': {
        'desc': 'Add a user ID',
        'common_flags': {
            '--allow-non-canonical-userids': 'Don\'t reject user IDs that are not in canonical form',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--email': '=ADDRESS',
            '--name': '=NAME',
            '--output': '=FILE',
            '--userid': '=USERID'
        },
        'examples': [
            'sq-key-userid-add  # Add a user ID'
        ],
        'category': 'Other'
    },
    'sq-key-userid-revoke': {
        'desc': 'Revoke a user ID',
        'common_flags': {
            '--add-email': '=EMAIL',
            '--add-userid': '=USERID',
            '--allow-non-canonical-userids': 'Don\'t reject new user IDs that are not in canonical form',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--email': '=EMAIL',
            '--message': '=MESSAGE',
            '--output': '=FILE',
            '--reason': '=REASON',
            '--revoker': '=FINGERPRINT|KEYID',
            '--revoker-email': '=EMAIL',
            '--revoker-file': '=PATH',
            '--revoker-userid': '=USERID'
        },
        'examples': [
            'sq-key-userid-revoke  # Revoke a user ID'
        ],
        'category': 'Other'
    },
    'sq-keyring-filter': {
        'desc': 'Join keys into a keyring applying a filter',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--domain': '=FQDN',
            '--email': '=ADDRESS',
            '--experimental': 'Opt-in to using an experimental feature',
            '--key': '=FINGERPRINT|KEYID',
            '--name': '=NAME',
            '--output': '=FILE',
            '--prune-certs': 'Remove certificate components not matching the filter',
            '--to-cert': 'Convert any keys in the input to certificates',
            '--userid': '=USERID'
        },
        'examples': [
            'sq-keyring-filter  # Join keys into a keyring applying a filter'
        ],
        'category': 'Other'
    },
    'sq-keyring-list': {
        'desc': 'List keys in a keyring',
        'common_flags': {
            '--all-userids': 'List all user IDs'
        },
        'examples': [
            'sq-keyring-list  # List keys in a keyring'
        ],
        'category': 'Other'
    },
    'sq-keyring-merge': {
        'desc': 'Merge keys or keyrings into a single keyring',
        'common_flags': {
            '--output': '=FILE'
        },
        'examples': [
            'sq-keyring-merge  # Merge keys or keyrings into a single keyring'
        ],
        'category': 'Other'
    },
    'sq-keyring-split': {
        'desc': 'Split a keyring into individual keys',
        'common_flags': {
            '--prefix': '=PREFIX'
        },
        'examples': [
            'sq-keyring-split  # Split a keyring into individual keys'
        ],
        'category': 'Other'
    },
    'sq-network-dane-generate': {
        'desc': 'Generate DANE records for the given domain and certs',
        'common_flags': {
            '--all': 'Publish authenticated certs with a user ID matching domain',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--domain': '=FQDN',
            '--size-limit': '=BYTES',
            '--ttl': '=DURATION',
            '--type': '=TYPE'
        },
        'examples': [
            'sq-network-dane-generate  # Generate DANE records for the given domain and cer',
            'sq-network-dane-generate --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-network-dane-search': {
        'desc': 'Retrieve certificates using DANE',
        'common_flags': {
            '--all': 'Fetch updates for all known certificates',
            '--output': '=FILE'
        },
        'examples': [
            'sq-network-dane-search  # Retrieve certificates using DANE',
            'sq-network-dane-search --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-network-keyserver-publish': {
        'desc': 'Publish certificates on key servers',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-domain': '=DOMAIN',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--server': '=URI'
        },
        'examples': [
            'sq-network-keyserver-publish  # Publish certificates on key servers'
        ],
        'category': 'Other'
    },
    'sq-network-keyserver-search': {
        'desc': 'Retrieve certificates from key servers',
        'common_flags': {
            '--all': 'Fetch updates for all known certificates',
            '--output': '=FILE',
            '--server': '=URI'
        },
        'examples': [
            'sq-network-keyserver-search  # Retrieve certificates from key servers',
            'sq-network-keyserver-search --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-network-search': {
        'desc': 'Retrieve certificates using all supported network services',
        'common_flags': {
            '--all': 'Fetch updates for all known certificates',
            '--iterations': '=N',
            '--output': '=FILE',
            '--server': '=URI',
            '--use-dane': '=ENABLE',
            '--use-wkd': '=ENABLE'
        },
        'examples': [
            'sq-network-search  # Retrieve certificates using all supported network ',
            'sq-network-search --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-network-wkd-publish': {
        'desc': 'Publish certificates in a Web Key Directory',
        'common_flags': {
            '--all': 'Publish authenticated certs with a user ID matching domain',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--create': 'Create the WKD hierarchy if it does not exist yet',
            '--domain': '=FQDN',
            '--method': '=METHOD',
            '--rsync': 'Use rsync(1) to access DEST',
            '--rsync-path': '=RSYNC'
        },
        'examples': [
            'sq-network-wkd-publish  # Publish certificates in a Web Key Directory',
            'sq-network-wkd-publish --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-network-wkd-search': {
        'desc': 'Retrieve certificates from a Web Key Directory',
        'common_flags': {
            '--all': 'Fetch updates for all known certificates',
            '--output': '=FILE'
        },
        'examples': [
            'sq-network-wkd-search  # Retrieve certificates from a Web Key Directory',
            'sq-network-wkd-search --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-packet-armor': {
        'desc': 'Convert binary to ASCII',
        'common_flags': {
            '--label': '=LABEL',
            '--output': '=FILE'
        },
        'examples': [
            'sq-packet-armor  # Convert binary to ASCII'
        ],
        'category': 'Other'
    },
    'sq-packet-dearmor': {
        'desc': 'Convert ASCII to binary',
        'common_flags': {
            '--output': '=FILE'
        },
        'examples': [
            'sq-packet-dearmor  # Convert ASCII to binary'
        ],
        'category': 'Other'
    },
    'sq-packet-decrypt': {
        'desc': 'Unwrap an encryption container',
        'common_flags': {
            '--binary': 'Emit binary data',
            '--dump-session-key': 'Print the session key to stderr',
            '--output': '=FILE',
            '--recipient-file': '=KEY_FILE',
            '--session-key': '=SESSION-KEY'
        },
        'examples': [
            'sq-packet-decrypt  # Unwrap an encryption container'
        ],
        'category': 'Other'
    },
    'sq-packet-dump': {
        'desc': 'List packets',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--hex': 'Print a hexdump',
            '--mpis': 'Print cryptographic artifacts',
            '--output': '=FILE',
            '--recipient-file': '=KEY_FILE',
            '--session-key': '=SESSION-KEY'
        },
        'examples': [
            'sq-packet-dump  # List packets'
        ],
        'category': 'Other'
    },
    'sq-packet-join': {
        'desc': 'Join packets split across files',
        'common_flags': {
            '--binary': 'Emit binary data',
            '--label': '=LABEL',
            '--output': '=FILE'
        },
        'examples': [
            'sq-packet-join  # Join packets split across files'
        ],
        'category': 'Other'
    },
    'sq-packet-split': {
        'desc': 'Split a message into packets',
        'common_flags': {
            '--binary': 'Emit binary data',
            '--output': '=FILE',
            '--output-prefix': '=PREFIX'
        },
        'examples': [
            'sq-packet-split  # Split a message into packets'
        ],
        'category': 'Other'
    },
    'sq-pki-authenticate': {
        'desc': 'Authenticate a binding',
        'common_flags': {
            '--amount': '=AMOUNT',
            '--cert': '=FINGERPRINT|KEYID',
            '--certification-network': 'Treats the network as a certification network',
            '--email': '=EMAIL',
            '--gossip': 'Treats all certificates as unreliable trust roots',
            '--show-paths': 'Show why a binding is authenticated',
            '--unusable': 'Show bindings that are unusable',
            '--userid': '=USERID'
        },
        'examples': [
            'sq-pki-authenticate  # Authenticate a binding'
        ],
        'category': 'Other'
    },
    'sq-pki-identify': {
        'desc': 'Identify a certificate',
        'common_flags': {
            '--amount': '=AMOUNT',
            '--cert': '=FINGERPRINT|KEYID',
            '--certification-network': 'Treats the network as a certification network',
            '--gossip': 'Treats all certificates as unreliable trust roots',
            '--show-paths': 'Show why a binding is authenticated',
            '--unusable': 'Show bindings that are unusable'
        },
        'examples': [
            'sq-pki-identify  # Identify a certificate'
        ],
        'category': 'Other'
    },
    'sq-pki-link-add': {
        'desc': 'Link a certificate and a user ID',
        'common_flags': {
            '--add-email': '=EMAIL',
            '--add-userid': '=USERID',
            '--all': 'Use all self-signed user IDs',
            '--allow-non-canonical-userids': 'Don\'t reject new user IDs that are not in canonical form',
            '--amount': '=AMOUNT',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-special': '=SPECIAL',
            '--email': '=EMAIL',
            '--expiration': '=EXPIRATION',
            '--recreate': 'Recreate signature even if the parameters did not change',
            '--signature-notation': 'NAME VALUE',
            '--temporary': 'Temporarily accepts the binding',
            '--userid': '=USERID',
            '--userid-by-email': '=EMAIL'
        },
        'examples': [
            'sq-pki-link-add  # Link a certificate and a user ID',
            'sq-pki-link-add --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-pki-link-authorize': {
        'desc': 'Make a certificate a trusted introducer',
        'common_flags': {
            '--add-email': '=EMAIL',
            '--add-userid': '=USERID',
            '--all': 'Use all self-signed user IDs',
            '--allow-non-canonical-userids': 'Don\'t reject new user IDs that are not in canonical form',
            '--amount': '=AMOUNT',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-special': '=SPECIAL',
            '--depth': '=TRUST_DEPTH',
            '--domain': '=DOMAIN',
            '--email': '=EMAIL',
            '--expiration': '=EXPIRATION',
            '--recreate': 'Recreate the signature even if the parameters did not change',
            '--regex': '=REGEX',
            '--signature-notation': 'NAME VALUE',
            '--unconstrained': 'Don\'t constrain the introducer'
        },
        'examples': [
            'sq-pki-link-authorize  # Make a certificate a trusted introducer',
            'sq-pki-link-authorize --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-pki-link-list': {
        'desc': 'List links',
        'common_flags': {
            '--ca': 'Only lists bindings linked as CAs',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-domain': '=DOMAIN',
            '--cert-email': '=EMAIL',
            '--cert-grep': '=PATTERN',
            '--cert-userid': '=USERID'
        },
        'examples': [
            'sq-pki-link-list  # List links'
        ],
        'category': 'Other'
    },
    'sq-pki-link-retract': {
        'desc': 'Retract links',
        'common_flags': {
            '--all': 'Use all self-signed user IDs',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-special': '=SPECIAL',
            '--email': '=EMAIL',
            '--recreate': 'Recreate signature even if the parameters did not change',
            '--signature-notation': 'NAME VALUE',
            '--userid': '=USERID',
            '--userid-by-email': '=EMAIL'
        },
        'examples': [
            'sq-pki-link-retract  # Retract links',
            'sq-pki-link-retract --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-pki-lookup': {
        'desc': 'Lookup the certificates associated with a User ID',
        'common_flags': {
            '--amount': '=AMOUNT',
            '--certification-network': 'Treats the network as a certification network',
            '--email': '=EMAIL',
            '--gossip': 'Treats all certificates as unreliable trust roots',
            '--show-paths': 'Show why a binding is authenticated',
            '--unusable': 'Show bindings that are unusable',
            '--userid': '=USERID'
        },
        'examples': [
            'sq-pki-lookup  # Lookup the certificates associated with a User ID'
        ],
        'category': 'Other'
    },
    'sq-pki-path': {
        'desc': 'Verify the specified path',
        'common_flags': {
            '--amount': '=AMOUNT',
            '--certification-network': 'Treats the network as a certification network',
            '--email': '=EMAIL',
            '--userid': '=USERID',
            '--userid-by-email': '=EMAIL'
        },
        'examples': [
            'sq-pki-path  # Verify the specified path'
        ],
        'category': 'Other'
    },
    'sq-pki-vouch-add': {
        'desc': 'Certify a User ID for a Certificate',
        'common_flags': {
            '--add-email': '=EMAIL',
            '--add-userid': '=USERID',
            '--all': 'Use all self-signed user IDs',
            '--allow-non-canonical-userids': 'Don\'t reject new user IDs that are not in canonical form',
            '--amount': '=AMOUNT',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-file': '=PATH',
            '--certifier': '=FINGERPRINT|KEYID',
            '--certifier-email': '=EMAIL',
            '--certifier-file': '=PATH',
            '--certifier-self': 'Create the certification using your default certification key',
            '--certifier-userid': '=USERID',
            '--email': '=EMAIL',
            '--expiration': '=EXPIRATION',
            '--local': 'Make the certification a local certification'
        },
        'examples': [
            'sq-pki-vouch-add  # Certify a User ID for a Certificate',
            'sq-pki-vouch-add --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-pki-vouch-authorize': {
        'desc': 'Mark a certificate as a trusted introducer',
        'common_flags': {
            '--add-email': '=EMAIL',
            '--add-userid': '=USERID',
            '--all': 'Use all self-signed user IDs',
            '--allow-non-canonical-userids': 'Don\'t reject new user IDs that are not in canonical form',
            '--amount': '=AMOUNT',
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-file': '=PATH',
            '--certifier': '=FINGERPRINT|KEYID',
            '--certifier-email': '=EMAIL',
            '--certifier-file': '=PATH',
            '--certifier-self': 'Create the certification using your default certification key',
            '--certifier-userid': '=USERID',
            '--depth': '=TRUST_DEPTH',
            '--domain': '=DOMAIN',
            '--email': '=EMAIL'
        },
        'examples': [
            'sq-pki-vouch-authorize  # Mark a certificate as a trusted introducer',
            'sq-pki-vouch-authorize --all  # Show all'
        ],
        'category': 'Other'
    },
    'sq-pki-vouch-list': {
        'desc': 'List certifications',
        'common_flags': {
            '--cert': '=FINGERPRINT|KEYID',
            '--cert-email': '=EMAIL',
            '--cert-file': '=PATH',
            '--cert-userid': '=USERID',
            '--certifier': '=FINGERPRINT|KEYID',
            '--certifier-email': '=EMAIL',
            '--certifier-file': '=PATH',
            '--certifier-self': 'Create the certification using your default certification key',
            '--certifier-special': '=SPECIAL',
            '--certifier-userid': '=USERID'
        },
        'examples': [
            'sq-pki-vouch-list  # List certifications'
        ],
        'category': 'Other'
    },
    'sq-pki-vouch-replay': {
        'desc': 'Replays vouches',
        'common_flags': {
            '--allow-dissimilar-userids': 'Don\'t check that the source and target share a self-signed user ID',
            '--output': '=FILE',
            '--source': '=FINGERPRINT|KEYID',
            '--source-email': '=EMAIL',
            '--source-file': '=PATH',
            '--source-userid': '=USERID',
            '--target': '=FINGERPRINT|KEYID',
            '--target-email': '=EMAIL',
            '--target-file': '=PATH',
            '--target-userid': '=USERID'
        },
        'examples': [
            'sq-pki-vouch-replay  # Replays vouches'
        ],
        'category': 'Other'
    },
    'sq-sign': {
        'desc': 'Sign messages or data files',
        'common_flags': {
            '--append': 'Append a signature to existing signature',
            '--binary': 'Emit binary data',
            '--cleartext': 'Create a cleartext-signed message',
            '--merge': '=SIGNED-MESSAGE',
            '--message': 'Create an inline-signed message',
            '--mode': '=MODE',
            '--output': '=FILE',
            '--signature-file': '=SIG',
            '--signature-notation': 'NAME VALUE',
            '--signer': '=FINGERPRINT|KEYID',
            '--signer-email': '=EMAIL',
            '--signer-file': '=PATH',
            '--signer-self': 'Sign using your default signer keys',
            '--signer-userid': '=USERID'
        },
        'examples': [
            'sq-sign  # Sign messages or data files'
        ],
        'category': 'Other'
    },
    'sq-verify': {
        'desc': 'Verify signed messages or detached signatures',
        'common_flags': {
            '--cleartext': 'Verify a cleartext-signed message',
            '--message': 'Verify an inline signed message',
            '--output': '=FILE',
            '--signature-file': '=SIG',
            '--signatures': '=N',
            '--signer': '=FINGERPRINT|KEYID',
            '--signer-domain': '=DOMAIN',
            '--signer-email': '=EMAIL',
            '--signer-file': '=PATH',
            '--signer-userid': '=USERID'
        },
        'examples': [
            'sq-verify  # Verify signed messages or detached signatures'
        ],
        'category': 'Other'
    },
    'sqv': {
        'desc': 'An OpenPGP signature verification tool',
        'common_flags': {
            '-V': 'Print version',
            '--version': 'Print version',
            '--cleartext': 'Verify a cleartext-signed message',
            '-h': 'Print help (see a summary with \'-h\')',
            '--help': 'Print help (see a summary with \'-h\')',
            '--keyring': '=FILE',
            '--message': 'Verify an inline signed message',
            '-n': '=N',
            '--signatures': '=N',
            '--not-after': '=TIMESTAMP',
            '--not-before': '=TIMESTAMP',
            '--output': '=FILE',
            '--policy-as-of': '=TIMESTAMP',
            '--signature-file': '=SIG',
            '-v': 'Be verbose'
        },
        'examples': [
            'sqv  # An OpenPGP signature verification tool',
            'sqv -h  # Show help',
            'sqv -v  # Show version',
            'sqv -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'ssh': {
        'desc': 'OpenSSH remote login client',
        'common_flags': {
            '-P': 'tag Specify a tag name that may be used to select configuration in ssh_config(5). Refer to the Tag and Match keywords in ssh_config(5) for more',
            '-p': 'port',
            '-Q': 'query_option',
            '-q': 'Quiet mode. Causes most warning and diagnostic messages to be suppressed.',
            '-R': '[bind_address:]port',
            '-S': 'ctl_path',
            '-s': 'May be used to request invocation of a subsystem on the remote system. Subsystems facilitate the use of SSH as a secure transport for other',
            '-T': 'Disable pseudo-terminal allocation.',
            '-t': 'Force pseudo-terminal allocation. This can be used to execute arbitrary screen-based programs on a remote machine, which can be very use‐',
            '-V': 'Display the version number and exit.',
            '-v': 'Verbose mode. Causes ssh to print debugging messages about its progress. This is helpful in debugging connection, authentication, and con‐',
            '-W': 'host:port',
            '-w': 'local_tun[:remote_tun]',
            '-X': 'Enables X11 forwarding. This can also be specified on a per-host basis in a configuration file.',
            '-x': 'Disables X11 forwarding.'
        },
        'examples': [
            'ssh  # OpenSSH remote login client',
            'ssh user@host  # Connect to remote host',
            'ssh -p 2222 user@host  # Custom port',
            'ssh user@host \'command\'  # Execute remote command'
        ],
        'category': 'Other'
    },
    'ssh-add': {
        'desc': 'adds private key identities to the OpenSSH authentication agent',
        'common_flags': {
            '-X': 'Unlock the agent.',
            '-x': 'Lock the agent with a password.'
        },
        'examples': [
            'ssh-add  # adds private key identities to the OpenSSH authent'
        ],
        'category': 'Other'
    },
    'ssh-agent': {
        'desc': 'OpenSSH authentication agent',
        'common_flags': {
            '-P': 'allowed_providers',
            '-S': 'or -s options to ssh-add(1). Libraries that do not match the pattern list will be refused. The default list is',
            '-s': 'Generate Bourne shell commands on standard output. This is the default if SHELL does not look like it\'s a csh style of shell.',
            '-t': 'life'
        },
        'examples': [
            'ssh-agent  # OpenSSH authentication agent'
        ],
        'category': 'Other'
    },
    'ssh-copy-id': {
        'desc': 'use locally available keys to authorise logins on a remote machine',
        'common_flags': {
            '-x': 'This option is for debugging the ssh-copy-id script itself. It sets the shell\'s -x flag, so that you can see the commands being run.',
            '-h': ', -? Print Usage summary'
        },
        'examples': [
            'ssh-copy-id  # use locally available keys to authorise logins on ',
            'ssh-copy-id -h  # Show help'
        ],
        'category': 'Other'
    },
    'ssh-keygen': {
        'desc': 'OpenSSH authentication key utility',
        'common_flags': {
            '-P': 'passphrase',
            '-p': 'Requests changing the passphrase of a private key file instead of creating a new private key. The program will prompt for the file contain‐',
            '-Q': 'Test whether keys have been revoked in a KRL. If the -l option is also specified then the contents of the KRL will be printed.',
            '-q': 'Silence ssh-keygen.',
            '-R': 'hostname | [hostname]:port',
            '-r': 'hostname',
            '-s': 'ca_key',
            '-t': 'ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa',
            '-U': 'When used in combination with -s or -Y sign, this option indicates that a CA key resides in a ssh-agent(1). See the “CERTIFICATES” section',
            '-u': 'Update a KRL. When specified with -k, keys listed via the command line are added to the existing KRL rather than a new KRL being created.',
            '-V': 'validity_interval',
            '-4': 'w:+4w',
            '-1': 'm:forever',
            '-v': 'options increase the verbosity. The maximum is 3.',
            '-w': 'provider'
        },
        'examples': [
            'ssh-keygen  # OpenSSH authentication key utility',
            'ssh-keygen -v  # Show version',
            'ssh-keygen -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'ssh-keygen1': {
        'desc': 'authentication key generation, management and conversion',
        'common_flags': {
            '-o': 'Causes ssh-keygen to save private keys using the new OpenSSH format rather than the more compatible PEM format. The new format has in‐',
            '-P': 'passphrase',
            '-p': 'Requests changing the passphrase of a private key file instead of creating a new private key. The program will prompt for the file contain‐',
            '-Q': 'Test whether keys have been revoked in a KRL.',
            '-q': 'Silence ssh-keygen.',
            '-R': 'hostname',
            '-r': 'hostname',
            '-S': 'start',
            '-s': 'ca_key',
            '-T': 'output_file',
            '-t': 'dsa | ecdsa | ed25519 | rsa | rsa1',
            '-u': 'Update a KRL. When specified with -k, keys listed via the command line are added to the existing KRL rather than a new KRL being created.',
            '-V': 'validity_interval',
            '-v': 'options increase the verbosity. The maximum is 3.',
            '-W': 'generator'
        },
        'examples': [
            'ssh-keygen1  # authentication key generation, management and conv',
            'ssh-keygen1 -v  # Show version',
            'ssh-keygen1 -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'ssh-keyscan': {
        'desc': 'gather SSH public keys from servers',
        'common_flags': {
            '-p': 'port',
            '-q': 'Quiet mode: do not print server host name and banners in comments.',
            '-T': 'timeout',
            '-t': 'type',
            '-v': 'Verbose mode: print debugging messages about progress.'
        },
        'examples': [
            'ssh-keyscan  # gather SSH public keys from servers',
            'ssh-keyscan -v  # Show version',
            'ssh-keyscan -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'ssh1': {
        'desc': 'OpenSSH SSH client (remote login program)',
        'common_flags': {
            '-p': 'port',
            '-Q': 'query_option',
            '-q': 'Quiet mode. Causes most warning and diagnostic messages to be suppressed.',
            '-R': 'remote_socket:local_socket',
            '-S': 'ctl_path',
            '-s': 'May be used to request invocation of a subsystem on the remote system. Subsystems facilitate the use of SSH as a secure transport for other',
            '-T': 'Disable pseudo-terminal allocation.',
            '-t': 'Force pseudo-terminal allocation. This can be used to execute arbitrary screen-based programs on a remote machine, which can be very use‐',
            '-V': 'Display the version number and exit.',
            '-v': 'Verbose mode. Causes ssh to print debugging messages about its progress. This is helpful in debugging connection, authentication, and con‐',
            '-W': 'host:port',
            '-w': 'local_tun[:remote_tun]',
            '-X': 'Enables X11 forwarding. This can also be specified on a per-host basis in a configuration file.',
            '-x': 'Disables X11 forwarding.',
            '-Y': 'Enables trusted X11 forwarding. Trusted X11 forwardings are not subjected to the X11 SECURITY extension controls.'
        },
        'examples': [
            'ssh1  # OpenSSH SSH client (remote login program)',
            'ssh1 -v  # Show version',
            'ssh1 -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'streamzip': {
        'desc': 'create a zip file from stdin',
        'common_flags': {
            '-z': 'ipfile=F',
            '-m': 'ethod=M',
            '-s': 'tream',
            '-0': 'means no compression and -9 for maximum compression.',
            '-1': 'Sets the compression level for \"deflate\". Ignored for all other compression methods.',
            '-2': 'Sets the compression level for \"deflate\". Ignored for all other compression methods.',
            '-3': 'Sets the compression level for \"deflate\". Ignored for all other compression methods.',
            '-4': 'Sets the compression level for \"deflate\". Ignored for all other compression methods.',
            '-5': 'Sets the compression level for \"deflate\". Ignored for all other compression methods.',
            '-6': 'Sets the compression level for \"deflate\". Ignored for all other compression methods.',
            '-7': 'Sets the compression level for \"deflate\". Ignored for all other compression methods.',
            '-8': 'Sets the compression level for \"deflate\". Ignored for all other compression methods.',
            '-9': 'Sets the compression level for \"deflate\". Ignored for all other compression methods.',
            '-v': 'ersion',
            '-h': 'elp'
        },
        'examples': [
            'streamzip  # create a zip file from stdin',
            'streamzip -h  # Show help',
            'streamzip -v  # Show version',
            'streamzip -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'strip': {
        'desc': 'discard symbols and other data from object files',
        'common_flags': {
            '-F': 'bfdname',
            '--target': '=bfdname',
            '--help': 'Show a summary of the options to strip and exit.',
            '--info': 'Display a list showing all architectures and object formats available.',
            '-I': 'bfdname',
            '--input-target': '=bfdname',
            '-O': 'bfdname',
            '--output-target': '=bfdname',
            '-R': 'sectionname',
            '--remove-section': '=.text.* --remove-section=!.text.foo',
            '--keep-section': '=sectionpattern',
            '--remove-relocations': '=.text.* --remove-relocations=!.text.foo',
            '--strip-section-headers': 'Strip section headers. This option is specific to ELF files. Implies --strip-all and --merge-notes.',
            '-s': '--strip-all',
            '-g': '-S'
        },
        'examples': [
            'strip  # discard symbols and other data from object files',
            'strip --help  # Show help'
        ],
        'category': 'Other'
    },
    'su': {
        'desc': 'run a command with substitute user and group ID',
        'common_flags': {
            '-c': 'command',
            '--command': 'command',
            '-f': 'Pass -f to the shell, which may or may not be useful, depending on the shell.',
            '--fast': 'Pass -f to the shell, which may or may not be useful, depending on the shell.',
            '-g': 'group',
            '--group': 'group',
            '-G': 'group',
            '--supp-group': 'group',
            '-m': 'Preserve the entire environment, i.e., do not set HOME, SHELL, USER or LOGNAME. This option is ignored if the option --login is specified.',
            '-p': 'Preserve the entire environment, i.e., do not set HOME, SHELL, USER or LOGNAME. This option is ignored if the option --login is specified.',
            '--preserve-environment': 'Preserve the entire environment, i.e., do not set HOME, SHELL, USER or LOGNAME. This option is ignored if the option --login is specified.',
            '-P': 'Create a pseudo-terminal for the session. The independent terminal provides better security as the user does not share a terminal with the',
            '--pty': 'Create a pseudo-terminal for the session. The independent terminal provides better security as the user does not share a terminal with the',
            '-s': 'shell',
            '--shell': 'shell'
        },
        'examples': [
            'su  # run a command with substitute user and group ID'
        ],
        'category': 'Other'
    },
    'systemctl': {
        'desc': 'Control the systemd system and service manager',
        'common_flags': {
            '-t': '=',
            '--type': '=',
            '--state': '=',
            '-p': '=',
            '--property': '=',
            '-P': 'Equivalent to --value --property=, i.e. shows the value of the property without the property name or \"=\". Note that using -P once will also',
            '-a': 'When listing units with list-units, also show inactive units and units which are following other units. When showing unit/job/manager',
            '--all': 'When listing units with list-units, also show inactive units and units which are following other units. When showing unit/job/manager',
            '-r': 'When listing units, also show units of local containers. Units of local containers will be prefixed with the container name, separated by a',
            '--recursive': 'When listing units, also show units of local containers. Units of local containers will be prefixed with the container name, separated by a',
            '--reverse': 'Show reverse dependencies between units with list-dependencies, i.e. follow dependencies of type WantedBy=, RequiredBy=, UpheldBy=, PartOf=,',
            '--after': 'With list-dependencies, show the units that are ordered before the specified unit. In other words, recursively list units following the After=',
            '--before': 'With list-dependencies, show the units that are ordered after the specified unit. In other words, recursively list units following the Before=',
            '--with-dependencies': 'When used with status, cat, list-units, and list-unit-files, those commands print all specified units and the dependencies of those units.',
            '-l': 'Do not ellipsize unit names, process tree entries, journal output, or truncate unit descriptions in the output of status, list-units, list-jobs,'
        },
        'examples': [
            'systemctl  # Control the systemd system and service manager',
            'systemctl -a  # Show all'
        ],
        'category': 'Other'
    },
    'systemd-ac-power': {
        'desc': 'Report whether we are connected to an external power source',
        'common_flags': {
            '-v': 'Show result as text instead of just returning success or failure.',
            '--verbose': 'Show result as text instead of just returning success or failure.',
            '--low': 'Instead of showing AC power state, show low battery state. In this case will return zero if all batteries are currently discharging and below 5%',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-ac-power  # Report whether we are connected to an external pow',
            'systemd-ac-power -h  # Show help',
            'systemd-ac-power -v  # Show version',
            'systemd-ac-power -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'systemd-analyze': {
        'desc': 'Analyze and debug system manager',
        'common_flags': {
            '--system': 'Operates on the system systemd instance. This is the implied default.',
            '--user': 'Operates on the user systemd instance.',
            '--global': 'Operates on the system-wide configuration for user systemd instance.',
            '--order': 'When used in conjunction with the dot command (see above), selects which dependencies are shown in the dependency graph. If --order is passed,',
            '--require': 'When used in conjunction with the dot command (see above), selects which dependencies are shown in the dependency graph. If --order is passed,',
            '--from-pattern': '=, --to-pattern=',
            '--fuzz': '=timespan',
            '--man': '=no',
            '--generators': 'Invoke unit generators, see systemd.generator(7). Some generators require root privileges. Under a normal user, running with generators enabled',
            '--instance': '=NAME',
            '--recursive-errors': '=MODE',
            '--root': '=PATH',
            '--image': '=, see above. If not specified defaults to the \"*\" policy, i.e. all recognized file systems in the image are used.',
            '--image-policy': '=policy',
            '--offline': '=BOOL'
        },
        'examples': [
            'systemd-analyze  # Analyze and debug system manager'
        ],
        'category': 'Other'
    },
    'systemd-ask-password': {
        'desc': 'Query the user for a system password',
        'common_flags': {
            '--icon': '=',
            '--id': '=',
            '--keyname': '=',
            '--credential': '=',
            '--timeout': '=',
            '--echo': 'Equivalent to --echo=yes, see above.',
            '-e': 'Equivalent to --echo=yes, see above.',
            '--emoji': '=yes|no|auto',
            '--no-tty': 'Never ask for password on current TTY even if one is available. Always use agent system.',
            '--accept-cached': 'If passed, accept cached passwords, i.e. passwords previously entered.',
            '--multiple': 'When used in conjunction with --accept-cached accept multiple passwords. This will output one password per line.',
            '--no-output': 'Do not print passwords to standard output. This is useful if you want to store a password in kernel keyring with --keyname= but do not want it',
            '-n': 'By default, when the acquired password is written to standard output it is suffixed by a newline character. This may be turned off with the -n',
            '--user': 'Controls whether to query the system-wide or the per-user password agents. By default if invoked privileged the system-wide agents are queried,',
            '--system': 'Controls whether to query the system-wide or the per-user password agents. By default if invoked privileged the system-wide agents are queried,'
        },
        'examples': [
            'systemd-ask-password  # Query the user for a system password'
        ],
        'category': 'Other'
    },
    'systemd-cat': {
        'desc': 'Connect a pipeline or program\'s output with the journal',
        'common_flags': {
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.',
            '-t': '=',
            '--identifier': '=',
            '-p': '=',
            '--priority': '= option, above, and both can be used at once. When both are used, --priority= will specify the default priority for standard output',
            '--stderr-priority': '=',
            '--level-prefix': '=',
            '--namespace': '='
        },
        'examples': [
            'systemd-cat  # Connect a pipeline or program\'s output with the jo',
            'systemd-cat -h  # Show help',
            'systemd-cat --version  # Show version'
        ],
        'category': 'Other'
    },
    'systemd-cgls': {
        'desc': 'Recursively show control group contents',
        'common_flags': {
            '--all': 'Do not hide empty control groups in the output.',
            '-l': 'Do not ellipsize process tree members.',
            '--full': 'Do not ellipsize process tree members.',
            '-u': 'Show cgroup subtrees for the specified units.',
            '--unit': 'Show cgroup subtrees for the specified units.',
            '--user-unit': 'Show cgroup subtrees for the specified user units.',
            '-k': 'Include kernel threads in output.',
            '-M': 'MACHINE, --machine=MACHINE',
            '-x': '=',
            '--xattr': '=',
            '-c': '=',
            '--cgroup-id': '=',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-cgls  # Recursively show control group contents',
            'systemd-cgls -h  # Show help',
            'systemd-cgls --version  # Show version',
            'systemd-cgls --all  # Show all'
        ],
        'category': 'Other'
    },
    'systemd-cgtop': {
        'desc': 'Show top control groups by their resource usage',
        'common_flags': {
            '-p': '=path',
            '--order': '=io',
            '-t': '=tasks',
            '-c': '=cpu',
            '-m': '=memory',
            '-i': '=io',
            '-b': 'Run in \"batch\" mode: do not accept input and run until the iteration limit set with --iterations= is exhausted or until killed. This mode could',
            '--batch': 'Run in \"batch\" mode: do not accept input and run until the iteration limit set with --iterations= is exhausted or until killed. This mode could',
            '-r': 'Format byte counts (as in memory usage and I/O metrics) and CPU time with raw numeric values rather than human-readable numbers.',
            '--raw': 'Format byte counts (as in memory usage and I/O metrics) and CPU time with raw numeric values rather than human-readable numbers.',
            '--cpu': '=percentage, --cpu=time',
            '-P': 'Count only userspace processes instead of all tasks. By default, all tasks are counted: each kernel thread and each userspace thread',
            '-k': 'Count only userspace processes and kernel threads instead of all tasks. By default, all tasks are counted: each kernel thread and each userspace',
            '--recursive': '=',
            '-n': '='
        },
        'examples': [
            'systemd-cgtop  # Show top control groups by their resource usage'
        ],
        'category': 'Other'
    },
    'systemd-creds': {
        'desc': 'Lists, shows, encrypts and decrypts service credentials',
        'common_flags': {
            '--system': 'When specified with the list and cat commands operates on the credentials passed to system as a whole instead of on those passed to the current',
            '--user': 'When specified with the encrypt and decrypt commands encrypts a user-scoped (rather than a system-scoped) credential. Use --uid= to select which',
            '--uid': '=',
            '--transcode': '=',
            '--newline': '=',
            '--pretty': 'When specified with encrypt controls whether to show the encrypted credential as SetCredentialEncrypted= setting that may be pasted directly',
            '-p': 'When specified with encrypt controls whether to show the encrypted credential as SetCredentialEncrypted= setting that may be pasted directly',
            '--name': '=name',
            '--timestamp': '=timestamp',
            '--not-after': '=timestamp',
            '--with-key': '=auto-initrd mode, to disable binding against the host secret.',
            '--tpm2-device': '=PATH',
            '--tpm2-pcrs': '=PCR[+PCR...]',
            '--tpm2-public-key': '=PATH, --tpm2-public-key-pcrs=PCR[+PCR...]',
            '--tpm2-signature': '=PATH'
        },
        'examples': [
            'systemd-creds  # Lists, shows, encrypts and decrypts service creden'
        ],
        'category': 'Other'
    },
    'systemd-delta': {
        'desc': 'Find overridden configuration files',
        'common_flags': {
            '-t': '=',
            '--type': '=',
            '--diff': '=',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.',
            '--no-pager': 'Do not pipe output into a pager.'
        },
        'examples': [
            'systemd-delta  # Find overridden configuration files',
            'systemd-delta -h  # Show help',
            'systemd-delta --version  # Show version'
        ],
        'category': 'Other'
    },
    'systemd-detect-virt': {
        'desc': 'Detect execution in a virtualized environment',
        'common_flags': {
            '-c': 'Only detects container virtualization (i.e. shared kernel virtualization).',
            '--container': 'Only detects container virtualization (i.e. shared kernel virtualization).',
            '-v': 'Only detects hardware virtualization.',
            '--vm': 'Only detects hardware virtualization.',
            '-r': 'Detect whether invoked in a chroot(2) environment. In this mode, no output is written, but the return value indicates whether the process was',
            '--chroot': 'Detect whether invoked in a chroot(2) environment. In this mode, no output is written, but the return value indicates whether the process was',
            '--private-users': 'Detect whether invoked in a user namespace. In this mode, no output is written, but the return value indicates whether the process was invoked',
            '--cvm': 'Detect whether invoked in a confidential virtual machine. The result of this detection may be used to disable features that should not be used',
            '-q': 'Suppress output of the virtualization technology identifier.',
            '--quiet': 'Suppress output of the virtualization technology identifier.',
            '--list': 'Output all currently known and detectable container and VM environments.',
            '--list-cvm': 'Output all currently known and detectable confidential virtualization technologies.',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-detect-virt  # Detect execution in a virtualized environment',
            'systemd-detect-virt -h  # Show help',
            'systemd-detect-virt -v  # Show version',
            'systemd-detect-virt -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'systemd-escape': {
        'desc': 'Escape strings for usage in systemd unit names',
        'common_flags': {
            '--suffix': '=',
            '--template': '=',
            '--mangle': 'Like --escape, but only escape characters that are obviously not escaped yet, and possibly automatically append an appropriate unit type suffix',
            '--path': 'When escaping or unescaping a string, assume it refers to a file system path. This simplifies the path (leading, trailing, and duplicate \"/\"',
            '-p': 'When escaping or unescaping a string, assume it refers to a file system path. This simplifies the path (leading, trailing, and duplicate \"/\"',
            '--unescape': 'Instead of escaping the specified strings, undo the escaping, reversing the operation. May not be used in conjunction with --suffix= or',
            '-u': 'Instead of escaping the specified strings, undo the escaping, reversing the operation. May not be used in conjunction with --suffix= or',
            '-m': 'Like --escape, but only escape characters that are obviously not escaped yet, and possibly automatically append an appropriate unit type suffix',
            '--instance': 'With --unescape, unescape and print only the instance part of an instantiated unit name template. Results in an error for an uninstantiated',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-escape  # Escape strings for usage in systemd unit names',
            'systemd-escape -h  # Show help',
            'systemd-escape --version  # Show version'
        ],
        'category': 'Other'
    },
    'systemd-firstboot': {
        'desc': 'Initialize basic system settings on or before the first boot-up of a system',
        'common_flags': {
            '--root': '=root',
            '--image': '=path',
            '--locale': '=LOCALE, --locale-messages=LOCALE',
            '--keymap': '=KEYMAP',
            '--timezone': '=TIMEZONE',
            '--hostname': '=HOSTNAME',
            '--setup-machine-id': 'Initialize the system\'s machine ID to a random ID. This controls the machine-id(5) file.',
            '--machine-id': '=ID',
            '--root-password': '= accepts the password to set directly on the command line, --root-password-file= reads it from a file and',
            '--root-password-hashed': '= accepts an already hashed password on the command line. See shadow(5) for more information on the format of the hashed',
            '--root-shell': '=SHELL',
            '--kernel-command-line': '=CMDLINE',
            '--prompt-locale': 'Prompt the user interactively for a specific basic setting. Note that any explicit configuration settings specified on the command line take',
            '--prompt-keymap': 'Prompt the user interactively for a specific basic setting. Note that any explicit configuration settings specified on the command line take',
            '--prompt-timezone': 'Prompt the user interactively for a specific basic setting. Note that any explicit configuration settings specified on the command line take'
        },
        'examples': [
            'systemd-firstboot  # Initialize basic system settings on or before the '
        ],
        'category': 'Other'
    },
    'systemd-firstboot.service': {
        'desc': 'Initialize basic system settings on or before the first boot-up of a system',
        'common_flags': {
            '--root': '=root',
            '--image': '=path',
            '--locale': '=LOCALE, --locale-messages=LOCALE',
            '--keymap': '=KEYMAP',
            '--timezone': '=TIMEZONE',
            '--hostname': '=HOSTNAME',
            '--setup-machine-id': 'Initialize the system\'s machine ID to a random ID. This controls the machine-id(5) file.',
            '--machine-id': '=ID',
            '--root-password': '= accepts the password to set directly on the command line, --root-password-file= reads it from a file and',
            '--root-password-hashed': '= accepts an already hashed password on the command line. See shadow(5) for more information on the format of the hashed',
            '--root-shell': '=SHELL',
            '--kernel-command-line': '=CMDLINE',
            '--prompt-locale': 'Prompt the user interactively for a specific basic setting. Note that any explicit configuration settings specified on the command line take',
            '--prompt-keymap': 'Prompt the user interactively for a specific basic setting. Note that any explicit configuration settings specified on the command line take',
            '--prompt-timezone': 'Prompt the user interactively for a specific basic setting. Note that any explicit configuration settings specified on the command line take'
        },
        'examples': [
            'systemd-firstboot.service  # Initialize basic system settings on or before the '
        ],
        'category': 'Other'
    },
    'systemd-id128': {
        'desc': 'Generate and print sd-128 identifiers',
        'common_flags': {
            '-p': 'Generate output as programming language snippets.',
            '--pretty': 'Generate output as programming language snippets.',
            '-P': 'Only print the value. May be combined with -u/--uuid.',
            '--value': 'Only print the value. May be combined with -u/--uuid.',
            '-a': 'app-id, --app-specific=app-id',
            '-u': 'Generate output as a UUID formatted in the \"canonical representation\", with five groups of digits separated by hyphens. See the Wikipedia entry',
            '--uuid': 'Generate output as a UUID formatted in the \"canonical representation\", with five groups of digits separated by hyphens. See the Wikipedia entry',
            '--no-pager': 'Do not pipe output into a pager.',
            '--no-legend': 'Do not print the legend, i.e. column headers and the footer with hints.',
            '--json': '=MODE',
            '-j': 'Equivalent to --json=pretty if running on a terminal, and --json=short otherwise.',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-id128  # Generate and print sd-128 identifiers',
            'systemd-id128 -h  # Show help',
            'systemd-id128 --version  # Show version',
            'systemd-id128 -a  # Show all'
        ],
        'category': 'Other'
    },
    'systemd-inhibit': {
        'desc': 'Execute a program with an inhibition lock taken',
        'common_flags': {
            '--what': '=',
            '--who': '=',
            '--why': '=',
            '--mode': '=',
            '--list': 'Lists all active inhibition locks instead of acquiring one.',
            '--no-ask-password': 'Do not query the user for authentication for privileged operations.',
            '--no-pager': 'Do not pipe output into a pager.',
            '--no-legend': 'Do not print the legend, i.e. column headers and the footer with hints.',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-inhibit  # Execute a program with an inhibition lock taken',
            'systemd-inhibit -h  # Show help',
            'systemd-inhibit --version  # Show version'
        ],
        'category': 'Other'
    },
    'systemd-machine-id-setup': {
        'desc': 'Initialize the machine ID in /etc/machine-id',
        'common_flags': {
            '--root': '=path',
            '--image': '=, see above. If not specified defaults to the \"*\" policy, i.e. all recognized file systems in the image are used.',
            '--image-policy': '=policy',
            '--commit': 'Commit a transient machine ID to disk. This command may be used to convert a transient machine ID into a persistent one. A transient machine ID',
            '--print': 'Print the machine ID generated or committed after the operation is complete.',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-machine-id-setup  # Initialize the machine ID in /etc/machine-id',
            'systemd-machine-id-setup -h  # Show help',
            'systemd-machine-id-setup --version  # Show version'
        ],
        'category': 'Other'
    },
    'systemd-measure': {
        'desc': 'Pre-calculate and sign expected TPM2 PCR 11 values for booted unified kernel images',
        'common_flags': {
            '--linux': '=PATH, --osrel=PATH, --cmdline=PATH, --initrd=PATH, --ucode=PATH, --splash=PATH, --dtb=PATH, --uname=PATH, --sbat=PATH, --pcrpkey=PATH,',
            '--profile': '=PATH, --dtbauto=PATH, --hwids=PATH',
            '--current': 'When used with the calculate or sign verb, takes the PCR 11 values currently in effect for the system (which should typically reflect the hashes',
            '--bank': '=DIGEST',
            '--private-key': '=PATH/URI, --private-key-source=TYPE[:NAME], --certificate=PATH/URI, --certificate-source=TYPE[:NAME]',
            '--certificate': '= can be used to specify an X.509 certificate as an alternative to --public-key= since v256.',
            '--tpm2-device': '=PATH',
            '--phase': '=PHASE',
            '--append': '=PATH',
            '--json': '=MODE',
            '--no-pager': 'Do not pipe output into a pager.',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-measure  # Pre-calculate and sign expected TPM2 PCR 11 values',
            'systemd-measure -h  # Show help',
            'systemd-measure --version  # Show version'
        ],
        'category': 'Other'
    },
    'systemd-mount': {
        'desc': 'Establish and destroy transient mount or auto-mount points',
        'common_flags': {
            '--no-block': 'Do not synchronously wait for the requested operation to finish. If this is not specified, the job will be verified, enqueued and systemd-mount',
            '-l': 'Do not ellipsize the output when --list is specified.',
            '--full': 'Do not ellipsize the output when --list is specified.',
            '--no-pager': 'Do not pipe output into a pager.',
            '--no-legend': 'Do not print the legend, i.e. column headers and the footer with hints.',
            '--no-ask-password': 'Do not query the user for authentication for privileged operations.',
            '--json': '=MODE',
            '--quiet': 'Suppresses additional informational output while running.',
            '-q': 'Suppresses additional informational output while running.',
            '--discover': 'Enable probing of the mount source. This switch is implied if a single argument is specified on the command line. If passed, additional metadata',
            '--type': '=, -t',
            '--options': '=, -o',
            '--owner': '=USER',
            '--fsck': '=',
            '--description': '='
        },
        'examples': [
            'systemd-mount  # Establish and destroy transient mount or auto-moun'
        ],
        'category': 'Other'
    },
    'systemd-notify': {
        'desc': 'Notify service manager about start-up completion and other daemon status changes',
        'common_flags': {
            '--ready': 'Inform the invoking service manager about service start-up or configuration reload completion. This is equivalent to systemd-notify READY=1. For',
            '--reloading': 'Inform the invoking service manager about the beginning of a configuration reload cycle. This is equivalent to systemd-notify RELOADING=1 (but',
            '--stopping': 'Inform the invoking service manager about the beginning of the shutdown phase of the service. This is equivalent to systemd-notify STOPPING=1.',
            '--pid': '=auto is equivalent to systemd-notify --pid=$PID. For details about the semantics of this option see sd_notify(3).',
            '--uid': '=USER',
            '--status': '=',
            '--booted': 'Returns 0 if the system was booted up with systemd, non-zero otherwise. If this option is passed, no message is sent. This option is hence',
            '--no-block': 'Do not synchronously wait for the requested operation to finish. Use of this option is only recommended when systemd-notify is spawned by the',
            '--exec': 'If specified systemd-notify will execute another command line after it completed its operation, replacing its own process. If used, the list of',
            '--fd': '=',
            '--fdname': '=',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-notify  # Notify service manager about start-up completion a',
            'systemd-notify -h  # Show help',
            'systemd-notify --version  # Show version'
        ],
        'category': 'Other'
    },
    'systemd-path': {
        'desc': 'List and query system and user paths',
        'common_flags': {
            '--suffix': '=',
            '--no-pager': 'Do not pipe output into a pager.',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-path  # List and query system and user paths',
            'systemd-path -h  # Show help',
            'systemd-path --version  # Show version'
        ],
        'category': 'Other'
    },
    'systemd-run': {
        'desc': 'Run programs in transient scope units, service units, or path-, socket-, or timer-triggered service units',
        'common_flags': {
            '--scope': 'Create a transient .scope unit instead of the default transient .service unit (see above).',
            '--unit': '=, -u',
            '--property': '=, -p',
            '--description': '=',
            '--slice': '=',
            '--slice-inherit': 'Make the new .service or .scope unit part of the slice the systemd-run itself has been invoked in. This option may be combined with --slice=, in',
            '--expand-environment': '=BOOL',
            '-r': 'After the service process has terminated, keep the service around until it is explicitly stopped. This is useful to collect runtime information',
            '--remain-after-exit': 'After the service process has terminated, keep the service around until it is explicitly stopped. This is useful to collect runtime information',
            '--send-sighup': 'When terminating the scope or service unit, send a SIGHUP immediately after SIGTERM. This is useful to indicate to shells and shell-like',
            '--service-type': '=',
            '--uid': '=, --gid=',
            '--nice': '=',
            '--working-directory': '=',
            '--same-dir': 'Similar to --working-directory=, but uses the current working directory of the caller for the service to execute.'
        },
        'examples': [
            'systemd-run  # Run programs in transient scope units, service uni'
        ],
        'category': 'Other'
    },
    'systemd-socket-activate': {
        'desc': 'Test socket activation of daemons',
        'common_flags': {
            '-l': 'address, --listen=address',
            '-a': 'Launch an instance of the service program for each connection and pass the connection socket.',
            '--accept': 'Launch an instance of the service program for each connection and pass the connection socket.',
            '-d': 'Listen on a datagram socket (SOCK_DGRAM), instead of a stream socket (SOCK_STREAM). May not be combined with --seqpacket.',
            '--datagram': 'Listen on a datagram socket (SOCK_DGRAM), instead of a stream socket (SOCK_STREAM). May not be combined with --seqpacket.',
            '--seqpacket': 'Listen on a sequential packet socket (SOCK_SEQPACKET), instead of a stream socket (SOCK_STREAM). May not be combined with --datagram.',
            '--inetd': 'Use the inetd protocol for passing file descriptors, i.e. as standard input and standard output, instead of the new-style protocol for passing',
            '-E': 'VAR[=VALUE], --setenv=VAR[=VALUE]',
            '--fdname': '=NAME[:NAME...]',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-socket-activate  # Test socket activation of daemons',
            'systemd-socket-activate -h  # Show help',
            'systemd-socket-activate --version  # Show version',
            'systemd-socket-activate -a  # Show all'
        ],
        'category': 'Other'
    },
    'systemd-stdio-bridge': {
        'desc': 'D-Bus proxy',
        'common_flags': {
            '--user': 'Talk to the service manager of the calling user, rather than the service manager of the system.',
            '--system': 'Talk to the service manager of the system. This is the implied default.',
            '-M': '=',
            '--machine': '=',
            '-p': 'PATH, --bus-path=PATH',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-stdio-bridge  # D-Bus proxy',
            'systemd-stdio-bridge -h  # Show help',
            'systemd-stdio-bridge --version  # Show version'
        ],
        'category': 'Other'
    },
    'systemd-tty-ask-password-agent': {
        'desc': 'List or process pending systemd password requests',
        'common_flags': {
            '--list': 'Lists all currently pending system password requests.',
            '--query': 'Process all currently pending system password requests by querying the user on the calling TTY.',
            '--watch': 'Continuously process password requests.',
            '--wall': 'Forward password requests to wall(1) instead of querying the user on the calling TTY.',
            '--plymouth': 'Ask question with plymouth(8) instead of querying the user on the calling TTY.',
            '--console': '[=DEVICE]',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-tty-ask-password-agent  # List or process pending systemd password requests',
            'systemd-tty-ask-password-agent -h  # Show help',
            'systemd-tty-ask-password-agent --version  # Show version'
        ],
        'category': 'Other'
    },
    'systemd-umount': {
        'desc': 'Establish and destroy transient mount or auto-mount points',
        'common_flags': {
            '--no-block': 'Do not synchronously wait for the requested operation to finish. If this is not specified, the job will be verified, enqueued and systemd-mount',
            '-l': 'Do not ellipsize the output when --list is specified.',
            '--full': 'Do not ellipsize the output when --list is specified.',
            '--no-pager': 'Do not pipe output into a pager.',
            '--no-legend': 'Do not print the legend, i.e. column headers and the footer with hints.',
            '--no-ask-password': 'Do not query the user for authentication for privileged operations.',
            '--json': '=MODE',
            '--quiet': 'Suppresses additional informational output while running.',
            '-q': 'Suppresses additional informational output while running.',
            '--discover': 'Enable probing of the mount source. This switch is implied if a single argument is specified on the command line. If passed, additional metadata',
            '--type': '=, -t',
            '--options': '=, -o',
            '--owner': '=USER',
            '--fsck': '=',
            '--description': '='
        },
        'examples': [
            'systemd-umount  # Establish and destroy transient mount or auto-moun'
        ],
        'category': 'Other'
    },
    'systemd-vpick': {
        'desc': 'Resolve paths to \".v/\" versioned directories',
        'common_flags': {
            '--basename': '=, -B',
            '-V': 'Explicitly configures the version to select. If specified, a filename with the specified version string will be looked for, instead of the',
            '-A': 'Explicitly configures the architecture to select. If specified, a filename with the specified architecture identifier will be looked for. If not',
            '--suffix': '=, -S',
            '--type': '=, -t',
            '--print': '=, -p',
            '--resolve': '=',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'systemd-vpick  # Resolve paths to \".v/\" versioned directories',
            'systemd-vpick -h  # Show help',
            'systemd-vpick --version  # Show version'
        ],
        'category': 'Other'
    },
    'tabs': {
        'desc': 'set terminal tab stops',
        'common_flags': {
            '-T': 'name',
            '-d': 'The debugging option shows a ruler line, followed by two data lines. The first data line shows the expected tab-stops marked with asterisks.',
            '-n': 'This option tells tabs to check the options and run any debugging option, but not to modify the terminal settings.',
            '-V': 'reports the version of ncurses which was used in this program, and exits.',
            '-a': '2 Assembler, IBM S/370, second format',
            '-c': '3 COBOL compact format extended',
            '-f': 'FORTRAN',
            '-p': 'PL/I',
            '-s': 'SNOBOL',
            '-u': 'UNIVAC 1100 Assembler'
        },
        'examples': [
            'tabs  # set terminal tab stops',
            'tabs -V  # Show version',
            'tabs -a  # Show all'
        ],
        'category': 'Other'
    },
    'tapestat': {
        'desc': 'Report tape statistics.',
        'common_flags': {
            '--human': 'Print sizes in human readable format (e.g. 1.0k, 1.2M, etc.) The units displayed with this option supersede any other default units (e.g.',
            '-k': 'Show the amount of data written or read in kilobytes per second instead of megabytes. This option is mutually exclusive with -m.',
            '-m': 'Show the amount of data written or read in megabytes per second instead of kilobytes. This option is mutually exclusive with -k.',
            '-t': 'Display time stamps. The time stamp format may depend on the value of the S_TIME_FORMAT environment variable (see below).',
            '-V': 'Print version and exit.',
            '-y': 'Omit the initial statistic showing values since boot.',
            '-z': 'Tell tapestat to omit output for any tapes for which there was no activity during the sample period.'
        },
        'examples': [
            'tapestat  # Report tape statistics.',
            'tapestat -V  # Show version'
        ],
        'category': 'Other'
    },
    'tar': {
        'desc': 'an archiving utility',
        'common_flags': {
            '-A': 'Append archives to the end of another archive. The arguments are treated as the names of archives to append. All archives must be of the',
            '--catenate': 'Append archives to the end of another archive. The arguments are treated as the names of archives to append. All archives must be of the',
            '--concatenate': 'Append archives to the end of another archive. The arguments are treated as the names of archives to append. All archives must be of the',
            '-c': 'Create a new archive. Arguments supply the names of the files to be archived. Directories are archived recursively, unless the --no-recur‐',
            '--create': 'Create a new archive. Arguments supply the names of the files to be archived. Directories are archived recursively, unless the --no-recur‐',
            '-d': 'Find differences between archive and file system. The arguments are optional and specify archive members to compare. If not given, the cur‐',
            '--diff': 'Find differences between archive and file system. The arguments are optional and specify archive members to compare. If not given, the cur‐',
            '--compare': 'Find differences between archive and file system. The arguments are optional and specify archive members to compare. If not given, the cur‐',
            '--delete': 'Delete from the archive. The arguments supply names of the archive members to be removed. At least one argument must be given.',
            '-r': 'Append files to the end of an archive. Arguments have the same meaning as for -c (--create).',
            '--append': 'Append files to the end of an archive. Arguments have the same meaning as for -c (--create).',
            '-t': 'List the contents of an archive. Arguments are optional. When given, they specify the names of the members to list.',
            '--list': 'List the contents of an archive. Arguments are optional. When given, they specify the names of the members to list.',
            '--test-label': 'Test the archive volume label and exit. When used without arguments, it prints the volume label (if any) and exits with status 0. When one',
            '-u': 'Append files which are newer than the corresponding copy in the archive. Arguments have the same meaning as with the -c and -r options. No‐'
        },
        'examples': [
            'tar  # an archiving utility',
            'tar -czf archive.tar.gz directory/  # Create compressed archive',
            'tar -xzf archive.tar.gz  # Extract compressed archive',
            'tar -tvf archive.tar.gz  # List contents'
        ],
        'category': 'Other'
    },
    'taskset': {
        'desc': 'set or retrieve a process\'s CPU affinity',
        'common_flags': {
            '-a': 'Set or retrieve the CPU affinity of all the tasks (threads) for a given PID.',
            '--all-tasks': 'Set or retrieve the CPU affinity of all the tasks (threads) for a given PID.',
            '-c': 'Interpret mask as numerical list of processors instead of a bitmask. Numbers are separated by commas and may include ranges. For example:',
            '--cpu-list': 'Interpret mask as numerical list of processors instead of a bitmask. Numbers are separated by commas and may include ranges. For example:',
            '-p': 'Operate on an existing PID and do not launch a new task.',
            '--pid': 'Operate on an existing PID and do not launch a new task.',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'taskset  # set or retrieve a process\'s CPU affinity',
            'taskset -h  # Show help',
            'taskset --version  # Show version',
            'taskset -a  # Show all'
        ],
        'category': 'Other'
    },
    'tempfile': {
        'desc': 'create a temporary file in a safe manner',
        'common_flags': {
            '-d': 'DIR',
            '--directory': 'DIR',
            '-m': 'MODE',
            '--mode': 'MODE',
            '-n': 'FILE',
            '--name': 'FILE',
            '-p': 'STRING',
            '--prefix': 'STRING',
            '-s': 'STRING',
            '--suffix': 'STRING',
            '--help': 'Print a usage message on standard output and exit successfully.',
            '--version': 'Print version information on standard output and exit successfully.'
        },
        'examples': [
            'tempfile  # create a temporary file in a safe manner',
            'tempfile --help  # Show help',
            'tempfile --version  # Show version'
        ],
        'category': 'Other'
    },
    'test': {
        'desc': 'check file types and compare values',
        'common_flags': {
            '--help': 'display this help and exit',
            '--version': 'output version information and exit',
            '-n': 'STRING',
            '-z': 'STRING',
            '-b': 'FILE',
            '-c': 'FILE',
            '-d': 'FILE',
            '-e': 'FILE',
            '-f': 'FILE',
            '-g': 'FILE',
            '-G': 'FILE',
            '-h': 'FILE',
            '-k': 'FILE',
            '-L': 'FILE',
            '-N': 'FILE'
        },
        'examples': [
            'test  # check file types and compare values',
            'test -h  # Show help',
            'test --version  # Show version'
        ],
        'category': 'Other'
    },
    'tic': {
        'desc': 'compile terminal descriptions for terminfo or termcap',
        'common_flags': {
            '-0': 'restricts the output to a single line',
            '-1': 'restricts the output to a single column',
            '-a': 'tells tic to retain commented-out capabilities rather than discarding them. Capabilities are commented by prefixing them with a period.',
            '-C': 'Force source translation to termcap format. Note: this differs from the -C option of infocmp(1) in that it does not merely translate capa‐',
            '-c': 'tells tic to only check file for errors, including syntax problems and bad use-links. If you specify -C (-I) with this option, the code will',
            '-D': 'tells tic to print the database locations that it knows about, and exit. The first location shown is the one to which it would write com‐',
            '-e': 'list',
            '-f': 'Display complex terminfo strings which contain if/then/else/endif expressions indented for readability.',
            '-G': 'Display constant literals in decimal form rather than their character equivalents.',
            '-g': 'Display constant character literals in quoted form rather than their decimal equivalents.',
            '-I': 'Force source translation to terminfo format.',
            '-K': 'Suppress some longstanding ncurses extensions to termcap format, e.g., \"\\s\" for space.',
            '-L': 'Force source translation to terminfo format using the long C variable names listed in <term.h>',
            '-N': 'Disable smart defaults. Normally, when translating from termcap to terminfo, the compiler makes a number of assumptions about the defaults',
            '-o': 'dir Write compiled entries to given database location. Overrides the TERMINFO environment variable.'
        },
        'examples': [
            'tic  # compile terminal descriptions for terminfo or term',
            'tic -a  # Show all'
        ],
        'category': 'Other'
    },
    'timedatectl': {
        'desc': 'Control the system time and date',
        'common_flags': {
            '--adjust-system-clock': 'If set-local-rtc is invoked and this option is passed, the system clock is synchronized from the RTC again, taking the new setting into account.',
            '--monitor': 'If timesync-status is invoked and this option is passed, then timedatectl monitors the status of systemd-timesyncd.service(8) and updates the',
            '-a': 'When showing properties of systemd-timesyncd.service(8), show all properties regardless of whether they are set or not.',
            '--all': 'When showing properties of systemd-timesyncd.service(8), show all properties regardless of whether they are set or not.',
            '-p': '=',
            '--property': '=',
            '--value': 'When printing properties with show-timesync, only print the value, and skip the property name and \"=\".',
            '-P': 'Equivalent to --value --property=, i.e. shows the value of the property without the property name or \"=\". Note that using -P once will also',
            '-H': '=',
            '--host': '=',
            '-M': '=',
            '--machine': '=',
            '--no-ask-password': 'Do not query the user for authentication for privileged operations.',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.'
        },
        'examples': [
            'timedatectl  # Control the system time and date',
            'timedatectl -h  # Show help',
            'timedatectl -a  # Show all'
        ],
        'category': 'Other'
    },
    'tload': {
        'desc': 'graphic representation of system load average',
        'common_flags': {
            '-s': 'number',
            '--scale': 'number',
            '-d': 'seconds',
            '--delay': 'seconds',
            '-h': 'Display this help text.',
            '--help': 'Display this help text.',
            '-V': 'Display version information and exit.',
            '--version': 'Display version information and exit.'
        },
        'examples': [
            'tload  # graphic representation of system load average',
            'tload -h  # Show help',
            'tload --version  # Show version'
        ],
        'category': 'Other'
    },
    'tmux': {
        'desc': 'terminal multiplexer',
        'common_flags': {
            '-t': '.',
            '-e': 'takes the form ‘VARIABLE=value’ and sets an environment variable for the newly created window; it may be specified multiple times.',
            '-I': 'and -O specify which of the shell-command output streams are connected to the pane: with -I stdout is connected (so anything',
            '-M': 'begins mouse resizing (only valid if bound to a mouse key binding, see “MOUSE SUPPORT”).',
            '-T': 'trims all lines below the current cursor position and moves lines out of the history to replace them.',
            '-m': 'and -M are used to set and clear the marked pane. There is one marked pane at a time, setting a new marked pane clears the last. The',
            '-l': 'option specifies the size of the new pane in lines (for vertical split) or in columns (for horizontal split); size may be followed by ‘%’',
            '-f': 'option creates a new pane spanning the full window height (with -h) or full window width (with -v), instead of splitting the active pane.',
            '-Z': 'zooms if the window is not zoomed, or keeps it zoomed if already zoomed.',
            '-D': 'swaps with the next pane (after it numerically). -d instructs tmux not to change the active pane and -Z keeps the window zoomed if it'
        },
        'examples': [
            'tmux  # terminal multiplexer'
        ],
        'category': 'Other'
    },
    'tnftp': {
        'desc': 'Internet file transfer program',
        'common_flags': {
            '-o': 'output is recommended, to avoid writing to unexpected file names.'
        },
        'examples': [
            'tnftp  # Internet file transfer program'
        ],
        'category': 'Other'
    },
    'toe': {
        'desc': 'list table of entries of terminfo terminal types',
        'common_flags': {
            '-a': 'lists entries from all terminal database directories that terminfo would search, instead of only the first that it finds.',
            '-h': 'writes a heading naming each directory as it is accessed.',
            '-s': 'sorts the output by the entry names.',
            '-u': 'file lists terminal type dependencies in file, a terminfo entry source or termcap database file. The report summarizes the “use” (terminfo) and',
            '-U': 'file lists terminal type reverse dependencies in file, a terminfo entry source or termcap database file. The report summarizes the “use” (ter‐',
            '-v': '[n] reports verbose status information to the standard error stream, showing toe\'s progress.',
            '-V': 'reports the version of ncurses associated with this program and exits with a successful status.'
        },
        'examples': [
            'toe  # list table of entries of terminfo terminal types',
            'toe -h  # Show help',
            'toe -v  # Show version',
            'toe -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'top': {
        'desc': 'display Linux processes',
        'common_flags': {
            '-----------------------': '+----------------------',
            '-b': 'Starts top in Batch mode, which could be useful for sending output from top to other programs or to a file. In this mode, top will not accept',
            '--batch': 'Starts top in Batch mode, which could be useful for sending output from top to other programs or to a file. In this mode, top will not accept',
            '-c': 'Starts top with the last remembered `c\' state reversed. Thus, if top was displaying command lines, now that field will show program names, and',
            '--cmdline-toggle': 'Starts top with the last remembered `c\' state reversed. Thus, if top was displaying command lines, now that field will show program names, and',
            '-d': '= SECS [.TENTHS]',
            '--delay': '= SECS [.TENTHS]',
            '-E': '= k | m | g | t | p | e',
            '--scale-summary-mem': '= k | m | g | t | p | e',
            '-e': '= k | m | g | t | p',
            '--scale-task-mem': '= k | m | g | t | p',
            '-H': 'Instructs top to display individual threads. Without this command-line option a summation of all threads in each process is shown. Later this',
            '--threads-show': 'Instructs top to display individual threads. Without this command-line option a summation of all threads in each process is shown. Later this',
            '-h': 'Display usage help text, then quit.',
            '--help': 'Display usage help text, then quit.'
        },
        'examples': [
            'top  # display Linux processes',
            'top -h  # Show help'
        ],
        'category': 'Other'
    },
    'tput': {
        'desc': 'initialize a terminal, exercise its capabilities, or query terminfo database',
        'common_flags': {
            '-S': 'retrieves more than one capability per invocation of tput. The capabilities must be passed to tput from the standard input stream instead',
            '-T': 'type indicates the terminal\'s type. Normally this option is unnecessary, because a default is taken from the TERM environment variable. If',
            '-v': 'causes tput to operate verbosely, reporting warnings.',
            '-V': 'reports the version of ncurses associated with tput, and exits with a successful status.',
            '-x': 'prevents “tput clear” from attempting to clear the scrollback buffer.'
        },
        'examples': [
            'tput  # initialize a terminal, exercise its capabilities, ',
            'tput -v  # Show version',
            'tput -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'troff': {
        'desc': 'GNU roff typesetter and document formatter',
        'common_flags': {
            '-h': 'and --help display a usage message, while -v and --version show version information; all exit afterward.',
            '-a': 'Generate a plain text approximation of the typeset output. The read-only register .A is set to 1. This option produces a sort of abstract',
            '-b': 'Write a backtrace reporting the state of troff\'s input parser to the standard error stream with each diagnostic message. The line numbers',
            '-c': 'Start with color output disabled.',
            '-C': 'Enable AT&T troff compatibility mode; implies -c. See groff_diff(7).',
            '-d': 'string=text',
            '-E': 'Inhibit troff error messages; implies -Ww. This option does not suppress messages sent to the standard error stream by documents or macro',
            '-f': 'fam Use fam as the default font family.',
            '-F': 'dir Search in directory dir for the selected output device\'s directory of device and font description files. See the description of',
            '-i': 'Read the standard input stream after all named input files have been processed.',
            '-I': 'dir Search the directory dir for files (those named on the command line; in psbb, so, and soquiet requests; and in “\\X\'ps: import\'”, “\\X\'ps:',
            '-m': 'name',
            '-M': 'dir Search directory dir for macro files. See the description of GROFF_TMAC_PATH in section “Environment” below for the default search locations',
            '-n': 'num Begin numbering pages at num. The default is 1.',
            '-o': 'list'
        },
        'examples': [
            'troff  # GNU roff typesetter and document formatter',
            'troff -h  # Show help',
            'troff -a  # Show all'
        ],
        'category': 'Other'
    },
    'true': {
        'desc': 'do nothing, successfully',
        'common_flags': {
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'true  # do nothing, successfully',
            'true --help  # Show help',
            'true --version  # Show version'
        ],
        'category': 'Other'
    },
    'tset': {
        'desc': 'initialize or reset terminal state',
        'common_flags': {
            '-c': 'Set control characters and modes.',
            '-e': 'ch',
            '-I': 'Do not send the terminal or tab initialization strings to the terminal.',
            '-i': 'ch',
            '-k': 'ch',
            '-m': 'mapping',
            '-Q': 'Do not display any values for the erase, interrupt and line kill characters. Normally tset displays the values for control characters which',
            '-q': 'The terminal type is displayed to the standard output, and the terminal is not initialized in any way. The option “-” by itself is equivalent',
            '-r': 'Print the terminal type to the standard error output.',
            '-s': 'Print the sequence of shell commands to initialize the environment variable TERM to the standard output; see subsection “Setting the Environ‐',
            '-V': 'reports the version of ncurses which was used in this program, and exits.',
            '-w': 'Resize the window to match the size deduced via setupterm(3NCURSES). Normally this has no effect, unless setupterm is not able to detect the'
        },
        'examples': [
            'tset  # initialize or reset terminal state',
            'tset -V  # Show version'
        ],
        'category': 'Other'
    },
    'ucf': {
        'desc': 'Update Configuration File: preserve user changes in configuration files',
        'common_flags': {
            '-h': 'Print a short usage message',
            '--help': 'Print a short usage message',
            '-n': 'Dry run. Print the actions that would be taken if the script is invoked, but take no action.',
            '--no-action': 'Dry run. Print the actions that would be taken if the script is invoked, but take no action.',
            '-d': '[n], --debug=[n]',
            '-p': 'Removes all vestiges of the file from the state hashfile. This is required to allow a package to be reinstalled after it is purged; since',
            '--purge': 'Removes all vestiges of the file from the state hashfile. This is required to allow a package to be reinstalled after it is purged; since',
            '-v': 'Make the script be very verbose about setting internal variables.',
            '--verbose': 'Make the script be very verbose about setting internal variables.',
            '-P': 'foo, --package foo',
            '-s': 'foo, --src-dir foo',
            '--sum-file': 'foo',
            '--three-way': 'This turns on the option, during installation, for the user to be offered a chance to see a merge of the changes between old maintainer ver‐',
            '--debconf-ok': 'Indicate that it is ok for ucf to use an already running debconf instance for prompting (it has always been ok to use ucf when debconf is not',
            '--debconf-template': 'foo'
        },
        'examples': [
            'ucf  # Update Configuration File: preserve user changes i',
            'ucf -h  # Show help',
            'ucf -v  # Show version',
            'ucf -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'ucfq': {
        'desc': 'query ucf database',
        'common_flags': {
            '--help': '-h Print out a usage message.',
            '--version': '-V Print version.',
            '--debug': '-d Turn on debugging mode.',
            '--verbose': '-v Make the script more verbose.',
            '--with-colons': '-w',
            '--state-dir': 'dir'
        },
        'examples': [
            'ucfq  # query ucf database',
            'ucfq --help  # Show help',
            'ucfq --version  # Show version',
            'ucfq --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'ucfr': {
        'desc': 'Update Configuration File Registry: associate packages with configuration files',
        'common_flags': {
            '-h': 'Print a short usage message',
            '--help': 'Print a short usage message',
            '-n': 'Dry run. Print the actions that would be taken if the script is invoked, but take no action.',
            '--no-action': 'Dry run. Print the actions that would be taken if the script is invoked, but take no action.',
            '-d': '[n], --debug [n]',
            '-p': 'Removes all vestiges of the association between the named package and the configuration file from the registry. The association must already',
            '--purge': 'Removes all vestiges of the association between the named package and the configuration file from the registry. The association must already',
            '-v': 'Make the script be very verbose about setting internal variables.',
            '--verbose': 'Make the script be very verbose about setting internal variables.',
            '-f': 'This option forces operations requested even if the configuration file in consideration is owned by another package. This allows a package',
            '--force': 'This option forces operations requested even if the configuration file in consideration is owned by another package. This allows a package',
            '--state-dir': '/path/to/dir'
        },
        'examples': [
            'ucfr  # Update Configuration File Registry: associate pack',
            'ucfr -h  # Show help',
            'ucfr -v  # Show version',
            'ucfr -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'uclampset': {
        'desc': 'manipulate the utilization clamping attributes of the system or a process',
        'common_flags': {
            '-m': 'Set util_min value.',
            '-M': 'Set util_max value.',
            '-a': 'Set or retrieve the utilization clamping attributes of all the tasks (threads) for a given PID.',
            '--all-tasks': 'Set or retrieve the utilization clamping attributes of all the tasks (threads) for a given PID.',
            '-p': 'Operate on an existing PID and do not launch a new task.',
            '--pid': 'Operate on an existing PID and do not launch a new task.',
            '-s': 'Set or retrieve the system-wide utilization clamping attributes.',
            '--system': 'Set or retrieve the system-wide utilization clamping attributes.',
            '-R': 'Set SCHED_FLAG_RESET_ON_FORK flag.',
            '--reset-on-fork': 'Set SCHED_FLAG_RESET_ON_FORK flag.',
            '-v': 'Show status information.',
            '--verbose': 'Show status information.',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.'
        },
        'examples': [
            'uclampset  # manipulate the utilization clamping attributes of ',
            'uclampset -h  # Show help',
            'uclampset -v  # Show version',
            'uclampset -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'ul': {
        'desc': 'do underlining',
        'common_flags': {
            '-i': 'Underlining is indicated by a separate line containing appropriate dashes `-\'; this is useful when you want to look at the underlining which is',
            '--indicated': 'Underlining is indicated by a separate line containing appropriate dashes `-\'; this is useful when you want to look at the underlining which is',
            '-t': 'terminal',
            '-T': 'terminal',
            '--terminal': 'terminal',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'ul  # do underlining',
            'ul -h  # Show help',
            'ul --version  # Show version'
        ],
        'category': 'Other'
    },
    'uncompress': {
        'desc': 'compress or expand files',
        'common_flags': {
            '-a': '--ascii',
            '-c': '--stdout --to-stdout',
            '-d': '--decompress --uncompress',
            '-f': '--force',
            '-h': '--help',
            '-k': '--keep',
            '-l': '--list',
            '-L': '--license',
            '-n': '--no-name',
            '-N': '--name',
            '-q': '--quiet',
            '-r': '--recursive',
            '-S': '.suf --suffix .suf',
            '--synchronous': 'Use synchronous output. With this option, gzip is less likely to lose data during a system crash, but it can be considerably slower.',
            '-t': '--test'
        },
        'examples': [
            'uncompress  # compress or expand files',
            'uncompress -h  # Show help',
            'uncompress -r -f  # Recursive and forced',
            'uncompress -a  # Show all'
        ],
        'category': 'Other'
    },
    'unlink': {
        'desc': 'call the unlink function to remove the specified file',
        'common_flags': {
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'unlink  # call the unlink function to remove the specified f',
            'unlink --help  # Show help',
            'unlink --version  # Show version'
        ],
        'category': 'Other'
    },
    'unlzma': {
        'desc': 'Compress or decompress .xz and .lzma files',
        'common_flags': {
            '-z': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '--compress': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '-d': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--decompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--uncompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '-t': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '--test': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '-l': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '--list': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '-k': 'Don\'t delete the input files.',
            '--keep': 'Don\'t delete the input files.',
            '-f': 'This option has several effects:',
            '--force': 'This option has several effects:',
            '-c': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.',
            '--stdout': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.'
        },
        'examples': [
            'unlzma  # Compress or decompress .xz and .lzma files'
        ],
        'category': 'Other'
    },
    'unshare': {
        'desc': 'run program in new namespaces',
        'common_flags': {
            '-i': '[=file]',
            '--ipc': '[=file]',
            '-m': '[=file]',
            '--mount': '[=file]',
            '-n': '[=file]',
            '--net': '[=file]',
            '-p': '[=file]',
            '--pid': '[=file]',
            '-u': '[=file]',
            '--uts': '[=file]',
            '-U': '[=file]',
            '--user': '[=file]',
            '-C': '[=file]',
            '--cgroup': '[=file]',
            '-T': '[=file]'
        },
        'examples': [
            'unshare  # run program in new namespaces'
        ],
        'category': 'Other'
    },
    'unxz': {
        'desc': 'Compress or decompress .xz and .lzma files',
        'common_flags': {
            '-z': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '--compress': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '-d': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--decompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--uncompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '-t': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '--test': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '-l': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '--list': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '-k': 'Don\'t delete the input files.',
            '--keep': 'Don\'t delete the input files.',
            '-f': 'This option has several effects:',
            '--force': 'This option has several effects:',
            '-c': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.',
            '--stdout': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.'
        },
        'examples': [
            'unxz  # Compress or decompress .xz and .lzma files'
        ],
        'category': 'Other'
    },
    'unzip': {
        'desc': 'list, test and extract compressed files in a ZIP archive',
        'common_flags': {
            '-Z': 'zipinfo(1) mode. If the first option on the command line is -Z, the remaining options are taken to be zipinfo(1) options. See the appropri‐',
            '-A': '[OS/2, Unix DLL] print extended help for the DLL\'s programming interface (API).',
            '-c': 'extract files to stdout/screen (``CRT\'\'). This option is similar to the -p option except that the name of each file is printed as it is ex‐',
            '-f': 'freshen existing files, i.e., extract only those files that already exist on disk and that are newer than the disk copies. By default unzip',
            '-l': 'list archive files (short format). The names, uncompressed file sizes and modification dates and times of the specified files are printed,',
            '-p': 'extract files to pipe (stdout). Nothing but the file data is sent to stdout, and the files are always extracted in binary format, just as',
            '-t': 'test archive files. This option extracts each specified file in memory and compares the CRC (cyclic redundancy check, an enhanced checksum)',
            '-T': '[most OSes] set the timestamp on the archive(s) to that of the newest file in each one. This corresponds to zip\'s -go option except that it',
            '-u': 'update existing files and create new ones if needed. This option performs the same function as the -f option, extracting (with query) files',
            '-v': 'list archive files (verbose format) or show diagnostic version info. This option has evolved and now behaves as both an option and a modi‐',
            '-z': 'display only the archive comment.'
        },
        'examples': [
            'unzip  # list, test and extract compressed files in a ZIP a',
            'unzip archive.zip  # Extract zip',
            'unzip -l archive.zip  # List contents'
        ],
        'category': 'Other'
    },
    'update-alternatives': {
        'desc': 'maintain symbolic links determining default commands',
        'common_flags': {
            '--altdir': 'directory',
            '--admindir': 'directory',
            '--instdir': 'directory',
            '--root': 'directory',
            '--log': 'file',
            '--force': 'Allow replacing or dropping any real file that is installed where an alternative link has to be installed or removed.',
            '--skip-auto': 'Skip configuration prompt for alternatives which are properly configured in automatic mode. This option is only relevant with --config or',
            '--all': '.',
            '--quiet': 'Do not generate any comments unless errors occur.',
            '--verbose': 'Generate more comments about what is being done.',
            '--debug': 'Generate even more comments, helpful for debugging, about what is being done (since version 1.19.3).'
        },
        'examples': [
            'update-alternatives  # maintain symbolic links determining default comman',
            'update-alternatives --verbose  # Verbose output',
            'update-alternatives --all  # Show all'
        ],
        'category': 'Other'
    },
    'update-mime-database': {
        'desc': 'a program to build the Shared MIME-Info database cache',
        'common_flags': {
            '-h': 'Print out a command summary.',
            '-v': 'Print out the version information.',
            '-V': 'Be verbose.',
            '-n': 'Only update if MIME-DIR/packages/ or a file in that directory is newer than MIME-DIR/version. This is useful for package pre- and post-in‐'
        },
        'examples': [
            'update-mime-database  # a program to build the Shared MIME-Info database c',
            'update-mime-database -h  # Show help',
            'update-mime-database -v  # Show version',
            'update-mime-database -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'uptime': {
        'desc': 'Tell how long the system has been running.',
        'common_flags': {
            '-p': 'show uptime in pretty format',
            '--pretty': 'show uptime in pretty format',
            '-h': 'display this help text',
            '--help': 'display this help text',
            '-s': 'system up since, in yyyy-mm-dd HH:MM:SS format',
            '--since': 'system up since, in yyyy-mm-dd HH:MM:SS format',
            '-V': 'display version information and exit',
            '--version': 'display version information and exit'
        },
        'examples': [
            'uptime  # Tell how long the system has been running.',
            'uptime -h  # Show help',
            'uptime --version  # Show version'
        ],
        'category': 'Other'
    },
    'vacuumdb': {
        'desc': 'garbage-collect and analyze a PostgreSQL database',
        'common_flags': {
            '-a': '--all',
            '--buffer-usage-limit': 'size',
            '--disable-page-skipping': 'Disable skipping pages based on the contents of the visibility map.',
            '-e': '--echo',
            '-f': '--full',
            '-F': '--freeze',
            '--force-index-cleanup': 'Always remove index entries pointing to dead tuples.',
            '-j': 'njobs',
            '--jobs': '=njobs',
            '--min-mxid-age': 'mxid_age',
            '--min-xid-age': 'xid_age',
            '-n': 'schema',
            '--schema': '=schema',
            '-N': 'schema',
            '--exclude-schema': '=schema'
        },
        'examples': [
            'vacuumdb  # garbage-collect and analyze a PostgreSQL database',
            'vacuumdb -a  # Show all'
        ],
        'category': 'Other'
    },
    'vacuumlo': {
        'desc': 'remove orphaned large objects from a PostgreSQL database',
        'common_flags': {
            '-l': 'limit',
            '--limit': '=limit',
            '-n': '--dry-run',
            '-v': '--verbose',
            '-V': '--version',
            '--help': 'Show help about vacuumlo command line arguments, and exit.',
            '-h': 'host',
            '--host': '=host',
            '-p': 'port',
            '--port': '=port',
            '-U': 'username',
            '--username': '=username',
            '-w': '--no-password',
            '-W': '--password'
        },
        'examples': [
            'vacuumlo  # remove orphaned large objects from a PostgreSQL da',
            'vacuumlo -h  # Show help',
            'vacuumlo -v  # Show version',
            'vacuumlo -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'varlinkctl': {
        'desc': 'Introspect with and invoke Varlink services',
        'common_flags': {
            '--more': 'When used with call: expect multiple method replies. If this flag is set the method call is sent with the more flag set, which tells the service',
            '-E': 'A shortcut for --more --timeout=infinity. This switch is useful for method calls that implement subscription to a continuous stream of updates.',
            '--collect': 'This is similar to --more but collects all responses in a JSON array, and prints it, rather than in JSON_SEQ mode.',
            '--oneway': 'When used with call: do not expect a method reply. If this flag is set the method call is sent with the oneway flag set (the command exits',
            '--json': '=MODE',
            '-j': 'Equivalent to --json=pretty when invoked interactively from a terminal. Otherwise equivalent to --json=short, in particular when the output is',
            '--quiet': 'Suppress output of method call replies.',
            '-q': 'Suppress output of method call replies.',
            '--graceful': '=',
            '--timeout': '=',
            '--no-pager': 'Do not pipe output into a pager.',
            '-h': 'Print a short help text and exit.',
            '--help': 'Print a short help text and exit.',
            '--version': 'Print a short version string and exit.'
        },
        'examples': [
            'varlinkctl  # Introspect with and invoke Varlink services',
            'varlinkctl -h  # Show help',
            'varlinkctl --version  # Show version'
        ],
        'category': 'Other'
    },
    'vi': {
        'desc': 'Vi IMproved, a programmer\'s text editor',
        'common_flags': {
            '-c': '{command}',
            '-A': 'If Vim has been compiled with ARABIC support for editing right-to-left oriented files and Arabic keyboard mapping, this option starts',
            '-b': 'Binary mode. A few options will be set that makes it possible to edit a binary or executable file.',
            '-C': 'Compatible. Set the \'compatible\' option. This will make Vim behave mostly like Vi, even though a .vimrc file exists.',
            '-d': '{device}, -dev {device}',
            '-D': 'Debugging. Go to debugging mode when executing the first command from a script.',
            '-e': 'Start Vim in Ex mode, just like the executable was called \"ex\".',
            '-E': 'Start Vim in improved Ex mode, just like the executable was called \"exim\".',
            '-f': 'Foreground. For the GUI version, Vim will not fork and detach from the shell it was started in. On the Amiga, Vim is not restarted to',
            '-F': 'If Vim has been compiled with FKMAP support for editing right-to-left oriented files and Farsi keyboard mapping, this option starts Vim',
            '-g': 'If Vim has been compiled with GUI support, this option enables the GUI. If no GUI support was compiled in, an error message is given',
            '-H': 'If Vim has been compiled with RIGHTLEFT support for editing right-to-left oriented files and Hebrew keyboard mapping, this option starts',
            '-i': '{viminfo}',
            '-l': 'Lisp mode. Sets the \'lisp\' and \'showmatch\' options on.',
            '-L': 'Same as -r.'
        },
        'examples': [
            'vi  # Vi IMproved, a programmer\'s text editor'
        ],
        'category': 'Other'
    },
    'view': {
        'desc': 'Vi IMproved, a programmer\'s text editor',
        'common_flags': {
            '-c': '{command}',
            '-A': 'If Vim has been compiled with ARABIC support for editing right-to-left oriented files and Arabic keyboard mapping, this option starts',
            '-b': 'Binary mode. A few options will be set that makes it possible to edit a binary or executable file.',
            '-C': 'Compatible. Set the \'compatible\' option. This will make Vim behave mostly like Vi, even though a .vimrc file exists.',
            '-d': '{device}, -dev {device}',
            '-D': 'Debugging. Go to debugging mode when executing the first command from a script.',
            '-e': 'Start Vim in Ex mode, just like the executable was called \"ex\".',
            '-E': 'Start Vim in improved Ex mode, just like the executable was called \"exim\".',
            '-f': 'Foreground. For the GUI version, Vim will not fork and detach from the shell it was started in. On the Amiga, Vim is not restarted to',
            '-F': 'If Vim has been compiled with FKMAP support for editing right-to-left oriented files and Farsi keyboard mapping, this option starts Vim',
            '-g': 'If Vim has been compiled with GUI support, this option enables the GUI. If no GUI support was compiled in, an error message is given',
            '-H': 'If Vim has been compiled with RIGHTLEFT support for editing right-to-left oriented files and Hebrew keyboard mapping, this option starts',
            '-i': '{viminfo}',
            '-l': 'Lisp mode. Sets the \'lisp\' and \'showmatch\' options on.',
            '-L': 'Same as -r.'
        },
        'examples': [
            'view  # Vi IMproved, a programmer\'s text editor'
        ],
        'category': 'Other'
    },
    'vim': {
        'desc': 'Vi IMproved, a programmer\'s text editor',
        'common_flags': {
            '-c': '{command}',
            '-A': 'If Vim has been compiled with ARABIC support for editing right-to-left oriented files and Arabic keyboard mapping, this option starts',
            '-b': 'Binary mode. A few options will be set that makes it possible to edit a binary or executable file.',
            '-C': 'Compatible. Set the \'compatible\' option. This will make Vim behave mostly like Vi, even though a .vimrc file exists.',
            '-d': '{device}, -dev {device}',
            '-D': 'Debugging. Go to debugging mode when executing the first command from a script.',
            '-e': 'Start Vim in Ex mode, just like the executable was called \"ex\".',
            '-E': 'Start Vim in improved Ex mode, just like the executable was called \"exim\".',
            '-f': 'Foreground. For the GUI version, Vim will not fork and detach from the shell it was started in. On the Amiga, Vim is not restarted to',
            '-F': 'If Vim has been compiled with FKMAP support for editing right-to-left oriented files and Farsi keyboard mapping, this option starts Vim',
            '-g': 'If Vim has been compiled with GUI support, this option enables the GUI. If no GUI support was compiled in, an error message is given',
            '-H': 'If Vim has been compiled with RIGHTLEFT support for editing right-to-left oriented files and Hebrew keyboard mapping, this option starts',
            '-i': '{viminfo}',
            '-l': 'Lisp mode. Sets the \'lisp\' and \'showmatch\' options on.',
            '-L': 'Same as -r.'
        },
        'examples': [
            'vim  # Vi IMproved, a programmer\'s text editor'
        ],
        'category': 'Other'
    },
    'vimtutor': {
        'desc': 'the Vim tutor',
        'common_flags': {
            '-l': 'ISO639',
            '--language': 'ISO639',
            '-c': 'NUMBER',
            '--chapter': 'NUMBER',
            '-g': 'Start vimtutor in the GUI version of vim if available, otherwise fallback to console vim.',
            '--gui': 'Start vimtutor in the GUI version of vim if available, otherwise fallback to console vim.',
            '-h': 'Display usage information.',
            '--help': 'Display usage information.',
            '--list': 'Display chapters and languages.'
        },
        'examples': [
            'vimtutor  # the Vim tutor',
            'vimtutor -h  # Show help'
        ],
        'category': 'Other'
    },
    'w': {
        'desc': 'Show who is logged on and what they are doing.',
        'common_flags': {
            '-h': 'Don\'t print the header.',
            '--no-header': 'Don\'t print the header.',
            '-u': 'Ignores the username while figuring out the current process and cpu times. To demonstrate this, do a su and do a w and a w -u.',
            '--no-current': 'Ignores the username while figuring out the current process and cpu times. To demonstrate this, do a su and do a w and a w -u.',
            '-s': 'Use the short format. Don\'t print the login time, JCPU or PCPU times.',
            '--short': 'Use the short format. Don\'t print the login time, JCPU or PCPU times.',
            '-t': 'Usually w will use either the systemd sessions table or the utmp file to locate users. In terminal mode w will scan the terminal devices and',
            '--terminal': 'Usually w will use either the systemd sessions table or the utmp file to locate users. In terminal mode w will scan the terminal devices and',
            '-f': 'Toggle printing the from (remote hostname) field. The default as released is for the from field to not be printed, although your system ad‐',
            '--from': 'Toggle printing the from (remote hostname) field. The default as released is for the from field to not be printed, although your system ad‐',
            '--help': 'Display help text and exit.',
            '-i': 'Display IP address instead of hostname for from field.',
            '--ip-addr': 'Display IP address instead of hostname for from field.',
            '-p': 'Display pid of the login process/the \"what\" process in the \"what\" field. The login process is also called the session leader.',
            '--pids': 'Display pid of the login process/the \"what\" process in the \"what\" field. The login process is also called the session leader.'
        },
        'examples': [
            'w  # Show who is logged on and what they are doing.',
            'w -h  # Show help'
        ],
        'category': 'Other'
    },
    'wall': {
        'desc': 'write a message to all users',
        'common_flags': {
            '-n': 'Suppress the banner.',
            '--nobanner': 'Suppress the banner.',
            '-t': 'timeout',
            '--timeout': 'timeout',
            '-g': 'group',
            '--group': 'group',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'wall  # write a message to all users',
            'wall -h  # Show help',
            'wall --version  # Show version'
        ],
        'category': 'Other'
    },
    'watch': {
        'desc': 'execute a program periodically, showing output fullscreen',
        'common_flags': {
            '-b': 'Beep if command has a non-zero exit.',
            '--beep': 'Beep if command has a non-zero exit.',
            '-c': 'Interpret ANSI color and style sequences.',
            '--color': 'Interpret ANSI color and style sequences.',
            '-C': 'Do not interpret ANSI color and style sequences.',
            '--no-color': 'Do not interpret ANSI color and style sequences.',
            '-d': '[=permanent]',
            '--differences': '[=permanent]',
            '-e': 'Freeze updates on command error, and exit after a key press.',
            '--errexit': 'Freeze updates on command error, and exit after a key press.',
            '-g': 'Exit when the visible output of command changes. Changes that are off the screen due to small screen size or large output will not cause',
            '--chgexit': 'Exit when the visible output of command changes. Changes that are off the screen due to small screen size or large output will not cause',
            '-n': 'seconds',
            '--interval': 'seconds',
            '-p': 'Make watch attempt to run command every --interval seconds. Try it with ntptime (if present) and notice how the fractional seconds stays'
        },
        'examples': [
            'watch  # execute a program periodically, showing output ful'
        ],
        'category': 'Other'
    },
    'wcurl': {
        'desc': 'a simple wrapper around curl to easily download files.',
        'common_flags': {
            '--curl-options': '=<CURL_OPTIONS>...',
            '-o': '=<PATH>',
            '-O': '=<PATH>',
            '--output': '=<PATH>',
            '--no-decode-filename': 'Don\'t percent-decode the output filename, even if the percent-encoding in the URL was done by wcurl, e.g.: The URL contained whitespaces.',
            '--dry-run': 'Do not actually execute curl, just print what would be invoked.',
            '-V': 'Print version information.',
            '--version': 'Print version information.',
            '-h': 'Print help message.',
            '--help': 'Print help message.'
        },
        'examples': [
            'wcurl  # a simple wrapper around curl to easily download fi',
            'wcurl -h  # Show help',
            'wcurl --version  # Show version'
        ],
        'category': 'Other'
    },
    'westcos-tool': {
        'desc': 'utility for manipulating data structures on westcos smart cards',
        'common_flags': {
            '--change-pin': 'Changes a PIN stored on the card. User authentication is required for this operation.',
            '-n': 'Changes a PIN stored on the card. User authentication is required for this operation.',
            '--certificate': 'file, -t file',
            '--finalize': 'Finalize the card. Once finalized the default key is invalidated, so PIN and PUK cannot be changed anymore without user authentication.',
            '-f': 'Finalize the card. Once finalized the default key is invalidated, so PIN and PUK cannot be changed anymore without user authentication.',
            '--generate-key': 'Generate a private key on the card. The card must not have been finalized and a PIN must be installed (i.e. the file for the PIN must have been',
            '-g': 'Generate a private key on the card. The card must not have been finalized and a PIN must be installed (i.e. the file for the PIN must have been',
            '--help': 'Print help message on screen.',
            '-h': 'Print help message on screen.',
            '--install-pin': 'Install PIN file in on the card. You must provide a PIN value with -x.',
            '-i': 'Install PIN file in on the card. You must provide a PIN value with -x.',
            '--key-length': 'length, -l length',
            '--overwrite-key': 'Overwrite the key if there is already a key on the card.',
            '-o': 'Overwrite the key if there is already a key on the card.',
            '--pin-value': 'pin, -x pin --puk-value puk, -y puk'
        },
        'examples': [
            'westcos-tool  # utility for manipulating data structures on westco',
            'westcos-tool -h  # Show help'
        ],
        'category': 'Other'
    },
    'whatis': {
        'desc': 'display one-line manual page descriptions',
        'common_flags': {
            '-d': 'Print debugging information.',
            '--debug': 'Print debugging information.',
            '-v': 'Print verbose warning messages.',
            '--verbose': 'Print verbose warning messages.',
            '-r': 'Interpret each name as a regular expression. If a name matches any part of a page name, a match will be made. This option causes whatis to',
            '--regex': 'Interpret each name as a regular expression. If a name matches any part of a page name, a match will be made. This option causes whatis to',
            '-w': 'Interpret each name as a pattern containing shell style wildcards. For a match to be made, an expanded name must match the entire page name.',
            '--wildcard': 'Interpret each name as a pattern containing shell style wildcards. For a match to be made, an expanded name must match the entire page name.',
            '-l': 'Do not trim output to the terminal width. Normally, output will be truncated to the terminal width to avoid ugly results from poorly-written',
            '--long': 'Do not trim output to the terminal width. Normally, output will be truncated to the terminal width to avoid ugly results from poorly-written',
            '-s': 'list, --sections=list, --section=list',
            '-m': 'system[,...], --systems=system[,...]',
            '-M': 'path, --manpath=path',
            '-L': 'locale, --locale=locale',
            '-C': 'file, --config-file=file'
        },
        'examples': [
            'whatis  # display one-line manual page descriptions',
            'whatis -v  # Show version',
            'whatis -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'whereis': {
        'desc': 'locate the binary, source, and manual page files for a command',
        'common_flags': {
            '-b': 'Search for binaries.',
            '-m': 'Search for manuals.',
            '-s': 'Search for sources.',
            '-u': 'Only show the command names that have unusual entries. A command is said to be unusual if it does not have just one entry of each explicitly',
            '-B': 'list',
            '-M': 'list',
            '-S': 'list',
            '-f': 'Terminates the directory list and signals the start of filenames. It must be used when any of the -B, -M, or -S options is used.',
            '-l': 'Output the list of effective lookup paths that whereis is using. When none of -B, -M, or -S is specified, the option will output the hard-coded',
            '-g': 'Interpret the next names as a glob(7) patterns. whereis always compares only filenames (aka basename) and never complete path. Using directory',
            '-h': 'Display help text and exit.',
            '--help': 'Display help text and exit.',
            '-V': 'Display version and exit.',
            '--version': 'Display version and exit.'
        },
        'examples': [
            'whereis  # locate the binary, source, and manual page files f',
            'whereis -h  # Show help',
            'whereis --version  # Show version'
        ],
        'category': 'Other'
    },
    'which': {
        'desc': 'locate a command',
        'common_flags': {
            '-a': 'print all matching pathnames of each argument',
            '-s': 'silently return 0 if all of the executables were found or 1 otherwise'
        },
        'examples': [
            'which  # locate a command',
            'which -a  # Show all'
        ],
        'category': 'Other'
    },
    'which.debianutils': {
        'desc': 'locate a command',
        'common_flags': {
            '-a': 'print all matching pathnames of each argument',
            '-s': 'silently return 0 if all of the executables were found or 1 otherwise'
        },
        'examples': [
            'which.debianutils  # locate a command',
            'which.debianutils -a  # Show all'
        ],
        'category': 'Other'
    },
    'whois': {
        'desc': 'client for the whois directory service',
        'common_flags': {
            '-h': 'HOST, --host=HOST Connect to HOST.',
            '-H': 'Do not display the legal disclaimers that some registries like to show you.',
            '-p': 'PORT, --port=PORT Connect to PORT.',
            '-I': 'First query whois.iana.org and then follow its referral to the whois server authoritative for that request. This works for IP addresses, AS',
            '--no-recursion': 'Disable recursion from registry to registrar servers.',
            '--verbose': 'Be verbose.',
            '--help': 'Display online help.',
            '--version': 'Display the program version.',
            '-a': 'Also search all the mirrored databases.',
            '-b': 'Return brief IP address ranges with abuse contact.',
            '-B': 'Disable objects filtering. (Show the e-mail addresses.)',
            '-c': 'Return the smallest IP address range with a reference to an irt object.',
            '-d': 'Return the reverse DNS delegation object too.',
            '-g': 'SOURCE:FIRST-LAST Search updates from SOURCE database between FIRST and LAST update serial number. It is useful to obtain Near Real Time',
            '-G': 'Disable grouping of associated objects.'
        },
        'examples': [
            'whois  # client for the whois directory service',
            'whois -h  # Show help',
            'whois --version  # Show version',
            'whois --verbose  # Verbose output'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-addr2line': {
        'desc': 'convert addresses or symbol+offset into file names and line numbers',
        'common_flags': {
            '-a': '--addresses',
            '-b': 'bfdname',
            '--target': '=bfdname',
            '-C': '--demangle[=style]',
            '-e': 'filename',
            '--exe': '=filename',
            '-f': '--functions',
            '-s': '--basenames',
            '-i': '--inlines',
            '-j': '--section',
            '-p': '--pretty-print',
            '-r': '-R',
            '--recurse-limit': '--no-recurse-limit',
            '--recursion-limit': '--no-recursion-limit'
        },
        'examples': [
            'x86_64-linux-gnu-addr2line  # convert addresses or symbol+offset into file names',
            'x86_64-linux-gnu-addr2line -r -f  # Recursive and forced',
            'x86_64-linux-gnu-addr2line -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-ar': {
        'desc': 'create, modify, and extract from archives',
        'common_flags': {
            '--output': 'dirname',
            '--help': 'Displays the list of command-line options supported by ar and then exits.',
            '--version': 'Displays the version information of ar and then exits.',
            '-X': '32_64',
            '--plugin': 'name',
            '--target': 'target',
            '--record-libdeps': 'libdeps',
            '--thin': 'Make the specified archive a thin archive. If it already exists and is a regular archive, the existing members must be present in the same'
        },
        'examples': [
            'x86_64-linux-gnu-ar  # create, modify, and extract from archives',
            'x86_64-linux-gnu-ar --help  # Show help',
            'x86_64-linux-gnu-ar --version  # Show version'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-as': {
        'desc': 'the portable GNU assembler.',
        'common_flags': {
            '-a': 's include symbols',
            '--alternate': 'Begin in alternate macro mode.',
            '--compress-debug-sections': '=zlib-gnu compresses DWARF debug sections using the obsoleted zlib-gnu format. The debug sections are renamed to begin',
            '--nocompress-debug-sections': 'Do not compress DWARF debug sections. This is usually the default for all targets except the x86/x86_64, but a configure time option can be',
            '-D': 'Enable debugging in target specific backends, if supported. Otherwise ignored. Even if ignored, this option is accepted for script',
            '--debug-prefix-map': 'old=new',
            '--defsym': 'sym=value',
            '--dump-config': 'Displays how the assembler is configured and then exits.',
            '--elf-stt-common': '=yes',
            '--emulation': '=name',
            '-f': '\"fast\"---skip whitespace and comment preprocessing (assume source is compiler output).',
            '-g': '--gen-debug',
            '--gstabs': '+',
            '--gdwarf-2': 'Generate DWARF2 debugging information for each assembler line. This may help debugging assembler code, if the debugger can handle it.',
            '--gdwarf-3': 'This option is the same as the --gdwarf-2 option, except that it allows for the possibility of the generation of extra debug information as per'
        },
        'examples': [
            'x86_64-linux-gnu-as  # the portable GNU assembler.',
            'x86_64-linux-gnu-as -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-elfedit': {
        'desc': 'update ELF header and program property of ELF files',
        'common_flags': {
            '--output-abiversion': '=version',
            '--enable-x86-feature': '.',
            '--input-mach': '=machine',
            '--output-mach': '=machine',
            '--input-type': '=type',
            '--output-type': '=type',
            '--input-osabi': '=osabi',
            '--output-osabi': '=osabi',
            '--input-abiversion': '=version',
            '--disable-x86-feature': '=feature',
            '-v': '--version',
            '-h': '--help'
        },
        'examples': [
            'x86_64-linux-gnu-elfedit  # update ELF header and program property of ELF file',
            'x86_64-linux-gnu-elfedit -h  # Show help',
            'x86_64-linux-gnu-elfedit -v  # Show version',
            'x86_64-linux-gnu-elfedit -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-ld': {
        'desc': 'The GNU linker',
        'common_flags': {
            '-W': 'l, (or whatever is appropriate for the particular compiler driver) like this:',
            '-a': 'keyword',
            '--audit': 'AUDITLIB',
            '-b': 'input-format',
            '--format': '=input-format',
            '-c': 'MRI-commandfile',
            '--mri-script': '=MRI-commandfile',
            '-d': 'p These three options are equivalent; multiple forms are supported for compatibility with other linkers. They assign space to common symbols even',
            '--depaudit': 'AUDITLIB',
            '-P': 'AUDITLIB',
            '--enable-linker-version': 'Enables the \"LINKER_VERSION\" linker script directive, described in Output Section Data. If this directive is used in a linker script and this',
            '--disable-linker-version': 'Disables the \"LINKER_VERSION\" linker script directive, so that it does not insert a version string. This is the default.',
            '--enable-non-contiguous-regions': 'This option avoids generating an error if an input section does not fit a matching output section. The linker tries to allocate the input',
            '--enable-non-contiguous-regions-warnings': 'This option enables warnings when \"--enable-non-contiguous-regions\" allows possibly unexpected matches in sections mapping, potentially leading',
            '-e': 'entry'
        },
        'examples': [
            'x86_64-linux-gnu-ld  # The GNU linker',
            'x86_64-linux-gnu-ld -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-ld.bfd': {
        'desc': 'The GNU linker',
        'common_flags': {
            '-W': 'l, (or whatever is appropriate for the particular compiler driver) like this:',
            '-a': 'keyword',
            '--audit': 'AUDITLIB',
            '-b': 'input-format',
            '--format': '=input-format',
            '-c': 'MRI-commandfile',
            '--mri-script': '=MRI-commandfile',
            '-d': 'p These three options are equivalent; multiple forms are supported for compatibility with other linkers. They assign space to common symbols even',
            '--depaudit': 'AUDITLIB',
            '-P': 'AUDITLIB',
            '--enable-linker-version': 'Enables the \"LINKER_VERSION\" linker script directive, described in Output Section Data. If this directive is used in a linker script and this',
            '--disable-linker-version': 'Disables the \"LINKER_VERSION\" linker script directive, so that it does not insert a version string. This is the default.',
            '--enable-non-contiguous-regions': 'This option avoids generating an error if an input section does not fit a matching output section. The linker tries to allocate the input',
            '--enable-non-contiguous-regions-warnings': 'This option enables warnings when \"--enable-non-contiguous-regions\" allows possibly unexpected matches in sections mapping, potentially leading',
            '-e': 'entry'
        },
        'examples': [
            'x86_64-linux-gnu-ld.bfd  # The GNU linker',
            'x86_64-linux-gnu-ld.bfd -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-nm': {
        'desc': 'list symbols from object files',
        'common_flags': {
            '-A': '-o',
            '--print-file-name': 'Precede each symbol by the name of the input file (or archive member) in which it was found, rather than identifying the input file once only,',
            '-a': '--debug-syms',
            '-B': 'The same as --format=bsd (for compatibility with the MIPS nm).',
            '-C': '--demangle[=style]',
            '--no-demangle': 'Do not demangle low-level symbol names. This is the default.',
            '--recurse-limit': '--no-recurse-limit',
            '--recursion-limit': '--no-recursion-limit',
            '-D': '--dynamic',
            '-f': 'format',
            '--format': '=format',
            '-g': '--extern-only',
            '-h': '--help',
            '--ifunc-chars': '=CHARS',
            '-l': '--line-numbers'
        },
        'examples': [
            'x86_64-linux-gnu-nm  # list symbols from object files',
            'x86_64-linux-gnu-nm -h  # Show help',
            'x86_64-linux-gnu-nm -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-objcopy': {
        'desc': 'copy and translate object files',
        'common_flags': {
            '-I': 'bfdname',
            '--input-target': '=bfdname',
            '-O': 'bfdname',
            '--output-target': '=bfdname',
            '-F': 'bfdname',
            '--target': '=bfdname',
            '-B': 'bfdarch',
            '--binary-architecture': '=bfdarch',
            '-j': 'sectionpattern',
            '--only-section': '=.text.* --only-section=!.text.foo',
            '-R': 'sectionpattern',
            '--remove-section': '=.text.* --remove-section=!.text.foo',
            '--keep-section': '=sectionpattern',
            '--remove-relocations': '=.text.* --remove-relocations=!.text.foo',
            '--strip-section-headers': 'Strip section header This option is specific to ELF files. Implies --strip-all and --merge-notes.'
        },
        'examples': [
            'x86_64-linux-gnu-objcopy  # copy and translate object files'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-objdump': {
        'desc': 'display information from object files',
        'common_flags': {
            '-a': 'must be given.',
            '-d': 'must be given.',
            '-D': 'must be given.',
            '-e': 'must be given.',
            '-f': 'must be given.',
            '-g': 'must be given.',
            '-G': 'must be given.',
            '-h': 'must be given.',
            '-H': 'must be given.',
            '-p': 'must be given.',
            '-P': 'must be given.',
            '-r': 'must be given.',
            '-R': 'must be given.',
            '-s': 'must be given.',
            '-S': 'must be given.'
        },
        'examples': [
            'x86_64-linux-gnu-objdump  # display information from object files',
            'x86_64-linux-gnu-objdump -h  # Show help',
            'x86_64-linux-gnu-objdump -r -f  # Recursive and forced',
            'x86_64-linux-gnu-objdump -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-ranlib': {
        'desc': 'generate an index to an archive',
        'common_flags': {
            '-h': '-H',
            '--help': 'Show usage information for ranlib.',
            '-v': '-V',
            '--version': 'Show the version number of ranlib.',
            '-D': 'Operate in deterministic mode. The symbol map archive member\'s header will show zero for the UID, GID, and timestamp. When this option is',
            '-t': 'Update the timestamp of the symbol map of an archive.',
            '-U': 'Do not operate in deterministic mode. This is the inverse of the -D option, above: the archive index will get actual UID, GID, timestamp, and'
        },
        'examples': [
            'x86_64-linux-gnu-ranlib  # generate an index to an archive',
            'x86_64-linux-gnu-ranlib -h  # Show help',
            'x86_64-linux-gnu-ranlib -v  # Show version',
            'x86_64-linux-gnu-ranlib -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-readelf': {
        'desc': 'display information about ELF files',
        'common_flags': {
            '-a': '--all',
            '--unwind': 'and --histogram.',
            '--section-groups': 'and --histogram.',
            '-h': '--file-header',
            '-l': '--program-headers',
            '--segments': 'Displays the information contained in the file\'s segment headers, if it has any.',
            '--quiet': 'Suppress \"no symbols\" diagnostic.',
            '-S': '--sections',
            '--section-headers': 'Displays the information contained in the file\'s section headers, if it has any.',
            '-g': '--section-groups',
            '-t': '--section-details',
            '-s': '--symbols',
            '--syms': 'Displays the entries in symbol table section of the file, if it has one. If a symbol has version information associated with it then this is',
            '--dyn-syms': 'Displays the entries in dynamic symbol table section of the file, if it has one. The output format is the same as the format used by the --syms',
            '--lto-syms': 'Displays the contents of any LTO symbol tables in the file.'
        },
        'examples': [
            'x86_64-linux-gnu-readelf  # display information about ELF files',
            'x86_64-linux-gnu-readelf -h  # Show help',
            'x86_64-linux-gnu-readelf -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-size': {
        'desc': 'list section sizes and total size of binary files',
        'common_flags': {
            '-A': '-B',
            '-G': '--format=compatibility',
            '--help': '-h',
            '-H': '-? Show a summary of acceptable arguments and options.',
            '-d': '-o',
            '-x': '--radix=number',
            '--common': 'Print total size of common symbols in each file. When using Berkeley or GNU format these are included in the bss size.',
            '-t': '--totals',
            '--target': '=bfdname',
            '-v': '-V',
            '--version': 'Display the version number of size.',
            '-f': 'Ignored. This option is used by other versions of the size program, but it is not supported by the GNU Binutils version.'
        },
        'examples': [
            'x86_64-linux-gnu-size  # list section sizes and total size of binary files',
            'x86_64-linux-gnu-size --help  # Show help',
            'x86_64-linux-gnu-size -v  # Show version',
            'x86_64-linux-gnu-size -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'x86_64-linux-gnu-strip': {
        'desc': 'discard symbols and other data from object files',
        'common_flags': {
            '-F': 'bfdname',
            '--target': '=bfdname',
            '--help': 'Show a summary of the options to strip and exit.',
            '--info': 'Display a list showing all architectures and object formats available.',
            '-I': 'bfdname',
            '--input-target': '=bfdname',
            '-O': 'bfdname',
            '--output-target': '=bfdname',
            '-R': 'sectionname',
            '--remove-section': '=.text.* --remove-section=!.text.foo',
            '--keep-section': '=sectionpattern',
            '--remove-relocations': '=.text.* --remove-relocations=!.text.foo',
            '--strip-section-headers': 'Strip section headers. This option is specific to ELF files. Implies --strip-all and --merge-notes.',
            '-s': '--strip-all',
            '-g': '-S'
        },
        'examples': [
            'x86_64-linux-gnu-strip  # discard symbols and other data from object files',
            'x86_64-linux-gnu-strip --help  # Show help'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-addr2line': {
        'desc': 'convert addresses or symbol+offset into file names and line numbers',
        'common_flags': {
            '-a': '--addresses',
            '-b': 'bfdname',
            '--target': '=bfdname',
            '-C': '--demangle[=style]',
            '-e': 'filename',
            '--exe': '=filename',
            '-f': '--functions',
            '-s': '--basenames',
            '-i': '--inlines',
            '-j': '--section',
            '-p': '--pretty-print',
            '-r': '-R',
            '--recurse-limit': '--no-recurse-limit',
            '--recursion-limit': '--no-recursion-limit'
        },
        'examples': [
            'x86_64-w64-mingw32-addr2line  # convert addresses or symbol+offset into file names',
            'x86_64-w64-mingw32-addr2line -r -f  # Recursive and forced',
            'x86_64-w64-mingw32-addr2line -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-ar': {
        'desc': 'create, modify, and extract from archives',
        'common_flags': {
            '--output': 'dirname',
            '--help': 'Displays the list of command-line options supported by ar and then exits.',
            '--version': 'Displays the version information of ar and then exits.',
            '-X': '32_64',
            '--plugin': 'name',
            '--target': 'target',
            '--record-libdeps': 'libdeps',
            '--thin': 'Make the specified archive a thin archive. If it already exists and is a regular archive, the existing members must be present in the same'
        },
        'examples': [
            'x86_64-w64-mingw32-ar  # create, modify, and extract from archives',
            'x86_64-w64-mingw32-ar --help  # Show help',
            'x86_64-w64-mingw32-ar --version  # Show version'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-as': {
        'desc': 'the portable GNU assembler.',
        'common_flags': {
            '-a': 's include symbols',
            '--alternate': 'Begin in alternate macro mode.',
            '--compress-debug-sections': '=zlib-gnu compresses DWARF debug sections using the obsoleted zlib-gnu format. The debug sections are renamed to begin',
            '--nocompress-debug-sections': 'Do not compress DWARF debug sections. This is usually the default for all targets except the x86/x86_64, but a configure time option can be',
            '-D': 'Enable debugging in target specific backends, if supported. Otherwise ignored. Even if ignored, this option is accepted for script',
            '--debug-prefix-map': 'old=new',
            '--defsym': 'sym=value',
            '--dump-config': 'Displays how the assembler is configured and then exits.',
            '--elf-stt-common': '=yes',
            '--emulation': '=name',
            '-f': '\"fast\"---skip whitespace and comment preprocessing (assume source is compiler output).',
            '-g': '--gen-debug',
            '--gstabs': '+',
            '--gdwarf-2': 'Generate DWARF2 debugging information for each assembler line. This may help debugging assembler code, if the debugger can handle it.',
            '--gdwarf-3': 'This option is the same as the --gdwarf-2 option, except that it allows for the possibility of the generation of extra debug information as per'
        },
        'examples': [
            'x86_64-w64-mingw32-as  # the portable GNU assembler.',
            'x86_64-w64-mingw32-as -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-dlltool': {
        'desc': 'create files needed to build and use DLLs',
        'common_flags': {
            '-d': 'filename',
            '--input-def': 'filename',
            '-b': 'filename',
            '--base-file': 'filename',
            '-e': 'filename',
            '--output-exp': 'filename',
            '-z': 'filename',
            '--output-def': 'filename',
            '-l': 'filename',
            '--output-lib': 'filename',
            '-y': 'filename',
            '--output-delaylib': 'filename',
            '--deterministic-libraries': '--non-deterministic-libraries',
            '--export-all-symbols': 'Treat all global and weak defined symbols found in the input object files as symbols to be exported. There is a small list of symbols which are',
            '--no-export-all-symbols': 'Only export symbols explicitly listed in an input .def file or in .drectve sections in the input object files. This is the default behaviour.'
        },
        'examples': [
            'x86_64-w64-mingw32-dlltool  # create files needed to build and use DLLs'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-dllwrap': {
        'desc': 'Ancient tool for generating PE style dll\'s.',
        'common_flags': {
            '-h': 'Show summary of options.',
            '--help': 'Show summary of options.'
        },
        'examples': [
            'x86_64-w64-mingw32-dllwrap  # Ancient tool for generating PE style dll\'s.',
            'x86_64-w64-mingw32-dllwrap -h  # Show help'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-elfedit': {
        'desc': 'update ELF header and program property of ELF files',
        'common_flags': {
            '--output-abiversion': '=version',
            '--enable-x86-feature': '.',
            '--input-mach': '=machine',
            '--output-mach': '=machine',
            '--input-type': '=type',
            '--output-type': '=type',
            '--input-osabi': '=osabi',
            '--output-osabi': '=osabi',
            '--input-abiversion': '=version',
            '--disable-x86-feature': '=feature',
            '-v': '--version',
            '-h': '--help'
        },
        'examples': [
            'x86_64-w64-mingw32-elfedit  # update ELF header and program property of ELF file',
            'x86_64-w64-mingw32-elfedit -h  # Show help',
            'x86_64-w64-mingw32-elfedit -v  # Show version',
            'x86_64-w64-mingw32-elfedit -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-ld': {
        'desc': 'The GNU linker',
        'common_flags': {
            '-W': 'l, (or whatever is appropriate for the particular compiler driver) like this:',
            '-a': 'keyword',
            '--audit': 'AUDITLIB',
            '-b': 'input-format',
            '--format': '=input-format',
            '-c': 'MRI-commandfile',
            '--mri-script': '=MRI-commandfile',
            '-d': 'p These three options are equivalent; multiple forms are supported for compatibility with other linkers. They assign space to common symbols even',
            '--depaudit': 'AUDITLIB',
            '-P': 'AUDITLIB',
            '--enable-linker-version': 'Enables the \"LINKER_VERSION\" linker script directive, described in Output Section Data. If this directive is used in a linker script and this',
            '--disable-linker-version': 'Disables the \"LINKER_VERSION\" linker script directive, so that it does not insert a version string. This is the default.',
            '--enable-non-contiguous-regions': 'This option avoids generating an error if an input section does not fit a matching output section. The linker tries to allocate the input',
            '--enable-non-contiguous-regions-warnings': 'This option enables warnings when \"--enable-non-contiguous-regions\" allows possibly unexpected matches in sections mapping, potentially leading',
            '-e': 'entry'
        },
        'examples': [
            'x86_64-w64-mingw32-ld  # The GNU linker',
            'x86_64-w64-mingw32-ld -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-ld.bfd': {
        'desc': 'The GNU linker',
        'common_flags': {
            '-W': 'l, (or whatever is appropriate for the particular compiler driver) like this:',
            '-a': 'keyword',
            '--audit': 'AUDITLIB',
            '-b': 'input-format',
            '--format': '=input-format',
            '-c': 'MRI-commandfile',
            '--mri-script': '=MRI-commandfile',
            '-d': 'p These three options are equivalent; multiple forms are supported for compatibility with other linkers. They assign space to common symbols even',
            '--depaudit': 'AUDITLIB',
            '-P': 'AUDITLIB',
            '--enable-linker-version': 'Enables the \"LINKER_VERSION\" linker script directive, described in Output Section Data. If this directive is used in a linker script and this',
            '--disable-linker-version': 'Disables the \"LINKER_VERSION\" linker script directive, so that it does not insert a version string. This is the default.',
            '--enable-non-contiguous-regions': 'This option avoids generating an error if an input section does not fit a matching output section. The linker tries to allocate the input',
            '--enable-non-contiguous-regions-warnings': 'This option enables warnings when \"--enable-non-contiguous-regions\" allows possibly unexpected matches in sections mapping, potentially leading',
            '-e': 'entry'
        },
        'examples': [
            'x86_64-w64-mingw32-ld.bfd  # The GNU linker',
            'x86_64-w64-mingw32-ld.bfd -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-nm': {
        'desc': 'list symbols from object files',
        'common_flags': {
            '-A': '-o',
            '--print-file-name': 'Precede each symbol by the name of the input file (or archive member) in which it was found, rather than identifying the input file once only,',
            '-a': '--debug-syms',
            '-B': 'The same as --format=bsd (for compatibility with the MIPS nm).',
            '-C': '--demangle[=style]',
            '--no-demangle': 'Do not demangle low-level symbol names. This is the default.',
            '--recurse-limit': '--no-recurse-limit',
            '--recursion-limit': '--no-recursion-limit',
            '-D': '--dynamic',
            '-f': 'format',
            '--format': '=format',
            '-g': '--extern-only',
            '-h': '--help',
            '--ifunc-chars': '=CHARS',
            '-l': '--line-numbers'
        },
        'examples': [
            'x86_64-w64-mingw32-nm  # list symbols from object files',
            'x86_64-w64-mingw32-nm -h  # Show help',
            'x86_64-w64-mingw32-nm -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-objcopy': {
        'desc': 'copy and translate object files',
        'common_flags': {
            '-I': 'bfdname',
            '--input-target': '=bfdname',
            '-O': 'bfdname',
            '--output-target': '=bfdname',
            '-F': 'bfdname',
            '--target': '=bfdname',
            '-B': 'bfdarch',
            '--binary-architecture': '=bfdarch',
            '-j': 'sectionpattern',
            '--only-section': '=.text.* --only-section=!.text.foo',
            '-R': 'sectionpattern',
            '--remove-section': '=.text.* --remove-section=!.text.foo',
            '--keep-section': '=sectionpattern',
            '--remove-relocations': '=.text.* --remove-relocations=!.text.foo',
            '--strip-section-headers': 'Strip section header This option is specific to ELF files. Implies --strip-all and --merge-notes.'
        },
        'examples': [
            'x86_64-w64-mingw32-objcopy  # copy and translate object files'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-objdump': {
        'desc': 'display information from object files',
        'common_flags': {
            '-a': 'must be given.',
            '-d': 'must be given.',
            '-D': 'must be given.',
            '-e': 'must be given.',
            '-f': 'must be given.',
            '-g': 'must be given.',
            '-G': 'must be given.',
            '-h': 'must be given.',
            '-H': 'must be given.',
            '-p': 'must be given.',
            '-P': 'must be given.',
            '-r': 'must be given.',
            '-R': 'must be given.',
            '-s': 'must be given.',
            '-S': 'must be given.'
        },
        'examples': [
            'x86_64-w64-mingw32-objdump  # display information from object files',
            'x86_64-w64-mingw32-objdump -h  # Show help',
            'x86_64-w64-mingw32-objdump -r -f  # Recursive and forced',
            'x86_64-w64-mingw32-objdump -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-ranlib': {
        'desc': 'generate an index to an archive',
        'common_flags': {
            '-h': '-H',
            '--help': 'Show usage information for ranlib.',
            '-v': '-V',
            '--version': 'Show the version number of ranlib.',
            '-D': 'Operate in deterministic mode. The symbol map archive member\'s header will show zero for the UID, GID, and timestamp. When this option is',
            '-t': 'Update the timestamp of the symbol map of an archive.',
            '-U': 'Do not operate in deterministic mode. This is the inverse of the -D option, above: the archive index will get actual UID, GID, timestamp, and'
        },
        'examples': [
            'x86_64-w64-mingw32-ranlib  # generate an index to an archive',
            'x86_64-w64-mingw32-ranlib -h  # Show help',
            'x86_64-w64-mingw32-ranlib -v  # Show version',
            'x86_64-w64-mingw32-ranlib -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-readelf': {
        'desc': 'display information about ELF files',
        'common_flags': {
            '-a': '--all',
            '--unwind': 'and --histogram.',
            '--section-groups': 'and --histogram.',
            '-h': '--file-header',
            '-l': '--program-headers',
            '--segments': 'Displays the information contained in the file\'s segment headers, if it has any.',
            '--quiet': 'Suppress \"no symbols\" diagnostic.',
            '-S': '--sections',
            '--section-headers': 'Displays the information contained in the file\'s section headers, if it has any.',
            '-g': '--section-groups',
            '-t': '--section-details',
            '-s': '--symbols',
            '--syms': 'Displays the entries in symbol table section of the file, if it has one. If a symbol has version information associated with it then this is',
            '--dyn-syms': 'Displays the entries in dynamic symbol table section of the file, if it has one. The output format is the same as the format used by the --syms',
            '--lto-syms': 'Displays the contents of any LTO symbol tables in the file.'
        },
        'examples': [
            'x86_64-w64-mingw32-readelf  # display information about ELF files',
            'x86_64-w64-mingw32-readelf -h  # Show help',
            'x86_64-w64-mingw32-readelf -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-size': {
        'desc': 'list section sizes and total size of binary files',
        'common_flags': {
            '-A': '-B',
            '-G': '--format=compatibility',
            '--help': '-h',
            '-H': '-? Show a summary of acceptable arguments and options.',
            '-d': '-o',
            '-x': '--radix=number',
            '--common': 'Print total size of common symbols in each file. When using Berkeley or GNU format these are included in the bss size.',
            '-t': '--totals',
            '--target': '=bfdname',
            '-v': '-V',
            '--version': 'Display the version number of size.',
            '-f': 'Ignored. This option is used by other versions of the size program, but it is not supported by the GNU Binutils version.'
        },
        'examples': [
            'x86_64-w64-mingw32-size  # list section sizes and total size of binary files',
            'x86_64-w64-mingw32-size --help  # Show help',
            'x86_64-w64-mingw32-size -v  # Show version',
            'x86_64-w64-mingw32-size -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-strip': {
        'desc': 'discard symbols and other data from object files',
        'common_flags': {
            '-F': 'bfdname',
            '--target': '=bfdname',
            '--help': 'Show a summary of the options to strip and exit.',
            '--info': 'Display a list showing all architectures and object formats available.',
            '-I': 'bfdname',
            '--input-target': '=bfdname',
            '-O': 'bfdname',
            '--output-target': '=bfdname',
            '-R': 'sectionname',
            '--remove-section': '=.text.* --remove-section=!.text.foo',
            '--keep-section': '=sectionpattern',
            '--remove-relocations': '=.text.* --remove-relocations=!.text.foo',
            '--strip-section-headers': 'Strip section headers. This option is specific to ELF files. Implies --strip-all and --merge-notes.',
            '-s': '--strip-all',
            '-g': '-S'
        },
        'examples': [
            'x86_64-w64-mingw32-strip  # discard symbols and other data from object files',
            'x86_64-w64-mingw32-strip --help  # Show help'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-windmc': {
        'desc': 'generates Windows message resources',
        'common_flags': {
            '-a': '--ascii_in',
            '-A': '--ascii_out',
            '-b': '--binprefix',
            '-c': '--customflag',
            '-C': 'codepage',
            '--codepage_in': 'codepage',
            '-d': '--decimal_values',
            '-e': 'ext',
            '--extension': 'ext',
            '-F': 'target',
            '--target': 'target',
            '-h': 'path',
            '--headerdir': 'path',
            '-H': '--help',
            '-m': 'characters'
        },
        'examples': [
            'x86_64-w64-mingw32-windmc  # generates Windows message resources',
            'x86_64-w64-mingw32-windmc -h  # Show help',
            'x86_64-w64-mingw32-windmc -a  # Show all'
        ],
        'category': 'Other'
    },
    'x86_64-w64-mingw32-windres': {
        'desc': 'manipulate Windows resources',
        'common_flags': {
            '-i': 'filename',
            '--input': 'filename',
            '-o': 'filename',
            '--output': 'filename',
            '-J': 'format',
            '--input-format': 'format',
            '-O': 'format',
            '--output-format': 'format',
            '-F': 'target',
            '--target': 'target',
            '--preprocessor': 'option has not been specified then a default set of preprocessor arguments will be used, with any --preprocessor-arg options',
            '--preprocessor-arg': 'option',
            '-I': 'directory',
            '--include-dir': 'directory',
            '-D': 'target'
        },
        'examples': [
            'x86_64-w64-mingw32-windres  # manipulate Windows resources'
        ],
        'category': 'Other'
    },
    'xargs': {
        'desc': 'build and execute command lines from standard input',
        'common_flags': {
            '-0': 'Input items are terminated by a null character instead of by whitespace, and the quotes and backslash are not special (every character is',
            '--null': 'Input items are terminated by a null character instead of by whitespace, and the quotes and backslash are not special (every character is',
            '-a': 'file, --arg-file=file',
            '--delimiter': '=delim, -d delim',
            '-E': 'eof-str',
            '-e': '[eof-str], --eof[=eof-str]',
            '-I': '{}. The -i option is deprecated; use -I instead.',
            '-i': '[replace-str], --replace[=replace-str]',
            '-L': 'max-lines',
            '-l': '[max-lines], --max-lines[=max-lines]',
            '-n': 'max-args, --max-args=max-args',
            '-P': 'max-procs, --max-procs=max-procs',
            '-o': 'Reopen stdin as /dev/tty in the child process before executing the command. This is useful if you want xargs to run an interactive applica‐',
            '--open-tty': 'Reopen stdin as /dev/tty in the child process before executing the command. This is useful if you want xargs to run an interactive applica‐',
            '-p': 'Prompt the user about whether to run each command line and read a line from the terminal. Only run the command line if the response starts'
        },
        'examples': [
            'xargs  # build and execute command lines from standard inpu',
            'xargs -a  # Show all'
        ],
        'category': 'Other'
    },
    'xauth': {
        'desc': 'X authority file utility',
        'common_flags': {
            '-f': 'authfile',
            '-q': 'This option indicates that xauth should operate quietly and not print unsolicited status messages. This is the default if an xauth command',
            '-v': 'This option indicates that xauth should operate verbosely and print status messages indicating the results of various operations (e.g., how',
            '-i': 'This option indicates that xauth should ignore any authority file locks. Normally, xauth will refuse to read or edit any authority files',
            '-b': 'This option indicates that xauth should attempt to break any authority file locks before proceeding. Use this option only to clean up stale',
            '-n': 'This option indicates that xauth should not attempt to resolve any hostnames, but should simply always print the host address as stored in',
            '-V': 'This option shows the version number of the xauth executable.'
        },
        'examples': [
            'xauth  # X authority file utility',
            'xauth -v  # Show version',
            'xauth -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'xdg-user-dirs-update': {
        'desc': 'Update XDG user dir configuration',
        'common_flags': {
            '--help': 'Print help output and exit.',
            '--force': 'Update existing user-dirs.dirs, but force a full reset. This means: Don\'t reset nonexisting directories to HOME, rather recreate the directory.',
            '--dummy-output': 'PATH',
            '--set': 'NAME PATH'
        },
        'examples': [
            'xdg-user-dirs-update  # Update XDG user dir configuration',
            'xdg-user-dirs-update --help  # Show help'
        ],
        'category': 'Other'
    },
    'xsubpp': {
        'desc': 'compiler to convert Perl XS code into C code',
        'common_flags': {
            '-h': 'iertype',
            '-e': 'xcept',
            '-t': 'ypemap typemap',
            '-o': 'utput filename',
            '-v': 'Prints the xsubpp version number to standard output, then exits.',
            '-p': 'rototypes',
            '-n': 'oargtypes',
            '-C': '++ Currently doesn\'t do anything at all. This flag has been a no-op for many versions of perl, at least as far back as perl5.003_07. It\'s',
            '-s': '=... or -strip=...'
        },
        'examples': [
            'xsubpp  # compiler to convert Perl XS code into C code',
            'xsubpp -h  # Show help',
            'xsubpp -v  # Show version',
            'xsubpp -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'xz': {
        'desc': 'Compress or decompress .xz and .lzma files',
        'common_flags': {
            '-z': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '--compress': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '-d': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--decompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--uncompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '-t': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '--test': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '-l': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '--list': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '-k': 'Don\'t delete the input files.',
            '--keep': 'Don\'t delete the input files.',
            '-f': 'This option has several effects:',
            '--force': 'This option has several effects:',
            '-c': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.',
            '--stdout': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.'
        },
        'examples': [
            'xz  # Compress or decompress .xz and .lzma files'
        ],
        'category': 'Other'
    },
    'xzcat': {
        'desc': 'Compress or decompress .xz and .lzma files',
        'common_flags': {
            '-z': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '--compress': 'Compress. This is the default operation mode when no operation mode option is specified and no other operation mode is implied from the com‐',
            '-d': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--decompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '--uncompress': 'Decompress. After successful decompression, the source file is removed unless writing to standard output or --keep was specified.',
            '-t': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '--test': 'Test the integrity of compressed files. This option is equivalent to --decompress --stdout except that the decompressed data is discarded',
            '-l': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '--list': 'Print information about compressed files. No uncompressed output is produced, and no files are created or removed. In list mode, the pro‐',
            '-k': 'Don\'t delete the input files.',
            '--keep': 'Don\'t delete the input files.',
            '-f': 'This option has several effects:',
            '--force': 'This option has several effects:',
            '-c': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.',
            '--stdout': 'Write the compressed or decompressed data to standard output instead of a file. This implies --keep.'
        },
        'examples': [
            'xzcat  # Compress or decompress .xz and .lzma files'
        ],
        'category': 'Other'
    },
    'yes': {
        'desc': 'output a string repeatedly until killed',
        'common_flags': {
            '--help': 'display this help and exit',
            '--version': 'output version information and exit'
        },
        'examples': [
            'yes  # output a string repeatedly until killed',
            'yes --help  # Show help',
            'yes --version  # Show version'
        ],
        'category': 'Other'
    },
    'ypdomainname': {
        'desc': 'show or set the system\'s NIS/YP domain name',
        'common_flags': {
            '-a': 'Display the alias name of the host (if used). This option is deprecated and should not be used anymore.',
            '--alias': 'Display the alias name of the host (if used). This option is deprecated and should not be used anymore.',
            '-A': 'Displays all FQDNs of the machine. This option enumerates all configured network addresses on all configured network interfaces, and trans‐',
            '--all-fqdns': 'Displays all FQDNs of the machine. This option enumerates all configured network addresses on all configured network interfaces, and trans‐',
            '-b': 'Always set a hostname; this allows the file specified by -F to be non-existent or empty, in which case the default hostname localhost will be',
            '--boot': 'Always set a hostname; this allows the file specified by -F to be non-existent or empty, in which case the default hostname localhost will be',
            '-d': 'Display the name of the DNS domain. Don\'t use the command domainname to get the DNS domain name because it will show the NIS domain name and',
            '--domain': 'Display the name of the DNS domain. Don\'t use the command domainname to get the DNS domain name because it will show the NIS domain name and',
            '-f': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '--fqdn': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '--long': 'Display the FQDN (Fully Qualified Domain Name). A FQDN consists of a short host name and the DNS domain name. Unless you are using bind or',
            '-F': 'filename',
            '--file': 'filename',
            '-i': 'Display the network address(es) of the host name. Note that this works only if the host name can be resolved. Avoid using this option; use',
            '--ip-address': 'Display the network address(es) of the host name. Note that this works only if the host name can be resolved. Avoid using this option; use'
        },
        'examples': [
            'ypdomainname  # show or set the system\'s NIS/YP domain name',
            'ypdomainname -a  # Show all'
        ],
        'category': 'Other'
    },
    'zcat': {
        'desc': 'compress or expand files',
        'common_flags': {
            '-a': '--ascii',
            '-c': '--stdout --to-stdout',
            '-d': '--decompress --uncompress',
            '-f': '--force',
            '-h': '--help',
            '-k': '--keep',
            '-l': '--list',
            '-L': '--license',
            '-n': '--no-name',
            '-N': '--name',
            '-q': '--quiet',
            '-r': '--recursive',
            '-S': '.suf --suffix .suf',
            '--synchronous': 'Use synchronous output. With this option, gzip is less likely to lose data during a system crash, but it can be considerably slower.',
            '-t': '--test'
        },
        'examples': [
            'zcat  # compress or expand files',
            'zcat -h  # Show help',
            'zcat -r -f  # Recursive and forced',
            'zcat -a  # Show all'
        ],
        'category': 'Other'
    },
    'zip': {
        'desc': 'package and compress (archive) files',
        'common_flags': {
            '-a': '--ascii',
            '-A': 'S',
            '--archive-clear': '[WIN32] Once archive is created (and tested if -T is used, which is recommended), clear the archive bits of files processed. WARNING: Once',
            '--archive-set': '[WIN32] Only include files that have the archive bit set. Directories are not stored when -AS is used, though by default the paths of en‐',
            '-B': 'n [TANDEM] set Edit/Enscribe formatting options with n defined as',
            '-b': 'path',
            '--temp-path': 'path',
            '-c': '--entry-comments',
            '-C': '5',
            '--preserve-case-2': '[VMS] Preserve case ODS2 on VMS. Negating this option (-C2-) downcases.',
            '--preserve-case-5': '[VMS] Preserve case ODS5 on VMS. Negating this option (-C5-) downcases.',
            '-d': 'd',
            '--display-bytes': 'Display running byte counts showing the bytes zipped and the bytes to go.',
            '--display-counts': 'Display running count of entries zipped and entries to go.',
            '--display-dots': 'Display dots while each entry is zipped (except on ports that have their own progress indicator). See -ds below for setting dot size. The'
        },
        'examples': [
            'zip  # package and compress (archive) files',
            'zip archive.zip file1 file2  # Create zip',
            'zip -r archive.zip directory/  # Recursive zip'
        ],
        'category': 'Other'
    },
    'zipcloak': {
        'desc': 'encrypt entries in a zipfile',
        'common_flags': {
            '-b': 'path',
            '--temp-path': 'path',
            '-d': '--decrypt',
            '-h': '--help',
            '-L': '--license',
            '-O': 'path',
            '--output-file': 'zipfile',
            '-q': '--quiet',
            '-v': '--version'
        },
        'examples': [
            'zipcloak  # encrypt entries in a zipfile',
            'zipcloak -h  # Show help',
            'zipcloak -v  # Show version',
            'zipcloak -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'zipdetails': {
        'desc': 'display the internal structure of zip files',
        'common_flags': {
            '---------': '-------'
        },
        'examples': [
            'zipdetails  # display the internal structure of zip files'
        ],
        'category': 'Other'
    },
    'zipinfo': {
        'desc': 'list detailed information about a ZIP archive',
        'common_flags': {
            '-1': 'list filenames only, one per line. This option excludes all others; headers, trailers and zipfile comments are never printed. It is in‐',
            '-2': 'list filenames only, one per line, but allow headers (-h), trailers (-t) and zipfile comments (-z), as well. This option may be useful in',
            '-s': 'list zipfile info in short Unix ``ls -l\'\' format. This is the default behavior; see below.',
            '-m': 'list zipfile info in medium Unix ``ls -l\'\' format. Identical to the -s output, except that the compression factor, expressed as a percent‐',
            '-l': 'list zipfile info in long Unix ``ls -l\'\' format. As with -m except that the compressed size (in bytes) is printed instead of the compression',
            '-v': 'list zipfile information in verbose, multi-page format.',
            '-h': 'list header line. The archive name, actual size (in bytes) and total number of files is printed.',
            '-M': 'pipe all output through an internal pager similar to the Unix more(1) command. At the end of a screenful of output, zipinfo pauses with a',
            '-t': 'list totals for files listed or for all files. The number of files listed, their uncompressed and compressed total sizes , and their overall',
            '-T': 'print the file dates and times in a sortable decimal format (yymmdd.hhmmss). The default date format is a more standard, human-readable ver‐',
            '-U': '[UNICODE_SUPPORT only] modify or disable UTF-8 handling. When UNICODE_SUPPORT is available, the option -U forces unzip to escape all non-',
            '-z': 'include the archive comment (if any) in the listing.'
        },
        'examples': [
            'zipinfo  # list detailed information about a ZIP archive',
            'zipinfo -h  # Show help',
            'zipinfo -v  # Show version',
            'zipinfo -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'zipnote': {
        'desc': 'write the comments in zipfile to stdout, edit comments and rename files in zipfile',
        'common_flags': {
            '-w': 'Write comments to a zipfile from stdin (see below).',
            '-b': 'path',
            '-h': 'Show a short help.',
            '-v': 'Show version information.',
            '-L': 'Show software license.'
        },
        'examples': [
            'zipnote  # write the comments in zipfile to stdout, edit comm',
            'zipnote -h  # Show help',
            'zipnote -v  # Show version',
            'zipnote -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'zipsplit': {
        'desc': 'split a zipfile into smaller zipfiles',
        'common_flags': {
            '-t': 'Report how many files it will take, but don\'t make them.',
            '-i': 'Make index (zipsplit.idx) and count its size against first zip file.',
            '-n': 'size',
            '-r': 'room',
            '-b': 'path',
            '-p': 'Pause between output zip files.',
            '-s': 'Do a sequential split even if it takes more zip files.',
            '-h': 'Show a short help.',
            '-v': 'Show version information.',
            '-L': 'Show software license.'
        },
        'examples': [
            'zipsplit  # split a zipfile into smaller zipfiles',
            'zipsplit -h  # Show help',
            'zipsplit -v  # Show version',
            'zipsplit -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'znew': {
        'desc': 'recompress .Z files to .gz files',
        'common_flags': {
            '-f': 'Force recompression from .Z to .gz format even if a .gz file already exists.',
            '-t': 'Tests the new files before deleting originals.',
            '-v': 'Verbose. Display the name and percentage reduction for each file compressed.',
            '-9': 'Use the slowest compression method (optimal compression).',
            '-P': 'Use pipes for the conversion to reduce disk space usage.',
            '-K': 'Keep a .Z file when it is smaller than the .gz file; implies -t.'
        },
        'examples': [
            'znew  # recompress .Z files to .gz files',
            'znew -v  # Show version',
            'znew -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'zshbuiltins': {
        'desc': 'zsh built-in commands',
        'common_flags': {
            '-f': 'prints full time-date stamps in the US `MM/DD/YY hh:mm\' format',
            '-r': ', if the function is not found, it is silently left unresolved until execution; with -R, an error message is printed and command processing',
            '-c': 'clear the directory stack.',
            '-l': 'print directory names in full instead of using of using ~ expressions (see Dynamic and Static named directories in zshexpn(1)).',
            '-p': 'print directory entries one per line.',
            '-v': 'number the directories in the stack when printing.',
            '-I': 'restricts to only internal events (not from $HISTFILE)',
            '-L': 'restricts to only local events (not from other shells, see SHARE_HISTORY in zshoptions(1) -- note that $HISTFILE is considered local',
            '-m': 'takes the first argument as a pattern (which should be quoted) and only the history events matching this pattern are considered',
            '-d': 'prints timestamps for each event',
            '-E': 'prints full time-date stamps in the European `dd.mm.yyyy hh:mm\' format',
            '-i': 'prints full time-date stamps in ISO8601 `yyyy-mm-dd hh:mm\' format',
            '-t': 'fmt prints time and date stamps in the given format; fmt is formatted with the strftime function with the zsh extensions described for the',
            '-D': 'prints elapsed times; may be combined with one of the options above',
            '-a': 'Print arguments with the column incrementing first. Only useful with the -c and -C options.'
        },
        'examples': [
            'zshbuiltins  # zsh built-in commands',
            'zshbuiltins -v  # Show version',
            'zshbuiltins -v  # Verbose output',
            'zshbuiltins -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'zshmodules': {
        'desc': 'zsh loadable modules',
        'common_flags': {
            '-A': 'array',
            '-H': 'hash',
            '-f': 'fd Use the file on file descriptor fd instead of named files; no list of file names is allowed in this case.',
            '-F': 'fmt Supplies a strftime (see strftime(3)) string for the formatting of the time elements. The format string supports all of the zsh ex‐',
            '-g': 'Show the time elements in the GMT time zone. The -s option is implied.',
            '-l': 'List the names of the type elements (to standard output or an array as appropriate) and return immediately; arguments, and options',
            '-L': 'Perform an lstat (see lstat(2)) rather than a stat system call. In this case, if the file is a link, information about the link it‐',
            '-n': 'Always show the names of files. Usually these are only shown when output is to standard output and there is more than one file in the',
            '-N': 'Never show the names of files.',
            '-o': 'If a raw file mode is printed, show it in octal, which is more useful for human consumption than the default of decimal. A leading',
            '-r': 'Print raw data (the default format) alongside string data (the -s format); the string data appears in parentheses after the raw data.',
            '-s': 'Print mode, uid, gid and the three time elements as strings instead of numbers. In each case the format is like that of ls -l.',
            '-t': 'Always show the type names for the elements of struct stat. Usually these are only shown when output is to standard output and no in‐',
            '-T': 'Never show the type names of the struct stat elements.',
            '-u': 'fd file'
        },
        'examples': [
            'zshmodules  # zsh loadable modules',
            'zshmodules -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'zshparam': {
        'desc': 'zsh parameters',
        'common_flags': {
            '-z': 'r -- $ZLE_LINE_ABORTED\' can be used to recover the line. Only the most recent line of this kind is remembered.'
        },
        'examples': [
            'zshparam  # zsh parameters'
        ],
        'category': 'Other'
    },
    'zshtcpsys': {
        'desc': 'zsh tcp system',
        'common_flags': {
            '-p': 'var can be used; on return, $var is set to the number of the pattern using ordinary zsh indexing, i.e. the first is 1, and so on. Note'
        },
        'examples': [
            'zshtcpsys  # zsh tcp system'
        ],
        'category': 'Other'
    },
    'zsoelim': {
        'desc': 'satisfy .so requests in roff input',
        'common_flags': {
            '-C': 'This flag is available for compatibility with other soelim programs. Its use is to enable .so requests followed by something other than',
            '--compatible': 'This flag is available for compatibility with other soelim programs. Its use is to enable .so requests followed by something other than',
            '-h': 'Print a help message and exit.',
            '--help': 'Print a help message and exit.',
            '-V': 'Display version information.',
            '--version': 'Display version information.'
        },
        'examples': [
            'zsoelim  # satisfy .so requests in roff input',
            'zsoelim -h  # Show help',
            'zsoelim --version  # Show version'
        ],
        'category': 'Other'
    },
    'ls': {
        'desc': 'list directory contents',
        'common_flags': {
            '-l': 'use a long listing format',
            '-a': 'do not ignore entries starting with .',
            '-h': 'with -l, print sizes in human readable format',
            '-R': 'list subdirectories recursively',
            '-t': 'sort by modification time, newest first',
            '-r': 'reverse order while sorting',
            '-S': 'sort by file size, largest first'
        },
        'examples': [
            'ls  # list directory contents',
            'ls -la  # List all with details',
            'ls -lh  # Human-readable sizes',
            'ls -R  # Recursive listing'
        ],
        'category': 'Other'
    },
    'cp': {
        'desc': 'copy files and directories',
        'common_flags': {
            '-r': 'copy directories recursively',
            '-i': 'prompt before overwrite',
            '-f': 'force copy by removing destination',
            '-p': 'preserve mode, ownership, timestamps',
            '-v': 'verbose - explain what is being done',
            '-a': 'archive mode; equals -dR --preserve=all'
        },
        'examples': [
            'cp  # copy files and directories',
            'cp source dest  # Copy file',
            'cp -r source/ dest/  # Copy directory'
        ],
        'category': 'Other'
    },
    'mv': {
        'desc': 'move (rename) files',
        'common_flags': {
            '-i': 'prompt before overwrite',
            '-f': 'force move by overwriting destination',
            '-v': 'verbose - explain what is being done',
            '-n': 'do not overwrite an existing file'
        },
        'examples': [
            'mv  # move (rename) files',
            'mv old new  # Rename/move file',
            'mv file directory/  # Move to directory'
        ],
        'category': 'Other'
    },
    'cat': {
        'desc': 'concatenate files and print on the standard output',
        'common_flags': {
            '-n': 'number all output lines',
            '-b': 'number nonempty output lines',
            '-s': 'suppress repeated empty output lines',
            '-v': 'display non-printing characters'
        },
        'examples': [
            'cat  # concatenate files and print on the standard output',
            'cat -v  # Show version',
            'cat -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'sed': {
        'desc': 'stream editor for filtering and transforming text',
        'common_flags': {
            '-i': 'edit files in place',
            '-e': 'add the script to commands',
            '-n': 'suppress automatic printing',
            '-r': 'use extended regular expressions'
        },
        'examples': [
            'sed  # stream editor for filtering and transforming text',
            'sed \'s/old/new/g\' file.txt  # Replace text',
            'sed -i \'s/old/new/g\' file.txt  # Edit in place'
        ],
        'category': 'Other'
    },
    'ps': {
        'desc': 'report a snapshot of the current processes',
        'common_flags': {
            'aux': 'show all processes with user info',
            '-e': 'select all processes',
            '-f': 'full-format listing'
        },
        'examples': [
            'ps  # report a snapshot of the current processes',
            'ps aux  # List all processes',
            'ps aux | grep process  # Find specific process'
        ],
        'category': 'Other'
    },
    'mkfifo': {
        'desc': 'make FIFOs (named pipes)',
        'common_flags': {
            '-m': 'set file permission bits to MODE',
            '-Z': 'set the SELinux security context'
        },
        'examples': [
            'mkfifo  # make FIFOs (named pipes)'
        ],
        'category': 'Other'
    },
    'head': {
        'desc': 'output the first part of files',
        'common_flags': {
            '-n': 'print the first NUM lines',
            '-c': 'print the first NUM bytes'
        },
        'examples': [
            'head  # output the first part of files'
        ],
        'category': 'Other'
    },
    'tail': {
        'desc': 'output the last part of files',
        'common_flags': {
            '-n': 'output the last NUM lines',
            '-f': 'output appended data as file grows',
            '-F': 'same as -f, but retry if inaccessible'
        },
        'examples': [
            'tail  # output the last part of files'
        ],
        'category': 'Other'
    },
    'cut': {
        'desc': 'remove sections from each line of files',
        'common_flags': {
            '-f': 'select only these fields',
            '-d': 'use DELIM instead of TAB',
            '-c': 'select only these characters'
        },
        'examples': [
            'cut  # remove sections from each line of files'
        ],
        'category': 'Other'
    },
    'sort': {
        'desc': 'sort lines of text files',
        'common_flags': {
            '-r': 'reverse the result',
            '-n': 'compare by numerical value',
            '-u': 'output only unique lines',
            '-k': 'sort via a key'
        },
        'examples': [
            'sort  # sort lines of text files'
        ],
        'category': 'Other'
    },
    'uniq': {
        'desc': 'report or omit repeated lines',
        'common_flags': {
            '-c': 'prefix lines by number of occurrences',
            '-d': 'only print duplicate lines',
            '-u': 'only print unique lines'
        },
        'examples': [
            'uniq  # report or omit repeated lines'
        ],
        'category': 'Other'
    },
    'wc': {
        'desc': 'print newline, word, and byte counts',
        'common_flags': {
            '-l': 'print the newline counts',
            '-w': 'print the word counts',
            '-c': 'print the byte counts'
        },
        'examples': [
            'wc  # print newline, word, and byte counts'
        ],
        'category': 'Other'
    },
    'diff': {
        'desc': 'compare files line by line',
        'common_flags': {
            '-u': 'output unified context',
            '-r': 'recursively compare subdirectories',
            '-q': 'report only when files differ'
        },
        'examples': [
            'diff  # compare files line by line'
        ],
        'category': 'Other'
    },
    'du': {
        'desc': 'estimate file space usage',
        'common_flags': {
            '-h': 'print sizes in human readable format',
            '-s': 'display only a total',
            '-c': 'produce a grand total'
        },
        'examples': [
            'du  # estimate file space usage',
            'du -h  # Show help'
        ],
        'category': 'Other'
    },
    'touch': {
        'desc': 'change file timestamps or create empty files',
        'common_flags': {
            '-a': 'change only the access time',
            '-m': 'change only the modification time',
            '-c': 'do not create any files'
        },
        'examples': [
            'touch  # change file timestamps or create empty files',
            'touch -a  # Show all'
        ],
        'category': 'Other'
    },
    'ln': {
        'desc': 'make links between files',
        'common_flags': {
            '-s': 'make symbolic links',
            '-f': 'force, remove existing destinations',
            '-v': 'print name of each linked file'
        },
        'examples': [
            'ln  # make links between files',
            'ln -v  # Show version',
            'ln -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'mknod': {
        'desc': 'make block or character special files',
        'common_flags': {
            '-m': 'set file permission bits',
            '-Z': 'set SELinux security context'
        },
        'examples': [
            'mknod  # make block or character special files'
        ],
        'category': 'Other'
    },
    'paste': {
        'desc': 'merge lines of files',
        'common_flags': {
            '-d': 'use characters from LIST instead of tabs',
            '-s': 'paste one file at a time'
        },
        'examples': [
            'paste  # merge lines of files'
        ],
        'category': 'Other'
    },
    'mount': {
        'desc': 'mount a filesystem',
        'common_flags': {
            '-t': 'specify filesystem type',
            '-o': 'set mount options',
            '-r': 'mount read-only'
        },
        'examples': [
            'mount  # mount a filesystem'
        ],
        'category': 'Other'
    },
    'umount': {
        'desc': 'unmount filesystems',
        'common_flags': {
            '-f': 'force unmount',
            '-l': 'lazy unmount',
            '-r': 'remount read-only'
        },
        'examples': [
            'umount  # unmount filesystems',
            'umount -r -f  # Recursive and forced'
        ],
        'category': 'Other'
    },
    'lsblk': {
        'desc': 'list block devices',
        'common_flags': {
            '-a': 'show all devices',
            '-f': 'show filesystem information',
            '-p': 'show full device paths'
        },
        'examples': [
            'lsblk  # list block devices',
            'lsblk -a  # Show all'
        ],
        'category': 'Other'
    },
    'blkid': {
        'desc': 'locate/print block device attributes',
        'common_flags': {
            '-s': 'show specified tag',
            '-o': 'set output format'
        },
        'examples': [
            'blkid  # locate/print block device attributes'
        ],
        'category': 'Other'
    },
    'fdisk': {
        'desc': 'manipulate disk partition table',
        'common_flags': {
            '-l': 'list partition tables',
            '-u': 'display in sectors'
        },
        'examples': [
            'fdisk  # manipulate disk partition table'
        ],
        'category': 'Other'
    },
    'gcc': {
        'desc': 'GNU project C and C++ compiler',
        'common_flags': {
            '-o': 'place output into file',
            '-c': 'compile without linking',
            '-g': 'produce debugging information',
            '-O': 'optimize code'
        },
        'examples': [
            'gcc  # GNU project C and C++ compiler'
        ],
        'category': 'Other'
    },
    'rmdir': {
        'desc': 'remove empty directories',
        'common_flags': {
            '-p': 'remove directory and ancestors',
            '-v': 'output diagnostic for each directory'
        },
        'examples': [
            'rmdir  # remove empty directories',
            'rmdir -v  # Show version',
            'rmdir -v  # Verbose output'
        ],
        'category': 'Other'
    },
    'cd': {
        'desc': 'change the shell working directory',
        'common_flags': {
            '~': 'go to home directory',
            '-': 'go to previous directory',
            '..': 'go to parent directory'
        },
        'examples': [
            'cd  # change the shell working directory'
        ],
        'category': 'Other'
    },
    'whoami': {
        'desc': 'Print effective user name',
        'common_flags': {},
        'examples': [
            'whoami    # Show current username',
        ],
        'category': 'User Information'
    },
    'id': {
        'desc': 'Print user and group information',
        'common_flags': {
            '-u': 'Print only effective user ID',
            '-g': 'Print only effective group ID',
            '-G': 'Print all group IDs',
            '-n': 'Print name instead of number',
            '-r': 'Print real ID instead of effective',
        },
        'examples': [
            'id                # Show all user/group info',
            'id -u             # Show user ID only',
            'id -un            # Show username',
            'id username       # Show info for specific user',
        ],
        'category': 'User Information'
    },
    'uname': {
        'desc': 'Print system information',
        'common_flags': {
            '-a': 'Print all information',
            '-s': 'Print kernel name',
            '-n': 'Print network node hostname',
            '-r': 'Print kernel release',
            '-v': 'Print kernel version',
            '-m': 'Print machine hardware name',
            '-o': 'Print operating system',
        },
        'examples': [
            'uname             # Print kernel name',
            'uname -a          # Print all system info',
            'uname -r          # Print kernel version',
            'uname -m          # Print architecture (x86_64, arm64, etc)',
        ],
        'category': 'System Information'
    },
    'pwd': {
        'desc': 'Print working directory',
        'common_flags': {
            '-L': 'Print logical path (with symlinks)',
            '-P': 'Print physical path (resolve symlinks)',
        },
        'examples': [
            'pwd               # Show current directory',
            'pwd -P            # Show physical path',
        ],
        'category': 'Navigation'
    },
    'env': {
        'desc': 'Display or set environment variables',
        'common_flags': {
            '-i': 'Start with empty environment',
            '-u': 'Remove variable from environment',
            '-0': 'End output lines with null byte'
        },
        'examples': [
            'env                    # Show all environment variables',
            'env | grep PATH       # Show PATH variable',
            'env VAR=value command # Run command with variable set'
        ],
        'category': 'Environment'
    },
    'printenv': {
        'desc': 'Print environment variables',
        'common_flags': {
            '-0': 'End output with null byte instead of newline'
        },
        'examples': [
            'printenv              # Show all variables',
            'printenv PATH         # Show PATH value',
            'printenv USER HOME    # Show multiple variables'
        ],
        'category': 'Environment'
    },
    'echo': {
        'desc': 'Display a line of text',
        'common_flags': {
            '-n': 'Do not output trailing newline',
            '-e': 'Enable interpretation of backslash escapes',
            '-E': 'Disable interpretation of backslash escapes'
        },
        'examples': [
            'echo "Hello World"    # Print text',
            'echo $PATH            # Print variable',
            'echo -n "No newline" # No trailing newline'
        ],
        'category': 'Text Processing'
    },
    'date': {
        'desc': 'Display or set system date and time',
        'common_flags': {
            '-d': 'Display time described by string',
            '-r': 'Display modification time of file',
            '-u': 'Display UTC time',
            '+FORMAT': 'Output date/time in specified format'
        },
        'examples': [
            'date                      # Current date/time',
            'date +%Y-%m-%d            # 2024-01-15',
            'date +%s                  # Unix timestamp',
            'date -d "tomorrow"        # Tomorrow\'s date'
        ],
        'category': 'System Information'
    },
    'uptime': {
        'desc': 'Show how long system has been running',
        'common_flags': {
            '-p': 'Show uptime in pretty format',
            '-s': 'Show system up since date/time'
        },
        'examples': [
            'uptime                # Show uptime and load',
            'uptime -p             # Pretty format',
            'uptime -s             # Up since when'
        ],
        'category': 'System Information'
    },
    'free': {
        'desc': 'Display memory usage',
        'common_flags': {
            '-h': 'Human readable (GB, MB)',
            '-m': 'Show in megabytes',
            '-g': 'Show in gigabytes',
            '-t': 'Show total line',
            '-s': 'Update every N seconds'
        },
        'examples': [
            'free                  # Show memory usage',
            'free -h               # Human readable',
            'free -h -s 5          # Update every 5 seconds'
        ],
        'category': 'System Information'
    },
    'df': {
        'desc': 'Report file system disk space usage',
        'common_flags': {
            '-h': 'Human readable sizes',
            '-T': 'Show file system type',
            '-i': 'Show inode information',
            '-a': 'Include all file systems'
        },
        'examples': [
            'df                    # Show disk usage',
            'df -h                 # Human readable',
            'df -hT                # With file system type'
        ],
        'category': 'Disk Usage'
    },
    'which': {
        'desc': 'Locate a command',
        'common_flags': {
            '-a': 'Show all matches in PATH'
        },
        'examples': [
            'which python          # Find python location',
            'which -a python       # Find all python locations'
        ],
        'category': 'System Information'
    },
    'type': {
        'desc': 'Display information about command type',
        'common_flags': {
            '-a': 'Show all locations',
            '-t': 'Show type only',
            '-p': 'Show path only'
        },
        'examples': [
            'type ls               # Check if builtin or external',
            'type -a python        # Show all python locations'
        ],
        'category': 'System Information'
    },

}
