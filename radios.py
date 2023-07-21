URL = "https://nypd.radio12.org/icecast/"

radios_by_borough = {
    "bk": [
        "ALT-nypd-bk-60-61",
        "ALT-nypd-bk-62-68",
        "ALT-nypd-bk-63-69",
        "ALT-nypd-bk-66-70",
        "ALT-nypd-bk-67-71",
        "ALT-nypd-bk-72-76-78",
        "ALT-nypd-bk-73-75",
        "ALT-nypd-bk-77-79",
        "ALT-nypd-bk-81-83",
        "ALT-nypd-bk-84-88",
        "ALT-nypd-bk-90-94",
    ],
    "mn": [
        "ALT-nypd-mn-1-5-7",
        "ALT-nypd-mn-6-9",
        "ALT-nypd-mn-10-13",
        "ALT-nypd-mn-17-mtx",
        "ALT-nypd-mn-19-23",
        "ALT-nypd-mn-20-24-cp",
        "ALT-nypd-mn-25-28-32",
        "ALT-nypd-mn-26-30",
        "ALT-nypd-mn-33-34",
    ],
    "qn": [
        "ALT-nypd-qn-100-101",
        "ALT-nypd-qn-102-106",
        "ALT-nypd-qn-103-107",
        "ALT-nypd-qn-104-112",
        "ALT-nypd-qn-105-113",
        "ALT-nypd-qn-108-114",
        "ALT-nypd-qn-109",
        "ALT-nypd-queens-110-115",
    ],
    "cw": ["nypd-cw-1", "nypd-cw-2", "ALT-nypd-cw-3", "ALT-nypd-cw-4", "ALT-nypd-sod"],
    "bx": [
        "ALT-nypd-bx-40-41",
        "ALT-nypd-bx-42-44",
        "ALT-nypd-bx-43-45",
        "ALT-nypd-bx-46-48",
        "ALT-nypd-bx-47-49",
        "ALT-nypd-bx-50-52",
    ],
}


def generate_stream_url(radio):
    # https://nypd.radio12.org/icecast/ALT-nypd-bk-67-71
    return URL + radio
