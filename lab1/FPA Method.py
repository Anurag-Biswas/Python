def calculate_ufp(inputs, files, queries, interfaces, outputs):
    # Ratios for each type of FP
    ratios = {
        'i/p': [1, 6, 3],
        'file': [1, 2, 2],
        'query': [1, 1, 1],  # All queries are average complexity
        'i/f': [0, 0, 1],   # All interfaces are complex
        'o/p': [2, 2, 1]
    }

    # Weight factors for FP complexity
    weights = {
        'simple': 0.5,
        'average': 1.0,
        'complex': 1.5
    }

    # Calculate UFP for each type
    ufp = 0

    # Calculate UFP for i/p (inputs)
    ufp_ip = sum([ratios['i/p'][i] / 10 * inputs for i in range(3)])
    ufp += ufp_ip

    # Calculate UFP for file (files)
    ufp_file = sum([ratios['file'][i] / 5 * files for i in range(3)])
    ufp += ufp_file

    # UFP for query (queries)
    ufp_query = ratios['query'][1] * queries  # All queries are average complexity
    ufp += ufp_query

    # UFP for i/f (interfaces)
    ufp_if = ratios['i/f'][2] * interfaces  # All interfaces are complex
    ufp += ufp_if

    # Calculate UFP for o/p (outputs)
    ufp_op = sum([ratios['o/p'][i] / 5 * outputs for i in range(3)])
    ufp += ufp_op

    return ufp

def calculate_tdi_and_vaf(reliability, complexity):
    # Calculate TDI (Technical Difficulty Indicator)
    tdi = 0.6 + (0.01 * (reliability + complexity))
    
    # Calculate VAF (Value Adjustment Factor)
    vaf = 0.65 + (0.01 * complexity)
    
    return tdi, vaf

def calculate_afp(ufp, vaf):
    # Calculate Adjusted Function Points (AFP)
    afp = ufp * vaf
    return afp

# Given inputs
inputs = 60
files = 25
queries = 35
interfaces = 20
outputs = 25

reliability = 65  # 65%
complexity = 75   # 0.75

# Calculate UFP
ufp = calculate_ufp(inputs, files, queries, interfaces, outputs)
print(f"Unadjusted Function Points (UFP): {ufp}")

# Calculate TDI and VAF
tdi, vaf = calculate_tdi_and_vaf(reliability, complexity)
print(f"Technical Difficulty Indicator (TDI): {tdi}")
print(f"Value Adjustment Factor (VAF): {vaf}")

# Calculate AFP
afp = calculate_afp(ufp, vaf)
print(f"Adjusted Function Points (AFP): {afp}")
