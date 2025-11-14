from datetime import datetime

class MasterTime:
    @staticmethod
    def ts_to_str(dateobj):
        date_format = "%d-%m-%Y %H:%M:%S"
        return dateobj.strftime(date_format)

    @staticmethod
    def ts_from_str(ts):
        date_format = "%Y-%m-%d %H:%M:%S"
        return datetime.strptime(ts, date_format)