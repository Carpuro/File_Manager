import os # This module provides functions for interacting with the operating system
import re # This module provides regular expression matching operations similar to those found in Perl
import glob # This module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell
import json # This module provides an easy way to encode and decode data in JSON format
import shutil # This module provides a higher-level interface for file operations, such as copying and moving files
import zipfile # This module provides tools to create, read, write, append, and list a ZIP file
import logging # This module provides a flexible framework for emitting log messages from Python programs
import colorlog # This module provides a way to add color to log messages in the console output
import traceback # This module provides a standard interface to extract, format, and print stack traces of Python programs
import pdfplumber # This module is used to extract text and metadata from PDF files
import data as dt # This module contains data structures and constants used in the script
import pandas as pd # This module provides data structures and data analysis tools, particularly for working with tabular data     
from datetime import datetime # This module provides classes for manipulating dates and times

# === Helping Functions ===

# Function that sets the log configuration
def setup_log():
    formatter = colorlog.ColoredFormatter(
        '%(asctime)s - %(log_color)s%(levelname)-8s%(reset)s - %(message)s',  # Format with colors
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    )

    # Set up the stream handler with the colored formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Set up the logger
    logging.basicConfig(
        level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, etc.)
        handlers=[console_handler]  # Only the console handler
    )

    logger = logging.getLogger()
    return logger

# Function to trim the filename to a maximum length
def trim_filename(filename: str, max_len: int = 85) -> str:
    """
    Shortens the base name (without extension) to max_len characters  
    to avoid path-length issues.

    Parameters
    ----------
    filename : str
        Full file name including extension.
    max_len : int, optional
        Maximum length for the base name (default is 95).    

    Returns
    -------
    str
        Trimmed file name, extension preserved.
    """
    base, ext = os.path.splitext(filename)
    if len(base) > max_len:
        base = base[:max_len] 
    return f"{base}{ext}"


# ================================================================================
# Functions to extract specific metadata from files 
# ================================================================================

 
def extract_lia_country(text: str, patterns: list, filename: str = "") -> str:
    """
    1) Try to capture the country right after any anchor in `patterns`
       (e.g. 'LOCAL IMPLEMENTATION AGREEMENT –').
    2) If not found, fallback to filename tokens.
    Returns canonical country name or "".
    """

    # ---------------- helper: alias → canonical ------------------
    def canon(token: str) -> str:
        tok_upper = token.strip().upper()
        for canon_name, aliases in dt.countries.items():
            if tok_upper in (alias.upper() for alias in aliases):
                return canon_name
        return ""

    # ---------------- (1) PDF text lookup -----------------------
    country_regex = r"([A-Za-z]{2,}(?:\s+[A-Za-z]{2,})*)"
    for anchor in patterns:
        rx = rf"{re.escape(anchor)}\s*[:\-–]?\s*{country_regex}"
        m = re.search(rx, text, flags=re.IGNORECASE)
        if m:
            raw = re.sub(r"[.,;:\s]+$", "", m.group(1).strip())
            if (c := canon(raw)):
                return c

    # ---------------- (2) filename fallback ---------------------
    base = os.path.splitext(filename)[0]
    for token in re.split(r"[ _\-]", base)[::-1]:          # de atrás hacia delante
        if (c := canon(token)):
            return c
    # ejemplo final “..._United_Kingdom”
    tail = re.search(r"([A-Z][a-z]+(?:[_\-\s][A-Z][a-z]+)*)$", base)
    if tail and (c := canon(tail.group(1).replace("_", " ").replace("-", " "))):
        return c

    return ""

def extract_trailing_number(text: str, trailing_patterns:list)-> str:
    for pattern in trailing_patterns:
        match = re.search(re.escape(pattern) + r"\s*(\S+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return ""

def extract_date(text: str, date_patterns: list) -> str:
    """
    Search for the first date after any anchor in `date_patterns` (or
    anywhere in the text) and return it normalized as MM/DD/YYYY.
    Returns "" when parsing fails.
    """

    # 1) ----------------------------------------------------------------
    # All regex formats we accept
    month_name = r"(January|February|March|April|May|June|July|August|" \
                 r"September|October|November|December)\s+\d{1,2},\s+\d{4}"
    ordinal_dm = r"\d{1,2}(?:st|nd|rd|th)?\s+" \
                 r"(January|February|March|April|May|June|July|August|" \
                 r"September|October|November|December)\s+\d{4}"
    numeric    = r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}"
    iso        = r"\d{4}-\d{2}-\d{2}"
    dots_eu    = r"\d{1,2}\.\d{1,2}\.\d{2,4}"
    abbr_mdy   = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+\d{4}"
    abbr_dmy   = r"\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}"

    date_union = f"({month_name}|{ordinal_dm}|{abbr_mdy}|{abbr_dmy}|{numeric}|{iso}|{dots_eu})"

    # 2) ----------------------------------------------------------------
    # Candidate date string, empty by default
    raw_date = ""

    # 2a) Anchored search
    for anchor in date_patterns:
        anchor_regex = rf"{re.escape(anchor)}\s*[:\-]?\s*{date_union}"
        m = re.search(anchor_regex, text, flags=re.IGNORECASE)
        if m:
            raw_date = m.group(m.lastindex)
            break

    # 2b) Generic search
    if not raw_date:
        m = re.search(date_union, text, flags=re.IGNORECASE)
        if m:
            raw_date = m.group(0)

    if not raw_date:
        return ""  # Nothing found

    # 3) ----------------------------------------------------------------
    # Normalization to MM/DD/YYYY
    raw_date = raw_date.strip()
    raw_date = re.sub(r"(\d{1,2})(st|nd|rd|th)", r"\1", raw_date, flags=re.I)

    patterns = [
        "%B %d, %Y",     # January 5, 2024
        "%d %B %Y",      # 5 January 2024
        "%b %d, %Y",     # Jan 5, 2024
        "%d %b %Y",      # 5 Jan 2024
        "%m/%d/%Y",      # 05/01/2024
        "%m/%d/%y",      # 05/01/24
        "%d-%m-%Y",      # 5-1-2024
        "%d-%m-%y",      # 5-1-24
        "%Y-%m-%d",      # 2024-01-05
        "%d.%m.%Y",      # 5.1.2024
        "%d.%m.%y",      # 5.1.24
    ]

    for fmt in patterns:
        try:
            dt = datetime.strptime(raw_date, fmt)
            return dt.strftime("%m/%d/%Y")
        except ValueError:
            continue

    # Could not parse
    return ""

 
# Initialize the logger
logger = setup_log()

# ================================================================================
# === STEP 1 : ZIP Files Extraction & and Creation of Contract Id Folders ========
# ================================================================================

def step_1(source_path, dest_path):
    try:
        logger.info(f"🔹🔹 Step 1.1: Validating Source and Destination Paths...")
        if not validate_paths(source_path, dest_path):
            logger.critical("❌ Step 1.1 Failed: Invalid source or destination path.")
            return {}

        logger.debug(f"🔹✅ Step 1.1 Completed: Validated the Paths.")

        try:
            logger.info(f"🔹🔹 Step 1.2: Processing folders and extracting ZIP files...")
            zip_summary = process_folder(source_path, dest_path, source_path)

            if not zip_summary:
                logger.critical("❌ Step 1.2 Failed: No ZIP files found to extract.")
                return {}

            logger.debug(f"🔹✅ Step 1.2 Completed: Processed all folders and extracted ZIP files.")

            return zip_summary

        except Exception as e:
            logger.error(f"🔹❌ Step 1.2 Error during folder processing: {e}")
            logger.error(traceback.format_exc())
            return {}

    except Exception as e:
        logger.error(f"❌ Step 1.0 Error during main folder process: {e}")
        logger.error(traceback.format_exc())
        return {}

# --------------------------------------------------------------------------------
# --- Step 1.1: Validate the source and destination paths ------------------------
# --------------------------------------------------------------------------------
def validate_paths(source_path, dest_path):
    try:
        if not os.path.isdir(source_path):
            logger.error(f"🔹❌ Source folder not found: {source_path}")
            return False
        logger.info(f"🔹🔹 Source folder is valid: {source_path}")

        if not os.path.isdir(dest_path):
            logger.error(f"🔹❌ Destination folder not found: {dest_path}")
            return False
        logger.info(f"🔹🔹 Destination folder is valid: {dest_path}")

        return True
    except Exception as e:
        logger.error(f"🔹❌ Error validating paths: {e}")
        logger.error(traceback.format_exc())
        return False
# --------------------------------------------------------------------------------
# --- Step 1.2: Recursive function to traverse folders and extract ZIP files -----
# --------------------------------------------------------------------------------
def process_folder(current_folder, dest_base, source_base):
    try:
        relative_path = os.path.relpath(current_folder, source_base)
        new_dest = os.path.join(dest_base, relative_path)
        os.makedirs(new_dest, exist_ok=True)

        zip_summary = {}  # ✅ Dictionary to store {Contract ID: number of files}

        # Process files
        for file_name in os.listdir(current_folder):
            file_path = os.path.join(current_folder, file_name)

            if os.path.isfile(file_path) and file_name.lower().endswith('.zip'):
                zip_folder_name = os.path.splitext(file_name)[0]
                zip_folder = os.path.join(new_dest, zip_folder_name)

                if os.path.exists(zip_folder):
                    logger.warning(f"🔹🔹 Skipping ZIP (already extracted): {file_name}")
                else:
                    os.makedirs(zip_folder, exist_ok=True)
                    file_count = extract_zip_files(file_path, zip_folder)

                    if file_count != -1:
                        logger.info(f"🔹📦 Extracted {file_count} files from {os.path.basename(file_name)}")
                        zip_summary[zip_folder_name] = file_count

        # Process subfolders recursively
        for sub_folder in os.listdir(current_folder):
            sub_folder_path = os.path.join(current_folder, sub_folder)
            if os.path.isdir(sub_folder_path):
                sub_summary = process_folder(sub_folder_path, dest_base, source_base)
                zip_summary.update(sub_summary)

        return zip_summary  # ✅ Return the summary of extracted ZIP files
    except Exception as e:
        logger.error(f"🔹❌ Error processing folder {current_folder}: {e}")
        logger.error(traceback.format_exc())
        return {}

# --------------------------------------------------------------------------------
# --- Step 1.2.1: Extract ZIP files and handle nested ZIPs -----------------------
# --------------------------------------------------------------------------------
def extract_zip_files(zip_path, extract_to):
    file_count = 0
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            if not zip_ref.namelist():
                logger.warning(f"🔹⚠️ ZIP is empty: {os.path.basename(zip_path)}")
                return file_count

            temp_extract_path = os.path.join(extract_to, "Temporal Folder")
            os.makedirs(temp_extract_path, exist_ok=True)

            zip_ref.extractall(temp_extract_path)

            # Move extracted files
            for root, _, files in os.walk(temp_extract_path):
                for file in files:
                    file_count += 1
                    src_file = os.path.join(root, file)
                    dest_file = os.path.join(extract_to, file)

                    try:
                        shutil.move(src_file, dest_file)
                    except FileExistsError:
                        os.remove(dest_file)
                        shutil.move(src_file, dest_file)

                    if file.lower().endswith('.zip'):
                        file_count += extract_zip_files(dest_file, extract_to)

            shutil.rmtree(temp_extract_path, ignore_errors=True)

    except zipfile.BadZipFile:
        logger.error(f"🔹❌ Bad ZIP file: {zip_path}")
        return -1
    except Exception as e:
        logger.error(f"🔹❌ Error extracting ZIP {zip_path}: {e}")
        logger.error(traceback.format_exc())
        return -1

    return file_count

# ================================================================================
# === STEP 2 : Classify files, build summaries and trim long names ===============
# ================================================================================

def step_2(extract_to: str, zip_folder_name: str):
    """
    1. Create category folders
    2. Initial PDF / other split
    3. Classify files (PDF text + filename heuristics)
    4. Build file_resume and contract_resume
    5. Trim long filenames
    6. Export CSV summaries
    """
    try:
        # ------------------------------------------------------- 1
        create_category_folders(extract_to, zip_folder_name)

        # ------------------------------------------------------- 2
        initial_preclassification(extract_to, zip_folder_name)

        # ------------------------------------------------------- 3
        file_resume = pd.DataFrame(columns=[
            "Category Folder",
            "Contract Id",
            "Supplier Name",
            "File Category",
            "Amendment Number",
            "Extracted Date",
            "File Extension",
            "File Original Name",
        ])
        contract_resume = pd.DataFrame(columns=["Contract_id", "Carlos Comments"])

        # ------------------------------------------------------- 4
        logger.info(f"📁 File classification starting for {zip_folder_name}")
        categorized_files = (
            
            assign_file_category_pdf(extract_to, zip_folder_name) +
            assign_file_category_filename(extract_to, zip_folder_name)
        )

 
        seen_keys = set()

        for info in categorized_files:
            file_key = info["file"]
            if file_key in seen_keys:        # avoid duplicates
                continue
            seen_keys.add(file_key)

            file_resume.loc[len(file_resume)] = {
                "Category Folder" : info.get("category", ""),
                "Contract Id"     : zip_folder_name,
                "Supplier Name"   : info.get("supplier", ""),
                "File Category"   : info.get("subcategory", ""),
                "Amendment Number": info.get("amendment_number", ""),
                "Extracted Date"  : info.get("date", ""),
                "File Extension"  : os.path.splitext(file_key)[-1].lower(),
                "File Original Name": file_key,
            }
 

        # ------------------------------------------------------- 5
        required_groups = {
            "BSA": {"BSA", "MSA","SSA", "POTAC", "SaaS","SLA","MCA","GBA", "LIA"}, 
        } 
        present = {cat.strip().upper() for cat in file_resume["File Category"]} 
        missing_docs = []
        for canon_name, aliases in required_groups.items():
            if not {a.upper() for a in aliases} & present:               
                missing_docs.append(canon_name) 
        if missing_docs:
            contract_resume.loc[len(contract_resume)] = {
                "Contract_id": zip_folder_name,
                "Carlos Comments": "Missing " + " ".join(sorted(missing_docs)),
            } 

        # ------------------------------------------------------- 6
        file_resume = trim_long_filenames(
            file_resume=file_resume,
            extract_to=extract_to,
            zip_folder_name=zip_folder_name,
            logger=logger,
        )

        # ------------------------------------------------------- 7
        output_folder = os.path.join(extract_to, zip_folder_name)
        file_resume.to_csv(os.path.join(output_folder, "file_resume.csv"), index=False)
        contract_resume.to_csv(os.path.join(output_folder, "contract_resume.csv"), index=False)
        return file_resume, contract_resume

    except Exception as e:
        logger.error(f"❌ Error during Step 2: {e}")
        logger.error(traceback.format_exc())
        return pd.DataFrame(), pd.DataFrame()


# --------------------------------------------------------------------------------
# --- Step: 2.1: Create category folders for each CW folder ----------------------
# --------------------------------------------------------------------------------
def create_category_folders(extract_to: str, zip_folder_name: str):
    """
    Build a folder for each category defined in dt.folder_categories
    plus a default 'Uncategorized' folder.
    """
    try:
        zip_folder_path = os.path.join(extract_to, zip_folder_name)
        if not os.path.exists(zip_folder_path):
            logger.error(f"ZIP folder path not found: {zip_folder_path}")
            return

        # Create main category folders
        for category in dt.folder_categories:
            category_path = os.path.join(zip_folder_path, category)
            os.makedirs(category_path, exist_ok=True)

        # Create 'Uncategorized'
        os.makedirs(os.path.join(zip_folder_path, "Uncategorized"), exist_ok=True)

    except Exception as e:
        logger.error(f"Error creating category folders: {e}")
        logger.error(traceback.format_exc())


# --------------------------------------------------------------------------------
# --- Step: 2.1.1  Initial pre-classification (PDF to Supporting, others to Uncategorized)
# --------------------------------------------------------------------------------
def initial_preclassification(extract_to: str, zip_folder_name: str):
    """
    Move PDFs and MSGs to 'Supporting Documents' and everything else
    to 'Uncategorized'. Keeps original filenames intact.
    """
    try:
        zip_folder_path = os.path.join(extract_to, zip_folder_name)
        if not os.path.exists(zip_folder_path):
            logger.error(f"ZIP folder path not found: {zip_folder_path}")
            return

        supporting = os.path.join(zip_folder_path, "Supporting Documents")
        uncategorized = os.path.join(zip_folder_path, "Uncategorized")
        os.makedirs(supporting, exist_ok=True)
        os.makedirs(uncategorized, exist_ok=True)

        for file in os.listdir(zip_folder_path):
            file_path = os.path.join(zip_folder_path, file)
            if not os.path.isfile(file_path):
                continue

            ext = os.path.splitext(file)[-1].lower()
            dest = supporting if ext in (".pdf", ".msg") else uncategorized

            try:
                shutil.move(file_path, os.path.join(dest, file))
            except Exception as e:
                logger.error(f"Error moving '{file}' → '{dest}': {e}")

    except Exception as e:
        logger.error(f"❌ Error during initial pre-classification: {e}")
        logger.error(traceback.format_exc())


# # --------------------------------------------------------------------------------
# --- Step: 2.2  Classification using PDF text -------------------------------------
# # --------------------------------------------------------------------------------
def assign_file_category_pdf(extract_to: str, zip_folder_name: str) -> list:
    """
    Read PDF text with pdfplumber, classify according to dt.folder_categories,
    extract any anchor-defined date, and trailing number (for *any* category
    that defines 'trailing_number_extraction').
    Returns a list of metadata dicts.
    """
    categorized: list = []

    try:
        # Silence noisy loggers
        logging.getLogger("pdfplumber").setLevel(logging.WARNING)
        logging.getLogger("pdfminer").setLevel(logging.WARNING)

        supporting_folder = os.path.join(extract_to,
                                         zip_folder_name,
                                         "Supporting Documents")
        if not os.path.exists(supporting_folder):
            logger.warning(f"Supporting Documents folder not found: {supporting_folder}")
            return []

        # ---------- Iterate every PDF in Supporting Documents -------
        for file in os.listdir(supporting_folder):
            if not file.lower().endswith(".pdf"):
                continue

            file_path = os.path.join(supporting_folder, file)
            try:
                with pdfplumber.open(file_path) as pdf:
                    full_text = " ".join(page.extract_text() or ""
                                         for page in pdf.pages)
            except Exception as e:
                logger.warning(f"Could not open PDF '{file}': {e}")
                continue

            # ---------- Run rules against each category --------------
            matched = False
            for folder_category, subcats in dt.folder_categories.items():
                for file_category, rules in subcats.items():
                    terms          = rules.get("file_category_extraction", [])
                    date_terms     = rules.get("date_extraction", [])
                    trailing_terms = rules.get("trailing_number_extraction", [])
                    country_patterns = rules.get("country_extraction", [])

                    # Check if any keyword matches the PDF text
                    if any(term.lower() in full_text.lower() for term in terms):
                        # --- Date extraction -----------------------------
                        extracted_date = extract_date(full_text, date_terms)

                        # --- Trailing number extraction ---
                        trailing_number = ""

                        if file_category == "LIA":
                            trailing_number = extract_lia_country(full_text, patterns=country_patterns, filename=file)
                        else: 
                            trailing_number = extract_trailing_number(full_text, trailing_terms)
 
                        # --- Move PDF to final category folder ---
                        dest_dir = os.path.join(extract_to, zip_folder_name,
                                                folder_category)
                        os.makedirs(dest_dir, exist_ok=True)
                        shutil.move(file_path, os.path.join(dest_dir, file))
                        logger.debug(f"Moved '{file}' → '{folder_category}' [{file_category}]")

                        # --- Append metadata ---
                        categorized.append({
                            "file"            : file,
                            "category"        : folder_category,
                            "subcategory"     : file_category,
                            "date"            : extracted_date or "", 
                            "amendment_number": trailing_number.strip()
                        })
 
                        matched = True
                        break  # exit subcat loop
                if matched:
                    break      # exit folder_category loop

    except Exception as e:
        logger.error(f"Error in assign_file_category_pdf: {e}")
        logger.error(traceback.format_exc())

    return categorized


# # --------------------------------------------------------------------------------
# --- Step: 2.3  Classification using filename heuristics --------------------------
# # --------------------------------------------------------------------------------
def assign_file_category_filename(extract_to: str,
                                  zip_folder_name: str) -> list:
    """
    Classify files by filename keywords/extension, move them to the final
    folder, extract dates, and fill 'amendment_number' either with:
      • the country (for LIA files)      – via extract_lia_country
      • the trailing number (other docs) – via extract_trailing_number
    Returns a list of metadata dictionaries.
    """
    categorized: list = []

    try:
        base_folder = os.path.join(extract_to, zip_folder_name)

        # Search only in provisional Supporting / Uncategorized
        for provisional in ["Supporting Documents", "Uncategorized"]:
            prov_path = os.path.join(base_folder, provisional)
            if not os.path.exists(prov_path):
                continue

            for file in os.listdir(prov_path):
                file_path = os.path.join(prov_path, file)

                # --- 1) Detect folder & file category -------------------
                folder_category = file_category = None
                file_lower      = file.lower()
                file_ext        = file.split(".")[-1].lower() if "." in file else ""

                trailing_terms  = []
                country_terms   = []      # anchors for LIA (may remain empty)

                for cat, subcats in dt.folder_categories.items():
                    for subcat, rules in subcats.items():
                        if file_ext == rules.get("extension", "") and any(
                            kw in file_lower for kw in rules["keywords"]
                        ):
                            folder_category, file_category = cat, subcat
                            trailing_terms = rules.get("trailing_number_extraction", [])
                            country_terms  = rules.get("country_extraction", [])
                            break
                    if folder_category:
                        break

                # --- 2) Fallback rules ---------------------------------
                if not folder_category and file_ext in ("pdf", "msg"):
                    folder_category, file_category = "Supporting Documents", "Supporting Document"
                    trailing_terms, country_terms = [], []
                if not folder_category:
                    folder_category, file_category = "Uncategorized", "Uncategorized"
                    trailing_terms, country_terms = [], []

                # --- 3) Extract metadata --------------------------------
                file_date   = extract_date(file, [])   # date in filename
                trailing_no = ""

                if file_category == "LIA":
                    trailing_no = extract_lia_country(
                        text="",                        # no PDF text here
                        patterns=country_terms,
                        filename=file
                    )
                elif trailing_terms:
                    trailing_no = extract_trailing_number(file, trailing_terms)

                # --- 4) Move file to final folder -----------------------
                dest_dir = os.path.join(base_folder, folder_category)
                os.makedirs(dest_dir, exist_ok=True)
                try:
                    shutil.move(file_path, os.path.join(dest_dir, file))
                    logger.debug(f"Moved '{file}' → '{folder_category}' [{file_category}]")
                except Exception as move_err:
                    logger.error(f"Error moving '{file}': {move_err}")

                # --- 5) Append metadata ---------------------------------
                categorized.append({
                    "file"            : file,
                    "category"        : folder_category,
                    "subcategory"     : file_category,
                    "date"            : file_date or "",
                    "amendment_number": trailing_no.strip()
                })

        logger.info(f"✅ File classification completed for {zip_folder_name}")
        logger.debug(f"Categorized {len(categorized)} files for {zip_folder_name} contract workspace.")

    except Exception as e:
        logger.error(f"Error during filename classification for {zip_folder_name}: {e}")
        logger.error(traceback.format_exc())

    return categorized

# # --------------------------------------------------------------------------------
# --- Step: 2.4  Trim long filenames AFTER classification --------------------------
# # --------------------------------------------------------------------------------
def trim_long_filenames(
    file_resume: pd.DataFrame,
    extract_to: str,
    zip_folder_name: str,
    logger: logging.Logger,
    max_len: int = 85,
) -> pd.DataFrame:
    """
    Shorten filenames (excluding extension) to <= `max_len` characters
    once files are in their final folders, renaming on disk and updating
    the DataFrame so CSV export is consistent.
    """
    for idx, row in file_resume.iterrows():
        original = row["File Original Name"]
        trimmed = trim_filename(original, max_len=max_len)

        if trimmed == original:
            continue  # no change needed

        category = row["Category Folder"]
        base_dir = os.path.join(extract_to, zip_folder_name, category)
        old_path = os.path.join(base_dir, original)
        new_path = os.path.join(base_dir, trimmed)

        try:
            if not os.path.exists(old_path):
                logger.warning(f"File not found: {old_path}")
                continue

            # Handle collision if trimmed name already exists
            if os.path.exists(new_path):
                base, ext = os.path.splitext(trimmed)
                counter = 1
                while True:
                    candidate = f"{base}_{counter}{ext}"
                    candidate_path = os.path.join(base_dir, candidate)
                    if not os.path.exists(candidate_path):
                        new_path, trimmed = candidate_path, candidate
                        break
                    counter += 1
                logger.warning(f"Name collision avoided: '{trimmed}'")

            os.rename(old_path, new_path)
            logger.debug(f"Renamed '{original}' → '{trimmed}'")

            # Update DataFrame
            file_resume.at[idx, "File Original Name"] = trimmed

        except Exception as e:
            logger.error(f"Error trimming '{original}': {e}")

    return file_resume

# ====================================================================
# === STEP 3: Merging all file_resume.csv & contract_resume.csv files=
# ====================================================================

def step_3(dest_path: str):
    try:
        logger.info("🔹📎 Step 3: Merging all file_resume.csv and contract_resume.csv files…")

        # 1) Collect every individual CSV -----------------------------------
        file_csvs     = glob.glob(os.path.join(dest_path, "**/file_resume.csv"),     recursive=True)
        contract_csvs = glob.glob(os.path.join(dest_path, "**/contract_resume.csv"), recursive=True)

        # 2) Merge into global DataFrames -----------------------------------
        all_files     = pd.concat([pd.read_csv(f) for f in file_csvs],     ignore_index=True) if file_csvs else pd.DataFrame()
        all_contracts = pd.concat([pd.read_csv(f) for f in contract_csvs], ignore_index=True) if contract_csvs else pd.DataFrame()

        all_files.drop_duplicates(inplace=True)
        all_contracts.drop_duplicates(inplace=True)

        out_files = os.path.join(dest_path, "File_Resume.csv")
        out_conts = os.path.join(dest_path, "Contract_Resume.csv")
        all_files.to_csv(out_files, index=False)
        all_contracts.to_csv(out_conts, index=False)

        logger.info("✅ Global CSVs saved.")
        logger.info(f"📁 File_Resume.csv      → {out_files}")
        logger.info(f"📁 Contract_Resume.csv  → {out_conts}")
        logger.info(f"🧮 Total rows – Files: {len(all_files)} | Contracts: {len(all_contracts)}")

        # 3) Remove empty folders inside each CW ----------------------------
        logger.info("Removing empty folders inside every contract workspace…")

        # Walk each CW folder (first-level subfolders of dest_path)
        for cw in [d for d in os.listdir(dest_path) if os.path.isdir(os.path.join(dest_path, d))]:
            cw_path = os.path.join(dest_path, cw)

            # Walk bottom-up so inner empty dirs are removed before parents
            for root, dirs, _ in os.walk(cw_path, topdown=False):
                for d in dirs:
                    dir_path = os.path.join(root, d)
                    # If directory is empty (no files and no subdirs) → delete
                    if not os.listdir(dir_path):
                        try:
                            os.rmdir(dir_path)
                        except OSError as err:
                            logger.warning(f"Could not remove {dir_path}: {err}")

        logger.info("✅ Empty-folder cleanup finished.")

    except Exception as e:
        logger.error(f"❌ Error during Step 3: {e}")
        logger.error(traceback.format_exc())