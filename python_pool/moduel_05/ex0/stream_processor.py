from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if type(data) is not list:
            return False

        for element in data:
            if type(element) is not int:
                return False

        return True

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return "Invalid numeric data"
            else:
                sum_ = 0
                avg = 0.0
                count = 0
                for item in data:
                    sum_ += item
                    count += 1

                avg = sum_ / count

                result = f"Processed {count} numeric values, sum={sum_}, avg={avg}"

                return result
        except ValueError as e:
            print(e)
            return (str(e))

    def format_output(self, result):
        return super().format_output(result)





class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        pass

    def process(self, data: Any) -> str:
        pass


    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"

def numeric_process(num: NumericProcessor, lst: list) -> str:
    print("Initializing Numeric Processor...")

    print(f"Processing data: {lst}")
    print("Validation:", end=" ")
    if num.validate(lst):
        print("Numeric data verified")
    else:
        print("Invalid numeric data")

    print(f"Output: {num.process(lst)}")
    return num.process(lst)

def text_processor(txt: TextProcessor, string: str) -> str:
    print("Initializing Text Processor...")
    pass

def log_processor(log: LogProcessor, string: str) -> str:
    print("Initializing Log Processor...")
    pass


def polymorphic_processing_demo(str1: str, str2: str, str3: str) -> None:
    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")

    print(f"Result 1: {str1}")
    print(f"Result 2: {str2}")
    print(f"Result 3: {str3}")

    print("\nFoundation systems online. Nexus ready for advanced streams.\n")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    lst = [1, 2, 3, 4, 5]
    text_to_process = "hello Nexus World"
    log_text = "Error: Connection timeout"

    num = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()

    result_1 = numeric_process(num, lst)
    result_2 = text_processor(txt, text_to_process)
    result_3 = log_processor(log, log_text)


    polymorphic_processing_demo(result_1, result_2, result_3)





if __name__ == "__main__":
    main()