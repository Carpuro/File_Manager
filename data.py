": "pdf"
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






