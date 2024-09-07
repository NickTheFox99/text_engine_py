from command import Command

class TextParser:
    @staticmethod
    def parse_cmd(x: str, dropped_actions: list[str], dropped_targets: list[str]) -> Command:
        split_str = x.split(",")
        split_action = split_str[0].split()
        split_target = split_str[1].split()
        action = split_action.copy()
        target = split_target.copy()
        for word in split_action:
            if word.lower() in dropped_actions:
                action.remove(word)
        for word in split_target:
            if word.lower() in dropped_targets:
                target.remove(word)
        return Command(" ".join(action), " ".join(target))
    @staticmethod
    def filter_words(x: str, dropped_words: list[str]) -> list[str]:
        split_str = x.split()
        result = split_str.copy()
        for word in split_str:
            if word.lower() in dropped_words:
                result.remove(word)
        return result

if __name__ == "__main__":
    print(TextParser.parse_cmd(input(" > "), ["a","b"], ["c","d"]).full())