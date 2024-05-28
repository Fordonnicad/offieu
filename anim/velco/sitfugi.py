from colorama import Fore, Back, Style

def cprint(text, color):
  """Prints text in color.

  Args:
    text: The text to print.
    color: The color to print the text in.
  """

  if color == 'red':
    print(Fore.RED + text + Fore.RESET)
  elif color == 'green':
    print(Fore.GREEN + text + Fore.RESET)
  elif color == 'blue':
    print(Fore.BLUE + text + Fore.RESET)
  elif color == 'yellow':
    print(Fore.YELLOW + text + Fore.RESET)
  elif color == 'magenta':
    print(Fore.MAGENTA + text + Fore.RESET)
  elif color == 'cyan':
    print(Fore.CYAN + text + Fore.RESET)
  elif color == 'white':
    print(Fore.WHITE + text + Fore.RESET)
  elif color == 'black':
    print(Fore.BLACK + text + Fore.RESET)

cprint('account 2 added', 'green')
