class FindSyncBytes:
    def __init__(self):
        self.log_sync_bytes = bytearray([0x08,0x1D])
        self.start_sync_bytes = bytearray([0x08, 0x19])
        self.stop_sync_bytes = bytearray([0xA5,0xA5])
    def find_log_sync_start_index(self,packets):
        return bytearray(packets).find(self.log_sync_bytes)
    def find_sync_start_index(self,packets):
        return bytearray(packets).find(self.start_sync_bytes)
    def find_sync_stop_index(self,packets):
        return bytearray(packets).find(self.stop_sync_bytes)
    