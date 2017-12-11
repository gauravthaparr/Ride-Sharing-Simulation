from driver import Driver
from rider import Rider
from location import Location, manhattan_distance
from container import Container, PriorityQueue
WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"



class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    def __init__(self):
        """Initialize a Dispatcher.

        @type self: Dispatcher
        @rtype: None
        """
        # TODO
        self.drivers = []
        self.riders = []

    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str

        >>> a = Dispatcher()
        >>> rider = Rider('Alex', Location(1,3), Location(2,4), WAITING, 15)
        >>> a.riders.append(rider)
        >>> a.drivers.append(Driver('Ben', Location(1,2), 15, True))
        >>> print(a)
        Registered Drivers: ['Driver name: Ben\\nDriver location: (1,2)\\nDriver speed: 15\\nIs Driver idle: True\\nDriver destination: None']
        Riders waiting: ['Rider ID: Alex\\nRider Origin:(1,3)\\nRider Destination:(2,4)\\nRider Status: waiting\\nRider Patience: 15']
        """
        # TODO
        riders = []
        drivers = []
        for i in self.riders:
            a = str(i)
            riders.append(a)
        for i in self.drivers:
            a = str(i)
            drivers.append(a)

        return 'Registered Drivers: {}\nRiders waiting: {}'.format(drivers,
                                                                   riders)

    def request_driver(self, rider):
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None

        >>> a = Dispatcher()
        >>> rider = Rider('Alex', Location(1,3), Location(2,4), WAITING, 15)
        >>> a.request_rider(Driver('Ben', Location(1,2), 15, True))
        >>> a.request_driver(rider)
        Driver name: Ben
        Driver location: (1,2)
        Driver speed: 15
        Is Driver idle: True
        Driver destination: None
        """
        # TODO
        free = []
        times = []
        for i in self.drivers:
            if i.destination is None:
                free.append(i)
        if len(free) == 0:
            self.riders.append(rider)
        else:
            for i in free:
                time = i.get_travel_time(rider.origin)
                times.append(time)
            min_time = min(times)
            for i in self.drivers:
                time = i.get_travel_time(rider.origin)
                if min_time == time:
                    return print(i)

    def request_rider(self, driver):
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None

        >>> a = Dispatcher()
        >>> rider = Rider('Alex', Location(1,3), Location(2,4), WAITING, 15)
        >>> a.request_driver(rider)
        >>> a.request_rider(Driver('Ben', Location(1,2), 15, True))
        Rider ID: Alex
        Rider Origin:(1,3)
        Rider Destination:(2,4)
        Rider Status: waiting
        Rider Patience: 15
        """
        # TODO
        if driver not in self.drivers:
            self.drivers.append(driver)
        if len(self.riders) != 0:
            a = self.riders[0]
            self.riders.remove(a)
            return print(a)

    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None

        >>> a = Dispatcher()
        >>> rider = Rider('Alex', Location(1,3), Location(2,4), WAITING, 15)
        >>> a.request_driver(rider)
        >>> a.cancel_ride(rider)
        >>> print(a)
        Registered Drivers: []
        Riders waiting: []
        """
        # TODO

        if rider in self.riders:
            self.riders.remove(rider)
        else:
            raise Exception('Rider did not request a driver in first place!')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
