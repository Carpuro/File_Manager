# Folder Paths

source_path = r'C:\Example\Source\Folder'
output_path = r'C:\Example\Outputh\Folder'
dest_path   = r'C:\Example\Destination\Folder'

# Folder Category
# This is the dictionary that contains the folder categories and their respective keywords, extensions, and other attributes.
# The keys are the folder names, and the values are dictionaries that contain the keywords, extensions, and other attributes for each folder.
# The keywords are used to identify the files that belong to that folder, and the extensions are used to filter the files based on their file type.

folder_categories = {
    "Contract Amendments": { # This is the folder for Contract Amendments and related documents.
        "Contract Amendment": {
            "keywords": ["amend", "amendment", "amending", "amd", "modification","mod", "addendum"],
            "extension": "pdf",
            "file_category_extraction": ["AMENDMENT TO AGREEMENT"],
            "trailing_number_extraction" : ["Amendment No.: "],
            "date_extraction": ["Effective Date of Amendment: ", "The effective date of this Amendment is "]
        }
    },
    "Base Service Agreement": { # This is the folder for Base Service Agreements and related documents.
        "BSA": { # This is the file configuration for Base Service Agreements (BSA) and related documents.
            "keywords": ["bsa","pfa","jcdpa","base services", "base agreement", "base services agreement","base service agreement",
                        "base services and consulting agreement", "base services agreement and consulting agreement",
                        "professional services agreement", "base services and consulting agreement"],
            "extension": "pdf",
            "file_category_extraction": ["Base Services and Consulting Agreement", "“Limited Use” Base Service", 
                                        "Limited Use Base Services Agreement","Professional Services Agreement",
                                        "JOINT CONTROLLER DATA PROCESSING AGREEMENT"],
            "date_extraction": ["This Base Services and Consulting Addgreement (\"Agreement\") is made and entered into on "]
        },       
        "MSA": { # This is the file configuration for Master Service Agreements (MSA) and related documents.
            "keywords": ["msa","mslsa","mssa","msps", "master", "master service agreement", "master services agreement", "master consolidated services agreement"],
            "extension": "pdf",
            "file_category_extraction": ["MASTER SERVICES AGREEMENT","MASTER STANDARD SERVICES AGREEMENT", 
                                        "MASTER CONSOLIDATED SERVICES AGREEMENT","MASTER SUBSCRIPTION SERVICES AGREEMENT"
                                        "MASTER SUBSCRIPTION LICENCE AND SERVICES AGREEMENT"],
            "date_extraction": ["This Master Services Agreement (\"Agreement\") is made and entered into on "]
        },
        "SSA": { # This is the file configuration for Standard Service Agreements (SSA) and related documents.
            "keywords": ["ssa", "standard service agreement", "standard agreement"],
            "extension": "pdf",
            "file_category_extraction": ["STANDARD SERVICES AGREEMENT"],
            "date_extraction": ["This Standard Services Agreement (\"Agreement\") is made and entered into on "]
        },
        "POTAC": { # This is the file configuration for Purchase Order Terms and Conditions (POTAC) and related documents.  
            "keywords": ["potac", "purchase order terms and conditions", "purchase order terms", "purchase order agreement"],
            "extension": "pdf",
            "file_category_extraction": ["PURCHASE ORDER TERMS AND CONDITIONS", "PURCHASE ORDER AGREEMENT"],
            "date_extraction" :["This Standalone (this “Standalone”) is made and entered into on "]
        }, 
        "LIA": { # This is the file configuration for Local Implementation Agreements (LIA) and related documents.
            "keywords": ["LIA", "limited", "local","lia", "implementation", "local implementation agreement"],
            "extension": "pdf",
            "country_extraction": ["LOCAL IMPLEMENTATION AGREEMENT – ", "LOCAL IMPLEMENTATION AGREEMENT"],
            "file_category_extraction": ["LOCAL IMPLEMENTATION AGREEMENT"],
            "date_extraction" :["The term of this LIA shall commence on "]
        },  
        "SaaS": { # This is the file configuration for Software as a Service (SaaS) agreements and related documents.
            "keywords": ["saas", "software as a service", "software as a service agreement"],
            "extension": "pdf",
            "file_category_extraction": ["SOFTWARE AS A SERVICE AGREEMENT"],
            "date_extraction" :["This Software as a Service Agreement (\"Agreement\") is made and entered into on "]
        },
        "SLA": { # This is the file configuration for Software License Agreements (SLA) and related documents.
            "keywords": ["isla","sla", "internal software license agreement", "internal software","software license agreement"],
            "extension": "pdf",
            "file_category_extraction": ["INTERNAL SOFTWARE LICENSE AGREEMENT","SOFTWARE LICENSE AGREEMENT"],
            "date_extraction": ["Software License Agreement (\"Agreement\") is made and entered into on "]
        },
        "MCA": { # This is the file configuration for Master Consulting Agreements (MCA) and related documents.
            "keywords": ["mca","master consulting"],
            "extension": "pdf",
            "file_category_extraction": ["MASTER CONSULTING AGREEMENT"],
            "date_extraction": ["This Software License Agreement (\"Agreement\") is made and entered into on "]
        },
        "GBA": { # This is the file configuration for Global Procurement Agreements (GBA) and related documents.
            "keywords": ["gba","global procurement agreement", "global procurement"],
            "extension": "pdf",
            "file_category_extraction": ["GLOBAL PROCUREMENT AGREEMENT","GLOBAL PROCUREMENT MASTER TERMS AGREEMENT"],
            "date_extraction": ["This Global Procurement Agreement (\"Agreement\") is made and entered into on "]
        }            
    },
    "Contract Summary": {
        "CSS": { # This is the file configuration for Contract Summary Sheets and related documents.
            "keywords": ["contract summary", "contract_summary", "exec summary", "executive", 
                        "overview", "snapshot", "css","agreement summary" "contract summary sheet", "brief", "synopsis"],
            "extension": "pdf"
        }
    },
    "Supporting Documents": {
        "Extension Letter": { # This is the file configuration for Extension Letters and related documents.
            "keywords": ["extension", "continuation", "renew", "renewal"],
            "extension": "pdf",
            "file_category_extraction": ["This letter serves as written notice of our election to renew"],
            "date_extraction" :["through"]
        },
        "Risk Memo": { # This is the file configuration for Risk Memos and related documents.
            "keywords": ["risk", "risk memo"], 
            "extension": "pdf"
        },
        "Payment Approval": { # This is the file configuration for Payment Approval documents and related files.
            "keywords": ["payment", "approval"],
            "extension": "pdf"
        },
        "SOW": { # This is the file configuration for Statements of Work (SOW) and related documents.
            "keywords": ["sow", "statement of work"],
            "extension": "pdf"
        },
        "COC": { # This is the file configuration for Certificates of Completion (COC) and related documents.
            "keywords": ["certificate", "certificate of completion"],
            "extension": "pdf"
        },
        "DnB": { # This is the file configuration for Dun & Bradstreet (DNB) reports and related documents.
            "keywords": ["dnb", "dun & bradstreet", "dun and bradstreet", "d_n_b", "dunbradstreet"],
            "extension": "pdf"
        },
        "CDA": { # This is the file configuration for Confidential Disclosure Agreements (CDA) and related documents.
            "keywords": ["cda", "confidential disclosure agreement", "confidentiality agreement", "nda", "non-disclosure agreement"],
            "extension": "pdf"
        },
        "Supporting document": { # This is the file configuration for general supporting documents and related files.
            "keywords": ["any"],
            "extension": ["pdf","msg"]
        }
    },
    "Uncategorized": {

        "Uncategorized": {
            "keywords": ["any"],
            "extension": ["doc", "docx", "txt", "xls", "xlsx"]
        }
    }
}

# Country Codes
# This dictionary contains country names as keys and a set of identifiers (country codes, abbreviations
# and names) as values. It is used to identify and categorize files based on the country they are associated with.
# The identifiers include ISO country codes, abbreviations, and common names in English and Spanish.

countries = {
    # ---------- A ----------
    "Afghanistan": {"AF", "AFG", "Afghanistan"},
    "Albania": {"AL", "ALB", "Albania", "Albania"},
    "Algeria": {"DZ", "DZA", "Algeria", "Argelia"},
    "Argentina": {"AR", "ARG", "Argentina", "Arg"},
    "Australia": {"AU", "AUS", "Australia", "Commonwealth of Australia"},
    "Austria": {"AT", "AUT", "Austria"},

    # ---------- B ----------
    "Bahamas": {"BS", "BHS", "Bahamas", "The Bahamas"},
    "Bangladesh": {"BD", "BGD", "Bangladesh"},
    "Belgium": {"BE", "BEL", "Belgium", "Bélgica"},
    "Belize": {"BZ", "BLZ", "Belize"},
    "Bolivia": {"BO", "BOL", "Bolivia", "Bolivia (Plurinational State of)"},
    "Brazil": {"BR", "BRA", "Brazil", "Brasil"},
    "Bulgaria": {"BG", "BGR", "Bulgaria"},

    # ---------- C ----------
    "Cambodia": {"KH", "KHM", "Cambodia", "Camboya"},
    "Cameroon": {"CM", "CMR", "Cameroon", "Camerún"},
    "Canada": {"CA", "CAN", "Canada", "Can"},
    "Chile": {"CL", "CHL", "Chile"},
    "China": {"CN", "CHN", "China", "PRC", "People's Republic of China"},
    "Colombia": {"CO", "COL", "Colombia"},
    "Costa Rica": {"CR", "CRI", "Costa Rica"},
    "Croatia": {"HR", "HRV", "Croatia", "Croacia"},
    "Czech Republic": {"CZ", "CZE", "Czech Republic", "Czechia"},

    # ---------- D ----------
    "Denmark": {"DK", "DNK", "Denmark", "Dinamarca"},
    "Dominican Republic": {"DO", "DOM", "Dominican Republic", "República Dominicana"},

    # ---------- E ----------
    "Ecuador": {"EC", "ECU", "Ecuador"},
    "Egypt": {"EG", "EGY", "Egypt", "Egipto"},
    "El Salvador": {"SV", "SLV", "El Salvador"},
    "Estonia": {"EE", "EST", "Estonia"},
    "Ethiopia": {"ET", "ETH", "Ethiopia", "Etiopía"},

    # ---------- F ----------
    "Finland": {"FI", "FIN", "Finland", "Finlandia"},
    "France": {"FR", "FRA", "France", "Francia"},

    # ---------- G ----------
    "Germany": {"DE", "DEU", "Germany", "Alemania"},
    "Ghana": {"GH", "GHA", "Ghana"},
    "Greece": {"GR", "GRC", "Greece", "Grecia"},
    "Guatemala": {"GT", "GTM", "Guatemala"},
    "Guyana": {"GY", "GUY", "Guyana"},

    # ---------- H ----------
    "Haiti": {"HT", "HTI", "Haiti"},
    "Honduras": {"HN", "HND", "Honduras"},
    "Hungary": {"HU", "HUN", "Hungary", "Hungría"},

    # ---------- I ----------
    "Iceland": {"IS", "ISL", "Iceland"},
    "India": {"IN", "IND", "India", "Bharat"},
    "Indonesia": {"ID", "IDN", "Indonesia"},
    "Iran": {"IR", "IRN", "Iran", "Iran, Islamic Republic of"},
    "Iraq": {"IQ", "IRQ", "Iraq"},
    "Ireland": {"IE", "IRL", "Ireland", "Éire"},
    "Israel": {"IL", "ISR", "Israel"},
    "Italy": {"IT", "ITA", "Italy", "Italia"},

    # ---------- J ----------
    "Jamaica": {"JM", "JAM", "Jamaica"},
    "Japan": {"JP", "JPN", "Japan", "Nippon"},
    "Jordan": {"JO", "JOR", "Jordan"},

    # ---------- K ----------
    "Kazakhstan": {"KZ", "KAZ", "Kazakhstan"},
    "Kenya": {"KE", "KEN", "Kenya"},
    "Korea, South": {"KR", "KOR", "South Korea", "Korea, Republic of", "ROK"},
    "Kuwait": {"KW", "KWT", "Kuwait"},
    "Kyrgyzstan": {"KG", "KGZ", "Kyrgyzstan"},

    # ---------- L ----------
    "Laos": {"LA", "LAO", "Laos", "Lao PDR"},
    "Latvia": {"LV", "LVA", "Latvia"},
    "Lebanon": {"LB", "LBN", "Lebanon", "Líbano"},
    "Libya": {"LY", "LBY", "Libya", "Libia"},
    "Lithuania": {"LT", "LTU", "Lithuania"},
    "Luxembourg": {"LU", "LUX", "Luxembourg"},

    # ---------- M ----------
    "Madagascar": {"MG", "MDG", "Madagascar"},
    "Malaysia": {"MY", "MYS", "Malaysia", "Malasia"},
    "Mexico": {"MX", "MEX", "Mexico", "Estados Unidos Mexicanos", "Mex"},
    "Morocco": {"MA", "MAR", "Morocco", "Marruecos"},
    "Mozambique": {"MZ", "MOZ", "Mozambique"},
    "Myanmar": {"MM", "MMR", "Myanmar", "Burma"},

    # ---------- N ----------
    "Namibia": {"NA", "NAM", "Namibia"},
    "Nepal": {"NP", "NPL", "Nepal"},
    "Netherlands": {"NL", "NLD", "Netherlands", "The Netherlands"},
    "New Zealand": {"NZ", "NZL", "New Zealand"},
    "Nicaragua": {"NI", "NIC", "Nicaragua"},
    "Nigeria": {"NG", "NGA", "Nigeria"},
    "Norway": {"NO", "NOR", "Norway", "Noruega"},

    # ---------- O ----------
    "Oman": {"OM", "OMN", "Oman"},

    # ---------- P ----------
    "Pakistan": {"PK", "PAK", "Pakistan"},
    "Panama": {"PA", "PAN", "Panama"},
    "Paraguay": {"PY", "PRY", "Paraguay"},
    "Peru": {"PE", "PER", "Peru", "Perú"},
    "Philippines": {"PH", "PHL", "Philippines", "Filipinas"},
    "Poland": {"PL", "POL", "Poland", "Polonia"},
    "Portugal": {"PT", "PRT", "Portugal"},

    # ---------- Q ----------
    "Qatar": {"QA", "QAT", "Qatar"},

    # ---------- R ----------
    "Romania": {"RO", "ROU", "Romania", "Rumania"},
    "Russia": {"RU", "RUS", "Russia", "Russian Federation"},
    "Rwanda": {"RW", "RWA", "Rwanda"},

    # ---------- S ----------
    "Saudi Arabia": {"SA", "SAU", "Saudi Arabia", "KSA"},
    "Senegal": {"SN", "SEN", "Senegal"},
    "Serbia": {"RS", "SRB", "Serbia"},
    "Singapore": {"SG", "SGP", "Singapore"},
    "Slovakia": {"SK", "SVK", "Slovakia", "Eslovaquia"},
    "Slovenia": {"SI", "SVN", "Slovenia"},
    "South Africa": {"ZA", "ZAF", "South Africa"},
    "Spain": {"ES", "ESP", "Spain", "España"},
    "Sri Lanka": {"LK", "LKA", "Sri Lanka"},
    "Sweden": {"SE", "SWE", "Sweden", "Suecia"},
    "Switzerland": {"CH", "CHE", "Switzerland", "Suiza"},
    "Syria": {"SY", "SYR", "Syria"},

    # ---------- T ----------
    "Taiwan": {"TW", "TWN", "Taiwan", "Republic of China"},
    "Tanzania": {"TZ", "TZA", "Tanzania"},
    "Thailand": {"TH", "THA", "Thailand", "Tailandia"},
    "Tunisia": {"TN", "TUN", "Tunisia", "Túnez"},
    "Turkey": {"TR", "TUR", "Turkey", "Türkiye"},

    # ---------- U ----------
    "Uganda": {"UG", "UGA", "Uganda"},
    "Ukraine": {"UA", "UKR", "Ukraine"},
    "United Arab Emirates": {"AE", "ARE", "UAE", "United Arab Emirates"},
    "United Kingdom": {"GB", "GBR", "UK", "United Kingdom", "Great Britain"},
    "United States": {"US", "USA", "United States", "United States of America", "EEUU"},

    # ---------- V ----------
    "Venezuela": {"VE", "VEN", "Venezuela", "Bolivarian Republic of Venezuela"},
    "Vietnam": {"VN", "VNM", "Vietnam", "Viet Nam"},

    # ---------- Z ----------
    "Zambia": {"ZM", "ZMB", "Zambia"},
    "Zimbabwe": {"ZW", "ZWE", "Zimbabwe"},
}








