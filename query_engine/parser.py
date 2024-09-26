class QueryParser:
    def parse(self, query_string):
        # Simple parser for demonstration
        parts = query_string.split()
        return {
            'metric': parts[0],
            'start_time': float(parts[1]),
            'end_time': float(parts[2])
        }
