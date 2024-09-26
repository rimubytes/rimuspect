class AlertRuleEngine:
    def __init__(self, config):
        self.rules = config['rules']

    async def check_alerts(self, db):
        for rule in self.rules:
            data = await db.query(rule['metric'], rule['time_range'][0], rule['time_range'][1])
            if self.evaluate_rule(rule, data):
                self.trigger_alert(rule)

    def evaluate_rule(self, rule, data):
        # Simple threshold check for demonstration
        return any(value > rule['threshold'] for _, value in data)

    def trigger_alert(self, rule):
        print(f"ALERT: {rule['metric']} exceeded threshold of {rule['threshold']}")
