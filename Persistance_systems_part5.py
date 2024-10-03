"""The CropRatio object can be used to calculate what proportion of a farm's harvest is a specific crop.
The object's proportion method should return 0 for crops that were not added.
Example :.
crop_ratio =CropRatio().
crop_ratio.add("Wheat", 4).
crop_ratio.add("Wheat", 5).
crop_ratio.add("Rice", 1).
Running crop_ratio.proportion("Wheat") should return 0.9.
Running crop_ratio.proportion("Rice") should return 0.1.
Running crop_ratio.proportion("Corn") should return 0."""


class CropRatio:
    def __init__(self):
        self.crops = {}
        self.total_harvest = 0

    def add(self, crop_name, quantity):
        if crop_name in self.crops:
            self.crops[crop_name] += quantity
        else:
            self.crops[crop_name] = quantity
        self.total_harvest += quantity

    def proportion(self, crop_name):
        if crop_name in self.crops:
            return self.crops[crop_name] / self.total_harvest
        else:
            return 0


crop_ratio = CropRatio()
crop_ratio.add("Wheat", 4)
crop_ratio.add("Wheat", 5)
crop_ratio.add("Rice", 1)

crop_ratio.proportion("Wheat")  # should return 0.9
crop_ratio.proportion("Rice")  # should return 0.1
crop_ratio.proportion("Corn")  # should return 0.
