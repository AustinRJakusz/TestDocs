from datetime import datetime


class Information:
    """Base information class for all other information related classes.

    All classes for information will inherit this class. This class will only hold API specific information or any
    information that is redundant between multiple classes.

    ..Information

    Attributes
    ----------
    ob_id: str
        the unique id of the server gathered by the uuid module
    timestamp: datetime
        the timestamp of object creation (default datetime.now())
    """

    def __init__(self, object_id: str, timestamp: datetime = datetime.now()) -> None:
        """
        Parameters
        ----------
        object_id: str
            the unique id of the server gathered by the uuid module
        timestamp: datetime, optional
            the timestamp of object creation (default datetime.now())
        """

        self.ob_id = object_id
        self.timestamp = timestamp
        return
