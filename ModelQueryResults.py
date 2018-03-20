class ModelQueryResults:
    units_before_target = None
    target = None
    units_after_target = None
    start_of_captured_units = None
    end_of_captured_units = None

    def __init__(self, units_before_target, target, units_after_target, start_of_captured_units, end_of_captured_units):
        self.units_before_target = units_before_target
        self.units_after_target = units_after_target
        self.target = target
        self.start_of_captured_units = start_of_captured_units
        self.end_of_captured_units = end_of_captured_units
