import os

'''
  QEMU HTTPS variable:

  By default lib/resource.txt AUTH URI construct is as
  ${AUTH_URI}   https://${OPENBMC_HOST}${AUTH_SUFFIX}
  ${AUTH_SUFFIX} is populated here by default EMPTY else
  the port from the OS environment
'''
def get_port_https():
    # defaulted to empty string
    l_suffix = ''
    try:
        l_https_port = os.getenv('HTTPS_PORT')
        if l_https_port:
           l_suffix = ':' + l_https_port
    except:
        print "Environment variable HTTPS_PORT not set,using default HTTPS port"
    return l_suffix

AUTH_SUFFIX={
    "https_port":[get_port_https()],
}

# Update the ':Port number' to this variable
AUTH_SUFFIX = AUTH_SUFFIX['https_port'][0]

# Here contains a list of valid Properties bases on fru_type after a boot.
INVENTORY_ITEMS={
    "CPU": [
        "Custom Field 1",
        "Custom Field 2",
        "Custom Field 3",
        "Custom Field 4",
        "Custom Field 5",
        "Custom Field 6",
        "Custom Field 7",
        "Custom Field 8",
        "FRU File ID",
        "Manufacturer",
        "Name",
        "Part Number",
        "Serial Number",
        "fault",
        "fru_type",
        "is_fru",
        "present",
        "version",
        ],

    "DIMM": [
        "Asset Tag",
        "Custom Field 1",
        "Custom Field 2",
        "Custom Field 3",
        "Custom Field 4",
        "Custom Field 5",
        "Custom Field 6",
        "Custom Field 7",
        "Custom Field 8",
        "FRU File ID",
        "Manufacturer",
        "Model Number",
        "Name",
        "Serial Number",
        "Version",
        "fault",
        "fru_type",
        "is_fru",
        "present",
        "version",
        ],
    "MEMORY_BUFFER": [
        "Custom Field 1",
        "Custom Field 2",
        "Custom Field 3",
        "Custom Field 4",
        "Custom Field 5",
        "Custom Field 6",
        "Custom Field 7",
        "Custom Field 8",
        "FRU File ID",
        "Manufacturer",
        "Name",
        "Part Number",
        "Serial Number",
        "fault",
        "fru_type",
        "is_fru",
        "present",
        "version",
        ],
    "FAN": [
        "fault",
        "fru_type",
        "is_fru",
        "present",
        "version",
        ],
    "DAUGHTER_CARD": [
        "Custom Field 1",
        "Custom Field 2",
        "Custom Field 3",
        "Custom Field 4",
        "Custom Field 5",
        "Custom Field 6",
        "Custom Field 7",
        "Custom Field 8",
        "FRU File ID",
        "Manufacturer",
        "Name",
        "Part Number",
        "Serial Number",
        "fault",
        "fru_type",
        "is_fru",
        "present",
        "version",
        ],
    "BMC": [
        "fault",
        "fru_type",
        "is_fru",
        "manufacturer",
        "present",
        "version",
        ],
    "MAIN_PLANAR": [
        "Custom Field 1",
        "Custom Field 2",
        "Custom Field 3",
        "Custom Field 4",
        "Custom Field 5",
        "Custom Field 6",
        "Custom Field 7",
        "Custom Field 8",
        "Part Number",
        "Serial Number",
        "Type",
        "fault",
        "fru_type",
        "is_fru",
        "present",
        "version",
        ],
    "SYSTEM": [
        "Custom Field 1",
        "Custom Field 2",
        "Custom Field 3",
        "Custom Field 4",
        "Custom Field 5",
        "Custom Field 6",
        "Custom Field 7",
        "Custom Field 8",
        "FRU File ID",
        "Manufacturer",
        "Model Number",
        "Name",
        "Serial Number",
        "Version",
        "fault",
        "fru_type",
        "is_fru",
        "present",
        "version",
        ],
    "CORE": [
        "fault",
        "fru_type",
        "is_fru",
        "present",
        "version",
        ],
}
