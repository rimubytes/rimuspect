import psutil

class Agent: 
    def __init__(self, config):
        self.config = config
    
    async def collect(self):
        metrics = {
            'cpu_percent': psutil.cpu_percent(),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent
        }
        return metrics