
class UnmetExpectation(AssertionError):

    """Error that is raised if an expectation is not met.

    This error class inherits :py:exc:`AssertionError` so it is compatible with
    unittest assertion errors and plain old python "assert" errors.

    To learn how to get the most out of your unmet expectations,
    see :doc:`usage/managing-expectations`
    """
    pass