cmdhelp - Command Line Helper
==============================

WHAT YOU HAVE
-------------
• cmdhelp tool (needs databases to work)
• Scrapers to generate databases from your system


STEP 1: GENERATE DATABASES
---------------------------

PowerShell (Windows):
  python scrape_powershell_robust.py
  → Creates: powershell_scraped_database.py

CMD (Windows):
  python scrape_cmd.py
  → Creates: cmd_scraped_database.py

Linux Man Pages:
  python scrape_man_pages.py scrape linux_commands.json
  → Creates: commands_database.json


STEP 2: RENAME DATABASES
-------------------------

PowerShell:
  ren powershell_scraped_database.py powershell_database.py

CMD:
  ren cmd_scraped_database.py cmd_database.py

Linux:
  json_to_cmdhelp.py man_commands_complete_with_examples.json command_database.py


STEP 3: USE CMDHELP
--------------------

  python cmdhelp dir
  python cmdhelp Get-Process
  python cmdhelp ls
  python cmdhelp list


SCRAPERS INCLUDED
-----------------

scrape_powershell.py
  • Alternative Python version
  • Same functionality

scrape_cmd.py
  • Scrapes CMD commands using help
  • Creates: cmd_scraped_database.py
  • 30-50 commands
  • Time: 1-2 minutes

scrape_man_pages.py
  • Scrapes Linux man pages
  • Creates JSON output
  • 1000-3000+ commands
  • Time: 5-10 minutes


REQUIREMENTS
------------

• Python 3.6+
• No external dependencies
• Windows (for PowerShell/CMD scrapers)
• Linux with man pages (for Linux scraper)
