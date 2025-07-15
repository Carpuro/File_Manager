FILE ORGANIZER - AUTOMATIC FILE CATEGORIZATION BOT
--------------------------------------------------

DESCRIPTION:
------------
This Python-based tool automatically classifies, renames, and organizes files from a specified source folder based on their filename patterns, extensions, and predefined keyword mappings. It moves categorized files into structured subfolders and generates a metadata log for tracking purposes.

FEATURES:
---------
- Automatically classifies files (PDF, DOCX, MSG, etc.) based on keywords and file extensions.
- Handles nested ZIP files by extracting and processing their content.
- Generates structured folders dynamically based on detected categories.
- Assigns standardized filenames following the pattern: 
  ContractId_Supplier_FileCategory_Description_YYYY-MM-DD.pdf
- Logs metadata for each processed file into a tracking table.
- Optionally handles long filenames by renaming them before extraction to avoid Windows path length issues.

REQUIREMENTS:
-------------
- Python 3.8+
- Required Libraries:
  - pandas
  - zipfile
  - os
  - shutil
  - datetime

SETUP:
------
1. Update the source and destination folder paths in the script:
   Example:
   source_folder = 'C:\\Your\\Source\\Folder'
   destination_folder = 'C:\\Your\\Destination\\Folder'

2. Adjust the keyword/category mappings in the configuration section of the script to suit your specific use case.

3. Run the script:
   python file_organizer.py

OUTPUT:
-------
- Organized folder structure with categorized files.
- Standardized filenames for easier tracking and reporting.
- Metadata tracking file (CSV or Excel format) containing:
    - Original Filename
    - New Filename
    - Assigned Category
    - Date Processed
    - File Path

DISCLAIMER:
-----------
This tool was developed for personal use and learning purposes. It is a general-purpose file organizer and does not represent proprietary processes from any specific company or organization.

CONTACT:
--------
Developed by Carlos Pulido Rosas
Email: carlos.pulido.rosas@gmail.com 
