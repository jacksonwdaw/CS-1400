import sys


def sort_files(book_text_name):
    books = {}
    line_sum = {"longest":0,
           "longest line":"",
           "longest line num":0,
            "shortest": 1000,
            "shortest line": "",
            "shortest line num": 0,
            "avg":0
        }
    summaries = {}
    with open(book_text_name, 'r', encoding= "utf8") as lib:
        library = lib.readlines()
        for line in library:
            line = line[:-1]
            split_line = line.split("|")
            split_line[1] = int(split_line[1])
            if split_line[2] not in summaries:
                summaries[split_line[2]] = line_sum.copy()
                books[split_line[2]] = []
            if len(split_line[0]) >= summaries[split_line[2]]["longest"]:
                if (summaries[split_line[2]]["longest line num"]) < split_line[1] or len(split_line[0]) > summaries[split_line[2]]["longest"]:
                    summaries[split_line[2]]["longest"] = len(split_line[0])
                    summaries[split_line[2]]["longest line"] = split_line[0]
                    summaries[split_line[2]]["longest line num"] = split_line[1]
            if len(split_line[0]) <= summaries[split_line[2]]["shortest"]:
                if (summaries[split_line[2]]["shortest line num"]) > split_line[1] or len(split_line[0]) < summaries[split_line[2]]["shortest"]:
                    summaries[split_line[2]]["shortest"] = len(split_line[0])
                    summaries[split_line[2]]["shortest line"] = split_line[0]
                    summaries[split_line[2]]["shortest line num"] = split_line[1]
            summaries[split_line[2]]["avg"] += len(split_line[0])
            books[split_line[2]].append(split_line)
        for key in summaries.keys():
            summaries[key]["avg"] = summaries[key]["avg"]/len(books[key])
            summaries[key]["avg"] = int(round(summaries[key]["avg"],0))
        for key in books.keys():
            books[key].sort(key = lambda x: int(x[1]))
        return books, summaries

def move_text(book_text_name):

    books, summaries = sort_files(book_text_name)
    with  open('novel_text.txt', 'w', encoding= "utf8") as novel:
        book_keys = list(books.keys())
        book_keys.sort()
        temp_book_keys = [""]
        for book_key in book_keys:
            novel.write(f"{book_key}\n")
            for line in books[book_key]:
                novel.write(f"{line[0]}\n")
            if len(temp_book_keys) < len(book_keys):
                temp_book_keys.append(book_key)
                novel.write("-----\n")
    with open('novel_summary.txt', 'w', encoding= "utf8") as novel_summary:
        for summary_key in book_keys:
            novel_summary.write(f"{summary_key}\n")
            novel_summary.write(f"Longest line ({summaries[summary_key]['longest line num']}): {summaries[summary_key]['longest line']}\n")
            novel_summary.write(f"Shortest line ({summaries[summary_key]['shortest line num']}): {summaries[summary_key]['shortest line']}\n")
            novel_summary.write(f"Average length: {summaries[summary_key]['avg']}\n")
            novel_summary.write("\n")

def main():
    if len(sys.argv) > 1:
        move_text(sys.argv[1])
    else:
        move_text('book_data.txt')

if __name__ == "__main__":
    main()


