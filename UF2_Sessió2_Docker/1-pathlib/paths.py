from    pathlib import Path
import  json

'''Example of getting the base dir.'''

# Main
# ----------------------------------------------------
def main() -> None:

    # 1. Get base dir
    main_file:  Path = Path(__file__)
    base_dir:   Path = main_file.resolve().parent

    # 2. Get data
    json_file:  Path        = base_dir/'db'/'papers.json'
    json_text:  str         = json_file.read_text()
    paper_list: list[dict]  = json.loads(json_text)

    # 3. Pretty-print paper titles
    title_list:     list[str] = [ paper['title'] for paper in paper_list ]
    title_list_str: str       = '\n'.join(title_list)
    print(title_list_str)

# ----------------------------------------------------
if __name__ == '__main__':
    main()
# ----------------------------------------------------
