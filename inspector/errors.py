class USIError(Exception):
    """Base class for all usi exceptions."""
    pass

class ServiceNotFound(USIError):
    """Raised when a specified service does not exist."""
    pass

class SystemctlError(USIError):
    """"Raised when systemctl command fails."""
    pass