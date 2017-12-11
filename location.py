class Location:
    """
    Intersection between north/south and east/south roads.
    """
    def __init__(self, row, column):
        """Initialize a location.

        @type self: Location
        @type row: int
        @type column: int
        @rtype: None
        """
        # TODO
        self._row, self._column = row, column

    def __str__(self):
        """Return a string representation.

        @rtype: str

        >>> a = Location(1, 2)
        >>> print(a)
        (1,2)
        """
        # TODO
        return '({},{})'.format(self._row, self._column)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @rtype: bool
        >>> a = Location(1, 3)
        >>> b = Location(1, 3)
        >>> a == b
        True
        """
        # TODO
        return type(self) == type(other) and self._row == other._row and \
               self._column == other._column

    def _get_row(self):
        """
        :return: return row value of Location self
        :rtype: int

        >>> a = Location(1, 3)
        >>> a._get_row()
        1
        """
        return self._row

    def _set_row(self, row):
        """

        :param row: the road going east/west.
        :type row: int\ float
        :return: set row of Location self
        :rtype: None
        """
        if self._row == type(float) or self._row < 0:
            raise Exception('street number has to be a positive int!')
        else:
            self._row = row

    horizontal = property(_get_row, _set_row)

    def _get_column(self):
        """

        :return: return the column value of Location self
        :rtype: int

        >>> a = Location(1,3)
        >>> a._get_column()
        3
        """
        return self._column

    def _set_column(self, column):
        """

        :param column: the road going north/south
        :type column: int/ float
        :return: set column of Location self
        :rtype: None
        """
        if self._column == type(float) or self._column < 0:
            raise Exception('street number has to be a positive int')
        else:
            self._column = column

    vertical = property(_get_column, _set_column)


def manhattan_distance(origin, destination):
    """Return the Manhattan distance between the origin and the destination.

    @type origin: Location
    @type destination: Location
    @rtype: int
    >>> a = Location(1,3)
    >>> b = Location(2,4)
    >>> manhattan_distance(a,b)
    2
    """
    # TODO
    return abs(origin._row - destination._row) + abs(origin._column - \
                                                     destination._column)


def deserialize_location(location_str):
    """Deserialize a location.

    @type location_str: str
        A location in the format 'row,col'
    @rtype: Location

    >>> a = '(1,2)'
    >>> c=deserialize_location(a)
    >>> a = '(134,12)'
    >>> d=deserialize_location(a)
    >>> manhattan_distance(d,c)
    143

    """
    # TODO

    index = location_str.find(',')
    row = location_str[1:index]
    column = location_str[index+1:-1]
    return Location(int(row), int(column))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

