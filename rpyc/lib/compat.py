"""
compatibility module for various versions of python (2.4/3+/jython)
and various platforms (posix/windows)
"""
try:
    from struct import Struct
except ImportError:
    import struct
    class Struct(object):
        __slots__ = ["format", "size"]
        def __init__(self, format):
            self.format = format
            self.size = struct.calcsize(format)
        def pack(self, *args):
            return struct.pack(self.format, *args)
        def unpack(self, data):
            return struct.unpack(self.format, data)

try:
    all = all
except NameError:
    def all(seq):
        for elem in seq:
            if not elem:
                return False
        return True

try:
    callable = callable
except NameError:
    def callable(obj):
        return hasattr(obj, "__call__")

try:
    import select as select_module
except ImportError:
    select_module = None
    def select(*args):
        raise ImportError("select not supported on this platform")
else:
    # jython
    if hasattr(select_module, 'cpython_compatible_select'):
        from select import cpython_compatible_select as select
    else:
        from select import select


if hasattr(select_module, "poll"):
    class PollingPoll(object):
        def __init__(self):
            self._poll = select_module.poll()
        def register(self, fd, mode):
            flags = 0
            if "r" in mode:
                flags |= select_module.POLLIN
            if "w" in mode:
                flags |= select_module.POLLOUT
            self._poll.register(fd, flags)
        modify = register
        def unregister(self, fd):
            self._poll.unregister(fd)
        def poll(self, timeout = None):
            events = self._poll.poll(timeout)
            processed = []
            for fd, evt in events:
                mask = ""
                if evt & (select_module.POLLIN | select_module.POLLPRI):
                    mask += "r"
                if evt & select_module.POLLOUT:
                    mask += "w"
                if evt & select_module.POLLERR:
                    mask += "e"
                if evt & select_module.POLLHUP:
                    mask += "h"
                if evt & select_module.POLLNVAL:
                    mask += "n"
                processed.append(fd)
            return processed
    
    poll = PollingPoll
else:
    class SelectingPoll(object):
        def __init__(self):
            self.rlist = set()
            self.wlist = set()
        def register(self, fd, mode):
            if "r" in mode:
                self.rlist.append(fd)
            if "w" in mode:
                self.wlist.append(fd)
        modify = register
        def unregister(self, fd):
            self.rlist.discard(fd)
            self.wlist.discard(fd)
        def poll(self, timeout = None):
            rl, wl, _ = select(self.rlist, self.wlist, (), timeout)
            return [(fd, "r") for fd in rl] + [(fd, "w") for fd in wl]
    
    poll = SelectingPoll


