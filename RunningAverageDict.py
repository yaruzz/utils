# adapted from from https://github.com/shariqfarooq123/AdaBins/blob/main/utils.py

class RunningAverage:
    def __init__(self):
        self.avg = 0
        self.total_count = 0

    def append(self, value, cnt=1):
        self.avg = (value + self.total_count * self.avg) / (self.total_count + cnt)
        self.total_count += cnt

    def get_value(self):
        return self.avg

class RunningAverageDict:
    def __init__(self):
        self._dict = None

    def update(self, new_dict, cnt=1):
        if self._dict is None:
            self._dict = dict()
            for key, value in new_dict.items():
                self._dict[key] = RunningAverage()

        for key, value in new_dict.items():
            self._dict[key].append(value,cnt)

    def get_value(self):
        return {key: value.get_value() for key, value in self._dict.items()}

