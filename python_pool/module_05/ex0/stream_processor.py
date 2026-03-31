from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    Abstract base class defining the interface for all data processors.
    """

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the given data and return a result string.
        Args:
            data: Input data to process.
        Returns:
            A string containing the processing result.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate if the provided data is suitable for processing.
        Args:
            data: Input data to validate.
        Returns:
            True if the data is valid, False otherwise.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Format the result string for display.

        Args:
            result: Processing result.

        Returns:
            A formatted output string.
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Processor responsible for handling numeric list data.
    Calculates count, sum, and average of numbers.
    """

    def validate(self, data: Any) -> bool:
        """
        Check whether the input is a list of integers.
        Args:
            data: Data to validate.
        Returns:
            True if data is a list of integers, otherwise False.
        """
        if type(data) is not list:
            return False

        for element in data:
            if type(element) is not int:
                return False

        return True

    def process(self, data: Any) -> str:
        """
        Process numeric data by computing count, sum, and average.
        Args:
            data: List of numeric values.
        Returns:
            A formatted string describing the numeric analysis.
        """
        try:
            if not self.validate(data):
                return "Invalid numeric data"
            else:
                sum_ = 0
                avg = 0.0
                i = 0
                for item in data:
                    sum_ += item
                    i += 1

                avg = sum_ / i

                res = f"Processed {i} numeric values, sum={sum_}, avg={avg}"

                return res
        except Exception as e:
            print(e)
            return (str(e))


class TextProcessor(DataProcessor):
    """
    Processor responsible for analyzing text data.
    Counts the number of characters and words in a string.
    """

    def validate(self, data: Any) -> bool:
        """
        Validate that the input is a string.

        Args:
            data: Data to validate.

        Returns:
            True if data is a string, otherwise False.
        """
        if type(data) is str:
            return True

        return False

    def process(self, data: Any) -> str:
        """
        Analyze text data to determine character and word counts.

        Args:
            data: Input string.

        Returns:
            A formatted string describing the text statistics.
        """
        try:

            if not self.validate(data):
                return "Invalid Text Data."

            else:
                w_count = 0
                ch_count = 0
                for _ in data:
                    ch_count += 1

                for _ in data.split():
                    w_count += 1

                res = f"Processed text: {ch_count} characters, {w_count} words"

                return res

        except ValueError as e:
            print(e)
            return (str(e))


class LogProcessor(DataProcessor):
    """
    Processor for structured log entries.

    Expected log format:
        LEVEL: message
    """

    def validate(self, data: Any) -> bool:
        """
        Validate that the input follows the expected log format.

        Args:
            data: Log entry to validate.

        Returns:
            True if the log entry is valid, otherwise False.
        """

        valid_log_list: List[str] = [
            "INFO",
            "WARNING",
            "ERROR",
            "DEBUG"
        ]

        if type(data) is not str:
            return False

        if ":" not in data:
            return False

        level, message = data.split(":", 1)

        if level not in valid_log_list:
            return False

        message.strip()
        if not message:
            return False

        return True

    def process(self, data: Any) -> str:
        """
        Interpret a log entry and generate a formatted alert message.

        Args:
            data: Log entry string.

        Returns:
            A formatted message describing the detected log level.
        """
        logs: Dict[str, str] = {
            "INFO": "INFO",
            "WARNING": "WARN",
            "ERROR": "ALERT",
            "DEBUG": "DEBUG"
        }

        try:
            if not self.validate(data):
                return "Invalid log data"

            else:
                lvl, msg = data.split(":", 1)
                msg = msg.strip()

                for log_level, log_type in logs.items():
                    if lvl == log_level:
                        res = f"[{log_type}] {log_level} level detected: {msg}"
                        break

                return res

        except ValueError as e:
            print(e)
            return (str(e))


def numeric_process(num: NumericProcessor, data_to_process: list[int]) -> str:
    """
    Demonstrate numeric data processing.

    Args:
        num: NumericProcessor instance.
        data_to_process: List of integers to process.

    Returns:
        Processing result string.
    """

    print("Initializing Numeric Processor...")

    print(f"Processing data: {data_to_process}")
    print("Validation:", end=" ")
    if num.validate(data_to_process):
        print("Numeric data verified")
    else:
        print("Invalid numeric data")

    print(num.format_output(num.process(data_to_process)))

    return num.process(data_to_process)


def text_processor(txt: TextProcessor, data_to_process: str) -> str:
    """
    Demonstrate text data processing.
    """
    print("Initializing Text Processor...")

    print(f"Processing data: \"{data_to_process}\"")
    print("Validation:", end=" ")
    if txt.validate(data_to_process):
        print("Text data verified")
    else:
        print("Invalid text data")

    print(txt.format_output(txt.process(data_to_process)))

    return txt.process(data_to_process)


def log_processor(log: LogProcessor, data_to_process: str) -> Union[str]:
    """
    Demonstrate log data processing.
    """
    print("Initializing Log Processor...")

    print(f"Processing data: \"{data_to_process}\"")
    print("Validation:", end=" ")
    if log.validate(data_to_process):
        print("Log entry verified")
    else:
        print("Invalid log data")

    print(log.format_output(log.process(data_to_process)))

    return log.process(data_to_process)


def polymorphic_processing_demo(processors_list: list[str]) -> Optional[None]:
    """
    Demonstrate polymorphic behavior using multiple processors.

    Args:
        results: List of processing results.
    """
    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")

    i = 1
    for processor in processors_list:
        print(f"Result {i}: {processor}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


def main() -> None:
    """
    Entry point of the Code Nexus demonstration program.
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    lst = [1, 2, 3, 4, 5]
    text_to_process = "Hello Nexus World"
    log_text = "ERROR: Connection timeout"

    num_1 = NumericProcessor()
    txt_1 = TextProcessor()
    log_1 = LogProcessor()

    numeric_process(num_1, lst)
    print()
    text_processor(txt_1, text_to_process)
    print()
    log_processor(log_1, log_text)

    num_2 = NumericProcessor()
    txt_2 = TextProcessor()
    log_2 = LogProcessor()

    processors_list = [
        num_2.process([1, 2, 3]),
        txt_2.process("Hello World!"),
        log_2.process("INFO: System ready")
    ]

    polymorphic_processing_demo(processors_list)


if __name__ == "__main__":
    main()
