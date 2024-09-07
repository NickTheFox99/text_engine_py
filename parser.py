from command import Command

class TextParser:
    @staticmethod
    def parse(x: str, dropped_actions: list[str], dropped_targets: list[str]) -> [Command, int]:
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
        return Command(" ".join(split_action), " ".join(split_target))

if __name__ == "__main__":
    print(TextParser.parse(input(" > "), ["a","b"], ["c","d"]).full())