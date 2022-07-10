from abc import ABC

from rasa.shared.core.slots import Slot


class BrightnessSlot(Slot, ABC):
    """
    The featurization defines how the value of this slot gets converted to a vector so
    Rasa Open Source machine learning model can deal with it.
    The slot has three possible “values”, which can be represented with a vector of length 2.
    (0,0)	not yet set
    (1,0)	between 1 and 6
    (0,1)	more than 6
    TODO concrete implementation. Currently copied from https://rasa.com/docs/rasa/domain/#custom-slot-types
    """

    def feature_dimensionality(self):
        return 2

    def as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            if self.value <= 6:
                r[0] = 1.0
            else:
                r[1] = 1.0
        return r


class ItemConfigSlot(Slot, ABC):
    """
    Should contain item configuration provided by other forms.
    TODO concrete implementation. Currently copied from https://rasa.com/docs/rasa/domain/#custom-slot-types
    """

    def feature_dimensionality(self):
        return 2

    def as_feature(self):
        r = [0.0] * self.feature_dimensionality()
        if self.value:
            if self.value <= 6:
                r[0] = 1.0
            else:
                r[1] = 1.0
        return r