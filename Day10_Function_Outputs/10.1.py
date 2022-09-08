# Functions with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it
  to return the title case version of the name."""
  # ^ Docstring inside a function ^
    if f_name == "" or l_name == "":
        return "No input"
    fmt_fname = f_name.title()
    fmt_lname = l_name.title()
    return f"{fmt_fname} {fmt_lname}"  # end of function, return this function
    print("This won't print b/c of return statement above")


format_name()  # Hover over () to view docstring

print(format_name(input("What is your first name? "),
      input("What is your last name? ")))
