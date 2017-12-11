"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"

from location import Location


class Rider:
    """
    a Rider who requests rides
    """
    def __init__(self, id, origin, destination, status, patience):
        """
        :param id: username of the person
        :type id: str
        :param origin: Rider self's current location
/        :type origin: Location
        :param destination: Rider self's destination
        :type destination: Location
        :param status: Rider self's status. could be one of WAITING,
        CANCELLED or SATISFIED
        :type status: str
        :param patience: time Rider self will wait
        :type patience: int
        :return: create new rider self with a name, origin, destination and a
        status.
        :rtype: None
        """
        self.id = id
        self.origin = origin
        self.destination = destination
        self.status = status
        self.patience = patience

    def __eq__(self, other):
        """

        :return: return True iff Rider self and Rider other are equal
        :rtype: bool

         >>> a = Rider('Alex', Location(1,3), Location(2,4), WAITING, 15)
         >>> b = Rider('Alex', Location(1,3), Location(2,4), WAITING, 15)
         >>> a == b
         True
        """
        return type(self) == type(other) and self.id == other.id \
        and self.origin == other.origin and self.destination ==\
                                            other.destination and \
        self.status == other.status and self.patience == other.patience

    def __str__(self):
        """

        :return: return str representation of Rider self
        :rtype: str


        >>> a = Rider('Alex', Location(1,3), Location(2,4), WAITING, 15)
        >>> print(a)
        Rider ID: Alex
        Rider Origin:(1,3)
        Rider Destination:(2,4)
        Rider Status: waiting
        Rider Patience: 15
        """
        return 'Rider ID: {}\nRider Origin:{}\nRider Destination:{}\nRider Status: {}\nRider Patience: {}'\
            .format(self.id, self.origin, self.destination, self.status,
                    self.patience)


if __name__ == '__main__':
    import doctest
    doctest.testmod()








