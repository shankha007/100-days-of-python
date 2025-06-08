def format_name(f_name, l_name):
    formatted_f_name = str(f_name).title()
    formatted_l_name = str(l_name).title()

    formatted_full_name = formatted_f_name + " " + formatted_l_name

    return formatted_full_name

print(format_name("SHANKHA", "das"))
