def celsius_converter(f_temp):
    celsius = (float(f_temp) - 32) * 5 / 9
    return round(celsius, 2)


def parse_and_clean(line):
    parts = [item.strip() for item in line.split("|")]

    if len(parts) != 5:
        return None

    if "N/A" in parts:
        return None

    if parts[4] != "ACTIVE":
        return None

    return parts