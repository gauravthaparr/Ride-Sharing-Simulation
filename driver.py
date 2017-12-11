from location import Location, manhattan_distance
from rider import Rider
WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    @type id: str
        A unique identifier for the driver.
    @type location: Location
        The current location of the driver.
    @type is_idle: bool
        A property that is True if the driver is idle and False otherwise.
    """

    def __init__(self, identifier, location, speed, is_idle):
        """Initialize a Driver.

        @type self: Driver
        @type identifier: str
        @type location: Location
        @type speed: int
        @type is_idle: bool
        @rtype: None
        """
        # TODO
        self.identifier = identifier
        self.location = location
        self.speed = speed
        self.destination = None
        self.is_idle = is_idle

    def __str__(self):
        """Return a string representation.

        @type self: Driver
        @rtype: str

        >>> a = Driver('Ben', Location(1,2), 15, True)
        >>> print(a)
        Driver name: Ben
        Driver location: (1,2)
        Driver speed: 15
        Is Driver idle: True
        Driver destination: None
        """
        # TODO
        return 'Driver name: {}\nDriver location: {}\nDriver speed: {}\nIs ' \
               'Driver idle: {}\nDriver destination: {}'.\
            format(self.identifier, self.location, self.speed,self.is_idle,
                   self.destination)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @type self: Driver
        @rtype: bool

        >>> a = Driver('Ben', Location(1,2), 15, False)
        >>> b = Driver('Ben', Location(1,2), 15, True)
        >>> a == b
        False
        """
        # TODO
        return type(self) == type(other) and self.identifier == \
                                             other.identifier\
        and self.location == other.location and self.speed == other.speed and\
        self.destination == other.destination and self.is_idle == other.is_idle

    def get_travel_time(self, destination):
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        @type self: Driver
        @type destination: Location
        @rtype: int

        >>> a = Driver('Ben', Location(1,2), 15, True)
        >>> a.get_travel_time(Location(16,17))
         2
        """
        # TODO
        distance = manhattan_distance(self.location, destination)
        return round(distance/self.speed)


    def start_drive(self, location):
        """Start driving to the location and return the time the drive will take.

        @type self: Driver
        @type location: Location
        @rtype: int

        >>> a = Driver('Ben', Location(1,2), 15, True)
        >>> a.start_drive(Location(16,17))
        2
        >>> print(a)
        Driver name: Ben
        Driver location: (1,2)
        Driver speed: 15
        Is Driver idle: False
        Driver destination: (16,17)

        """
        # TODO
        if not self.is_idle:
            raise Exception('Driver is not idle!')

        self.destination = location
        self.is_idle = False
        return self.get_travel_time(location)

    def end_drive(self):
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        # TODO
        self.location = self.destination
        self.is_idle = True
        self.destination = None

    def start_ride(self, rider):
        """Start a ride and return the time the ride will take.

        @type self: Driver
        @type rider: Rider
        @rtype: int

        >>> a = Rider('Alex', Location(1,2), Location(16,17), WAITING, 15)
        >>> b = Driver('Ben', Location(1,2), 15, True)
        >>> b.start_ride(a)
        2
        """
        # TODO
        self.destination = rider.destination
        self.is_idle = False
        return self.get_travel_time(self.destination)

    def end_ride(self):
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        # TODO
        self.location = self.destination
        self.is_idle = True
        self.destination = None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
