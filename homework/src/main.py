from homework.src._internals.CountWordsMixIn import CountWordsMixIn
from homework.src._internals.ParseArgsMixin import ParseArgsMixin
from homework.src._internals.PreprocessLinesMixin import PreprocessLinesMixin
from homework.src._internals.ReadAllLinesMixin import ReadAllLinesMixin
from homework.src._internals.SplitIntoWordsMixIn import SplitIntoWordsMixIn
from homework.src._internals.WriteWordCountMixIn import WriteWordCountMixIn


class WordCountApp(
    ParseArgsMixin,
    ReadAllLinesMixin,
    PreprocessLinesMixin,
    SplitIntoWordsMixIn,
    CountWordsMixIn,
    WriteWordCountMixIn,
):
    def __init__(self):
        self.input_folder = None
        self.output_folder = None
        self.lines = None
        self.preprocessed_lines = None
        self.lines = None
        self.word = None

    def run(self):

        self.parse_args()
        self.read_all_lines()
        self.preprocess_lines()
        self.split_into_words()
        self.count_words()
        self.write_word_counts()


if __name__ == "__main__":
    WordCountApp().run()
