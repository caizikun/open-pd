import serial

class PowerMeter(object):
    def __init__(self, device='/dev/ttyUSB.openpd'):
        """ Open a power meter device """
        self.dev = serial.Serial(device, timeout=10)
        self.dev.flushInput()
        self.dev.write('v=0\n')
        self.dev.readline()
        self.dev.write('3\n')  # force to intermediate range
        self.dev.readline()
        self.dev.write('A\n')
        self.dev.readline()
        # Force a sample
        self.sample()

    def sample(self):
        """ Sample the power """
        self.dev.write('\n')
        while True:
            l = self.dev.readline()
            if l.startswith('#'):
                continue
            l = l.split()
            rng = int(l[0])
            power = float(l[1])
            return (rng, power)
