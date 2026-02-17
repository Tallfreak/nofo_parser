import parse_nofo

def main():
  parsed_nofo_info = parse_nofo.parse('C:\\Users\\Collin\\Downloads\\FY2026-BARM-NOFA.pdf')
  print(parsed_nofo_info)
  return parsed_nofo_info
main()
