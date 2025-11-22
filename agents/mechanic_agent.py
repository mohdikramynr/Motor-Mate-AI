class MechanicAgent:
    def __init__(self, tools=None):
        self.tools = tools or {}
        self.name = "mechanic-agent"
    def generate_steps(self, diagnosis, model):
        if "battery" in diagnosis.lower():
            steps = [
                {"step_id":1, "desc":"Check battery terminals and voltage", "expected_time_minutes":10},
                {"step_id":2, "desc":"Replace battery if voltage < 11.5V", "expected_time_minutes":20},
            ]
        else:
            steps = [{"step_id":1, "desc":"Inspect parts related to: " + diagnosis, "expected_time_minutes":20}]
        return {"steps": steps}
