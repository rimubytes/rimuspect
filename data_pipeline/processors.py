class DataProcessor:
    def process(self, raw_data):
        # Add timestamp and any other necessary transformations
        processed_data = raw_data.copy()
        processed_data['timestamp'] = time.time()
        return processed_data