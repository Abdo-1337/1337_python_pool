from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    """
    Abstract base class representing a generic data stream.

    This class defines the common interface for all stream types
    in the system. Subclasses must implement the `process_batch`
    method to process incoming data.
    """

    def __init__(
            self,
            stream_id: str,
            stream_type: str,
            data_type: str
            ) -> None:
        """
        Initialize a data stream.

        Args:
            stream_id: Unique identifier of the stream.
            stream_type: Category of the stream (e.g., Environmental Data).
            data_type: Specific data handled by the stream.
        """
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.data_type = data_type
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of data.

        Args:
            data_batch: List containing the batch of data elements.

        Returns:
            A string describing the result of the processing.
        """
        pass

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
            ) -> List[Any]:
        """
        Filter data elements based on a criteria.

        Args:
            data_batch: List of data elements.
            criteria: Optional string used to filter elements.

        Returns:
            A list containing only the elements matching the criteria.
        """
        if criteria is None:
            return data_batch
        return [element for element in data_batch if criteria in str(element)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """
        Return statistics about the stream.

        Returns:
            A dictionary containing stream metadata and processing stats.
        """
        return {
            "ID": self.stream_id,
            "Type": self.stream_type,
            "Items": self.processed_count,
            "Data_type": self.data_type
        }


class SensorStream(DataStream):
    """
    Stream implementation for environmental sensor data.

    This class processes batches of sensor readings and computes
    statistics such as the average temperature.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize a sensor data stream.

        Args:
            stream_id: Unique identifier for the stream.
        """
        super().__init__(stream_id, "Environmental Data", "Sensor")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of sensor readings.

        Args:
            data_batch: List of sensor readings in the format "key:value".

        Returns:
            A formatted string summarizing the analysis results.
        """
        try:
            total_tmp = 0.0
            avg_tmp = 0.0
            for _ in data_batch:
                self.processed_count += 1

            count = 0
            for element in data_batch:
                key, value = element.split(":")
                if key.strip() == "temp":
                    total_tmp += float(value.strip())
                    count += 1

            if count > 0:
                avg_tmp = total_tmp / count

            p_count = self.processed_count
            res = (
                f"{self.data_type} analysis: {p_count} readings processed, "
                f"avg temp: {avg_tmp}°C"
            )

            return res

        except ValueError as e:
            print(e)
            return (str(e))

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
            ) -> List[Any]:
        """
        Filter sensor readings to detect critical temperature alerts.

        Args:
            data_batch: List of sensor readings.
            criteria: Optional filtering criteria (unused here).

        Returns:
            A list containing temperature values considered critical.
        """
        try:
            filtered_list: List[Any] = []

            for element in data_batch:
                if element.startswith("temp"):
                    value = float(element.split(":")[1])
                    if value >= 100:
                        filtered_list.append(int(value))

            print(f"{len(filtered_list)} critical sensor alerts", end=",")

            return filtered_list
        except ValueError as e:
            print(e)
            return []


class TransactionStream(DataStream):
    """
    Stream implementation for financial transaction data.

    This class processes batches of transactions and calculates
    the net flow of units between buy and sell operations.
    """

    def __init__(self, stream_id: str) -> None:
        """
        Initialize a transaction data stream.

        Args:
            stream_id: Unique identifier for the stream.
        """
        super().__init__(stream_id, "Financial Data", "Transaction")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of transaction operations.

        Args:
            data_batch: List of transaction entries "operation:value".

        Returns:
            A formatted string describing the transaction analysis.
        """
        try:
            units = 0
            buy_units = 0
            sell_units = 0

            for _ in data_batch:
                self.processed_count += 1

            for element in data_batch:
                key, value = element.split(":")
                if key.strip() == "buy":
                    buy_units += int(value.strip())
                elif key.strip() == "sell":
                    sell_units += int(value.strip())

            units = buy_units - sell_units

            if units >= 0:
                op = "+"
            else:
                op = "-"
                units = -units

            p_count = self.processed_count
            res = (
                f"{self.data_type} analysis: {p_count} operations, "
                f"net flow: {op}{units} units"
                )

            return res

        except ValueError as e:
            print(e)
            return (str(e))

    def filter_data(
            self,
            data_batch: List[Any],
            criteria: Optional[str] = None
            ) -> List[Any]:
        """
        Filter transactions to detect large operations.

        Args:
            data_batch: List of transaction records.
            criteria: Optional filtering criteria (unused here).

        Returns:
            A list of transaction values considered large.
        """
        try:
            filtered_list: List[int] = []
            for element in data_batch:
                _, value = element.split(":")
                if int(value) >= 200:
                    filtered_list.append(int(value))

            print(f" {len(filtered_list)} large transaction", end="")

            return filtered_list
        except ValueError as e:
            print(e)
            return []


class EventStream(DataStream):
    """
    Stream implementation for system event data.

    This class processes batches of events and detects
    the number of error occurrences.
    """
    def __init__(self, stream_id: str) -> None:
        """
        Initialize an event stream.

        Args:
            stream_id: Unique identifier for the stream.
        """
        super().__init__(stream_id, "System Events", "Event")

    def process_batch(self, data_batch: List[Any]) -> str:
        """
        Process a batch of system events.

        Args:
            data_batch: List of event strings.

        Returns:
            A formatted string summarizing the event analysis.
        """
        try:
            error_count = 0

            for _ in data_batch:
                self.processed_count += 1

            for element in data_batch:
                if element.strip() == "error":
                    error_count += 1

            if error_count <= 1:
                s_p = ""
            else:
                s_p = "s"

            p_count = self.processed_count
            res = (
                f"{self.data_type} analysis: {p_count} events, "
                f"{error_count} error{s_p} detected"
                )

            return res
        except ValueError as e:
            print(e)
            return (str(e))


class StreamProcessor:
    """
    Manager responsible for orchestrating multiple DataStream objects.

    The processor executes batch processing, filtering operations,
    and collects statistics from all registered streams.
    """

    def __init__(self) -> None:
        """
        Initialize the stream processor.

        Creates an empty list of streams and initializes
        the batch counter.
        """
        self.streams: List[DataStream] = []
        self.batch: int = 1

    def add_stream(self, stream: DataStream) -> None:
        """
        Register a new data stream.

        Args:
            stream: A DataStream object to be managed by the processor.
        """
        self.streams.append(stream)

    def process_streams(self, data_batches: List[Any]) -> None:
        """
        Process batches of data through each registered stream.

        Args:
            data_batches: A list of batches where each batch corresponds
                to a stream in the processor.
        """
        for i in range(len(self.streams)):
            stream = self.streams[i]
            batch = data_batches[i]

            res = stream.process_batch(batch).split(",")[0]
            data_type = res.split(":")[0].removesuffix(" analysis")
            new_res = res.split(":")[1].removesuffix(" analysis")

            if "processed" not in res:
                print(f"- {data_type} data:{new_res} processed")
            else:
                print(f"- {data_type} data:{new_res}")

        self.batch += 1

    def filter_streams(
            self,
            data_batches: List[List[Any]],
            criteria: Optional[str]
            ) -> None:
        """
        Filter data in each stream using a specified criteria.

        Args:
            data_batches: List of batches corresponding to each stream.
            criteria: Optional filtering criteria applied to the stream data.
        """
        print("Stream filtering active: High-priority data only")

        print("Filtered results: ", end="")

        for i in range(len(self.streams)):
            stream = self.streams[i]
            batch = data_batches[i]

            stream.filter_data(batch)


def ft_sensor_stream(stream_id: str, data_batch: List[Any]) -> None:
    """
    Demonstrate the behavior of the SensorStream class.

    Args:
        stream_id: Unique identifier of the sensor stream.
        data_batch: List of sensor readings to process.
    """

    print("Initializing Sensor Stream...")
    stream = SensorStream(stream_id)

    res = stream.process_batch(data_batch)
    stats = stream.get_stats()
    id = stats["ID"]
    type = stats["Type"]

    print(f"Stream ID: {id}, Type: {type}")
    print(f"Processing sensor batch: {data_batch}")
    print(res)


def ft_transaction_stream(stream_id: str, data_batch: List[Any]) -> None:
    """
    Demonstrate the behavior of the TransactionStream class.

    Args:
        stream_id: Unique identifier of the transaction stream.
        data_batch: List of transaction records to process.
    """
    print("Initializing Transaction Stream...")
    stream = TransactionStream(stream_id)

    res = stream.process_batch(data_batch)
    stats = stream.get_stats()
    id = stats["ID"]
    type = stats["Type"]

    print(f"Stream ID: {id}, Type: {type}")
    print(f"Processing transaction batch: {data_batch}")
    print(res)


def ft_event_stream(stream_id: str, data_batch: List[Any]) -> None:
    """
    Demonstrate the behavior of the EventStream class.

    Args:
        stream_id: Unique identifier of the event stream.
        data_batch: List of system events to process.
    """
    print("Initializing Event Stream...")
    stream = EventStream(stream_id)

    res = stream.process_batch(data_batch)
    stats = stream.get_stats()
    id = stats["ID"]
    type = stats["Type"]

    print(f"Stream ID: {id}, Type: {type}")
    print(f"Processing event batch: {data_batch}")
    print(res)


def ft_polymorphic_stream() -> None:
    """
    Demonstrate polymorphic processing using StreamProcessor.

    This function initializes different stream types, processes
    their data batches through a unified interface, and applies
    filtering across all streams.
    """
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    data_batches = [
        ["temp:100", "temp:121"],
        ["buy:100", "sell:250", "buy:75", "sell:10"],
        ["login", "error", "logout"]
    ]

    process = StreamProcessor()

    process.add_stream(sensor)
    process.add_stream(transaction)
    process.add_stream(event)

    print(f"Batch {process.batch} Results:")
    process.process_streams(data_batches)
    print()
    process.filter_streams(data_batches, None)

    print()
    print("\nAll streams processed successfully. Nexus throughput optimal.")


def main() -> None:
    """
    Entry point of the Code Nexus polymorphic stream system.

    Demonstrates individual stream processing and the unified
    polymorphic stream processing using StreamProcessor.
    """

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    s1_id = "SENSOR_001"
    s1_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    s2_id = "TRANS_001"
    s2_data = ["buy:100", "sell:150", "buy:75"]
    s3_id = "EVENT_001"
    s3_data = ["login", "error", "logout"]

    ft_sensor_stream(s1_id, s1_data)
    print()
    ft_transaction_stream(s2_id, s2_data)
    print()
    ft_event_stream(s3_id, s3_data)
    print()
    ft_polymorphic_stream()


if __name__ == "__main__":
    main()
