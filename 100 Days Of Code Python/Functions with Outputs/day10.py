# Function with output
def format_name(f_name, l_name):
    """Takes the first and last name and format it to title case version."""
    if f_name == "" or l_name == "":
        return "No input provided or first name or last name!"
    title_f_name = f_name.title()
    title_l_name = l_name.title()
    # return ends the function
    return f"{title_f_name} {title_l_name}"
    # Anything after return does not get executated
    print("Not gonna happen!")

input_f_name = input("What's your first name: ")
input_l_name = input("What's your last name: ")
formatted_string = format_name(input_f_name, input_l_name)
print(formatted_string)