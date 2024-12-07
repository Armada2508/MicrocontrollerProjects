from machine import SPI, Pin


class MCP3008:
    """https://ww1.microchip.com/downloads/aemDocuments/documents/MSLD/ProductDocuments/DataSheets/MCP3004-MCP3008-Data-Sheet-DS20001295.pdf"""

    def __init__(self, bus: int, clock_pin: int, mosi_pin: int, miso_pin: int, chip_select_pin: int) -> None:
        """Initalizes a SPI bus for communicating with an MCP3008 chip."""
        self._spi = SPI(bus, baudrate=3_600_000, sck=Pin(clock_pin), mosi=Pin(mosi_pin), miso=Pin(miso_pin))
        self._chip_select = Pin(chip_select_pin, mode=Pin.OUT, value=1)
        self._write_buf = bytearray(3)
        self._write_buf[0] = 0x01  # Start bit
        self._read_buf = bytearray(3)  # Must be the same length as the write buffer

    def read_adc(self, channel: int) -> float | None:
        """
        Returns the value between [0-1023] that the MCP3008 is currently reading off the provided channel.
        To convert this value to a voltage multiply by (V_REF / 1023).
        """
        if channel < 0 or channel > 7:
            return None
        self._chip_select.value(0)
        self._write_buf[1] = (1 << 7) | channel << 4  # single-ended
        self._spi.write_readinto(self._write_buf, self._read_buf)
        self._chip_select.value(1)
        return ((self._read_buf[1] & 0x03) << 8) | self._read_buf[2]  # Drop the first null bit and return 10 bits
