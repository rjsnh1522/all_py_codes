from enum import Enum

class Codes(Enum):
    @classmethod
    def get_mappings(cls):
        return [k.value for k in list(cls)]

    def get_id(self):
        ss = self
        id = ss.value[0]
        return id
        
    def get_str(self):
        ss = self
        str_ = ss.value[1]
        return str_


class SlaForChoices(Codes):
    CLOUSER = (1, "Closure")
    FIRST_RESPONSE = (2, "First response")



print(SlaForChoices.CLOUSER.get_id())
print(SlaForChoices.FIRST_RESPONSE.get_id())

print(SlaForChoices.CLOUSER.get_str())
print(SlaForChoices.FIRST_RESPONSE.get_str())